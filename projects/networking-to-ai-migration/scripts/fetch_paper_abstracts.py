#!/usr/bin/env python3
"""Fetch paper abstracts from OpenAlex and Semantic Scholar free APIs.

Input: data/new_core_clean_papers.json (2,236 clean papers)
Output: data/paper_abstracts.json (abstracts keyed by paper_id)
Caches:
  - data/usenix_nsdi_abstract_cache.json
  - data/abstract_title_match_quarantine.json

Strategy:
  - USENIX NSDI paper pages for NSDI records, which usually lack DOI in DBLP
  - OpenAlex works API by DOI (10 req/s rate limit, generous)
  - OpenAlex works search by title with strict title matching
  - Semantic Scholar by DOI/title with strict title matching

OpenAlex stores abstracts as inverted indices; this script reconstructs them.
"""

from __future__ import annotations

import json
import random
import re
import subprocess
from html.parser import HTMLParser
from html import unescape
import sys
import time
from pathlib import Path
from typing import Any
from urllib.parse import quote, urlencode, urljoin

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

INPUT_CLEAN_PAPERS = DATA_DIR / "new_core_clean_papers.json"
OUTPUT_ABSTRACTS = DATA_DIR / "paper_abstracts.json"
USENIX_CACHE_FILE = DATA_DIR / "usenix_nsdi_abstract_cache.json"
TITLE_MATCH_QUARANTINE_FILE = DATA_DIR / "abstract_title_match_quarantine.json"

# OpenAlex is very generous: 100k requests/day, 10 req/s recommended.
# We stay at 8 req/s to be polite.
OPENALEX_DELAY = 0.125  # 8 req/s
SEMANTIC_SCHOLAR_DELAY = 0.75  # ~1.3 req/s (conservative without key)
MAX_RETRIES = 4
REQUEST_TIMEOUT = 25

SEMANTIC_SCHOLAR_BASE = "https://api.semanticscholar.org/graph/v1"
OPENALEX_BASE = "https://api.openalex.org"
USENIX_BASE = "https://www.usenix.org"

QUARANTINED_TITLE_MATCHES: list[dict[str, Any]] = []


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


def normalize_title(title: str) -> str:
    title = re.sub(r"&[a-zA-Z]+;", " ", title or "")
    title = re.sub(r"[^\w\s]", " ", title.lower())
    title = re.sub(r"\s+", " ", title).strip()
    return title


def title_match_metrics(target_title: str, source_title: str) -> dict[str, float | int | bool]:
    target_norm = normalize_title(target_title)
    source_norm = normalize_title(source_title)
    target_words = set(target_norm.split())
    source_words = set(source_norm.split())
    if not target_words or not source_words:
        return {
            "exact": False,
            "forward_overlap": 0.0,
            "backward_overlap": 0.0,
            "max_overlap": 0.0,
            "source_word_count": len(source_words),
        }
    overlap = len(target_words & source_words)
    forward = overlap / len(target_words)
    backward = overlap / len(source_words)
    return {
        "exact": target_norm == source_norm,
        "forward_overlap": round(forward, 4),
        "backward_overlap": round(backward, 4),
        "max_overlap": round(max(forward, backward), 4),
        "source_word_count": len(source_words),
    }


def title_match_acceptable(target_title: str, source_title: str) -> tuple[bool, dict[str, float | int | bool]]:
    """Accept only exact or high-forward-overlap title matches."""
    metrics = title_match_metrics(target_title, source_title)
    acceptable = bool(metrics["exact"]) or (
        float(metrics["forward_overlap"]) >= 0.75 and int(metrics["source_word_count"]) >= 4
    )
    return acceptable, metrics


def quarantine_title_match(
    *,
    source: str,
    paper_title: str,
    source_title: str,
    source_doi: str = "",
    reason: str,
    metrics: dict[str, Any],
) -> None:
    QUARANTINED_TITLE_MATCHES.append({
        "source": source,
        "paper_title": paper_title,
        "source_title": source_title,
        "source_doi": source_doi,
        "reason": reason,
        "metrics": metrics,
    })


