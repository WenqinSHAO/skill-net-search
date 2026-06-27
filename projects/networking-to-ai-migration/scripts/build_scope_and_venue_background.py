#!/usr/bin/env python3
"""Build Part I.1/I.2 scope and venue-year background artifacts.

This script materializes the first gate in ANALYSIS_PLAN.md:

I.1 Paper scope
  - data/analysis_scope_manifest.json
  - data/analysis_scope_audit.csv
  - data/analysis_scope_audit.json

I.2 Venue-year background, cohort-neutral
  - data/venue_year_background.json
  - data/venue_year_background.csv
  - data/venue_year_topic_vectors_stage1.json
  - data/venue_year_author_concentration.csv
  - VENUE_YEAR_BACKGROUND.md

Inputs:
  - data/new_core_clean_papers.json
  - data/venue_accepted_totals.json, when available
  - scripts/classify_paper_topics.py taxonomy and keyword rules
"""

from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from classify_paper_topics import TOPICS, classify_title, matched_keywords

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

INPUT_CLEAN_PAPERS = DATA_DIR / "new_core_clean_papers.json"
INPUT_VENUE_TOTALS = DATA_DIR / "venue_accepted_totals.json"

OUT_SCOPE_MANIFEST = DATA_DIR / "analysis_scope_manifest.json"
OUT_SCOPE_AUDIT_CSV = DATA_DIR / "analysis_scope_audit.csv"
OUT_SCOPE_AUDIT_JSON = DATA_DIR / "analysis_scope_audit.json"
OUT_BACKGROUND_JSON = DATA_DIR / "venue_year_background.json"
OUT_BACKGROUND_CSV = DATA_DIR / "venue_year_background.csv"
OUT_TOPIC_VECTORS = DATA_DIR / "venue_year_topic_vectors_stage1.json"
OUT_CONCENTRATION_CSV = DATA_DIR / "venue_year_author_concentration.csv"
OUT_REPORT = PROJECT_DIR / "VENUE_YEAR_BACKGROUND.md"

YEARS = list(range(2018, 2027))
TOP_NET_VENUES = ["SIGCOMM", "NSDI", "CoNEXT", "HotNets", "IMC"]
TOPIC_KEYS = list(TOPICS.keys())

SPACE_RE = re.compile(r"\s+")
PUNCT_RE = re.compile(r"[^\w\s]", re.UNICODE)


def load_json(path: Path) -> Any:
    with open(path) as f:
        return json.load(f)


def norm_author(author: dict[str, Any]) -> str:
    pid = (author.get("pid") or "").strip()
    if pid:
        return f"pid:{pid}"
    name = (author.get("name") or "").casefold().strip()
    name = PUNCT_RE.sub(" ", name)
    name = SPACE_RE.sub(" ", name)
    return f"name:{name}" if name else "unknown"


def gini(values: list[int]) -> float:
    vals = sorted(v for v in values if v >= 0)
    n = len(vals)
    if n == 0:
        return 0.0
    total = sum(vals)
    if total == 0:
        return 0.0
    weighted_sum = sum((i + 1) * v for i, v in enumerate(vals))
    return round((2 * weighted_sum) / (n * total) - (n + 1) / n, 4)


def hhi(values: list[int]) -> float:
    total = sum(values)
    if total == 0:
        return 0.0
    return round(sum((v / total) ** 2 for v in values), 4)


def classify_stage1(paper: dict[str, Any]) -> dict[str, Any]:
    title = paper.get("title", "")
    label = classify_title(title)
    hits = matched_keywords(title)
    return {
        **label,
        "matched_keywords": hits,
        "evidence_mode": "title_only",
        "classification_stage": "stage1_keyword_rules",
    }


