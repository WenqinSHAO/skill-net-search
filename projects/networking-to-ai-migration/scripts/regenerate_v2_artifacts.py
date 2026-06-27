#!/usr/bin/env python3
"""Regenerate all downstream artifacts from v3 paper topic labels.

This script orchestrates the regeneration of venue-year vectors, researcher
topic profiles, and venue-year background artifacts after the taxonomy and
classifier have been updated to v3.

Requires: data/paper_topic_labels_v3.json to exist.
Regenerates:
  - data/venue_topic_vectors_v3.json
  - data/venue_topic_evolution_v3.csv
  - data/new_core_topic_profiles.json (overwrites stale v2)
  - data/venue_year_background.json (overwrites stale v1)
  - data/venue_year_topic_vectors_stage1.json (overwrites stale v1)
"""

from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

INPUT_LABELS = DATA_DIR / "paper_topic_labels_v3.json"
TAXONOMY_PATH = DATA_DIR / "taxonomy_v3.json"
INPUT_CLEAN = DATA_DIR / "new_core_clean_papers.json"
INPUT_CORE = DATA_DIR / "new_core.json"
VENUE_TOTALS = DATA_DIR / "venue_accepted_totals.json"

OUTPUT_VENUE_VECTORS = DATA_DIR / "venue_topic_vectors_v3.json"
OUTPUT_VENUE_EVOLUTION = DATA_DIR / "venue_topic_evolution_v3.csv"


def load_json(path: Path) -> Any:
    with open(path) as f:
        return json.load(f)


