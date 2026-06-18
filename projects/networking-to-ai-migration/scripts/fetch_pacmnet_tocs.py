#!/usr/bin/env python3
"""Fetch PACMNET TOC records used as CoNEXT long-paper evidence.

PACMNET is ACM's journal-integrated proceedings venue for CoNEXT long papers.
This script fetches DBLP TOC volumes and writes a local paper table with full
DBLP author PIDs where available. It is intentionally separate from the main
new-core builder so network access and rate-limit retries are isolated.

Output:
  - data/pacmnet_toc_papers.json
Progress:
  - data/fetch_pacmnet_tocs_progress.json
"""

from __future__ import annotations

import json
import random
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
OUTPUT_FILE = DATA_DIR / "pacmnet_toc_papers.json"
PROGRESS_FILE = DATA_DIR / "fetch_pacmnet_tocs_progress.json"

# DBLP PACMNET volume mapping. Volume/year mapping is verified by paper years in
# fetched records; records with non-matching years are kept but flagged.
VOLUMES = [
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
    with open(path, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def fetch_volume(volume: str, retries: int = 7) -> dict[str, Any] | None:
    toc_key = f"db/journals/pacmnet/{volume}"
    url = (
        "https://dblp.org/search/publ/api"
        f"?q=toc%3A{toc_key.replace('/', '%2F')}.bht%3A"
        "&format=json&h=250"
    )
    for attempt in range(retries):
        wait = 20 * (2 ** attempt) + random.uniform(0, 5)
        try:
            result = subprocess.run(
                [
                    "curl", "-s", "-S", "--fail", "--max-time", "60",
                    "--connect-timeout", "15", "-H",
                    "User-Agent: networking-to-ai-migration/1.0 (academic research)",
                    url,
                ],
                capture_output=True,
                timeout=75,
            )
            if result.returncode != 0:
                stderr = result.stderr.decode("utf-8", errors="replace").strip()
                raise OSError(f"curl exited {result.returncode}: {stderr}")
            data = json.loads(result.stdout)
            hits = data.get("result", {}).get("hits", {})
            total = int(hits.get("@total", 0))
            if total == 0:
                return None
            return data
        except Exception as exc:
            if attempt == retries - 1:
                print(f"{volume}: failed after {retries} attempts: {exc}", file=sys.stderr)
                return None
            print(f"{volume}: attempt {attempt + 1} failed: {exc}; waiting {wait:.0f}s", file=sys.stderr)
            time.sleep(wait)
    return None


def parse_hits(data: dict[str, Any], volume: str, expected_year: int) -> list[dict[str, Any]]:
    hits = data.get("result", {}).get("hits", {})
    raw = hits.get("hit", [])
    if isinstance(raw, dict):
        raw = [raw]
    papers = []
    for hit in raw:
        info = hit.get("info", {})
        title = (info.get("title", "") or "").rstrip(".")
        year = int(info.get("year", 0) or 0)
        authors_raw = info.get("authors", {}).get("author", [])
        if isinstance(authors_raw, dict):
            authors_raw = [authors_raw]
        authors = []
        for author in authors_raw:
            pid = author.get("@pid", "")
            name = author.get("text", "")
            if pid or name:
                authors.append({"pid": pid, "name": name})
        if not title:
            continue
        papers.append({
            "title": title,
            "venue": "PACMNET",
            "year": year,
            "expected_year": expected_year,
            "year_matches_volume": year == expected_year,
            "volume": volume,
            "authors": authors,
            "dblp_url": info.get("url", ""),
            "doi": info.get("doi", ""),
            "source": "dblp_pacmnet_toc",
        })
    return papers


def main() -> None:
    progress = load_json(PROGRESS_FILE, {"completed_volumes": []})
    completed = set(progress.get("completed_volumes", []))
    existing = load_json(OUTPUT_FILE, {"papers": []})
    papers_by_url = {p.get("dblp_url", ""): p for p in existing.get("papers", []) if p.get("dblp_url")}
    metadata_by_volume = existing.get("metadata", {}).get("volumes", {})

    for spec in VOLUMES:
        volume = spec["volume"]
        expected_year = spec["expected_year"]
        if volume in completed:
            print(f"{volume}: already fetched")
            continue
        print(f"{volume}: fetching...", flush=True)
        data = fetch_volume(volume)
        if data is None:
            metadata_by_volume[volume] = {"expected_year": expected_year, "status": "not_found_or_failed"}
            completed.add(volume)
        else:
            hits = data.get("result", {}).get("hits", {})
            total = int(hits.get("@total", 0))
            parsed = parse_hits(data, volume, expected_year)
            for paper in parsed:
                papers_by_url[paper.get("dblp_url") or f"{paper['volume']}:{paper['title']}"] = paper
            metadata_by_volume[volume] = {
                "expected_year": expected_year,
                "status": "fetched",
                "dblp_total": total,
                "parsed_papers": len(parsed),
                "year_distribution": {},
            }
            counts: dict[str, int] = {}
            for paper in parsed:
                counts[str(paper["year"])] = counts.get(str(paper["year"]), 0) + 1
            metadata_by_volume[volume]["year_distribution"] = dict(sorted(counts.items()))
            completed.add(volume)
            print(f"{volume}: {len(parsed)} papers (DBLP total {total})")
        progress["completed_volumes"] = sorted(completed)
        save_json(PROGRESS_FILE, progress)
        output = {
            "metadata": {
                "description": "PACMNET DBLP TOC records for CoNEXT long-paper evidence",
                "volumes": metadata_by_volume,
                "fetched_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            },
            "papers": sorted(papers_by_url.values(), key=lambda p: (p.get("year", 0), p.get("title", ""))),
        }
        save_json(OUTPUT_FILE, output)
        time.sleep(8 + random.uniform(0, 4))

    print(f"Wrote {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
