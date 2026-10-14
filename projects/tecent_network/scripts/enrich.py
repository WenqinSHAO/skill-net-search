#!/usr/bin/env python3
"""Fill PDF URLs and missing abstracts from title-matched primary metadata."""
import json
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import quote, urljoin

from bs4 import BeautifulSoup

from collect import ROOT, fetch, norm, save, text


def enrich(p):
    p = dict(p)
    log = {"paper_id": p["paper_id"], "status": "not_needed"}
    url = p["url"] if p["venue"] == "NSDI" else "https://api.crossref.org/works/" + quote(p["doi"], safe="") if p.get("doi") and not p.get("abstract") else ""
    if not url:
        return p, log
    log["url"] = url
    try:
        raw, info = fetch(url)
        if p["venue"] == "NSDI":
            soup = BeautifulSoup(raw, "html.parser")
            if not any(norm(text(h)) == norm(p["title"]) for h in soup.select("h1, h2")):
                raise ValueError("Paper page title did not match")
            pdf = next((urljoin(url, a["href"]) for a in soup.select("a[href]") if "/system/files/" in a["href"] and a["href"].endswith(".pdf") and "slides" not in a["href"]), "")
            if pdf:
                p["pdf_url"] = pdf
                p["pdf_source"] = url
                p["pdf_source_cache"] = info["cache_file"]
            p["paper_page_cache"] = info["cache_file"]
        else:
            message = json.loads(raw)["message"]
            if not message.get("title") or norm(message["title"][0]) != norm(p["title"]):
                raise ValueError("Crossref title did not match")
            if message.get("abstract"):
                p["abstract"] = text(BeautifulSoup(message["abstract"], "html.parser"))
                p["abstract_source"] = url
                p["abstract_source_cache"] = info["cache_file"]
            p["crossref_source_cache"] = info["cache_file"]
        log["status"] = "title_matched"
        log["source_cache"] = info["cache_file"]
    except Exception as exc:
        log.update(status="error", detail=f"{type(exc).__name__}: {exc}")
    return p, log


def main():
    path = ROOT / "data/publications.json"
    data = json.loads(path.read_text())
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(enrich, data["publications"]))
    data["publications"] = [p for p, log in results]
    save(path, data)
    save(ROOT / "data/enrichment.json", {"attempts": [log for p, log in results]})
    print(json.dumps({"records": len(results), "pdf_urls": sum(bool(p.get("pdf_url")) for p, log in results),
                      "abstracts": sum(bool(p.get("abstract")) for p, log in results),
                      "errors": [log for p, log in results if log["status"] == "error"]}, indent=2))


if __name__ == "__main__":
    main()
