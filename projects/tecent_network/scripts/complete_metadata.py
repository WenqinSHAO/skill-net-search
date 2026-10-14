#!/usr/bin/env python3
"""Cross-check user-reviewed papers against primary publisher deposits.

Raw evidence is cached. This never infers affiliations from current employment.
PDF mappings are applied only from separately reviewed metadata overrides.
"""
from __future__ import annotations

import json
import re
import time
import subprocess
import unicodedata
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from urllib.parse import quote

from bs4 import BeautifulSoup

from collect import ROOT, fetch, save, text, parse_sigcomm
from build_completeness import author_key, key


def pdf_fields(check):
    raw = subprocess.run(["pdftotext", "-f", "1", "-l", "2", "-raw", str(ROOT / check["cache_file"]), "-"],
                         check=True, capture_output=True, text=True).stdout
    raw = unicodedata.normalize("NFKC", raw)
    # PDF line-end word hyphenation is removed; semantic hyphens remain.
    raw = re.sub(r"(?<=\w)-\n(?=\w)", "", raw)
    for old, new in {"costeffective": "cost-effective", "kernelmodification-free": "kernel-modification-free",
                     "longtail": "long-tail", "newflow": "new-flow"}.items():
        raw = raw.replace(old, new)
    abstract = re.search(r"(?:^|\n)ABSTRACT\s*\n(.*?)(?:\nCCS CONCEPTS|\nKeywords|\nKEYWORDS)", raw, re.S | re.I)
    keywords = re.search(r"(?:^|\n)KEYWORDS\s*\n(.*?)(?:\nACM Reference Format|\nPermission to|\n©|\n1\s+INTRODUCTION|\n[§†∗*])", raw, re.S | re.I)
    return {"abstract": re.sub(r"\s+", " ", abstract[1]).strip() if abstract else "",
            "keywords": [x.strip(" .") for x in re.split(r";|,", re.sub(r"\s+", " ", keywords[1])) if x.strip(" .")] if keywords else []}


def user_list(papers):
    content = (ROOT / "COLLECTION_PLAN.md").read_text().split("## Offical Programm or paper links", 1)[1]
    venue, year, url = "", 0, ""
    rows = []
    alias = {key("FlexWAN: Software Hardware Co-design for Flexible and Cost-Effective Optical Backbones"):
             key("FlexWAN: Software Hardware Co-design for Cost-Effective and Resilient Optical Backbones")}
    for line in content.splitlines():
        if line.startswith("### "):
            venue = line[4:].strip()
        match = re.match(r"- (\d{4}): (https?://\S+)", line)
        if match:
            year, url = int(match[1]), match[2]
        elif line.startswith("  - "):
            title = line[4:].strip()
            if title == "NA":
                rows.append({"venue": venue, "year": year, "user_title": title, "official_url": url,
                             "status": "user_observed_no_primary_paper_not_certified_absence", "paper_id": ""})
                continue
            canonical = alias.get(key(title), key(title))
            matches = [p for p in papers if p["venue"] == venue and p["year"] == year and key(p["title"]) == canonical]
            rows.append({"venue": venue, "year": year, "user_title": title, "official_url": url,
                         "status": "matched_title_variant" if key(title) in alias and len(matches) == 1 else "matched" if len(matches) == 1 else "unmatched_or_ambiguous",
                         "paper_id": matches[0]["paper_id"] if len(matches) == 1 else ""})
    return rows


def deposit(p):
    if not p.get("doi"):
        return p["paper_id"], {"status": "doi_not_assigned_or_not_collected"}
    url = "https://api.crossref.org/works/" + quote(p["doi"], safe="")
    try:
        for attempt in range(3):
            try:
                raw, info = fetch(url)
                break
            except Exception as exc:
                if "429" not in str(exc) or attempt == 2:
                    raise
                time.sleep(5 * (attempt + 1))
        message = json.loads(raw)["message"]
        if key(message["title"][0]) != key(p["title"]):
            raise ValueError("Publisher-deposited title does not match")
        authors = [{"name": " ".join(filter(None, [a.get("given", ""), a.get("family", "")])),
                    "affiliations_raw": [v["name"] for v in a.get("affiliation", [])],
                    "orcid": a.get("ORCID", "").replace("http://orcid.org/", "https://orcid.org/")}
                   for a in message.get("author", [])]
        return p["paper_id"], {"status": "title_matched", "url": url, **info,
            "title": message["title"][0], "authors": authors,
            "abstract": text(BeautifulSoup(message.get("abstract", ""), "html.parser")),
            "publisher": message.get("publisher", ""), "pages": message.get("page", ""),
            "published_date": "-".join(str(x).zfill(2) if i else str(x) for i, x in enumerate(message.get("published", {}).get("date-parts", [[]])[0])),
            "license_urls": sorted({x["URL"] for x in message.get("license", []) if x.get("URL")}),
            "resource_urls": sorted({x["URL"] for x in message.get("link", []) if x.get("URL")})}
    except Exception as exc:
        return p["paper_id"], {"status": "error", "url": url, "detail": str(exc)}


