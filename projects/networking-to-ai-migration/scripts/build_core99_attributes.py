#!/usr/bin/env python3
"""Build observable researcher attributes for the provisional core-99 sample.

This is a derived table only. It does not modify the raw broad cohort,
publication-history, or itinerary files.
"""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path
from statistics import median
from typing import Any

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
INPUT_FILE = DATA_DIR / "researcher_itineraries.json"
OUTPUT_JSON = DATA_DIR / "core99_researcher_attributes.json"
OUTPUT_CSV = DATA_DIR / "core99_researcher_attributes.csv"
OUTPUT_MD = PROJECT_DIR / "CORE99_RESEARCHER_ATTRIBUTES.md"

BASELINE_YEARS = list(range(2018, 2023))
POST_YEARS = list(range(2023, 2027))
OBSERVATION_YEARS = list(range(2018, 2027))
NETWORK_THRESHOLD = 6
QUALIFYING_VENUES = {"SIGCOMM", "NSDI", "CoNEXT", "HotNets", "IMC"}

# When True, annualized rates use the count of years with actual papers
# rather than the full period length. This corrects for 2026 incompleteness.
USE_EFFECTIVE_YEARS = False

# When set to "fractional", each paper counts as 1/N for N authors.
# When set to "lead_weighted", first-author = 1.0, last-author = 0.5,
# middle = 1/(N-2) for papers with >=3 authors.
# When None (default), all co-authors receive equal credit (1 paper = 1 incidence).
FRACTIONAL_COUNTING: str | None = None  # "fractional" | "lead_weighted" | None

VENUE_ALIASES = {
    "Internet Measurement Conference": "IMC",
    "ACM Internet Measurement Conference": "IMC",
}


def normalize_venue(venue: str) -> str:
    venue = (venue or "Unknown").strip()
    return VENUE_ALIASES.get(venue, venue)


def year_int(year: str | int) -> int:
    return int(year)


def flatten_itinerary(researcher: dict[str, Any]) -> list[dict[str, Any]]:
    papers = []
    for year, items in researcher.get("itinerary", {}).items():
        for item in items:
            paper = dict(item)
            paper["year"] = int(paper.get("year") or year)
            paper["venue_normalized"] = normalize_venue(paper.get("venue", ""))
            paper["is_top_networking"] = paper["venue_normalized"] in QUALIFYING_VENUES
            papers.append(paper)
    papers.sort(key=lambda p: (p["year"], p.get("venue_normalized", ""), p.get("title", "")))
    return papers


def period_papers(papers: list[dict[str, Any]], years: list[int]) -> list[dict[str, Any]]:
    year_set = set(years)
    return [p for p in papers if int(p.get("year") or 0) in year_set]


def count_by_year(papers: list[dict[str, Any]], years: list[int], *, top_networking_only: bool = False) -> dict[str, int]:
    counts = Counter()
    for paper in papers:
        year = int(paper.get("year") or 0)
        if year not in years:
            continue
        if top_networking_only and not paper.get("is_top_networking"):
            continue
        counts[str(year)] += 1
    return {str(year): counts.get(str(year), 0) for year in years}


def venue_counts(papers: list[dict[str, Any]]) -> Counter:
    return Counter(p.get("venue_normalized", "Unknown") for p in papers)


def compact_counts(counter: Counter, limit: int | None = None) -> list[dict[str, Any]]:
    items = counter.most_common(limit)
    return [{"venue": venue, "count": count} for venue, count in items]




def author_role_summary(papers: list[dict[str, Any]]) -> dict[str, Any]:
    total = len(papers)
    matched = [p for p in papers if p.get("author_position") is not None]
    matched_count = len(matched)
    first = sum(1 for p in matched if p.get("is_first_author"))
    last = sum(1 for p in matched if p.get("is_last_author"))
    single = sum(1 for p in matched if p.get("is_single_author"))
    middle = sum(1 for p in matched if not p.get("is_first_author") and not p.get("is_last_author"))
    unmatched = total - matched_count

    def share(count: int) -> float | None:
        return round(count / matched_count, 4) if matched_count else None

    if matched_count == 0:
        profile = "unknown"
    elif share(first) is not None and share(first) >= 0.5:
        profile = "mostly_lead"
    elif share(last) is not None and share(last) >= 0.5:
        profile = "mostly_senior"
    elif share(middle) is not None and share(middle) >= 0.5:
        profile = "mostly_collaborator"
    else:
        profile = "mixed"

    return {
        "paper_count": total,
        "matched_author_position_count": matched_count,
        "unmatched_author_position_count": unmatched,
        "first_author_count": first,
        "last_author_count": last,
        "middle_author_count": middle,
        "single_author_count": single,
        "first_author_share": share(first),
        "last_author_share": share(last),
        "middle_author_share": share(middle),
        "author_role_profile": profile,
    }


