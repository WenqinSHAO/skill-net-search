#!/usr/bin/env python3
"""Build a derived review packet for the provisional selected sample.

The selected sample is currently defined as researchers with more than six
qualifying top-networking papers during the 2018-2022 baseline window. This
script does not filter or rewrite the raw cohort/itinerary artifacts; it creates
derived review files for deeper inspection.
"""

from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from statistics import median
from typing import Any

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
INPUT_FILE = DATA_DIR / "researcher_itineraries.json"
OUTPUT_JSON = DATA_DIR / "selected_sample_network_gt6_packet.json"
OUTPUT_CSV = DATA_DIR / "selected_sample_network_gt6_summary.csv"
OUTPUT_MD = PROJECT_DIR / "SELECTED_SAMPLE_NETWORK_GT6.md"

BASELINE_YEARS = {2018, 2019, 2020, 2021, 2022}
POST_YEARS = {2023, 2024, 2025, 2026}
QUALIFYING_VENUES = {"SIGCOMM", "NSDI", "CoNEXT", "HotNets", "IMC"}
NETWORK_THRESHOLD = 6
MAX_TITLES_PER_YEAR = 12

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "based", "by", "for", "from",
    "in", "into", "is", "of", "on", "or", "over", "the", "to", "toward",
    "towards", "using", "via", "with", "without",
    "adaptive", "analysis", "approach", "architectures", "automatic",
    "efficient", "enabling", "evaluating", "evaluation", "fast", "fine",
    "framework", "large", "new", "online", "performance", "practical",
    "rethinking", "scalable", "scaling", "system", "systems",
}


def normalize_title(title: str) -> str:
    return re.sub(r"\s+", " ", title.replace("&apos;", "'")).strip()


def title_tokens(title: str) -> list[str]:
    words = re.findall(r"[A-Za-z][A-Za-z0-9+\-]{2,}", title.lower())
    return [w for w in words if w not in STOPWORDS and not w.isdigit()]


def top_terms(papers: list[dict[str, Any]], n: int = 12) -> list[dict[str, Any]]:
    counts = Counter()
    for paper in papers:
        counts.update(title_tokens(paper.get("title", "")))
    return [{"term": term, "count": count} for term, count in counts.most_common(n)]


def year_int(year: str | int) -> int:
    return int(year)


def paper_year(paper: dict[str, Any]) -> int:
    return int(paper.get("year") or 0)


def flatten_itinerary(researcher: dict[str, Any]) -> list[dict[str, Any]]:
    papers = []
    for year, items in researcher.get("itinerary", {}).items():
        for item in items:
            paper = dict(item)
            paper["year"] = int(paper.get("year") or year)
            paper["title"] = normalize_title(paper.get("title", ""))
            paper["is_qualifying_top_networking"] = (
                paper["year"] in BASELINE_YEARS
                and paper.get("venue") in QUALIFYING_VENUES
            )
            papers.append(paper)
    papers.sort(key=lambda p: (paper_year(p), p.get("venue", ""), p.get("title", "")))
    return papers


def summarize_researcher(researcher: dict[str, Any]) -> dict[str, Any]:
    papers = flatten_itinerary(researcher)
    baseline = [p for p in papers if paper_year(p) in BASELINE_YEARS]
    post = [p for p in papers if paper_year(p) in POST_YEARS]
    baseline_network = [p for p in baseline if p.get("venue") in QUALIFYING_VENUES]
    venues = Counter(p.get("venue", "Unknown") for p in papers)
    years = Counter(str(paper_year(p)) for p in papers)
    post_venues = Counter(p.get("venue", "Unknown") for p in post)

    return {
        "name": researcher.get("name", ""),
        "dblp_pid": researcher.get("dblp_pid", ""),
        "identity": researcher.get("identity", {}),
        "baseline_top_networking_count": researcher.get("baseline_top_networking_count", 0),
        "clean_publication_count": researcher.get("clean_publication_count", 0),
        "baseline_clean_publication_count": len(baseline),
        "post2023_clean_publication_count": len(post),
        "baseline_networking_share": round(len(baseline_network) / len(baseline), 4) if baseline else None,
        "active_years": sorted(years, key=int),
        "count_by_year": dict(sorted(years.items(), key=lambda x: int(x[0]))),
        "top_venues": [{"venue": v, "count": c} for v, c in venues.most_common(12)],
        "post2023_top_venues": [{"venue": v, "count": c} for v, c in post_venues.most_common(8)],
        "baseline_title_terms": top_terms(baseline),
        "post2023_title_terms": top_terms(post),
        "all_title_terms": top_terms(papers),
        "papers_by_year": {
            str(year): [
                {
                    "title": p.get("title", ""),
                    "venue": p.get("venue", ""),
                    "dblp_url": p.get("dblp_url", ""),
                    "is_qualifying_top_networking": p.get("is_qualifying_top_networking", False),
                }
                for p in papers
                if paper_year(p) == year
            ]
            for year in range(2018, 2027)
            if any(paper_year(p) == year for p in papers)
        },
    }


