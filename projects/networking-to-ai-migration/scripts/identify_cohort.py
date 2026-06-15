#!/usr/bin/env python3
"""
Phase 1: Identify the qualified cohort of networking researchers.

Queries DBLP for all papers at {SIGCOMM, NSDI, CoNEXT, HotNets, IMC} during
2018–2022, extracts unique authors with their DBLP PIDs, counts papers per
author across the five venues, and filters to those with at least MIN_PAPERS papers.

Uses curl (subprocess) for HTTP — more reliable than Python requests against
DBLP's server, which tends to drop keep-alive connections.

Output: data/qualified_cohort.json
"""

import json
import time
import sys
import random
import subprocess
from pathlib import Path
from collections import defaultdict
from urllib.parse import urlencode

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

QUALIFYING_VENUES = ["SIGCOMM", "NSDI", "CoNEXT", "HotNets", "IMC"]
BASELINE_START = 2018
BASELINE_END = 2022
MIN_PAPERS = 1

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
OUTPUT_FILE = DATA_DIR / "qualified_cohort.json"
RAW_CACHE_FILE = DATA_DIR / "raw_dblp_papers.json"
PROGRESS_FILE = DATA_DIR / "fetch_progress.json"

DBLP_SEARCH_URL = "https://dblp.org/search/publ/api"
BASE_DELAY = 4.0       # seconds between requests
JITTER = 2.0            # random jitter
HITS_PER_PAGE = 250
MAX_RETRIES = 5
BACKOFF_BASE = 10       # seconds — exponential backoff base


# ---------------------------------------------------------------------------
# DBLP client via curl subprocess
# ---------------------------------------------------------------------------

def _curl_fetch(url: str, timeout: int = 60) -> bytes:
    """Fetch a URL using curl. Returns raw bytes on success, raises on failure."""
    cmd = [
        "curl", "-s", "-S",  # silent, but show errors
        "--max-time", str(timeout),
        "--connect-timeout", "15",
        "-H", "Accept: application/json",
        "-H", "User-Agent: networking-to-ai-migration/1.0 (academic research)",
        url,
    ]
    result = subprocess.run(cmd, capture_output=True, timeout=timeout + 10)
    if result.returncode != 0:
        stderr = result.stderr.decode("utf-8", errors="replace").strip()
        raise OSError(f"curl exited {result.returncode}: {stderr}")
    return result.stdout


def search_venue_year(venue: str, year: int, first: int = 0,
                      hits: int = HITS_PER_PAGE) -> dict:
    """Search DBLP for papers at a venue in a given year. Returns parsed JSON."""
    query = f"venue:{venue}:year:{year}:"
    params = {"q": query, "format": "json", "h": hits, "f": first}
    url = f"{DBLP_SEARCH_URL}?{urlencode(params)}"

    for attempt in range(MAX_RETRIES):
        try:
            raw = _curl_fetch(url)
            data = json.loads(raw)
            return data
        except (OSError, json.JSONDecodeError) as e:
            wait = BACKOFF_BASE * (2 ** attempt) + random.uniform(0, 3)
            print(f"  Attempt {attempt+1}/{MAX_RETRIES} for {venue} {year}: {e}",
                  file=sys.stderr)
            print(f"  Waiting {wait:.0f}s...", file=sys.stderr)
            time.sleep(wait)

    raise RuntimeError(f"Failed to fetch {venue} {year} after {MAX_RETRIES} retries")


def fetch_all_papers(venue: str, year: int) -> list[dict]:
    """Fetch all papers for a venue-year, handling pagination."""
    all_papers = []
    first = 0
    total = None

    while True:
        data = search_venue_year(venue, year, first=first)
        hits = data.get("result", {}).get("hits", {})
        if total is None:
            total = int(hits.get("@total", 0))
            if total == 0:
                print(f"  {venue} {year}: 0 papers (empty)")
                break
            print(f"  {venue} {year}: {total} papers", flush=True)

        paper_list = hits.get("hit", [])
        if not paper_list:
            break

        all_papers.extend(paper_list)
        first += len(paper_list)

        if first >= total:
            break

        # Polite delay between paginated requests
        time.sleep(BASE_DELAY + random.uniform(0, JITTER))

    return all_papers


# ---------------------------------------------------------------------------
# Author extraction
# ---------------------------------------------------------------------------

def extract_authors(paper: dict) -> list[dict]:
    """Extract author list from a DBLP paper hit. Returns list of {pid, name}."""
    info = paper.get("info", {})
    authors = info.get("authors", {})
    author_list = authors.get("author", [])

    if isinstance(author_list, dict):
        author_list = [author_list]

    result = []
    for a in author_list:
        pid = a.get("@pid", "")
        name = a.get("text", "")
        if pid and name:
            result.append({"pid": pid, "name": name})
        elif name:
            result.append({"pid": f"name:{name}", "name": name})

    return result


def extract_paper_info(paper: dict) -> dict:
    """Extract minimal paper info from a DBLP paper hit."""
    info = paper.get("info", {})
    return {
        "title": info.get("title", "").rstrip("."),
        "venue": info.get("venue", ""),
        "year": int(info.get("year", 0)),
        "dblp_url": info.get("url", ""),
        "doi": info.get("doi", ""),
    }


# ---------------------------------------------------------------------------
# Resume / progress tracking
# ---------------------------------------------------------------------------

def load_progress() -> dict[str, list[int]]:
    """Load fetch progress: {venue: [years_done]}."""
    if PROGRESS_FILE.exists():
        with open(PROGRESS_FILE) as f:
            return json.load(f)
    return {}