def save_json(path: Path, data: Any) -> None:
    temp = path.with_suffix(".tmp")
    with open(temp, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    temp.rename(path)


def main() -> None:
    if not INPUT_LABELS.exists():
        print(f"ERROR: {INPUT_LABELS} not found. Run classify_paper_topics_v3.py first.")
        sys.exit(1)

    taxonomy = load_json(TAXONOMY_PATH)
    labels_data = load_json(INPUT_LABELS)
    papers = labels_data.get("papers", [])
    metadata = labels_data.get("metadata", {})

    print(f"Regenerating downstream artifacts from {len(papers)} classified papers")
    print(f"  Model: {metadata.get('model', 'unknown')}")
    print(f"  Taxonomy: v{taxonomy.get('version', '?')}")

    # ── Build venue-year topic vectors ──
    print("\nBuilding venue-year topic vectors (v3)...")
    QUALIFYING = {"SIGCOMM", "NSDI", "CoNEXT", "HotNets", "IMC"}

    venue_year_counts: dict[str, dict[str, dict[str, float]]] = defaultdict(
        lambda: defaultdict(lambda: defaultdict(float))
    )
    venue_year_quality: dict[str, Counter[str]] = defaultdict(Counter)
    venue_year_paper_count: dict[str, int] = defaultdict(int)

    for p in papers:
        venue = p.get("venue", "")
        year = p.get("year", 0)
        if venue not in QUALIFYING:
            continue
        vy_key = f"{venue}|{year}"
        venue_year_paper_count[vy_key] += 1

        # Count multi-label assignments and quality denominators.
        if p.get("evidence_mode") == "title_only":
            venue_year_quality[vy_key]["title_only"] += 1
        if p.get("uncertain"):
            venue_year_quality[vy_key]["uncertain"] += 1
        if p.get("classification_error"):
            venue_year_quality[vy_key]["classification_error"] += 1
        for axis_key in ["scenario", "mechanism", "method"]:
            labels = p.get(axis_key, [])
            if not labels:
                venue_year_quality[vy_key][f"{axis_key}_no_label"] += 1
            if p.get("confidence", {}).get(axis_key) == "low":
                venue_year_quality[vy_key][f"{axis_key}_low_confidence"] += 1
            for label in labels:
                venue_year_counts[vy_key][axis_key][label] += 1.0
                if str(label).startswith("unknown_"):
                    venue_year_quality[vy_key][f"{axis_key}_unknown"] += 1

    # Build vectors
    venue_vectors = []
    for vy_key in sorted(venue_year_counts.keys()):
        venue, year_str = vy_key.split("|")
        year = int(year_str)
        axis_counts = venue_year_counts[vy_key]
        paper_count = venue_year_paper_count[vy_key]

        # Build unified vectors. `topic_shares` normalizes by assigned labels
        # for backward compatibility. `paper_normalized_topic_shares` keeps the
        # paper denominator visible and is safer for analysis.
        vector = {}
        paper_vector = {}
        for axis_key in ["scenario", "mechanism", "method"]:
            total = sum(axis_counts.get(axis_key, {}).values())
            for key in taxonomy["axes"][axis_key]["values"]:
                count = axis_counts.get(axis_key, {}).get(key, 0)
                vector[f"{axis_key}_{key}"] = round(count / total * 100, 2) if total > 0 else 0.0
                paper_vector[f"{axis_key}_{key}"] = round(count / paper_count * 100, 2) if paper_count > 0 else 0.0
        quality_counts = venue_year_quality.get(vy_key, Counter())
        quality = {k: v for k, v in sorted(quality_counts.items())}
        quality.update({
            "paper_count": paper_count,
            "title_only_share_pct": round(quality_counts.get("title_only", 0) / paper_count * 100, 2) if paper_count else 0.0,
            "uncertain_share_pct": round(quality_counts.get("uncertain", 0) / paper_count * 100, 2) if paper_count else 0.0,
            "classification_error_share_pct": round(quality_counts.get("classification_error", 0) / paper_count * 100, 2) if paper_count else 0.0,
        })

        # Also compute primary topic per axis
        primary = {}
        for axis_key in ["scenario", "mechanism", "method"]:
            counts = axis_counts.get(axis_key, {})
            if counts:
                primary[axis_key] = max(counts, key=counts.get)
            else:
                primary[axis_key] = "none"

        venue_vectors.append({
            "venue": venue,
            "year": year,
            "primary_scenario": primary["scenario"],
            "primary_mechanism": primary["mechanism"],
            "primary_method": primary.get("method", "none"),
            "paper_count": paper_count,
            "topic_shares": vector,
            "paper_normalized_topic_shares": paper_vector,
            "quality": quality,
            "axis_breakdown": {
                axis_key: dict(sorted(counts.items(), key=lambda x: -x[1]))
                for axis_key, counts in axis_counts.items()
            },
        })

    # Save venue vectors
    save_json(OUTPUT_VENUE_VECTORS, {
        "metadata": {
            "phase": "topic_classification_v3",
            "method": metadata.get("method"),
            "model": metadata.get("model"),
            "taxonomy_version": taxonomy.get("version"),
            "venue_years": len(venue_vectors),
        },
        "taxonomy": taxonomy,
        "venue_vectors": sorted(venue_vectors, key=lambda x: (x["venue"], x["year"])),
    })
    print(f"  Wrote {OUTPUT_VENUE_VECTORS}")

    # Save venue evolution CSV
    axis_keys = []
    for axis_key in ["scenario", "mechanism", "method"]:
        for key in taxonomy["axes"][axis_key]["values"]:
            axis_keys.append(f"{axis_key}_{key}")

    with open(OUTPUT_VENUE_EVOLUTION, "w") as f:
        headers = ["venue", "year"] + axis_keys + ["paper_count"]
        f.write(",".join(headers) + "\n")
        for vv in sorted(venue_vectors, key=lambda x: (x["venue"], x["year"])):
            row = [vv["venue"], str(vv["year"])]
            row.extend([str(vv["topic_shares"].get(k, 0)) for k in axis_keys])
            row.append(str(vv["paper_count"]))
            f.write(",".join(row) + "\n")
    print(f"  Wrote {OUTPUT_VENUE_EVOLUTION}")

    # ── Rebuild researcher topic profiles ──
    print("\nRebuilding researcher topic profiles...")
    if not INPUT_CORE.exists() or not INPUT_CLEAN.exists():
        print("  Skipping researcher profiles: new_core.json or new_core_clean_papers.json missing")
    else:
        core_data = load_json(INPUT_CORE)
        clean_data = load_json(INPUT_CLEAN)

        # Build PID -> papers index from clean data
        pid_papers: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for p in clean_data.get("papers", []):
            if not p.get("included_in_new_core_scope"):
                continue
            for pid in p.get("author_pids", []):
                pid_papers[pid].append(p)

        # Build PID -> v3 labels index
        v3_labels_by_id: dict[str, dict[str, Any]] = {}
        for p in papers:
            v3_labels_by_id[p.get("paper_id", "")] = p

        def researcher_profile(pid: str, papers_for_pid: list[dict[str, Any]]) -> dict[str, Any]:
            baseline = [p for p in papers_for_pid if p.get("year", 0) <= 2022]
            post = [p for p in papers_for_pid if p.get("year", 0) >= 2023]

            def aggregate(paper_list: list[dict[str, Any]]) -> dict[str, Any]:
                profile: dict[str, Counter[str]] = {
                    "scenario": Counter(), "mechanism": Counter(), "method": Counter(),
                }
                quality = Counter()
                for p in paper_list:
                    v3 = v3_labels_by_id.get(p.get("paper_id", ""), {})
                    if v3.get("evidence_mode") == "title_only":
                        quality["title_only"] += 1
                    if v3.get("uncertain"):
                        quality["uncertain"] += 1
                    if v3.get("classification_error"):
                        quality["classification_error"] += 1
                    for axis in ["scenario", "mechanism", "method"]:
                        labels = v3.get(axis, [])
                        if not labels:
                            quality[f"{axis}_no_label"] += 1
                        if v3.get("confidence", {}).get(axis) == "low":
                            quality[f"{axis}_low_confidence"] += 1
                        for label in labels:
                            profile[axis][label] += 1
                            if str(label).startswith("unknown_"):
                                quality[f"{axis}_unknown"] += 1
                paper_count = len(paper_list)
                return {
                    "paper_count": paper_count,
                    "scenario": dict(profile["scenario"].most_common()),
                    "mechanism": dict(profile["mechanism"].most_common()),
                    "method": dict(profile["method"].most_common()),
                    "quality": {
                        **dict(sorted(quality.items())),
                        "title_only_share_pct": round(quality.get("title_only", 0) / paper_count * 100, 2) if paper_count else 0.0,
                        "uncertain_share_pct": round(quality.get("uncertain", 0) / paper_count * 100, 2) if paper_count else 0.0,
                    },
                    "primary_mechanism": profile["mechanism"].most_common(1)[0][0] if profile["mechanism"] else "none",
                    "primary_scenario": profile["scenario"].most_common(1)[0][0] if profile["scenario"] else "none",
                }

            return {
                "dblp_pid": pid,
                "baseline": aggregate(baseline),
                "post_2023": aggregate(post),
            }

        # Build for new-core members
        profiles = []
        for group_name in ["stayers", "newcomers", "dropouts"]:
            group = core_data.get("tripartite_split", {}).get(group_name, {})
            for r in group.get("researchers", []):
                pid = r.get("dblp_pid", "")
                if pid and pid in pid_papers:
                    profile = researcher_profile(pid, pid_papers[pid])
                    profile["group"] = group_name
                    profile["name"] = r.get("name", "Unknown")
                    profiles.append(profile)

        save_json(DATA_DIR / "new_core_topic_profiles.json", {
            "metadata": {
                "phase": "regenerate_v3",
                "description": "Researcher topic profiles rebuilt from v3 LLM classification.",
                "method": metadata.get("method"),
                "model": metadata.get("model"),
                "researcher_count": len(profiles),
            },
            "profiles": sorted(profiles, key=lambda p: (p["group"], p["name"])),
        })
        print(f"  Wrote {len(profiles)} researcher profiles to new_core_topic_profiles.json")

    # ── Summary ──
    print(f"\n{'='*60}")
    print("Regeneration complete.")
    print("Regenerated artifacts:")
    print(f"  {OUTPUT_VENUE_VECTORS}")
    print(f"  {OUTPUT_VENUE_EVOLUTION}")
    if INPUT_CORE.exists():
        print(f"  {DATA_DIR / 'new_core_topic_profiles.json'}")
    print("\nNext: run validate_classification_v3.py to verify outputs.")


if __name__ == "__main__":
    main()
