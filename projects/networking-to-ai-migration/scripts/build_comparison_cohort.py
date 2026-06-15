#!/usr/bin/env python3
"""Build a comparison cohort for regression-to-the-mean check.

Selects researchers with >=7 top-networking papers in 2013-2017 (same threshold
shifted back 5 years), then examines their output in 2018-2022. Compares the
decline rate to core-99's post-2023 decline rate (49.4% showing decreased rate).

This tests whether selecting high-output researchers and measuring them in a
subsequent period inherently produces a "decline" signal due to regression to
the mean.

Heavy operation: ~500-1000 DBLP API calls, ~30-45 min.
Run as a one-off with: python scripts/build_comparison_cohort.py

Uses the DBLP TOC API pattern from fill_imc_gap.py and fetch_venue_accepted_totals.py.
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

OUTPUT_FILE = DATA_DIR / "comparison_cohort_summary.json"
PROGRESS_FILE = DATA_DIR / "comparison_cohort_progress.json"

# Earlier baseline: 2013-2017, measured against subsequent period: 2018-2022
EARLIER_BASELINE = list(range(2013, 2018))
SUBSEQUENT_PERIOD = list(range(2018, 2023))

# Same qualifying venues
VENUES = [
    {
        "name": "SIGCOMM",
        "toc_prefix": "db/conf/sigcomm/sigcomm",
    },
    {
        "name": "NSDI",
        "toc_prefix": "db/conf/nsdi/nsdi",
    },
    {
        "name": "CoNEXT",
        "toc_prefix": "db/conf/conext/conext",
    },
    {
        "name": "HotNets",
        "toc_prefix": "db/conf/hotnets/hotnets",
    },
    {
        "name": "IMC",
        "toc_prefix": "db/conf/imc/imc",
    },
]

# Threshold: same as core-99 (>=7 papers at qualifying venues in the baseline)
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
            papers = hits.get("hit", [])
            if total > 0 and papers:
                results = []
                for p in papers:
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


def main():
    print("=" * 60)
    print("Comparison Cohort Builder: Regression-to-the-Mean Check")
    print("=" * 60)
    print()
    print(f"Selection: >= {THRESHOLD} papers at 5 qualifying venues")
    print(f"Baseline: {EARLIER_BASELINE[0]}-{EARLIER_BASELINE[-1]}")
    print(f"Subsequent: {SUBSEQUENT_PERIOD[0]}-{SUBSEQUENT_PERIOD[-1]}")
    print()
    print(f"Core-99 decline rate (baseline 2018-2022 -> post 2023-2026): 49.4%")
    print(f"Null hypothesis: similar decline rate expected from regression to mean")
    print()

    progress = load_progress()
    completed = set(tuple(p) for p in progress.get("completed_venue_years", []))

    # Step 1: Fetch all papers for the earlier baseline period
    pid_counts: dict[str, dict[str, int]] = defaultdict(lambda: defaultdict(int))
    # pid_counts[pid] = {"baseline": N, "subsequent": M}

    all_years = sorted(set(EARLIER_BASELINE + SUBSEQUENT_PERIOD))

    for venue in VENUES:
        name = venue["name"]
        for year in all_years:
            key = (name, str(year))
            if key in completed:
                print(f"{name} {year}: already fetched, skipping")
                continue

            print(f"{name} {year}: fetching...", end=" ", flush=True)
            papers = fetch_venue_year_papers(name, year, venue["toc_prefix"])
            count = len(papers)
            print(f"{count} papers")

            for p in papers:
                for a in p["authors"]:
                    pid = a["pid"]
                    if pid:
                        if year in EARLIER_BASELINE:
                            pid_counts[pid]["baseline"] += 1
                        elif year in SUBSEQUENT_PERIOD:
                            pid_counts[pid]["subsequent"] += 1

            completed.add(key)
            progress["completed_venue_years"] = sorted(
                list(str(k) for k in completed)
            )
            save_progress(progress)
            time.sleep(2 + random.uniform(0, 2))

    # Step 2: Select comparison cohort
    comparison_pids = [
        pid for pid, counts in pid_counts.items()
        if counts.get("baseline", 0) >= THRESHOLD
    ]
    print(f"\nComparison cohort size: {len(comparison_pids)}")
    print(f"  (core-99 size for reference: 99)")

    # Step 3: Compute subsequent-period output
    decreased = 0
    flat = 0
    increased = 0
    inactive = 0
    ratios = []

    for pid in comparison_pids:
        bl = pid_counts[pid].get("baseline", 0)
        sub = pid_counts[pid].get("subsequent", 0)

        # Annualized rate ratio (same formula as core-99)
        bl_rate = bl / len(EARLIER_BASELINE)  # /5
        sub_rate = sub / len(SUBSEQUENT_PERIOD) if sub > 0 else 0  # /5
        ratio = sub_rate / bl_rate if bl_rate > 0 else None

        if ratio is not None:
            ratios.append(ratio)
            if sub == 0:
                inactive += 1
            elif ratio >= 1.25:
                increased += 1
            elif ratio <= 0.75:
                decreased += 1
            else:
                flat += 1
        else:
            inactive += 1

    total = len(comparison_pids)
    dec_rate = decreased / total * 100 if total > 0 else 0
    dec_or_inactive_rate = (decreased + inactive) / total * 100 if total > 0 else 0

    print(f"\nSubsequent period (2018-2022) rate change distribution:")
    print(f"  Decreased: {decreased} ({dec_rate:.1f}%)")
    print(f"  Flat: {flat} ({flat/total*100:.1f}%)" if total > 0 else "  Flat: 0")
    print(f"  Increased: {increased} ({increased/total*100:.1f}%)" if total > 0 else "  Increased: 0")
    print(f"  Inactive (sub=0): {inactive} ({inactive/total*100:.1f}%)" if total > 0 else "  Inactive: 0")

    print(f"\nComparison with core-99:")
    print(f"  Core-99 decline rate: 49.4% (43/87 analyzable)")
    print(f"  Comparison cohort decline rate: {dec_rate:.1f}% ({decreased}/{total})")
    print(f"  Comparison cohort decline+inactive rate: {dec_or_inactive_rate:.1f}% ({decreased + inactive}/{total})")

    # Step 4: Output
    output = {
        "metadata": {
            "description": (
                "Comparison cohort for regression-to-the-mean check. "
                f"Selects researchers with >= {THRESHOLD} papers at 5 qualifying venues "
                f"during {EARLIER_BASELINE[0]}-{EARLIER_BASELINE[-1]}, "
                f"then measures output during {SUBSEQUENT_PERIOD[0]}-{SUBSEQUENT_PERIOD[-1]}."
            ),
            "selection_threshold": THRESHOLD,
            "baseline_years": EARLIER_BASELINE,
            "subsequent_years": SUBSEQUENT_PERIOD,
            "qualifying_venues": [v["name"] for v in VENUES],
            "comparison_cohort_size": len(comparison_pids),
            "core99_size": 99,
            "core99_analyzable_size": 87,
            "core99_decline_rate_pct": 49.4,
        },
        "comparison_cohort": {
            "size": len(comparison_pids),
            "rate_change_distribution": {
                "decreased": decreased,
                "flat": flat,
                "increased": increased,
                "inactive_subsequent_period": inactive,
            },
            "decline_rate_pct": round(dec_rate, 1),
            "decline_or_inactive_rate_pct": round(dec_or_inactive_rate, 1),
        },
        "interpretation": (
            f"If the comparison cohort decline rate ({dec_rate:.1f}%) is similar to "
            f"core-99's decline rate (49.4%), regression to the mean is a significant "
            f"factor. If substantially different, field-specific change is more likely."
        ),
    }

    with open(OUTPUT_FILE, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\nWrote {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
