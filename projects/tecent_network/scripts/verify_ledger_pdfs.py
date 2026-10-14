#!/usr/bin/env python3
"""Resolve public NSDI PDFs for unresolved ledger entries and the Tencent corpus."""
import json
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from audit_pdfs import check
from build_completeness import key
from collect import ROOT, fetch, save, text


def verify(p):
    for url in p["paper_urls"].split("; "):
        if not url:
            continue
        try:
            raw, cache = fetch(url)
            soup = BeautifulSoup(raw, "html.parser")
            headings = [key(text(h)) for h in soup.select("h1, h2")]
            if key(p["title"]) not in headings:
                raise ValueError("Paper-page title does not match ledger title")
            pdf = next((urljoin(url, a["href"]) for a in soup.select("a[href]") if "/system/files/" in a["href"] and ".pdf" in a["href"] and "slides" not in a["href"]), "")
            if not pdf:
                raise ValueError("No public paper PDF link found")
            result = check(pdf)
            return {**result, "ledger_id": p["ledger_id"], "venue": p["venue"], "year": p["year"], "title": p["title"],
                    "paper_page_url": url, "paper_page_cache": cache["cache_file"]}
        except Exception as exc:
            result = {"ledger_id": p["ledger_id"], "venue": p["venue"], "year": p["year"], "title": p["title"],
                      "url": url, "status": "paper_page_or_pdf_error", "detail": str(exc)}
    return result


def main():
    ledger = json.loads((ROOT / "data/proceedings_ledger.json").read_text())["publications"]
    targets = [p for p in ledger if p["venue"] == "NSDI" and p["paper_urls"] and (p["decision"] == "unresolved" or p["project_paper_id"])]
    previous = ROOT / "data/ledger_pdf_audit.json"
    checks = {p["ledger_id"]: p for p in json.loads(previous.read_text()).get("checks", [])} if previous.exists() else {}
    targets = [p for p in targets if p["ledger_id"] not in checks or checks[p["ledger_id"]]["status"] != "first_two_pages_checked"]
    with ThreadPoolExecutor(max_workers=4) as pool:
        for i, result in enumerate(pool.map(verify, targets), 1):
            checks[result["ledger_id"]] = result
            if result.get("tencent_occurrences") or result["status"] != "first_two_pages_checked":
                print(json.dumps({k:v for k,v in result.items() if k != "tencent_occurrences"}), flush=True)
            if i % 20 == 0:
                print(f"Ledger PDF verification: {i}/{len(targets)}", flush=True)
            save(previous, {"checks": list(checks.values())})


if __name__ == "__main__":
    main()
