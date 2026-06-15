#!/usr/bin/env python3
"""Compute researcher output as share of venue-family total volume.

Reads venue_accepted_totals.json and core99_researcher_attributes.json,
computes each researcher's papers as a percentage of the total papers
at the qualifying venues for each period.

This is a domain-volume normalization: "did the researcher publish less,
or did the venue publish less?" It complements the researcher-internal
percentage vectors used in the main analysis.

Output: data/domain_normalized_shares.json
"""

import json
import sys
from pathlib import Path
from collections import defaultdict

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

DENOMINATOR_FILE = DATA_DIR / "venue_accepted_totals.json"
ATTRIBUTES_FILE = DATA_DIR / "core99_researcher_attributes.json"
OUTPUT_FILE = DATA_DIR / "domain_normalized_shares.json"

BASELINE_YEARS = [2018, 2019, 2020, 2021, 2022]
POST_YEARS = [2023, 2024, 2025, 2026]


def load_denominator(path: Path) -> dict:
    """Load venue-year totals and return structured denominator data."""
    with open(path) as f:
        data = json.load(f)
    return data.get("totals", {})


def aggregate_period_denominator(
    totals: dict, years: list[int], venues: list[str]
) -> dict[str, int]:
    """Sum total papers per venue across a period, handling nulls."""
    result: dict[str, int] = defaultdict(int)
    null_years: dict[str, list[int]] = defaultdict(list)
    for year in years:
        year_str = str(year)
        if year_str not in totals:
            continue
        for venue in venues:
            count = totals[year_str].get(venue)
            if count is not None:
                result[venue] += count
            else:
                null_years[venue].append(year)
    return dict(result), dict(null_years)


def compute_normalized_shares(
    attributes: list[dict],
    baseline_denom: dict[str, int],
    post_denom: dict[str, int],
) -> list[dict]:
    """Compute per-researcher normalized shares."""
    results = []
    for r in attributes:
        name = r["name"]
        bl_counts_raw = r.get("baseline_top_networking_venue_counts", [])
        post_counts_raw = r.get("post2023_top_networking_venue_counts", [])
        # Convert list-of-dicts to plain dict
        bl_counts = {item["venue"]: item["count"] for item in bl_counts_raw} if isinstance(bl_counts_raw, list) else bl_counts_raw
        post_counts = {item["venue"]: item["count"] for item in post_counts_raw} if isinstance(post_counts_raw, list) else post_counts_raw

        # Compute normalized share for each venue (researcher_count / venue_total)
        bl_shares = {}
        post_shares = {}
        bl_total_share = 0.0
        post_total_share = 0.0

        for venue in baseline_denom:
            denom = baseline_denom[venue]
            if denom > 0:
                count = bl_counts.get(venue, 0)
                bl_shares[venue] = round(count / denom, 5)
                bl_total_share += count / denom

        for venue in post_denom:
            denom = post_denom[venue]
            if denom > 0:
                count = post_counts.get(venue, 0)
                post_shares[venue] = round(count / denom, 5)
                post_total_share += count / denom

        # Also compute the researcher-internal percentage for comparison
        bl_total = r.get("baseline_top_networking_count", 0)
        post_total = r.get("post2023_top_networking_count", 0)

        results.append({
            "name": name,
            "baseline": {
                "absolute_count": bl_total,
                "normalized_share_sum": round(bl_total_share, 5),
                "per_venue_shares": bl_shares,
            },
            "post2023": {
                "absolute_count": post_total,
                "normalized_share_sum": round(post_total_share, 5),
                "per_venue_shares": post_shares,
            },
            "normalized_share_ratio": round(
                post_total_share / bl_total_share, 3
            ) if bl_total_share > 0 else None,
        })

    return results


