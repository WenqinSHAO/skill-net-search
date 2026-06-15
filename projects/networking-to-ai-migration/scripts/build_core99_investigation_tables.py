#!/usr/bin/env python3
"""Build deterministic investigation tables for core-99 questions 1-3."""

from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
ITINERARIES_FILE = DATA_DIR / "researcher_itineraries.json"
ATTRIBUTES_FILE = DATA_DIR / "core99_researcher_attributes.json"
RAW_PAPERS_FILE = DATA_DIR / "raw_dblp_papers.json"
VENUE_FAMILY_FILE = DATA_DIR / "venue_family_map.json"

SUMMARY_JSON = DATA_DIR / "core99_investigation_summary.json"
TRANSITIONS_CSV = DATA_DIR / "core99_researcher_venue_family_transitions.csv"
DECREASE_CSV = DATA_DIR / "core99_topnet_decrease_clean_flat_or_increase.csv"
FLAT_INCREASE_CSV = DATA_DIR / "core99_topnet_flat_or_increase_profiles.csv"
CONCENTRATION_CSV = DATA_DIR / "top_venue_author_concentration_2018_2022.csv"
SUMMARY_MD = PROJECT_DIR / "CORE99_INVESTIGATION_TABLES.md"

BASELINE_YEARS = set(range(2018, 2023))
POST_YEARS = set(range(2023, 2027))
QUALIFYING_VENUES = {"SIGCOMM", "NSDI", "CoNEXT", "HotNets", "IMC"}

def _load_venue_family_map():
    """Load venue family map from JSON (single source of truth)."""
    with open(VENUE_FAMILY_FILE) as f:
        data = json.load(f)
    return data.get("aliases", {}), data.get("venue_families", {})

VENUE_ALIASES, VENUE_FAMILY_MAP = _load_venue_family_map()


def normalize_venue(venue: str) -> str:
    venue = (venue or "Unknown").strip()
    return VENUE_ALIASES.get(venue, venue)


def venue_family(venue: str) -> str:
    return VENUE_FAMILY_MAP.get(normalize_venue(venue), "unknown")


def flatten_itinerary(researcher: dict[str, Any]) -> list[dict[str, Any]]:
    papers = []
    for year, items in researcher.get("itinerary", {}).items():
        for item in items:
            paper = dict(item)
            paper["year"] = int(paper.get("year") or year)
            paper["venue_normalized"] = normalize_venue(paper.get("venue", ""))
            paper["venue_family"] = venue_family(paper["venue_normalized"])
            papers.append(paper)
    return papers


def period(papers: list[dict[str, Any]], years: set[int]) -> list[dict[str, Any]]:
    return [p for p in papers if p["year"] in years]


def counts(items: list[str]) -> Counter:
    return Counter(items)


def compact(counter: Counter, limit: int | None = None) -> str:
    return "; ".join(f"{k}:{v}" for k, v in counter.most_common(limit))


def list_compact(counter: Counter, limit: int | None = None) -> list[dict[str, Any]]:
    return [{"label": k, "count": v} for k, v in counter.most_common(limit)]


def gini(values: list[int]) -> float:
    if not values:
        return 0.0
    sorted_values = sorted(values)
    total = sum(sorted_values)
    if total == 0:
        return 0.0
    n = len(sorted_values)
    weighted = sum((i + 1) * value for i, value in enumerate(sorted_values))
    return round((2 * weighted) / (n * total) - (n + 1) / n, 4)


def hhi(values: list[int]) -> float:
    total = sum(values)
    if total == 0:
        return 0.0
    return round(sum((value / total) ** 2 for value in values), 4)


