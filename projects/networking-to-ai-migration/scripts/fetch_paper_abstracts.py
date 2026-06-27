#!/usr/bin/env python3
"""Fetch paper abstracts from OpenAlex and Semantic Scholar free APIs.

Input: data/new_core_clean_papers.json (2,236 clean papers)
Output: data/paper_abstracts.json (abstracts keyed by paper_id)
Progress: data/abstract_fetch_progress.json

Strategy:
  - Primary: OpenAlex works API by DOI (10 req/s rate limit, generous)
  - Fallback: OpenAlex works search by title (when DOI missing)
  - Tertiary: Semantic Scholar API by title (when OpenAlex returns nothing)

OpenAlex stores abstracts as inverted indices; this script reconstructs them.
"""

from __future__ import annotations

import json
import random
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import Any
from urllib.parse import quote, urlencode

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

INPUT_CLEAN_PAPERS = DATA_DIR / "new_core_clean_papers.json"
OUTPUT_ABSTRACTS = DATA_DIR / "paper_abstracts.json"
PROGRESS_FILE = DATA_DIR / "abstract_fetch_progress.json"

# OpenAlex is very generous: 100k requests/day, 10 req/s recommended.
# We stay at 8 req/s to be polite.
OPENALEX_DELAY = 0.125  # 8 req/s
SEMANTIC_SCHOLAR_DELAY = 0.75  # ~1.3 req/s (conservative without key)
MAX_RETRIES = 4
REQUEST_TIMEOUT = 25

SEMANTIC_SCHOLAR_BASE = "https://api.semanticscholar.org/graph/v1"
OPENALEX_BASE = "https://api.openalex.org"


def load_json(path: Path, default: Any = None) -> Any:
    if not path.exists():
        return default
    with open(path) as f:
        return json.load(f)


