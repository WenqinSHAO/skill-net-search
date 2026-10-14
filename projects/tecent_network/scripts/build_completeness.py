#!/usr/bin/env python3
"""Account for each publication; a missing Tencent string never certifies recall."""
from __future__ import annotations

import argparse
import difflib
import hashlib
import html
import json
import re
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime, timezone
from urllib.parse import quote, urljoin

from bs4 import BeautifulSoup

from collect import ROOT, WORKSPACE, fetch, parenthetical_authors, save, text, usenix_authors

VENUES = ["NSDI", "SIGCOMM", "CoNEXT", "IMC", "HotNets"]
TENCENT = re.compile(r"\btencent\b|腾讯", re.I)


def key(value):
    value = html.unescape(value or "")
    if "<" in value:
        value = BeautifulSoup(value, "html.parser").get_text(" ")
    value = unicodedata.normalize("NFKC", value).casefold()
    return re.sub(r"[^\w]+", "", value)


def author_key(value):
    return key(re.sub(r" \d{4}$", "", value))


def doi_from(value):
    match = re.search(r"10\.\d{4,9}/[^\s?#\"<>]+", value or "")
    return match.group().rstrip(".,)") if match else ""


def without_title(block, heading):
    """Remove only the title, not all bold nodes (which can contain authors)."""
    raw = text(block)
    title = text(heading)
    return raw[len(title):].strip() if raw.startswith(title) else ""


def evidence(heading, people, block, page, authors=None):
    heading_copy = BeautifulSoup(str(heading), "html.parser")
    for badge in heading_copy.select(".label, .badge"):
        badge.decompose()
    title = text(heading_copy)
    title = re.sub(r"\s*(?:-\s*Won\s+|\s+)(?:Long\s+|Short\s+)?(?:Best Paper(?: Award)?|Best Community(?: Contribution)?(?: Award)?|Community Contribution Award)$", "", title, flags=re.I)
    title = re.sub(r"\s+(?:long|short)(?: paper)?$", "", title, flags=re.I)
    title = re.sub(r"\s+(?:Research|Experience|Industrial) Track.*$", "", title)
    title = re.sub(r"\s*\((?:Experience|Research|Industrial) Paper\)\s*$", "", title, flags=re.I)
    title = re.sub(r"^#\d+\s+", "", title).strip()
    line = text(people) if not isinstance(people, str) else people
    links = [a.get("href", "") for a in block.select("a[href]")]
    base_node = block.find_parent("html")
    base_tag = base_node.select_one("base[href]") if base_node else None
    base = urljoin(page["url"], base_tag["href"]) if base_tag else re.sub(r"partials/.*$", "", page["url"])
    pdfs = [urljoin(base, href) for href in links if ".pdf" in href.lower() and "slides" not in href.lower()]
    doi = next((doi_from(href) for href in links if doi_from(href)), "")
    return {"title": title, "title_key": key(title), "author_line": line,
            "authors": authors if authors is not None else parenthetical_authors(line),
            "url": page["url"], "cache_file": page["cache_file"], "retrieved_at": page.get("retrieved_at", ""),
            "doi": doi, "pdf_urls": pdfs, "block_text": text(block)[:16000]}


