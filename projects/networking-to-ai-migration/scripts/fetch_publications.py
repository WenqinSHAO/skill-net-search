#!/usr/bin/env python3
"""
Phase 2: Fetch full publication history for each qualified researcher.

Reads data/qualified_cohort.json, queries DBLP for each researcher's complete
publication record (2018–2026), and saves enriched data.

Uses DBLP's author PID endpoint (XML) for efficiency — one request per author
gives all publications.

Output: data/publication_history.json
  For each researcher: {dblp_pid, name, papers: [{title, venue, year, dblp_url, doi, coauthors}]}
"""

import json
import time
import sys
import random
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path
from collections import defaultdict
from publication_scope import annotate_scope

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

OBSERVATION_START = 2018
OBSERVATION_END = 2026

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
INPUT_FILE = DATA_DIR / "qualified_cohort.json"
OUTPUT_FILE = DATA_DIR / "publication_history.json"
PROGRESS_FILE = DATA_DIR / "fetch_publications_progress.json"

BASE_DELAY = 3.0
JITTER = 2.0
MAX_RETRIES = 5
BACKOFF_BASE = 10


# ---------------------------------------------------------------------------
# HTTP client
# ---------------------------------------------------------------------------

def curl_fetch(url: str, timeout: int = 60) -> bytes:
    """Fetch a URL using curl. Returns raw bytes on success."""
    cmd = [
        "curl", "-s", "-S",
        "--max-time", str(timeout),
        "--connect-timeout", "15",
        "-H", "Accept: application/xml, text/xml",
        "-H", "User-Agent: networking-to-ai-migration/1.0 (academic research)",
        url,
    ]
    result = subprocess.run(cmd, capture_output=True, timeout=timeout + 10)
    if result.returncode != 0:
        stderr = result.stderr.decode("utf-8", errors="replace").strip()
        raise OSError(f"curl exited {result.returncode}: {stderr}")
    return result.stdout


def fetch_author_publications_xml(pid: str) -> str:
    """Fetch an author's full publication list from DBLP PID endpoint (XML)."""
    url = f"https://dblp.org/pid/{pid}.xml"

    for attempt in range(MAX_RETRIES):
        try:
            raw = curl_fetch(url, timeout=90)
            return raw.decode("utf-8", errors="replace")
        except (OSError, UnicodeDecodeError) as e:
            wait = BACKOFF_BASE * (2 ** attempt) + random.uniform(0, 3)
            print(f"  Attempt {attempt+1}/{MAX_RETRIES} for PID {pid}: {e}",
                  file=sys.stderr)
            print(f"  Waiting {wait:.0f}s...", file=sys.stderr)
            time.sleep(wait)

    raise RuntimeError(f"Failed to fetch PID {pid} after {MAX_RETRIES} retries")


# ---------------------------------------------------------------------------
# XML parsing
# ---------------------------------------------------------------------------

# DBLP XML namespace
NS = {"dblp": "https://dblp.org/dtd/dblp.dtd"}


def parse_author_xml(xml_str: str) -> list[dict]:
    """
    Parse DBLP author PID XML and extract publications.

    DBLP PID XML format:
    <dblpperson>
      <r>  <!-- each <r> is a publication -->
        <inproceedings key="conf/sigcomm/..." mdate="2022-08-15">
          <author>...</author>
          <title>...</title>
          <year>2022</year>
          <booktitle>...</booktitle>
          <ee>https://doi.org/...</ee>
          ...
        </inproceedings>
      </r>
      ...
    </dblpperson>
    """
    # Strip namespaces for easier parsing — DBLP XML may or may not have them
    # Remove default namespace declaration
    xml_str = xml_str.replace('xmlns="https://dblp.org/dtd/dblp.dtd"', "")
    xml_str = xml_str.replace("xmlns:mml", "xmlns:mml-ignore")
    xml_str = xml_str.replace("xmlns:xlink", "xmlns:xlink-ignore")

    # Try to parse with and without namespace stripping
    try:
        root = ET.fromstring(xml_str)
    except ET.ParseError:
        # If XML has issues, try more aggressive cleaning
        xml_str_clean = xml_str.encode("utf-8", errors="replace").decode("utf-8")
        root = ET.fromstring(xml_str_clean)

    publications = []

    # Find all publication elements inside <r> tags
    pub_tags = {"inproceedings", "article", "proceedings", "book", "incollection",
                "phdthesis", "mastersthesis", "www", "data"}

    for r_elem in root.iter("r"):
        for child in r_elem:
            tag = child.tag.lower()
            if tag not in pub_tags:
                continue

            pub = _parse_publication(child)
            if pub:
                # Filter to observation window
                year = pub.get("year", 0)
                if OBSERVATION_START <= year <= OBSERVATION_END:
                    publications.append(pub)

    return publications


