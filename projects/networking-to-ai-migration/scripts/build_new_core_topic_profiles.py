#!/usr/bin/env python3
"""Build researcher topic profiles from the canonical new-core clean paper table.

Reads data/new_core_clean_papers.json and data/new_core.json to compute
per-researcher topic distributions for all 171 stayers/newcomers/dropouts,
including DBLP-only complete newcomers who have no itinerary.

Unlike the old build_researcher_topic_profiles.py (which read from itineraries
and post_gpt_core.json), this script uses the repaired clean paper table with
full author PIDs and PACMNET-inclusive CoNEXT data.

Outputs:
  - data/new_core_topic_profiles.json — per-researcher topic vectors
  - data/new_core_topic_profiles.csv — flat CSV for comparison
"""

import csv
import json
import sys
from pathlib import Path
from collections import defaultdict

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

sys.path.insert(0, str(PROJECT_DIR / "scripts"))
from classify_paper_topics import classify_title, TOPICS

OUTPUT_PROFILES = DATA_DIR / "new_core_topic_profiles.json"
OUTPUT_CSV = DATA_DIR / "new_core_topic_profiles.csv"

QUALIFYING_VENUES = {"SIGCOMM", "NSDI", "CoNEXT", "HotNets", "IMC"}
TOPIC_KEYS = list(TOPICS.keys())
BASELINE_YEARS = set(range(2018, 2023))
POST_YEARS = set(range(2023, 2027))


def build_pid_index(clean_papers: list[dict]) -> dict[str, list[dict]]:
    """Build PID → [paper] index from the clean paper table."""
    pid_papers = defaultdict(list)
    for paper in clean_papers:
        pids = paper.get("author_pids", [])
        title = paper.get("title", "")
        venue = paper.get("venue_group", paper.get("venue", ""))
        year = paper.get("year", 0)

        if not title or not year:
            continue

        paper_ref = {
            "title": title,
            "venue": venue,
            "year": year,
            "paper_id": paper.get("paper_id", ""),
            "sources": paper.get("sources", []),
        }

        for pid in pids:
            pid_papers[pid].append(paper_ref)

    return pid_papers


def compute_topic_profile(
    papers: list[dict],
    years: set[int] | None = None,
    venue_filter: set[str] | None = None,
) -> dict:
    """Compute topic distribution for a set of papers.

    Args:
        papers: list of paper dicts with 'title', 'venue', 'year'
        years: if set, only include papers whose year is in this set
        venue_filter: if set, only include papers whose venue is in this set

    Returns:
        {topic_shares: {topic: pct}, qualifying_papers: int, primary_topic: str}
    """
    topic_counts = defaultdict(float)
    total = 0

    for paper in papers:
        year = paper.get("year", 0)
        venue = paper.get("venue", "")

        if years is not None and year not in years:
            continue
        if venue_filter is not None and venue not in venue_filter:
            continue

        title = paper.get("title", "")
        if not title:
            continue

        classification = classify_title(title)
        total += 1
        for topic, conf in classification["all_topics"].items():
            topic_counts[topic] += conf

    shares = {}
    for topic in TOPIC_KEYS:
        shares[topic] = round(topic_counts.get(topic, 0) / total * 100, 2) if total > 0 else 0.0

    primary = max(shares, key=shares.get) if shares else "other"

    return {
        "qualifying_papers": total,
        "topic_shares": shares,
        "primary_topic": primary,
    }


