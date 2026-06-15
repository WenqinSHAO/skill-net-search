#!/usr/bin/env python3
"""MLSys sensitivity check: recompute venue-family deltas with MLSys as AI_ML.

The default venue_family_map.json classifies MLSys under 'systems'.
This script recomputes per-researcher delta profiles with MLSys mapped to
'AI_ML' instead, and reports which researchers' profiles change materially.

Output: data/mlsys_sensitivity_check.json
"""

import json
import sys
from pathlib import Path
from collections import defaultdict

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

FEATURE_VECTORS_FILE = DATA_DIR / "core99_feature_vectors.json"
VENUE_FAMILY_FILE = DATA_DIR / "venue_family_map.json"
OUTPUT_FILE = DATA_DIR / "mlsys_sensitivity_check.json"

# The default family assignment for MLSys
DEFAULT_FAMILY = "systems"
ALTERNATIVE_FAMILY = "AI_ML"

# Venues that host MLSys papers (DBLP canonical form)
MLSYS_VENUE_NAMES = [
    "MLSys",
    "Conference on Machine Learning and Systems",
    "Proceedings of Machine Learning and Systems",
]


def load_venue_to_family() -> dict[str, str]:
    """Load venue->family mapping, applying the default classification."""
    with open(VENUE_FAMILY_FILE) as f:
        vf = json.load(f)
    aliases = vf.get("aliases", {})
    families = vf.get("venue_families", {})

    venue_to_family = {}
    for family, venues in families.items():
        for venue in venues:
            venue_to_family[venue] = family
    # Apply aliases
    for full_name, short_name in aliases.items():
        if short_name in venue_to_family:
            venue_to_family[full_name] = venue_to_family[short_name]
    return venue_to_family


def compute_researcher_deltas(
    itinerary_file: Path,
    venue_to_family: dict[str, str],
    mlsys_family: str,
) -> list[dict]:
    """Recompute delta profiles with the specified MLSys family assignment.

    This is approximate — it uses the venue_family_map at the itinerary level.
    For a full recomputation, we'd need to re-run build_core99_attributes.py.
    Instead, we estimate the effect by identifying researchers with MLSys papers
    and computing the per-paper reclassification impact.
    """
    with open(itinerary_file) as f:
        data = json.load(f)

    researchers = data.get("researchers", [])
    results = []

    for r in researchers:
        name = r.get("name", "")
        baseline_top = int(r.get("baseline_top_networking_count", 0))
        if baseline_top <= 6:
            continue  # Not core-99

        # Count MLSys papers by period
        mlsys_bl = 0
        mlsys_post = 0
        total_bl = 0
        total_post = 0

        itinerary = r.get("itinerary", {})
        for year_str, papers in itinerary.items():
            year = int(year_str)
            for paper in papers:
                venue = paper.get("venue", "")
                # Check if this is an MLSys paper
                is_mlsys = any(
                    mname.lower() in venue.lower() for mname in MLSYS_VENUE_NAMES
                )
                # Must also be a clean paper (inproceedings, not excluded)
                is_clean = paper.get("included_in_analysis", True)

                if not is_clean:
                    continue

                if 2018 <= year <= 2022:
                    total_bl += 1
                    if is_mlsys:
                        mlsys_bl += 1
                elif 2023 <= year <= 2026:
                    total_post += 1
                    if is_mlsys:
                        mlsys_post += 1

        if mlsys_bl == 0 and mlsys_post == 0:
            continue  # No MLSys papers, unaffected

        # Estimate delta impact: moving MLSys from systems to AI_ML
        # For each MLSys paper, the systems count decreases by 1 and AI_ML increases by 1
        # As a percentage share: delta_systems_pct = -mlsys / total * 100
        bl_systems_shift = -mlsys_bl / max(total_bl, 1) * 100
        bl_aiml_shift = mlsys_bl / max(total_bl, 1) * 100
        post_systems_shift = -mlsys_post / max(total_post, 1) * 100
        post_aiml_shift = mlsys_post / max(total_post, 1) * 100

        # Net delta change: (post_aiml - post_systems) - (bl_aiml - bl_systems)
        # Actually: the delta profile is post_pct - baseline_pct
        # Delta change for systems: post_systems_shift - bl_systems_shift
        # Delta change for AI_ML: post_aiml_shift - bl_aiml_shift
        delta_systems_change = post_systems_shift - bl_systems_shift
        delta_aiml_change = post_aiml_shift - bl_aiml_shift

        results.append({
            "name": name,
            "mlsys_papers_baseline": mlsys_bl,
            "mlsys_papers_post2023": mlsys_post,
            "total_clean_papers_baseline": total_bl,
            "total_clean_papers_post2023": total_post,
            "estimated_impact": {
                "delta_systems_change_pp": round(delta_systems_change, 2),
                "delta_AI_ML_change_pp": round(delta_aiml_change, 2),
                "net_magnitude": round(abs(delta_systems_change) + abs(delta_aiml_change), 2),
            },
            "interpretation": (
                "MLSys reclassification would shift systems delta by "
                f"{delta_systems_change:+.1f}pp and AI_ML delta by "
                f"{delta_aiml_change:+.1f}pp"
            ),
        })

    return results