def qualifying_venue_mix(counter: Counter) -> str:
    q = {venue: counter.get(venue, 0) for venue in sorted(QUALIFYING_VENUES)}
    total = sum(q.values())
    if total == 0:
        return "none"
    leader, leader_count = max(q.items(), key=lambda item: item[1])
    if leader_count / total >= 0.6:
        return f"{leader}_heavy"
    if sum(1 for c in q.values() if c > 0) >= 3:
        return "mixed_3plus"
    return "mixed_2"


def effective_post_years(post_papers: list[dict[str, Any]]) -> int:
    """Count how many of POST_YEARS have at least one paper.

    Used to correct the annualization denominator when 2026 data is incomplete.
    Returns at least 1 to avoid division by zero.
    """
    years_with_papers = {p["year"] for p in post_papers if p["year"] in POST_YEARS}
    return max(len(years_with_papers), 1)


def fractional_paper_weight(paper: dict[str, Any], scheme: str | None) -> float:
    """Compute fractional weight for a paper based on author contribution.

    Args:
        paper: Paper dict with author_count and optional author_position fields.
        scheme: "fractional" for 1/N, "lead_weighted" for lead-weighted scheme.

    Returns:
        Weight between 0 and 1.
    """
    if scheme is None:
        return 1.0
    author_count = max(paper.get("author_count", 1), 1)
    if scheme == "fractional":
        return 1.0 / author_count
    if scheme == "lead_weighted":
        if paper.get("is_first_author"):
            return 1.0
        if paper.get("is_last_author") and author_count >= 3:
            return 0.5
        # Middle authors share remaining credit
        if author_count <= 2:
            return 0.5  # Two-author paper: both get equal credit
        return 1.0 / (author_count - 2) if author_count > 2 else 1.0
    return 1.0


def annualized_rate_ratio(
    baseline_count: int,
    post_count: int,
    baseline_year_count: int | None = None,
    post_year_count: int | None = None,
) -> float | None:
    bl_years = baseline_year_count if baseline_year_count is not None else len(BASELINE_YEARS)
    po_years = post_year_count if post_year_count is not None else len(POST_YEARS)
    baseline_rate = baseline_count / bl_years
    post_rate = post_count / po_years
    if baseline_rate == 0:
        return None
    return round(post_rate / baseline_rate, 3)


def rate_change_label(
    baseline_count: int,
    post_count: int,
    baseline_year_count: int | None = None,
    post_year_count: int | None = None,
) -> str:
    if post_count == 0:
        return "inactive_after_2022"
    ratio = annualized_rate_ratio(baseline_count, post_count, baseline_year_count, post_year_count)
    if ratio is None:
        return "new_after_2022"
    if ratio >= 1.25:
        return "increased"
    if ratio <= 0.75:
        return "decreased"
    return "flat"


def activity_label(baseline_active_years: int, post_active_years: int) -> str:
    if post_active_years == 0:
        return "inactive_after_2022"
    if baseline_active_years >= 4 and post_active_years >= 3:
        return "continuous"
    if post_active_years >= 3:
        return "post_active"
    if post_active_years == 1:
        return "sporadic_post"
    return "intermittent_post"


