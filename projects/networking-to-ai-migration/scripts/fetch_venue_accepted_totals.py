#!/usr/bin/env python3
"""Fetch total accepted paper counts per qualifying venue per year from DBLP TOC API.

Generalizes the pattern from fill_imc_gap.py to fetch per-venue per-year totals
for SIGCOMM, NSDI, CoNEXT, HotNets, and IMC across 2018-2026.

Only fetches @total counts — does not enumerate individual papers.
Output: data/venue_accepted_totals.json
Progress file: data/fetch_venue_totals_progress.json (for resume on failure)
"""

import json
import subprocess
import time
import random
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
OUTPUT_FILE = DATA_DIR / "venue_accepted_totals.json"
PROGRESS_FILE = DATA_DIR / "fetch_venue_totals_progress.json"

# Venue definitions: canonical name, DBLP TOC key prefix
VENUES = [
    {
        "name": "SIGCOMM",
        "toc_prefix": "db/conf/sigcomm/sigcomm",
        "years": list(range(2018, 2027)),
    },
    {
        "name": "NSDI",
        "toc_prefix": "db/conf/nsdi/nsdi",
        "years": list(range(2018, 2027)),
    },
    {
        "name": "CoNEXT",
        "toc_prefix": "db/conf/conext/conext",
        "years": list(range(2018, 2027)),
    },
    {
        "name": "HotNets",
        "toc_prefix": "db/conf/hotnets/hotnets",
        "years": list(range(2018, 2027)),
    },
    {
        "name": "IMC",
        "toc_prefix": "db/conf/imc/imc",
        "years": list(range(2018, 2027)),
    },
]


def fetch_toc_total(venue_name: str, year: int, toc_prefix: str) -> int | None:
    """Fetch @total from DBLP TOC API for a venue-year. Returns None on failure."""
    url = (
        f"https://dblp.org/search/publ/api"
        f"?q=toc%3A{toc_prefix.replace('/', '%2F')}{year}.bht%3A"
        f"&format=json&h=1"
    )
    for attempt in range(5):
        try:
            result = subprocess.run(
                ["curl", "-s", "-S", "--max-time", "45", "--connect-timeout", "15", url],
                capture_output=True, timeout=55,
            )
            data = json.loads(result.stdout)
            hits = data.get("result", {}).get("hits", {})
            total = int(hits.get("@total", 0))
            if total > 0:
                return total
            # Total is 0 — might mean the venue/year doesn't exist yet
            if total == 0 and year >= 2025:
                return None  # Probably not yet indexed
            time.sleep(8 * (2 ** attempt) + random.uniform(0, 4))
        except Exception as e:
            print(f"  Attempt {attempt + 1}: {e}", file=sys.stderr)
            time.sleep(8 * (2 ** attempt) + random.uniform(0, 4))
    return None  # All retries exhausted


def load_progress() -> dict:
    if PROGRESS_FILE.exists():
        with open(PROGRESS_FILE) as f:
            return json.load(f)
    return {"completed": []}


def save_progress(progress: dict):
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=2)


def main():
    progress = load_progress()
    completed = set(tuple(p) for p in progress.get("completed", []))

    # Load existing output if any
    totals: dict[str, dict[str, int | None]] = {}
    if OUTPUT_FILE.exists():
        with open(OUTPUT_FILE) as f:
            existing = json.load(f)
            totals = existing.get("totals", {})

    for venue in VENUES:
        name = venue["name"]
        for year in venue["years"]:
            key = (name, str(year))
            if key in completed:
                print(f"{name} {year}: already fetched, skipping")
                continue

            year_str = str(year)
            print(f"{name} {year}: fetching...", end=" ", flush=True)
            count = fetch_toc_total(name, year, venue["toc_prefix"])
            if count is not None:
                print(f"{count} papers")
            else:
                print("NOT FOUND (not yet indexed or TOC key mismatch)")

            # Store result
            if year_str not in totals:
                totals[year_str] = {}
            totals[year_str][name] = count

            # Mark complete
            completed.add(key)
            progress["completed"] = sorted(list(completed))
            save_progress(progress)

            # Write output incrementally
            output = {
                "metadata": {
                    "description": "Total accepted papers per qualifying venue per year from DBLP TOC API",
                    "venues": [v["name"] for v in VENUES],
                    "years_fetched": sorted(set(
                        int(y) for y in totals.keys()
                    )),
                    "fetched_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                    "null_means": "Not yet indexed, TOC key mismatch, or fetch failure",
                },
                "totals": totals,
            }
            with open(OUTPUT_FILE, "w") as f:
                json.dump(output, f, indent=2, ensure_ascii=False)

            time.sleep(2 + random.uniform(0, 2))  # Rate limiting between requests

    # Final summary
    print(f"\nDone. Results in {OUTPUT_FILE}")
    for year_s in sorted(totals.keys()):
        print(f"  {year_s}: {totals[year_s]}")


if __name__ == "__main__":
    main()
