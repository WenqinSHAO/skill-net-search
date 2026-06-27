#!/usr/bin/env python3
"""Validate v3 classification output.

Checks:
  - All paper_ids from input are present in output
  - All assigned labels exist in the taxonomy
  - evidence_mode is set for every paper
  - confidence per axis is valid (high/medium/low)
  - No papers with zero labels on required axes (scenario, mechanism)
  - Distribution sanity vs expected baselines

Output: prints validation report to stdout.
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

INPUT_PAPERS = DATA_DIR / "new_core_clean_papers.json"
INPUT_LABELS = DATA_DIR / "paper_topic_labels_v3.json"
TAXONOMY_PATH = DATA_DIR / "taxonomy_v3.json"


def load_json(path: Path) -> Any:
    with open(path) as f:
        return json.load(f)


def main() -> None:
    errors = []
    warnings = []

    # Load inputs
    if not INPUT_LABELS.exists():
        print(f"ERROR: {INPUT_LABELS} not found. Run classify_paper_topics_v3.py first.")
        sys.exit(1)

    taxonomy = load_json(TAXONOMY_PATH)
    labels_data = load_json(INPUT_LABELS)
    clean_data = load_json(INPUT_PAPERS)

    papers = labels_data.get("papers", [])
    metadata = labels_data.get("metadata", {})
    taxonomy_labels = labels_data.get("taxonomy", taxonomy)
    axes = taxonomy_labels.get("axes", {})

    print("=" * 60)
    print("Classification Validation Report")
    print("=" * 60)
    print(f"Model: {metadata.get('model', 'unknown')}")
    print(f"Taxonomy version: {metadata.get('taxonomy_version', 'unknown')}")
    print(f"Papers classified: {len(papers)}")

    # Expected paper count
    all_papers = clean_data.get("papers", [])
    expected_papers = [p for p in all_papers if p.get("included_in_new_core_scope")]
    expected_ids = {p["paper_id"] for p in expected_papers}

    # Check 1: All expected papers present
    actual_ids = {p.get("paper_id") for p in papers}
    missing = expected_ids - actual_ids
    extra = actual_ids - expected_ids
    if missing:
        errors.append(f"{len(missing)} expected papers missing from output")
    if extra:
        warnings.append(f"{len(extra)} papers in output not in input (redundant)")

    # Check 2: Label validity
    valid_labels = {}
    for axis_key in ["scenario", "mechanism", "method"]:
        valid_labels[axis_key] = set(axes.get(axis_key, {}).get("values", {}).keys())
        valid_labels[axis_key].add("other")  # Allow "other" as fallback

    invalid_labels = Counter()
    zero_scenario = 0
    zero_mechanism = 0
    zero_method = 0
    missing_evidence_mode = 0
    invalid_confidence = 0
    uncertain_count = 0
    classification_error_count = 0
    title_only_not_uncertain = 0
    unknown_label_count = Counter()

    for p in papers:
        # Check labels
        for s in p.get("scenario", []):
            if s not in valid_labels["scenario"]:
                invalid_labels[f"scenario:{s}"] += 1

        for m in p.get("mechanism", []):
            if m not in valid_labels["mechanism"]:
                invalid_labels[f"mechanism:{m}"] += 1

        for m in p.get("method", []):
            if m not in valid_labels["method"]:
                invalid_labels[f"method:{m}"] += 1

        # Check zero labels on required axes
        if not p.get("scenario"):
            zero_scenario += 1
        if not p.get("mechanism"):
            zero_mechanism += 1
        if not p.get("method"):
            zero_method += 1  # method is optional, just count

        # Check evidence_mode
        if not p.get("evidence_mode"):
            missing_evidence_mode += 1

        # Check confidence validity
        for axis in ["scenario", "mechanism", "method"]:
            conf = p.get("confidence", {}).get(axis)
            if conf not in ("high", "medium", "low"):
                invalid_confidence += 1

        # Count uncertain and quality gates
        if p.get("uncertain"):
            uncertain_count += 1
        if p.get("classification_error"):
            classification_error_count += 1
        if p.get("evidence_mode") == "title_only" and not p.get("uncertain"):
            title_only_not_uncertain += 1
        for axis in ["scenario", "mechanism", "method"]:
            for label in p.get(axis, []):
                if str(label).startswith("unknown_"):
                    unknown_label_count[f"{axis}:{label}"] += 1

    if invalid_labels:
        errors.append(f"{len(invalid_labels)} invalid labels assigned: {dict(invalid_labels.most_common(10))}")
    if zero_scenario > 0:
        errors.append(f"{zero_scenario} papers with zero scenario labels (required)")
    if zero_mechanism > 0:
        errors.append(f"{zero_mechanism} papers with zero mechanism labels (required)")
    if missing_evidence_mode > 0:
        errors.append(f"{missing_evidence_mode} papers missing evidence_mode")
    if invalid_confidence > 0:
        errors.append(f"{invalid_confidence} invalid confidence values")
    if classification_error_count > 0:
        errors.append(f"{classification_error_count} papers have classification_error fallback rows")
    if title_only_not_uncertain > 0:
        warnings.append(f"{title_only_not_uncertain} title-only papers are marked not uncertain; verify explicit title evidence")

    # Check 3: Distributions
    print(f"\n--- Distribution Summary ---")
    total = len(papers)

    for axis_key, axis_label in [("scenario", "Scenario"), ("mechanism", "Mechanism"), ("method", "Method")]:
        counts: Counter[str] = Counter()
        for p in papers:
            for label in p.get(axis_key, []):
                counts[label] += 1
        unique = len(counts)
        top_label, top_count = counts.most_common(1)[0] if counts else ("none", 0)
        human = axes.get(axis_key, {}).get("values", {}).get(top_label, {}).get("label", top_label)
        no_label = sum(1 for p in papers if not p.get(axis_key))
        print(f"  {axis_label}: {unique} unique labels used, "
              f"top={top_label}({human}): {top_count} ({top_count/total*100:.1f}%), "
              f"no_label={no_label}")

    print(f"\n--- Quality Metrics ---")
    abstract_count = sum(1 for p in papers if p.get("evidence_mode") == "title_and_abstract")
    errors_list = [p for p in papers if p.get("classification_error")]
    print(f"  Evidence mode title+abstract: {abstract_count} ({abstract_count/total*100:.1f}%)")
    print(f"  Evidence mode title_only: {total - abstract_count} ({(total-abstract_count)/total*100:.1f}%)")
    print(f"  Uncertain: {uncertain_count} ({uncertain_count/total*100:.1f}%)")
    print(f"  Method axis empty: {zero_method} ({zero_method/total*100:.1f}%)")
    print(f"  Classification errors: {len(errors_list)}")
    print(f"  Title-only not uncertain: {title_only_not_uncertain}")
    if unknown_label_count:
        print("  Unknown label distribution:")
        for key, count in sorted(unknown_label_count.items()):
            print(f"    {key}: {count}")

    confidence_dist: Counter[str] = Counter()
    for p in papers:
        for axis in ["scenario", "mechanism", "method"]:
            conf = p.get("confidence", {}).get(axis, "low")
            confidence_dist[f"{axis}:{conf}"] += 1
    print(f"\n  Confidence distribution:")
    for key, count in sorted(confidence_dist.items()):
        print(f"    {key}: {count}")

    # Check 4: Venue coverage
    venue_counts: Counter[str] = Counter()
    for p in papers:
        venue = p.get("venue", "?")
        venue_counts[venue] += 1
    print(f"\n  Top venues by paper count:")
    for venue, count in venue_counts.most_common(10):
        print(f"    {venue}: {count}")

    # Final judgment
    print(f"\n{'='*60}")
    if errors:
        print(f"FAILED: {len(errors)} errors found")
        for e in errors:
            print(f"  ERROR: {e}")
    else:
        print("PASSED: No validation errors.")
    if warnings:
        for w in warnings:
            print(f"  WARNING: {w}")

    print(f"\nSummary: {len(papers)} papers, {len(errors)} errors, {len(warnings)} warnings")
    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