def save_title_match_quarantine() -> None:
    save_json(TITLE_MATCH_QUARANTINE_FILE, {
        "metadata": {
            "description": "Rejected title-sourced abstract matches. These are not used in paper_abstracts.json.",
            "count": len(QUARANTINED_TITLE_MATCHES),
            "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        },
        "matches": QUARANTINED_TITLE_MATCHES,
    })


def curl_text(url: str, timeout: int = REQUEST_TIMEOUT) -> str | None:
    cmd = [
        "curl", "-s", "-S", "--fail",
        "--max-time", str(timeout),
        "--connect-timeout", "10",
        "-H", "Accept: text/html,application/xhtml+xml",
        "-H", "User-Agent: networking-to-ai-migration/1.0 (academic research; mailto:research@example.com)",
        url,
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, timeout=timeout + 5)
    except subprocess.TimeoutExpired:
        return None
    if result.returncode != 0:
        return None
    return result.stdout.decode("utf-8", errors="replace")


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


class UsenixPaperParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.meta: dict[str, str] = {}
        self.text_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "meta":
            return
        attrs_d = {k.lower(): v or "" for k, v in attrs}
        key = (attrs_d.get("name") or attrs_d.get("property") or "").lower()
        if key:
            self.meta[key] = attrs_d.get("content", "")

    def handle_data(self, data: str) -> None:
        text = data.strip()
        if text:
            self.text_parts.append(text)

    @property
    def text(self) -> str:
        return re.sub(r"\s+", " ", " ".join(self.text_parts)).strip()


def usenix_nsdi_slug(year: int) -> str:
    return f"nsdi{str(year)[-2:]}"


def usenix_nsdi_technical_sessions_url(year: int) -> str:
    slug = usenix_nsdi_slug(year)
    return f"{USENIX_BASE}/conference/{slug}/technical-sessions"



def html_to_text(html: str) -> str:
    text = re.sub(r"<script\b[^>]*>.*?</script>", " ", html, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<style\b[^>]*>.*?</style>", " ", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<[^>]+>", " ", text)
    text = unescape(text)
    return re.sub(r"\s+", " ", text).strip()


def extract_usenix_field(html: str, class_name: str) -> str:
    markers = [
        f"field--name-{class_name}",
        f"field-{class_name.replace('_', '-')}",
        f"field-name-{class_name}",
        f"field-name-{class_name.replace('-', '_')}",
        f"field-name-{class_name}-long",
    ]
    idx = -1
    marker = ""
    for candidate in markers:
        idx = html.find(candidate)
        if idx >= 0:
            marker = candidate
            break
    if idx < 0:
        return ""
    start = html.rfind("<div", 0, idx)
    if start < 0:
        start = idx
    # USENIX has used multiple Drupal generations. Capturing until the next
    # field/media/article marker is more robust than assuming a fixed </div>
    # depth, and works for both paper pages and inline schedule blocks.
    end_candidates = [
        html.find('field--name-', idx + len(marker)),
        html.find('field-name-', idx + len(marker)),
        html.find('usenix-schedule-media', idx + len(marker)),
        html.find('<article ', idx + len(marker)),
        html.find('</article>', idx + len(marker)),
    ]
    end_candidates = [x for x in end_candidates if x > idx]
    end = min(end_candidates) if end_candidates else min(len(html), idx + 16000)
    return html_to_text(html[start:end])


def parse_usenix_inline_sessions(index_url: str, html: str, year: int) -> dict[str, dict[str, str]]:
    """Parse paper title/abstract blocks embedded in a USENIX sessions page.

    NSDI 2023 exposes many accepted papers directly in the technical-sessions
    page rather than via separate paper-page metadata. This supports both newer
    field--name-* pages and older schedule articles with field-name-* classes.
    """
    out: dict[str, dict[str, str]] = {}

    article_pat = re.compile(
        r'<article\b[^>]*class="[^"]*node-paper[^"]*"[^>]*>(.*?)</article>',
        re.DOTALL | re.IGNORECASE,
    )
    articles = list(article_pat.finditer(html))
    if articles:
        for article in articles:
            block = article.group(1)
            title_match = re.search(r'<h2[^>]*>\s*<a[^>]*href="([^"]+)"[^>]*>(.*?)</a>', block, re.DOTALL | re.IGNORECASE)
            if not title_match:
                continue
            href = title_match.group(1)
            title = html_to_text(title_match.group(2))
            abstract = extract_usenix_field(block, "field-paper-description")
            if not abstract or len(abstract.split()) < 20:
                abstract = extract_usenix_field(block, "field-paper-description-long")
            if not abstract or len(abstract.split()) < 20:
                abstract = extract_usenix_abstract_from_text(html_to_text(block))
            if not title or not abstract or len(abstract.split()) < 20:
                continue
            out[normalize_title(title)] = {
                "source": "usenix_nsdi_inline_sessions",
                "title": title,
                "abstract": abstract,
                "url": urljoin(USENIX_BASE, href) if href else index_url,
                "doi": "",
                "abstract_truncated": False,
            }
        if out:
            return out

    title_pat = re.compile(
        r'class="[^"]*field--name-field-paper-title[^"]*"[^>]*>(.*?)</div>',
        re.DOTALL | re.IGNORECASE,
    )
    matches = list(title_pat.finditer(html))
    for i, match in enumerate(matches):
        title = html_to_text(match.group(1))
        if not title:
            continue
        block_end = matches[i + 1].start() if i + 1 < len(matches) else min(len(html), match.end() + 16000)
        block = html[match.end():block_end]
        abstract = extract_usenix_field(block, "field-paper-description")
        if not abstract or len(abstract.split()) < 20:
            abstract = extract_usenix_abstract_from_text(html_to_text(block))
        if not abstract or len(abstract.split()) < 20:
            continue
        out[normalize_title(title)] = {
            "source": "usenix_nsdi_inline_sessions",
            "title": title,
            "abstract": abstract,
            "url": index_url,
            "doi": "",
            "abstract_truncated": False,
        }
    return out

def extract_usenix_abstract_from_text(text: str) -> str:
    markers = ["Abstract:", "Abstract"]
    start = -1
    marker_len = 0
    for marker in markers:
        start = text.find(marker)
        if start >= 0:
            marker_len = len(marker)
            break
    if start < 0:
        return ""
    work = text[start + marker_len:].strip()
    end_markers = [
        "View the Presentation",
        "Presentation Video",
        "Open Access Media",
        "BibTeX",
        "Authors:",
        "Author(s):",
        "Paper PDF",
        "Download",
    ]
    end_positions = [work.find(marker) for marker in end_markers if work.find(marker) > 0]
    if end_positions:
        work = work[:min(end_positions)]
    work = re.sub(r"\s+", " ", work).strip()
    return work if len(work.split()) >= 20 else ""


def parse_usenix_paper_page(url: str, html: str) -> dict[str, str] | None:
    parser = UsenixPaperParser()
    parser.feed(html)
    title = (
        parser.meta.get("citation_title")
        or parser.meta.get("og:title")
        or parser.meta.get("twitter:title")
        or ""
    ).strip()

    # USENIX stores the abstract in a Drupal field on most paper pages.
    abstract = extract_usenix_field(html, "field-paper-description")
    if not abstract:
        abstract = (
            parser.meta.get("description")
            or parser.meta.get("og:description")
            or ""
        ).strip()
    if len(abstract.split()) < 20:
        abstract = extract_usenix_abstract_from_text(parser.text)
    if not title or not abstract:
        return None
    return {
        "source": "usenix_nsdi_page",
        "title": title,
        "abstract": abstract,
        "url": url,
        "doi": "",
        "abstract_truncated": False,
    }


def fetch_usenix_nsdi_year(year: int) -> dict[str, dict[str, str]]:
    """Fetch NSDI abstracts from USENIX paper pages for one year.

    Uses regex to extract presentation links from the technical-sessions page
    (the HTMLParser-based approach fails on USENIX's nested-link structure).
    """
    index_url = usenix_nsdi_technical_sessions_url(year)
    html = curl_text(index_url, timeout=45)
    if not html:
        return {}

    slug = usenix_nsdi_slug(year)
    pattern = re.compile(
        r'<a[^>]*href="([^"]*' + re.escape(f"/conference/{slug}/presentation/") + r'[^"]*)"[^>]*>(.*?)</a>',
        re.DOTALL,
    )
    # Deduplicate URLs keeping longest text
    best_text: dict[str, str] = {}
    for href, raw_text in pattern.findall(html):
        text_clean = re.sub(r"<[^>]+>", " ", raw_text).strip()
        text_clean = re.sub(r"\s+", " ", text_clean).strip()
        if text_clean and len(text_clean) > len(best_text.get(href, "")):
            best_text[href] = text_clean

    out: dict[str, dict[str, str]] = parse_usenix_inline_sessions(index_url, html, year)
    if len(out) >= 20:
        return out

    urls = sorted(best_text.keys())
    for i, href in enumerate(urls):
        full = urljoin(USENIX_BASE, href)
        page = curl_text(full, timeout=45)
        if not page:
            continue
        parsed = parse_usenix_paper_page(full, page)
        if parsed:
            out[normalize_title(parsed["title"])] = parsed
        if i % 10 == 9:
            time.sleep(0.5 + random.uniform(0, 0.2))
    return out


def load_usenix_nsdi_cache(years: list[int]) -> dict[int, dict[str, dict[str, str]]]:
    cache = load_json(USENIX_CACHE_FILE, {"years": {}})
    cached_years = cache.get("years", {})
    changed = False
    for year in sorted(set(years)):
        year_s = str(year)
        if cached_years.get(year_s):
            continue
        print(f"  Fetching USENIX NSDI {year} abstract cache...")
        cached_years[year_s] = fetch_usenix_nsdi_year(year)
        changed = True
        time.sleep(1.0 + random.uniform(0, 0.5))
    if changed:
        save_json(USENIX_CACHE_FILE, {
            "metadata": {
                "description": "USENIX NSDI paper-page abstracts keyed by normalized title.",
                "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            },
            "years": cached_years,
        })
    return {int(year): rows for year, rows in cached_years.items()}


def is_nsdi_paper(paper: dict[str, Any]) -> bool:
    return (paper.get("venue_group") or paper.get("venue")) == "NSDI"


def fetch_usenix_nsdi_by_title(paper: dict[str, Any], cache: dict[int, dict[str, dict[str, str]]]) -> dict[str, str] | None:
    year = int(paper.get("year") or 0)
    if not is_nsdi_paper(paper) or year not in cache:
        return None
    title = paper.get("title", "")
    title_norm = normalize_title(title)
    candidates = cache.get(year, {})
    if title_norm in candidates:
        result = dict(candidates[title_norm])
        result["match_mode"] = "exact_normalized_title"
        result["match_metrics"] = title_match_metrics(title, result.get("title", ""))
        return result
    best: tuple[float, dict[str, str], dict[str, Any]] | None = None
    for source_title_norm, candidate in candidates.items():
        metrics = title_match_metrics(title, candidate.get("title", source_title_norm))
        score = float(metrics["forward_overlap"])
        if best is None or score > best[0]:
            best = (score, candidate, metrics)
    if best and best[0] >= 0.9:
        result = dict(best[1])
        result["match_mode"] = "high_forward_overlap"
        result["match_metrics"] = best[2]
        return result
    return None


def existing_abstract_is_usable(paper: dict[str, Any], record: dict[str, Any]) -> bool:
    if not record.get("abstract"):
        return False
    source = record.get("source", "")
    if source not in {"openalex_title", "semantic_scholar_title"}:
        return True
    source_title = record.get("source_title", "")
    acceptable, metrics = title_match_acceptable(paper.get("title", ""), source_title)
    if acceptable:
        return True
    quarantine_title_match(
        source=source,
        paper_title=paper.get("title", ""),
        source_title=source_title,
        source_doi=record.get("source_doi", ""),
        reason="existing_unsafe_title_match",
        metrics=metrics,
    )
    return False


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

    for work in results:
        source_title = work.get("title") or ""
        acceptable, metrics = title_match_acceptable(title, source_title)
        abstract = reconstruct_abstract(work.get("abstract_inverted_index"))
        if acceptable and abstract:
            return {
                "source": "openalex_title",
                "doi": work.get("doi", ""),
                "title": source_title,
                "abstract": abstract,
                "abstract_truncated": False,
                "match_metrics": metrics,
            }
        if abstract:
            quarantine_title_match(
                source="openalex_title",
                paper_title=title,
                source_title=source_title,
                source_doi=work.get("doi", ""),
                reason="unsafe_title_match",
                metrics=metrics,
            )
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

    for paper in papers:
        source_title = paper.get("title") or ""
        acceptable, metrics = title_match_acceptable(title, source_title)
        abstract = paper.get("abstract") or ""
        if acceptable and abstract:
            return {
                "source": "semantic_scholar_title",
                "doi": "",
                "title": source_title,
                "abstract": abstract,
                "abstract_truncated": len(abstract) > 3000,
                "match_metrics": metrics,
            }
        if abstract:
            quarantine_title_match(
                source="semantic_scholar_title",
                paper_title=title,
                source_title=source_title,
                reason="unsafe_title_match",
                metrics=metrics,
            )
    return None


def fetch_abstract_for_paper(paper: dict[str, Any], stats: dict[str, int], usenix_cache: dict[int, dict[str, dict[str, str]]] | None = None) -> dict[str, str] | None:
    """Try all available strategies to fetch an abstract for a paper."""
    title = paper.get("title", "")
    doi = paper.get("doi", "").strip()
    year = int(paper.get("year") or 0)

    # Strategy 0: USENIX NSDI paper pages. NSDI rows from DBLP usually lack
    # DOI, while USENIX technical-session pages carry abstracts.
    if usenix_cache and is_nsdi_paper(paper):
        stats["attempted_usenix_nsdi"] += 1
        result = fetch_usenix_nsdi_by_title(paper, usenix_cache)
        if result and result.get("abstract"):
            stats["success_usenix_nsdi"] += 1
            return result

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

    # Load existing abstracts
    existing = load_json(OUTPUT_ABSTRACTS, {"abstracts": {}, "metadata": {}})
    abstracts = existing.get("abstracts", {})

    stats = {
        "attempted_oa_doi": 0, "success_oa_doi": 0,
        "attempted_oa_title": 0, "success_oa_title": 0,
        "attempted_s2_doi": 0, "success_s2_doi": 0,
        "attempted_s2_title": 0, "success_s2_title": 0,
        "attempted_usenix_nsdi": 0, "success_usenix_nsdi": 0,
        "not_found": 0, "already_had": 0,
    }

    # Count already-fetched records that still pass current safety checks.
    usable_existing: set[str] = set()
    for p in included:
        existing_record = abstracts.get(p["paper_id"], {})
        if existing_abstract_is_usable(p, existing_record):
            usable_existing.add(p["paper_id"])
            stats["already_had"] += 1

    pending = [p for p in included if p["paper_id"] not in usable_existing]
    print(f"Already have abstracts: {stats['already_had']}")
    print(f"Need to fetch: {len(pending)}")

    nsdi_years = sorted({int(p.get("year") or 0) for p in pending if is_nsdi_paper(p)})
    usenix_cache = load_usenix_nsdi_cache(nsdi_years) if nsdi_years else {}

    checkpoint_interval = 50
    for i, paper in enumerate(pending):
        pid = paper["paper_id"]
        title_short = paper["title"][:70]

        result = fetch_abstract_for_paper(paper, stats, usenix_cache)

        if result:
            abstracts[pid] = {
                "paper_id": pid,
                "abstract": result["abstract"],
                "source": result["source"],
                "source_title": result.get("title", ""),
                "source_doi": result.get("doi", ""),
                "source_url": result.get("url", ""),
                "match_mode": result.get("match_mode", ""),
                "match_metrics": result.get("match_metrics", {}),
            }
            print(f"  [{i+1}/{len(pending)}] OK ({result['source']}): {title_short}")
        else:
            abstracts[pid] = {
                "paper_id": pid,
                "abstract": "",
                "source": "none",
                "source_title": "",
                "source_doi": "",
                "source_url": "",
                "match_mode": "",
                "match_metrics": {},
            }
            print(f"  [{i+1}/{len(pending)}] NO ABSTRACT: {title_short}")

        # Checkpoint
        if (i + 1) % checkpoint_interval == 0:
            found = sum(1 for a in abstracts.values() if a.get("abstract"))
            total_done = stats["already_had"] + i + 1
            output = {
                "metadata": {
                    "description": "Fetched paper abstracts for networking paper classification.",
                    "sources": ["usenix_nsdi_page", "openalex", "semantic_scholar"],
                    "total_papers_processed": total_done,
                    "abstracts_found": found,
                    "abstracts_not_found": max(total_done - found, 0),
                    "fetch_date": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                },
                "abstracts": dict(sorted(abstracts.items())),
            }
            save_json(OUTPUT_ABSTRACTS, output)
            save_title_match_quarantine()
            print(f"  [checkpoint {total_done}/{len(included)}] saved; {found} have abstracts")

    # Final save
    found = sum(1 for a in abstracts.values() if a.get("abstract"))
    output = {
        "metadata": {
            "description": "Fetched paper abstracts for networking paper classification.",
            "sources": ["usenix_nsdi_page", "openalex", "semantic_scholar"],
            "total_papers_processed": len(included),
            "abstracts_found": found,
            "abstracts_not_found": len(included) - found,
            "fetch_date": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "stats": stats,
        },
        "abstracts": dict(sorted(abstracts.items())),
    }
    save_json(OUTPUT_ABSTRACTS, output)
    save_title_match_quarantine()
    print(f"\nDone. Wrote {OUTPUT_ABSTRACTS}")
    print(f"Abstracts found: {found}/{len(included)} ({found/len(included)*100:.1f}%)")
    for k, v in sorted(stats.items()):
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