def parse_page(page):
    soup = BeautifulSoup((ROOT / page["cache_file"]).read_text(), "html.parser")
    venue, year = page["venue"], page["year"]
    out = []
    if venue == "NSDI":
        for block in soup.select(".node-paper"):
            heading = block.select_one("h2 a, h3 a")
            people = block.select_one(".field-name-field-paper-people-text")
            if heading and people:
                item = evidence(heading, people, block, page, usenix_authors(people))
                item["paper_url"] = urljoin(page["url"], heading.get("href", ""))
                out.append(item)
        return out
    if venue == "SIGCOMM":
        if soup.select("b.paper-title"):
            for heading in soup.select("b.paper-title"):
                block = heading.find_parent("p")
                people = block.select_one(".table-description")
                if people:
                    item = evidence(heading, people, block, page)
                    item["doi"] = doi_from(heading.get("data-pdf", ""))
                    out.append(item)
        elif soup.select("table.long_table_program p.style_italic"):
            for block in soup.select("table.long_table_program tr"):
                people, heading = block.select_one("p.style_italic"), block.select_one(".text-color-primary")
                if people and heading:
                    out.append(evidence(heading, people, block, page))
        elif soup.select("div.collapse .collapse-title"):
            for block in soup.select("div.collapse"):
                heading, people = block.select_one(".collapse-title .font-semibold"), block.select_one(".collapse-title .font-normal")
                if heading and people:
                    out.append(evidence(heading, people, block, page))
        else:
            # A td can contain several papers; iterate headings, not table cells.
            headings = soup.select("td h2, td .paper-header")
            for heading in headings:
                if heading.select_one("h2") or heading.find_parent(class_="keynote-header"):
                    continue
                people = heading.find_next("p")
                if people is not None and not text(people).startswith("Abstract"):
                    item = evidence(heading, people, heading.find_parent("td"), page)
                    item["doi"] = doi_from(str(heading))
                    out.append(item)
        for block in soup.select("li, td"):
            people = block.select_one("p.style_italic, .table-description, p.text-base")
            heading = block.select_one(".text-color-primary, b, p.font-bold")
            if people and heading:
                out.append(evidence(heading, people, block, page))
        return out
    if venue in {"CoNEXT", "IMC"}:
        for body in soup.select(".paper-entry .paper-body"):
            heading = body.select_one("strong")
            divs = body.find_all("div", recursive=False)
            if heading and len(divs) >= 2 and body.find_parent("li"):
                out.append(evidence(heading, divs[1], body.find_parent("li"), page))
        for block in soup.select("li.list-group-item"):
            col = block.select_one(".col-md-7")
            if not col:
                continue
            heading = col.select_one("strong, .title")
            if not heading:
                continue
            direct_divs = col.find_all("div", recursive=False)
            people = direct_divs[1] if len(direct_divs) > 1 else None
            if people and len(text(heading)) > 12:
                out.append(evidence(heading, people, block, page))
        for heading in soup.select(".title"):
            block = heading.find_parent("li")
            if block and block.select_one(".author"):
                out.append(evidence(heading, block.select_one(".author"), block, page))
        if "accepted" in page["url"] or page.get("publication_type") == "poster":
            for heading in soup.select("main li strong, main li u, main p strong, li > u, li > b, p > strong"):
                block = heading.find_parent("li") or heading.find_parent("p")
                if block and len(without_title(block, heading)) > 5 and len(text(heading)) > 12:
                    out.append(evidence(heading, without_title(block, heading), block, page))
        return out
    if venue == "HotNets":
        for block in soup.select("li.accepted_papers"):
            heading, people = block.select_one(".accepted_title, strong"), block.select_one(".accepted_authors")
            if heading and people:
                out.append(evidence(heading, people, block, page))
        for block in soup.select("td"):
            heading = block.find("b", recursive=False)
            if not heading or len(text(heading)) < 12 or re.match(r"Session|Keynote|Panel|Welcome|Lunch|Break|[0-9]+:", text(heading), re.I):
                continue
            people = block.find("i", recursive=False)
            line = text(people) if people else without_title(block, heading)
            line = re.split(r"\[(?:PDF|Digital Library)\]|Abstract:", line)[0].strip()
            out.append(evidence(heading, line, block, page))
        return out
    return out


def load_sources():
    discovery = json.loads((ROOT / "data/program_discovery.json").read_text())
    pages = [p for p in discovery["pages"] if "/partials/toc.html" not in p["url"] and ("program" in p["url"] or "accepted" in p["url"])]
    coverage = json.loads((ROOT / "data/coverage.json").read_text())
    for p in coverage["attempts"]:
        if p["venue"] in {"NSDI", "SIGCOMM"} and p.get("year", 0) >= 2019 and p.get("source_cache"):
            pages.append({**p, "cache_file": p["source_cache"]})
    # Poster and publisher-TOC pages use these same parsers where possible.
    extra = ROOT / "data/completeness_sources.json"
    if extra.exists():
        pages += json.loads(extra.read_text()).get("pages", [])
    unique = {(p["venue"], p["year"], p["url"]): p for p in pages}
    blocks = defaultdict(list)
    logs = []
    for page in unique.values():
        try:
            if page["venue"] == "CoNEXT" and page["year"] == 2022 and page.get("publication_type") == "poster":
                content = BeautifulSoup((ROOT / page["cache_file"]).read_text(), "html.parser").get_text(" ", strip=True)
                if re.match(r"CoNEXT 2020 (Student Workshop Program|Call for Posters)", content):
                    logs.append({"venue": page["venue"], "year": page["year"], "url": page["url"],
                        "cache_file": page["cache_file"], "paper_blocks": 0, "status": "excluded_stale_template",
                        "detail": "2022 URL serves a CoNEXT 2020 heading and content; not evidence of 2022 publications."})
                    continue
            entries = parse_page(page)
            for entry in entries:
                if entry["title_key"]:
                    entry["source_publication_type"] = page.get("publication_type", "")
                    blocks[(page["venue"], page["year"])].append(entry)
            logs.append({"venue": page["venue"], "year": page["year"], "url": page["url"], "cache_file": page["cache_file"],
                         "paper_blocks": len(entries), "status": "parsed" if entries else "no_supported_paper_blocks"})
        except Exception as exc:
            logs.append({"venue": page["venue"], "year": page["year"], "url": page["url"], "status": "parse_error", "detail": str(exc)})
    return blocks, logs


