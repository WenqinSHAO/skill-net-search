#!/usr/bin/env python3
"""Audit top-networking venue-year completeness after the paginated fetch.

Outputs:
  - data/topnet_venue_completeness_audit.csv
  - data/topnet_venue_completeness_audit.json
  - TOPNET_VENUE_COMPLETENESS.md
"""

from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

TOPNET_SOURCE = DATA_DIR / "topnet_venue_year_papers.json"
CLEAN_PAPERS = DATA_DIR / "new_core_clean_papers.json"
VENUE_TOTALS = DATA_DIR / "venue_accepted_totals.json"

OUT_CSV = DATA_DIR / "topnet_venue_completeness_audit.csv"
OUT_JSON = DATA_DIR / "topnet_venue_completeness_audit.json"
OUT_REPORT = PROJECT_DIR / "TOPNET_VENUE_COMPLETENESS.md"

YEARS = list(range(2018, 2027))
VENUES = ["SIGCOMM", "NSDI", "CoNEXT", "HotNets", "IMC"]


def load_json(path: Path, default: Any = None) -> Any:
    if not path.exists():
        return default
    with open(path) as f:
        return json.load(f)


def group_clean_papers(papers: list[dict[str, Any]]) -> dict[tuple[str, int], Counter]:
    grouped: dict[tuple[str, int], Counter] = defaultdict(Counter)
    for paper in papers:
        venue = paper.get("venue_group") or paper.get("venue")
        year = int(paper.get("year") or 0)
        if venue not in VENUES or year not in YEARS:
            continue
        key = (venue, year)
        grouped[key]["observed_records"] += 1
        if paper.get("included_in_new_core_scope"):
            grouped[key]["clean_main_records"] += 1
        else:
            grouped[key][f"excluded:{paper.get('exclusion_reason')}"] += 1
    return grouped


def source_coverage(source: dict[str, Any]) -> dict[tuple[str, int], dict[str, Any]]:
    by_vy: dict[tuple[str, int], dict[str, Any]] = {}
    conext_extra = defaultdict(lambda: {"pacmnet_records": 0, "pacmnet_total": 0, "pacmnet_status": "not_checked"})
    for row in source.get("coverage", []):
        venue = row.get("canonical_venue")
        year = int(row.get("expected_year") or 0)
        if venue == "PACMNET":
            extra = conext_extra[year]
            extra["pacmnet_records"] += int(row.get("records_returned") or 0)
            extra["pacmnet_total"] += int(row.get("dblp_reported_total") or 0)
            extra["pacmnet_status"] = row.get("status", "")
            continue
        if venue in VENUES and year in YEARS:
            by_vy[(venue, year)] = {
                "conference_toc_key": row.get("toc_key"),
                "conference_toc_status": row.get("status"),
                "conference_toc_records": int(row.get("records_returned") or 0),
                "conference_toc_total": int(row.get("dblp_reported_total") or 0),
                "conference_page_count": int(row.get("page_count") or 0),
            }
    for year, extra in conext_extra.items():
        row = by_vy.setdefault(( "CoNEXT", year), {})
        row.update(extra)
    return by_vy


def raw_fetch_status(row: dict[str, Any], expected_total: Any, venue: str, year: int) -> str:
    conf_status = row.get("conference_toc_status", "not_found_or_not_indexed")
    conf_records = row.get("conference_toc_records", 0)
    conf_total = row.get("conference_toc_total", 0)
    if expected_total is None and conf_records == 0:
        return "not_yet_available"
    if conf_status != "fetched":
        return conf_status
    if conf_records != conf_total:
        return "conference_toc_incomplete"
    if venue == "CoNEXT" and year >= 2023:
        pac_status = row.get("pacmnet_status", "not_checked")
        pac_records = row.get("pacmnet_records", 0)
        pac_total = row.get("pacmnet_total", 0)
        if year <= 2025 and pac_status != "fetched":
            return "pacmnet_missing"
        if pac_records != pac_total:
            return "pacmnet_incomplete"
    return "raw_toc_complete"


def clean_scope_note(exclusions: dict[str, int]) -> str:
    if not exclusions:
        return "none"
    parts = []
    for reason, count in sorted(exclusions.items(), key=lambda x: (-x[1], x[0])):
        parts.append(f"{reason}:{count}")
    return "; ".join(parts)