def main():
    if not FEATURE_VECTORS_FILE.exists():
        print(f"ERROR: {FEATURE_VECTORS_FILE} not found.", file=sys.stderr)
        sys.exit(1)

    # Find the itinerary file
    itinerary_file = DATA_DIR / "researcher_itineraries.json"
    if not itinerary_file.exists():
        print(
            f"ERROR: {itinerary_file} not found. "
            "Cannot compute MLSys sensitivity without itineraries.",
            file=sys.stderr,
        )
        sys.exit(1)

    venue_to_family = load_venue_to_family()
    default_mlsys = venue_to_family.get("MLSys", "not found")
    print(f"Default MLSys classification: {default_mlsys}")
    print(f"Alternative MLSys classification: {ALTERNATIVE_FAMILY}")
    print()

    results = compute_researcher_deltas(
        itinerary_file, venue_to_family, ALTERNATIVE_FAMILY
    )

    if not results:
        print("No researchers with MLSys papers found.")
        return

    # Sort by impact magnitude
    results.sort(key=lambda r: r["estimated_impact"]["net_magnitude"], reverse=True)

    print(f"Researchers with MLSys papers: {len(results)}")
    print()
    for r in results:
        mag = r["estimated_impact"]["net_magnitude"]
        if mag >= 2.0:
            significance = "MATERIAL (>2pp)"
        elif mag >= 1.0:
            significance = "MODERATE (1-2pp)"
        else:
            significance = "minor (<1pp)"

        print(
            f"  {r['name']}: "
            f"MLSys {r['mlsys_papers_baseline']}→{r['mlsys_papers_post2023']} papers "
            f"(bl/post), "
            f"systems Δ={r['estimated_impact']['delta_systems_change_pp']:+.1f}pp, "
            f"AI_ML Δ={r['estimated_impact']['delta_AI_ML_change_pp']:+.1f}pp "
            f"[{significance}]"
        )

    # Summary
    material = [r for r in results if r["estimated_impact"]["net_magnitude"] >= 2.0]
    moderate = [
        r
        for r in results
        if 1.0 <= r["estimated_impact"]["net_magnitude"] < 2.0
    ]
    minor = [r for r in results if r["estimated_impact"]["net_magnitude"] < 1.0]

    output = {
        "metadata": {
            "description": (
                "Sensitivity check: recomputing venue-family deltas with MLSys "
                f"classified as '{ALTERNATIVE_FAMILY}' instead of '{DEFAULT_FAMILY}'."
            ),
            "default_classification": DEFAULT_FAMILY,
            "alternative_classification": ALTERNATIVE_FAMILY,
            "researchers_with_mlsys_papers": len(results),
            "material_impact_count": len(material),
            "moderate_impact_count": len(moderate),
            "minor_impact_count": len(minor),
            "material_threshold_pp": 2.0,
            "note": (
                "These are estimated impacts based on itinerary-level MLSys paper "
                "counts. Full recomputation of feature vectors would require "
                "re-running build_core99_attributes.py with a modified venue_family_map."
            ),
        },
        "researchers": results,
    }

    with open(OUTPUT_FILE, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\nSummary: {len(material)} material, {len(moderate)} moderate, {len(minor)} minor")
    print(f"Wrote {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