def main():
    print("=" * 60)
    print("New-Core Researcher Topic Profile Builder")
    print("=" * 60)

    # ── Load data ──
    with open(DATA_DIR / "new_core_clean_papers.json") as f:
        clean_data = json.load(f)

    with open(DATA_DIR / "new_core.json") as f:
        core_data = json.load(f)

    # Build PID → name lookup from old sources for display names
    pid_name = {}
    # From new_core.json tripartite split
    for group_name in ["stayers", "newcomers", "dropouts"]:
        group = core_data["tripartite_split"][group_name]
        for r in group["researchers"]:
            pid = r["dblp_pid"]
            name = r.get("name", "Unknown")
            if pid and name and pid not in pid_name:
                pid_name[pid] = name

    # Supplement with names from itineraries if available
    itins_path = DATA_DIR / "researcher_itineraries.json"
    if itins_path.exists():
        with open(itins_path) as f:
            itins = json.load(f)
        for r in itins.get("researchers", []):
            pid = r.get("dblp_pid", "")
            name = r.get("name", "")
            if pid and name and pid not in pid_name:
                pid_name[pid] = name

    # Supplement with names from core99 attributes
    core99_path = DATA_DIR / "core99_researcher_attributes.json"
    if core99_path.exists():
        with open(core99_path) as f:
            core99 = json.load(f)
        for r in core99.get("researchers", []):
            pid = r.get("dblp_pid", "")
            name = r.get("name", "")
            if pid and name and pid not in pid_name:
                pid_name[pid] = name

    # ── Build PID index from clean papers ──
    all_papers = clean_data.get("papers", [])
    clean_papers = [p for p in all_papers if p.get("included_in_new_core_scope")]
    print(f"Indexing {len(clean_papers)} clean papers by author PID...")
    pid_papers = build_pid_index(clean_papers)
    print(f"  {len(pid_papers)} unique PIDs with papers")

    # ── Collect researchers by group ──
    groups = {}
    group_pids = {}
    for group_name in ["stayers", "newcomers", "dropouts"]:
        group = core_data["tripartite_split"][group_name]
        # Use singular group label
        label = {"stayers": "stayer", "newcomers": "newcomer", "dropouts": "dropout"}[group_name]
        researchers = []
        pids = set()
        for r in group["researchers"]:
            pid = r["dblp_pid"]
            pids.add(pid)
            researchers.append({
                "dblp_pid": pid,
                "name": pid_name.get(pid, r.get("name", "Unknown")),
                "group": label,
                "baseline_top_networking_count": r.get("baseline_top_networking_count", 0),
                "new_core_observed_top_networking_count": r.get("new_core_observed_top_networking_count", 0),
                "in_core99": r.get("in_core99", label != "newcomer"),
                "in_broad_cohort": r.get("in_broad_cohort", label != "newcomer"),
            })
        groups[label] = researchers
        group_pids[label] = pids

    # ── Compute topic profiles ──
    print("\nComputing researcher topic profiles...")

    all_profiles = []

    for group_label, researchers in groups.items():
        print(f"  {group_label}: {len(researchers)} researchers")
        for r in researchers:
            pid = r["dblp_pid"]
            papers = pid_papers.get(pid, [])

            # Qualifying-venue topic profile. The canonical clean paper table
            # contains only qualifying venues, so this is not a full publication
            # portfolio for the researcher.
            baseline_profile = compute_topic_profile(papers, years=BASELINE_YEARS)
            post_profile = compute_topic_profile(papers, years=POST_YEARS)

            # Same computation with an explicit venue filter kept for diagnostics.
            topnet_baseline = compute_topic_profile(
                papers, years=BASELINE_YEARS, venue_filter=QUALIFYING_VENUES
            )
            topnet_post = compute_topic_profile(
                papers, years=POST_YEARS, venue_filter=QUALIFYING_VENUES
            )

            profile = {
                "dblp_pid": pid,
                "name": r["name"],
                "group": group_label,
                "baseline_top_networking_count": r["baseline_top_networking_count"],
                "new_core_observed_top_networking_count": r["new_core_observed_top_networking_count"],
                "in_core99": r["in_core99"],
                "in_broad_cohort": r["in_broad_cohort"],
                # Baseline
                "baseline_qualifying_papers": baseline_profile["qualifying_papers"],
                "baseline_topic_shares": baseline_profile["topic_shares"],
                "baseline_primary_topic": baseline_profile["primary_topic"],
                # Post-2023
                "post_qualifying_papers": post_profile["qualifying_papers"],
                "post_topic_shares": post_profile["topic_shares"],
                "post_primary_topic": post_profile["primary_topic"],
                # Delta
                "delta_topic_shares": {
                    topic: round(
                        post_profile["topic_shares"].get(topic, 0)
                        - baseline_profile["topic_shares"].get(topic, 0),
                        2,
                    )
                    for topic in TOPIC_KEYS
                },
                # Top-networking only
                "topnet_baseline": {
                    "qualifying_papers": topnet_baseline["qualifying_papers"],
                    "topic_shares": topnet_baseline["topic_shares"],
                    "primary_topic": topnet_baseline["primary_topic"],
                },
                "topnet_post": {
                    "qualifying_papers": topnet_post["qualifying_papers"],
                    "topic_shares": topnet_post["topic_shares"],
                    "primary_topic": topnet_post["primary_topic"],
                },
                "topnet_delta_topic_shares": {
                    topic: round(
                        topnet_post["topic_shares"].get(topic, 0)
                        - topnet_baseline["topic_shares"].get(topic, 0),
                        2,
                    )
                    for topic in TOPIC_KEYS
                },
            }
            all_profiles.append(profile)

    # ── Group-level summaries ──
    def group_mean_shares(profiles: list[dict], period: str) -> dict:
        """Compute mean topic shares for a group."""
        n = len(profiles)
        if n == 0:
            return {}
        means = defaultdict(float)
        for p in profiles:
            for topic, share in p[f"{period}_topic_shares"].items():
                means[topic] += share
        return {topic: round(v / n, 2) for topic, v in means.items()}

    print(f"\n{'=' * 60}")
    print("GROUP SUMMARIES (Post-2023 Topic Shares, qualifying-venue papers)")
    print(f"{'=' * 60}")

    group_summaries = {}
    for label in ["stayer", "newcomer", "dropout"]:
        profiles = [p for p in all_profiles if p["group"] == label]
        if not profiles:
            continue
        post_mean = group_mean_shares(profiles, "post")
        bl_mean = group_mean_shares(profiles, "baseline")

        # Delta means
        delta_means = {}
        for topic in TOPIC_KEYS:
            delta_means[topic] = round(post_mean.get(topic, 0) - bl_mean.get(topic, 0), 2)

        group_summaries[label] = {
            "n": len(profiles),
            "baseline_mean_shares": bl_mean,
            "post_mean_shares": post_mean,
            "delta_mean_shares": delta_means,
        }

        print(f"\n{label} (n={len(profiles)}):")
        top5 = sorted(post_mean.items(), key=lambda x: -x[1])[:5]
        for topic, share in top5:
            print(f"  {TOPICS[topic]['label']}: {share:.1f}%")
        ai_share = post_mean.get("ai_infrastructure", 0)
        print(f"  → AI Infrastructure: {ai_share:.1f}%")

    # Delta comparison
    print(f"\n{'=' * 60}")
    print("DELTA COMPARISON (Post - Baseline, pp change)")
    print(f"{'=' * 60}")
    for label in ["stayer", "newcomer", "dropout"]:
        gs = group_summaries.get(label)
        if not gs:
            continue
        deltas = gs["delta_mean_shares"]
        significant = [(t, v) for t, v in deltas.items() if abs(v) >= 2.0]
        significant.sort(key=lambda x: -abs(x[1]))
        print(f"\n{label} (n={gs['n']}):")
        for topic, val in significant[:6]:
            direction = "↑" if val > 0 else "↓"
            print(f"  {TOPICS[topic]['label']}: {direction}{abs(val):.1f}pp")

    # ── Top-networking only summaries ──
    print(f"\n{'=' * 60}")
    print("TOP-NETWORKING-ONLY POST-2023 TOPIC SHARES")
    print(f"{'=' * 60}")
    for label in ["stayer", "newcomer", "dropout"]:
        profiles = [p for p in all_profiles if p["group"] == label]
        if not profiles:
            continue
        n = len(profiles)
        # Mean of topnet_post topic shares
        topnet_means = defaultdict(float)
        for p in profiles:
            if p["topnet_post"]["qualifying_papers"] > 0:
                for topic, share in p["topnet_post"]["topic_shares"].items():
                    topnet_means[topic] += share
        topnet_means = {t: round(v / n, 2) for t, v in topnet_means.items()}
        print(f"\n{label} (n={n}):")
        for topic, share in sorted(topnet_means.items(), key=lambda x: -x[1])[:5]:
            print(f"  {TOPICS[topic]['label']}: {share:.1f}%")
        ai_share = topnet_means.get("ai_infrastructure", 0)
        print(f"  → AI Infrastructure: {ai_share:.1f}%")

    # ── Baseline sufficiency diagnostics ──
    baseline_sufficiency = {}
    for label in ["stayer", "newcomer", "dropout"]:
        profiles = [p for p in all_profiles if p["group"] == label]
        baseline_sufficiency[label] = {
            "n": len(profiles),
            "baseline_zero": sum(1 for p in profiles if p["baseline_qualifying_papers"] == 0),
            "baseline_lt5": sum(1 for p in profiles if p["baseline_qualifying_papers"] < 5),
            "baseline_ge5": sum(1 for p in profiles if p["baseline_qualifying_papers"] >= 5),
        }

    def group_delta_for_subset(profiles: list[dict]) -> dict:
        n = len(profiles)
        if n == 0:
            return {topic: None for topic in TOPIC_KEYS}
        out = {}
        for topic in TOPIC_KEYS:
            out[topic] = round(sum(p["delta_topic_shares"].get(topic, 0) for p in profiles) / n, 2)
        return out

    delta_sensitivity = {}
    for label in ["stayer", "newcomer", "dropout"]:
        profiles = [p for p in all_profiles if p["group"] == label]
        subsets = {
            "all": profiles,
            "baseline_ge1": [p for p in profiles if p["baseline_qualifying_papers"] >= 1],
            "baseline_ge5": [p for p in profiles if p["baseline_qualifying_papers"] >= 5],
        }
        delta_sensitivity[label] = {
            name: {
                "n": len(subset),
                "mean_delta_topic_shares": group_delta_for_subset(subset),
            }
            for name, subset in subsets.items()
        }

    print("\nBaseline sufficiency diagnostics:")
    for label, stats in baseline_sufficiency.items():
        print(
            f"  {label}: n={stats['n']}, baseline_zero={stats['baseline_zero']}, "
            f"baseline_lt5={stats['baseline_lt5']}, baseline_ge5={stats['baseline_ge5']}"
        )

    # ── Save JSON output ──
    output = {
        "metadata": {
            "phase": "new_core_topic_profiles",
            "method": "keyword_classification",
            "input_sources": [
                "data/new_core_clean_papers.json",
                "data/new_core.json",
            ],
            "topics": {k: v["label"] for k, v in TOPICS.items()},
            "total_profiles": len(all_profiles),
            "by_group": {
                label: len([p for p in all_profiles if p["group"] == label])
                for label in ["stayer", "newcomer", "dropout"]
            },
            "coverage_note": "All 171 stayers/newcomers/dropouts have profiles, including 9 DBLP-only complete newcomers. Profiles are qualifying-venue only. Researchers with zero baseline qualifying papers have zero-valued baseline topic shares, so delta claims must be read with baseline sufficiency diagnostics.",
        },
        "group_summaries": group_summaries,
        "baseline_sufficiency": baseline_sufficiency,
        "delta_sensitivity": delta_sensitivity,
        "researchers": sorted(
            all_profiles,
            key=lambda p: ({"stayer": 0, "newcomer": 1, "dropout": 2}[p["group"]], p["name"]),
        ),
    }

    with open(OUTPUT_PROFILES, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"\nWrote {OUTPUT_PROFILES}")

    # ── Save CSV ──
    with open(OUTPUT_CSV, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "name",
                "dblp_pid",
                "group",
                "baseline_top_networking_count",
                "new_core_observed_top_networking_count",
                "in_core99",
                "in_broad_cohort",
                "baseline_qualifying_papers",
                "post_qualifying_papers",
                "bl_ai_infra_pct",
                "post_ai_infra_pct",
                "delta_ai_infra_pp",
                "bl_classical_pct",
                "post_classical_pct",
                "delta_classical_pp",
                "bl_primary_topic",
                "post_primary_topic",
                "topnet_bl_ai_infra_pct",
                "topnet_post_ai_infra_pct",
            ],
        )
        writer.writeheader()
        for p in sorted(
            all_profiles,
            key=lambda x: ({"stayer": 0, "newcomer": 1, "dropout": 2}[x["group"]], x["name"]),
        ):
            writer.writerow(
                {
                    "name": p["name"],
                    "dblp_pid": p["dblp_pid"],
                    "group": p["group"],
                    "baseline_top_networking_count": p["baseline_top_networking_count"],
                    "new_core_observed_top_networking_count": p[
                        "new_core_observed_top_networking_count"
                    ],
                    "in_core99": p["in_core99"],
                    "in_broad_cohort": p["in_broad_cohort"],
                    "baseline_qualifying_papers": p["baseline_qualifying_papers"],
                    "post_qualifying_papers": p["post_qualifying_papers"],
                    "bl_ai_infra_pct": p["baseline_topic_shares"].get("ai_infrastructure", 0),
                    "post_ai_infra_pct": p["post_topic_shares"].get("ai_infrastructure", 0),
                    "delta_ai_infra_pp": p["delta_topic_shares"].get("ai_infrastructure", 0),
                    "bl_classical_pct": p["baseline_topic_shares"].get("classical_networking", 0),
                    "post_classical_pct": p["post_topic_shares"].get("classical_networking", 0),
                    "delta_classical_pp": p["delta_topic_shares"].get("classical_networking", 0),
                    "bl_primary_topic": p["baseline_primary_topic"],
                    "post_primary_topic": p["post_primary_topic"],
                    "topnet_bl_ai_infra_pct": p["topnet_baseline"]["topic_shares"].get(
                        "ai_infrastructure", 0
                    ),
                    "topnet_post_ai_infra_pct": p["topnet_post"]["topic_shares"].get(
                        "ai_infrastructure", 0
                    ),
                }
            )
    print(f"Wrote {OUTPUT_CSV}")

    # ── Coverage diagnostics ──
    zero_baseline = sum(
        1 for p in all_profiles if p["baseline_qualifying_papers"] == 0
    )
    zero_post = sum(
        1 for p in all_profiles if p["post_qualifying_papers"] == 0
    )
    print(f"\nCoverage diagnostics:")
    print(f"  Researchers with zero baseline qualifying papers: {zero_baseline}")
    print(f"  Researchers with zero post-2023 qualifying papers: {zero_post}")
    print(f"  DBLP-only (not in broad cohort): {sum(1 for p in all_profiles if not p['in_broad_cohort'])}")

    print("\nDone.")


if __name__ == "__main__":
    main()