def refresh_recent_catalog():
    records, attempts = [], []
    tasks = [(v, f"db/conf/{'conext' if v == 'CoNEXT' else v.lower()}/{('conext' if v == 'CoNEXT' else v.lower())}2026") for v in VENUES]
    tasks += [("PACMNET", "db/journals/pacmnet/pacmnet4")]
    for venue, toc in tasks:
        url = "https://dblp.org/search/publ/api?q=" + quote("toc:" + toc + ".bht:") + "&format=json&h=1000&f=0"
        try:
            raw, info = fetch(url)
            response = json.loads(raw)["result"]["hits"]
            hits = response.get("hit", [])
            if isinstance(hits, dict):
                hits = [hits]
            for hit in hits:
                p = hit["info"]
                authors = p.get("authors", {}).get("author", [])
                if isinstance(authors, dict) or isinstance(authors, str):
                    authors = [authors]
                records.append({"title": p["title"], "venue": venue, "year": int(p["year"]), "doi": p.get("doi", ""),
                    "authors": [{"name": a.get("text", "") if isinstance(a, dict) else a, "pid": a.get("@pid", "") if isinstance(a, dict) else ""} for a in authors],
                    "dblp_key": p.get("key", ""), "dblp_url": p.get("url", ""),
                    "record_type": "inproceedings" if p.get("type") == "Conference and Workshop Papers" else "article" if p.get("type") == "Journal Articles" else "proceedings",
                    "source_toc_key": toc, "source_cache": info["cache_file"]})
            attempts.append({"venue": venue, "year": 2026, "url": url, "status": "fetched", "reported_total": int(response.get("@total", 0)), "returned": len(hits), **info})
        except Exception as exc:
            attempts.append({"venue": venue, "year": 2026, "url": url, "status": "fetch_or_parse_error", "detail": str(exc)})
        print(f"Recent catalog {venue}: {attempts[-1]['status']}", flush=True)
    save(ROOT / "data/recent_catalog.json", {"papers": records, "attempts": attempts})


def pub_type(p):
    title = p["title"].casefold()
    if "editorial" in title or p.get("record_type") == "proceedings":
        return "non_paper_record"
    if re.match(r"poster\s*:", title) or "poster" in p.get("source_toc_key", "").lower():
        return "poster"
    if re.match(r"demo\s*:", title):
        return "demo"
    if p["venue"] == "PACMNET":
        return "journal_paper"
    return "conference_paper" if p["venue"] != "HotNets" else "workshop_paper"


def author_agreement(expected, observed):
    return bool(expected) and [author_key(a["name"]) for a in expected] == [author_key(a["name"]) for a in observed]