def save_json(path: Path, data: Any) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(".tmp")
    with open(temp, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    temp.rename(path)


def curl_json(url: str, timeout: int = REQUEST_TIMEOUT) -> dict[str, Any] | None:
    cmd = [
        "curl", "-s", "-S", "--fail",
        "--max-time", str(timeout),
        "--connect-timeout", "10",
        "-H", "Accept: application/json",
        "-H", "User-Agent: networking-to-ai-migration/1.0 (academic research; mailto:research@example.com)",
        url,
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, timeout=timeout + 5)
    except subprocess.TimeoutExpired:
        return None
    if result.returncode != 0:
        return None
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        return None


def reconstruct_abstract(inverted_index: dict[str, list[int]] | None) -> str:
    """Reconstruct plain text from OpenAlex abstract_inverted_index."""
    if not inverted_index:
        return ""
    word_positions: list[tuple[int, str]] = []
    for word, positions in inverted_index.items():
        for pos in positions:
            word_positions.append((pos, word))
    word_positions.sort(key=lambda x: x[0])
    return " ".join(w for _, w in word_positions)


def fetch_openalex_by_doi(doi: str) -> dict[str, str] | None:
    """Fetch a single work from OpenAlex by DOI."""
    encoded = quote(doi.strip(), safe="")
    url = f"{OPENALEX_BASE}/works/doi:{encoded}?select=id,doi,title,abstract_inverted_index,publication_date"
    data = curl_json(url)
    if not data or not data.get("id"):
        return None
    abstract = reconstruct_abstract(data.get("abstract_inverted_index"))
    return {
        "source": "openalex",
        "doi": data.get("doi", doi),
        "title": data.get("title", ""),
        "abstract": abstract,
        "abstract_truncated": False,
    }


def fetch_openalex_by_title(title: str, year: int | None = None) -> dict[str, str] | None:
    """Search OpenAlex by title, verify match, return abstract."""
    # Clean title for search: remove punctuation, truncate to reasonable length
    clean = re.sub(r"[^\w\s]", " ", title)
    clean = re.sub(r"\s+", " ", clean).strip()
    # Use first 200 chars as search query
    query = clean[:200]
    params = {
        "search": query,
        "per_page": "3",
        "select": "id,doi,title,abstract_inverted_index,publication_date",
    }
    url = f"{OPENALEX_BASE}/works?{urlencode(params)}"
    data = curl_json(url)
    if not data:
        return None
    results = data.get("results", [])
    if not results:
        return None

    # Verify title similarity using bidirectional Jaccard
    norm_title = clean.lower()
    title_words = set(norm_title.split())
    if len(title_words) < 3:
        return None

    for work in results:
        work_title = (work.get("title") or "").lower()
        work_words = set(work_title.split())
        if not work_words:
            continue
        # Bidirectional: handle partial/short titles (e.g., "403 Forbidden" matches
        # "403 Forbidden: A Global View of CDN Geoblocking")
        intersection = len(title_words & work_words)
        forward = intersection / len(title_words) if title_words else 0
        backward = intersection / len(work_words) if work_words else 0
        overlap = max(forward, backward)
        if overlap >= 0.4:  # Lenient for partial matches
            abstract = reconstruct_abstract(work.get("abstract_inverted_index"))
            return {
                "source": "openalex_title",
                "doi": work.get("doi", ""),
                "title": work.get("title", ""),
                "abstract": abstract,
                "abstract_truncated": False,
            }
    return None


def fetch_semantic_scholar_by_doi(doi: str) -> dict[str, str] | None:
    """Fetch abstract from Semantic Scholar by DOI."""
    encoded = quote(doi.strip(), safe="")
    url = f"{SEMANTIC_SCHOLAR_BASE}/paper/DOI:{encoded}?fields=title,abstract"
    data = curl_json(url)
    if not data or not data.get("paperId"):
        return None
    abstract = data.get("abstract") or ""
    return {
        "source": "semantic_scholar",
        "doi": doi,
        "title": data.get("title", ""),
        "abstract": abstract,
        "abstract_truncated": len(abstract) > 3000,
    }


def fetch_semantic_scholar_by_title(title: str) -> dict[str, str] | None:
    """Search Semantic Scholar by title, verify, return abstract."""
    params = {"query": title[:250], "limit": "3", "fields": "title,abstract"}
    url = f"{SEMANTIC_SCHOLAR_BASE}/paper/search?{urlencode(params)}"
    data = curl_json(url)
    if not data:
        return None
    papers = data.get("data", [])
    if not papers:
        return None

    norm_title = re.sub(r"[^\w\s]", " ", title).lower()
    norm_title = re.sub(r"\s+", " ", norm_title).strip()
    title_words = set(norm_title.split())
    if len(title_words) < 3:
        return None

    for paper in papers:
        work_title = (paper.get("title") or "").lower()
        work_words = set(work_title.split())
        if not work_words:
            continue
        intersection = len(title_words & work_words)
        forward = intersection / len(title_words) if title_words else 0
        backward = intersection / len(work_words) if work_words else 0
        overlap = max(forward, backward)
        if overlap >= 0.4:
            abstract = paper.get("abstract") or ""
            return {
                "source": "semantic_scholar_title",
                "doi": "",
                "title": paper.get("title", ""),
                "abstract": abstract,
                "abstract_truncated": len(abstract) > 3000,
            }
    return None


def fetch_abstract_for_paper(paper: dict[str, Any], stats: dict[str, int]) -> dict[str, str] | None:
    """Try all available strategies to fetch an abstract for a paper."""
    title = paper.get("title", "")
    doi = paper.get("doi", "").strip()
    year = int(paper.get("year") or 0)

    # Strategy 1: OpenAlex by DOI (fastest, most reliable)
    if doi:
        stats["attempted_oa_doi"] += 1
        result = fetch_openalex_by_doi(doi)
        if result and result.get("abstract"):
            stats["success_oa_doi"] += 1
            return result
        time.sleep(OPENALEX_DELAY + random.uniform(0, 0.05))

    # Strategy 2: OpenAlex by title
    stats["attempted_oa_title"] += 1
    result = fetch_openalex_by_title(title, year)
    if result and result.get("abstract"):
        stats["success_oa_title"] += 1
        return result
    time.sleep(OPENALEX_DELAY + random.uniform(0, 0.05))

    # Strategy 3: Semantic Scholar by DOI
    if doi:
        stats["attempted_s2_doi"] += 1
        result = fetch_semantic_scholar_by_doi(doi)
        if result and result.get("abstract"):
            stats["success_s2_doi"] += 1
            return result
        time.sleep(SEMANTIC_SCHOLAR_DELAY + random.uniform(0, 0.3))

    # Strategy 4: Semantic Scholar by title
    stats["attempted_s2_title"] += 1
    result = fetch_semantic_scholar_by_title(title)
    if result and result.get("abstract"):
        stats["success_s2_title"] += 1
        return result
    time.sleep(SEMANTIC_SCHOLAR_DELAY + random.uniform(0, 0.3))

    stats["not_found"] += 1
    return None


def main() -> None:
    clean_data = load_json(INPUT_CLEAN_PAPERS, {"papers": []})
    all_papers = clean_data.get("papers", [])
    included = [p for p in all_papers if p.get("included_in_new_core_scope")]
    print(f"Loaded {len(included)} included papers from {INPUT_CLEAN_PAPERS}")

    # Load existing abstracts and progress
    existing = load_json(OUTPUT_ABSTRACTS, {"abstracts": {}, "metadata": {}})
    abstracts = existing.get("abstracts", {})

    stats = {
        "attempted_oa_doi": 0, "success_oa_doi": 0,
        "attempted_oa_title": 0, "success_oa_title": 0,
        "attempted_s2_doi": 0, "success_s2_doi": 0,
        "attempted_s2_title": 0, "success_s2_title": 0,
        "not_found": 0, "already_had": 0,
    }

    # Count already-fetched
    for p in included:
        if p["paper_id"] in abstracts and abstracts[p["paper_id"]].get("abstract"):
            stats["already_had"] += 1

    pending = [p for p in included if p["paper_id"] not in abstracts or not abstracts[p["paper_id"]].get("abstract")]
    print(f"Already have abstracts: {stats['already_had']}")
    print(f"Need to fetch: {len(pending)}")

    checkpoint_interval = 50
    for i, paper in enumerate(pending):
        pid = paper["paper_id"]
        title_short = paper["title"][:70]

        result = fetch_abstract_for_paper(paper, stats)

        if result:
            abstracts[pid] = {
                "paper_id": pid,
                "abstract": result["abstract"],
                "source": result["source"],
                "source_title": result.get("title", ""),
                "source_doi": result.get("doi", ""),
            }
            print(f"  [{i+1}/{len(pending)}] OK ({result['source']}): {title_short}")
        else:
            abstracts[pid] = {
                "paper_id": pid,
                "abstract": "",
                "source": "none",
                "source_title": "",
                "source_doi": "",
            }
            print(f"  [{i+1}/{len(pending)}] NO ABSTRACT: {title_short}")

        # Checkpoint
        if (i + 1) % checkpoint_interval == 0:
            found = sum(1 for a in abstracts.values() if a.get("abstract"))
            total_done = stats["already_had"] + i + 1
            total_with = stats["already_had"] + found
            output = {
                "metadata": {
                    "description": "Fetched paper abstracts for networking paper classification.",
                    "source_apis": ["openalex", "semantic_scholar"],
                    "total_papers_processed": total_done,
                    "abstracts_found": total_with,
                    "abstracts_not_found": total_done - total_with,
                    "fetch_date": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                },
                "abstracts": dict(sorted(abstracts.items())),
            }
            save_json(OUTPUT_ABSTRACTS, output)
            print(f"  [checkpoint {total_done}/{len(included)}] saved; {total_with} have abstracts")

    # Final save
    found = sum(1 for a in abstracts.values() if a.get("abstract"))
    output = {
        "metadata": {
            "description": "Fetched paper abstracts for networking paper classification.",
            "source_apis": ["openalex", "semantic_scholar"],
            "total_papers_processed": len(included),
            "abstracts_found": found,
            "abstracts_not_found": len(included) - found,
            "fetch_date": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "stats": stats,
        },
        "abstracts": dict(sorted(abstracts.items())),
    }
    save_json(OUTPUT_ABSTRACTS, output)
    print(f"\nDone. Wrote {OUTPUT_ABSTRACTS}")
    print(f"Abstracts found: {found}/{len(included)} ({found/len(included)*100:.1f}%)")
    for k, v in sorted(stats.items()):
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
