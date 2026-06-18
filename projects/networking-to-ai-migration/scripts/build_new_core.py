#!/usr/bin/env python3
"""Build the neutral new-core cohort from a canonical clean paper table.

This replaces the exploratory post-GPT core path for cohort construction. It is
network-free: it reuses existing local artifacts, applies explicit main-paper
scope rules, and keeps source/coverage diagnostics visible.

Outputs:
  - data/new_core_clean_papers.json
  - data/new_core.json
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from publication_scope import exclusion_reason, normalize_title

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

RAW_BASELINE = DATA_DIR / "raw_dblp_papers.json"
POST_VENUE_PAPERS = DATA_DIR / "post_gpt_venue_papers.json"
PACMNET_TOC_PAPERS = DATA_DIR / "pacmnet_toc_papers.json"
ITINERARIES = DATA_DIR / "researcher_itineraries.json"
CORE99_ATTRS = DATA_DIR / "core99_researcher_attributes.json"
VENUE_TOTALS = DATA_DIR / "venue_accepted_totals.json"
OLD_POST_CORE = DATA_DIR / "post_gpt_core.json"

OUTPUT_PAPERS = DATA_DIR / "new_core_clean_papers.json"
OUTPUT_CORE = DATA_DIR / "new_core.json"

BASELINE_YEARS = set(range(2018, 2023))
NEW_CORE_YEARS = set(range(2023, 2027))
ALL_YEARS = BASELINE_YEARS | NEW_CORE_YEARS
QUALIFYING_VENUES = {"SIGCOMM", "NSDI", "CoNEXT", "HotNets", "IMC", "PACMNET"}
DISPLAY_QUALIFYING_VENUES = ["SIGCOMM", "NSDI", "CoNEXT", "HotNets", "IMC"]
THRESHOLD = 7

NON_MAIN_PREFIX_RE = re.compile(r"^\s*(poster|demo|proceedings)\b", re.IGNORECASE)
CONEXT_WORKSHOP_RE = re.compile(
    r"(workshop|student workshop|workshop summary|chairs workshop summary|" 
    r"\bPN['&]?(?:25)?\b|BlockNetSys|ECCAI|INet4AI|INCAS|CNC Workshop)",
    re.IGNORECASE,
)
POSTER_DEMO_VENUE_RE = re.compile(r"\b(posters?|demos?)\b", re.IGNORECASE)


def load_json(path: Path, default: Any = None) -> Any:
    if not path.exists():
        return default
    with open(path) as f:
        return json.load(f)


def canonical_venue(venue: str) -> str:
    venue = (venue or "").strip()
    aliases = {
        "Internet Measurement Conference": "IMC",
        "ACM Internet Measurement Conference": "IMC",
        "Proceedings of the ACM on Networking": "PACMNET",
    }
    return aliases.get(venue, venue)


def infer_canonical_venue(paper: dict[str, Any]) -> str:
    dblp_url = paper.get("dblp_url", "") or ""
    dblp_key = paper.get("dblp_key", "") or paper.get("key", "") or ""
    if "journals/pacmnet" in dblp_url or dblp_key.startswith("journals/pacmnet"):
        return "PACMNET"
    return canonical_venue(paper.get("venue", ""))


def paper_key(title: str, venue: str, year: int) -> str:
    return f"{normalize_title(title)}|{canonical_venue(venue)}|{year}"


def normalize_person_name(name: str) -> str:
    return re.sub(r"\s+\d{4}$", "", name or "").strip().casefold()


def build_name_pid_lookup() -> dict[str, str]:
    candidates: dict[str, set[str]] = defaultdict(set)

    itins = load_json(ITINERARIES, {"researchers": []})
    for r in itins.get("researchers", []):
        pid = r.get("dblp_pid", "")
        name = r.get("name", "")
        if pid and name:
            candidates[normalize_person_name(name)].add(pid)

    core99 = load_json(CORE99_ATTRS, {"researchers": []})
    for r in core99.get("researchers", []):
        pid = r.get("dblp_pid", "")
        name = r.get("name", "")
        if pid and name:
            candidates[normalize_person_name(name)].add(pid)

    old = load_json(OLD_POST_CORE, {})
    for group in old.get("tripartite_split", {}).values() if isinstance(old, dict) else []:
        for r in group.get("researchers", []):
            pid = r.get("dblp_pid", "")
            name = r.get("name", "")
            if pid and name:
                candidates[normalize_person_name(name)].add(pid)

    # Resolve only unambiguous names. Ambiguous names stay unresolved rather than
    # silently assigning the wrong PID.
    return {name: next(iter(pids)) for name, pids in candidates.items() if len(pids) == 1}


def extract_author_entries(raw_authors: list[Any], name_to_pid: dict[str, str] | None = None) -> list[dict[str, str]]:
    authors = []
    name_to_pid = name_to_pid or {}
    for author in raw_authors or []:
        if isinstance(author, dict):
            pid = author.get("pid") or author.get("@pid") or ""
            name = author.get("name") or author.get("text") or ""
        else:
            pid = ""
            name = str(author)
        if not pid and name:
            pid = name_to_pid.get(normalize_person_name(name), "")
        if pid or name:
            authors.append({"pid": pid, "name": name})
    return authors


def main_paper_exclusion(paper: dict[str, Any]) -> str | None:
    """Return an exclusion reason for non-main-paper records.

    `publication_scope.py` catches generic journals/editorials/proceedings-volume
    patterns. This local layer catches DBLP TOC records that are syntactically
    paper-like but clearly posters, demos, or workshop summaries.
    """
    scoped_reason = exclusion_reason(paper)
    if scoped_reason:
        return scoped_reason

    title = paper.get("title", "") or ""
    venue = paper.get("venue", "") or ""
    if NON_MAIN_PREFIX_RE.search(title):
        return "non_main_prefix"
    if POSTER_DEMO_VENUE_RE.search(venue):
        return "poster_demo_venue"
    if canonical_venue(venue) == "CoNEXT" and CONEXT_WORKSHOP_RE.search(title):
        return "conext_workshop_or_summary"
    return None


def add_or_merge_paper(
    papers: dict[str, dict[str, Any]],
    paper: dict[str, Any],
    *,
    source: str,
    partial_author_pids: bool = False,
    force_include: bool = False,
    name_to_pid: dict[str, str] | None = None,
) -> None:
    title = (paper.get("title") or "").rstrip(".")
    year = int(paper.get("year") or 0)
    venue = infer_canonical_venue(paper)
    if year not in ALL_YEARS or venue not in QUALIFYING_VENUES or not title:
        return

    work = dict(paper)
    work["title"] = title
    work["venue"] = venue
    reason = None if force_include else main_paper_exclusion(work)
    included = reason is None
    key = paper_key(title, venue, year)
    authors = extract_author_entries(work.get("authors") or [], name_to_pid)
    unresolved_pid_count = sum(1 for author in authors if not author.get("pid"))

    if key not in papers:
        papers[key] = {
            "paper_id": key,
            "title": title,
            "venue": venue,
            "venue_group": "CoNEXT" if venue == "PACMNET" else venue,
            "year": year,
            "dblp_url": work.get("dblp_url", ""),
            "doi": work.get("doi", ""),
            "authors": [],
            "author_pids": [],
            "sources": [],
            "included_in_new_core_scope": included,
            "exclusion_reason": reason,
            "partial_author_pids": partial_author_pids or unresolved_pid_count > 0,
            "author_pid_unresolved_count": unresolved_pid_count,
        }

    entry = papers[key]
    if source not in entry["sources"]:
        entry["sources"].append(source)
    if partial_author_pids or unresolved_pid_count > 0:
        entry["partial_author_pids"] = True
    if included and not entry["included_in_new_core_scope"]:
        entry["included_in_new_core_scope"] = True
        entry["exclusion_reason"] = None

    by_name = {normalize_person_name(a.get("name", "")): a for a in entry["authors"] if a.get("name")}
    seen = {a.get("pid") or f"name:{a.get('name','')}" for a in entry["authors"]}
    for author in authors:
        norm_name = normalize_person_name(author.get("name", ""))
        existing = by_name.get(norm_name)
        if existing:
            if author.get("pid") and not existing.get("pid"):
                existing["pid"] = author["pid"]
            continue
        identity = author.get("pid") or f"name:{author.get('name','')}"
        if identity and identity not in seen:
            entry["authors"].append(author)
            seen.add(identity)
            if norm_name:
                by_name[norm_name] = author

    entry["author_pids"] = sorted({a["pid"] for a in entry["authors"] if a.get("pid")})
    entry["author_pid_unresolved_count"] = sum(1 for a in entry["authors"] if not a.get("pid"))
    if entry["author_pid_unresolved_count"] == 0:
        entry["partial_author_pids"] = False


def build_papers() -> tuple[dict[str, dict[str, Any]], dict[str, Any]]:
    papers: dict[str, dict[str, Any]] = {}
    diagnostics: dict[str, Any] = {"inputs": {}, "notes": []}
    name_to_pid = build_name_pid_lookup()
    diagnostics["inputs"]["unambiguous_name_pid_lookup_size"] = len(name_to_pid)

    raw_baseline = load_json(RAW_BASELINE, [])
    diagnostics["inputs"]["raw_dblp_papers"] = len(raw_baseline)
    for p in raw_baseline:
        if int(p.get("year") or 0) in BASELINE_YEARS:
            add_or_merge_paper(papers, p, source="raw_dblp_papers", name_to_pid=name_to_pid)

    post_data = load_json(POST_VENUE_PAPERS, {"papers": []})
    post_papers = post_data.get("papers", [])
    diagnostics["inputs"]["post_gpt_venue_papers"] = len(post_papers)
    diagnostics["inputs"]["post_gpt_venue_papers_metadata"] = post_data.get("metadata", {})
    for p in post_papers:
        year = int(p.get("year") or 0)
        if year in NEW_CORE_YEARS:
            add_or_merge_paper(papers, p, source="post_gpt_venue_papers", name_to_pid=name_to_pid)

    pacmnet_data = load_json(PACMNET_TOC_PAPERS, {"papers": []})
    pacmnet_papers = pacmnet_data.get("papers", [])
    diagnostics["inputs"]["pacmnet_toc_papers"] = len(pacmnet_papers)
    diagnostics["inputs"]["pacmnet_toc_papers_metadata"] = pacmnet_data.get("metadata", {})
    for p in pacmnet_papers:
        year = int(p.get("year") or 0)
        if year in NEW_CORE_YEARS:
            add_or_merge_paper(papers, p, source="pacmnet_toc_papers", name_to_pid=name_to_pid)

    # Add PACMNET long-paper evidence from the clean itinerary path. This is
    # author-partial: it only contains broad-cohort researchers whose histories
    # have already been fetched. That limitation is explicit in the output.
    itins = load_json(ITINERARIES, {"researchers": []})
    diagnostics["inputs"]["researcher_itineraries"] = len(itins.get("researchers", []))
    pacmnet_rows = 0
    for researcher in itins.get("researchers", []):
        pid = researcher.get("dblp_pid", "")
        name = researcher.get("name", "")
        for year_s, items in researcher.get("itinerary", {}).items():
            year = int(year_s)
            if year not in NEW_CORE_YEARS:
                continue
            for item in items:
                if canonical_venue(item.get("venue", "")) != "PACMNET":
                    continue
                paper = dict(item)
                paper["venue"] = "PACMNET"
                paper["authors"] = [{"pid": pid, "name": name}] if pid else [{"pid": "", "name": name}]
                add_or_merge_paper(
                    papers,
                    paper,
                    source="researcher_itineraries_pacmnet",
                    partial_author_pids=True,
                    force_include=True,
                    name_to_pid=name_to_pid,
                )
                pacmnet_rows += 1
    diagnostics["inputs"]["pacmnet_itinerary_rows"] = pacmnet_rows
    diagnostics["notes"].append(
        "PACMNET records are read from data/pacmnet_toc_papers.json when available; local venue-paper and itinerary records are merged as auxiliary evidence."
    )

    return papers, diagnostics


def count_authors(papers: dict[str, dict[str, Any]], years: set[int]) -> Counter:
    counts = Counter()
    for paper in papers.values():
        if paper["year"] not in years or not paper["included_in_new_core_scope"]:
            continue
        for pid in paper.get("author_pids", []):
            counts[pid] += 1
    return counts


def build_name_lookup(papers: dict[str, dict[str, Any]], itineraries: dict[str, Any]) -> dict[str, str]:
    names = {}
    for r in itineraries.get("researchers", []):
        if r.get("dblp_pid"):
            names[r["dblp_pid"]] = r.get("name", "Unknown")
    for paper in papers.values():
        for author in paper.get("authors", []):
            pid = author.get("pid", "")
            if pid and pid not in names:
                names[pid] = author.get("name", "Unknown")
    return names


def coverage_summary(papers: dict[str, dict[str, Any]]) -> dict[str, Any]:
    by_vy = defaultdict(lambda: Counter())
    for paper in papers.values():
        venue = paper["venue_group"]
        year = str(paper["year"])
        c = by_vy[f"{venue}|{year}"]
        c["raw_or_observed"] += 1
        if paper["included_in_new_core_scope"]:
            c["clean"] += 1
        else:
            c[f"excluded:{paper.get('exclusion_reason')}"] += 1
        if paper.get("partial_author_pids"):
            c["partial_author_pids"] += 1

    totals = load_json(VENUE_TOTALS, {"totals": {}}).get("totals", {})
    rows = []
    for year in sorted(ALL_YEARS):
        for venue in DISPLAY_QUALIFYING_VENUES:
            key = f"{venue}|{year}"
            c = by_vy.get(key, Counter())
            rows.append({
                "venue": venue,
                "year": year,
                "observed_records": c.get("raw_or_observed", 0),
                "clean_main_records": c.get("clean", 0),
                "partial_author_pid_records": c.get("partial_author_pids", 0),
                "dblp_toc_total_diagnostic": totals.get(str(year), {}).get(venue),
                "coverage_status": "missing" if c.get("raw_or_observed", 0) == 0 else "observed",
                "exclusions": {k.replace("excluded:", ""): v for k, v in c.items() if k.startswith("excluded:")},
            })
    return {"venue_years": rows}


def researcher_entry(pid: str, name: str, baseline_counts: Counter, post_counts: Counter, broad_pids: set[str], core99_pids: set[str]) -> dict[str, Any]:
    return {
        "dblp_pid": pid,
        "name": name,
        "baseline_top_networking_count": baseline_counts.get(pid, 0),
        "new_core_observed_top_networking_count": post_counts.get(pid, 0),
        "in_core99": pid in core99_pids,
        "in_broad_cohort": pid in broad_pids,
        "profile_coverage_expected": "itinerary_available" if pid in broad_pids else "dblp_toc_only",
    }


def main() -> None:
    papers, diagnostics = build_papers()
    clean_papers = [p for p in papers.values() if p["included_in_new_core_scope"]]

    baseline_counts = count_authors(papers, BASELINE_YEARS)
    post_counts = count_authors(papers, NEW_CORE_YEARS)

    itins = load_json(ITINERARIES, {"researchers": []})
    broad_pids = {r.get("dblp_pid", "") for r in itins.get("researchers", []) if r.get("dblp_pid")}
    names = build_name_lookup(papers, itins)

    core99 = load_json(CORE99_ATTRS, {"researchers": []})
    core99_pids = {r.get("dblp_pid", "") for r in core99.get("researchers", []) if r.get("dblp_pid")}

    new_core_pids = {pid for pid, count in post_counts.items() if count >= THRESHOLD}
    stayer_pids = new_core_pids & core99_pids
    newcomer_pids = new_core_pids - core99_pids
    dropout_pids = core99_pids - new_core_pids

    def make_entries(pids: set[str]) -> list[dict[str, Any]]:
        return sorted(
            [researcher_entry(pid, names.get(pid, "Unknown"), baseline_counts, post_counts, broad_pids, core99_pids) for pid in pids],
            key=lambda r: (-r["new_core_observed_top_networking_count"], r["name"]),
        )

    complete_newcomers = [
        r for r in make_entries(newcomer_pids)
        if r["baseline_top_networking_count"] == 0 and not r["in_broad_cohort"]
    ]

    old = load_json(OLD_POST_CORE, {})
    old_summary = old.get("summary", {}) if isinstance(old, dict) else {}

    papers_output = {
        "metadata": {
            "phase": "build_new_core_clean_papers",
            "description": "Canonical clean-paper table for neutral new-core construction.",
            "years": sorted(ALL_YEARS),
            "new_core_years": sorted(NEW_CORE_YEARS),
            "qualifying_venues": DISPLAY_QUALIFYING_VENUES,
            "threshold": THRESHOLD,
            "paper_count_total_records": len(papers),
            "paper_count_clean_records": len(clean_papers),
            "diagnostics": diagnostics,
        },
        "coverage": coverage_summary(papers),
        "papers": sorted(papers.values(), key=lambda p: (p["year"], p["venue_group"], p["title"])),
    }
    with open(OUTPUT_PAPERS, "w") as f:
        json.dump(papers_output, f, indent=2, ensure_ascii=False)

    core_output = {
        "metadata": {
            "phase": "build_new_core",
            "description": "Neutral current leading cohort: researchers with >=7 clean qualifying top-networking papers in observed 2023-2026.",
            "selection_threshold": THRESHOLD,
            "baseline_years": sorted(BASELINE_YEARS),
            "new_core_years": sorted(NEW_CORE_YEARS),
            "qualifying_venues": DISPLAY_QUALIFYING_VENUES,
            "pacmnet_policy": "PACMNET is treated as CoNEXT conference-integrated evidence; DBLP PACMNET TOC records are used when available, with local itinerary evidence merged for diagnostics.",
            "coverage_warning": "2026 is observed as available; SIGCOMM/CoNEXT/HotNets/IMC 2026 are currently missing from local venue-paper artifacts.",
        },
        "summary": {
            "core99_size": len(core99_pids),
            "new_core_size": len(new_core_pids),
            "stayer_count": len(stayer_pids),
            "newcomer_count": len(newcomer_pids),
            "dropout_count": len(dropout_pids),
            "newcomers_from_outside_broad_cohort": len(complete_newcomers),
            "newcomers_from_within_broad_cohort": len(newcomer_pids) - len(complete_newcomers),
            "overlap_rate_pct": round(len(stayer_pids) / len(core99_pids) * 100, 1) if core99_pids else None,
            "renewal_rate_pct": round(len(newcomer_pids) / len(new_core_pids) * 100, 1) if new_core_pids else None,
            "old_post_gpt_summary_for_comparison": old_summary,
        },
        "tripartite_split": {
            "stayers": {"count": len(stayer_pids), "researchers": make_entries(stayer_pids)},
            "newcomers": {"count": len(newcomer_pids), "researchers": make_entries(newcomer_pids)},
            "dropouts": {"count": len(dropout_pids), "researchers": make_entries(dropout_pids)},
        },
        "coverage": coverage_summary(papers),
    }
    with open(OUTPUT_CORE, "w") as f:
        json.dump(core_output, f, indent=2, ensure_ascii=False)

    print(f"Wrote {OUTPUT_PAPERS}")
    print(f"Wrote {OUTPUT_CORE}")
    print("Summary:")
    for k, v in core_output["summary"].items():
        if k != "old_post_gpt_summary_for_comparison":
            print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
