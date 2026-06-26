#!/usr/bin/env python3
"""Parse NVIDIA Research page HTML and create shared-layer paper records.

Reads HTML from stdin or file, extracts publication entries, and writes
paper markdown files + updates index/all_papers.json.

The HTML should be fetched via SearXNG web_url_read and piped here.
"""

from __future__ import annotations

import json
import re
import sys
import hashlib
from datetime import datetime
from pathlib import Path
from urllib.parse import unquote

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
INDEX_PATH = REPO_ROOT / "index" / "all_papers.json"
PAPERS_DIR = REPO_ROOT / "papers"

# Venue name normalization
VENUE_MAP = {
    "CVPR": "CVPR",
    "ICLR": "ICLR",
    "ICML": "ICML",
    "NeurIPS": "NeurIPS",
    "SIGGRAPH": "SIGGRAPH",
    "ICCV": "ICCV",
    "CORL": "CoRL",
    "ICRA": "ICRA",
    "IROS": "IROS",
    "RSS": "RSS",
    "PLDI": "PLDI",
    "ISCA": "ISCA",
    "MICRO": "MICRO",
    "ASPLOS": "ASPLOS",
    "HPCA": "HPCA",
    "SC": "SC",
    "OSDI": "OSDI",
    "SOSP": "SOSP",
    "NSDI": "NSDI",
    "SIGCOMM": "SIGCOMM",
    "ATC": "USENIX ATC",
    "EuroSys": "EuroSys",
    "FAST": "FAST",
    "EMNLP": "EMNLP",
    "ACL": "ACL",
    "NAACL": "NAACL",
    "AAAI": "AAAI",
    "IJCAI": "IJCAI",
    "VLDB": "VLDB",
    "SIGMOD": "SIGMOD",
    "DAC": "DAC",
    "ECCV": "ECCV",
}

# Conference to venue_lower mapping for paper paths
VENUE_PATH_MAP = {
    "CVPR": "cvpr", "ICLR": "iclr", "ICML": "icml", "NeurIPS": "neurips",
    "SIGGRAPH": "siggraph", "ICCV": "iccv", "CoRL": "corl", "ICRA": "icra",
    "IROS": "iros", "RSS": "rss", "PLDI": "pldi", "ISCA": "isca",
    "MICRO": "micro", "ASPLOS": "asplos", "HPCA": "hpca", "SC": "sc",
    "OSDI": "osdi", "SOSP": "sosp", "NSDI": "nsdi", "SIGCOMM": "sigcomm",
    "USENIX ATC": "atc", "EuroSys": "eurosys", "FAST": "fast",
    "EMNLP": "emnlp", "ACL": "acl", "NAACL": "naacl", "AAAI": "aaai",
    "IJCAI": "ijcai", "VLDB": "vldb", "SIGMOD": "sigmod", "DAC": "dac",
    "ECCV": "eccv",
}


def normalize_nvidia_url(url: str) -> str:
    if not url:
        return ""
    return unquote(url).replace("%5F", "_").replace("%5f", "_")


def slugify(title: str) -> str:
    """Create a filesystem-safe slug from a title."""
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
    """Normalize venue name. Returns (canonical_name, venue_lower)."""
    for key, canonical in VENUE_MAP.items():
        if key.lower() in venue_tag.lower():
            path = VENUE_PATH_MAP.get(canonical, venue_tag.lower().replace(' ', '-'))
            return f"{canonical} {year}", path
    # Unknown venue - treat as arXiv
    return f"arXiv {year}", "arxiv"


def parse_html(html: str) -> list[dict]:
    """Parse NVIDIA Research page (markdown from SearXNG) into paper records."""
    papers = []
    current_venue = None
    processed_indices = set()  # Track lines already handled via lookahead

    lines = html.split('\n')

    for i, line in enumerate(lines):
        if i in processed_indices:
            continue

        # Detect "X results found" to know we're in results
        if re.search(r'\d+\s+results?\s+found', line):
            continue

        # Detect "Publication Year" section followed by year counts
        year_count_m = re.search(r'\[(\d{4})\s+\((\d+)\)\]', line)
        if year_count_m and 'publication%5Fdate' in line:
            continue

        # Detect "Events" filters: * [VENUE (N)] or * [VENUE]
        event_m = re.search(
            r'\*\s*\[([A-Z][A-Za-z0-9\s\-\']+(?:\s+\d+)?)\]'
            r'\([^)]*publication%5Fevents[^)]*\)',
            line
        )
        if event_m:
            current_venue = event_m.group(1)
            current_venue = re.sub(r'\s+\d{4}$', '', current_venue)
            continue

        # Skip section headings
        if re.match(r'###\s+(?:Publication Year|Research Areas|Events|\d{4})\s*$', line.strip()):
            current_venue = None
            continue

        # Clear filter button resets venue
        if 'Clear all' in line:
            current_venue = None
            continue

        # Find publication links in format: [Title](/publication/YYYY-MM_slug)
        pub_matches = list(re.finditer(
            r'\[([^\]]+)\]\((/publication/(\d{4})-(\d{2})[%_5F][^\)]+)\)',
            line
        ))

        # Also check next line for publication link if current line has event tag pattern
        if not pub_matches and i + 1 < len(lines):
            next_line = lines[i + 1]
            pub_matches = list(re.finditer(
                r'\[([^\]]+)\]\((/publication/(\d{4})-(\d{2})[%_5F][^\)]+)\)',
                next_line
            ))
            if pub_matches:
                line = next_line
                i = i + 1
                processed_indices.add(i)

        for pub_m in pub_matches:
            title = pub_m.group(1)
            url = normalize_nvidia_url(f"https://research.nvidia.com{pub_m.group(2)}")
            year = int(pub_m.group(3))
            month = pub_m.group(4)

            # Get rest of this line + next few lines for authors
            # Authors may be on the same line, immediately following, or after a blank line
            rest = line[pub_m.end():].strip()
            author_lines = []
            for j in range(i + 1, min(i + 4, len(lines))):
                nl = lines[j].strip()
                # Stop if we hit another publication link, event tag, or heading
                if re.match(r'^\s*[\*\#]|^\s*\[.*\]\(/publication/', nl):
                    break
                if '/publication/' in nl:
                    break
                if nl:  # Non-empty line
                    author_lines.append(nl)

            rest += ' ' + ' '.join(author_lines)

            # Parse NVIDIA authors (linked to /person/)
            nv_authors = []
            for pm in re.finditer(r'\[([^\]]+)\]\(/person/[^\)]+\)', rest):
                name = pm.group(1)
                if name not in nv_authors:
                    nv_authors.append(name)

            # Parse academic (non-NVIDIA) authors
            ac_authors = []
            clean = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', rest)
            for part in clean.split(','):
                name = part.strip()
                name = re.sub(r'\s+', ' ', name)
                # Remove trailing/leading punctuation
                name = name.strip('.,;')
                if name and len(name) > 1 and name not in nv_authors:
                    if name not in ac_authors:
                        ac_authors.append(name)

            venue_tag = current_venue or "Unknown"
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

            current_venue = None  # Reset after use

    return papers