def save_progress(progress: dict):
    """Save fetch progress to disk."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=2)


def load_raw_cache() -> list[dict]:
    """Load previously fetched papers from cache."""
    if RAW_CACHE_FILE.exists():
        with open(RAW_CACHE_FILE) as f:
            return json.load(f)
    return []


def append_to_raw_cache(new_papers: list[dict]):
    """Append new papers to the raw cache file."""
    existing = load_raw_cache()
    existing.extend(new_papers)
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(RAW_CACHE_FILE, "w") as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def fetch_all_qualifying_papers() -> list[dict]:
    """Fetch all papers with resume support."""
    progress = load_progress()
    all_papers = load_raw_cache()

    total_combos = len(QUALIFYING_VENUES) * (BASELINE_END - BASELINE_START + 1)
    done_combos = sum(len(v) for v in progress.values())
    print(f"Resume state: {done_combos}/{total_combos} venue-years already fetched\n")

    for venue in QUALIFYING_VENUES:
        done_years = set(progress.get(venue, []))
        for year in range(BASELINE_START, BASELINE_END + 1):
            if year in done_years:
                print(f"  {venue} {year}: skipping (already fetched)")
                continue

            try:
                papers = fetch_all_papers(venue, year)
                extracted = []
                for p in papers:
                    paper_info = extract_paper_info(p)
                    paper_info["authors"] = extract_authors(p)
                    extracted.append(paper_info)
                    all_papers.append(paper_info)

                append_to_raw_cache(extracted)
                if venue not in progress:
                    progress[venue] = []
                progress[venue].append(year)
                save_progress(progress)
                print(f"  → saved {len(extracted)} papers "
                      f"(cumulative: {len(all_papers)})", flush=True)

            except RuntimeError as e:
                print(f"\n  ERROR: {e}", file=sys.stderr)
                print("  Progress saved. Re-run to resume from here.",
                      file=sys.stderr)
                sys.exit(1)

    return all_papers


def build_author_index(papers: list[dict]) -> dict[str, dict]:
    """Build per-author paper counts keyed by DBLP PID."""
    author_index: dict[str, dict] = defaultdict(lambda: {
        "dblp_pid": "",
        "name": "",
        "paper_count": 0,
        "papers": [],
        "venues_seen": set(),
    })

    for paper in papers:
        for author in paper.get("authors", []):
            pid = author["pid"]
            entry = author_index[pid]
            entry["dblp_pid"] = pid
            entry["name"] = author["name"]
            entry["paper_count"] += 1
            entry["papers"].append({
                "title": paper["title"],
                "venue": paper["venue"],
                "year": paper["year"],
                "dblp_url": paper["dblp_url"],
            })
            entry["venues_seen"].add(paper["venue"])

    for entry in author_index.values():
        entry["venues_seen"] = sorted(entry["venues_seen"])

    return dict(author_index)


def filter_qualified(author_index: dict[str, dict]) -> list[dict]:
    """Filter to authors with ≥ MIN_PAPERS papers."""
    return [e for e in author_index.values() if e["paper_count"] >= MIN_PAPERS]


def run():
    """Run the full Phase 1 pipeline."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("Phase 1: Identify Qualified Networking Researcher Cohort")
    print("=" * 60)
    print(f"Qualifying venues: {QUALIFYING_VENUES}")
    print(f"Baseline period: {BASELINE_START}–{BASELINE_END}")
    print(f"Minimum papers: {MIN_PAPERS}")
    print()

    # Step 1: Fetch
    print("Step 1: Fetching all qualifying papers from DBLP...")
    print("(Progress saved after each venue-year. Interrupt-safe.)\n")
    all_papers = fetch_all_qualifying_papers()
    print(f"\nTotal papers fetched: {len(all_papers)}")

    # Step 2: Author index
    print("\nStep 2: Building author index...")
    author_index = build_author_index(all_papers)
    print(f"Unique authors found: {len(author_index)}")

    # Step 3: Filter
    print(f"\nStep 3: Filtering to authors with ≥{MIN_PAPERS} papers...")
    qualified = filter_qualified(author_index)
    print(f"Qualified researchers: {len(qualified)}")

    # Step 4: Sort & rank
    qualified.sort(key=lambda x: x["paper_count"], reverse=True)
    for i, entry in enumerate(qualified):
        entry["rank"] = i + 1

    # Step 5: Save
    output = {
        "metadata": {
            "phase": "identify_cohort",
            "qualifying_venues": QUALIFYING_VENUES,
            "baseline_start": BASELINE_START,
            "baseline_end": BASELINE_END,
            "min_papers": MIN_PAPERS,
            "total_papers_fetched": len(all_papers),
            "total_authors_found": len(author_index),
            "qualified_count": len(qualified),
        },
        "researchers": qualified,
    }

    with open(OUTPUT_FILE, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"\nOutput saved to {OUTPUT_FILE}")

    # Step 6: Summary
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"Qualified researchers (≥{MIN_PAPERS} paper): {len(qualified)}")

    count_dist = defaultdict(int)
    for entry in qualified:
        count_dist[entry["paper_count"]] += 1
    print("\nPapers-per-researcher distribution:")
    for count in sorted(count_dist, reverse=True):
        bar = "█" * min(count_dist[count], 80)
        print(f"  {count:2d} papers: {count_dist[count]:3d} researchers {bar}")

    print("\nTop 25 most prolific researchers:")
    for entry in qualified[:25]:
        venues = ", ".join(entry["venues_seen"])
        print(f"  {entry['rank']:3d}. {entry['name']:<45s} "
              f"{entry['paper_count']:2d} papers  [{venues}]")

    return qualified


if __name__ == "__main__":
    run()
