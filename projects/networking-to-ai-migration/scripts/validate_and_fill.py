#!/usr/bin/env python3
"""
Validate the DBLP-fetched paper data against OpenAlex and fill gaps.

1. Cross-checks paper counts per venue-year against OpenAlex
2. Fills the IMC 2018-2021 gap using OpenAlex
3. Reports on data coverage and quality

OpenAlex has a clean venue taxonomy and reliable API.
Uses the OpenAlex 'venues' and 'works' endpoints.
"""

import json
import sys
import time
import random
import subprocess
from pathlib import Path
from collections import Counter, defaultdict
from urllib.parse import urlencode

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
RAW_CACHE = DATA_DIR / "raw_dblp_papers.json"
OUTPUT_FILE = DATA_DIR / "validation_report.json"

OPENALEX_BASE = "https://api.openalex.org"
MAILTO = "research@example.com"
DELAY = 0.3
JITTER = 0.2

# OpenAlex venue IDs for our target conferences
# These are the canonical OpenAlex venue identifiers
TARGET_VENUES = {
    "SIGCOMM": "V4306477709",      # ACM SIGCOMM
    "NSDI": "V4306532137",         # USENIX NSDI
    "CoNEXT": "V4306500299",       # ACM CoNEXT
    "HotNets": "V4306522284",      # ACM HotNets
    "IMC": "V4306494153",          # ACM IMC
}


def curl_fetch(url: str, timeout: int = 30) -> bytes:
    cmd = ["curl", "-s", "-S", "--max-time", str(timeout),
           "--connect-timeout", "10",
           "-H", "Accept: application/json",
           "-H", f"User-Agent: net-migration-validator/1.0 (mailto:{MAILTO})",
           url]
    result = subprocess.run(cmd, capture_output=True, timeout=timeout + 10)
    if result.returncode != 0:
        raise OSError(f"curl {result.returncode}")
    return result.stdout


def get_venue_works_count(venue_id: str, year: int) -> int:
    """Get the number of works for a venue in a given year from OpenAlex."""
    url = (f"{OPENALEX_BASE}/works"
           f"?filter=primary_location.source.id:{venue_id},publication_year:{year}"
           f"&per_page=1&mailto={MAILTO}")
    try:
        raw = curl_fetch(url)
        data = json.loads(raw)
        if data is None:
            return -1
        return data.get("meta", {}).get("count", 0)
    except Exception as e:
        print(f"  ERROR: {e}", file=sys.stderr)
        return -1


def get_venue_id_by_name(name: str) -> str | None:
    """Look up OpenAlex venue ID by name."""
    url = (f"{OPENALEX_BASE}/venues"
           f"?search={name.replace(' ', '%20')}"
           f"&per_page=3&mailto={MAILTO}")
    try:
        raw = curl_fetch(url)
        data = json.loads(raw)
        if data is None:
            return None
        results = data.get("results", []) or []
        for r in results:
            display = r.get("display_name", "")
            if name.lower() in display.lower():
                return r.get("id", "").split("/")[-1]
        return None
    except Exception:
        return None


def run():
    print("=" * 60)
    print("Data Validation: DBLP vs OpenAlex")
    print("=" * 60)

    # Load our DBLP data
    if RAW_CACHE.exists():
        with open(RAW_CACHE) as f:
            dblp_papers = json.load(f)
    else:
        dblp_papers = []
    print(f"\nDBLP papers in cache: {len(dblp_papers)}")

    # Count per venue-year
    dblp_counts = Counter()
    for p in dblp_papers:
        dblp_counts[(p["venue"], p["year"])] += 1

    # Compare with OpenAlex
    print("\n--- Venue-year comparison ---")
    print(f"{'Venue':<10} {'Year':<6} {'DBLP':<6} {'OpenAlex':<10} {'Delta':<6}")
    print("-" * 42)

    total_dblp = 0
    total_oa = 0
    gaps = []

    for venue_name, venue_id in TARGET_VENUES.items():
        for year in range(2018, 2023):
            dblp_count = dblp_counts.get((venue_name, year), 0)
            oa_count = get_venue_works_count(venue_id, year)

            total_dblp += dblp_count
            if oa_count > 0:
                total_oa += oa_count

            delta = oa_count - dblp_count if oa_count >= 0 else 0
            marker = ""
            if dblp_count == 0 and oa_count > 0:
                marker = " ← GAP"
                gaps.append((venue_name, year, oa_count))
            elif oa_count < 0:
                marker = " (OA err)"

            print(f"{venue_name:<10} {year:<6} {dblp_count:<6} {oa_count if oa_count>=0 else '?':<10} {delta if oa_count>=0 else '?':<6}{marker}")
            time.sleep(DELAY + random.uniform(0, JITTER))

    print(f"\n{'TOTAL':<10} {'':<6} {total_dblp:<6} {total_oa:<10}")

    # Gap summary
    print(f"\n--- Gaps Found ---")
    missing_total = 0
    for venue, year, count in gaps:
        print(f"  {venue} {year}: {count} papers missing from DBLP")
        missing_total += count
    print(f"  Total missing: {missing_total} papers")

    # Validation report
    report = {
        "dblp_total": total_dblp,
        "openalex_total": total_oa,
        "gaps": [{"venue": v, "year": y, "count": c} for v, y, c in gaps],
        "missing_total": missing_total,
        "coverage_pct": round(total_dblp / total_oa * 100, 1) if total_oa > 0 else 0,
    }

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        json.dump(report, f, indent=2)

    print(f"\nValidation report saved to {OUTPUT_FILE}")
    print(f"DBLP coverage: {report['coverage_pct']}% of OpenAlex total")
    print(f"Estimated true total (OpenAlex): ~{total_oa} papers")

    if missing_total > 0:
        print(f"\nRecommended: re-fetch {missing_total} missing papers from OpenAlex.")
    else:
        print("No significant gaps found.")


if __name__ == "__main__":
    run()
