#!/usr/bin/env python3
"""Fetch canonical top-networking venue-year paper records from DBLP TOCs.

This script repairs the incomplete post-2023 venue source used by earlier
new-core analysis. The old `post_gpt_venue_papers.json` path fetched only one
DBLP page per venue-year; this script paginates with `f=` and records fetch
coverage explicitly.

Output:
  - data/topnet_venue_year_papers.json
Progress:
  - data/fetch_topnet_venue_year_papers_progress.json
"""

from __future__ import annotations

import json
import random
import subprocess
import sys
import time
from pathlib import Path
from typing import Any
from urllib.parse import urlencode

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
OUTPUT_FILE = DATA_DIR / "topnet_venue_year_papers.json"
PROGRESS_FILE = DATA_DIR / "fetch_topnet_venue_year_papers_progress.json"

YEARS = list(range(2018, 2027))
PAGE_SIZE = 100
MAX_RETRIES = 6
BASE_DELAY = 2.5
JITTER = 1.5

VENUES = [
    {
        "name": "SIGCOMM",
        "toc_prefix": "db/conf/sigcomm/sigcomm",
        "years": YEARS,
        "year_suffix_overrides": {},
    },
    {
        "name": "NSDI",
        "toc_prefix": "db/conf/nsdi/nsdi",
        "years": YEARS,
        "year_suffix_overrides": {},
    },
    {
        "name": "CoNEXT",
        "toc_prefix": "db/conf/conext/conext",
        "years": YEARS,
        "year_suffix_overrides": {
            2023: "c",
        },
    },
    {
        "name": "HotNets",
        "toc_prefix": "db/conf/hotnets/hotnets",
        "years": YEARS,
        "year_suffix_overrides": {},
    },
    {
        "name": "IMC",
        "toc_prefix": "db/conf/imc/imc",
        "years": YEARS,
        "year_suffix_overrides": {},
    },
]

PACMNET_VOLUMES = [
    {"volume": "pacmnet1", "expected_year": 2023},
    {"volume": "pacmnet2", "expected_year": 2024},
    {"volume": "pacmnet3", "expected_year": 2025},
    {"volume": "pacmnet4", "expected_year": 2026},
]


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    with open(path) as f:
        return json.load(f)


def save_json(path: Path, data: Any) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def curl_json(url: str, timeout: int = 70) -> dict[str, Any]:
    cmd = [
        "curl",
        "-s",
        "-S",
        "--fail",
        "--max-time",
        str(timeout),
        "--connect-timeout",
        "15",
        "-H",
        "Accept: application/json",
        "-H",
        "User-Agent: networking-to-ai-migration/1.0 (academic research)",
        url,
    ]
    result = subprocess.run(cmd, capture_output=True, timeout=timeout + 10)
    if result.returncode != 0:
        stderr = result.stderr.decode("utf-8", errors="replace").strip()
        raise OSError(f"curl exited {result.returncode}: {stderr}")
    return json.loads(result.stdout)


def fetch_page(toc_key: str, first: int) -> dict[str, Any]:
    params = {
        "q": f"toc:{toc_key}.bht:",
        "format": "json",
        "h": PAGE_SIZE,
        "f": first,
    }
    url = f"https://dblp.org/search/publ/api?{urlencode(params)}"
    for attempt in range(MAX_RETRIES):
        try:
            return curl_json(url)
        except Exception as exc:
            if attempt == MAX_RETRIES - 1:
                raise
            wait = 8 * (2 ** attempt) + random.uniform(0, 4)
            print(
                f"  {toc_key} f={first}: attempt {attempt + 1} failed: {exc}; waiting {wait:.0f}s",
                file=sys.stderr,
            )
            time.sleep(wait)
    raise RuntimeError(f"unreachable retry loop for {toc_key}")


def raw_hits(data: dict[str, Any]) -> tuple[int, list[dict[str, Any]]]:
    hits = data.get("result", {}).get("hits", {})
    total = int(hits.get("@total", 0))
    hit_list = hits.get("hit", [])
    if isinstance(hit_list, dict):
        hit_list = [hit_list]
    return total, hit_list


