#!/usr/bin/env python3
"""Audit missing/unmatched author-position data for the core-99 sample."""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path
from typing import Any

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
INPUT_FILE = DATA_DIR / "researcher_itineraries.json"
OUTPUT_CSV = DATA_DIR / "core99_author_position_issues.csv"
OUTPUT_JSON = DATA_DIR / "core99_author_position_issues.json"
OUTPUT_MD = PROJECT_DIR / "CORE99_AUTHOR_POSITION_ISSUES.md"

NETWORK_THRESHOLD = 6


def issue_rows(researcher: dict[str, Any]) -> list[dict[str, Any]]:
    rows = []
    for year, papers in researcher.get("itinerary", {}).items():
        for paper in papers:
            confidence = paper.get("author_match_confidence")
            if confidence not in {"unmatched", "missing_authors"}:
                continue
            rows.append({
                "name": researcher.get("name", ""),
                "dblp_pid": researcher.get("dblp_pid", ""),
                "year": paper.get("year") or year,
                "venue": paper.get("venue", ""),
                "title": paper.get("title", ""),
                "dblp_url": paper.get("dblp_url", ""),
                "issue": confidence,
                "author_count": paper.get("author_count", 0),
                "authors": "; ".join(paper.get("authors") or []),
            })
    return rows


def write_csv(rows: list[dict[str, Any]]) -> None:
    fields = [
        "name", "dblp_pid", "year", "venue", "title", "dblp_url",
        "issue", "author_count", "authors",
    ]
    with open(OUTPUT_CSV, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(packet: dict[str, Any]) -> None:
    lines = [
        "# Core-99 Author-Position Issues",
        "",
        "This is a derived audit table for papers where the scoped core-99 researcher could not be confidently positioned in the stored DBLP author list.",
        "",
        "## Summary",
        "",
        f"- Core-99 researchers: {packet['metadata']['core99_researchers']}",
        f"- Core-99 clean papers checked: {packet['metadata']['core99_clean_papers_checked']}",
        f"- Issue rows: {packet['metadata']['issue_rows']}",
        "",
        "| Issue | Papers |",
        "|---|---:|",
    ]
    for issue, count in packet["issue_distribution"].items():
        lines.append(f"| {issue} | {count} |")

    lines.extend([
        "",
        "## Researchers With Most Issues",
        "",
        "| Researcher | Issues |",
        "|---|---:|",
    ])
    for item in packet["top_researchers_by_issue_count"]:
        lines.append(f"| {item['name']} | {item['issues']} |")

    lines.extend([
        "",
        "## Issue Rows",
        "",
        "The full table is in `data/core99_author_position_issues.csv`. The preview below shows the first 100 rows.",
        "",
        "| Researcher | Year | Venue | Issue | Title |",
        "|---|---:|---|---|---|",
    ])
    for row in packet["issues"][:100]:
        title = row["title"].replace("|", "\\|")
        lines.append(f"| {row['name']} | {row['year']} | {row['venue']} | {row['issue']} | {title} |")
    lines.append("")
    OUTPUT_MD.write_text("\n".join(lines))


def run() -> dict[str, Any]:
    with open(INPUT_FILE) as f:
        data = json.load(f)

    selected = [
        r for r in data["researchers"]
        if int(r.get("baseline_top_networking_count", 0)) > NETWORK_THRESHOLD
    ]

    rows = []
    clean_papers_checked = 0
    for researcher in selected:
        for papers in researcher.get("itinerary", {}).values():
            clean_papers_checked += len(papers)
        rows.extend(issue_rows(researcher))

    rows.sort(key=lambda r: (r["name"], int(r["year"] or 0), r["venue"], r["title"]))
    issue_counts = Counter(row["issue"] for row in rows)
    researcher_counts = Counter(row["name"] for row in rows)

    packet = {
        "metadata": {
            "phase": "audit_core99_author_positions",
            "input_file": str(INPUT_FILE.relative_to(PROJECT_DIR)),
            "selection_rule": f"baseline_top_networking_count > {NETWORK_THRESHOLD}",
            "raw_data_policy": "Derived audit only; no source records are modified.",
            "core99_researchers": len(selected),
            "core99_clean_papers_checked": clean_papers_checked,
            "issue_rows": len(rows),
        },
        "issue_distribution": dict(issue_counts.most_common()),
        "top_researchers_by_issue_count": [
            {"name": name, "issues": count}
            for name, count in researcher_counts.most_common(25)
        ],
        "issues": rows,
    }

    with open(OUTPUT_JSON, "w") as f:
        json.dump(packet, f, indent=2, ensure_ascii=False)
    write_csv(rows)
    write_markdown(packet)

    print(f"Core-99 researchers: {len(selected)}")
    print(f"Clean papers checked: {clean_papers_checked}")
    print(f"Issue rows: {len(rows)}")
    print(f"Wrote {OUTPUT_CSV}")
    print(f"Wrote {OUTPUT_JSON}")
    print(f"Wrote {OUTPUT_MD}")
    return packet


if __name__ == "__main__":
    run()
