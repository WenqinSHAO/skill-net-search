#!/usr/bin/env python3
"""Enrich existing NVIDIA papers by scraping individual detail pages.

For each paper, fetches the detail page and extracts:
- Research areas (NVIDIA's own taxonomy, mapped to project domains)
- Abstract
- Full venue name (for papers where listing page didn't have it)
- External links (project pages, etc.)

Updates both paper markdown files and index/all_papers.json.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
import time
from html import unescape
from datetime import datetime
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
INDEX_PATH = REPO_ROOT / "index" / "all_papers.json"

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

INDUSTRY_KEYWORDS = {
    "nvidia",
    "google",
    "deepmind",
    "microsoft",
    "meta",
    "facebook",
    "apple",
    "amazon",
    "adobe",
    "intel",
    "amd",
    "arm",
    "qualcomm",
    "ibm",
    "oracle",
    "salesforce",
    "bytedance",
    "tencent",
    "alibaba",
    "huawei",
    "samsung",
    "sony",
    "tesla",
    "openai",
    "anthropic",
}

# NVIDIA research area → project domain taxonomy mapping
RESEARCH_AREA_TO_DOMAIN = {
    "Artificial Intelligence and Machine Learning": "AI & Machine Learning",
    "Computer Vision": "Computer Vision",
    "Computer Graphics": "Graphics_rendering",
    "Robotics": "Robotics_autonomous",
    "Autonomous Vehicles": "Robotics_autonomous",
    "Generative AI": "Foundation_models",
    "Computer Architecture": "GPU_architecture",
    "Circuits and VLSI Design": "GPU_architecture",
    "High Performance Computing": "Simulation_HPC",
    "Networking": "Interconnect_networking",
    "Natural Language Processing": "Foundation_models",
    "Speech Processing": "Foundation_models",
    "Machine Translation": "Foundation_models",
    "Real-Time Rendering": "Graphics_rendering",
    "VR, AR and Display Technology": "Graphics_rendering",
    "Programming Languages, Systems and Tools": "CUDA_ecosystem",
    "Algorithms and Numerical Methods": "CUDA_ecosystem",
    "Esports": "Applied_perception",
    "Applied Perception": "Applied_perception",
    "Human Computer Interaction": "Applied_perception",
    "Climate Simulation": "Simulation_HPC",
    "World Simulation": "Simulation_HPC",
    "Quantum Computing": "Quantum_computing",
    "Medical": "Medical_imaging",
    "Telecommunications": "Interconnect_networking",
    "Storage and Systems": "Data_systems",
    "Physical AI": "Robotics_autonomous",
    "Hyperscale Graphics": "Graphics_rendering",
    "Computational Photography and Imaging": "Computer Vision",
    "Resilience and Safety": "Robotics_autonomous",
    "Security": "Miscellaneous",
    "3D Deep Learning": "Computer Vision",
}


def fetch_detail_page(url: str, timeout: int = 20) -> str | None:
    """Fetch a paper detail page via curl."""
    cmd = [
        "curl", "-s", "--max-time", str(timeout),
        "-H", f"User-Agent: {USER_AGENT}",
        url
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 5)
        if result.returncode != 0:
            return None
        return result.stdout
    except Exception:
        return None


def clean_text(text: str) -> str:
    """Normalize scraped text and remove YAML-hostile control characters."""
    text = unescape(text)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', text)
    return re.sub(r'\s+', ' ', text).strip()


def yaml_quote(value: object) -> str:
    return json.dumps("" if value is None else str(value), ensure_ascii=False)


def is_industry_affiliation(affiliation: str) -> bool:
    lowered = affiliation.lower()
    return any(keyword in lowered for keyword in INDUSTRY_KEYWORDS)


def split_frontmatter(content: str) -> tuple[str, str] | tuple[None, str]:
    if not content.startswith("---\n"):
        return None, content
    marker = "\n---\n"
    end = content.find(marker, 4)
    if end == -1:
        return None, content
    return content[4:end], content[end + len(marker):]


def extract_field_section(html: str, field_name: str) -> str:
    """Return a Drupal field section, bounded by the next field section."""
    start_m = re.search(
        rf'class="[^"]*field--name-{re.escape(field_name)}[^"]*"',
        html,
        re.DOTALL,
    )
    if not start_m:
        return ""
    tag_start = html.rfind("<", 0, start_m.start())
    if tag_start == -1:
        tag_start = start_m.start()
    next_m = re.search(
        r'<(?:section|div)\b[^>]*class="[^"]*field--name-',
        html[start_m.end():],
        re.DOTALL,
    )
    end = start_m.end() + next_m.start() if next_m else len(html)
    return html[tag_start:end]


def parse_author_chunks_from_html(section: str) -> list[str]:
    """Extract one author-ish text chunk per linked or text author in order."""
    if not section:
        return []

    normalized = section
    normalized = re.sub(r'<a\b[^>]*href="/person/[^"]*"[^>]*>(.*?)</a>', r'\1 (NVIDIA)', normalized, flags=re.I | re.S)
    normalized = re.sub(r'</(?:div|p|li|span|a)>\s*', '\n', normalized, flags=re.I)
    normalized = re.sub(r'<br\s*/?>', '\n', normalized, flags=re.I)
    text = clean_text(normalized.replace('\n', ' | '))

    chunks = []
    for chunk in re.split(r'\s*\|\s*', text):
        chunk = chunk.strip(' ,')
        if not chunk:
            continue
        if chunk.lower() in {"authors", "author"}:
            continue
        if re.search(r'\([^)]+\)', chunk):
            chunks.append(chunk)
            continue
        if chunk and not re.search(r'^(publication date|published in|research area|external links)\b', chunk, re.I):
            chunks.append(chunk)
    return chunks


def parse_authors_from_detail_page(html: str) -> list[dict]:
    """Extract canonical detail-page author order and affiliations."""
    section = extract_field_section(html, "field-authors")
    chunks = parse_author_chunks_from_html(section)

    if not chunks:
        text = clean_text(re.sub(r'<br\s*/?>', '\n', html, flags=re.I))
        m = re.search(
            r'(?:^|\s)Authors\s+(.*?)(?:\s+Publication Date\s+|\s+Published in\s+|\s+Research Area\s+)',
            text,
            re.I | re.S,
        )
        if m:
            chunks = [c.strip() for c in re.split(r'\s{2,}| \| ', m.group(1)) if c.strip()]

    authors = []
    seen = set()
    for chunk in chunks:
        chunk = clean_text(chunk).strip(' ,')
        if not chunk:
            continue
        if chunk.endswith(")") and " (" in chunk:
            name_part, affiliation_part = chunk.split(" (", 1)
            name = clean_text(name_part)
            affiliation = clean_text(affiliation_part[:-1])
        else:
            name = clean_text(chunk)
            affiliation = ""
        if not name or name.lower() in seen:
            continue
        seen.add(name.lower())
        authors.append({
            "name": name,
            "affiliation": affiliation,
            "is_industry": is_industry_affiliation(affiliation),
        })
    return authors


def merge_detail_authors(existing_authors: list[dict], detail_authors: list[dict]) -> list[dict]:
    """Prefer detail-page order and affiliations, preserving unmatched existing authors."""
    if not detail_authors:
        return existing_authors

    existing_by_name = {
        (a.get("name") or "").strip().lower(): a
        for a in existing_authors
        if isinstance(a, dict) and (a.get("name") or "").strip()
    }

    merged = []
    used = set()
    for detail in detail_authors:
        name = detail["name"]
        key = name.lower()
        existing = existing_by_name.get(key, {})
        affiliation = detail.get("affiliation") or existing.get("affiliation", "")
        is_industry = bool(
            detail.get("is_industry")
            or existing.get("is_industry")
            or is_industry_affiliation(affiliation)
        )
        merged.append({
            "name": name,
            "affiliation": affiliation,
            "is_industry": is_industry,
        })
        used.add(key)

    return merged


def parse_detail_page(html: str) -> dict:
    """Extract enrichment data from a paper detail page."""
    data = {"authors": parse_authors_from_detail_page(html)}

    # Abstract (field--name-body)
    body_m = re.search(
        r'class="[^"]*field--name-body[^"]*".*?<p>(.*?)</p>',
        html, re.DOTALL
    )
    if body_m:
        abstract = body_m.group(1)
        abstract = re.sub(r'<[^>]+>', '', abstract)
        abstract = re.sub(r'\s+', ' ', abstract).strip()
        data["abstract"] = abstract

    # Research areas (field--name-field-id-res-area)
    research_areas = []
    ra_section = re.search(
        r'class="[^"]*field--name-field-id-res-area[^"]*".*?</div>\s*</div>\s*</section>',
        html, re.DOTALL
    )
    if ra_section:
        for link_m in re.finditer(
            r'<a href="/research-area/[^"]*"[^>]*>([^<]+)</a>',
            ra_section.group()
        ):
            ra_name = link_m.group(1).strip()
            if ra_name not in research_areas:
                research_areas.append(ra_name)
    data["research_areas"] = research_areas

    # Map research areas to project domains
    domains = set()
    for ra in research_areas:
        domain = RESEARCH_AREA_TO_DOMAIN.get(ra)
        if domain:
            domains.add(domain)
    data["domains"] = sorted(domains) if domains else ["AI & Machine Learning"]

    # Published in (field--name-field-published-in) — richer venue info
    pub_section = re.search(
        r'class="[^"]*field--name-field-published-in[^"]*".*?</div>\s*</div>\s*</section>',
        html, re.DOTALL
    )
    if pub_section:
        link_m = re.search(r'<a href="([^"]*)"[^>]*>([^<]+)</a>', pub_section.group())
        if link_m:
            data["published_in"] = link_m.group(2).strip()
            data["published_in_url"] = link_m.group(1).strip()

    # External links (field--name-field-extrefs)
    ext_links = []
    ext_section = re.search(
        r'class="[^"]*field--name-field-extrefs[^"]*".*?</div>\s*</div>\s*</section>',
        html, re.DOTALL
    )
    if ext_section:
        for link_m in re.finditer(
            r'<a href="([^"]+)"[^>]*>([^<]+)</a>',
            ext_section.group()
        ):
            ext_links.append({"name": link_m.group(2).strip(), "url": link_m.group(1).strip()})
    data["external_links"] = ext_links

    return data


def update_paper_file(file_path: Path, enrichment: dict, paper: dict):
    """Update a paper markdown file with enriched content."""
    if not file_path.exists():
        print(f"  WARNING: file not found: {file_path}", file=sys.stderr)
        return

    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    fm_str, body = split_frontmatter(content)
    if fm_str is None:
        print(f"  WARNING: no frontmatter in {file_path}", file=sys.stderr)
        return

    sanitized_fm = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', fm_str)
    try:
        fm = yaml.safe_load(sanitized_fm) or {}
    except Exception as exc:
        print(f"  WARNING: cannot parse frontmatter in {file_path}: {exc}", file=sys.stderr)
        return

    existing_authors = fm.get("authors") if isinstance(fm.get("authors"), list) else []
    fm["authors"] = merge_detail_authors(existing_authors, enrichment.get("authors", []))
    fm["topics"] = enrichment.get("domains", fm.get("topics") or ["AI & Machine Learning"])
    if enrichment.get("research_areas"):
        fm["research_areas"] = enrichment["research_areas"]
    if enrichment.get("external_links"):
        fm["external_links"] = enrichment["external_links"]
    if enrichment.get("abstract"):
        fm["abstract"] = enrichment["abstract"][:300]

    new_body = body
    if enrichment.get("abstract"):
        abs_text = enrichment["abstract"]
        if '*(待补充)*' in new_body:
            new_body = new_body.replace(
                '## 摘要\n\n*(待补充)*',
                f'## 摘要\n\n{abs_text}'
            )
        abs_pattern = r'## 摘要\n\n\*\(待补充\)\*'
        if re.search(abs_pattern, new_body):
            new_body = re.sub(abs_pattern, f'## 摘要\n\n{abs_text}', new_body)
        elif '## 摘要' in new_body and '*(待补充)*' in new_body:
            new_body = new_body.replace(
                '## 摘要\n\n*(待补充)*',
                f'## 摘要\n\n{abs_text}'
            )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(f'---\n{render_frontmatter(fm)}---\n{new_body}')


def render_frontmatter(fm: dict) -> str:
    """Render canonical paper YAML without duplicate top-level keys."""
    preferred = [
        "id",
        "title",
        "conference",
        "date",
        "authors",
        "topics",
        "tags",
        "arxiv",
        "research_areas",
        "external_links",
        "abstract",
        "url",
        "status",
    ]
    lines = []

    def emit_key(key: str, value: object):
        if key == "authors":
            lines.append("authors:")
            for author in value or []:
                if not isinstance(author, dict):
                    continue
                lines.append(f"  - name: {yaml_quote(author.get('name', ''))}")
                lines.append(f"    affiliation: {yaml_quote(author.get('affiliation', ''))}")
                lines.append(f"    is_industry: {str(bool(author.get('is_industry', False))).lower()}")
            return
        if key in {"topics", "tags", "research_areas"}:
            lines.append(f"{key}:")
            for item in value or []:
                lines.append(f"  - {yaml_quote(item) if key == 'research_areas' else item}")
            return
        if key == "external_links":
            lines.append("external_links:")
            for link in value or []:
                if not isinstance(link, dict):
                    continue
                lines.append(f"  - name: {yaml_quote(link.get('name', ''))}")
                lines.append(f"    url: {yaml_quote(link.get('url', ''))}")
            return
        if isinstance(value, bool):
            lines.append(f"{key}: {str(value).lower()}")
        else:
            lines.append(f"{key}: {yaml_quote(value)}")

    emitted = set()
    for key in preferred:
        if key in fm:
            emit_key(key, fm[key])
            emitted.add(key)
    for key in fm:
        if key not in emitted:
            emit_key(key, fm[key])

    return "\n".join(lines) + "\n"


def update_index_entry(paper: dict, enrichment: dict):
    """Update the index entry for a paper."""
    # Update topics
    paper["topics"] = enrichment.get("domains", paper.get("topics", ["AI & Machine Learning"]))

    # Add abstract
    if enrichment.get("abstract"):
        paper["abstract"] = enrichment["abstract"][:500]  # Keep index abstract manageable

    # Add research areas
    if enrichment.get("research_areas"):
        paper["research_areas"] = enrichment["research_areas"]

    # Add enriched conference name
    if enrichment.get("published_in"):
        paper["published_in"] = enrichment["published_in"]

    if enrichment.get("authors"):
        paper["author_affiliations_enriched"] = True


def main():
    import argparse
    ap = argparse.ArgumentParser(description="Enrich NVIDIA papers from detail pages")
    ap.add_argument("--limit", type=int, default=0, help="Max papers to process (0=all)")
    ap.add_argument("--dry-run", action="store_true", help="Preview only")
    ap.add_argument("--start-from", type=int, default=0, help="Start from paper index N")
    args = ap.parse_args()

    # Load index
    with open(INDEX_PATH) as f:
        idx = json.load(f)

    nv_papers = [p for p in idx["papers"] if "nvidia-research" in p.get("tags", [])]
    print(f"Found {len(nv_papers)} NVIDIA papers in index", file=sys.stderr)

    to_process = nv_papers[args.start_from:]
    if args.limit > 0:
        to_process = to_process[:args.limit]

    print(f"Processing {len(to_process)} papers...", file=sys.stderr)

    enriched_count = 0
    error_count = 0
    ra_distribution = {}
    domain_distribution = {}

    for i, paper in enumerate(to_process):
        url = paper.get("nvidia_url") or paper.get("url", "")
        if not url:
            continue

        print(f"  [{i+1}/{len(to_process)}] {paper['id']}: {paper['title'][:70]}...", file=sys.stderr)

        html = fetch_detail_page(url)
        if not html:
            print(f"    ERROR: failed to fetch", file=sys.stderr)
            error_count += 1
            continue

        enrichment = parse_detail_page(html)

        if not enrichment.get("abstract") and not enrichment.get("research_areas"):
            print(f"    WARNING: no enrichment data extracted", file=sys.stderr)
            error_count += 1
            continue

        # Print what we found
        if enrichment.get("research_areas"):
            print(f"    Research areas: {enrichment['research_areas']}", file=sys.stderr)
            for ra in enrichment["research_areas"]:
                ra_distribution[ra] = ra_distribution.get(ra, 0) + 1
        if enrichment.get("domains"):
            print(f"    Domains: {enrichment['domains']}", file=sys.stderr)
            for d in enrichment["domains"]:
                domain_distribution[d] = domain_distribution.get(d, 0) + 1
        if enrichment.get("abstract"):
            print(f"    Abstract: {enrichment['abstract'][:100]}...", file=sys.stderr)
        if enrichment.get("published_in"):
            print(f"    Published in: {enrichment['published_in']}", file=sys.stderr)
        if enrichment.get("external_links"):
            print(f"    External links: {len(enrichment['external_links'])}", file=sys.stderr)

        if not args.dry_run:
            # Update paper markdown file
            file_path = REPO_ROOT / paper["file"]
            update_paper_file(file_path, enrichment, paper)

            # Update index entry
            update_index_entry(paper, enrichment)

        enriched_count += 1
        time.sleep(0.3)  # Polite delay

    # Save updated index
    if not args.dry_run and enriched_count > 0:
        idx["last_updated"] = datetime.now().strftime("%Y-%m-%d")
        with open(INDEX_PATH, 'w', encoding='utf-8') as f:
            json.dump(idx, f, ensure_ascii=False, indent=2)
        print(f"\nIndex saved: {idx['total_count']} total papers", file=sys.stderr)

    # Summary
    print(f"\n{'='*50}", file=sys.stderr)
    print(f"Enriched: {enriched_count} papers", file=sys.stderr)
    print(f"Errors: {error_count}", file=sys.stderr)
    print(f"\nResearch area distribution:", file=sys.stderr)
    for ra, count in sorted(ra_distribution.items(), key=lambda x: -x[1]):
        print(f"  {ra}: {count}", file=sys.stderr)
    print(f"\nDomain distribution:", file=sys.stderr)
    for d, count in sorted(domain_distribution.items(), key=lambda x: -x[1]):
        print(f"  {d}: {count}", file=sys.stderr)


if __name__ == "__main__":
    main()
