#!/usr/bin/env python3
"""Cache CoNEXT, IMC, and HotNets programs, retaining whole-page Tencent contexts."""
import json
import re
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

from collect import ROOT, fetch, save, text


def inspect(task):
    venue, year = task
    slug = "co-next" if venue == "CoNEXT" else venue.lower()
    base = f"https://conferences.sigcomm.org/{slug}/{year}/"
    pages, errors = [], []
    urls = [base]
    seen = set()
    while urls and len(seen) < 12:
        url = urls.pop(0)
        if url in seen:
            continue
        seen.add(url)
        try:
            html, info = fetch(url)
            soup = BeautifulSoup(html, "html.parser")
            if url == base:
                if venue == "CoNEXT":
                    for script in soup.select("script[src]"):
                        if "app.js" in script["src"]:
                            js, _ = fetch(urljoin(base, script["src"]))
                            for template in re.findall(r'templateUrl\s*:\s*[\"\x27]([^\"\x27]+)', js):
                                if any(word in template for word in ["accepted-papers", "partials/program.html", "partials/toc.html"]):
                                    urls.append(urljoin(base, template))
                for a in soup.select("a[href]"):
                    label = text(a).lower()
                    href = urljoin(url, a["href"])
                    if href.startswith(base) and any(w in label for w in ["program", "accepted paper", "technical session"]):
                        if not any(w in label for w in ["committee", "student", "workshop", "poster", "travel"]):
                            urls.append(href.split("#")[0])
                urls.extend([base + "program.html", base + "program/", base + "accepted-papers.html"])
            contexts = []
            for node in soup.find_all(string=lambda s: s and re.search(r"\btencent\b|腾讯", s, re.I)):
                parents = list(node.parents)
                contexts.append({"text": str(node).strip(), "parent_html": str(parents[min(2, len(parents) - 1)])[:15000],
                                 "ancestry": [{"tag": p.name, "class": p.get("class")} for p in parents[:5]]})
            link_base = base if "/partials/" in url else url
            pdfs = list(dict.fromkeys(urljoin(link_base, a["href"]) for a in soup.select("a[href]") if ".pdf" in a["href"].lower()))
            pages.append({**info, "venue": venue, "year": year, "title": text(soup.title),
                          "tencent_contexts": contexts, "pdf_urls": pdfs, "body_text": text(soup.body or soup)[:150000]})
        except Exception as exc:
            errors.append({"venue": venue, "year": year, "url": url, "status": "fetch_error", "detail": str(exc)})
    print(f'{venue} {year}: {len(pages)} pages, {sum(len(p["tencent_contexts"]) for p in pages)} Tencent contexts, {sum(len(p["pdf_urls"]) for p in pages)} PDF links', flush=True)
    return pages, errors


def main():
    tasks = [(v, y) for v in ["CoNEXT", "IMC", "HotNets"] for y in range(2019, 2027)]
    pages, errors = [], []
    with ThreadPoolExecutor(max_workers=4) as pool:
        for ps, es in pool.map(inspect, tasks):
            pages.extend(ps)
            errors.extend(es)
            save(ROOT / "data/program_discovery.json", {"pages": pages, "errors": errors})


if __name__ == "__main__":
    main()