def build():
    local = WORKSPACE / "projects/networking-to-ai-migration/data"
    catalog = json.loads((local / "topnet_venue_year_papers.json").read_text())["papers"]
    catalog += json.loads((local / "pacmnet_toc_papers.json").read_text())["papers"]
    recent = ROOT / "data/recent_catalog.json"
    if recent.exists():
        catalog += json.loads(recent.read_text())["papers"]
    blocks, logs = load_sources()
    overrides = json.loads((ROOT / "data/overrides.json").read_text())
    known = [{**p, **overrides.get(p["paper_id"], {})} for p in json.loads((ROOT / "data/publications.json").read_text())["publications"]]
    pdfs = json.loads((ROOT / "data/independent_pdf_audit.json").read_text())["checks"]
    extra_pdfs = ROOT / "data/ledger_pdf_audit.json"
    if extra_pdfs.exists():
        pdfs += json.loads(extra_pdfs.read_text())["checks"]
    pdf_by_url = {p["url"]: p for p in pdfs if p["status"] == "first_two_pages_checked"}
    groups = {}
    excluded = []
    for p in catalog:
        venue = "CoNEXT" if p["venue"] == "PACMNET" else p["venue"]
        if venue not in VENUES or not 2019 <= p["year"] <= 2026:
            continue
        kind = pub_type(p)
        if kind == "non_paper_record":
            excluded.append({"venue": venue, "year": p["year"], "title": p["title"], "reason": "proceedings_volume_or_editorial", "dblp_url": p.get("dblp_url", "")})
            continue
        ident = (venue, p["year"], key(p["title"]))
        groups.setdefault(ident, {"catalog": [], "primary": [], "known": []})["catalog"].append({**p, "publication_type": kind})
    for cell, entries in blocks.items():
        for p in entries:
            ident = (*cell, p["title_key"])
            # Reviewable title variants require full ordered author agreement or DOI.
            if ident not in groups:
                matches = []
                for candidate_id, candidate in groups.items():
                    if candidate_id[:2] != cell:
                        continue
                    for original in candidate["catalog"]:
                        same_doi = bool(p["doi"]) and p["doi"].casefold() == original.get("doi", "").casefold()
                        same_authors = author_agreement(original.get("authors", []), p["authors"])
                        similarity = difflib.SequenceMatcher(None, p["title_key"], candidate_id[2]).ratio()
                        prefix = min(len(p["title_key"]), len(candidate_id[2])) > 30 and (p["title_key"].startswith(candidate_id[2]) or candidate_id[2].startswith(p["title_key"]))
                        reviewed_flexwan = (cell == ("SIGCOMM", 2023) and same_authors
                            and p["title"].startswith("FlexWAN: Software Hardware Co-design for Flexible and Cost-Effective")
                            and original["title"].startswith("FlexWAN: Software Hardware Co-design for Cost-Effective and Resilient"))
                        if same_doi or reviewed_flexwan or same_authors and (similarity >= 0.86 or prefix):
                            matches.append((candidate_id, "doi" if same_doi else "title_variant_complete_author_agreement"))
                if len(set(c[0] for c in matches)) == 1:
                    ident, p["title_match_method"] = matches[0]
            groups.setdefault(ident, {"catalog": [], "primary": [], "known": []})["primary"].append(p)
    for p in known:
        ident = (p["venue"], p["year"], key(p["title"]))
        groups.setdefault(ident, {"catalog": [], "primary": [], "known": []})["known"].append(p)
    rows = []
    for (venue, year, title_key), group in sorted(groups.items()):
        bibliography, primary, included = group["catalog"], group["primary"], group["known"]
        main = included[0] if included else bibliography[0] if bibliography else primary[0]
        expected = main.get("authors", [])
        title = main["title"]
        kind = main.get("publication_type") or next((p["source_publication_type"] for p in primary if p["source_publication_type"]), "conference_paper" if year == 2026 and venue != "HotNets" else "workshop_paper" if venue == "HotNets" else "unclassified_primary_listing_record")
        # Explicit non-paper agenda items remain in diagnostics, never in denominators.
        agenda = re.search(r"^(keynote|panel|session|welcome|closing|lightning|best of ccr|introduction|opening remarks|student talk|noon|drink and snack|\(?[0-9]+:[0-9]+)", title, re.I) or any(re.match(r"^(Keynote Speaker|Panelists:|Participants:|Location:)", p["author_line"], re.I) for p in primary)
        if not bibliography and not included and agenda:
            excluded.append({"venue": venue, "year": year, "title": title, "reason": "agenda_item_not_research_paper"})
            continue
        verified_lines = [p for p in primary if bibliography and author_agreement(expected, p["authors"]) and all(a.get("affiliations_raw") for a in p["authors"])]
        program_only_lines = [p for p in primary if not bibliography and p["authors"] and all(a.get("affiliations_raw") for a in p["authors"])
                              and key("; ".join(a["name"] for a in p["authors"]))]
        if not expected:
            candidates = [p for p in primary if p["authors"] and all(a.get("affiliations_raw") for a in p["authors"])]
            if candidates:
                expected = max(candidates, key=lambda p: len(p["authors"]))["authors"]
            # Program-only author lists have no independent bibliographic corroboration.
        positive = [p for p in primary if TENCENT.search(p["author_line"])]
        row_id = "ledger-" + hashlib.sha256(f"{venue}|{year}|{title_key}".encode()).hexdigest()[:20]
        urls = {u for p in primary for u in p["pdf_urls"]}
        urls.update(p["url"] for p in pdfs if p.get("ledger_id") == row_id)
        if included:
            urls.update(p["pdf_url"] for p in included if p.get("pdf_url"))
        checked = [pdf_by_url[u] for u in sorted(urls) if u in pdf_by_url]
        matched_pdf = []
        for p in checked:
            content = (ROOT / p["text_cache"]).read_text(errors="replace")
            if title_key in key(content[:10000]):
                matched_pdf.append(p)
        decision, level, reason = "unresolved", "none", "Publication affiliation evidence not yet sufficient."
        evidence_urls, evidence_caches = [], []
        if included:
            decision = "tencent_coauthorship_confirmed" if main.get("affiliation_status") == "pdf_verified" else "tencent_coauthorship_supported"
            level = "reviewed_pdf" if decision.endswith("confirmed") else "reviewed_publisher_deposit_pdf_pending" if main.get("affiliation_status") == "publisher_deposit_verified" else "existing_program_or_index_evidence_pdf_pending"
            reason = main["inclusion_reason"]
            evidence_urls = [main["affiliation_source"]]
            evidence_caches = [main.get("affiliation_metadata_cache", main["source_cache"]) if main.get("affiliation_status") == "publisher_deposit_verified" else main.get("affiliation_pdf_cache", main["source_cache"])]
        elif positive:
            reason = "Tencent appears in the extracted author line; manual inclusion and author mapping review required."
            level = "new_tencent_author_line_lead"
            evidence_urls = [p["url"] for p in positive]
            evidence_caches = [p["cache_file"] for p in positive]
        elif verified_lines:
            decision = "no_tencent_in_complete_program_affiliations"
            level = "complete_author_order_matched_program"
            reason = "All ordered authors agree with independent bibliography and have program affiliation assignments; none lists Tencent. Final-PDF/current-address review still pending."
            evidence_urls = [p["url"] for p in verified_lines]
            evidence_caches = [p["cache_file"] for p in verified_lines]
        elif program_only_lines:
            decision = "no_tencent_in_program_only_affiliations"
            level = "parsed_program_assignments_without_independent_author_check"
            reason = "No Tencent in parsed program author affiliations, but independent author-list and final-PDF verification are still missing."
            evidence_urls = [p["url"] for p in program_only_lines]
            evidence_caches = [p["cache_file"] for p in program_only_lines]
        # PDF-negative evidence is stronger only after title AND all author names match.
        for p in matched_pdf:
            content = (ROOT / p["text_cache"]).read_text(errors="replace")
            if expected and all(author_key(a["name"]) in key(content[:14000]) for a in expected) and not TENCENT.search(content):
                if not included and not positive:
                    decision, level = "no_tencent_in_matched_pdf_screen", "title_and_all_author_names_matched_pdf"
                    reason = "Title and every bibliographic author name matched the first two PDF pages; no explicit Tencent string there. This is screened absence, not manually verified exhaustive affiliation absence."
                    evidence_urls, evidence_caches = [p["url"]], [p["cache_file"]]
        row = {"ledger_id": row_id, "venue": venue, "year": year, "title": title,
            "publication_type": kind, "doi": main.get("doi", "") or next((p["doi"] for p in primary if p["doi"]), ""),
            "authors_ordered": "; ".join(a["name"] for a in expected), "author_count": len(expected),
            "decision": decision, "evidence_level": level, "reason": reason,
            "project_paper_id": main.get("paper_id", "") if included else "",
            "scope_status": main.get("scope_status", "not_reviewed") if included else "not_reviewed",
            "in_independent_catalog": bool(bibliography), "in_primary_listing": bool(primary),
            "catalog_source_venues": "; ".join(sorted({p["venue"] for p in bibliography})),
            "catalog_urls": "; ".join(sorted({p.get("dblp_url", "") for p in bibliography} - {""})),
            "primary_source_urls": "; ".join(sorted({p["url"] for p in primary})),
            "evidence_urls": "; ".join(dict.fromkeys(evidence_urls)), "evidence_caches": "; ".join(dict.fromkeys(evidence_caches)),
            "pdf_urls": "; ".join(sorted(urls)), "matched_pdf_count": len(matched_pdf),
            "paper_urls": "; ".join(sorted({p["paper_url"] for p in primary if p.get("paper_url")})),
            "program_author_list_match": bool(verified_lines),
            "title_variant_review_required": any(p.get("title_match_method") == "title_variant_complete_author_agreement" for p in primary),
            "needs_manual_review": decision == "unresolved" or decision == "no_tencent_in_matched_pdf_screen" or level != "reviewed_pdf",
            "year_status": "year_to_date" if year == 2026 else "historical",
            "author_line_evidence": " || ".join(dict.fromkeys(p["author_line"] for p in primary))[:28000]}
        rows.append(row)
    cells = []
    for venue in VENUES:
        for year in range(2019, 2027):
            records = [p for p in rows if (p["venue"], p["year"]) == (venue, year)]
            counts = Counter(p["decision"] for p in records)
            cells.append({"venue": venue, "year": year, "inventory_records": len(records),
                "primary_venue_records": sum(p["publication_type"] in {"conference_paper", "workshop_paper", "journal_paper"} for p in records),
                "poster_demo_records": sum(p["publication_type"] in {"poster", "demo"} for p in records),
                "publication_type_unresolved": sum(p["publication_type"] == "unclassified_primary_listing_record" for p in records),
                "catalog_records": sum(p["in_independent_catalog"] for p in records),
                "primary_listing_records": sum(p["in_primary_listing"] for p in records),
                "catalog_only_records": sum(p["in_independent_catalog"] and not p["in_primary_listing"] for p in records),
                "primary_only_records": sum(p["in_primary_listing"] and not p["in_independent_catalog"] for p in records),
                "tencent_confirmed_pdf": counts["tencent_coauthorship_confirmed"],
                "tencent_supported_pdf_pending": counts["tencent_coauthorship_supported"],
                "no_tencent_program_supported": counts["no_tencent_in_complete_program_affiliations"],
                "no_tencent_program_only": counts["no_tencent_in_program_only_affiliations"],
                "no_tencent_pdf_screened": counts["no_tencent_in_matched_pdf_screen"], "unresolved": counts["unresolved"],
                "new_tencent_author_line_leads": sum(p["evidence_level"] == "new_tencent_author_line_lead" for p in records),
                "needs_manual_review": sum(p["needs_manual_review"] for p in records),
                "inventory_reconciliation": "open_discrepancies" if any(p["in_independent_catalog"] != p["in_primary_listing"] for p in records) else "title_sets_agree" if records else "sources_unavailable",
                "affiliation_completeness": "not_established", "year_status": "year_to_date" if year == 2026 else "historical",
                "completion_blocker": "Reconcile catalog-only/program-only records and publication types; resolve affiliations; audit PDF/current-address discrepancies. Screened negative decisions are not manual certification."})
    now = datetime.now(timezone.utc).isoformat()
    save(ROOT / "data/proceedings_ledger.json", {"generated_at": now, "scope": "2019-2026 five venues; all publication types retained separately", "publications": rows})
    save(ROOT / "data/completeness_dashboard.json", {"generated_at": now, "venue_years": cells,
        "decision_counts": dict(Counter(p["decision"] for p in rows)), "source_parse_logs": logs,
        "excluded_non_paper_records": excluded,
        "completion_rule": "Never certify completeness from a negative string search. Each cell needs reconciled inventories and individually supported publication-time affiliation decisions; 2026 remains a dated cutoff."})
    print(json.dumps({"inventory_records": len(rows), "venue_year_cells": len(cells), "decision_counts": dict(Counter(p["decision"] for p in rows)),
        "new_tencent_leads": [{k:p[k] for k in ["venue", "year", "title", "author_line_evidence"]} for p in rows if p["evidence_level"] == "new_tencent_author_line_lead"],
        "by_venue": {v: dict(Counter(p["decision"] for p in rows if p["venue"] == v)) for v in VENUES}}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--refresh-recent-catalog", action="store_true")
    args = parser.parse_args()
    if args.refresh_recent_catalog:
        refresh_recent_catalog()
    build()
