#!/usr/bin/env python3
"""Generate cohort-shape summaries and visualizations.

This script implements TODO 1 from ANALYSIS_PLAN.md. It is intentionally
non-interpretive: it summarizes the broad cohort shape without assigning
trajectory or migration labels.
"""

from __future__ import annotations

import csv
import json
import math
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean, median
from typing import Iterable

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
FIG_DIR = PROJECT_DIR / "figures" / "cohort_shape"
INPUT_FILE = DATA_DIR / "researcher_itineraries.json"
SUMMARY_JSON = DATA_DIR / "cohort_shape_summary.json"
RESEARCHER_CSV = DATA_DIR / "cohort_shape_researchers.csv"
SUMMARY_MD = PROJECT_DIR / "COHORT_SHAPE.md"
HIGH_TOTAL_OUTLIERS_CSV = DATA_DIR / "cohort_shape_high_total_outliers.csv"
TOTAL_ONE_CSV = DATA_DIR / "cohort_shape_total_one_researchers.csv"
CORE_SLICE_CSV = DATA_DIR / "cohort_shape_candidate_core_network_gt6.csv"

BASELINE_YEARS = {"2018", "2019", "2020", "2021", "2022"}
POST_YEARS = {"2023", "2024", "2025", "2026"}
QUALIFYING_VENUES = ["SIGCOMM", "NSDI", "CoNEXT", "HotNets", "IMC"]


def bucket_count(value: int) -> str:
    if value <= 10:
        return str(value)
    if value <= 20:
        return "11-20"
    if value <= 50:
        return "21-50"
    if value <= 100:
        return "51-100"
    if value <= 200:
        return "101-200"
    if value <= 500:
        return "201-500"
    return "501+"


def summarize_values(values: list[int]) -> dict:
    values_sorted = sorted(values)
    n = len(values_sorted)
    if n == 0:
        return {"count": 0}

    def pct(p: float) -> int:
        idx = min(n - 1, max(0, math.ceil(p * n) - 1))
        return values_sorted[idx]

    return {
        "count": n,
        "min": values_sorted[0],
        "p25": pct(0.25),
        "median": median(values_sorted),
        "mean": round(mean(values_sorted), 2),
        "p75": pct(0.75),
        "p90": pct(0.90),
        "p95": pct(0.95),
        "p99": pct(0.99),
        "max": values_sorted[-1],
    }


def venue_combo(papers: list[dict]) -> str:
    venues = sorted({p.get("venue", "") for p in papers if p.get("venue")})
    return "+".join(venues) if venues else "Unknown"


def year_sum(counts: dict[str, int], years: set[str]) -> int:
    return sum(int(counts.get(y, 0)) for y in years)


def top_rows(rows: list[dict], key: str, n: int = 25) -> list[dict]:
    return sorted(rows, key=lambda r: (r[key], r["name"]), reverse=True)[:n]


def write_rows_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in fields})


def write_csv(rows: list[dict]) -> None:
    fields = [
        "name", "dblp_pid", "baseline_top_networking_count",
        "baseline_clean_publication_count", "post2023_clean_publication_count",
        "clean_publication_count", "baseline_networking_share",
        "baseline_active_year_count", "qualifying_venue_combo",
        "proposed_exclude_total_one", "region", "sector",
    ]
    write_rows_csv(RESEARCHER_CSV, rows, fields)


def bar_plot(counter: Counter, title: str, xlabel: str, ylabel: str, path: Path,
             sort_numeric: bool = True, max_labels: int | None = None) -> None:
    items = list(counter.items())
    if sort_numeric:
        def sort_key(item):
            label = item[0]
            try:
                return int(label)
            except ValueError:
                return label
        items.sort(key=sort_key)
    else:
        items.sort(key=lambda x: x[1], reverse=True)
    if max_labels is not None:
        items = items[:max_labels]
    labels = [str(k) for k, _ in items]
    values = [v for _, v in items]

    fig, ax = plt.subplots(figsize=(max(8, len(labels) * 0.45), 5.5))
    ax.bar(labels, values, color="#4C78A8")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(axis="y", alpha=0.25)
    fig.tight_layout()
    fig.savefig(path, dpi=160)
    plt.close(fig)