def _parse_publication(elem: ET.Element) -> dict | None:
    """Parse a single DBLP publication element."""
    try:
        record_type = elem.tag.lower()
        title = ""
        venue = ""
        year = 0
        dblp_url = ""
        doi = ""
        authors = []
        ee_list = []

        title_el = elem.find("title")
        if title_el is not None and title_el.text:
            title = title_el.text.rstrip(".")

        year_el = elem.find("year")
        if year_el is not None and year_el.text:
            try:
                year = int(year_el.text)
            except ValueError:
                year = 0

        # Venue from booktitle (conferences) or journal (articles)
        booktitle_el = elem.find("booktitle")
        journal_el = elem.find("journal")
        if booktitle_el is not None and booktitle_el.text:
            venue = booktitle_el.text
        elif journal_el is not None and journal_el.text:
            venue = journal_el.text

        # Authors
        for author_el in elem.findall("author"):
            if author_el.text:
                # DBLP author text may include disambiguation number
                authors.append(author_el.text)

        # URLs
        dblp_key = elem.get("key", "")
        if dblp_key:
            dblp_url = f"https://dblp.org/rec/{dblp_key}"

        for ee_el in elem.findall("ee"):
            if ee_el.text:
                ee_list.append(ee_el.text)
                # Prefer DOI URLs
                if "doi.org" in ee_el.text and not doi:
                    doi = ee_el.text

        # If no DOI from ee, check dedicated doi element
        if not doi:
            doi_el = elem.find("doi")
            if doi_el is not None and doi_el.text:
                doi = doi_el.text

        if not title:
            return None

        return annotate_scope({
            "dblp_key": dblp_key,
            "record_type": record_type,
            "title": title,
            "venue": venue,
            "year": year,
            "dblp_url": dblp_url,
            "doi": doi,
            "ee": ee_list,
            "authors": authors,
            "is_journal": record_type == "article",
        })

    except Exception as e:
        print(f"  Warning: failed to parse publication element: {e}",
              file=sys.stderr)
        return None


# ---------------------------------------------------------------------------
# Progress tracking
# ---------------------------------------------------------------------------

def load_progress() -> set[str]:
    """Load set of already-fetched PIDs."""
    if PROGRESS_FILE.exists():
        with open(PROGRESS_FILE) as f:
            return set(json.load(f))
    return set()


def save_progress(pids_done: set[str]):
    """Save progress to disk."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(PROGRESS_FILE, "w") as f:
        json.dump(sorted(pids_done), f)


def load_existing_results() -> dict[str, dict]:
    """Load previously saved publication history."""
    if OUTPUT_FILE.exists():
        with open(OUTPUT_FILE) as f:
            data = json.load(f)
            return {r["dblp_pid"]: r for r in data.get("researchers", [])}
    return {}


def save_results(researchers: list[dict], metadata: dict):
    """Save all results to output file."""
    output = {
        "metadata": metadata,
        "researchers": sorted(researchers, key=lambda r: r.get("total_papers", 0), reverse=True),
    }
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def run():
    """Run the full Phase 2 pipeline."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # Load qualified cohort
    if not INPUT_FILE.exists():
        print(f"ERROR: {INPUT_FILE} not found. Run Phase 1 first.",
              file=sys.stderr)
        sys.exit(1)

    with open(INPUT_FILE) as f:
        cohort_data = json.load(f)

    researchers = cohort_data.get("researchers", [])
    print("=" * 60)
    print("Phase 2: Fetch Full Publication History")
    print("=" * 60)
    print(f"Researchers to process: {len(researchers)}")
    print(f"Observation window: {OBSERVATION_START}–{OBSERVATION_END}")
    print()

    # Resume state
    done_pids = load_progress()
    existing_results = load_existing_results()
    print(f"Already fetched: {len(done_pids)} researchers")
    print(f"Remaining: {len(researchers) - len(done_pids)}")
    print()

    results = list(existing_results.values())
    processed = 0
    errors = 0

    for i, researcher in enumerate(researchers):
        pid = researcher["dblp_pid"]

        if pid in done_pids:
            continue

        name = researcher["name"]
        print(f"[{i+1}/{len(researchers)}] {name} (PID: {pid})", flush=True)

        try:
            xml_str = fetch_author_publications_xml(pid)
            papers = parse_author_xml(xml_str)

            result = {
                "dblp_pid": pid,
                "name": name,
                "cohort_paper_count": researcher["paper_count"],
                "cohort_rank": researcher["rank"],
                "total_papers": len(papers),
                "papers": sorted(papers, key=lambda p: (p["year"], p.get("venue", ""))),
            }
            results.append(result)

            done_pids.add(pid)
            processed += 1

            # Save progress periodically (every 10 researchers)
            if processed % 10 == 0:
                save_progress(done_pids)
                save_results(results, {
                    "phase": "fetch_publications",
                    "observation_start": OBSERVATION_START,
                    "observation_end": OBSERVATION_END,
                    "total_researchers_in_cohort": len(researchers),
                    "researchers_processed": len(done_pids),
                })
                print(f"  → {len(papers)} papers (checkpoint saved)", flush=True)
            else:
                print(f"  → {len(papers)} papers", flush=True)

        except RuntimeError as e:
            print(f"  ERROR: {e}", file=sys.stderr)
            errors += 1
            if errors > 10:
                print("  Too many errors. Aborting.", file=sys.stderr)
                break

        # Polite delay
        time.sleep(BASE_DELAY + random.uniform(0, JITTER))

    # Final save
    save_progress(done_pids)
    save_results(results, {
        "phase": "fetch_publications",
        "observation_start": OBSERVATION_START,
        "observation_end": OBSERVATION_END,
        "total_researchers_in_cohort": len(researchers),
        "researchers_processed": len(done_pids),
        "errors": errors,
    })

    print(f"\nOutput saved to {OUTPUT_FILE}")
    print(f"Processed: {processed}, Errors: {errors}")
    print(f"Total researchers with history: {len(results)}")

    # Quick stats
    total_pubs = sum(r["total_papers"] for r in results)
    print(f"Total publications fetched: {total_pubs}")


if __name__ == "__main__":
    run()
