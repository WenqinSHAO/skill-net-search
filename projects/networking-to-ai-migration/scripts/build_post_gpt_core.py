#!/usr/bin/env python3
"""Build the post-GPT core cohort (2023-2026) and cross-reference with core-99.

Selects researchers with >=7 top-networking papers in 2023-2026, then splits into:
  - stayers: in both core-99 (2018-2022) and post-GPT core (2023-2026)
  - newcomers: in post-GPT core only (not in core-99)
  - dropouts: in core-99 only (fell below threshold in 2023-2026)

Also fetches paper-level data for venue topic analysis (Workstream A).

Uses two data sources:
  1. researcher_itineraries.json for the broad cohort (3,571 researchers with >=1
     top-networking paper in 2018-2022). Captures stayers + rising stars within the
     known cohort.
  2. DBLP TOC API for 2023-2026 to find complete newcomers (researchers with 0
     top-networking papers in 2018-2022 but >=7 in 2023-2026).

Heavy operation: DBLP API calls for 20 venue-years, ~30-45 min on first run.
Progress is checkpointed per venue-year.

Outputs:
  - data/post_gpt_core.json — tripartite split with researcher-level data
  - data/post_gpt_venue_papers.json — paper-level data for venue topic analysis
"""

import json
import subprocess
import time
import random
import sys
from pathlib import Path
from collections import Counter, defaultdict

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

OUTPUT_CORE = DATA_DIR / "post_gpt_core.json"
OUTPUT_PAPERS = DATA_DIR / "post_gpt_venue_papers.json"
PROGRESS_FILE = DATA_DIR / "post_gpt_core_progress.json"

# Post-GPT baseline period
POST_GPT_YEARS = list(range(2023, 2027))  # 2023-2026

# Baseline years for cross-reference (use existing data, not re-fetched)
BASELINE_YEARS = list(range(2018, 2023))

# Same qualifying venues as core-99
VENUES = [
    {"name": "SIGCOMM", "toc_prefix": "db/conf/sigcomm/sigcomm"},
    {"name": "NSDI", "toc_prefix": "db/conf/nsdi/nsdi"},
    {"name": "CoNEXT", "toc_prefix": "db/conf/conext/conext"},
    {"name": "HotNets", "toc_prefix": "db/conf/hotnets/hotnets"},
    {"name": "IMC", "toc_prefix": "db/conf/imc/imc"},
]

# Same threshold as core-99: >6 means >=7
THRESHOLD = 7


def fetch_venue_year_papers(venue_name: str, year: int, toc_prefix: str) -> list[dict]:
    """Fetch all papers for a venue-year from DBLP TOC API.

    Returns list of {title, year, venue, authors: [{pid, name}]}.
    """
    url = (
        f"https://dblp.org/search/publ/api"
        f"?q=toc%3A{toc_prefix.replace('/', '%2F')}{year}.bht%3A"
        f"&format=json&h=250"
    )
    for attempt in range(5):
        try:
            result = subprocess.run(
                ["curl", "-s", "-S", "--max-time", "60", "--connect-timeout", "15", url],
                capture_output=True, timeout=70,
            )
            data = json.loads(result.stdout)
            hits = data.get("result", {}).get("hits", {})
            total = int(hits.get("@total", 0))
            papers_list = hits.get("hit", [])
            if total > 0 and papers_list:
                results = []
                for p in papers_list:
                    info = p.get("info", {})
                    authors_raw = info.get("authors", {}).get("author", [])
                    if isinstance(authors_raw, dict):
                        authors_raw = [authors_raw]
                    authors = []
                    for a in authors_raw:
                        pid = a.get("@pid", "")
                        name = a.get("text", "")
                        if pid:
                            authors.append({"pid": pid, "name": name})
                    results.append({
                        "title": info.get("title", "").rstrip("."),
                        "venue": info.get("venue", venue_name),
                        "year": int(info.get("year", year)),
                        "authors": authors,
                        "dblp_url": info.get("url", ""),
                    })
                return results
            time.sleep(10 * (2 ** attempt) + random.uniform(0, 5))
        except Exception as e:
            print(f"  Attempt {attempt + 1}: {e}", file=sys.stderr)
            time.sleep(10 * (2 ** attempt) + random.uniform(0, 5))
    return []


def load_progress() -> dict:
    if PROGRESS_FILE.exists():
        with open(PROGRESS_FILE) as f:
            return json.load(f)
    return {"completed_venue_years": []}


def save_progress(progress: dict):
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=2)