def concentration_for_papers(papers: list[dict[str, Any]]) -> dict[str, Any]:
    author_counts: Counter[str] = Counter()
    paper_authors: list[set[str]] = []
    unresolved_papers = 0

    for paper in papers:
        authors = [norm_author(a) for a in paper.get("authors", [])]
        authors = [a for a in authors if a != "unknown"]
        if paper.get("partial_author_pids") or paper.get("author_pid_unresolved_count", 0):
            unresolved_papers += 1
        unique = set(authors)
        paper_authors.append(unique)
        author_counts.update(unique)

    counts = list(author_counts.values())
    total_incidences = sum(counts)
    repeat_authors = {a for a, c in author_counts.items() if c > 1}
    papers_with_repeat_author = sum(1 for authors in paper_authors if authors & repeat_authors)
    top_counts = sorted(counts, reverse=True)

    def top_share(k: int) -> float:
        if total_incidences == 0:
            return 0.0
        return round(sum(top_counts[:k]) / total_incidences * 100, 2)

    return {
        "unique_authors": len(author_counts),
        "author_paper_incidences": total_incidences,
        "papers_with_repeat_author": papers_with_repeat_author,
        "repeat_author_share_pct": round(papers_with_repeat_author / len(papers) * 100, 2) if papers else 0.0,
        "top5_author_incidence_share_pct": top_share(5),
        "top10_author_incidence_share_pct": top_share(10),
        "gini_author_paper_counts": gini(counts),
        "hhi_author_paper_counts": hhi(counts),
        "max_author_paper_count": max(counts) if counts else 0,
        "papers_with_partial_author_pids": unresolved_papers,
    }


def topic_vector_for_papers(papers: list[dict[str, Any]]) -> tuple[dict[str, float], Counter[str], list[dict[str, Any]]]:
    topic_weights = defaultdict(float)
    primary_counts: Counter[str] = Counter()
    labeled = []
    for paper in papers:
        classification = classify_stage1(paper)
        primary_counts[classification["primary_topic"]] += 1
        for topic, weight in classification["all_topics"].items():
            topic_weights[topic] += weight
        labeled.append({
            "paper_id": paper.get("paper_id"),
            "title": paper.get("title"),
            "venue": paper.get("venue_group", paper.get("venue")),
            "year": paper.get("year"),
            "primary_topic": classification["primary_topic"],
            "primary_label": classification["primary_label"],
            "all_topics": classification["all_topics"],
            "multi_topic": classification["multi_topic"],
            "matched_keywords": classification["matched_keywords"],
            "evidence_mode": classification["evidence_mode"],
        })
    total = sum(topic_weights.values())
    vector = {topic: round(topic_weights.get(topic, 0.0) / total * 100, 2) if total else 0.0 for topic in TOPIC_KEYS}
    return vector, primary_counts, labeled


def scope_manifest(clean_meta: dict[str, Any]) -> dict[str, Any]:
    return {
        "metadata": {
            "phase": "analysis_scope_manifest",
            "description": "Canonical scope terminology for the reorganized networking-to-ai migration analysis.",
            "input_source": "data/new_core_clean_papers.json",
            "input_clean_paper_metadata": clean_meta,
        },
        "paper_scopes": {
            "total_papers": {
                "definition": "All in-scope conference papers attached to a researcher after deduplication and record cleaning; broad activity universe for volume and venue-family analysis.",
                "current_materialization_note": "Full researcher-level total papers live in researcher_itineraries. This I.1/I.2 materialization audits the top-net repaired clean-paper table first.",
            },
            "net_papers": {
                "definition": "Subset of total papers that are networking-related, either by venue or by topic evidence in title/abstract.",
                "current_materialization_note": "All top_net_papers are net_papers by definition; broader net_paper extraction from adjacent venues is deferred until the fine networking-topic classifier is reviewed.",
            },
            "top_net_papers": {
                "definition": "Subset of net papers in SIGCOMM, NSDI, CoNEXT, HotNets, and IMC. CoNEXT 2023+ includes PACMNET long-paper evidence where appropriate.",
                "venues": TOP_NET_VENUES,
            },
        },
        "aggregation_modes": {
            "unique_paper_count": "Union of papers; coauthored papers by multiple scoped researchers count once.",
            "author_summed_count": "Sum of researcher-paper incidences; coauthored papers by multiple scoped researchers count once per scoped researcher.",
        },
        "excluded_record_classes": [
            "poster", "demo", "proceedings_volume", "workshop", "editorial", "keynote", "journal_article", "record_type:*", "missing_venue", "venue:CoRR", "other_non_main_paper"
        ],
        "naming_policy": {
            "avoid_scope_name": "clean_papers",
            "reason": "Cleaning is a processing step, not a substantive paper universe. Prefer total/net/top-net paper terminology.",
        },
    }