def main():
    path = ROOT / "data/publications.json"
    data = json.loads(path.read_text())
    papers = data["publications"]
    checks = user_list(papers)
    if any(r["status"] == "unmatched_or_ambiguous" for r in checks):
        raise ValueError("User paper list does not reconcile; resolve before enrichment")
    primary_ids = {r["paper_id"] for r in checks if r["paper_id"]}
    with ThreadPoolExecutor(max_workers=1) as pool:
        deposits = dict(pool.map(deposit, papers))
    reviews_path = ROOT / "data/metadata_reviews.json"
    reviews = json.loads(reviews_path.read_text()) if reviews_path.exists() else {}
    decisions = json.loads((ROOT / "data/metadata_review_decisions.json").read_text())
    pdf_checks = []
    for audit in ["ledger_pdf_audit.json", "independent_pdf_audit.json", "metadata_pdf_checks.json"]:
        pdf_checks += json.loads((ROOT / "data" / audit).read_text())["checks"]
    pdf_by_url = {x["url"]: x for x in pdf_checks if x["status"] == "first_two_pages_checked"}
    pdf_sources = json.loads((ROOT / "data/metadata_pdf_sources.json").read_text())
    audits = []
    for p in papers:
        d = deposits[p["paper_id"]]
        before = [a["name"] for a in p["authors"]]
        p.setdefault("dblp_author_list_check", p.get("author_list_check", "not_checked"))
        p.setdefault("program_authors", json.loads(json.dumps(p["authors"])))
        p.setdefault("program_affiliation_source", p["affiliation_source"])
        p.setdefault("program_affiliation_cache", p["source_cache"])
        if d["status"] == "title_matched":
            p.update(publisher=d["publisher"], pages=d["pages"], published_date=d["published_date"],
                     publisher_metadata_source=d["url"], publisher_metadata_cache=d["cache_file"],
                     license_urls=d["license_urls"])
            if d["abstract"]:
                p.update(abstract=d["abstract"], abstract_source=d["url"], abstract_source_cache=d["cache_file"],
                         abstract_status="complete_publisher_deposit")
            # IDs only transferred after full ordered-author agreement.
            agrees = [author_key(a["name"]) for a in d["authors"]] == [author_key(a["name"]) for a in p["authors"]]
            if agrees:
                for a, deposited in zip(p["authors"], d["authors"]):
                    a["publisher_affiliations_raw"] = deposited["affiliations_raw"]
                    if deposited["orcid"]:
                        a.update(orcid=deposited["orcid"], orcid_source=d["url"], orcid_source_cache=d["cache_file"])
                p["publisher_author_list_check"] = "exact_order_match"
                p["author_list_check"] = "exact_order_match"
                p["author_list_check_source"] = d["url"]
            else:
                p["publisher_author_list_check"] = "mismatch_review_required"
        if p["paper_id"] in pdf_sources:
            p["pdf_url"] = pdf_sources[p["paper_id"]]
        if p["paper_id"] in decisions["reviewed_pdf_paper_ids"]:
            check = pdf_by_url[p["pdf_url"]]
            p.update(affiliation_status="pdf_verified", affiliation_source=p["pdf_url"],
                     affiliation_pdf_cache=check["cache_file"],
                     author_header_review="reviewed_complete_order_and_affiliation_markers")
            if p["venue"] == "SIGCOMM":
                fields = pdf_fields(check)
                if fields["abstract"] and "\ufffd" not in fields["abstract"]:
                    p.update(abstract=fields["abstract"], abstract_source=p["pdf_url"],
                             abstract_source_cache=check["cache_file"], abstract_status="complete_reviewed_pdf_abstract")
                if fields["keywords"] and not any("\ufffd" in x for x in fields["keywords"]):
                    p.update(author_keywords=fields["keywords"], keyword_source=p["pdf_url"], keyword_source_cache=check["cache_file"])
        elif p["paper_id"] in decisions["reviewed_publisher_paper_ids"]:
            if d["status"] != "title_matched" or p.get("publisher_author_list_check") != "exact_order_match" or not all(a["affiliations_raw"] for a in d["authors"]):
                raise ValueError("Reviewed publisher mapping is no longer corroborated: " + p["title"])
            for a, deposited in zip(p["authors"], d["authors"]):
                a["affiliations_raw"] = deposited["affiliations_raw"]
            p.update(affiliation_status="publisher_deposit_verified", affiliation_source=d["url"],
                     affiliation_metadata_cache=d["cache_file"],
                     author_header_review="reviewed_publisher_complete_order_and_affiliation_assignments")
        if p["venue"] == "NSDI":
            soup = BeautifulSoup((ROOT / p["paper_page_cache"]).read_text(), "html.parser")
            abstract_node = soup.select_one(".field-name-field-paper-description")
            if abstract_node and key(text(abstract_node)) == key(p["abstract"]):
                p.update(abstract=text(abstract_node), abstract_source=p["url"],
                         abstract_source_cache=p["paper_page_cache"], abstract_status="complete_official_paper_page")
            # Primary BibTeX supplies pagination, dates, publisher and ISBN without inventing DOIs.
            bibtex = soup.select_one("#bibtex")
            bib = text(bibtex) if bibtex else soup.get_text(" ")
            pages = re.search(r"pages\s*=\s*\{([^}]+)\}", bib)
            if pages:
                p["pages"] = pages[1].replace("--", "–")
            p["publisher"] = "USENIX Association"
            month = re.search(r"month\s*=\s*(?:\{)?([a-z]{3})", bib, re.I)
            if month:
                months = {m:i for i,m in enumerate(["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}
                if month[1].casefold() in months:
                    p["published_date"] = f'{p["year"]}-{months[month[1].casefold()]:02d}'
        if p["paper_id"] in decisions["notes_by_id"]:
            p["metadata_notes"] = decisions["notes_by_id"][p["paper_id"]]
        if p["paper_id"] == "tn-fcb9ef7a1565882f":
            p["authors"][-1]["name_as_in_pdf"] = "Juncheng Jiang"
        if p["venue"] == "SIGCOMM" and p.get("abstract_status") != "complete_reviewed_pdf_abstract" and p["publication_type"] == "conference_paper":
            found, _ = parse_sigcomm((ROOT / p["source_cache"]).read_text(), p["year"], p["url"],
                                     {"cache_file": p["source_cache"], "retrieved_at": p["retrieved_at"]})
            matched = [x for x in found if key(x["title"]) == key(p["title"]) and x["abstract"]]
            if len(matched) == 1 and key(matched[0]["abstract"]) == key(p["abstract"]):
                p.update(abstract_status="complete_official_program_abstract", abstract_source_cache=p["source_cache"])
        if p["venue"] == "CoNEXT" and p["affiliation_status"] == "pdf_verified" and p.get("abstract"):
            p["abstract_status"] = "complete_reviewed_pdf_abstract"
            p["abstract_source_cache"] = pdf_by_url[p["pdf_url"]]["cache_file"]
        if not p.get("pdf_url") and d.get("resource_urls"):
            p["pdf_url"] = next((u for u in d["resource_urls"] if "/doi/pdf/" in u), "")
        p["pdf_access_status"] = "public_pdf_cached" if p.get("pdf_url") in pdf_by_url else "publisher_pdf_link_not_retrieved" if p.get("pdf_url") else "not_found"
        if not p.get("author_keywords") and p["venue"] == "NSDI" and p["affiliation_status"] == "pdf_verified":
            p["keyword_status"] = "not_present_in_reviewed_front_matter"
        p["metadata_status"] = "required_metadata_complete" if (p.get("abstract_status", "").startswith("complete_")
            and p["affiliation_status"] in {"pdf_verified", "publisher_deposit_verified"}
            and p["author_header_review"].startswith("reviewed_")) else "review_pending_or_field_missing"
        review = reviews.get(p["paper_id"], {})
        if review:
            p.update(review)
        if p.get("abstract") and not p.get("abstract_status"):
            p["abstract_status"] = "available_primary_source_review_pending"
        p["user_reviewed_primary_set"] = p["paper_id"] in primary_ids
        p["metadata_checked_at"] = datetime.now(timezone.utc).isoformat()
        p["pages"] = re.sub(r"(?<=\d)-(?=\d)", "–", p.get("pages", ""))
        audits.append({"paper_id": p["paper_id"], "venue": p["venue"], "year": p["year"], "title": p["title"],
            "user_reviewed_primary_set": p["user_reviewed_primary_set"], "publisher_check_status": d["status"],
            "publisher_author_list_check": p.get("publisher_author_list_check", "not_available"),
            "authors_before": "; ".join(before), "authors_final": "; ".join(a["name"] for a in p["authors"]),
            "authors_publisher": "; ".join(a["name"] for a in d.get("authors", [])),
            "publisher_affiliations_raw": json.dumps(d.get("authors", []), ensure_ascii=False),
            "abstract_status": p.get("abstract_status", "missing"), "abstract_characters": len(p.get("abstract", "")),
            "abstract_source": p.get("abstract_source", ""), "affiliation_status": p["affiliation_status"],
            "author_header_review": p.get("author_header_review", "pending"),
            "metadata_notes": p.get("metadata_notes", ""), "source_url": d.get("url", ""),
            "source_cache": d.get("cache_file", ""), "checked_at": p["metadata_checked_at"]})
    save(path, data)
    save(ROOT / "data/user_program_check.json", {"checks": checks})
    save(ROOT / "data/metadata_audit.json", {"checks": audits, "publisher_deposits": deposits})
    print(json.dumps({"records": len(papers), "user_primary_records": len(primary_ids),
        "abstracts": sum(bool(p.get("abstract")) for p in papers),
        "publisher_author_list_checks": {s: sum(p.get("publisher_author_list_check", "not_available") == s for p in papers) for s in ["exact_order_match", "mismatch_review_required", "not_available"]},
        "publisher_errors": [d for d in deposits.values() if d["status"] == "error"]}, indent=2))


if __name__ == "__main__":
    main()