def write_csv(rows: list[dict[str, Any]]) -> None:
    fields = [
        "name", "dblp_pid", "baseline_top_networking_count",
        "baseline_clean_publication_count", "post2023_clean_publication_count",
        "clean_publication_count", "baseline_networking_share",
        "top_venues", "post2023_top_venues", "baseline_title_terms",
        "post2023_title_terms", "region", "sector",
    ]
    with open(OUTPUT_CSV, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            ident = row.get("identity", {})
            writer.writerow({
                "name": row["name"],
                "dblp_pid": row["dblp_pid"],
                "baseline_top_networking_count": row["baseline_top_networking_count"],
                "baseline_clean_publication_count": row["baseline_clean_publication_count"],
                "post2023_clean_publication_count": row["post2023_clean_publication_count"],
                "clean_publication_count": row["clean_publication_count"],
                "baseline_networking_share": row["baseline_networking_share"],
                "top_venues": "; ".join(f"{v['venue']}:{v['count']}" for v in row["top_venues"][:8]),
                "post2023_top_venues": "; ".join(f"{v['venue']}:{v['count']}" for v in row["post2023_top_venues"][:8]),
                "baseline_title_terms": "; ".join(f"{t['term']}:{t['count']}" for t in row["baseline_title_terms"][:8]),
                "post2023_title_terms": "; ".join(f"{t['term']}:{t['count']}" for t in row["post2023_title_terms"][:8]),
                "region": ident.get("region", "Unknown"),
                "sector": ident.get("sector", "Unknown"),
            })


def format_terms(terms: list[dict[str, Any]], n: int = 8) -> str:
    if not terms:
        return "none"
    return ", ".join(f"{t['term']} ({t['count']})" for t in terms[:n])


def format_venues(venues: list[dict[str, Any]], n: int = 8) -> str:
    if not venues:
        return "none"
    return ", ".join(f"{v['venue']} ({v['count']})" for v in venues[:n])


def write_markdown(packet: dict[str, Any]) -> None:
    rows = packet["researchers"]
    lines = [
        "# Selected Sample: Baseline Top-Networking Count > 6",
        "",
        "This is a derived review packet for the provisional selected sample. It does not filter or rewrite the raw cohort, publication history, or itinerary artifacts.",
        "",
        "The summaries below are title-based because abstract coverage is not yet reliable enough to use silently.",
        "",
        "## Sample Summary",
        "",
        f"- Researchers: {packet['metadata']['researcher_count']}",
        f"- Selection rule: {packet['metadata']['selection_rule']}",
        f"- Baseline: {packet['metadata']['baseline']}",
        f"- Observation window: {packet['metadata']['observation_window']}",
        f"- Median total clean publications: {packet['metadata']['median_clean_publication_count']}",
        f"- Median baseline top-networking papers: {packet['metadata']['median_baseline_top_networking_count']}",
        f"- High-total researchers with total clean publications >100: {packet['metadata']['high_total_gt_100_count']}",
        "",
        "## Aggregate Title Vocabulary",
        "",
        f"- Baseline terms: {format_terms(packet['aggregate']['baseline_title_terms'], 20)}",
        f"- Post-2023 terms: {format_terms(packet['aggregate']['post2023_title_terms'], 20)}",
        "",
        "## Researcher Table",
        "",
        "| Researcher | Baseline net | Total clean | Post-2023 | Top venues | Baseline title terms | Post-2023 title terms |",
        "|---|---:|---:|---:|---|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['name']} | {row['baseline_top_networking_count']} | "
            f"{row['clean_publication_count']} | {row['post2023_clean_publication_count']} | "
            f"{format_venues(row['top_venues'], 5)} | "
            f"{format_terms(row['baseline_title_terms'], 5)} | "
            f"{format_terms(row['post2023_title_terms'], 5)} |"
        )

    lines.extend([
        "",
        "## Per-Researcher Evidence",
        "",
        "Each section lists compact yearly title evidence. Years with many publications are truncated in this markdown view; the full packet is in `data/selected_sample_network_gt6_packet.json`.",
    ])

    for row in rows:
        lines.extend([
            "",
            f"### {row['name']}",
            "",
            f"- DBLP pid: `{row['dblp_pid']}`",
            f"- Counts: baseline networking `{row['baseline_top_networking_count']}`, total clean `{row['clean_publication_count']}`, post-2023 clean `{row['post2023_clean_publication_count']}`",
            f"- Top venues: {format_venues(row['top_venues'])}",
            f"- Baseline title terms: {format_terms(row['baseline_title_terms'])}",
            f"- Post-2023 title terms: {format_terms(row['post2023_title_terms'])}",
            "",
        ])
        for year, papers in row["papers_by_year"].items():
            shown = papers[:MAX_TITLES_PER_YEAR]
            lines.append(f"- {year}:")
            for paper in shown:
                marker = " [qualifying]" if paper.get("is_qualifying_top_networking") else ""
                lines.append(f"  - {paper.get('venue', '')}: {paper.get('title', '')}{marker}")
            if len(papers) > MAX_TITLES_PER_YEAR:
                lines.append(f"  - ... {len(papers) - MAX_TITLES_PER_YEAR} more in JSON packet")

    lines.append("")
    OUTPUT_MD.write_text("\n".join(lines))


def run() -> dict[str, Any]:
    with open(INPUT_FILE) as f:
        data = json.load(f)

    selected = [
        r for r in data["researchers"]
        if int(r.get("baseline_top_networking_count", 0)) > NETWORK_THRESHOLD
    ]
    selected.sort(
        key=lambda r: (
            int(r.get("baseline_top_networking_count", 0)),
            int(r.get("clean_publication_count", 0)),
            r.get("name", ""),
        ),
        reverse=True,
    )
    rows = [summarize_researcher(r) for r in selected]

    baseline_papers = []
    post_papers = []
    all_papers = []
    for row in rows:
        for year, papers in row["papers_by_year"].items():
            all_papers.extend(papers)
            if int(year) in BASELINE_YEARS:
                baseline_papers.extend(papers)
            if int(year) in POST_YEARS:
                post_papers.extend(papers)

    packet = {
        "metadata": {
            "phase": "build_selected_sample_packet",
            "input_file": str(INPUT_FILE.relative_to(PROJECT_DIR)),
            "selection_rule": f"baseline_top_networking_count > {NETWORK_THRESHOLD}",
            "raw_data_policy": "Derived packet only; raw cohort, publication history, and researcher itinerary files are not modified.",
            "baseline": "2018-2022",
            "observation_window": "2018-2026",
            "researcher_count": len(rows),
            "median_clean_publication_count": median([r["clean_publication_count"] for r in rows]) if rows else 0,
            "median_baseline_top_networking_count": median([r["baseline_top_networking_count"] for r in rows]) if rows else 0,
            "high_total_gt_100_count": sum(1 for r in rows if r["clean_publication_count"] > 100),
            "title_summary_caveat": "Title-vocabulary summaries are descriptive review aids, not topic labels.",
        },
        "aggregate": {
            "baseline_title_terms": top_terms(baseline_papers, 40),
            "post2023_title_terms": top_terms(post_papers, 40),
            "all_title_terms": top_terms(all_papers, 40),
        },
        "researchers": rows,
    }

    with open(OUTPUT_JSON, "w") as f:
        json.dump(packet, f, indent=2, ensure_ascii=False)
    write_csv(rows)
    write_markdown(packet)

    print(f"Selected researchers: {len(rows)}")
    print(f"Wrote {OUTPUT_JSON}")
    print(f"Wrote {OUTPUT_CSV}")
    print(f"Wrote {OUTPUT_MD}")
    return packet


if __name__ == "__main__":
    run()