def hist_plot(values: list[int], title: str, xlabel: str, path: Path,
              bins: Iterable[int] | int = 40, log_y: bool = False) -> None:
    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.hist(values, bins=bins, color="#59A14F", edgecolor="white")
    if log_y:
        ax.set_yscale("log")
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Researchers")
    ax.grid(axis="y", alpha=0.25)
    fig.tight_layout()
    fig.savefig(path, dpi=160)
    plt.close(fig)


def scatter_plot(rows: list[dict], path: Path) -> None:
    x = [r["baseline_top_networking_count"] for r in rows]
    y = [r["clean_publication_count"] for r in rows]
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.scatter(x, y, s=16, alpha=0.35, color="#E15759")
    ax.set_yscale("symlog", linthresh=20)
    ax.set_title("Baseline Top-Networking Count vs Total Clean Publications")
    ax.set_xlabel("Baseline top-networking papers, 2018-2022")
    ax.set_ylabel("Total clean conference papers, 2018-2026 (symlog)")
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(path, dpi=160)
    plt.close(fig)


def heatmap(crosstab: dict[str, dict[str, int]], path: Path) -> None:
    row_labels = sorted(crosstab.keys(), key=lambda x: int(x) if x.isdigit() else 999)
    col_order = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11-20", "21-50", "51-100", "101-200", "201-500", "501+"]
    col_labels = [c for c in col_order if any(crosstab[r].get(c, 0) for r in row_labels)]
    matrix = [[crosstab[r].get(c, 0) for c in col_labels] for r in row_labels]

    fig, ax = plt.subplots(figsize=(max(9, len(col_labels) * 0.7), max(5, len(row_labels) * 0.35)))
    im = ax.imshow(matrix, cmap="Blues", aspect="auto")
    ax.set_xticks(range(len(col_labels)), col_labels, rotation=45, ha="right")
    ax.set_yticks(range(len(row_labels)), row_labels)
    ax.set_xlabel("Total clean publication count bucket")
    ax.set_ylabel("Baseline top-networking paper count")
    ax.set_title("Cohort Cross-Tab: Networking Anchor vs Total Publication Volume")
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val:
                ax.text(j, i, str(val), ha="center", va="center", fontsize=8,
                        color="white" if val > max(max(r) for r in matrix) * 0.45 else "black")
    fig.colorbar(im, ax=ax, label="Researchers")
    fig.tight_layout()
    fig.savefig(path, dpi=160)
    plt.close(fig)


