#!/usr/bin/env python3
"""Compare independent bibliographic catalogs to actual recovered program text."""
import json
import html
import re
from collections import Counter

from bs4 import BeautifulSoup

from collect import ROOT, WORKSPACE, norm, save


def title_key(value):
    decoded = html.unescape(value)
    plain = BeautifulSoup(decoded, "html.parser").get_text(" ") if "<" in decoded else decoded
    return re.sub(r"[^\w]+", "", plain.casefold())


def main():
    discovery = json.loads((ROOT / "data/program_discovery.json").read_text())
    local = WORKSPACE / "projects/networking-to-ai-migration/data"
    catalog = json.loads((local / "topnet_venue_year_papers.json").read_text())["papers"]
    pacmnet = json.loads((local / "pacmnet_toc_papers.json").read_text())["papers"]
    pdfs = json.loads((ROOT / "data/independent_pdf_audit.json").read_text())["checks"]
    rows = []
    for venue in ["CoNEXT", "IMC", "HotNets"]:
        for year in range(2019, 2027):
            pages = [p for p in discovery["pages"] if (p["venue"], p["year"]) == (venue, year)
                     and len(p["body_text"]) > 1000 and "/partials/toc.html" not in p["url"]]
            bibliography = [p for p in catalog if p["venue"] == venue and p["year"] == year and p.get("year_matches_expected", True) and p.get("record_type") == "inproceedings"]
            if venue == "CoNEXT":
                bibliography += [p for p in pacmnet if p["year"] == year and "editorial" not in p["title"].lower()]
            by_title = {title_key(p["title"]): p for p in bibliography}
            content = title_key(" ".join(p["body_text"] for p in pages))
            matched = [p for title, p in by_title.items() if title in content]
            missing = [p for title, p in by_title.items() if title not in content]
            paper_checks = [p for p in pdfs if p["status"] == "first_two_pages_checked" and f"/{venue.lower() if venue != 'CoNEXT' else 'co-next'}/{year}/" in p["url"] and "/papers/" in p["url"]]
            rows.append({"venue": venue, "year": year, "program_pages_with_content": len(pages),
                         "independent_catalog_records": len(by_title), "catalog_titles_found_in_program_text": len(matched),
                         "catalog_titles_not_matched": len(missing), "paper_pdf_headers_checked": len(paper_checks),
                         "pdf_header_tencent_hits": sum(bool(p["tencent_occurrences"]) for p in paper_checks),
                         "source_urls": "; ".join(p["url"] for p in pages), "completeness": "not_established",
                         "note": "Title-text overlap is diagnostic, not a guarantee of author/affiliation completeness. Catalog may include posters. PACMNET journal titles are included under CoNEXT; 2026 catalog is incomplete.",
                         "unmatched_titles": "; ".join(p["title"] for p in missing)})
    index = json.loads((ROOT / "data/independent_openalex.json").read_text())
    save(ROOT / "data/audit_summary.json", {"venue_year_checks": rows,
         "pdf_status_counts": dict(Counter(p["status"] for p in pdfs)),
         "institution_index_works_seen": index["works_seen"], "institution_index_catalog_matches": len(index["five_venue_matches"]),
         "limitation": "Do not interpret unindexed works or missing affiliations as proof of absence. PDF checks use first two pages only; non-paper PDFs are not included in venue paper-header counts."})
    print("\n".join(str((r["venue"],r["year"],r["independent_catalog_records"],r["catalog_titles_found_in_program_text"],r["paper_pdf_headers_checked"])) for r in rows))


if __name__ == "__main__":
    main()