def write_csv(path: Path, rows: list[dict[str, Any]], fields: list[str]) -> None:
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def researcher_transition_rows(itineraries: list[dict[str, Any]], attrs: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    rows = []
    for researcher in itineraries:
        pid = researcher["dblp_pid"]
        if pid not in attrs:
            continue
        papers = flatten_itinerary(researcher)
        baseline = period(papers, BASELINE_YEARS)
        post = period(papers, POST_YEARS)
        baseline_families = counts([p["venue_family"] for p in baseline])
        post_families = counts([p["venue_family"] for p in post])
        baseline_venues = counts([p["venue_normalized"] for p in baseline])
        post_venues = counts([p["venue_normalized"] for p in post])
        attr = attrs[pid]
        ident = attr.get("identity", {})
        rows.append({
            "name": researcher["name"],
            "dblp_pid": pid,
            "top_networking_rate_change": attr["top_networking_rate_change"],
            "top_networking_rate_ratio_post_vs_baseline": attr["top_networking_rate_ratio_post_vs_baseline"],
            "clean_publication_rate_change": attr["clean_publication_rate_change"],
            "clean_publication_rate_ratio_post_vs_baseline": attr["clean_publication_rate_ratio_post_vs_baseline"],
            "baseline_clean_publication_count": attr["baseline_clean_publication_count"],
            "post2023_clean_publication_count": attr["post2023_clean_publication_count"],
            "baseline_top_networking_count": attr["baseline_top_networking_count"],
            "post2023_top_networking_count": attr["post2023_top_networking_count"],
            "baseline_author_role_profile": attr["baseline_author_role_profile"],
            "post2023_author_role_profile": attr["post2023_author_role_profile"],
            "qualifying_venue_mix": attr["qualifying_venue_mix"],
            "region": ident.get("region", "Unknown"),
            "sector": ident.get("sector", "Unknown"),
            "baseline_venue_families": compact(baseline_families),
            "post2023_venue_families": compact(post_families),
            "baseline_top_venues": compact(baseline_venues, 8),
            "post2023_top_venues": compact(post_venues, 8),
        })
    return rows


def aggregate_family_shift(rows: list[dict[str, Any]], pids: set[str], itineraries: list[dict[str, Any]]) -> dict[str, Any]:
    baseline_counter = Counter()
    post_counter = Counter()
    baseline_venue_counter = Counter()
    post_venue_counter = Counter()
    for researcher in itineraries:
        if researcher["dblp_pid"] not in pids:
            continue
        papers = flatten_itinerary(researcher)
        for paper in period(papers, BASELINE_YEARS):
            baseline_counter[paper["venue_family"]] += 1
            baseline_venue_counter[paper["venue_normalized"]] += 1
        for paper in period(papers, POST_YEARS):
            post_counter[paper["venue_family"]] += 1
            post_venue_counter[paper["venue_normalized"]] += 1
    return {
        "baseline_families": list_compact(baseline_counter),
        "post2023_families": list_compact(post_counter),
        "baseline_venues": list_compact(baseline_venue_counter, 25),
        "post2023_venues": list_compact(post_venue_counter, 25),
    }


def concentration_rows(raw_papers: list[dict[str, Any]], core_pids: set[str]) -> list[dict[str, Any]]:
    rows = []
    for venue in ["SIGCOMM", "NSDI", "CoNEXT", "HotNets", "IMC"]:
        papers = [p for p in raw_papers if normalize_venue(p.get("venue", "")) == venue and p.get("year") in BASELINE_YEARS]
        author_counts = Counter()
        core_author_counts = Counter()
        core_paper_count = 0
        for paper in papers:
            paper_core = False
            for author in paper.get("authors", []):
                pid = author.get("pid")
                if not pid:
                    continue
                author_counts[pid] += 1
                if pid in core_pids:
                    core_author_counts[pid] += 1
                    paper_core = True
            if paper_core:
                core_paper_count += 1
        vals = list(author_counts.values())
        repeat_authors = sum(1 for v in vals if v >= 2)
        rows.append({
            "venue": venue,
            "baseline_papers": len(papers),
            "unique_authors": len(author_counts),
            "author_paper_incidences": sum(vals),
            "papers_per_unique_author": round(len(papers) / len(author_counts), 4) if author_counts else 0,
            "repeat_author_count_ge2": repeat_authors,
            "repeat_author_share_ge2": round(repeat_authors / len(author_counts), 4) if author_counts else 0,
            "author_paper_gini": gini(vals),
            "author_paper_hhi": hhi(vals),
            "core99_unique_authors": len(core_author_counts),
            "core99_author_paper_incidences": sum(core_author_counts.values()),
            "core99_papers": core_paper_count,
            "core99_paper_share": round(core_paper_count / len(papers), 4) if papers else 0,
        })
    return rows




def format_label_counts(items: list[dict[str, Any]]) -> str:
    return ", ".join(f"{item['label']} ({item['count']})" for item in items)


def write_markdown(summary: dict[str, Any], transitions: list[dict[str, Any]],
                   decrease_rows: list[dict[str, Any]], flat_rows: list[dict[str, Any]],
                   concentration: list[dict[str, Any]]) -> None:
    lines = [
        "# Core-99 Investigation Tables",
        "",
        "Deterministic tables for the first three investigation questions. No LLM interpretation is used here.",
        "",
        "## Question 1: Top-Net Decrease, Overall Flat/Increase",
        "",
        f"- Researchers in slice: {summary['question1']['researcher_count']}",
        "- Slice rule: `top_networking_rate_change = decreased` and `clean_publication_rate_change in {flat, increased}`.",
        "",
        "### Aggregate Venue-Family Shift",
        "",
        f"- Baseline families: {format_label_counts(summary['question1']['aggregate_shift']['baseline_families'])}",
        f"- Post-2023 families: {format_label_counts(summary['question1']['aggregate_shift']['post2023_families'])}",
        "",
        "Top post-2023 venues in this slice:",
        "",
        "| Venue | Papers |",
        "|---|---:|",
    ]
    for item in summary["question1"]["aggregate_shift"]["post2023_venues"][:15]:
        lines.append(f"| {item['label']} | {item['count']} |")

    lines.extend([
        "",
        "## Question 2: Top-Net Flat/Increase Profiles",
        "",
        f"- Researchers in slice: {summary['question2']['researcher_count']}",
        "- Slice rule: `top_networking_rate_change in {flat, increased}`.",
        "",
        "### Profile Distributions",
        "",
    ])
    for title, key in [
        ("Top-net trend", "top_networking_rate_change_distribution"),
        ("Qualifying venue mix", "qualifying_venue_mix_distribution"),
        ("Baseline author role", "baseline_author_role_profile_distribution"),
        ("Post-2023 author role", "post2023_author_role_profile_distribution"),
        ("Region", "region_distribution"),
        ("Sector", "sector_distribution"),
    ]:
        lines.extend([f"#### {title}", "", "| Label | Researchers |", "|---|---:|"])
        for label, count in summary["question2"][key].items():
            lines.append(f"| {label} | {count} |")
        lines.append("")

    lines.extend([
        "## Question 3: Baseline Top-Venue Author Concentration",
        "",
        "Computed from `data/raw_dblp_papers.json` for 2018-2022 accepted papers in the five qualifying venues.",
        "",
        "| Venue | Papers | Unique authors | Repeat-author share >=2 | Gini | HHI | Core-99 paper share |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ])
    for row in concentration:
        lines.append(
            f"| {row['venue']} | {row['baseline_papers']} | {row['unique_authors']} | "
            f"{row['repeat_author_share_ge2']} | {row['author_paper_gini']} | "
            f"{row['author_paper_hhi']} | {row['core99_paper_share']} |"
        )

    lines.extend([
        "",
        "## Output Files",
        "",
        "- `data/core99_investigation_summary.json`",
        "- `data/core99_researcher_venue_family_transitions.csv`",
        "- `data/core99_topnet_decrease_clean_flat_or_increase.csv`",
        "- `data/core99_topnet_flat_or_increase_profiles.csv`",
        "- `data/top_venue_author_concentration_2018_2022.csv`",
        "- `data/venue_family_map.json`",
        "",
    ])
    SUMMARY_MD.write_text("\n".join(lines))


def run() -> dict[str, Any]:
    itineraries = json.load(open(ITINERARIES_FILE))["researchers"]
    attr_packet = json.load(open(ATTRIBUTES_FILE))
    attrs = {r["dblp_pid"]: r for r in attr_packet["researchers"]}
    raw_papers = json.load(open(RAW_PAPERS_FILE))
    core_pids = set(attrs)

    transitions = researcher_transition_rows(itineraries, attrs)
    decrease_rows = [
        r for r in transitions
        if r["top_networking_rate_change"] == "decreased"
        and r["clean_publication_rate_change"] in {"flat", "increased"}
    ]
    flat_rows = [
        r for r in transitions
        if r["top_networking_rate_change"] in {"flat", "increased"}
    ]
    decrease_pids = {r["dblp_pid"] for r in decrease_rows}
    flat_pids = {r["dblp_pid"] for r in flat_rows}
    concentration = concentration_rows(raw_papers, core_pids)

    def dist(rows: list[dict[str, Any]], key: str) -> dict[str, int]:
        return dict(Counter(str(r.get(key, "Unknown")) for r in rows).most_common())

    summary = {
        "metadata": {
            "phase": "build_core99_investigation_tables",
            "raw_data_policy": "Derived tables only; source cohort/publication records are not modified.",
            "core99_researchers": len(transitions),
            "venue_family_map_file": str(VENUE_FAMILY_FILE.relative_to(PROJECT_DIR)),
        },
        "question1": {
            "researcher_count": len(decrease_rows),
            "slice_rule": "top_networking_rate_change = decreased and clean_publication_rate_change in {flat, increased}",
            "aggregate_shift": aggregate_family_shift(decrease_rows, decrease_pids, itineraries),
        },
        "question2": {
            "researcher_count": len(flat_rows),
            "slice_rule": "top_networking_rate_change in {flat, increased}",
            "aggregate_shift": aggregate_family_shift(flat_rows, flat_pids, itineraries),
            "top_networking_rate_change_distribution": dist(flat_rows, "top_networking_rate_change"),
            "qualifying_venue_mix_distribution": dist(flat_rows, "qualifying_venue_mix"),
            "baseline_author_role_profile_distribution": dist(flat_rows, "baseline_author_role_profile"),
            "post2023_author_role_profile_distribution": dist(flat_rows, "post2023_author_role_profile"),
            "region_distribution": dist(flat_rows, "region"),
            "sector_distribution": dist(flat_rows, "sector"),
        },
        "question3": {
            "venue_author_concentration": concentration,
        },
    }

    write_csv(TRANSITIONS_CSV, transitions, list(transitions[0].keys()))
    write_csv(DECREASE_CSV, decrease_rows, list(transitions[0].keys()))
    write_csv(FLAT_INCREASE_CSV, flat_rows, list(transitions[0].keys()))
    write_csv(CONCENTRATION_CSV, concentration, list(concentration[0].keys()))
    with open(SUMMARY_JSON, "w") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    with open(VENUE_FAMILY_FILE, "w") as f:
        json.dump({
            "metadata": {
                "purpose": "Conservative venue-context labels for deterministic itinerary summaries; not topic labels.",
                "unknown_policy": "Unmapped venues remain unknown.",
            },
            "aliases": VENUE_ALIASES,
            "venue_families": VENUE_FAMILY_MAP,
        }, f, indent=2, ensure_ascii=False)
    write_markdown(summary, transitions, decrease_rows, flat_rows, concentration)

    print(f"Core-99 researchers: {len(transitions)}")
    print(f"Question 1 slice: {len(decrease_rows)}")
    print(f"Question 2 slice: {len(flat_rows)}")
    print(f"Wrote {SUMMARY_JSON}")
    print(f"Wrote {SUMMARY_MD}")
    return summary


if __name__ == "__main__":
    run()