def build_scope_audit(all_records: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    grouped: dict[tuple[str, str, int, bool, str], dict[str, Any]] = {}
    for paper in all_records:
        venue = paper.get("venue_group") or paper.get("venue") or "Unknown"
        year = int(paper.get("year") or 0)
        included = bool(paper.get("included_in_new_core_scope"))
        reason = paper.get("exclusion_reason") or "included"
        sources = paper.get("sources") or ["unknown"]
        for source in sources:
            key = (source, venue, year, included, reason)
            if key not in grouped:
                grouped[key] = {
                    "source": source,
                    "venue": venue,
                    "year": year,
                    "included_in_top_net_scope": included,
                    "exclusion_reason": reason,
                    "record_count": 0,
                    "partial_author_pid_records": 0,
                }
            grouped[key]["record_count"] += 1
            if paper.get("partial_author_pids") or paper.get("author_pid_unresolved_count", 0):
                grouped[key]["partial_author_pid_records"] += 1

    rows = sorted(grouped.values(), key=lambda r: (r["year"], r["venue"], r["source"], str(r["included_in_top_net_scope"]), r["exclusion_reason"]))
    summary = {
        "total_records": len(all_records),
        "included_records": sum(1 for p in all_records if p.get("included_in_new_core_scope")),
        "excluded_records": sum(1 for p in all_records if not p.get("included_in_new_core_scope")),
        "by_exclusion_reason": dict(Counter(p.get("exclusion_reason") or "included" for p in all_records)),
        "by_source": dict(Counter(source for p in all_records for source in (p.get("sources") or ["unknown"]))),
    }
    return rows, summary


def coverage_status(expected_total: Any, observed: int) -> str:
    if expected_total is None:
        return "unavailable_or_not_indexed"
    if observed == expected_total:
        return "matches_expected_total"
    if observed < expected_total:
        return "below_expected_total"
    return "above_expected_total"


def build_background(included: list[dict[str, Any]], all_records: list[dict[str, Any]], venue_totals: dict[str, Any]) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    expected = venue_totals.get("totals", {}) if venue_totals else {}
    all_records_by_vy = defaultdict(list)
    included_by_vy = defaultdict(list)
    included_by_year = defaultdict(list)
    for paper in all_records:
        all_records_by_vy[(paper.get("venue_group") or paper.get("venue"), int(paper.get("year") or 0))].append(paper)
    for paper in included:
        venue = paper.get("venue_group") or paper.get("venue")
        year = int(paper.get("year") or 0)
        included_by_vy[(venue, year)].append(paper)
        included_by_year[year].append(paper)

    rows: list[dict[str, Any]] = []
    topic_rows: list[dict[str, Any]] = []
    labeled_papers: list[dict[str, Any]] = []

    def add_row(scope: str, venue: str, year: int, papers: list[dict[str, Any]], all_for_vy: list[dict[str, Any]], expected_total: Any = None) -> None:
        vector, primary_counts, labels = topic_vector_for_papers(papers)
        conc = concentration_for_papers(papers)
        excluded_count = len([p for p in all_for_vy if not p.get("included_in_new_core_scope")]) if scope == "venue_year" else 0
        row = {
            "scope": scope,
            "venue": venue,
            "year": year,
            "unique_paper_count": len(papers),
            "expected_total_from_venue_totals": expected_total,
            "coverage_status": coverage_status(expected_total, len(papers)) if scope == "venue_year" else "combined_scope_not_applicable",
            "excluded_record_count": excluded_count,
            "other_or_uncertain_primary_count": primary_counts.get("other", 0),
            "other_or_uncertain_primary_share_pct": round(primary_counts.get("other", 0) / len(papers) * 100, 2) if papers else 0.0,
            **conc,
        }
        for topic in TOPIC_KEYS:
            row[f"topic_share_{topic}"] = vector.get(topic, 0.0)
        rows.append(row)
        topic_rows.append({
            "scope": scope,
            "venue": venue,
            "year": year,
            "unique_paper_count": len(papers),
            "topic_shares": vector,
            "primary_topic_counts": dict(primary_counts),
            "other_or_uncertain_primary_share_pct": row["other_or_uncertain_primary_share_pct"],
        })
        labeled_papers.extend(labels)

    for year in YEARS:
        add_row("all_top_net_year", "ALL_TOP_NET", year, included_by_year.get(year, []), [])

    for venue in TOP_NET_VENUES:
        for year in YEARS:
            papers = included_by_vy.get((venue, year), [])
            expected_total = expected.get(str(year), {}).get(venue)
            add_row("venue_year", venue, year, papers, all_records_by_vy.get((venue, year), []), expected_total)

    return rows, topic_rows, labeled_papers


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str] | None = None) -> None:
    if not rows:
        return
    if fieldnames is None:
        fieldnames = list(rows[0].keys())
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def top_topic_summary(row: dict[str, Any], n: int = 4) -> str:
    shares = []
    for topic in TOPIC_KEYS:
        shares.append((topic, row.get(f"topic_share_{topic}", 0.0)))
    parts = []
    for topic, share in sorted(shares, key=lambda x: -x[1])[:n]:
        parts.append(f"{TOPICS[topic]['label']} {share:.1f}%")
    return "; ".join(parts)