def write_markdown(summary: dict) -> None:
    lines = []
    lines.append("# Cohort Shape Summary")
    lines.append("")
    lines.append("This is a descriptive data-foundation summary, not an interpretation of migration or trajectory.")
    lines.append("")
    lines.append("## Cohort")
    lines.append("")
    lines.append(f"- Researchers: {summary['metadata']['researcher_count']}")
    lines.append(f"- Cohort rule: {summary['metadata']['cohort_rule']}")
    lines.append("- Baseline means 2018-2022.")
    lines.append("- Post-2023 means 2023-2026.")
    lines.append("- Total means 2018-2026.")
    lines.append("- Clean publications are in-scope conference/workshop records after excluding journals, CoRR/arXiv, proceedings volumes, and other out-of-scope DBLP record types.")
    lines.append("")
    lines.append("## Baseline Top-Networking Count Distribution")
    lines.append("")
    lines.append("| Count | Researchers |")
    lines.append("|---:|---:|")
    for k, v in summary["baseline_top_networking_count_distribution"].items():
        lines.append(f"| {k} | {v} |")
    lines.append("")
    lines.append("## Summary Statistics")
    lines.append("")
    lines.append("| Metric | Min | P25 | Median | Mean | P75 | P90 | P95 | P99 | Max |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
    for metric, stats in summary["summary_stats"].items():
        lines.append(
            f"| {metric} | {stats.get('min')} | {stats.get('p25')} | {stats.get('median')} | "
            f"{stats.get('mean')} | {stats.get('p75')} | {stats.get('p90')} | "
            f"{stats.get('p95')} | {stats.get('p99')} | {stats.get('max')} |"
        )
    lines.append("")
    lines.append("## Proposed Scope Flags")
    lines.append("")
    lines.append(f"- Researchers with total clean publications equal to 1: {summary['proposed_scope_flags']['total_clean_publication_count_eq_1']}")
    lines.append("- These are flagged as likely too sparse for trajectory analysis, though retained in raw cohort artifacts.")
    lines.append("")
    lines.append("## Candidate Core Slice Summaries")
    lines.append("")
    lines.append("| Slice | Researchers | High-total >100 | High-total share | Median total clean pubs |")
    lines.append("|---|---:|---:|---:|---:|")
    for item in summary["candidate_core_slices"]:
        lines.append(f"| {item['slice']} | {item['researchers']} | {item['high_total_gt_100']} | {item['high_total_gt_100_share']} | {item['median_clean_publication_count']} |")
    lines.append("")
    lines.append("## High-Total Publication Outliers")
    lines.append("")
    lines.append("Researchers with total clean publications > 100 are listed in `data/cohort_shape_high_total_outliers.csv`.")
    lines.append("These are important to review because common-name profiles, broad cross-domain researchers, or one-off collaborators can bias aggregate analysis.")
    lines.append("")
    lines.append("## Top Qualifying Venue Combinations")
    lines.append("")
    lines.append("| Venue combination | Researchers |")
    lines.append("|---|---:|")
    for item in summary["top_qualifying_venue_combinations"][:25]:
        lines.append(f"| {item['venue_combo']} | {item['researchers']} |")
    lines.append("")
    lines.append("## Generated Figures")
    lines.append("")
    for fig in summary["figures"]:
        lines.append(f"- `{fig}`")
    lines.append("")
    SUMMARY_MD.write_text("\n".join(lines))


def run() -> dict:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    with open(INPUT_FILE) as f:
        data = json.load(f)
    researchers = data["researchers"]

    rows = []
    baseline_dist = Counter()
    total_bucket_dist = Counter()
    baseline_clean_bucket_dist = Counter()
    post_bucket_dist = Counter()
    venue_combo_counts = Counter()
    crosstab = defaultdict(Counter)

    for r in researchers:
        by_year = {str(k): int(v) for k, v in r.get("clean_publication_count_by_year", {}).items()}
        baseline_clean = year_sum(by_year, BASELINE_YEARS)
        post_clean = year_sum(by_year, POST_YEARS)
        total_clean = int(r.get("clean_publication_count", 0))
        baseline_top = int(r.get("baseline_top_networking_count", 0))
        active_baseline_years = sum(1 for y in BASELINE_YEARS if by_year.get(y, 0) > 0)
        combo = venue_combo(r.get("baseline_top_networking_papers", []))
        share = round(baseline_top / baseline_clean, 4) if baseline_clean else None
        ident = r.get("identity", {})

        row = {
            "name": r.get("name", ""),
            "dblp_pid": r.get("dblp_pid", ""),
            "baseline_top_networking_count": baseline_top,
            "baseline_clean_publication_count": baseline_clean,
            "post2023_clean_publication_count": post_clean,
            "clean_publication_count": total_clean,
            "baseline_networking_share": share,
            "baseline_active_year_count": active_baseline_years,
            "qualifying_venue_combo": combo,
            "proposed_exclude_total_one": total_clean == 1,
            "region": ident.get("region", "Unknown"),
            "sector": ident.get("sector", "Unknown"),
        }
        rows.append(row)

        baseline_dist[str(baseline_top)] += 1
        total_bucket_dist[bucket_count(total_clean)] += 1
        baseline_clean_bucket_dist[bucket_count(baseline_clean)] += 1
        post_bucket_dist[bucket_count(post_clean)] += 1
        venue_combo_counts[combo] += 1
        crosstab[str(baseline_top)][bucket_count(total_clean)] += 1

    high_total_rows = sorted([r for r in rows if r["clean_publication_count"] > 100], key=lambda r: (r["baseline_top_networking_count"], r["clean_publication_count"], r["name"]), reverse=True)
    total_one_rows = sorted([r for r in rows if r["clean_publication_count"] == 1], key=lambda r: (r["baseline_top_networking_count"], r["name"]), reverse=True)
    core_gt6_rows = sorted([r for r in rows if r["baseline_top_networking_count"] > 6], key=lambda r: (r["baseline_top_networking_count"], r["clean_publication_count"], r["name"]), reverse=True)

    candidate_slices = []
    for threshold in [1, 2, 3, 4, 5, 6, 7, 10]:
        slice_rows = [r for r in rows if r["baseline_top_networking_count"] >= threshold]
        if not slice_rows:
            continue
        high = [r for r in slice_rows if r["clean_publication_count"] > 100]
        candidate_slices.append({
            "slice": f"baseline_top_networking_count >= {threshold}",
            "researchers": len(slice_rows),
            "high_total_gt_100": len(high),
            "high_total_gt_100_share": round(len(high) / len(slice_rows), 4),
            "median_clean_publication_count": median([r["clean_publication_count"] for r in slice_rows]),
        })
    slice_rows = [r for r in rows if r["baseline_top_networking_count"] > 6]
    high = [r for r in slice_rows if r["clean_publication_count"] > 100]
    candidate_slices.append({
        "slice": "baseline_top_networking_count > 6",
        "researchers": len(slice_rows),
        "high_total_gt_100": len(high),
        "high_total_gt_100_share": round(len(high) / len(slice_rows), 4) if slice_rows else 0,
        "median_clean_publication_count": median([r["clean_publication_count"] for r in slice_rows]) if slice_rows else 0,
    })

    summary = {
        "metadata": {
            "phase": "analyze_cohort_shape",
            "input_file": str(INPUT_FILE.relative_to(PROJECT_DIR)),
            "researcher_count": len(rows),
            "cohort_rule": data.get("metadata", {}).get("cohort_rule"),
            "definitions": {
                "baseline": "2018-2022",
                "post_2023": "2023-2026",
                "total": "2018-2026",
                "clean_publications": "In-scope conference/workshop records after excluding journals, CoRR/arXiv, proceedings volumes, and other out-of-scope DBLP record types.",
            },
            "raw_data_policy": "No raw cohort, publication history, or itinerary records are filtered or rewritten by this script; proposed exclusions and core definitions are derived flags/slices only.",
        },
        "summary_stats": {
            "baseline_top_networking_count": summarize_values([r["baseline_top_networking_count"] for r in rows]),
            "baseline_clean_publication_count": summarize_values([r["baseline_clean_publication_count"] for r in rows]),
            "post2023_clean_publication_count": summarize_values([r["post2023_clean_publication_count"] for r in rows]),
            "clean_publication_count": summarize_values([r["clean_publication_count"] for r in rows]),
            "baseline_active_year_count": summarize_values([r["baseline_active_year_count"] for r in rows]),
        },
        "baseline_top_networking_count_distribution": dict(sorted(baseline_dist.items(), key=lambda x: int(x[0]))),
        "proposed_scope_flags": {
            "total_clean_publication_count_eq_1": len(total_one_rows),
        },
        "candidate_core_slices": candidate_slices,
        "high_total_gt_100_count": len(high_total_rows),
        "high_total_gt_100_by_baseline_top_networking_count": dict(sorted(Counter(str(r["baseline_top_networking_count"]) for r in high_total_rows).items(), key=lambda x: int(x[0]))),
        "total_clean_publication_bucket_distribution": dict(total_bucket_dist),
        "baseline_clean_publication_bucket_distribution": dict(baseline_clean_bucket_dist),
        "post2023_clean_publication_bucket_distribution": dict(post_bucket_dist),
        "baseline_top_networking_by_total_clean_bucket": {k: dict(v) for k, v in sorted(crosstab.items(), key=lambda x: int(x[0]))},
        "top_qualifying_venue_combinations": [
            {"venue_combo": combo, "researchers": count}
            for combo, count in venue_combo_counts.most_common(50)
        ],
        "top_by_baseline_top_networking_count": top_rows(rows, "baseline_top_networking_count", 25),
        "top_by_clean_publication_count": top_rows(rows, "clean_publication_count", 25),
        "top_by_post2023_clean_publication_count": top_rows(rows, "post2023_clean_publication_count", 25),
        "figures": [],
    }

    write_csv(rows)
    csv_fields = [
        "name", "dblp_pid", "baseline_top_networking_count",
        "baseline_clean_publication_count", "post2023_clean_publication_count",
        "clean_publication_count", "baseline_networking_share",
        "baseline_active_year_count", "qualifying_venue_combo",
        "proposed_exclude_total_one", "region", "sector",
    ]
    write_rows_csv(HIGH_TOTAL_OUTLIERS_CSV, high_total_rows, csv_fields)
    write_rows_csv(TOTAL_ONE_CSV, total_one_rows, csv_fields)
    write_rows_csv(CORE_SLICE_CSV, core_gt6_rows, csv_fields)

    fig1 = FIG_DIR / "baseline_top_networking_count_distribution.png"
    bar_plot(baseline_dist, "Baseline Top-Networking Paper Count Distribution", "Baseline top-networking papers", "Researchers", fig1)

    fig2 = FIG_DIR / "total_clean_publication_histogram.png"
    hist_plot([r["clean_publication_count"] for r in rows], "Total Clean Conference Publications, 2018-2026", "Clean conference papers", fig2, bins=60, log_y=True)

    fig3 = FIG_DIR / "baseline_clean_publication_histogram.png"
    hist_plot([r["baseline_clean_publication_count"] for r in rows], "Clean Baseline Publications, 2018-2022", "Clean conference papers", fig3, bins=40, log_y=True)

    fig4 = FIG_DIR / "post2023_clean_publication_histogram.png"
    hist_plot([r["post2023_clean_publication_count"] for r in rows], "Clean Post-2023 Publications, 2023-2026", "Clean conference papers", fig4, bins=40, log_y=True)

    fig5 = FIG_DIR / "baseline_networking_vs_total_clean_scatter.png"
    scatter_plot(rows, fig5)

    fig6 = FIG_DIR / "baseline_networking_by_total_clean_heatmap.png"
    heatmap(summary["baseline_top_networking_by_total_clean_bucket"], fig6)

    fig7 = FIG_DIR / "qualifying_venue_combo_top20.png"
    bar_plot(Counter(dict(venue_combo_counts.most_common(20))), "Top Qualifying Venue Combinations", "Venue combination", "Researchers", fig7, sort_numeric=False)
    plt.close("all")

    summary["figures"] = [str(p.relative_to(PROJECT_DIR)) for p in [fig1, fig2, fig3, fig4, fig5, fig6, fig7]]

    with open(SUMMARY_JSON, "w") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    write_markdown(summary)

    print(f"Researchers: {len(rows)}")
    print(f"Wrote {SUMMARY_JSON}")
    print(f"Wrote {RESEARCHER_CSV}")
    print(f"Wrote {HIGH_TOTAL_OUTLIERS_CSV}")
    print(f"Wrote {TOTAL_ONE_CSV}")
    print(f"Wrote {CORE_SLICE_CSV}")
    print(f"Wrote {SUMMARY_MD}")
    for fig in summary["figures"]:
        print(f"Figure: {fig}")
    return summary


if __name__ == "__main__":
    run()
