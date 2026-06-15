#!/usr/bin/env python3
"""Fetch missing IMC 2018-2021 papers and merge into raw cache."""
import json, subprocess, time, random, sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
RAW_CACHE = DATA_DIR / "raw_dblp_papers.json"

IMC_URLS = {
    2018: "https://dblp.org/search/publ/api?q=toc%3Adb%2Fconf%2Fimc%2Fimc2018.bht%3A&format=json&h=250",
    2019: "https://dblp.org/search/publ/api?q=toc%3Adb%2Fconf%2Fimc%2Fimc2019.bht%3A&format=json&h=250",
    2020: "https://dblp.org/search/publ/api?q=toc%3Adb%2Fconf%2Fimc%2Fimc2020.bht%3A&format=json&h=250",
    2021: "https://dblp.org/search/publ/api?q=toc%3Adb%2Fconf%2Fimc%2Fimc2021.bht%3A&format=json&h=250",
}

def fetch(url, retries=5):
    for attempt in range(retries):
        try:
            result = subprocess.run(
                ["curl", "-s", "-S", "--max-time", "45", "--connect-timeout", "15", url],
                capture_output=True, timeout=55)
            data = json.loads(result.stdout)
            hits = data["result"]["hits"]
            total = int(hits["@total"])
            papers = hits.get("hit", [])
            if total > 0 and papers:
                return papers, total
            time.sleep(10 * (2**attempt) + random.uniform(0, 5))
        except Exception as e:
            print(f"  Attempt {attempt+1}: {e}", file=sys.stderr)
            time.sleep(10 * (2**attempt) + random.uniform(0, 5))
    raise RuntimeError("All retries exhausted")

# Load existing cache
with open(RAW_CACHE) as f:
    papers = json.load(f)
print(f"Existing papers: {len(papers)}")

# Check which IMC years already exist
existing_imc = set()
for p in papers:
    if p["venue"] == "IMC":
        existing_imc.add(p["year"])
print(f"Existing IMC years: {existing_imc}")

# Fetch missing
new_total = 0
for year, url in IMC_URLS.items():
    if year in existing_imc:
        print(f"IMC {year}: already in cache, skipping")
        continue

    print(f"IMC {year}: fetching...", end=" ", flush=True)
    try:
        imc_papers, count = fetch(url)
        for p in imc_papers:
            info = p.get("info", {})
            paper = {
                "title": info.get("title", "").rstrip("."),
                "venue": info.get("venue", "IMC"),
                "year": int(info.get("year", year)),
                "dblp_url": info.get("url", ""),
                "doi": info.get("doi", ""),
                "authors": []
            }
            # Extract authors
            authors = info.get("authors", {})
            author_list = authors.get("author", [])
            if isinstance(author_list, dict):
                author_list = [author_list]
            for a in author_list:
                pid = a.get("@pid", "")
                name = a.get("text", "")
                if pid:
                    paper["authors"].append({"pid": pid, "name": name})
                elif name:
                    paper["authors"].append({"pid": f"name:{name}", "name": name})
            papers.append(paper)
        new_total += len(imc_papers)
        print(f"{len(imc_papers)} papers (expected {count})")
    except Exception as e:
        print(f"FAILED: {e}")
    time.sleep(3 + random.uniform(0, 2))

# Save
with open(RAW_CACHE, "w") as f:
    json.dump(papers, f, indent=2, ensure_ascii=False)

print(f"\nAdded {new_total} papers. New total: {len(papers)}")
