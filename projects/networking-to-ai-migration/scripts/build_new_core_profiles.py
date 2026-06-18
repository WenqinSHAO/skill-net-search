#!/usr/bin/env python3
"""Build descriptive researcher profiles for the repaired new-core split.

This does not classify research topics. It derives coverage-safe, deterministic
researcher profiles directly from data/new_core_clean_papers.json so every
new-core researcher, including DBLP-only complete newcomers, is represented.

Outputs:
  - data/new_core_researcher_profiles.json
  - data/new_core_researcher_profiles.csv
"""

from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

INPUT_PAPERS = DATA_DIR / "new_core_clean_papers.json"
INPUT_CORE = DATA_DIR / "new_core.json"
INPUT_ITINERARIES = DATA_DIR / "researcher_itineraries.json"
OUTPUT_JSON = DATA_DIR / "new_core_researcher_profiles.json"
OUTPUT_CSV = DATA_DIR / "new_core_researcher_profiles.csv"

BASELINE_YEARS = set(range(2018, 2023))
NEW_CORE_YEARS = set(range(2023, 2027))


def load_json(path: Path) -> Any:
    with open(path) as f:
        return json.load(f)


def author_role(author_index: int, author_count: int) -> str:
    if author_count == 1:
        return "single"
    if author_index == 0:
        return "first"
    if author_index == author_count - 1:
        return "last"
    return "middle"


def summarize_roles(roles: list[str]) -> dict[str, Any]:
    c = Counter(roles)
    total = sum(c.values())
    if total == 0:
        label = "unknown"
    elif c["first"] + c["single"] >= total * 0.5:
        label = "mostly_lead"
    elif c["last"] >= total * 0.5:
        label = "mostly_senior"
    elif c["middle"] >= total * 0.5:
        label = "mostly_collaborator"
    else:
        label = "mixed"
    return {
        "paper_count": total,
        "first_count": c["first"],
        "middle_count": c["middle"],
        "last_count": c["last"],
        "single_count": c["single"],
        "first_share": round(c["first"] / total, 4) if total else None,
        "middle_share": round(c["middle"] / total, 4) if total else None,
        "last_share": round(c["last"] / total, 4) if total else None,
        "single_share": round(c["single"] / total, 4) if total else None,
        "author_role_profile": label,
    }


def compact_counts(counter: Counter) -> list[dict[str, Any]]:
    return [{"key": key, "count": count} for key, count in counter.most_common()]


