#!/usr/bin/env python3
"""Build researcher-level topic profiles for core-99 and post-GPT core.

Computes per-researcher topic distributions using the paper topic classifier,
then compares stayer vs. newcomer vs. dropout profiles for both periods.

Outputs:
  - data/researcher_topic_profiles.json — per-researcher topic vectors
  - data/post_gpt_core_profiles.csv — CSV for comparison
"""

import json
import sys
from pathlib import Path
from collections import defaultdict

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

# Import the topic classifier from classify_paper_topics
sys.path.insert(0, str(PROJECT_DIR / "scripts"))
from classify_paper_topics import classify_title, TOPICS

OUTPUT_PROFILES = DATA_DIR / "researcher_topic_profiles.json"
OUTPUT_CSV = DATA_DIR / "post_gpt_core_profiles.csv"

QUALIFYING_VENUES = {"SIGCOMM", "NSDI", "CoNEXT", "HotNets", "IMC"}
TOPIC_KEYS = list(TOPICS.keys())


def compute_researcher_topic_profile(researcher: dict, years: list[str]) -> dict:
    """Compute topic distribution for a researcher over given years."""
    topic_counts = defaultdict(float)
    total_papers = 0

    itinerary = researcher.get("itinerary", {})
    for year in years:
        for paper in itinerary.get(str(year), []):
            title = paper.get("title", "")
            if not title:
                continue
            classification = classify_title(title)
            total_papers += 1
            for topic, conf in classification["all_topics"].items():
                topic_counts[topic] += conf

    shares = {}
    for topic in TOPIC_KEYS:
        shares[topic] = round(topic_counts.get(topic, 0) / total_papers * 100, 2) if total_papers > 0 else 0.0

    # Also count top-networking papers
    top_net_count = 0
    for year in years:
        for paper in itinerary.get(str(year), []):
            venue = paper.get("venue", "").strip()
            if venue in QUALIFYING_VENUES:
                top_net_count += 1

    # Top-networking topic profile
    top_net_topic_counts = defaultdict(float)
    top_net_total = 0
    for year in years:
        for paper in itinerary.get(str(year), []):
            venue = paper.get("venue", "").strip()
            if venue not in QUALIFYING_VENUES:
                continue
            title = paper.get("title", "")
            if not title:
                continue
            classification = classify_title(title)
            top_net_total += 1
            for topic, conf in classification["all_topics"].items():
                top_net_topic_counts[topic] += conf

    top_net_topic_shares = {}
    for topic in TOPIC_KEYS:
        top_net_topic_shares[topic] = round(
            top_net_topic_counts.get(topic, 0) / top_net_total * 100, 2
        ) if top_net_total > 0 else 0.0

    return {
        "total_papers": total_papers,
        "top_networking_papers": top_net_count,
        "topic_shares": shares,
        "top_networking_topic_shares": top_net_topic_shares,
        "primary_topic": max(shares, key=shares.get) if shares else "other",
        "primary_top_net_topic": max(top_net_topic_shares, key=top_net_topic_shares.get) if top_net_topic_shares else "other",
    }


