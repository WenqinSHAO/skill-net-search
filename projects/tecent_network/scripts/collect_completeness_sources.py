#!/usr/bin/env python3
"""Follow official accepted/poster/TOC links, preserving errors and source roles."""
import json
import re
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from collect import ROOT, fetch, save, text


def task(cell):
    venue, year = cell
    slug = "co-next" if venue == "CoNEXT" else venue.lower()
    base = f"https://conferences.sigcomm.org/{slug}/{year}/"
    pages, errors = [], []
    urls = {base: "home"}
    discovery = json.loads((ROOT / "data/program_discovery.json").read_text())
    for p in discovery["pages"]:
        if (p["venue"], p["year"]) == cell and ("program" in p["url"] or "accepted" in p["url"]):
            urls[p["url"]] = "program"
    if venue == "SIGCOMM":
        urls[base + ("accepted/" if year >= 2025 else "accepted-papers.html")] = "accepted_papers"
        urls[base + ("papers-posters-demos-info/" if year == 2025 else "cf-posters.html")] = "poster"
    seen = set()
    while urls and len(seen) < 12:
        url, role = next(iter(urls.items()))
        del urls[url]
        if url in seen:
            continue
        seen.add(url)
        try:
            raw, info = fetch(url)
            soup = BeautifulSoup(raw, "html.parser")
            if role != "home":
                pages.append({**info, "venue": venue, "year": year, "role": role, "publication_type": "poster" if role == "poster" else ""})
            linkbase = urljoin(url, soup.select_one("base[href]")["href"]) if soup.select_one("base[href]") else base if "/partials/" in url else url
            for a in soup.select("a[href]"):
                label = text(a).casefold()
                href = urljoin(linkbase, a["href"]).split("#")[0]
                if not href.startswith(base) or ".pdf" in href.lower():
                    continue
                if any(w in label for w in ["accepted paper", "accepted poster", "poster schedule", "open table of contents", "toc", "list of papers"]):
                    urls[href] = "poster" if "poster" in label else "publisher_toc" if "toc" in label or "table of contents" in label else "accepted_papers"
            if role == "home" and venue == "CoNEXT":
                for script in soup.select("script[src]"):
                    if "app.js" in script["src"]:
                        js, _ = fetch(urljoin(base, script["src"]))
                        for template in re.findall(r'templateUrl\s*:\s*[\"\x27]([^\"\x27]+)', js):
                            if re.search(r"(?:accepted-posters|program-poster|(?:^|/)posters\.html|pprogram\.html)", template):
                                urls[urljoin(base, template)] = "poster"
        except Exception as exc:
            errors.append({"venue": venue, "year": year, "url": url, "role": role, "status": "fetch_error", "detail": str(exc)})
    print(f"Extra official sources {venue} {year}: {len(pages)} pages, {len(errors)} failures", flush=True)
    return pages, errors


def main():
    cells = [(v, y) for v in ["SIGCOMM", "CoNEXT", "IMC", "HotNets"] for y in range(2019, 2027)]
    pages, errors = [], []
    with ThreadPoolExecutor(max_workers=4) as pool:
        for ps, es in pool.map(task, cells):
            pages.extend(ps)
            errors.extend(es)
            save(ROOT / "data/completeness_sources.json", {"pages": pages, "errors": errors})


if __name__ == "__main__":
    main()