def main() -> None:
    papers_data = load_json(INPUT_PAPERS)
    core_data = load_json(INPUT_CORE)
    itins = load_json(INPUT_ITINERARIES)

    group_by_pid = {}
    core_entry_by_pid = {}
    for group_name, group in core_data["tripartite_split"].items():
        singular = {"stayers": "stayer", "newcomers": "newcomer", "dropouts": "dropout"}[group_name]
        for researcher in group["researchers"]:
            pid = researcher["dblp_pid"]
            group_by_pid[pid] = singular
            core_entry_by_pid[pid] = researcher

    itinerary_pids = {r.get("dblp_pid") for r in itins.get("researchers", []) if r.get("dblp_pid")}
    name_by_pid = {pid: entry.get("name", "Unknown") for pid, entry in core_entry_by_pid.items()}

    profile = defaultdict(lambda: {
        "baseline_papers": [],
        "new_core_papers": [],
        "baseline_roles": [],
        "new_core_roles": [],
        "baseline_venues": Counter(),
        "new_core_venues": Counter(),
        "baseline_years": Counter(),
        "new_core_years": Counter(),
        "source_counts": Counter(),
        "partial_pid_paper_count": 0,
    })

    for paper in papers_data.get("papers", []):
        if not paper.get("included_in_new_core_scope"):
            continue
        year = int(paper.get("year") or 0)
        period = "baseline" if year in BASELINE_YEARS else "new_core" if year in NEW_CORE_YEARS else None
        if period is None:
            continue
        authors = paper.get("authors", [])
        author_count = len(authors)
        for idx, author in enumerate(authors):
            pid = author.get("pid", "")
            if pid not in group_by_pid:
                continue
            name_by_pid.setdefault(pid, author.get("name", "Unknown"))
            rec = profile[pid]
            paper_ref = {
                "title": paper.get("title", ""),
                "venue": paper.get("venue_group", paper.get("venue", "")),
                "raw_venue": paper.get("venue", ""),
                "year": year,
                "author_role": author_role(idx, author_count),
                "author_count": author_count,
                "sources": paper.get("sources", []),
                "partial_author_pids": paper.get("partial_author_pids", False),
            }
            rec[f"{period}_papers"].append(paper_ref)
            rec[f"{period}_roles"].append(paper_ref["author_role"])
            rec[f"{period}_venues"][paper_ref["venue"]] += 1
            rec[f"{period}_years"][str(year)] += 1
            for source in paper.get("sources", []):
                rec["source_counts"][source] += 1
            if paper.get("partial_author_pids"):
                rec["partial_pid_paper_count"] += 1

    rows = []
    for pid, group in sorted(group_by_pid.items(), key=lambda item: (item[1], name_by_pid.get(item[0], ""))):
        rec = profile[pid]
        baseline_count = len(rec["baseline_papers"])
        new_count = len(rec["new_core_papers"])
        rows.append({
            "dblp_pid": pid,
            "name": name_by_pid.get(pid, "Unknown"),
            "group": group,
            "baseline_top_networking_count": baseline_count,
            "new_core_top_networking_count": new_count,
            "in_itinerary": pid in itinerary_pids,
            "profile_coverage": "canonical_clean_paper_table",
            "baseline_venue_counts": compact_counts(rec["baseline_venues"]),
            "new_core_venue_counts": compact_counts(rec["new_core_venues"]),
            "baseline_year_counts": dict(sorted(rec["baseline_years"].items())),
            "new_core_year_counts": dict(sorted(rec["new_core_years"].items())),
            "baseline_author_roles": summarize_roles(rec["baseline_roles"]),
            "new_core_author_roles": summarize_roles(rec["new_core_roles"]),
            "source_counts": dict(rec["source_counts"]),
            "partial_pid_paper_count": rec["partial_pid_paper_count"],
            "baseline_papers": sorted(rec["baseline_papers"], key=lambda p: (p["year"], p["venue"], p["title"])),
            "new_core_papers": sorted(rec["new_core_papers"], key=lambda p: (p["year"], p["venue"], p["title"])),
        })

    summary = {
        "total_profiles": len(rows),
        "by_group": dict(Counter(r["group"] for r in rows)),
        "not_in_itinerary": sum(1 for r in rows if not r["in_itinerary"]),
        "profiles_with_zero_new_core_papers": sum(1 for r in rows if r["new_core_top_networking_count"] == 0),
    }

    output = {
        "metadata": {
            "phase": "build_new_core_profiles",
            "description": "Descriptive researcher profiles derived from canonical new-core clean paper table.",
            "input_papers": str(INPUT_PAPERS.relative_to(PROJECT_DIR)),
            "input_core": str(INPUT_CORE.relative_to(PROJECT_DIR)),
        },
        "summary": summary,
        "researchers": rows,
    }
    with open(OUTPUT_JSON, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    with open(OUTPUT_CSV, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "name", "dblp_pid", "group", "baseline_top_networking_count",
            "new_core_top_networking_count", "in_itinerary", "baseline_author_role",
            "new_core_author_role", "partial_pid_paper_count", "new_core_venue_counts",
        ])
        writer.writeheader()
        for r in rows:
            writer.writerow({
                "name": r["name"],
                "dblp_pid": r["dblp_pid"],
                "group": r["group"],
                "baseline_top_networking_count": r["baseline_top_networking_count"],
                "new_core_top_networking_count": r["new_core_top_networking_count"],
                "in_itinerary": r["in_itinerary"],
                "baseline_author_role": r["baseline_author_roles"]["author_role_profile"],
                "new_core_author_role": r["new_core_author_roles"]["author_role_profile"],
                "partial_pid_paper_count": r["partial_pid_paper_count"],
                "new_core_venue_counts": "; ".join(f"{x['key']}:{x['count']}" for x in r["new_core_venue_counts"]),
            })

    print(f"Wrote {OUTPUT_JSON}")
    print(f"Wrote {OUTPUT_CSV}")
    print(summary)


if __name__ == "__main__":
    main()
