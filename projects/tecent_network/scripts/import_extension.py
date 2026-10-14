#!/usr/bin/env python3
"""Import the explicitly reviewed expansion evidence without replacing old records."""
import json
import re
from collections import Counter

from bs4 import BeautifulSoup

from collect import ROOT, enrich_local, fetch, parenthetical_authors, record, save, text


def main():
    discovery = json.loads((ROOT / "data/program_discovery.json").read_text())
    page = next(p for p in discovery["pages"] if p["venue"] == "CoNEXT" and p["year"] == 2021 and p["tencent_contexts"])
    soup = BeautifulSoup((ROOT / page["cache_file"]).read_text(), "html.parser")
    node = soup.find(string=lambda s: s and "Discovering Obscure" in s)
    block = node.find_parent("li")
    people = block.select_one(".col-md-7 > div:nth-of-type(2)")
    title = re.sub(r"\s+long$", "", text(block.select_one("strong")))
    abstract = re.sub(r"^Abstract:\s*", "", text(block.select_one(".collapse")))
    conext = record(title, people, parenthetical_authors(text(people)), abstract, "CoNEXT", 2021,
                    page["url"], page, "10.1145/3485983.3494857", "https://jessiehuiwang.github.io/files/2021CoNEXT.pdf")
    # PDF page one was inspected: departmental detail is not retained in its header.
    for a in conext["authors"]:
        a["affiliations_raw"] = ["Tencent Technology" if a["name"] == "Zujiang Pan" else "CETC" if a["name"] == "Zhiyong Zhang" else "Tsinghua University"]
    conext.update(scope_status="included", affiliation_status="pdf_verified", affiliation_source=conext["pdf_url"],
                  affiliation_pdf_cache="raw/87dd5e9198c2a2bedf59.pdf", author_keywords=["Looking Glass", "Internet Measurement", "Focused Crawler"],
                  analyst_tags=["measurement_reliability", "routing_control"], tag_status="analyst_review_primary_program",
                  inclusion_reason="Official CoNEXT program and author-hosted PDF both explicitly identify Tencent coauthor Zujiang Pan.")
    url = "https://conferences.sigcomm.org/sigcomm/2019/cf-posters.html"
    html, cache = fetch(url)
    soup = BeautifulSoup(html, "html.parser")
    block = soup.find(string=lambda s: s and "Network-Aware and Unsupervised Diagnostics" in s).find_parent("td")
    title = re.sub(r"^#\d+\s+", "", text(block.select_one(".paper-header")))
    people = block.find_all("p")[-1]
    poster = record(title, people, parenthetical_authors(text(people)), "", "SIGCOMM", 2019, url, cache, "10.1145/3342280.3342320")
    poster.update(publication_type="poster", scope_status="included", analyst_tags=["measurement_reliability"],
                  tag_status="analyst_review_primary_program", inclusion_reason="Official SIGCOMM poster listing identifies both authors as Tencent; not a main-track paper.")
    url = "https://api.openalex.org/works/https://doi.org/10.1145/3603269.3610841"
    html, cache = fetch(url)
    indexed = json.loads(html)
    authors = [{"name": a["raw_author_name"], "affiliations_raw": a["raw_affiliation_strings"]} for a in indexed["authorships"]]
    repo = "https://experts.umn.edu/en/publications/poster-too-accelerating-loss-recovery-by-taming-on-off-traffic-pa/"
    html, repo_cache = fetch(repo)
    soup = BeautifulSoup(html, "html.parser")
    abstract_node = soup.select_one(".textblock")
    too = record(indexed["title"], None, authors, text(abstract_node), "SIGCOMM", 2023, repo, cache, "10.1145/3603269.3610841")
    too.update(publication_type="poster", scope_status="included", affiliation_source=url,
               affiliation_status="independent_index_raw_affiliations_pdf_review_pending", author_line_raw="; ".join(a["name"] for a in authors),
               abstract_source=repo, author_keywords=["QUIC", "application limitation", "loss recovery"],
               analyst_tags=["transport_congestion", "edge_CDN_media"], tag_status="analyst_review_primary_program", review_source=repo,
               inclusion_reason="Independent index preserves three Tencent raw publication affiliations; university repository corroborates bibliography and abstract. Poster, not main-track paper.")
    added = [conext, poster, too]
    enrich_local(added)
    data = json.loads((ROOT / "data/publications.json").read_text())
    records = {p["paper_id"]: p for p in data["publications"]}
    records.update({p["paper_id"]: p for p in added})
    data["publications"] = sorted(records.values(), key=lambda p: (p["year"], p["venue"], p["title"]))
    save(ROOT / "data/publications.json", data)
    coverage = json.loads((ROOT / "data/coverage.json").read_text())
    coverage["pending_venues"] = [v for v in coverage["pending_venues"] if v not in {"CoNEXT/PACMNET", "IMC", "HotNets", "ICNP", "MobiCom", "MobiSys"}]
    coverage["excluded_venues"] = ["ICNP", "MobiCom", "MobiSys", "other mobile-centric conferences"]
    coverage["attempts"] = [a for a in coverage["attempts"] if a["venue"] not in {"CoNEXT", "IMC", "HotNets"}]
    for venue in ["CoNEXT", "IMC", "HotNets"]:
        for year in range(2019, 2027):
            pages = [p for p in discovery["pages"] if (p["venue"], p["year"]) == (venue, year) and len(p["body_text"]) > 1000]
            coverage["attempts"].append({"venue": venue, "year": year, "status": "program_discovery_scanned" if pages else "program_not_available",
                "url": "; ".join(p["url"] for p in pages), "tencent_records": sum(p["venue"] == venue and p["year"] == year for p in added),
                "completeness": "not_established", "note": "Independent institution-index and PDF-header checks recorded separately. Zero confirmed records is not proven zero output. 2026 is year-to-date."})
    save(ROOT / "data/coverage.json", coverage)
    print(Counter(p["venue"] for p in data["publications"]))


if __name__ == "__main__":
    main()
