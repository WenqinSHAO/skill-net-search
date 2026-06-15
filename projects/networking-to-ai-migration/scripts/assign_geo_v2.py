#!/usr/bin/env python3
"""
Phase 4 (v2): Assign geographic regions to researchers using OpenAlex API.

OpenAlex provides author disambiguation and institution data with country codes.
Free tier: 100k calls/day with polite mailto parameter.

Strategy:
  1. Search OpenAlex by author name
  2. Pick best match (highest works_count as tiebreaker)
  3. Extract country_code from last_known_institutions
  4. Map country_code → region (US, Europe, China, Other)

Reads: data/publication_history_zones.json
Writes: data/publication_history_geo.json (same structure + region/institution fields)
"""

import json
import sys
import time
import random
import subprocess
from pathlib import Path
from collections import Counter
from urllib.parse import urlencode, quote

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
INPUT_FILE = DATA_DIR / "publication_history_zones.json"
OUTPUT_FILE = DATA_DIR / "publication_history_geo.json"
PROGRESS_FILE = DATA_DIR / "geo_openalex_progress.json"

OPENALEX_AUTHOR_SEARCH = "https://api.openalex.org/authors"
MAILTO = "research@example.com"
BASE_DELAY = 0.5   # OpenAlex is fast, polite pool allows higher rates
JITTER = 0.3
MAX_RETRIES = 3
BACKOFF_BASE = 5

# Country code → Region
# Europe includes EU/EFTA/UK/CH/IL (Israel often grouped with European CS research)
EUROPE_CODES = {
    "GB", "DE", "FR", "IT", "ES", "NL", "BE", "CH", "SE", "NO", "DK",
    "FI", "AT", "IE", "PT", "GR", "PL", "CZ", "HU", "RO", "BG", "HR",
    "SI", "SK", "EE", "LV", "LT", "LU", "MT", "CY", "IS", "LI",
    "RU", "UA", "BY", "RS", "TR", "IL",
}
US_CODES = {"US"}
CHINA_CODES = {"CN", "HK", "TW", "MO"}

# Manual overrides for researchers where OpenAlex gets it wrong
# (name → {affiliation, country_code, region})
MANUAL_OVERRIDES = {
    # Add known cases where OpenAlex data is stale or wrong
    "Marco Chiesa": {"affiliation": "KTH Royal Institute of Technology", "country_code": "SE", "region": "Europe"},
}


def country_to_region(country_code: str) -> str:
    """Map ISO country code to region."""
    cc = country_code.upper().strip()
    if cc in US_CODES:
        return "US"
    if cc in EUROPE_CODES:
        return "Europe"
    if cc in CHINA_CODES:
        return "China"
    return "Other"


# ---------------------------------------------------------------------------
# OpenAlex client
# ---------------------------------------------------------------------------

def curl_fetch(url: str, timeout: int = 30) -> bytes:
    """Fetch URL using curl."""
    cmd = [
        "curl", "-s", "-S",
        "--max-time", str(timeout),
        "--connect-timeout", "10",
        "-H", "Accept: application/json",
        "-H", "User-Agent: networking-to-ai-migration/1.0 (mailto:research@example.com)",
        url,
    ]
    result = subprocess.run(cmd, capture_output=True, timeout=timeout + 10)
    if result.returncode != 0:
        raise OSError(f"curl exited {result.returncode}")
    return result.stdout


def search_author_openalex(name: str) -> dict | None:
    """
    Search OpenAlex for an author by name.
    Returns the best-matching author record or None.
    """
    # Clean name — remove DBLP disambiguation number suffix
    clean_name = name
    # Remove trailing 4-digit disambiguation (e.g., "Xin Jin 0008")
    import re
    clean_name = re.sub(r'\s+\d{4}$', '', name)

    params = {
        "search": clean_name,
        "per_page": "5",
        "mailto": MAILTO,
    }
    url = f"{OPENALEX_AUTHOR_SEARCH}?{urlencode(params)}"

    for attempt in range(MAX_RETRIES):
        try:
            raw = curl_fetch(url)
            data = json.loads(raw)
            if data is None:
                return None  # OpenAlex returned null
            results = data.get("results") or []  # handle {"results": null}

            if not results:
                return None

            # Pick best match: highest works_count as proxy for prominence
            # Also prefer exact name match
            best = None
            best_score = -1
            for r in results:
                score = r.get("works_count", 0) + r.get("cited_by_count", 0) / 100
                display = r.get("display_name", "").lower()
                if clean_name.lower() in display:
                    score += 100  # bonus for name match

                # Penalize if institution is a publisher (common OpenAlex artifact)
                insts = r.get("last_known_institutions") or []
                for inst in insts:
                    inst_name = inst.get("display_name", "").lower()
                    if any(kw in inst_name for kw in ["press", "publishing", "publisher"]):
                        score -= 200

                if score > best_score:
                    best_score = score
                    best = r

            time.sleep(BASE_DELAY + random.uniform(0, JITTER))
            return best

        except (OSError, json.JSONDecodeError) as e:
            wait = BACKOFF_BASE * (2 ** attempt) + random.uniform(0, 2)
            print(f"  Retry {attempt+1}/{MAX_RETRIES} for '{name}': {e}",
                  file=sys.stderr)
            time.sleep(wait)

    return None