def main():
    if not DENOMINATOR_FILE.exists():
        print(
            f"ERROR: {DENOMINATOR_FILE} not found. "
            "Run fetch_venue_accepted_totals.py first.",
            file=sys.stderr,
        )
        sys.exit(1)

    if not ATTRIBUTES_FILE.exists():
        print(
            f"ERROR: {ATTRIBUTES_FILE} not found.",
            file=sys.stderr,
        )
        sys.exit(1)

    totals = load_denominator(DENOMINATOR_FILE)
    venues = ["SIGCOMM", "NSDI", "CoNEXT", "HotNets", "IMC"]

    # Aggregate denominators per period
    bl_denom, bl_nulls = aggregate_period_denominator(totals, BASELINE_YEARS, venues)
    post_denom, post_nulls = aggregate_period_denominator(totals, POST_YEARS, venues)

    print("Baseline denominator (2018-2022):")
    for v in venues:
        n = bl_nulls.get(v, [])
        print(f"  {v}: {bl_denom.get(v, 0)} papers" + (f" (null years: {n})" if n else ""))
    print(f"  TOTAL: {sum(bl_denom.values())}")

    print("\nPost-2023 denominator (2023-2026):")
    for v in venues:
        n = post_nulls.get(v, [])
        print(f"  {v}: {post_denom.get(v, 0)} papers" + (f" (null years: {n})" if n else ""))
    print(f"  TOTAL: {sum(post_denom.values())}")

    # Load researcher attributes
    with open(ATTRIBUTES_FILE) as f:
        attr_data = json.load(f)
    researchers = attr_data.get("researchers", [])

    # Compute normalized shares
    shares = compute_normalized_shares(researchers, bl_denom, post_denom)

    # Summary statistics
    analyzable = [s for s in shares if s["baseline"]["absolute_count"] > 0]
    ratios = [s["normalized_share_ratio"] for s in analyzable if s["normalized_share_ratio"] is not None]

    print(f"\nNormalized share ratios (n={len(ratios)}):")
    if ratios:
        ratios.sort()
        print(f"  Min: {ratios[0]:.3f}")
        print(f"  P25: {ratios[len(ratios)//4]:.3f}")
        print(f"  Median: {ratios[len(ratios)//2]:.3f}")
        print(f"  P75: {ratios[3*len(ratios)//4]:.3f}")
        print(f"  Max: {ratios[-1]:.3f}")
        decreased = sum(1 for r in ratios if r < 0.75)
        flat = sum(1 for r in ratios if 0.75 <= r <= 1.25)
        increased = sum(1 for r in ratios if r > 1.25)
        print(f"  Decreased (<0.75): {decreased}")
        print(f"  Flat (0.75-1.25): {flat}")
        print(f"  Increased (>1.25): {increased}")

    # Top and bottom movers
    print("\nTop 5 by normalized share ratio (most increasing relative presence):")
    top5 = sorted(analyzable, key=lambda s: s["normalized_share_ratio"] or 0, reverse=True)[:5]
    for s in top5:
        print(
            f"  {s['name']}: {s['baseline']['absolute_count']} -> "
            f"{s['post2023']['absolute_count']} papers, "
            f"share sum {s['baseline']['normalized_share_sum']:.4f} -> "
            f"{s['post2023']['normalized_share_sum']:.4f} "
            f"(ratio: {s['normalized_share_ratio']})"
        )

    print("\nBottom 5 by normalized share ratio (most decreasing relative presence):")
    bot5 = sorted(
        [s for s in analyzable if s["normalized_share_ratio"] is not None],
        key=lambda s: s["normalized_share_ratio"],
    )[:5]
    for s in bot5:
        print(
            f"  {s['name']}: {s['baseline']['absolute_count']} -> "
            f"{s['post2023']['absolute_count']} papers, "
            f"share sum {s['baseline']['normalized_share_sum']:.4f} -> "
            f"{s['post2023']['normalized_share_sum']:.4f} "
            f"(ratio: {s['normalized_share_ratio']})"
        )

    # Write output
    output = {
        "metadata": {
            "description": (
                "Per-researcher domain-normalized shares: researcher papers at "
                "qualifying venues divided by total DBLP TOC papers at those venues. "
                "Uses DBLP TOC counts which include workshop papers — shares are "
                "informative for relative comparison within the same denominator source, "
                "not absolute acceptance-rate shares."
            ),
            "baseline_years": BASELINE_YEARS,
            "post_years": POST_YEARS,
            "denominator_source": str(DENOMINATOR_FILE),
            "baseline_null_years": bl_nulls,
            "post_null_years": post_nulls,
            "warning": (
                "DBLP TOC counts include workshop/posters alongside main-conference "
                "proceedings. Shares should be interpreted as relative measures within "
                "the same DBLP data universe, not as acceptance-rate percentages."
            ),
        },
        "period_denominators": {
            "baseline": bl_denom,
            "post2023": post_denom,
        },
        "researchers": shares,
    }

    with open(OUTPUT_FILE, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\nWrote {len(shares)} researcher records to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