def extract_authors(info: dict[str, Any]) -> list[dict[str, str]]:
    authors_raw = info.get("authors", {}).get("author", [])
    if isinstance(authors_raw, dict):
        authors_raw = [authors_raw]
    authors = []
    for author in authors_raw or []:
        pid = author.get("@pid", "")
        name = author.get("text", "")
        if pid or name:
            authors.append({"pid": pid, "name": name})
    return authors


def normalized_record_type(dblp_type: str, canonical_venue: str) -> str:
    type_cf = (dblp_type or "").strip().casefold()
    if type_cf == "conference and workshop papers":
        return "inproceedings"
    if type_cf == "journal articles" and canonical_venue == "PACMNET":
        return "inproceedings"
    if type_cf == "journal articles":
        return "article"
    if type_cf == "editorship":
        return "proceedings"
    return type_cf


def extract_paper(hit: dict[str, Any], *, canonical_venue: str, source_toc_key: str, source_kind: str, expected_year: int | None = None) -> dict[str, Any] | None:
    info = hit.get("info", {})
    title = (info.get("title") or "").rstrip(".")
    if not title:
        return None
    try:
        year = int(info.get("year") or expected_year or 0)
    except ValueError:
        year = int(expected_year or 0)
    dblp_type = hit.get("type") or info.get("type", "")
    return {
        "title": title,
        "venue": canonical_venue,
        "year": year,
        "authors": extract_authors(info),
        "dblp_url": info.get("url", ""),
        "doi": info.get("doi", ""),
        "dblp_key": info.get("key", ""),
        "record_type": normalized_record_type(dblp_type, canonical_venue),
        "dblp_publication_type": dblp_type,
        "is_journal": dblp_type == "Journal Articles",
        "source": source_kind,
        "source_toc_key": source_toc_key,
        "expected_year": expected_year,
        "year_matches_expected": None if expected_year is None else year == expected_year,
    }


def fetch_toc_records(toc_key: str, *, canonical_venue: str, source_kind: str, expected_year: int | None = None) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    papers: list[dict[str, Any]] = []
    first = 0
    total: int | None = None
    pages = []

    while True:
        data = fetch_page(toc_key, first)
        page_total, hits = raw_hits(data)
        if total is None:
            total = page_total
        pages.append({"first": first, "returned": len(hits), "reported_total": page_total})
        if not hits:
            break
        for hit in hits:
            paper = extract_paper(
                hit,
                canonical_venue=canonical_venue,
                source_toc_key=toc_key,
                source_kind=source_kind,
                expected_year=expected_year,
            )
            if paper is not None:
                papers.append(paper)
        first += len(hits)
        if first >= page_total:
            break
        time.sleep(BASE_DELAY + random.uniform(0, JITTER))

    status = "not_found_or_not_indexed" if not total else "fetched"
    audit = {
        "toc_key": toc_key,
        "canonical_venue": canonical_venue,
        "expected_year": expected_year,
        "source_kind": source_kind,
        "status": status,
        "dblp_reported_total": total or 0,
        "records_returned": len(papers),
        "page_count": len(pages),
        "pages": pages,
        "year_distribution": {},
    }
    by_year: dict[str, int] = {}
    for paper in papers:
        year_s = str(paper.get("year", ""))
        by_year[year_s] = by_year.get(year_s, 0) + 1
    audit["year_distribution"] = dict(sorted(by_year.items()))
    if total is not None and len(papers) != total:
        audit["status"] = "count_mismatch_after_pagination"
    return papers, audit


def record_key(paper: dict[str, Any]) -> str:
    if paper.get("dblp_key"):
        return f"dblp:{paper['dblp_key']}"
    if paper.get("doi"):
        return f"doi:{paper['doi'].strip().lower()}"
    return f"{paper.get('source_toc_key')}|{paper.get('year')}|{paper.get('title', '').casefold()}"


