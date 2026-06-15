#!/usr/bin/env python3
"""Publication inclusion and deduplication rules for the migration analysis."""

from __future__ import annotations

import re
from typing import Any


EXCLUDED_RECORD_TYPES = {
    "article",
    "proceedings",
    "book",
    "incollection",
    "phdthesis",
    "mastersthesis",
    "www",
    "data",
}

INCLUDED_RECORD_TYPES = {"inproceedings"}
EXCLUDED_VENUES = {"CoRR"}
PROCEEDINGS_TITLE_RE = re.compile(r"^\s*proceedings\s+of\b", re.IGNORECASE)
CONF_VOLUME_WORD_RE = re.compile(r"\b(proceedings|conference|symposium|workshop)\b", re.IGNORECASE)
CONF_VOLUME_YEAR_RE = re.compile(r"\b(20\d{2}|'\d{2})\b")
ACRONYM_VOLUME_RE = re.compile(r"^\s*[A-Z][A-Za-z0-9&.+ -]+\s+'\d{2}:")
SPACE_RE = re.compile(r"\s+")
PUNCT_RE = re.compile(r"[^\w\s]", re.UNICODE)


def normalize_title(title: str) -> str:
    """Normalize title text for fallback identity matching."""
    title = title.casefold().strip()
    title = PUNCT_RE.sub(" ", title)
    title = SPACE_RE.sub(" ", title)
    return title


def canonical_publication_id(paper: dict[str, Any]) -> str:
    """
    Return a stable publication identity.

    DBLP key is preferred. DOI is second best. Title/year/venue is a fallback for
    older cached data that predates storing the DBLP key.
    """
    key = paper.get("dblp_key") or paper.get("key")
    if key:
        return f"dblp:{key}"

    doi = paper.get("doi") or ""
    if doi:
        return f"doi:{doi.strip().lower()}"

    title = normalize_title(paper.get("title", ""))
    year = paper.get("year", "")
    venue = (paper.get("venue") or "").strip().casefold()
    return f"title:{title}|year:{year}|venue:{venue}"


def looks_like_proceedings_volume(paper: dict[str, Any]) -> bool:
    """Heuristic for DBLP proceedings-volume records stored as inproceedings."""
    title = paper.get("title", "") or ""
    authors = paper.get("authors") or []
    if authors:
        return False
    if PROCEEDINGS_TITLE_RE.search(title):
        return True
    if ACRONYM_VOLUME_RE.search(title):
        return True
    return bool(CONF_VOLUME_WORD_RE.search(title) and CONF_VOLUME_YEAR_RE.search(title))


def exclusion_reason(paper: dict[str, Any]) -> str | None:
    """Return an exclusion reason, or None when the record is in scope."""
    venue = (paper.get("venue") or "").strip()
    title = paper.get("title", "")
    record_type = (paper.get("record_type") or "").strip().lower()

    if paper.get("is_journal"):
        return "journal_article"
    if record_type in EXCLUDED_RECORD_TYPES:
        return f"record_type:{record_type}"
    if record_type and record_type not in INCLUDED_RECORD_TYPES:
        return f"record_type:{record_type}"
    if not venue:
        return "missing_venue"
    if venue in EXCLUDED_VENUES:
        return f"venue:{venue}"
    if looks_like_proceedings_volume(paper):
        return "proceedings_volume"

    return None


def annotate_scope(paper: dict[str, Any]) -> dict[str, Any]:
    """Mutate and return a paper with analysis inclusion metadata."""
    reason = exclusion_reason(paper)
    paper["analysis_id"] = canonical_publication_id(paper)
    paper["included_in_analysis"] = reason is None
    paper["exclusion_reason"] = reason
    return paper
