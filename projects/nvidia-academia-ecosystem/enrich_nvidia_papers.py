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
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
INDEX_PATH = REPO_ROOT / "index" / "all_papers.json"

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

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


def parse_detail_page(html: str) -> dict:
    """Extract enrichment data from a paper detail page."""
    data = {}

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

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split frontmatter from body
    fm_match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if not fm_match:
        print(f"  WARNING: no frontmatter in {file_path}", file=sys.stderr)
        return

    fm_str = fm_match.group(1)
    body = fm_match.group(2)

    # Parse existing frontmatter as lines
    fm_lines = fm_str.split('\n')

    # Build new frontmatter
    # Update topics with enriched domains
    new_topics = enrichment.get("domains", ["AI & Machine Learning"])

    # Build new frontmatter lines
    new_fm_lines = []
    in_topics = False
    in_tags = False
    topics_written = False
    tags_written = False
    arxiv_written = False

    for line in fm_lines:
        stripped = line.strip()

        # Track which section we're in
        if stripped.startswith('topics:'):
            in_topics = True
            new_fm_lines.append('topics:')
            for t in new_topics:
                new_fm_lines.append(f'  - {t}')
            topics_written = True
            continue
        elif stripped.startswith('tags:'):
            in_topics = False
            in_tags = True
        elif stripped.startswith('arxiv:'):
            in_tags = False
            in_topics = False
        elif stripped.startswith('  - ') and (in_topics or in_tags):
            # Skip old topics/tags, already written
            continue

        if stripped.startswith('arxiv:') and not arxiv_written:
            new_fm_lines.append(line)
            arxiv_written = True
            # After arxiv, add enriched fields
            if enrichment.get("research_areas"):
                new_fm_lines.append('research_areas:')
                for ra in enrichment["research_areas"]:
                    new_fm_lines.append(f'  - "{ra}"')
            if enrichment.get("external_links"):
                new_fm_lines.append('external_links:')
                for el in enrichment["external_links"]:
                    new_fm_lines.append(f'  - name: "{el["name"]}"')
                    new_fm_lines.append(f'    url: "{el["url"]}"')
            if enrichment.get("abstract"):
                # Truncate for frontmatter — full abstract in body
                short_abs = enrichment["abstract"][:300]
                new_fm_lines.append(f'abstract: "{short_abs}"')
            continue

        new_fm_lines.append(line)

    new_fm = '\n'.join(new_fm_lines)

    # Update body with abstract
    new_body = body
    if enrichment.get("abstract"):
        abs_text = enrichment["abstract"]
        # Replace placeholder abstract section
        if '*(待补充)*' in new_body:
            new_body = new_body.replace(
                '## 摘要\n\n*(待补充)*',
                f'## 摘要\n\n{abs_text}'
            )
        # Update abstract in a more targeted way
        abs_pattern = r'## 摘要\n\n\*\(待补充\)\*'
        if re.search(abs_pattern, new_body):
            new_body = re.sub(abs_pattern, f'## 摘要\n\n{abs_text}', new_body)
        # If no placeholder found, still has "*(待补充)*" somewhere
        elif '## 摘要' in new_body and '*(待补充)*' in new_body:
            new_body = new_body.replace(
                '## 摘要\n\n*(待补充)*',
                f'## 摘要\n\n{abs_text}'
            )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(f'---\n{new_fm}\n---\n{new_body}')


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
