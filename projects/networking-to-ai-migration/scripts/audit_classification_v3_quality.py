#!/usr/bin/env python3
"""Audit v3 networking-topic classification quality.

This is a review/audit script, not a classifier. It checks abstract coverage,
title-match risks, validation failures, and label-quality indicators for the
three-axis v3 classifier.

Outputs:
  - data/classification_v3_quality_audit.json
  - data/classification_v3_quality_audit.csv
  - I5_CLASSIFICATION_REVIEW.md
"""

from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

CLEAN_PAPERS = DATA_DIR / "new_core_clean_papers.json"
ABSTRACTS = DATA_DIR / "paper_abstracts.json"
LABELS = DATA_DIR / "paper_topic_labels_v3.json"

OUT_JSON = DATA_DIR / "classification_v3_quality_audit.json"
OUT_CSV = DATA_DIR / "classification_v3_quality_audit.csv"
OUT_REPORT = PROJECT_DIR / "I5_CLASSIFICATION_REVIEW.md"


def load_json(path: Path, default: Any = None) -> Any:
    if not path.exists():
        return default
    with open(path) as f:
        return json.load(f)


def words(text: str) -> set[str]:
    return set(re.sub(r"[^\w\s]", " ", (text or "").lower()).split())


def title_match_scores(title: str, source_title: str) -> tuple[float, float, float, int]:
    title_words = words(title)
    source_words = words(source_title)
    if not title_words or not source_words:
        return 0.0, 0.0, 0.0, len(source_words)
    overlap = len(title_words & source_words)
    forward = overlap / len(title_words)
    backward = overlap / len(source_words)
    return max(forward, backward), forward, backward, len(source_words)


def pct(num: int, den: int) -> float:
    return round(num / den * 100, 1) if den else 0.0


def build_audit() -> dict[str, Any]:
    clean = load_json(CLEAN_PAPERS, {"papers": []})
    abs_data = load_json(ABSTRACTS, {"abstracts": {}, "metadata": {}})
    labels_data = load_json(LABELS, {"papers": [], "metadata": {}})

    papers = [p for p in clean.get("papers", []) if p.get("included_in_new_core_scope")]
    by_id = {p["paper_id"]: p for p in papers}
    abstracts = abs_data.get("abstracts", {})
    labels = labels_data.get("papers", [])

    abstract_rows = []
    for paper in papers:
        pid = paper["paper_id"]
        abs_info = abstracts.get(pid, {})
        has_abstract = bool(abs_info.get("abstract"))
        abstract_rows.append({
            "paper_id": pid,
            "title": paper.get("title", ""),
            "venue": paper.get("venue_group") or paper.get("venue", ""),
            "year": int(paper.get("year") or 0),
            "has_doi": bool(paper.get("doi")),
            "has_abstract": has_abstract,
            "abstract_source": abs_info.get("source", "missing"),
            "source_title": abs_info.get("source_title", ""),
        })

    missing = [r for r in abstract_rows if not r["has_abstract"]]
    source_counts = Counter(r["abstract_source"] for r in abstract_rows)

    title_match_rows = []
    for row in abstract_rows:
        if row["abstract_source"] not in {"openalex_title", "semantic_scholar_title"}:
            continue
        score, forward, backward, source_word_count = title_match_scores(row["title"], row["source_title"])
        suspect = forward < 0.75 or source_word_count < 4
        item = {
            **row,
            "title_match_score": round(score, 3),
            "title_forward_overlap": round(forward, 3),
            "title_backward_overlap": round(backward, 3),
            "source_word_count": source_word_count,
            "suspect_title_match": suspect,
        }
        title_match_rows.append(item)

    label_rows = []
    for label in labels:
        paper = by_id.get(label.get("paper_id", ""), {})
        label_rows.append({
            "paper_id": label.get("paper_id", ""),
            "title": label.get("title", ""),
            "venue": label.get("venue", ""),
            "year": int(label.get("year") or 0),
            "evidence_mode": label.get("evidence_mode", ""),
            "uncertain": bool(label.get("uncertain")),
            "scenario_count": len(label.get("scenario", [])),
            "mechanism_count": len(label.get("mechanism", [])),
            "method_count": len(label.get("method", [])),
            "scenario_confidence": label.get("confidence", {}).get("scenario", ""),
            "mechanism_confidence": label.get("confidence", {}).get("mechanism", ""),
            "method_confidence": label.get("confidence", {}).get("method", ""),
            "classification_error": label.get("classification_error", ""),
            "has_abstract": bool(abstracts.get(label.get("paper_id", ""), {}).get("abstract")),
            "has_doi": bool(paper.get("doi")),
        })

    total = len(label_rows)
    zero_scenario = [r for r in label_rows if r["scenario_count"] == 0]
    zero_mechanism = [r for r in label_rows if r["mechanism_count"] == 0]
    errors = [r for r in label_rows if r["classification_error"]]
    title_only = [r for r in label_rows if r["evidence_mode"] == "title_only"]
    title_only_not_uncertain = [r for r in title_only if not r["uncertain"]]

    summary = {
        "paper_count": len(papers),
        "classified_count": len(label_rows),
        "abstracts_found": sum(1 for r in abstract_rows if r["has_abstract"]),
        "abstracts_missing": len(missing),
        "abstract_coverage_pct": pct(sum(1 for r in abstract_rows if r["has_abstract"]), len(abstract_rows)),
        "missing_abstracts_with_doi": sum(1 for r in missing if r["has_doi"]),
        "missing_abstracts_without_doi": sum(1 for r in missing if not r["has_doi"]),
        "missing_abstracts_by_venue": dict(Counter(r["venue"] for r in missing).most_common()),
        "missing_abstracts_by_year": dict(sorted(Counter(r["year"] for r in missing).items())),
        "abstract_source_counts": dict(source_counts.most_common()),
        "title_source_abstract_count": len(title_match_rows),
        "suspect_title_source_matches": sum(1 for r in title_match_rows if r["suspect_title_match"]),
        "classification_errors": len(errors),
        "zero_scenario_count": len(zero_scenario),
        "zero_mechanism_count": len(zero_mechanism),
        "zero_method_count": sum(1 for r in label_rows if r["method_count"] == 0),
        "uncertain_count": sum(1 for r in label_rows if r["uncertain"]),
        "uncertain_pct": pct(sum(1 for r in label_rows if r["uncertain"]), total),
        "title_only_count": len(title_only),
        "title_only_pct": pct(len(title_only), total),
        "title_only_not_uncertain_count": len(title_only_not_uncertain),
        "title_only_not_uncertain_pct_of_title_only": pct(len(title_only_not_uncertain), len(title_only)),
        "confidence_counts": dict(Counter(
            f"{axis}:{row[f'{axis}_confidence']}"
            for row in label_rows
            for axis in ["scenario", "mechanism", "method"]
        ).most_common()),
    }

    return {
        "summary": summary,
        "abstract_rows": abstract_rows,
        "title_match_rows": title_match_rows,
        "label_rows": label_rows,
        "examples": {
            "suspect_title_matches": sorted(
                [r for r in title_match_rows if r["suspect_title_match"]],
                key=lambda r: (r["title_forward_overlap"], r["source_word_count"]),
            )[:20],
            "zero_scenario": zero_scenario[:20],
            "zero_mechanism": zero_mechanism[:20],
            "classification_errors": errors[:20],
            "title_only_not_uncertain": title_only_not_uncertain[:20],
        },
    }