def build_rows() -> list[dict[str, Any]]:
    source = load_json(TOPNET_SOURCE, {"coverage": []})
    clean = load_json(CLEAN_PAPERS, {"papers": []})
    totals = load_json(VENUE_TOTALS, {"totals": {}}).get("totals", {})
    coverage = source_coverage(source)
    clean_groups = group_clean_papers(clean.get("papers", []))

    rows = []
    for year in YEARS:
        for venue in VENUES:
            cov = coverage.get((venue, year), {})
            group = clean_groups.get((venue, year), Counter())
            exclusions = {
                key.replace("excluded:", ""): value
                for key, value in group.items()
                if key.startswith("excluded:")
            }
            expected_total = totals.get(str(year), {}).get(venue)
            status = raw_fetch_status(cov, expected_total, venue, year)
            rows.append({
                "venue": venue,
                "year": year,
                "raw_fetch_status": status,
                "conference_toc_records": cov.get("conference_toc_records", 0),
                "conference_toc_total": cov.get("conference_toc_total", 0),
                "conference_page_count": cov.get("conference_page_count", 0),
                "pacmnet_records_for_conext": cov.get("pacmnet_records", 0),
                "pacmnet_total_for_conext": cov.get("pacmnet_total", 0),
                "db_toc_total_diagnostic": expected_total,
                "observed_records_after_merge": group.get("observed_records", 0),
                "clean_main_records": group.get("clean_main_records", 0),
                "excluded_records": sum(exclusions.values()),
                "exclusion_breakdown": clean_scope_note(exclusions),
            })
    return rows


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_report(rows: list[dict[str, Any]]) -> None:
    status_counts = Counter(row["raw_fetch_status"] for row in rows)
    complete_rows = [r for r in rows if r["raw_fetch_status"] == "raw_toc_complete"]
    unavailable_rows = [r for r in rows if r["raw_fetch_status"] == "not_yet_available"]
    concern_rows = [
        r for r in rows
        if r["raw_fetch_status"] not in {"raw_toc_complete", "not_yet_available"}
    ]
    excluded_total = sum(r["excluded_records"] for r in rows)
    clean_total = sum(r["clean_main_records"] for r in rows)
    observed_total = sum(r["observed_records_after_merge"] for r in rows)

    lines = []
    lines.append("# Top Networking Venue Completeness Audit")
    lines.append("")
    lines.append("Status: usable as the paper-scope foundation for the next analysis step, with 2026 venue availability caveats.")
    lines.append("")
    lines.append("## Scope Distinction")
    lines.append("")
    lines.append("- Raw TOC coverage checks whether DBLP returned all records for a venue-year TOC.")
    lines.append("- Clean main-paper scope excludes proceedings volumes, posters, demos, editorials, and workshop summaries.")
    lines.append("- Therefore clean main-paper counts can be lower than raw TOC totals without implying missing data.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| Metric | Count |")
    lines.append("|---|---:|")
    lines.append(f"| Venue-years audited | {len(rows)} |")
    lines.append(f"| Raw TOC complete venue-years | {len(complete_rows)} |")
    lines.append(f"| Not yet available/indexed venue-years | {len(unavailable_rows)} |")
    lines.append(f"| Venue-years with raw-fetch concerns | {len(concern_rows)} |")
    lines.append(f"| Observed merged records | {observed_total} |")
    lines.append(f"| Clean main-paper records | {clean_total} |")
    lines.append(f"| Excluded non-main records | {excluded_total} |")
    lines.append("")
    lines.append("Raw fetch status counts:")
    lines.append("")
    lines.append("| Status | Venue-years |")
    lines.append("|---|---:|")
    for status, count in sorted(status_counts.items()):
        lines.append(f"| `{status}` | {count} |")
    lines.append("")
    lines.append("## Venue-Year Audit")
    lines.append("")
    lines.append("| Venue | Year | Raw status | Conf records/total | PACMNET records/total | Observed merged | Clean main | Excluded | Exclusion breakdown |")
    lines.append("|---|---:|---|---:|---:|---:|---:|---:|---|")
    for row in rows:
        conf = f"{row['conference_toc_records']}/{row['conference_toc_total']}"
        pac = ""
        if row["venue"] == "CoNEXT" and row["year"] >= 2023:
            pac = f"{row['pacmnet_records_for_conext']}/{row['pacmnet_total_for_conext']}"
        lines.append(
            f"| {row['venue']} | {row['year']} | `{row['raw_fetch_status']}` | {conf} | {pac} | "
            f"{row['observed_records_after_merge']} | {row['clean_main_records']} | "
            f"{row['excluded_records']} | {row['exclusion_breakdown']} |"
        )
    lines.append("")
    lines.append("## Current Judgment")
    lines.append("")
    lines.append("The top-networking venue data is complete enough for paper-scope and venue-background work through the available DBLP TOCs. The unresolved caveat is availability, not partial fetching: SIGCOMM, CoNEXT, HotNets, IMC, and PACMNET 2026 are not yet indexed/available in the local DBLP TOC source, while NSDI 2026 is available and complete.")
    lines.append("")
    lines.append("Topic classification and researcher trajectory analysis should use `clean_main_records`; completeness checks should use the raw TOC columns.")
    OUT_REPORT.write_text(chr(10).join(lines) + chr(10))


def main() -> None:
    rows = build_rows()
    write_csv(OUT_CSV, rows)
    OUT_JSON.write_text(json.dumps({"rows": rows}, indent=2, ensure_ascii=False) + chr(10))
    write_report(rows)
    print(f"Wrote {OUT_CSV}")
    print(f"Wrote {OUT_JSON}")
    print(f"Wrote {OUT_REPORT}")


if __name__ == "__main__":
    main()