def summarize_researcher(researcher: dict[str, Any]) -> dict[str, Any]:
    papers = flatten_itinerary(researcher)
    baseline = period_papers(papers, BASELINE_YEARS)
    post = period_papers(papers, POST_YEARS)
    baseline_top = [p for p in baseline if p.get("is_top_networking")]
    post_top = [p for p in post if p.get("is_top_networking")]
    all_top = [p for p in papers if p.get("is_top_networking")]

    # Fractional / weighted counting
    scheme = FRACTIONAL_COUNTING
    baseline_clean_count_w = round(sum(fractional_paper_weight(p, scheme) for p in baseline), 3)
    post_clean_count_w = round(sum(fractional_paper_weight(p, scheme) for p in post), 3)
    baseline_top_count_w = round(sum(fractional_paper_weight(p, scheme) for p in baseline_top), 3)
    post_top_count_w = round(sum(fractional_paper_weight(p, scheme) for p in post_top), 3)

    baseline_clean_count = len(baseline)
    post_clean_count = len(post)
    total_clean_count = len(papers)
    selection_baseline_top_count = int(researcher.get("baseline_top_networking_count", len(baseline_top)))
    baseline_top_count = len(baseline_top)
    post_top_count = len(post_top)

    baseline_active_years = sum(1 for year, count in count_by_year(baseline, BASELINE_YEARS).items() if count > 0)
    post_active_years = sum(1 for year, count in count_by_year(post, POST_YEARS).items() if count > 0)
    baseline_top_active_years = sum(1 for count in count_by_year(baseline_top, BASELINE_YEARS).values() if count > 0)
    post_top_active_years = sum(1 for count in count_by_year(post_top, POST_YEARS).values() if count > 0)

    baseline_author_roles = author_role_summary(baseline)
    post_author_roles = author_role_summary(post)
    baseline_top_author_roles = author_role_summary(baseline_top)
    post_top_author_roles = author_role_summary(post_top)

    baseline_venues = venue_counts(baseline)
    post_venues = venue_counts(post)
    all_venues = venue_counts(papers)
    baseline_top_venues = venue_counts(baseline_top)
    post_top_venues = venue_counts(post_top)

    # Effective post years: count only years with actual papers
    eff_post_years = effective_post_years(post) if USE_EFFECTIVE_YEARS else None
    eff_post_top_years = effective_post_years(post_top) if USE_EFFECTIVE_YEARS else None
    baseline_year_count = len(BASELINE_YEARS)
    post_year_count = eff_post_years if USE_EFFECTIVE_YEARS else len(POST_YEARS)
    post_top_year_count = eff_post_top_years if USE_EFFECTIVE_YEARS else len(POST_YEARS)

    baseline_rate = round(baseline_top_count / baseline_year_count, 3)
    post_rate = round(post_top_count / post_top_year_count, 3)
    top_rate_ratio = annualized_rate_ratio(baseline_top_count, post_top_count, baseline_year_count, post_top_year_count)
    volume_ratio = round(post_clean_count / baseline_clean_count, 3) if baseline_clean_count else None
    volume_rate_ratio = annualized_rate_ratio(baseline_clean_count, post_clean_count, baseline_year_count, post_year_count)

    result = {
        "name": researcher.get("name", ""),
        "dblp_pid": researcher.get("dblp_pid", ""),
        "identity": researcher.get("identity", {}),
        "selection_baseline_top_networking_count": selection_baseline_top_count,
        "baseline_top_networking_count": baseline_top_count,
        "baseline_top_networking_count_delta_vs_selection": baseline_top_count - selection_baseline_top_count,
        "post2023_top_networking_count": post_top_count,
        "total_top_networking_count": len(all_top),
        "top_networking_count_by_year": count_by_year(papers, OBSERVATION_YEARS, top_networking_only=True),
        "top_networking_rate_baseline_per_year": baseline_rate,
        "top_networking_rate_post2023_per_year": post_rate,
        "top_networking_rate_ratio_post_vs_baseline": top_rate_ratio,
        "top_networking_rate_change": rate_change_label(baseline_top_count, post_top_count, baseline_year_count, post_top_year_count),
        "baseline_clean_publication_count": baseline_clean_count,
        "post2023_clean_publication_count": post_clean_count,
        "clean_publication_count": total_clean_count,
        "clean_publication_count_by_year": count_by_year(papers, OBSERVATION_YEARS),
        "publication_volume_change_ratio_post_vs_baseline": volume_ratio,
        "clean_publication_rate_ratio_post_vs_baseline": volume_rate_ratio,
        "clean_publication_rate_change": rate_change_label(baseline_clean_count, post_clean_count, baseline_year_count, post_year_count),
        "baseline_active_year_count": baseline_active_years,
        "post2023_active_year_count": post_active_years,
        "baseline_top_networking_active_year_count": baseline_top_active_years,
        "post2023_top_networking_active_year_count": post_top_active_years,
        "clean_publication_activity_coverage": activity_label(baseline_active_years, post_active_years),
        "baseline_networking_share": round(baseline_top_count / baseline_clean_count, 4) if baseline_clean_count else None,
        "post2023_networking_share": round(post_top_count / post_clean_count, 4) if post_clean_count else 0,
        "baseline_author_roles": baseline_author_roles,
        "post2023_author_roles": post_author_roles,
        "baseline_top_networking_author_roles": baseline_top_author_roles,
        "post2023_top_networking_author_roles": post_top_author_roles,
        "baseline_first_author_share": baseline_author_roles["first_author_share"],
        "baseline_middle_author_share": baseline_author_roles["middle_author_share"],
        "baseline_last_author_share": baseline_author_roles["last_author_share"],
        "post2023_first_author_share": post_author_roles["first_author_share"],
        "post2023_middle_author_share": post_author_roles["middle_author_share"],
        "post2023_last_author_share": post_author_roles["last_author_share"],
        "baseline_top_networking_first_author_share": baseline_top_author_roles["first_author_share"],
        "baseline_top_networking_middle_author_share": baseline_top_author_roles["middle_author_share"],
        "baseline_top_networking_last_author_share": baseline_top_author_roles["last_author_share"],
        "post2023_top_networking_first_author_share": post_top_author_roles["first_author_share"],
        "post2023_top_networking_middle_author_share": post_top_author_roles["middle_author_share"],
        "post2023_top_networking_last_author_share": post_top_author_roles["last_author_share"],
        "baseline_author_role_profile": baseline_author_roles["author_role_profile"],
        "post2023_author_role_profile": post_author_roles["author_role_profile"],
        "baseline_top_networking_author_role_profile": baseline_top_author_roles["author_role_profile"],
        "post2023_top_networking_author_role_profile": post_top_author_roles["author_role_profile"],
        "qualifying_venue_mix": qualifying_venue_mix(baseline_top_venues),
        "baseline_top_networking_venue_counts": compact_counts(baseline_top_venues),
        "post2023_top_networking_venue_counts": compact_counts(post_top_venues),
        "baseline_venue_portfolio": compact_counts(baseline_venues, 12),
        "post2023_venue_portfolio": compact_counts(post_venues, 12),
        "all_venue_portfolio": compact_counts(all_venues, 15),
        "post_year_denominator": post_year_count,
        "post_year_denominator_is_effective": USE_EFFECTIVE_YEARS,
    }

    # Add fractional counts if enabled
    if scheme:
        result["fractional_counting_scheme"] = scheme
        result["baseline_top_networking_count_fractional"] = baseline_top_count_w
        result["post2023_top_networking_count_fractional"] = post_top_count_w
        result["baseline_clean_publication_count_fractional"] = baseline_clean_count_w
        result["post2023_clean_publication_count_fractional"] = post_clean_count_w
        result["top_networking_rate_ratio_fractional"] = annualized_rate_ratio(
            baseline_top_count_w, post_top_count_w, baseline_year_count, post_top_year_count
        )
        result["clean_publication_rate_ratio_fractional"] = annualized_rate_ratio(
            baseline_clean_count_w, post_clean_count_w, baseline_year_count, post_year_count
        )

    return result