def main() -> None:
    progress = load_json(PROGRESS_FILE, {"completed": []})
    completed = {tuple(item) for item in progress.get("completed", [])}
    existing = load_json(OUTPUT_FILE, {"papers": [], "coverage": []})
    papers_by_key = {record_key(p): p for p in existing.get("papers", [])}
    coverage_by_key = {
        (row.get("source_kind"), row.get("toc_key")): row
        for row in existing.get("coverage", [])
    }

    for venue in VENUES:
        name = venue["name"]
        for year in venue["years"]:
            suffix = venue.get("year_suffix_overrides", {}).get(year, "")
            toc_key = f"{venue['toc_prefix']}{year}{suffix}"
            progress_key = ("conference_toc", toc_key)
            if progress_key in completed:
                print(f"{name} {year}: already fetched")
                continue
            print(f"{name} {year}: fetching {toc_key}...", flush=True)
            papers, audit = fetch_toc_records(
                toc_key,
                canonical_venue=name,
                source_kind="conference_toc",
                expected_year=year,
            )
            for paper in papers:
                papers_by_key[record_key(paper)] = paper
            coverage_by_key[(audit["source_kind"], audit["toc_key"])] = audit
            completed.add(progress_key)
            progress["completed"] = sorted([list(item) for item in completed])
            save_json(PROGRESS_FILE, progress)
            write_output(papers_by_key, coverage_by_key)
            print(f"  returned {len(papers)} / DBLP total {audit['dblp_reported_total']}")
            time.sleep(BASE_DELAY + random.uniform(0, JITTER))

    for spec in PACMNET_VOLUMES:
        volume = spec["volume"]
        expected_year = spec["expected_year"]
        toc_key = f"db/journals/pacmnet/{volume}"
        progress_key = ("pacmnet_toc", toc_key)
        if progress_key in completed:
            print(f"{volume}: already fetched")
            continue
        print(f"{volume}: fetching {toc_key}...", flush=True)
        papers, audit = fetch_toc_records(
            toc_key,
            canonical_venue="PACMNET",
            source_kind="pacmnet_toc",
            expected_year=expected_year,
        )
        for paper in papers:
            papers_by_key[record_key(paper)] = paper
        coverage_by_key[(audit["source_kind"], audit["toc_key"])] = audit
        completed.add(progress_key)
        progress["completed"] = sorted([list(item) for item in completed])
        save_json(PROGRESS_FILE, progress)
        write_output(papers_by_key, coverage_by_key)
        print(f"  returned {len(papers)} / DBLP total {audit['dblp_reported_total']}")
        time.sleep(BASE_DELAY + random.uniform(0, JITTER))

    write_output(papers_by_key, coverage_by_key)
    print(f"Wrote {OUTPUT_FILE}")


def write_output(papers_by_key: dict[str, dict[str, Any]], coverage_by_key: dict[tuple[str, str], dict[str, Any]]) -> None:
    papers = sorted(
        papers_by_key.values(),
        key=lambda p: (int(p.get("year") or 0), p.get("venue", ""), p.get("title", "")),
    )
    coverage = sorted(
        coverage_by_key.values(),
        key=lambda r: (r.get("source_kind", ""), r.get("canonical_venue", ""), int(r.get("expected_year") or 9999), r.get("toc_key", "")),
    )
    output = {
        "metadata": {
            "description": "Canonical paginated DBLP TOC records for top-networking venue-year completeness checks.",
            "venues": [v["name"] for v in VENUES],
            "years": YEARS,
            "page_size": PAGE_SIZE,
            "coNEXT_policy": "CoNEXT 2023 uses conext2023c for conference proceedings; PACMNET volumes are fetched separately as CoNEXT long-paper evidence.",
            "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "paper_count": len(papers),
        },
        "coverage": coverage,
        "papers": papers,
    }
    save_json(OUTPUT_FILE, output)


if __name__ == "__main__":
    main()
