#!/usr/bin/env python3
"""Scrape NVIDIA Research publications page (raw HTML via curl) and import papers.

Fetches HTML pages with curl, parses Drupal views-rows, and creates shared-layer
paper records using the same pipeline as import_nvidia_papers.py.

Usage:
  python scrape_nvidia_papers.py --year 2025           # single year
  python scrape_nvidia_papers.py --year 2025 --page 1  # single page
  python scrape_nvidia_papers.py --years 2020-2025     # year range
  python scrape_nvidia_papers.py --dry-run             # preview only
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
import hashlib
import time
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
INDEX_PATH = REPO_ROOT / "index" / "all_papers.json"
PAPERS_DIR = REPO_ROOT / "papers"

# Venue name normalization (same as import_nvidia_papers.py)
VENUE_MAP = {
    "CVPR": "CVPR", "ICLR": "ICLR", "ICML": "ICML", "NeurIPS": "NeurIPS",
    "SIGGRAPH": "SIGGRAPH", "ICCV": "ICCV", "CoRL": "CoRL", "ICRA": "ICRA",
    "IROS": "IROS", "RSS": "RSS", "PLDI": "PLDI", "ISCA": "ISCA",
    "MICRO": "MICRO", "ASPLOS": "ASPLOS", "HPCA": "HPCA", "SC": "SC",
    "OSDI": "OSDI", "SOSP": "SOSP", "NSDI": "NSDI", "SIGCOMM": "SIGCOMM",
    "ATC": "USENIX ATC", "EuroSys": "EuroSys", "FAST": "FAST",
    "EMNLP": "EMNLP", "ACL": "ACL", "NAACL": "NAACL", "AAAI": "AAAI",
    "IJCAI": "IJCAI", "VLDB": "VLDB", "SIGMOD": "SIGMOD", "DAC": "DAC",
    "ECCV": "ECCV", "ISPD": "ISPD", "VSS": "VSS",
}

VENUE_PATH_MAP = {
    "CVPR": "cvpr", "ICLR": "iclr", "ICML": "icml", "NeurIPS": "neurips",
    "SIGGRAPH": "siggraph", "ICCV": "iccv", "CoRL": "corl", "ICRA": "icra",
    "IROS": "iros", "RSS": "rss", "PLDI": "pldi", "ISCA": "isca",
    "MICRO": "micro", "ASPLOS": "asplos", "HPCA": "hpca", "SC": "sc",
    "OSDI": "osdi", "SOSP": "sosp", "NSDI": "nsdi", "SIGCOMM": "sigcomm",
    "USENIX ATC": "atc", "EuroSys": "eurosys", "FAST": "fast",
    "EMNLP": "emnlp", "ACL": "acl", "NAACL": "naacl", "AAAI": "aaai",
    "IJCAI": "ijcai", "VLDB": "vldb", "SIGMOD": "sigmod", "DAC": "dac",
    "ECCV": "eccv", "ISPD": "ispd", "VSS": "vss",
}

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
BASE_URL = "https://research.nvidia.com/publications"


def slugify(title: str) -> str:
    slug = title.lower()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'[\s-]+', '-', slug)
    slug = slug.strip('-')
    if len(slug) > 80:
        slug = slug[:80].rstrip('-')
    if not slug:
        slug = hashlib.md5(title.encode()).hexdigest()[:12]
    return slug


def normalize_venue(venue_tag: str, year: int) -> tuple[str, str]:
    for key, canonical in VENUE_MAP.items():
        if key.lower() in venue_tag.lower():
            path = VENUE_PATH_MAP.get(canonical, venue_tag.lower().replace(' ', '-'))
            return f"{canonical} {year}", path
    return f"arXiv {year}", "arxiv"


def fetch_page(year: int, page: int, timeout: int = 30) -> str | None:
    """Fetch a single page of NVIDIA publications for a given year."""
    url = f"{BASE_URL}?f%5B0%5D=publication_date%3A{year}&page={page}"
    cmd = [
        "curl", "-s", "--max-time", str(timeout),
        "-H", f"User-Agent: {USER_AGENT}",
        url
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 5)
        if result.returncode != 0:
            print(f"  curl failed: {result.stderr}", file=sys.stderr)
            return None
        return result.stdout
    except Exception as e:
        print(f"  fetch error: {e}", file=sys.stderr)
        return None


def parse_html(html: str) -> list[dict]:
    """Parse NVIDIA Research page raw HTML into paper records."""
    papers = []

    # Each paper entry is a <div class="views-row"> containing:
    #   views-field-title: <a href="/publication/YYYY-MM_slug">Title</a>
    #   views-field-field-authors: <a href="/person/name">NV Author</a>, plain names
    #   views-field-field-published-in: <a href="...publication_events:ID">VENUE</a>

    # Find all views-row divs
    row_pattern = re.compile(
        r'<div class="views-row">'
        r'(.*?)'
        r'</div>\s*<div class="views-row">|'
        r'<div class="views-row">(.*?)</div>\s*</div>\s*</div>',  # last row
        re.DOTALL
    )

    # Simpler: split by views-row boundaries
    rows = re.split(r'<div class="views-row">', html)[1:]  # first split is before first row

    for row_html in rows:
        # Extract title and URL
        title_m = re.search(
            r'<a href="(/publication/(\d{4})-(\d{2})[^"]+)"[^>]*>([^<]+)</a>',
            row_html
        )
        if not title_m:
            continue

        url_path = title_m.group(1)
        year = int(title_m.group(2))
        month = title_m.group(3)
        title = title_m.group(4).strip()
        url = f"https://research.nvidia.com{url_path}"

        # Extract NVIDIA authors (with /person/ links)
        nv_authors = []
        for pm in re.finditer(r'<a href="/person/[^"]*"[^>]*>([^<]+)</a>', row_html):
            name = pm.group(1).strip()
            if name not in nv_authors:
                nv_authors.append(name)

        # Extract academic authors (plain text not inside <a> tags)
        # Get the authors field content
        authors_field_m = re.search(
            r'views-field-field-authors[^>]*>.*?<span class="field-content">(.*?)</span>',
            row_html, re.DOTALL
        )
        ac_authors = []
        if authors_field_m:
            authors_html = authors_field_m.group(1)
            # Remove all <a> tags and their content (NVIDIA authors)
            clean = re.sub(r'<a[^>]*>[^<]*</a>', '', authors_html)
            # Also remove any remaining HTML tags
            clean = re.sub(r'<[^>]+>', '', clean)
            # Split by commas
            for name in clean.split(','):
                name = name.strip()
                name = re.sub(r'\s+', ' ', name)
                if name and len(name) > 1 and name not in nv_authors:
                    if name not in ac_authors:
                        ac_authors.append(name)

        # Extract venue
        venue_m = re.search(
            r'publication_events[^"]*">([^<]+)</a>',
            row_html
        )
        venue_tag = venue_m.group(1).strip() if venue_m else "Unknown"

        canonical_venue, venue_path = normalize_venue(venue_tag, year)

        papers.append({
            "title": title,
            "url": url,
            "nvidia_url": url,
            "year": year,
            "month": month,
            "date": f"{year}-{month}",
            "venue_tag": venue_tag,
            "conference": canonical_venue,
            "venue_path": venue_path,
            "nvidia_authors": nv_authors,
            "academic_authors": ac_authors,
            "all_authors": nv_authors + ac_authors,
        })

    return papers


def create_filter_records(papers: list[dict]) -> list[dict]:
    """Convert parsed papers to filter records matching SPEC.md format."""
    records = []
    existing_ids = set()
    existing_urls = set()
    venue_counters = {}

    if INDEX_PATH.exists():
        with open(INDEX_PATH) as f:
            idx = json.load(f)
            for p in idx.get("papers", []):
                existing_ids.add(p["id"])
                if p.get("url"):
                    existing_urls.add(p["url"])
                vid = p["id"]
                m = re.match(r'([a-z]+)(\d{2,4})[-.](\d+)', vid)
                if m:
                    prefix = m.group(1) + m.group(2)
                    num = int(m.group(3))
                    venue_counters[prefix] = max(venue_counters.get(prefix, 0), num)
                else:
                    m2 = re.match(r'([a-z]+)-(\d+)', vid)
                    if m2:
                        prefix = m2.group(1)
                        num = int(m2.group(2))
                        venue_counters[prefix] = max(venue_counters.get(prefix, 0), num)

    for p in papers:
        if p["url"] in existing_urls:
            continue

        vp = p["venue_path"]
        if vp not in venue_counters:
            venue_counters[vp] = 0
        venue_counters[vp] += 1
        paper_id = f"{vp}-{venue_counters[vp]:04d}"

        slug = slugify(p["title"])
        topics = ["AI & Machine Learning"]

        record = {
            "id": paper_id,
            "title": p["title"],
            "conference": p["conference"],
            "date": p["date"],
            "authors": [],
            "topics": topics,
            "tags": ["nvidia-research"],
            "arxiv": "",
            "url": p["url"],
            "status": "new",
            "is_industry": True,
            "file": f"papers/{vp}/{p['year']}/{paper_id}-{slug}.md",
            "nvidia_authors": p["nvidia_authors"],
            "academic_authors": p["academic_authors"],
            "nvidia_url": p["nvidia_url"],
            "venue_tag": p["venue_tag"],
        }

        for name in p["all_authors"]:
            is_nv = name in p["nvidia_authors"]
            record["authors"].append({
                "name": name,
                "affiliation": "NVIDIA" if is_nv else "",
                "is_industry": is_nv,
            })

        records.append(record)

    return records


def write_paper_files(records: list[dict], dry_run: bool = False):
    for r in records:
        file_path = REPO_ROOT / r["file"]
        if not dry_run:
            file_path.parent.mkdir(parents=True, exist_ok=True)

        lines = ["---"]
        lines.append(f"id: {r['id']}")
        lines.append(f"title: \"{r['title']}\"")
        lines.append(f"conference: {r['conference']}")
        lines.append(f"date: {r['date']}")
        lines.append("authors:")
        for a in r["authors"]:
            lines.append(f"  - name: \"{a['name']}\"")
            lines.append(f"    affiliation: \"{a['affiliation']}\"")
            lines.append(f"    is_industry: {str(a['is_industry']).lower()}")
        lines.append("topics:")
        for t in r["topics"]:
            lines.append(f"  - {t}")
        lines.append("tags:")
        for t in r["tags"]:
            lines.append(f"  - {t}")
        lines.append(f"arxiv: \"{r['arxiv']}\"")
        lines.append(f"url: \"{r['url']}\"")
        lines.append(f"status: {r['status']}")
        lines.append("---")
        fm_yaml = "\n".join(lines)
        content = fm_yaml + "\n\n"
        content += f"# {r['title']}\n\n"
        content += "## 摘要\n\n*(待补充)*\n\n"
        content += "## Problem\n\n*(待补充)*\n\n"
        content += "## Method\n\n*(待补充)*\n\n"
        content += "## Evaluation\n\n*(待补充)*\n\n"
        content += "## Limitations\n\n*(待补充)*\n"

        if not dry_run:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  Wrote: {file_path}")


def update_index(records: list[dict], dry_run: bool = False):
    if INDEX_PATH.exists():
        with open(INDEX_PATH) as f:
            idx = json.load(f)
    else:
        idx = {"last_updated": "", "total_count": 0, "papers": []}

    existing_ids = {p["id"] for p in idx["papers"]}
    new_count = 0

    for r in records:
        if r["id"] not in existing_ids:
            idx_entry = {
                "id": r["id"],
                "title": r["title"],
                "conference": r["conference"],
                "date": r["date"],
                "topics": r["topics"],
                "tags": r["tags"],
                "abstract": "",
                "arxiv": r["arxiv"],
                "url": r["url"],
                "status": r["status"],
                "is_industry": r["is_industry"],
                "file": r["file"],
            }
            idx["papers"].append(idx_entry)
            existing_ids.add(r["id"])
            new_count += 1

    idx["total_count"] = len(idx["papers"])
    idx["last_updated"] = datetime.now().strftime("%Y-%m-%d")

    if not dry_run:
        with open(INDEX_PATH, 'w', encoding='utf-8') as f:
            json.dump(idx, f, ensure_ascii=False, indent=2)
        print(f"  Index updated: {new_count} new, {idx['total_count']} total")

    return new_count


def scrape_year(year: int, dry_run: bool = False) -> int:
    """Scrape all pages for a given year."""
    total = 0
    page = 0

    while True:
        print(f"  Fetching year={year} page={page}...", file=sys.stderr)
        html = fetch_page(year, page)
        if not html:
            print(f"  Failed to fetch page {page}", file=sys.stderr)
            break

        papers = parse_html(html)
        if not papers:
            print(f"  No papers found on page {page}", file=sys.stderr)
            break

        print(f"  Parsed {len(papers)} papers from page {page}", file=sys.stderr)

        records = create_filter_records(papers)
        new_count = len(records)
        print(f"  {new_count} new records ({len(papers) - new_count} duplicates)", file=sys.stderr)

        if not dry_run and records:
            write_paper_files(records, dry_run=False)
            update_index(records, dry_run=False)

        total += new_count
        page += 1

        # Stop only when page returns zero results
        if len(papers) == 0:
            break

        time.sleep(1)  # Polite delay

    return total


def main():
    import argparse
    ap = argparse.ArgumentParser(description="Scrape NVIDIA Research publications")
    ap.add_argument("--year", type=int, help="Single year to scrape")
    ap.add_argument("--years", help="Year range, e.g. 2020-2025")
    ap.add_argument("--page", type=int, default=0, help="Start page (only with --year)")
    ap.add_argument("--dry-run", action="store_true", help="Preview only")
    ap.add_argument("--json-only", action="store_true", help="Output JSON only, no file writes")
    args = ap.parse_args()

    if args.years:
        start, end = map(int, args.years.split('-'))
        years = list(range(start, end + 1))
    elif args.year:
        years = [args.year]
    else:
        print("Specify --year or --years", file=sys.stderr)
        sys.exit(1)

    grand_total = 0
    for year in sorted(years, reverse=True):
        print(f"\n{'='*50}", file=sys.stderr)
        print(f"Scraping {year}...", file=sys.stderr)
        if args.year and args.page > 0:
            # Single page mode
            html = fetch_page(year, args.page)
            if html:
                papers = parse_html(html)
                records = create_filter_records(papers)
                if args.json_only:
                    print(json.dumps(records, ensure_ascii=False, indent=2))
                elif args.dry_run:
                    for r in records:
                        print(f"  {r['id']}: {r['title'][:80]}")
                else:
                    write_paper_files(records)
                    update_index(records)
                grand_total = len(records)
        else:
            count = scrape_year(year, dry_run=args.dry_run)
            grand_total += count

    print(f"\n{'='*50}", file=sys.stderr)
    print(f"Done. Total new papers: {grand_total}", file=sys.stderr)


if __name__ == "__main__":
    main()