def compute_top_networking_from_itineraries(itineraries_data: dict, years: list[str]) -> dict:
    """Compute per-PID top-networking paper counts from itineraries for given years."""
    qualifying_venues = {v["name"] for v in VENUES}
    pid_counts = defaultdict(int)
    for r in itineraries_data.get("researchers", []):
        pid = r.get("dblp_pid", "")
        if not pid:
            continue
        itinerary = r.get("itinerary", {})
        for year in years:
            for paper in itinerary.get(str(year), []):
                venue = paper.get("venue", "").strip()
                if venue in qualifying_venues:
                    pid_counts[pid] += 1
    return pid_counts


def main():
    print("=" * 60)
    print("Post-GPT Core Builder: 2023-2026 Top-Networking Cohort")
    print("=" * 60)
    print()
    print(f"Selection: >= {THRESHOLD} papers at 5 qualifying venues")
    print(f"Post-GPT period: {POST_GPT_YEARS[0]}-{POST_GPT_YEARS[-1]}")
    print(f"Also fetching {BASELINE_YEARS[0]}-{BASELINE_YEARS[-1]} for venue topic analysis")
    print()

    # ── Load existing data ──
    print("Loading existing data...")

    # Core-99 attributes
    with open(DATA_DIR / "core99_researcher_attributes.json") as f:
        core99_data = json.load(f)
    core99_pids = set()
    core99_by_pid = {}
    for r in core99_data["researchers"]:
        pid = r.get("dblp_pid", "")
        if pid:
            core99_pids.add(pid)
            core99_by_pid[pid] = r

    # Researcher itineraries (broad cohort, 3571 researchers)
    with open(DATA_DIR / "researcher_itineraries.json") as f:
        itineraries_data = json.load(f)

    qualifying_venues = {v["name"] for v in VENUES}

    # ── Step 1: Identify post-GPT core from broad cohort ──
    print("Computing post-2023 top-networking counts from itineraries...")
    pid_post_counts = compute_top_networking_from_itineraries(
        itineraries_data, [str(y) for y in POST_GPT_YEARS]
    )

    # Build name lookup from itineraries
    pid_name = {}
    pid_baseline_count = {}
    for r in itineraries_data.get("researchers", []):
        pid = r.get("dblp_pid", "")
        if pid:
            pid_name[pid] = r.get("name", "Unknown")
            pid_baseline_count[pid] = r.get("baseline_top_networking_count", 0)

    # ── Step 2: Load 2018-2022 venue data from existing cache ──
    print("\nLoading 2018-2022 venue papers from raw_dblp_papers.json...")
    all_papers_by_year_venue = defaultdict(lambda: defaultdict(list))

    with open(DATA_DIR / "raw_dblp_papers.json") as f:
        raw_papers = json.load(f)

    for p in raw_papers:
        year = str(p.get("year", ""))
        venue = p.get("venue", "")
        if venue in qualifying_venues and int(year) in BASELINE_YEARS:
            all_papers_by_year_venue[year][venue].append({
                "title": p.get("title", "").rstrip("."),
                "venue": venue,
                "year": int(year),
                "authors": p.get("authors", []),
                "dblp_url": p.get("dblp_url", ""),
            })

    baseline_paper_count = sum(
        len(papers) for year_data in all_papers_by_year_venue.values()
        for papers in year_data.values()
    )
    print(f"  Loaded {baseline_paper_count} papers from 2018-2022 cache")

    # ── Step 3: Fetch 2023-2026 venue papers (for complete newcomers + topic analysis) ──
    print("\nFetching 2023-2026 venue-year papers from DBLP TOC API...")
    progress = load_progress()
    completed = set(tuple(p) for p in progress.get("completed_venue_years", []))

    # Author PID counts from DBLP TOC (independent of itineraries)
    dblp_pid_post_counts = defaultdict(int)
    # Also compute DBLP baseline counts from raw data
    dblp_pid_baseline_counts = defaultdict(int)
    for year_str, venues in all_papers_by_year_venue.items():
        for venue_name, papers in venues.items():
            for p in papers:
                for a in p.get("authors", []):
                    pid = a.get("pid", "")
                    if pid:
                        dblp_pid_baseline_counts[pid] += 1

    for venue in VENUES:
        name = venue["name"]
        for year in POST_GPT_YEARS:
            key = (name, str(year))
            if key in completed:
                print(f"  {name} {year}: already fetched, skipping")
                continue

            print(f"  {name} {year}: fetching...", end=" ", flush=True)
            papers = fetch_venue_year_papers(name, year, venue["toc_prefix"])
            count = len(papers)
            print(f"{count} papers")

            all_papers_by_year_venue[str(year)][name] = papers

            # Count per-author PIDs for post-GPT years
            for p in papers:
                for a in p["authors"]:
                    pid = a["pid"]
                    if pid:
                        dblp_pid_post_counts[pid] += 1

            completed.add(key)
            progress["completed_venue_years"] = sorted(
                list([str(k[0]), str(k[1])] for k in completed)
            )
            save_progress(progress)
            time.sleep(2 + random.uniform(0, 2))

    # ── Step 3: Identify complete newcomers not in broad cohort ──
    print("\nIdentifying complete newcomers...")
    # Get all PIDs from itineraries
    itinerary_pids = set()
    for r in itineraries_data.get("researchers", []):
        pid = r.get("dblp_pid", "")
        if pid:
            itinerary_pids.add(pid)

    complete_newcomer_pids = set()
    for pid, count in dblp_pid_post_counts.items():
        if count >= THRESHOLD and pid not in itinerary_pids:
            complete_newcomer_pids.add(pid)

    print(f"  Complete newcomers (not in broad cohort): {len(complete_newcomer_pids)}")

    # Get names for complete newcomers from DBLP papers
    newcomer_name = {}
    for year_str, venues in all_papers_by_year_venue.items():
        if int(year_str) not in POST_GPT_YEARS:
            continue
        for venue_name, papers in venues.items():
            for p in papers:
                for a in p["authors"]:
                    if a["pid"] in complete_newcomer_pids:
                        if a["pid"] not in newcomer_name:
                            newcomer_name[a["pid"]] = a["name"]

    # Verify: complete newcomers should have 0 baseline papers by definition
    # (they weren't in the broad cohort, so no 2018-2022 top-networking papers)
    for pid in complete_newcomer_pids:
        bl = dblp_pid_baseline_counts.get(pid, 0)
        if bl > 0:
            print(f"  WARNING: {newcomer_name.get(pid, pid)} has {bl} baseline papers but not in broad cohort")

    # ── Step 4: Build the tripartite split ──
    print("\nBuilding tripartite split...")

    # All PIDs with >=7 post-2023 papers (from both sources)
    all_post_core_pids = set()
    for pid, count in pid_post_counts.items():
        if count >= THRESHOLD:
            all_post_core_pids.add(pid)
    all_post_core_pids |= complete_newcomer_pids

    # Get final post count for each researcher
    def get_post_count(pid):
        itinerary_count = pid_post_counts.get(pid, 0)
        dblp_count = dblp_pid_post_counts.get(pid, 0)
        return max(itinerary_count, dblp_count)  # Use the higher count

    def get_baseline_count(pid):
        itinerary_bl = pid_baseline_count.get(pid, 0)
        dblp_bl = dblp_pid_baseline_counts.get(pid, 0)
        return max(itinerary_bl, dblp_bl)

    def get_name(pid):
        if pid in pid_name:
            return pid_name[pid]
        if pid in core99_by_pid:
            return core99_by_pid[pid].get("name", "Unknown")
        if pid in newcomer_name:
            return newcomer_name[pid]
        return "Unknown"

    stayers = []
    newcomers = []
    for pid in all_post_core_pids:
        post_count = get_post_count(pid)
        bl_count = get_baseline_count(pid)
        entry = {
            "dblp_pid": pid,
            "name": get_name(pid),
            "baseline_top_networking_count": bl_count,
            "post_top_networking_count": post_count,
            "in_core99": pid in core99_pids,
            "in_broad_cohort": pid in itinerary_pids,
            "source": "itineraries" if pid in itinerary_pids else "dblp_toc",
        }
        if pid in core99_pids:
            stayers.append(entry)
        else:
            newcomers.append(entry)

    # Sort by post count descending
    stayers.sort(key=lambda x: -x["post_top_networking_count"])
    newcomers.sort(key=lambda x: -x["post_top_networking_count"])

    # Dropouts: core-99 researchers NOT in post-GPT core
    dropouts = []
    for pid in core99_pids:
        if pid not in all_post_core_pids:
            r = core99_by_pid[pid]
            dropouts.append({
                "dblp_pid": pid,
                "name": r.get("name", "Unknown"),
                "baseline_top_networking_count": r.get("baseline_top_networking_count", 0),
                "post_top_networking_count": r.get("post2023_top_networking_count", 0),
                "in_core99": True,
                "in_broad_cohort": True,
                "source": "core99_attributes",
            })
    dropouts.sort(key=lambda x: -x["post_top_networking_count"])

    print(f"\n  Stayers (in both cores): {len(stayers)}")
    print(f"  Newcomers (post-GPT core only): {len(newcomers)}")
    print(f"  Dropouts (core-99 only): {len(dropouts)}")
    print(f"  Total post-GPT core: {len(stayers) + len(newcomers)}")
    print(f"  Total core-99: {len(stayers) + len(dropouts)}")

    # Verification
    assert len(stayers) + len(dropouts) == 99, \
        f"Expected 99 core-99 researchers, got {len(stayers) + len(dropouts)}"
    print("  ✓ Core-99 integrity check passed")

    # ── Step 5: Save paper-level data for venue topic analysis ──
    print("\nSaving venue paper data for topic analysis...")
    # Flatten papers for output
    venue_papers = []
    for year_str in sorted(all_papers_by_year_venue.keys()):
        for venue_name in sorted(all_papers_by_year_venue[year_str].keys()):
            papers = all_papers_by_year_venue[year_str][venue_name]
            for p in papers:
                venue_papers.append({
                    "title": p["title"],
                    "venue": venue_name,
                    "year": int(year_str),
                    "authors": p["authors"],
                    "dblp_url": p.get("dblp_url", ""),
                })

    with open(OUTPUT_PAPERS, "w") as f:
        json.dump({
            "metadata": {
                "phase": "build_post_gpt_core",
                "venues": [v["name"] for v in VENUES],
                "years_fetched": f"{POST_GPT_YEARS[0]}-{POST_GPT_YEARS[-1]}",
                "baseline_from_cache": f"{BASELINE_YEARS[0]}-{BASELINE_YEARS[-1]}",
                "total_papers": len(venue_papers),
            },
            "papers": venue_papers,
        }, f, indent=2, ensure_ascii=False)
    print(f"  Wrote {len(venue_papers)} papers to {OUTPUT_PAPERS}")

    # ── Step 6: Save post-GPT core output ──
    print("\nSaving post-GPT core data...")
    output = {
        "metadata": {
            "description": (
                "Post-GPT core cohort: researchers with >=7 papers at 5 qualifying "
                "networking venues during 2023-2026. Cross-referenced with 2018-2022 "
                "core-99 to produce stayers/newcomers/dropouts tripartite split."
            ),
            "selection_threshold": THRESHOLD,
            "post_gpt_years": POST_GPT_YEARS,
            "baseline_years": BASELINE_YEARS,
            "qualifying_venues": [v["name"] for v in VENUES],
            "core99_size": 99,
            "post_gpt_core_size": len(stayers) + len(newcomers),
            "complete_newcomers_from_dblp": len(complete_newcomer_pids),
            "generated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        },
        "tripartite_split": {
            "stayers": {
                "description": "Researchers with >=7 top-networking papers in BOTH 2018-2022 and 2023-2026",
                "count": len(stayers),
                "researchers": stayers,
            },
            "newcomers": {
                "description": "Researchers with >=7 top-networking papers in 2023-2026 who were NOT in core-99",
                "count": len(newcomers),
                "researchers": newcomers,
            },
            "dropouts": {
                "description": "Core-99 researchers with <7 top-networking papers in 2023-2026",
                "count": len(dropouts),
                "researchers": dropouts,
            },
        },
        "summary": {
            "stayer_count": len(stayers),
            "newcomer_count": len(newcomers),
            "dropout_count": len(dropouts),
            "newcomers_from_outside_broad_cohort": len(complete_newcomer_pids),
            "newcomers_from_within_broad_cohort": len(newcomers) - len(complete_newcomer_pids),
            "overlap_rate_pct": round(len(stayers) / 99 * 100, 1),
            "renewal_rate_pct": round(len(newcomers) / (len(stayers) + len(newcomers)) * 100, 1),
        },
    }

    with open(OUTPUT_CORE, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"  Wrote {OUTPUT_CORE}")

    # ── Summary ──
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"  Post-GPT core size: {len(stayers) + len(newcomers)}")
    print(f"    Stayers (core-99 ∩ post-GPT): {len(stayers)}")
    print(f"    Newcomers (post-GPT \\ core-99): {len(newcomers)}")
    print(f"      - From within broad cohort: {len(newcomers) - len(complete_newcomer_pids)}")
    print(f"      - Complete newcomers (outside broad cohort): {len(complete_newcomer_pids)}")
    print(f"  Dropouts (core-99 \\ post-GPT): {len(dropouts)}")
    print(f"  Core-99 overlap rate: {len(stayers)/99*100:.1f}%")
    print(f"  Post-GPT core renewal rate: {len(newcomers)/(len(stayers)+len(newcomers))*100:.1f}%")


if __name__ == "__main__":
    main()