def write_csv(path: Path, audit: dict[str, Any]) -> None:
    rows = audit["label_rows"]
    if not rows:
        return
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_report(audit: dict[str, Any]) -> None:
    s = audit["summary"]
    lines = []
    lines.append("# I.5 Classification Review")
    lines.append("")
    lines.append("Status: the v3 three-axis classifier is a promising draft, but it is not analysis-ready.")
    lines.append("")
    lines.append("## Executive Findings")
    lines.append("")
    lines.append(f"- Classified papers: {s['classified_count']} / {s['paper_count']}.")
    lines.append(f"- Abstract coverage: {s['abstracts_found']} papers ({s['abstract_coverage_pct']}%); {s['abstracts_missing']} missing.")
    lines.append(f"- Missing abstracts are overwhelmingly NSDI: {s['missing_abstracts_by_venue']}.")
    lines.append(f"- Missing abstracts without DOI: {s['missing_abstracts_without_doi']}; with DOI: {s['missing_abstracts_with_doi']}.")
    lines.append(f"- Validation blockers: {s['zero_scenario_count']} zero-scenario papers, {s['zero_mechanism_count']} zero-mechanism papers, {s['classification_errors']} classification errors.")
    lines.append(f"- Uncertain labels: {s['uncertain_count']} papers ({s['uncertain_pct']}%).")
    lines.append(f"- Title-only labels: {s['title_only_count']} papers ({s['title_only_pct']}%); {s['title_only_not_uncertain_count']} of those are marked not uncertain.")
    lines.append(f"- Suspect title-source abstract matches: {s['suspect_title_source_matches']} / {s['title_source_abstract_count']}.")
    lines.append("")
    lines.append("## Method Review")
    lines.append("")
    lines.append("The three-axis design is directionally better than the prior flat keyword taxonomy because it separates deployment context, networking mechanism, and method. However, the current axes are not yet clean enough for a networking-audience analysis.")
    lines.append("")
    lines.append("Main concerns:")
    lines.append("")
    lines.append("1. Scenario mixes deployment domain and workload. For example, `dcn_ai_training`, `dcn_cloud`, `interconnect`, `cdn`, and `internet_core` are not mutually comparable dimensions.")
    lines.append("2. Mechanism is missing common networking categories that appear in top venues, such as packet processing/programming, naming/DNS, content/video/QoE, sensing/localization, network economics/policy/censorship, reliability/resilience, and experimentation/testbed/tooling.")
    lines.append("3. Method labels mix technique with artifact maturity. `systems_building` becomes a broad default and is assigned to nearly half the papers, which limits interpretability.")
    lines.append("4. The prompt instruction `when uncertain, choose the more specific label` conflicts with the project principle of not forcing labels. It likely contributes to over-specific low-confidence labels.")
    lines.append("5. Downstream vectors normalize by assigned labels per axis, not by paper denominator plus no-label/uncertain shares. That hides missing-label and uncertainty mass.")
    lines.append("")
    lines.append("## Abstract Coverage Diagnosis")
    lines.append("")
    lines.append("The missing-abstract problem is mostly not random:")
    lines.append("")
    for venue, count in s["missing_abstracts_by_venue"].items():
        lines.append(f"- {venue}: {count}")
    lines.append("")
    lines.append("Root cause: DBLP-derived NSDI records have no DOI in `new_core_clean_papers.json`, so OpenAlex DOI lookup cannot work. The fallback title search recovers only a small number of NSDI abstracts. USENIX technical-session pages provide abstracts, but the current fetcher does not scrape USENIX.")
    lines.append("")
    lines.append("Secondary issue: title-based matching is too lenient. A few OpenAlex title matches use short source titles or low forward overlap, which can attach the wrong abstract.")
    lines.append("")
    lines.append("## Label Quality Risks")
    lines.append("")
    lines.append("- `validate_classification_v3.py` fails, so the v3 output should not be described as passed or completed.")
    lines.append("- 37 papers are fallback `all_retries_failed` rows and should be re-run before aggregation.")
    lines.append("- 84 title-only papers are marked not uncertain. This is too optimistic unless the title explicitly contains all assigned evidence.")
    lines.append("- The mechanism distribution is dominated by `measurement_telemetry`; this may be plausible for IMC-heavy slices but should be checked with venue-year examples.")
    lines.append("- `systems_building` appears too broad and should either be narrowed or treated as an evidence-quality/artifact flag rather than a method topic.")
    lines.append("")
    lines.append("## Recommended Fix Order")
    lines.append("")
    lines.append("1. Do not use v3 topic profiles or venue vectors for interpretation yet.")
    lines.append("2. Add a USENIX NSDI abstract fetch path keyed by NSDI year/title.")
    lines.append("3. Tighten title-match validation: require high forward overlap or exact normalized title match; quarantine short-title subset matches.")
    lines.append("4. Re-run the 37 failed classifications and all papers affected by suspect abstracts.")
    lines.append("5. Revise taxonomy before full reclassification: add missing mechanism categories; split method from artifact/evidence flags; add explicit `unknown/insufficient_evidence` handling.")
    lines.append("6. Regenerate venue and researcher vectors with quality denominators: title-only share, no-label share, low-confidence share, and uncertainty share.")
    lines.append("")
    lines.append("## Example Suspect Abstract Matches")
    lines.append("")
    lines.append("| Year | Venue | Paper title | Source title | Forward overlap |")
    lines.append("|---:|---|---|---|---:|")
    for row in audit["examples"]["suspect_title_matches"][:10]:
        lines.append(
            f"| {row['year']} | {row['venue']} | {row['title']} | {row['source_title']} | {row['title_forward_overlap']} |"
        )
    lines.append("")
    lines.append("## Example Zero-Mechanism Papers")
    lines.append("")
    lines.append("| Year | Venue | Title | Evidence mode | Error |")
    lines.append("|---:|---|---|---|---|")
    for row in audit["examples"]["zero_mechanism"][:10]:
        lines.append(
            f"| {row['year']} | {row['venue']} | {row['title']} | {row['evidence_mode']} | {row['classification_error']} |"
        )
    OUT_REPORT.write_text("\n".join(lines) + "\n")


def main() -> None:
    audit = build_audit()
    OUT_JSON.write_text(json.dumps(audit, indent=2, ensure_ascii=False) + "\n")
    write_csv(OUT_CSV, audit)
    write_report(audit)
    print(f"Wrote {OUT_JSON}")
    print(f"Wrote {OUT_CSV}")
    print(f"Wrote {OUT_REPORT}")


if __name__ == "__main__":
    main()
