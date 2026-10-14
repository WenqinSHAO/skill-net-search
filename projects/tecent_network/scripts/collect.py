#!/usr/bin/env python3
"""Cache official programs and collect Tencent author evidence; never infer employment."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parents[1]


def norm(value):
    return re.sub(r"[^\w]+", " ", value.casefold()).strip()


def text(node):
    return re.sub(r"\s+", " ", node.get_text(" ", strip=True)).strip() if node else ""


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    tmp.replace(path)


def fetch(url, refresh=False):
    key = hashlib.sha256(url.encode()).hexdigest()[:20]
    path = ROOT / "raw" / (key + ".html")
    meta = path.with_suffix(".json")
    if path.exists() and meta.exists() and not refresh:
        info = json.loads(meta.read_text())
        return path.read_text(), info
    response = requests.get(url, timeout=(10, 25), headers={"User-Agent": "Tencent-networking-survey/0.1"})
    response.raise_for_status()
    response.encoding = "utf-8"
    info = {"url": url, "final_url": response.url, "retrieved_at": datetime.now(timezone.utc).isoformat(),
            "cache_file": str(path.relative_to(ROOT)), "sha256": hashlib.sha256(response.content).hexdigest()}
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(response.text)
    save(meta, info)
    return response.text, info


def names(value):
    value = re.sub(r"\band\b|&", ",", value)
    return [n.strip(" ,;.*†‡0123456789") for n in value.split(",") if n.strip(" ,;.*†‡0123456789")]


def usenix_authors(node):
    copy = BeautifulSoup(str(node), "html.parser")
    for em in copy.find_all("em"):
        raw = text(em)
        em.replace_with(" [[" + raw.rstrip(";") + "]]" + (";" if raw.endswith(";") else ""))
    authors = []
    for group in text(copy).split(";"):
        affiliations = re.findall(r"\[\[(.*?)\]\]", group)
        author_text = group.split("[[", 1)[0]
        if not affiliations:
            continue
        for name in names(author_text):
            authors.append({"name": name, "affiliations_raw": affiliations})
    return authors


def parenthetical_authors(value):
    authors = []
    for match in re.finditer(r"([^()]*)\(([^()]*)\)", value):
        for name in names(match.group(1)):
            authors.append({"name": name, "affiliations_raw": [match.group(2).strip()]})
    return authors


def record(title, author_node, authors, abstract, venue, year, url, cache, doi="", pdf=""):
    title = re.sub(r"\s+(Research|Experience|Industrial) Track.*$", "", title).strip()
    key = f"{venue}|{year}|{norm(title)}"
    return {"paper_id": "tn-" + hashlib.sha256(key.encode()).hexdigest()[:16],
            "title": title, "venue": venue, "year": year, "publication_type": "conference_paper",
            "doi": doi, "url": url, "pdf_url": pdf, "abstract": abstract,
            "abstract_source": url if abstract else "", "author_keywords": [],
            "authors": authors, "author_line_raw": text(author_node),
            "affiliation_source": url, "affiliation_status": "program_parsed_pdf_review_pending",
            "scope_status": "included" if venue == "SIGCOMM" else "candidate",
            "inclusion_reason": "Official proceedings author line explicitly lists Tencent; " +
                ("networking venue" if venue == "SIGCOMM" else "networking relevance needs review"),
            "tencent_relationship": "coauthor", "version_group_id": "", "version_status": "not_reviewed",
            "source_cache": cache["cache_file"], "retrieved_at": cache["retrieved_at"]}


def parse_usenix(html, year, url, cache):
    soup = BeautifulSoup(html, "html.parser")
    blocks = soup.select(".node-paper")
    records = []
    for block in blocks:
        people = block.select_one(".field-name-field-paper-people-text")
        heading = block.select_one("h2 a, h3 a")
        if not people or not heading or not re.search(r"\btencent\b|腾讯", text(people), re.I):
            continue
        abstract = text(block.select_one(".field-name-field-paper-description-long"))
        records.append(record(text(heading), people, usenix_authors(people), abstract,
                              "NSDI", year, urljoin(url, heading.get("href", "")), cache))
    return records, len(blocks)


def parse_sigcomm(html, year, url, cache):
    soup = BeautifulSoup(html, "html.parser")
    records, seen = [], set()
    if soup.select("b.paper-title"):
        headings = soup.select("b.paper-title")
        for heading in headings:
            block = heading.find_parent("p")
            people = block.select_one(".table-description")
            if not people or not re.search(r"\btencent\b|腾讯", text(people), re.I):
                continue
            abstract_node = block.find_next_sibling()
            abstract = re.sub(r"^Abstract:\s*", "", text(abstract_node)) if abstract_node and "paper-abstract" in abstract_node.get("class", []) else ""
            doi_link = heading.get("data-pdf", "")
            doi = re.search(r"10\.\d{4,9}/[^?#\s]+", doi_link)
            records.append(record(text(heading), people, parenthetical_authors(text(people)), abstract,
                                  "SIGCOMM", year, url, cache, doi.group() if doi else ""))
        return records, len(headings)
    if soup.select("table.long_table_program .style_italic"):
        blocks = [tr for tr in soup.select("table.long_table_program tr") if tr.select_one("p.style_italic")]
        for block in blocks:
            heading = block.select_one(".text-color-primary")
            people = block.select_one("p.style_italic")
            if not heading or not re.search(r"\btencent\b|腾讯", text(people), re.I):
                continue
            following = block.find_next_sibling("tr")
            abstract = re.sub(r"^Abstract:\s*", "", text(following)) if following and "abstract-row" in following.get("class", []) else ""
            doi_link = next((a["href"] for a in block.select("a[href]") if "/10." in a["href"]), "")
            doi = re.search(r"10\.\d{4,9}/[^?#\s]+", doi_link)
            records.append(record(text(heading), people, parenthetical_authors(text(people)), abstract,
                                  "SIGCOMM", year, url, cache, doi.group() if doi else ""))
        return records, len(blocks)
    # Modern programs use collapse cards; older programs use a table cell per paper.
    blocks = soup.select("div.collapse")
    if not blocks:
        blocks = [td for td in soup.select("td") if td.select_one("h2, h3")]
    for block in blocks:
        heading = block.select_one(".collapse-title .font-semibold, h2, h3")
        if not heading:
            continue
        people = block.select_one(".collapse-title .font-normal")
        if people is None:
            people = next((p for p in block.select("p") if re.search(r"\btencent\b|腾讯", text(p), re.I)
                           and "(" in text(p) and not text(p).startswith("Abstract")), None)
        if not people or not re.search(r"\btencent\b|腾讯", text(people), re.I):
            continue
        title = text(heading)
        if title in seen:
            continue
        seen.add(title)
        abstract_node = block.select_one(".collapse-content")
        if abstract_node is None:
            abstract_node = next((p for p in block.select("p") if text(p).startswith("Abstract:")), None)
        abstract = re.sub(r"^Abstract:\s*", "", text(abstract_node))
        doi_link = next((a.get("href") for a in block.select("a[href]") if "/10." in a.get("href", "")), "")
        doi = re.search(r"10\.\d{4,9}/[^?#\s]+", doi_link)
        pdf = next((urljoin(url, a["href"]) for a in block.select("a[href]") if a["href"].endswith(".pdf")), "")
        records.append(record(title, people, parenthetical_authors(text(people)), abstract,
                              "SIGCOMM", year, url, cache, doi.group() if doi else "", pdf))
    return records, len(blocks)


def collect_year(task):
    venue, year, refresh = task
    if venue == "NSDI":
        urls = [f"https://www.usenix.org/conference/nsdi{year % 100:02d}/technical-sessions"]
        parser = parse_usenix
    else:
        base = f"https://conferences.sigcomm.org/sigcomm/{year}/"
        urls = [base + "program/", base + "program.html"] if year >= 2024 else [base + "program.html", base + "program/"]
        if year == 2025:
            urls.insert(0, base + "program/papers-info/")
        elif year >= 2026:
            urls.insert(0, base + "program/papers/")
        parser = parse_sigcomm
    coverage = []
    records = []
    for url in urls:
        entry = {"venue": venue, "year": year, "url": url, "status": "", "tencent_records": 0,
                 "completeness": "not_established", "note": "Program scan only; independent recall/PDF review required"}
        try:
            html, info = fetch(url, refresh)
            found, blocks = parser(html, year, url, info)
            records.extend(found)
            entry.update(status="parsed" if blocks else "unsupported_layout", paper_blocks=blocks,
                         tencent_records=len(found), retrieved_at=info["retrieved_at"], source_cache=info["cache_file"])
            if blocks:
                coverage.append(entry)
                break
        except Exception as exc:
            entry.update(status="fetch_error", note=f"{type(exc).__name__}: {exc}")
        coverage.append(entry)
    return records, coverage


def enrich_local(records):
    local = WORKSPACE / "projects/networking-to-ai-migration/data/topnet_venue_year_papers.json"
    bibliography = json.loads(local.read_text()).get("papers", []) if local.exists() else []
    by_title = {(p["venue"], p["year"], norm(p["title"])): p for p in bibliography}
    shared_path = WORKSPACE / "index/all_papers.json"
    shared = json.loads(shared_path.read_text()).get("papers", []) if shared_path.exists() else []
    for p in records:
        match = by_title.get((p["venue"], p["year"], norm(p["title"])))
        p["bibliography_match"] = "not_found"
        if match:
            p["bibliography_match"] = "exact_venue_year_title"
            p["dblp_key"], p["dblp_url"] = match.get("dblp_key", ""), match.get("dblp_url", "")
            p["doi"] = p["doi"] or match.get("doi", "")
            observed = [norm(a["name"]) for a in p["authors"]]
            expected = [norm(re.sub(r" \d{4}$", "", a["name"])) for a in match["authors"]]
            p["author_list_check"] = "exact_order_match" if observed == expected else "mismatch_review_required"
            p["dblp_authors"] = match["authors"]
            if observed == expected:
                for author, original in zip(p["authors"], match["authors"]):
                    author["dblp_pid"] = original.get("pid", "")
        else:
            p["author_list_check"] = "no_independent_check"
        existing = [s for s in shared if norm(s["title"]) == norm(p["title"])
                    and s.get("conference") == f'{p["venue"]} {p["year"]}']
        p["shared_paper_id"] = existing[0]["id"] if len(existing) == 1 else ""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start-year", type=int, default=2010)
    parser.add_argument("--end-year", type=int, default=datetime.now().year)
    parser.add_argument("--venues", nargs="+", choices=["NSDI", "SIGCOMM"], default=["NSDI", "SIGCOMM"])
    parser.add_argument("--refresh", action="store_true")
    args = parser.parse_args()
    if not 1998 <= args.start_year <= args.end_year <= datetime.now().year:
        parser.error("Use a year range within 1998 through the current year")
    path = ROOT / "data/publications.json"
    existing = json.loads(path.read_text()).get("publications", []) if path.exists() else []
    by_id = {p["paper_id"]: p for p in existing}
    coverage_path = ROOT / "data/coverage.json"
    coverage = json.loads(coverage_path.read_text()).get("attempts", []) if coverage_path.exists() else []
    attempts = {(e["venue"], e["year"], e["url"]): e for e in coverage}
    tasks = [(v, y, args.refresh) for v in args.venues for y in range(max(2004 if v == "NSDI" else 1998, args.start_year), args.end_year + 1)]
    with ThreadPoolExecutor(max_workers=4) as pool:
        for found, entries in pool.map(collect_year, tasks):
            for p in found:
                by_id[p["paper_id"]] = p
            for e in entries:
                attempts[(e["venue"], e["year"], e["url"])] = e
            save(path, {"collection_status": "initial_partial_program_sweep", "publications": sorted(by_id.values(), key=lambda p: (p["year"], p["venue"], p["title"]))})
            save(coverage_path, {"target_years": "1998-present", "completeness": "not_established", "attempts": list(attempts.values()),
                 "pending_venues": ["CoNEXT/PACMNET", "INFOCOM", "ToN", "IMC", "HotNets", "APNet", "MobiCom", "MobiSys", "ICNP", "ICCCN", "EuroSys", "ATC", "OSDI", "SOSP", "Security", "arXiv", "Chinese-language outlets"]})
            print(f'{entries[-1]["venue"]} {entries[-1]["year"]}: {len(found)} Tencent records ({entries[-1]["status"]})', flush=True)
    records = list(by_id.values())
    enrich_local(records)
    save(path, {"collection_status": "initial_partial_program_sweep", "publications": sorted(records, key=lambda p: (p["year"], p["venue"], p["title"]))})
    print(f"Collected {len(records)} records. Coverage is not established.")


if __name__ == "__main__":
    main()