def create_filter_records(papers: list[dict]) -> list[dict]:
    """Convert parsed papers to filter records matching SPEC.md format."""
    records = []

    # Load existing index to check duplicates and get next IDs
    existing_ids = set()
    existing_urls = set()
    venue_counters = {}

    if INDEX_PATH.exists():
        with open(INDEX_PATH) as f:
            idx = json.load(f)
            for p in idx.get("papers", []):
                existing_ids.add(p["id"])
                if p.get("url"):
                    existing_urls.add(normalize_nvidia_url(p["url"]))
                # Track counters
                vid = p["id"]
                # Handle various ID formats: nsdi26-001, arxiv-2501, arxiv23-001
                m = re.match(r'([a-z]+)(\d{2,4})[-.](\d+)', vid)
                if m:
                    prefix = m.group(1) + m.group(2)
                    num = int(m.group(3))
                    venue_counters[prefix] = max(venue_counters.get(prefix, 0), num)
                else:
                    # Simpler format: arxiv-2501
                    m2 = re.match(r'([a-z]+)-(\d+)', vid)
                    if m2:
                        prefix = m2.group(1)
                        num = int(m2.group(2))
                        venue_counters[prefix] = max(venue_counters.get(prefix, 0), num)

    for p in papers:
        # Skip if URL already in index
        if normalize_nvidia_url(p["url"]) in existing_urls:
            continue

        # Generate ID
        vp = p["venue_path"]
        if vp not in venue_counters:
            venue_counters[vp] = 0
        venue_counters[vp] += 1
        paper_id = f"{vp}-{venue_counters[vp]:04d}"

        # Build slug
        slug = slugify(p["title"])

        # Determine topics from venue/domain
        topics = ["AI & Machine Learning"]  # default for NVIDIA research

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
            # Project-specific fields
            "nvidia_authors": p["nvidia_authors"],
            "academic_authors": p["academic_authors"],
            "nvidia_url": p["nvidia_url"],
            "venue_tag": p["venue_tag"],
        }

        # Build author list
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
    """Write paper markdown files to papers/ directory."""
    for r in records:
        # file field is relative to repo root, e.g. "papers/arxiv/2026/id-slug.md"
        file_path = REPO_ROOT / r["file"]
        if not dry_run:
            file_path.parent.mkdir(parents=True, exist_ok=True)

        # Build YAML frontmatter manually
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
    """Update index/all_papers.json with new records."""
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


def main():
    import argparse
    ap = argparse.ArgumentParser(description="Parse NVIDIA Research HTML and create paper records")
    ap.add_argument("html_file", help="HTML file from NVIDIA Research page")
    ap.add_argument("--dry-run", action="store_true", help="Don't write files, just show what would be done")
    ap.add_argument("--json-only", action="store_true", help="Output JSON only, don't write paper files")
    args = ap.parse_args()

    with open(args.html_file, 'r', encoding='utf-8') as f:
        html = f.read()

    papers = parse_html(html)
    print(f"Parsed {len(papers)} papers from HTML", file=sys.stderr)

    records = create_filter_records(papers)
    print(f"Created {len(records)} filter records ({len(papers) - len(records)} duplicates skipped)", file=sys.stderr)

    if args.json_only:
        print(json.dumps(records, ensure_ascii=False, indent=2))
        return

    if args.dry_run:
        print(f"DRY RUN - would create {len(records)} paper files and update index")
        for r in records:
            print(f"  {r['id']}: {r['title'][:80]} -> {r['file']}")
        return

    write_paper_files(records)
    update_index(records)

    print(f"Done. {len(records)} papers added.", file=sys.stderr)


if __name__ == "__main__":
    main()
