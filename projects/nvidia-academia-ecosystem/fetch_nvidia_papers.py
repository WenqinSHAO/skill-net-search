#!/usr/bin/env python3
"""Fetch NVIDIA-affiliated papers from arXiv API for 2020-2026.

Uses arXiv API to search for papers with NVIDIA author affiliations
across relevant categories. Parses Atom XML, filters by affiliation,
and outputs JSON for import into the shared database.
"""

from __future__ import annotations

import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

# arXiv categories relevant to NVIDIA's research
CATEGORIES = [
    "cs.AI", "cs.LG", "cs.CL", "cs.CV", "cs.AR", "cs.DC",
    "cs.GR", "cs.RO", "cs.NI", "cs.OS", "cs.SE", "cs.PL",
    "cs.ET", "cs.IT", "cs.MM", "cs.NE", "cs.SD",
    "stat.ML", "eess.IV", "eess.AS", "quant-ph",
]

BASE_URL = "https://export.arxiv.org/api/query"

NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
}

PAPERS_DIR = Path(__file__).resolve().parent.parent.parent / "papers"
INDEX_FILE = Path(__file__).resolve().parent.parent.parent / "index" / "all_papers.json"
OUTPUT_FILE = Path(__file__).resolve().parent / "arxiv_nvidia_results.json"

# Track venue abbrevs already used for ID generation
VENUE_COUNTERS: dict[str, int] = {}


def search_arxiv(
    query: str, start: int = 0, max_results: int = 100
) -> tuple[list[dict], int]:
    """Search arXiv API and return parsed results + total count."""
    params = {
        "search_query": query,
        "start": start,
        "max_results": max_results,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }
    url = f"{BASE_URL}?{urllib.parse.urlencode(params)}"
    print(f"  Fetching: {url}")

    try:
        req = urllib.request.Request(url, headers={"User-Agent": "NetResearch/1.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read().decode("utf-8")
    except Exception as e:
        print(f"  ERROR: {e}")
        return [], 0

    root = ET.fromstring(data)
    total_results = int(
        root.find(".//atom:totalResults", NS).text
        if root.find(".//atom:totalResults", NS) is not None
        else "0"
    )

    papers = []
    for entry in root.findall("atom:entry", NS):
        paper = parse_entry(entry)
        if paper:
            papers.append(paper)

    return papers, total_results


def parse_entry(entry: ET.Element) -> dict | None:
    """Parse an Atom entry into our intermediate format."""
    title_el = entry.find("atom:title", NS)
    title = title_el.text.strip() if title_el is not None and title_el.text else ""
    # Normalize: remove newlines and extra spaces
    title = " ".join(title.split())

    # Get authors
    authors = []
    nvidia_authors = []
    non_nvidia_affiliations = set()

    for author_el in entry.findall("atom:author", NS):
        name_el = author_el.find("atom:name", NS)
        name = name_el.text.strip() if name_el is not None and name_el.text else ""

        affiliations = []
        for aff_el in author_el.findall("arxiv:affiliation", NS):
            aff = aff_el.text.strip() if aff_el.text else ""
            if aff:
                affiliations.append(aff)

        author_info = {"name": name, "affiliations": affiliations}
        authors.append(author_info)

        is_nvidia = any("nvidia" in aff.lower() for aff in affiliations)
        if is_nvidia:
            nvidia_authors.append(name)
        else:
            for aff in affiliations:
                non_nvidia_affiliations.add(aff)

    if not nvidia_authors:
        return None  # Skip papers without NVIDIA affiliation

    # Get abstract
    summary_el = entry.find("atom:summary", NS)
    abstract = summary_el.text.strip() if summary_el is not None and summary_el.text else ""
    abstract = " ".join(abstract.split())

    # Get arXiv ID
    id_el = entry.find("atom:id", NS)
    arxiv_url = id_el.text.strip() if id_el is not None and id_el.text else ""
    arxiv_id = ""
    if "arxiv.org/abs/" in arxiv_url:
        arxiv_id = arxiv_url.split("arxiv.org/abs/")[-1]
        if "v" in arxiv_id:
            # Strip version
            pass  # Keep version in ID for now, strip later if needed

    # Get published date
    published_el = entry.find("atom:published", NS)
    published = published_el.text[:7] if published_el is not None and published_el.text else ""  # YYYY-MM

    # Get categories
    categories = [
        cat.get("term", "")
        for cat in entry.findall("atom:category", NS)
        if cat.get("term")
    ]

    # Get DOI if present
    doi = ""
    for link_el in entry.findall("atom:link", NS):
        if link_el.get("title") == "doi":
            doi = link_el.get("href", "")

    return {
        "raw_title": title,
        "arxiv_id": arxiv_id.split("v")[0],  # strip version
        "arxiv_id_full": arxiv_id,
        "published": published,
        "year": int(published[:4]) if published else 0,
        "authors": authors,
        "nvidia_authors": nvidia_authors,
        "academic_affiliations": sorted(non_nvidia_affiliations),
        "abstract": abstract,
        "categories": categories,
        "doi": doi,
        "url": f"https://arxiv.org/abs/{arxiv_id.split('v')[0]}",
    }


def fetch_year(year: int, max_per_year: int = 500) -> list[dict]:
    """Fetch NVIDIA papers for a specific year from arXiv."""
    all_papers = []
    seen_ids = set()

    for cat in CATEGORIES:
        # Search for NVIDIA in any field within category + year
        query = f"cat:{cat} AND all:nvidia AND submittedDate:[{year}01010000 TO {year}12312359]"
        start = 0
        batch_size = 100

        while start < max_per_year:
            papers, total = search_arxiv(query, start=start, max_results=batch_size)
            if not papers:
                break

            new_count = 0
            for p in papers:
                aid = p["arxiv_id"]
                if aid and aid not in seen_ids:
                    seen_ids.add(aid)
                    all_papers.append(p)
                    new_count += 1

            print(f"    cat={cat} start={start}: got {len(papers)} results, {new_count} new (total so far: {len(all_papers)})")
            start += batch_size
            time.sleep(0.5)  # Rate limiting

            if len(papers) < batch_size:
                break

        time.sleep(0.3)

    return all_papers


def main():
    all_papers = []

    for year in range(2020, 2027):
        print(f"\n{'='*60}")
        print(f"Fetching year {year}...")
        papers = fetch_year(year)
        print(f"Year {year}: found {len(papers)} NVIDIA-affiliated papers")
        all_papers.extend(papers)
        time.sleep(1)

    print(f"\n{'='*60}")
    print(f"Total: {len(all_papers)} NVIDIA-affiliated papers from arXiv (2020-2026)")

    # Save results
    output = {
        "source": "arXiv API",
        "fetch_date": time.strftime("%Y-%m-%d"),
        "years": "2020-2026",
        "total_count": len(all_papers),
        "papers": all_papers,
    }

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"Results saved to {OUTPUT_FILE}")

    # Print year distribution
    year_counts = {}
    for p in all_papers:
        y = p["year"]
        year_counts[y] = year_counts.get(y, 0) + 1
    print("\nYear distribution:")
    for y in sorted(year_counts):
        print(f"  {y}: {year_counts[y]}")


if __name__ == "__main__":
    main()
