#!/usr/bin/env python3
"""Build year-by-year researcher itineraries for trajectory discovery.

The itinerary artifact is intentionally raw-evidence-first: it groups clean
conference papers by researcher and year without imposing migration labels.
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from publication_scope import exclusion_reason

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
INPUT_FILE_GEO = DATA_DIR / "publication_history_geo.json"
INPUT_FILE_ZONES = DATA_DIR / "publication_history_zones.json"
INPUT_FILE_PUBLICATIONS = DATA_DIR / "publication_history.json"
COHORT_FILE = DATA_DIR / "qualified_cohort.json"
INPUT_FILE = (
    INPUT_FILE_GEO if INPUT_FILE_GEO.exists()
    else INPUT_FILE_ZONES if INPUT_FILE_ZONES.exists()
    else INPUT_FILE_PUBLICATIONS
)
OUTPUT_FILE = DATA_DIR / "researcher_itineraries.json"
TOP100_FILE = DATA_DIR / "top100_itineraries.json"

BASELINE_START = 2018
BASELINE_END = 2022
OBSERVATION_END = 2026
QUALIFYING_VENUES = {"SIGCOMM", "NSDI", "CoNEXT", "HotNets", "IMC", "PACMNET"}
TOP_N = 100


def is_clean_analysis_paper(paper: dict[str, Any]) -> bool:
    # Apply current scope rules at itinerary-build time so older derived
    # publication-history files do not keep stale clean/excluded flags.
    if exclusion_reason(paper) is not None:
        return False
    if not paper.get("included_in_analysis", True):
        return False
    zone = paper.get("zone")
    return zone != "Excluded"


def is_top_networking_baseline_paper(paper: dict[str, Any]) -> bool:
    return (
        is_clean_analysis_paper(paper)
        and BASELINE_START <= paper.get("year", 0) <= BASELINE_END
        and paper.get("venue") in QUALIFYING_VENUES
    )


AUTHOR_ALIASES = {
    "Kimberly C. Claffy": {"K. C. Claffy"},
    "Philip Brighten Godfrey": {"Brighten Godfrey"},
    "Ran Ben Basat": {"Ran Ben-Basat"},
    "Matthew Luckie": {"Matthew J. Luckie"},
    "Ítalo Cunha": {"Ítalo S. Cunha"},
    "Haitham Hassanieh": {"Haitham Al-Hassanieh"},
    "Vasileios Giotsas": {"Vasilis Giotsas"},
    "Manya Ghobadi": {"Monia Ghobadi"},
}


def normalize_author_name(name: str) -> str:
    return re.sub(r"\s+\d{4}$", "", name or "").strip().lower()


def candidate_author_names(researcher_name: str) -> set[str]:
    return {researcher_name, *AUTHOR_ALIASES.get(researcher_name, set())}


def author_role_fields(paper: dict[str, Any], researcher_name: str) -> dict[str, Any]:
    authors = paper.get("authors") or []
    if not authors:
        return {
            "authors": [],
            "author_count": 0,
            "author_position": None,
            "is_first_author": False,
            "is_last_author": False,
            "is_single_author": False,
            "author_match_confidence": "missing_authors",
        }

    candidates = candidate_author_names(researcher_name)
    exact_positions = [i + 1 for i, author in enumerate(authors) if author in candidates]
    if exact_positions:
        position = exact_positions[0]
        confidence = "exact" if researcher_name in authors else "alias"
    else:
        normalized_candidates = {normalize_author_name(name) for name in candidates}
        fuzzy_positions = [
            i + 1 for i, author in enumerate(authors)
            if normalize_author_name(author) in normalized_candidates
        ]
        position = fuzzy_positions[0] if fuzzy_positions else None
        confidence = "normalized" if position is not None else "unmatched"

    author_count = len(authors)
    return {
        "authors": authors,
        "author_count": author_count,
        "author_position": position,
        "is_first_author": position == 1,
        "is_last_author": position == author_count if position is not None else False,
        "is_single_author": author_count == 1 and position == 1,
        "author_match_confidence": confidence,
    }


def compact_paper(paper: dict[str, Any], researcher_name: str) -> dict[str, Any]:
    item = {
        "title": paper.get("title", ""),
        "venue": paper.get("venue", ""),
        "year": paper.get("year"),
        "dblp_url": paper.get("dblp_url", ""),
        "doi": paper.get("doi", ""),
    }
    item.update(author_role_fields(paper, researcher_name))
    if paper.get("abstract"):
        item["abstract"] = paper["abstract"]
    if paper.get("zone"):
        item["aux_zone"] = paper["zone"]
    if paper.get("zone_confidence"):
        item["aux_zone_confidence"] = paper["zone_confidence"]
    if paper.get("classification_reason"):
        item["aux_classification_reason"] = paper["classification_reason"]
    return item


def build_itinerary(researcher: dict[str, Any], cohort_entry: dict[str, Any] | None = None) -> dict[str, Any]:
    papers = researcher.get("papers", [])
    yearly: dict[str, list[dict[str, Any]]] = defaultdict(list)
    clean_count_by_year = Counter()
    venue_count = Counter()
    audit_counts = Counter()

    baseline_top_networking_papers = []

    for paper in papers:
        if not is_clean_analysis_paper(paper):
            audit_counts[f"excluded:{paper.get('exclusion_reason') or 'unknown'}"] += 1
            continue

        year = paper.get("year")
        if not year or year < BASELINE_START or year > OBSERVATION_END:
            audit_counts["outside_window"] += 1
            continue

        compact = compact_paper(paper, researcher.get("name", ""))
        yearly[str(year)].append(compact)
        clean_count_by_year[str(year)] += 1
        venue_count[paper.get("venue", "")] += 1

        if is_top_networking_baseline_paper(paper):
            baseline_top_networking_papers.append(compact)

    for year in yearly:
        yearly[year].sort(key=lambda p: (p.get("venue", ""), p.get("title", "")))

    baseline_count = (
        cohort_entry.get("paper_count", 0)
        if cohort_entry is not None
        else len(baseline_top_networking_papers)
    )
    clean_total = sum(clean_count_by_year.values())

    return {
        "name": researcher.get("name", ""),
        "dblp_pid": researcher.get("dblp_pid", ""),
        "identity": {
            "affiliation": researcher.get("affiliation"),
            "country_code": researcher.get("country_code"),
            "region": researcher.get("region", "Unknown"),
            "geo_source": researcher.get("source"),
            "sector": researcher.get("sector", "Unknown"),
        },
        "baseline_top_networking_count": baseline_count,
        "baseline_top_networking_papers": baseline_top_networking_papers,
        "clean_publication_count": clean_total,
        "clean_publication_count_by_year": dict(sorted(clean_count_by_year.items(), key=lambda x: int(x[0]))),
        "venue_count": dict(venue_count.most_common()),
        "audit_counts": dict(audit_counts),
        "itinerary": {year: yearly[year] for year in sorted(yearly, key=int)},
    }


def run() -> dict[str, Any]:
    if not INPUT_FILE.exists():
        print(f"ERROR: no publication history input found: {INPUT_FILE}", file=sys.stderr)
        sys.exit(1)

    with open(INPUT_FILE) as f:
        data = json.load(f)

    cohort_by_pid = {}
    cohort_size = None
    if COHORT_FILE.exists():
        with open(COHORT_FILE) as f:
            cohort_data = json.load(f)
        cohort_researchers = cohort_data.get("researchers", [])
        cohort_size = len(cohort_researchers)
        cohort_by_pid = {r.get("dblp_pid"): r for r in cohort_researchers}

    researchers = data.get("researchers", [])
    itineraries = [build_itinerary(r, cohort_by_pid.get(r.get("dblp_pid"))) for r in researchers]
    scoped = [r for r in itineraries if r["baseline_top_networking_count"] >= 1]
    scoped.sort(
        key=lambda r: (
            r["baseline_top_networking_count"],
            r["clean_publication_count"],
            r["name"],
        ),
        reverse=True,
    )

    top100 = scoped[:TOP_N]

    metadata = {
        "phase": "build_itineraries",
        "input_file": str(INPUT_FILE.relative_to(PROJECT_DIR)),
        "baseline_start": BASELINE_START,
        "baseline_end": BASELINE_END,
        "observation_end": OBSERVATION_END,
        "qualifying_venues": sorted(QUALIFYING_VENUES),
        "cohort_rule": ">=1 qualifying top-networking paper in 2018-2022",
        "researchers_in_input": len(researchers),
        "broad_cohort_size": cohort_size,
        "cohort_members_missing_publication_history": max(cohort_size - len(researchers), 0) if cohort_size is not None else None,
        "researchers_in_scope": len(scoped),
        "top_discovery_count": len(top100),
    }

    output = {"metadata": metadata, "researchers": scoped}
    top_output = {"metadata": metadata | {"subset": f"top_{TOP_N}_by_baseline_top_networking_count"}, "researchers": top100}

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    with open(TOP100_FILE, "w") as f:
        json.dump(top_output, f, indent=2, ensure_ascii=False)

    print(f"Input researchers: {len(researchers)}")
    print(f"In-scope researchers: {len(scoped)}")
    print(f"Top discovery subset: {len(top100)}")
    print(f"Output: {OUTPUT_FILE}")
    print(f"Top-{TOP_N}: {TOP100_FILE}")
    return output


if __name__ == "__main__":
    run()