def extract_geo_from_openalex(author_data: dict) -> dict:
    """Extract affiliation, country, and region from an OpenAlex author record."""
    insts = author_data.get("last_known_institutions") or []
    affiliation = None
    country_code = None
    region = "Unknown"

    if insts:
        inst = insts[0]
        affiliation = inst.get("display_name", "")
        country_code = inst.get("country_code", "")

    if country_code:
        region = country_to_region(country_code)

    return {
        "affiliation": affiliation,
        "country_code": country_code.upper() if country_code else None,
        "region": region,
        "source": "openalex",
    }


# ---------------------------------------------------------------------------
# Progress tracking
# ---------------------------------------------------------------------------

def load_progress() -> dict[str, dict]:
    """Load already-resolved geo data."""
    if PROGRESS_FILE.exists():
        with open(PROGRESS_FILE) as f:
            return json.load(f)
    return {}


def save_progress(progress: dict):
    """Save geo progress to disk."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=2)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def run():
    """Run improved Phase 4: assign regions via OpenAlex."""
    if not INPUT_FILE.exists():
        print(f"ERROR: {INPUT_FILE} not found.", file=sys.stderr)
        sys.exit(1)

    with open(INPUT_FILE) as f:
        data = json.load(f)

    researchers = data.get("researchers", [])
    progress = load_progress()

    print("=" * 60)
    print("Phase 4 (v2): Assign Regions via OpenAlex")
    print("=" * 60)
    print(f"Researchers to process: {len(researchers)}")
    print(f"Already resolved: {len(progress)}")
    print()

    region_counts = Counter()
    unknown_count = 0
    resolved_count = len(progress)

    for i, researcher in enumerate(researchers):
        pid = researcher.get("dblp_pid", "")
        name = researcher.get("name", "")

        # Check progress — only skip if we have a real region assigned
        if pid in progress and progress[pid].get("region") != "Unknown":
            geo = progress[pid]
            researcher.update(geo)
            region_counts[geo.get("region", "Unknown")] += 1
            continue

        # Check manual overrides
        if name in MANUAL_OVERRIDES:
            geo = MANUAL_OVERRIDES[name]
            geo["source"] = "manual"
            geo["country_code"] = geo.get("country_code", "")
            print(f"[{i+1}/{len(researchers)}] {name} → {geo['affiliation']} ({geo['region']}) [manual]")
        else:
            print(f"[{i+1}/{len(researchers)}] {name}", end="", flush=True)

            try:
                author_data = search_author_openalex(name)
            except Exception as e:
                print(f" → ERROR: {e}")
                author_data = None

            if author_data:
                geo = extract_geo_from_openalex(author_data)
                if geo["region"] == "Unknown":
                    unknown_count += 1
                    print(f" → {geo['affiliation'] or '?'} → Unknown")
                else:
                    resolved_count += 1
                    print(f" → {geo['affiliation']} ({geo['region']})")
            else:
                geo = {
                    "affiliation": None,
                    "country_code": None,
                    "region": "Unknown",
                    "source": None,
                }
                unknown_count += 1
                print(f" → No OpenAlex match")

        researcher.update(geo)
        region_counts[geo.get("region", "Unknown")] += 1

        # Save progress
        progress[pid] = {
            "affiliation": geo.get("affiliation"),
            "country_code": geo.get("country_code"),
            "region": geo.get("region"),
            "source": geo.get("source"),
        }

        # Save periodically
        if (i + 1) % 20 == 0:
            save_progress(progress)
            # Also save intermediate output
            output = {
                "metadata": {
                    "phase": "assign_geo_v2",
                    "total_researchers": len(researchers),
                    "resolved": resolved_count,
                    "unknown": unknown_count,
                    "region_counts": dict(region_counts),
                },
                "researchers": researchers,
            }
            DATA_DIR.mkdir(parents=True, exist_ok=True)
            with open(OUTPUT_FILE, "w") as f:
                json.dump(output, f, indent=2, ensure_ascii=False)
            print(f"  [checkpoint at {i+1}/{len(researchers)}]", flush=True)

        # Longer delay every 20 to stay in polite pool
        if (i + 1) % 50 == 0:
            time.sleep(2.0)

    # Final save
    save_progress(progress)

    output = {
        "metadata": {
            "phase": "assign_geo_v2",
            "total_researchers": len(researchers),
            "resolved": resolved_count,
            "unknown": unknown_count,
            "region_counts": dict(region_counts),
        },
        "researchers": researchers,
    }

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\nOutput saved to {OUTPUT_FILE}")
    print(f"\nRegion distribution:")
    for region in ["US", "Europe", "China", "Other", "Unknown"]:
        count = region_counts[region]
        pct = 100 * count / len(researchers) if researchers else 0
        print(f"  {region}: {count:4d} ({pct:5.1f}%)")

    print(f"\nResolved: {resolved_count}, Unknown: {unknown_count} "
          f"({100*unknown_count/len(researchers):.1f}%)")


if __name__ == "__main__":
    run()