def main():
    print("=" * 60)
    print("Researcher Topic Profile Builder")
    print("=" * 60)

    # ── Load data ──
    with open(DATA_DIR / "researcher_itineraries.json") as f:
        itins_data = json.load(f)

    with open(DATA_DIR / "post_gpt_core.json") as f:
        pgc_data = json.load(f)

    with open(DATA_DIR / "core99_researcher_attributes.json") as f:
        core99_data = json.load(f)

    # Build PID lookups
    stayer_pids = {r["dblp_pid"] for r in pgc_data["tripartite_split"]["stayers"]["researchers"]}
    newcomer_pids = {r["dblp_pid"] for r in pgc_data["tripartite_split"]["newcomers"]["researchers"]}
    dropout_pids = {r["dblp_pid"] for r in pgc_data["tripartite_split"]["dropouts"]["researchers"]}

    # Build PID -> researcher lookup from itineraries
    pid_to_researcher = {}
    for r in itins_data.get("researchers", []):
        pid = r.get("dblp_pid", "")
        if pid:
            pid_to_researcher[pid] = r

    # Build PID -> attributes lookup
    pid_to_attrs = {}
    for r in core99_data.get("researchers", []):
        pid = r.get("dblp_pid", "")
        if pid:
            pid_to_attrs[pid] = r

    # ── Compute topic profiles ──
    print("\nComputing researcher topic profiles...")

    baseline_years = [str(y) for y in range(2018, 2023)]
    post_years = [str(y) for y in range(2023, 2027)]

    all_profiles = {}

    def process_group(pids, group_label):
        profiles = []
        for pid in pids:
            researcher = pid_to_researcher.get(pid)
            if not researcher:
                continue

            baseline_profile = compute_researcher_topic_profile(researcher, baseline_years)
            post_profile = compute_researcher_topic_profile(researcher, post_years)

            attrs = pid_to_attrs.get(pid, {})

            profile = {
                "dblp_pid": pid,
                "name": researcher.get("name", "Unknown"),
                "group": group_label,
                "baseline_top_networking_count": researcher.get("baseline_top_networking_count", 0),
                "post_top_networking_count": post_profile["top_networking_papers"],
                "baseline": baseline_profile,
                "post_2023": post_profile,
                # Delta
                "delta": {
                    topic: round(post_profile["topic_shares"].get(topic, 0) - baseline_profile["topic_shares"].get(topic, 0), 2)
                    for topic in TOPIC_KEYS
                },
                "top_net_delta": {
                    topic: round(post_profile["top_networking_topic_shares"].get(topic, 0) - baseline_profile["top_networking_topic_shares"].get(topic, 0), 2)
                    for topic in TOPIC_KEYS
                },
                # Career context
                "career": {
                    "first_dblp_year": attrs.get("first_dblp_year", "unknown"),
                    "author_role_baseline": attrs.get("baseline_author_role_profile", "unknown"),
                    "author_role_post": attrs.get("post2023_author_role_profile", "unknown"),
                },
            }
            profiles.append(profile)
        return profiles

    stayer_profiles = process_group(stayer_pids, "stayer")
    newcomer_profiles = process_group(newcomer_pids, "newcomer")
    dropout_profiles = process_group(dropout_pids, "dropout")

    # ── Group-level summaries ──
    def group_summary(profiles, period_key="post_2023"):
        """Compute mean topic shares for a group."""
        n = len(profiles)
        if n == 0:
            return {}
        means = defaultdict(float)
        for p in profiles:
            for topic, share in p[period_key]["topic_shares"].items():
                means[topic] += share
        return {topic: round(v / n, 2) for topic, v in means.items()}

    print(f"\n=== GROUP SUMMARIES (Post-2023 Topic Shares) ===")

    for label, profiles in [("Stayers", stayer_profiles), ("Newcomers", newcomer_profiles), ("Dropouts", dropout_profiles)]:
        if not profiles:
            continue
        summary = group_summary(profiles)
        print(f"\n{label} (n={len(profiles)}):")
        top5 = sorted(summary.items(), key=lambda x: -x[1])[:5]
        for topic, share in top5:
            print(f"  {TOPICS[topic]['label']}: {share:.1f}%")

        # AI infra share
        ai_share = summary.get("ai_infrastructure", 0)
        print(f"  → AI Infrastructure: {ai_share:.1f}%")

    # Delta comparisons
    print(f"\n=== DELTA COMPARISON (Post - Baseline topic shares, pp) ===")
    for label, profiles in [("Stayers", stayer_profiles), ("Newcomers", newcomer_profiles), ("Dropouts", dropout_profiles)]:
        if not profiles:
            continue
        n = len(profiles)
        mean_delta = defaultdict(float)
        for p in profiles:
            for topic in TOPIC_KEYS:
                mean_delta[topic] += p["delta"].get(topic, 0)
        mean_delta = {topic: round(v / n, 2) for topic, v in mean_delta.items()}

        significant = [(topic, val) for topic, val in mean_delta.items() if abs(val) >= 2.0]
        significant.sort(key=lambda x: -abs(x[1]))

        print(f"\n{label} (n={n}):")
        for topic, val in significant[:5]:
            direction = "↑" if val > 0 else "↓"
            print(f"  {TOPICS[topic]['label']}: {direction}{abs(val):.1f}pp")

    # ── Save output ──
    output = {
        "metadata": {
            "phase": "researcher_topic_profiles",
            "method": "keyword_classification",
            "topics": {k: v["label"] for k, v in TOPICS.items()},
            "groups": {
                "stayers": len(stayer_profiles),
                "newcomers": len(newcomer_profiles),
                "dropouts": len(dropout_profiles),
            },
        },
        "group_summaries": {
            "stayers_post2023_mean": group_summary(stayer_profiles, "post_2023"),
            "newcomers_post2023_mean": group_summary(newcomer_profiles, "post_2023"),
            "dropouts_post2023_mean": group_summary(dropout_profiles, "post_2023"),
        },
        "researchers": stayer_profiles + newcomer_profiles + dropout_profiles,
    }

    with open(OUTPUT_PROFILES, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"\nWrote {OUTPUT_PROFILES}")

    # ── Save CSV ──
    with open(OUTPUT_CSV, "w") as f:
        headers = ["name", "pid", "group", "bl_top_net", "post_top_net",
                   "bl_ai_infra_pct", "post_ai_infra_pct", "delta_ai_infra_pp",
                   "bl_classical_pct", "post_classical_pct", "delta_classical_pp",
                   "bl_primary_topic", "post_primary_topic"]
        f.write(",".join(headers) + "\n")
        for p in stayer_profiles + newcomer_profiles + dropout_profiles:
            row = [
                p["name"], p["dblp_pid"], p["group"],
                str(p["baseline_top_networking_count"]), str(p["post_top_networking_count"]),
                str(p["baseline"]["topic_shares"].get("ai_infrastructure", 0)),
                str(p["post_2023"]["topic_shares"].get("ai_infrastructure", 0)),
                str(p["delta"].get("ai_infrastructure", 0)),
                str(p["baseline"]["topic_shares"].get("classical_networking", 0)),
                str(p["post_2023"]["topic_shares"].get("classical_networking", 0)),
                str(p["delta"].get("classical_networking", 0)),
                p["baseline"]["primary_topic"],
                p["post_2023"]["primary_topic"],
            ]
            f.write(",".join(row) + "\n")
    print(f"Wrote {OUTPUT_CSV}")

    print("\nDone.")


if __name__ == "__main__":
    main()