def write_report(background_rows: list[dict[str, Any]], scope_summary: dict[str, Any]) -> None:
    all_rows = [r for r in background_rows if r["scope"] == "all_top_net_year"]
    venue_rows = [r for r in background_rows if r["scope"] == "venue_year"]
    years = [r for r in all_rows if r["unique_paper_count"] > 0]
    ai_by_year = [(r["year"], r["topic_share_ai_infrastructure"], r["unique_paper_count"], r["other_or_uncertain_primary_share_pct"]) for r in years]
    concentration_rank = sorted(
        [r for r in venue_rows if r["unique_paper_count"] > 0],
        key=lambda r: r["gini_author_paper_counts"],
        reverse=True,
    )[:10]
    ai_rank = sorted(
        [r for r in venue_rows if r["unique_paper_count"] > 0],
        key=lambda r: r["topic_share_ai_infrastructure"],
        reverse=True,
    )[:10]
    coverage_issues = [r for r in venue_rows if r["coverage_status"] not in {"matches_expected_total", "combined_scope_not_applicable"}]

    lines = []
    lines.append("# Venue-Year Background: I.1/I.2 First Pass")
    lines.append("")
    lines.append("This report materializes the first gate in `ANALYSIS_PLAN.md`: paper-scope definitions and cohort-neutral venue-year background. It uses the repaired top-net paper table and does not yet overlay core-99/new-core cohort labels.")
    lines.append("")
    lines.append("## 1. Scope Audit")
    lines.append("")
    lines.append("| Metric | Count |")
    lines.append("|---|---:|")
    lines.append(f"| Total top-net table records | {scope_summary['total_records']} |")
    lines.append(f"| Included top-net main-paper records | {scope_summary['included_records']} |")
    lines.append(f"| Excluded records | {scope_summary['excluded_records']} |")
    lines.append("")
    lines.append("Excluded-record reasons:")
    lines.append("")
    lines.append("| Reason | Count |")
    lines.append("|---|---:|")
    for reason, count in sorted(scope_summary["by_exclusion_reason"].items(), key=lambda x: (-x[1], x[0])):
        if reason == "included":
            continue
        lines.append(f"| `{reason}` | {count} |")
    lines.append("")
    lines.append("## 2. All Top-Net Venues Combined By Year")
    lines.append("")
    lines.append("| Year | Papers | AI infra % | Classical networking % | Measurement % | Wireless/mobile % | Other/uncertain primary % | Gini | Repeat-author paper share % |")
    lines.append("|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
    for r in all_rows:
        lines.append(
            f"| {r['year']} | {r['unique_paper_count']} | {r['topic_share_ai_infrastructure']:.1f} | "
            f"{r['topic_share_classical_networking']:.1f} | {r['topic_share_network_measurement']:.1f} | "
            f"{r['topic_share_wireless_mobile']:.1f} | {r['other_or_uncertain_primary_share_pct']:.1f} | "
            f"{r['gini_author_paper_counts']:.3f} | {r['repeat_author_share_pct']:.1f} |"
        )
    lines.append("")
    lines.append("Description: the combined top-net table provides the field-level yearly baseline. AI infrastructure is low before 2023 and becomes visibly larger after 2023, while the `Other/uncertain` share remains high enough that topic claims should stay provisional.")
    lines.append("")
    lines.append("## 3. Highest AI-Infrastructure Venue-Years")
    lines.append("")
    lines.append("| Rank | Venue | Year | Papers | AI infra % | Other/uncertain primary % | Top topics |")
    lines.append("|---:|---|---:|---:|---:|---:|---|")
    for i, r in enumerate(ai_rank, 1):
        lines.append(f"| {i} | {r['venue']} | {r['year']} | {r['unique_paper_count']} | {r['topic_share_ai_infrastructure']:.1f} | {r['other_or_uncertain_primary_share_pct']:.1f} | {top_topic_summary(r, 3)} |")
    lines.append("")
    lines.append("Interpretation: AI-infrastructure signal is not venue-uniform. It is most visible in recent NSDI/SIGCOMM years and some smaller HotNets/CoNEXT years, so researcher-level AI-infra claims should be compared against each author's venue background.")
    lines.append("")
    lines.append("## 4. Most Concentrated Venue-Years By Gini")
    lines.append("")
    lines.append("| Rank | Venue | Year | Papers | Unique authors | Gini | HHI | Top-5 incidence share % | Repeat-author paper share % |")
    lines.append("|---:|---|---:|---:|---:|---:|---:|---:|---:|")
    for i, r in enumerate(concentration_rank, 1):
        lines.append(f"| {i} | {r['venue']} | {r['year']} | {r['unique_paper_count']} | {r['unique_authors']} | {r['gini_author_paper_counts']:.3f} | {r['hhi_author_paper_counts']:.3f} | {r['top5_author_incidence_share_pct']:.1f} | {r['repeat_author_share_pct']:.1f} |")
    lines.append("")
    lines.append("Interpretation: concentration should be read with paper count. Smaller venues can show high concentration because a few repeated authors cover a larger share of papers. Gini, HHI, top-k share, and repeat-author share should be read together rather than as one decisive metric.")
    lines.append("")
    lines.append("## 5. Coverage And Count Mismatches")
    lines.append("")
    lines.append("The `expected_total_from_venue_totals` column comes from the existing venue totals artifact. Mismatches in this section compare clean included main papers with raw TOC-like totals, so they are diagnostics, not automatic errors. A separate `TOPNET_VENUE_COMPLETENESS.md` audit checks raw fetched coverage before cleaning.")
    lines.append("")
    lines.append("| Venue | Year | Observed included papers | Expected total | Status | Excluded records in repaired table |")
    lines.append("|---|---:|---:|---:|---|---:|")
    for r in coverage_issues:
        expected = "" if r["expected_total_from_venue_totals"] is None else r["expected_total_from_venue_totals"]
        lines.append(f"| {r['venue']} | {r['year']} | {r['unique_paper_count']} | {expected} | `{r['coverage_status']}` | {r['excluded_record_count']} |")
    lines.append("")
    lines.append("## 6. What Can Be Said Now")
    lines.append("")
    lines.append("Data-supported observations:")
    lines.append("")
    lines.append("1. The repaired top-net table contains {} included main-paper records and {} excluded non-main records.".format(scope_summary["included_records"], scope_summary["excluded_records"]))
    lines.append("2. Raw DBLP TOC coverage and clean main-paper scope are distinct: one audits data fetch completeness; the other defines the analyzable paper universe.")
    lines.append("3. Venue-year background can now be described without researcher cohort labels, but topic shares remain Stage-1 diagnostics.")
    lines.append("4. Author concentration varies by venue-year and needs multiple metrics; no single concentration number should drive interpretation.")
    lines.append("")
    lines.append("Interpretive cautions:")
    lines.append("")
    lines.append("- This is a Stage-1 topic view based on title keyword rules. It is appropriate for scoping and anomaly detection, not final semantic claims.")
    lines.append("- Cohort overlays such as core-99/new-core/stayer/newcomer/dropout are intentionally deferred until this venue baseline is reviewed.")
    lines.append("- 2026 remains incomplete; missing venue-years should not be interpreted as topical absence.")
    OUT_REPORT.write_text("\n".join(lines) + "\n")


def main() -> None:
    clean = load_json(INPUT_CLEAN_PAPERS)
    all_records = clean.get("papers", [])
    included = [p for p in all_records if p.get("included_in_new_core_scope")]
    venue_totals = load_json(INPUT_VENUE_TOTALS) if INPUT_VENUE_TOTALS.exists() else {}

    OUT_SCOPE_MANIFEST.write_text(json.dumps(scope_manifest(clean.get("metadata", {})), indent=2, ensure_ascii=False) + "\n")

    scope_rows, scope_summary = build_scope_audit(all_records)
    write_csv(OUT_SCOPE_AUDIT_CSV, scope_rows)
    OUT_SCOPE_AUDIT_JSON.write_text(json.dumps({"summary": scope_summary, "rows": scope_rows}, indent=2, ensure_ascii=False) + "\n")

    background_rows, topic_rows, labeled_papers = build_background(included, all_records, venue_totals)
    bg_meta = {
        "phase": "venue_year_background_stage1",
        "description": "Cohort-neutral venue-year background for top-net venues.",
        "input_source": "data/new_core_clean_papers.json",
        "topic_method": "stage1_keyword_rules_from_classify_paper_topics.py",
        "topic_caveat": "High other/uncertain share; use for first-pass background only.",
        "cohort_overlay_included": False,
        "aggregation_modes": ["all_top_net_year", "venue_year"],
    }
    OUT_BACKGROUND_JSON.write_text(json.dumps({"metadata": bg_meta, "rows": background_rows}, indent=2, ensure_ascii=False) + "\n")

    bg_fields = list(background_rows[0].keys())
    write_csv(OUT_BACKGROUND_CSV, background_rows, bg_fields)

    concentration_fields = [
        "scope", "venue", "year", "unique_paper_count", "unique_authors", "author_paper_incidences",
        "papers_with_repeat_author", "repeat_author_share_pct", "top5_author_incidence_share_pct",
        "top10_author_incidence_share_pct", "gini_author_paper_counts", "hhi_author_paper_counts",
        "max_author_paper_count", "papers_with_partial_author_pids",
    ]
    write_csv(OUT_CONCENTRATION_CSV, [{k: r[k] for k in concentration_fields} for r in background_rows], concentration_fields)

    OUT_TOPIC_VECTORS.write_text(json.dumps({
        "metadata": {
            **bg_meta,
            "topics": {k: v["label"] for k, v in TOPICS.items()},
            "labeled_paper_count": len(labeled_papers),
        },
        "vectors": topic_rows,
        "paper_labels": labeled_papers,
    }, indent=2, ensure_ascii=False) + "\n")

    write_report(background_rows, scope_summary)

    print("Wrote:")
    for path in [
        OUT_SCOPE_MANIFEST,
        OUT_SCOPE_AUDIT_CSV,
        OUT_SCOPE_AUDIT_JSON,
        OUT_BACKGROUND_JSON,
        OUT_BACKGROUND_CSV,
        OUT_TOPIC_VECTORS,
        OUT_CONCENTRATION_CSV,
        OUT_REPORT,
    ]:
        print(f"  {path.relative_to(PROJECT_DIR)}")


if __name__ == "__main__":
    main()