def format_author_role_compact(summary: dict[str, Any]) -> str:
    if not summary or summary.get("matched_author_position_count", 0) == 0:
        return "unknown"
    return (
        f"F:{summary.get('first_author_share')} "
        f"M:{summary.get('middle_author_share')} "
        f"L:{summary.get('last_author_share')} "
        f"({summary.get('author_role_profile')})"
    )


def csv_value(value: Any) -> str:
    if isinstance(value, dict):
        return "; ".join(f"{k}:{v}" for k, v in value.items())
    if isinstance(value, list):
        if value and isinstance(value[0], dict) and "venue" in value[0]:
            return "; ".join(f"{item['venue']}:{item['count']}" for item in value)
        return json.dumps(value, ensure_ascii=False)
    return "" if value is None else str(value)


def write_csv(rows: list[dict[str, Any]]) -> None:
    fields = [
        "name",
        "dblp_pid",
        "selection_baseline_top_networking_count",
        "baseline_top_networking_count",
        "baseline_top_networking_count_delta_vs_selection",
        "post2023_top_networking_count",
        "total_top_networking_count",
        "top_networking_rate_baseline_per_year",
        "top_networking_rate_post2023_per_year",
        "top_networking_rate_ratio_post_vs_baseline",
        "top_networking_rate_change",
        "baseline_clean_publication_count",
        "post2023_clean_publication_count",
        "clean_publication_count",
        "publication_volume_change_ratio_post_vs_baseline",
        "clean_publication_rate_ratio_post_vs_baseline",
        "clean_publication_rate_change",
        "baseline_active_year_count",
        "post2023_active_year_count",
        "baseline_top_networking_active_year_count",
        "post2023_top_networking_active_year_count",
        "clean_publication_activity_coverage",
        "baseline_networking_share",
        "post2023_networking_share",
        "qualifying_venue_mix",
        "baseline_first_author_share",
        "baseline_middle_author_share",
        "baseline_last_author_share",
        "post2023_first_author_share",
        "post2023_middle_author_share",
        "post2023_last_author_share",
        "baseline_top_networking_first_author_share",
        "baseline_top_networking_middle_author_share",
        "baseline_top_networking_last_author_share",
        "post2023_top_networking_first_author_share",
        "post2023_top_networking_middle_author_share",
        "post2023_top_networking_last_author_share",
        "baseline_author_role_profile",
        "post2023_author_role_profile",
        "baseline_top_networking_author_role_profile",
        "post2023_top_networking_author_role_profile",
        "baseline_author_roles",
        "post2023_author_roles",
        "baseline_top_networking_author_roles",
        "post2023_top_networking_author_roles",
        "top_networking_count_by_year",
        "clean_publication_count_by_year",
        "baseline_top_networking_venue_counts",
        "post2023_top_networking_venue_counts",
        "baseline_venue_portfolio",
        "post2023_venue_portfolio",
        "region",
        "sector",
    ]
    with open(OUTPUT_CSV, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            ident = row.get("identity", {})
            out = {field: csv_value(row.get(field)) for field in fields}
            out["region"] = ident.get("region", "Unknown")
            out["sector"] = ident.get("sector", "Unknown")
            writer.writerow(out)


def count_distribution(rows: list[dict[str, Any]], field: str) -> dict[str, int]:
    return dict(Counter(str(r.get(field)) for r in rows).most_common())


def write_markdown(packet: dict[str, Any]) -> None:
    rows = packet["researchers"]
    lines = [
        "# Core-99 Researcher Attributes",
        "",
        "This is a derived attribute table for the provisional core-99 sample. It keeps the broad cohort intact and adds observable/pre-interpretive fields for review.",
        "",
        "## Summary",
        "",
        f"- Researchers: {packet['metadata']['researcher_count']}",
        f"- Selection rule: {packet['metadata']['selection_rule']}",
        f"- Baseline: {packet['metadata']['baseline']}",
        f"- Post-2023 window: {packet['metadata']['post_2023']}",
        f"- Median selection baseline top-networking count: {packet['summary']['median_selection_baseline_top_networking_count']}",
        f"- Median clean-itinerary baseline top-networking count: {packet['summary']['median_clean_baseline_top_networking_count']}",
        f"- Baseline count mismatches versus selection count: {packet['summary']['baseline_top_networking_count_mismatch_count']}",
        f"- Median post-2023 top-networking count: {packet['summary']['median_post2023_top_networking_count']}",
        f"- Median top-networking rate ratio post/base: {packet['summary']['median_top_networking_rate_ratio_post_vs_baseline']}",
        f"- Median total clean publication count: {packet['summary']['median_clean_publication_count']}",
        f"- Median clean-publication rate ratio post/base: {packet['summary']['median_clean_publication_rate_ratio_post_vs_baseline']}",
        "",
        "## Column Definitions",
        "",
        "All labels in this table are deterministic rule-based labels from counts. No LLM is used here.",
        "",
        "- Selection baseline top-net: the original count used to select the core-99 sample from the cohort artifact. It is kept only for traceability.",
        "- Clean baseline top-net: current clean itinerary-derived count in SIGCOMM/NSDI/CoNEXT/HotNets/IMC during 2018-2022. Use this for analysis.",
        "- Post-2023 top-net: current clean count in SIGCOMM/NSDI/CoNEXT/HotNets/IMC during 2023-2026.",
        "- Top-net rate ratio: `(post-2023 top-net / 4) / (clean baseline top-net / 5)`.",
        "- Top-net trend: deterministic label from top-net rate ratio. Increased means ratio >= 1.25, decreased means ratio <= 0.75, flat is between those bounds, and zero post-2023 top-net papers is inactive_after_2022.",
        "- Baseline clean pubs and post-2023 clean pubs: all clean conference/workshop papers in each period, not only top-networking papers.",
        "- Clean-pub rate ratio: `(post-2023 clean pubs / 4) / (baseline clean pubs / 5)`.",
        "- Clean-pub trend: deterministic label using the same thresholds as top-net trend, but applied to all clean publications.",
        "- Clean-pub activity coverage: deterministic label from active publication years. Continuous means >=4 active baseline years and >=3 active post-2023 years; post_active means <4 active baseline years but >=3 active post-2023 years; intermittent_post means 2 active post-2023 years; sporadic_post means 1; inactive_after_2022 means 0.",
        "- Authorship placement uses DBLP author order after explicit alias resolution. First/middle/last shares are computed over papers where the scoped researcher is matched in the author list. Single-author papers count as both first and last.",
        "- Author role profile: mostly_lead if first-author share >= 0.5; mostly_senior if last-author share >= 0.5; mostly_collaborator if middle-author share >= 0.5; mixed otherwise; unknown if no matched author positions.",
        "",
        "## Distributions",
        "",
        "### Top-Networking Rate Change",
        "",
        "| Label | Researchers |",
        "|---|---:|",
    ]
    for label, count in packet["summary"]["top_networking_rate_change_distribution"].items():
        lines.append(f"| {label} | {count} |")
    lines.extend(["", "### Clean-Publication Rate Change", "", "| Label | Researchers |", "|---|---:|"])
    for label, count in packet["summary"]["clean_publication_rate_change_distribution"].items():
        lines.append(f"| {label} | {count} |")
    lines.extend(["", "### Clean-Publication Activity Coverage", "", "| Label | Researchers |", "|---|---:|"])
    for label, count in packet["summary"]["clean_publication_activity_coverage_distribution"].items():
        lines.append(f"| {label} | {count} |")
    lines.extend(["", "### Qualifying Venue Mix", "", "| Label | Researchers |", "|---|---:|"])
    for label, count in packet["summary"]["qualifying_venue_mix_distribution"].items():
        lines.append(f"| {label} | {count} |")
    lines.extend(["", "### Baseline Author-Role Profile", "", "| Label | Researchers |", "|---|---:|"])
    for label, count in packet["summary"]["baseline_author_role_profile_distribution"].items():
        lines.append(f"| {label} | {count} |")
    lines.extend(["", "### Post-2023 Author-Role Profile", "", "| Label | Researchers |", "|---|---:|"])
    for label, count in packet["summary"]["post2023_author_role_profile_distribution"].items():
        lines.append(f"| {label} | {count} |")

    lines.extend([
        "",
        "## Researcher Attributes",
        "",
        "| Researcher | Selection baseline top-net | Clean baseline top-net | Post-2023 top-net | Top-net rate ratio | Top-net trend | Baseline clean pubs | Post-2023 clean pubs | Clean-pub rate ratio | Clean-pub trend | Clean-pub activity coverage | All-clean authorship baseline | All-clean authorship post | Top-net authorship baseline | Top-net authorship post | Venue mix | Baseline top venues | Post top venues |",
        "|---|---:|---:|---:|---:|---|---:|---:|---:|---|---|---|---|---|---|---|---|---|",
    ])
    for row in rows:
        lines.append(
            f"| {row['name']} | {row['selection_baseline_top_networking_count']} | "
            f"{row['baseline_top_networking_count']} | {row['post2023_top_networking_count']} | "
            f"{row['top_networking_rate_ratio_post_vs_baseline']} | {row['top_networking_rate_change']} | "
            f"{row['baseline_clean_publication_count']} | {row['post2023_clean_publication_count']} | "
            f"{row['clean_publication_rate_ratio_post_vs_baseline']} | {row['clean_publication_rate_change']} | "
            f"{row['clean_publication_activity_coverage']} | "
            f"{format_author_role_compact(row['baseline_author_roles'])} | "
            f"{format_author_role_compact(row['post2023_author_roles'])} | "
            f"{format_author_role_compact(row['baseline_top_networking_author_roles'])} | "
            f"{format_author_role_compact(row['post2023_top_networking_author_roles'])} | "
            f"{row['qualifying_venue_mix']} | "
            f"{csv_value(row['baseline_top_networking_venue_counts'])} | "
            f"{csv_value(row['post2023_top_networking_venue_counts'])} |"
        )
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

    packet = {
        "metadata": {
            "phase": "build_core99_attributes",
            "input_file": str(INPUT_FILE.relative_to(PROJECT_DIR)),
            "selection_rule": f"baseline_top_networking_count > {NETWORK_THRESHOLD}",
            "raw_data_policy": "Derived attributes only; raw cohort, publication history, and itinerary files are not modified.",
            "baseline": "2018-2022",
            "post_2023": "2023-2026",
            "researcher_count": len(rows),
            "venue_aliases_applied": VENUE_ALIASES,
            "rate_change_rule": "For a metric count, compare annualized post-2023 rate against annualized baseline rate: ratio >=1.25 is increased, ratio <=0.75 is decreased, otherwise flat; zero post count is inactive_after_2022.",
            "activity_coverage_rule": "Continuous means >=4 active baseline years and >=3 active post-2023 years; post_active means <4 active baseline years but >=3 active post-2023 years; intermittent_post means 2 active post-2023 years; sporadic_post means 1; inactive_after_2022 means 0.",
        },
        "summary": {
            "median_selection_baseline_top_networking_count": median([r["selection_baseline_top_networking_count"] for r in rows]) if rows else 0,
            "median_clean_baseline_top_networking_count": median([r["baseline_top_networking_count"] for r in rows]) if rows else 0,
            "baseline_top_networking_count_mismatch_count": sum(1 for r in rows if r["baseline_top_networking_count_delta_vs_selection"] != 0),
            "median_post2023_top_networking_count": median([r["post2023_top_networking_count"] for r in rows]) if rows else 0,
            "median_top_networking_rate_ratio_post_vs_baseline": median([r["top_networking_rate_ratio_post_vs_baseline"] for r in rows if r["top_networking_rate_ratio_post_vs_baseline"] is not None]) if rows else 0,
            "median_clean_publication_count": median([r["clean_publication_count"] for r in rows]) if rows else 0,
            "median_clean_publication_rate_ratio_post_vs_baseline": median([r["clean_publication_rate_ratio_post_vs_baseline"] for r in rows if r["clean_publication_rate_ratio_post_vs_baseline"] is not None]) if rows else 0,
            "top_networking_rate_change_distribution": count_distribution(rows, "top_networking_rate_change"),
            "clean_publication_rate_change_distribution": count_distribution(rows, "clean_publication_rate_change"),
            "clean_publication_activity_coverage_distribution": count_distribution(rows, "clean_publication_activity_coverage"),
            "qualifying_venue_mix_distribution": count_distribution(rows, "qualifying_venue_mix"),
            "baseline_author_role_profile_distribution": count_distribution(rows, "baseline_author_role_profile"),
            "post2023_author_role_profile_distribution": count_distribution(rows, "post2023_author_role_profile"),
        },
        "researchers": rows,
    }

    with open(OUTPUT_JSON, "w") as f:
        json.dump(packet, f, indent=2, ensure_ascii=False)
    write_csv(rows)
    write_markdown(packet)

    print(f"Core-99 researchers: {len(rows)}")
    print(f"Wrote {OUTPUT_JSON}")
    print(f"Wrote {OUTPUT_CSV}")
    print(f"Wrote {OUTPUT_MD}")
    return packet


if __name__ == "__main__":
    run()
