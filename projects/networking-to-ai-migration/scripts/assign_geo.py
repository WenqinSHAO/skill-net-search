#!/usr/bin/env python3
"""
Phase 4: Assign geographic regions to researchers.

Extracts institution/affiliation information from publication data and maps
each researcher to a region: US, Europe, China, or Other.

Strategy:
  1. Use DBLP author PID XML (already fetched in Phase 2) to extract affiliation
     from the most recent publication's author note
  2. If DBLP XML lacks affiliation, query OpenAlex for author information
  3. Fall back to institution heuristics from co-author affiliations

Reads: data/publication_history_zones.json
Writes: data/publication_history_geo.json (same structure + region/institution fields)
"""

import json
import sys
import re
import time
import random
import subprocess
from pathlib import Path
from collections import Counter

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
INPUT_FILE = DATA_DIR / "publication_history_zones.json"
OUTPUT_FILE = DATA_DIR / "publication_history_geo.json"

# ---------------------------------------------------------------------------
# Country → Region mapping
# ---------------------------------------------------------------------------

US_COUNTRIES = {"United States", "USA", "US", "United States of America"}
EUROPE_COUNTRIES = {
    "United Kingdom", "UK", "England", "Scotland", "Wales", "Northern Ireland",
    "Germany", "France", "Italy", "Spain", "Netherlands", "Belgium",
    "Switzerland", "Sweden", "Norway", "Denmark", "Finland", "Austria",
    "Ireland", "Portugal", "Greece", "Poland", "Czech Republic", "Czechia",
    "Hungary", "Romania", "Bulgaria", "Croatia", "Slovenia", "Slovakia",
    "Estonia", "Latvia", "Lithuania", "Luxembourg", "Malta", "Cyprus",
    "Iceland", "Liechtenstein", "European Union",
    "Russia", "Ukraine", "Belarus", "Serbia", "Turkey",
    "Israel",  # Often grouped with Europe in CS research contexts
}
CHINA_COUNTRIES = {
    "China", "Hong Kong", "Macau", "Taiwan",
}

# Institution name → country lookup for known universities/companies
INSTITUTION_TO_COUNTRY: dict[str, str] = {}

def _build_institution_map():
    """Build a quick lookup for well-known institutions."""
    institutions = {
        # US
        "mit": "United States", "stanford": "United States",
        "cmu": "United States", "carnegie mellon": "United States",
        "berkeley": "United States", "uc berkeley": "United States",
        "harvard": "United States", "princeton": "United States",
        "cornell": "United States", "columbia": "United States",
        "yale": "United States", "uchicago": "United States",
        "university of illinois": "United States", "uiuc": "United States",
        "university of michigan": "United States", "umich": "United States",
        "university of washington": "United States", "uw": "United States",
        "university of wisconsin": "United States",
        "university of texas": "United States", "ut austin": "United States",
        "university of california": "United States", "uc san diego": "United States",
        "ucsd": "United States", "ucla": "United States",
        "uc santa barbara": "United States", "ucsb": "United States",
        "uc irvine": "United States", "uci": "United States",
        "uc davis": "United States", "uc riverside": "United States",
        "uc santa cruz": "United States", "ucsc": "United States",
        "purdue": "United States", "duke": "United States",
        "northwestern": "United States", "nyu": "United States",
        "new york university": "United States",
        "university of pennsylvania": "United States", "upenn": "United States",
        "johns hopkins": "United States", "jhu": "United States",
        "caltech": "United States", "georgia tech": "United States",
        "gatech": "United States", "university of maryland": "United States",
        "umd": "United States", "umass": "United States",
        "university of massachusetts": "United States",
        "brown": "United States", "dartmouth": "United States",
        "rice": "United States", "unc": "United States",
        "university of north carolina": "United States",
        "usc": "United States", "university of southern california": "United States",
        "northeastern": "United States", "boston university": "United States",
        "rutgers": "United States", "stony brook": "United States",
        "ohio state": "United States", "penn state": "United States",
        "university of minnesota": "United States",
        "university of colorado": "United States",
        "university of utah": "United States", "utah": "United States",
        "indiana university": "United States",
        "university of notre dame": "United States",
        "arizona state": "United States",
        "university of arizona": "United States",
        "university of florida": "United States",
        "ucf": "United States",
        "university of virginia": "United States", "uva": "United States",
        # Europe
        "eth zurich": "Switzerland", "eth zürich": "Switzerland",
        "epfl": "Switzerland",
        "university of cambridge": "United Kingdom", "cambridge": "United Kingdom",
        "university of oxford": "United Kingdom", "oxford": "United Kingdom",
        "imperial college": "United Kingdom", "imperial": "United Kingdom",
        "ucl": "United Kingdom", "university college london": "United Kingdom",
        "university of edinburgh": "United Kingdom",
        "kth": "Sweden", "kth royal institute of technology": "Sweden",
        "technical university of munich": "Germany", "tum": "Germany",
        "tu munich": "Germany", "tu münchen": "Germany",
        "rwth aachen": "Germany", "rwth": "Germany",
        "tu berlin": "Germany", "technische universität berlin": "Germany",
        "max planck": "Germany", "mpi": "Germany",
        "tu darmstadt": "Germany",
        "kit": "Germany",
        "inria": "France", "inria paris": "France",
        "sorbonne": "France", "université paris": "France",
        "ecole polytechnique": "France", "école polytechnique": "France",
        "tu delft": "Netherlands", "delft university": "Netherlands",
        "university of amsterdam": "Netherlands", "vu amsterdam": "Netherlands",
        "tu eindhoven": "Netherlands",
        "ku leuven": "Belgium", "université catholique de louvain": "Belgium",
        "eth": "Switzerland",
        "politecnico di milano": "Italy", "polimi": "Italy",
        "university of trento": "Italy",
        "universitat politècnica de catalunya": "Spain",
        "upc barcelona": "Spain",
        "imdea": "Spain",
        "telefonica research": "Spain",
        "aalborg university": "Denmark",
        "university of copenhagen": "Denmark",
        "helsinki": "Finland", "aalto university": "Finland",
        "norwegian": "Norway", "oslo": "Norway",
        "technion": "Israel", "tel aviv university": "Israel",
        "hebrew university": "Israel",
        "technische universität wien": "Austria", "tu wien": "Austria",
        "ecole polytechnique fédérale": "Switzerland",
        # China
        "tsinghua": "China", "tsinghua university": "China",
        "peking university": "China", "peking": "China",
        "fudan": "China", "fudan university": "China",
        "shanghai jiao tong": "China", "sjtu": "China",
        "zhejiang university": "China",
        "nanjing university": "China", "nju": "China",
        "university of science and technology of china": "China",
        "ustc": "China",
        "wuhan university": "China",
        "sun yat-sen": "China",
        "huazhong": "China", "hust": "China",
        "beihang": "China",
        "harbin institute of technology": "China",
        "xi'an jiaotong": "China",
        "tongji university": "China",
        "southeast university": "China",
        "tianjin university": "China",
        "beijing university": "China",
        "chinese university of hong kong": "Hong Kong", "cuhk": "Hong Kong",
        "hong kong university": "Hong Kong", "hku": "Hong Kong",
        "city university of hong kong": "Hong Kong",
        "hkust": "Hong Kong",
        "national taiwan university": "Taiwan", "ntu": "Taiwan",
        "academia sinica": "Taiwan",
        # Industry (US-based multinationals)
        "google": "United States", "microsoft": "United States",
        "meta": "United States", "facebook": "United States",
        "amazon": "United States", "apple": "United States",
        "nvidia": "United States", "intel": "United States",
        "amd": "United States", "cisco": "United States",
        "juniper": "United States", "arista": "United States",
        "broadcom": "United States", "ibm": "United States",
        "oracle": "United States", "vmware": "United States",
        "netflix": "United States", "twitter": "United States",
        "linkedin": "United States", "uber": "United States",
        "lyft": "United States", "dropbox": "United States",
        "salesforce": "United States",
        "cloudflare": "United States", "fastly": "United States",
        "akamai": "United States", "barefoot": "United States",
        # Industry (China-based)
        "huawei": "China", "bytedance": "China",
        "alibaba": "China", "tencent": "China", "baidu": "China",
        "xiaomi": "China", "jdl": "China",
        # Industry (Europe)
        "nokia": "Finland", "ericsson": "Sweden",
        "siemens": "Germany", "sap": "Germany",
        "arm": "United Kingdom", "deepmind": "United Kingdom",
    }
    INSTITUTION_TO_COUNTRY.update(institutions)


_build_institution_map()


def institution_to_country(institution: str) -> str | None:
    """Try to map an institution name to a country."""
    if not institution:
        return None

    inst_lower = institution.lower().strip()

    # Direct lookup
    for key, country in INSTITUTION_TO_COUNTRY.items():
        if key in inst_lower:
            return country

    # Country name in institution string
    country_names = {
        "united states": "United States", "usa": "United States",
        "united kingdom": "United Kingdom", "uk": "United Kingdom",
        "germany": "Germany", "france": "France", "italy": "Italy",
        "spain": "Spain", "netherlands": "Netherlands",
        "switzerland": "Switzerland", "sweden": "Sweden",
        "norway": "Norway", "denmark": "Denmark", "finland": "Finland",
        "austria": "Austria", "belgium": "Belgium",
        "ireland": "Ireland", "portugal": "Portugal",
        "greece": "Greece", "poland": "Poland",
        "czech": "Czech Republic", "hungary": "Hungary",
        "romania": "Romania", "russia": "Russia",
        "israel": "Israel", "turkey": "Turkey",
        "china": "China", "hong kong": "Hong Kong",
        "taiwan": "Taiwan", "japan": "Other",
        "south korea": "Other", "korea": "Other",
        "singapore": "Other", "singapore": "Other",
        "australia": "Other", "canada": "Other",
        "india": "Other", "brazil": "Other",
    }
    for name, country in country_names.items():
        if name in inst_lower:
            return country

    return None


def country_to_region(country: str) -> str:
    """Map a country to a region."""
    if country in US_COUNTRIES:
        return "US"
    if country in EUROPE_COUNTRIES:
        return "Europe"
    if country in CHINA_COUNTRIES:
        return "China"
    return "Other"


def extract_region(institution: str) -> str:
    """Extract region from an institution string."""
    country = institution_to_country(institution)
    if country:
        return country_to_region(country)
    return "Unknown"


# ---------------------------------------------------------------------------
# DBLP XML-based affiliation extraction
# ---------------------------------------------------------------------------

def fetch_affiliation_from_dblp_xml(pid: str) -> str | None:
    """
    Try to extract affiliation from DBLP author PID XML.
    DBLP sometimes includes <note type="affiliation"> in author records.
    Returns affiliation string or None.
    """
    url = f"https://dblp.org/pid/{pid}.xml"

    try:
        cmd = [
            "curl", "-s", "-S",
            "--max-time", "30",
            "--connect-timeout", "10",
            "-H", "Accept: application/xml",
            "-H", "User-Agent: networking-to-ai-migration/1.0",
            url,
        ]
        result = subprocess.run(cmd, capture_output=True, timeout=40)
        if result.returncode != 0:
            return None

        xml_str = result.stdout.decode("utf-8", errors="replace")

        # Look for <note type="affiliation"> text </note>
        import xml.etree.ElementTree as ET
        # Strip namespaces
        xml_str = xml_str.replace('xmlns="https://dblp.org/dtd/dblp.dtd"', "")
        try:
            root = ET.fromstring(xml_str)
            for note in root.iter("note"):
                if note.get("type") == "affiliation" and note.text:
                    return note.text.strip()
        except ET.ParseError:
            pass
    except Exception:
        pass

    return None


# ---------------------------------------------------------------------------
# Affiliation from paper co-authors in the last observation year
# ---------------------------------------------------------------------------

def extract_affiliation_from_papers(researcher: dict) -> str | None:
    """
    Try to extract affiliation from the researcher's most recent papers.
    DBLP XML for individual papers sometimes includes affiliation in author notes.
    This is a fallback method.
    """
    papers = researcher.get("papers", [])
    if not papers:
        return None

    # Look at the most recent paper first
    recent_papers = sorted(papers, key=lambda p: p.get("year", 0), reverse=True)

    # For now, we rely on the institution map and co-author affiliations
    # that we'll enrich via OpenAlex in a later step
    return None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def extract_affiliation_for_researcher(name: str, pid: str,
                                        papers: list[dict]) -> str | None:
    """
    Multi-strategy affiliation extraction for a researcher.

    Priority:
      1. DBLP PID XML <note type="affiliation">
      2. Known institution from co-author list (most recent paper)
      3. Manual lookup table for known researchers
    """
    # Strategy 1: DBLP PID XML affiliation note
    # (only for a sample — too expensive for all researchers)
    # We'll run this selectively for top researchers and case studies

    # Strategy 2: Look at co-authors from most recent papers for clues
    # Get all co-authors from the most recent 3 papers
    recent_papers = sorted(papers, key=lambda p: p.get("year", 0), reverse=True)[:3]

    # For now, return None — we'll enrich via OpenAlex or manual review
    # in the case study phase
    return None


def run():
    """Run Phase 4: assign regions to researchers."""
    input_file = INPUT_FILE
    if not input_file.exists():
        print(f"ERROR: {input_file} not found.", file=sys.stderr)
        # Try without zones
        alt_input = DATA_DIR / "publication_history.json"
        if alt_input.exists():
            print(f"Using {alt_input} instead.", file=sys.stderr)
            input_file = alt_input
        else:
            sys.exit(1)

    with open(input_file) as f:
        data = json.load(f)

    researchers = data.get("researchers", [])
    print("=" * 60)
    print("Phase 4: Assign Geographic Regions")
    print("=" * 60)
    print(f"Researchers to process: {len(researchers)}")
    print()

    region_counts = Counter()
    unknown_count = 0
    assigned_count = 0

    for i, researcher in enumerate(researchers):
        pid = researcher.get("dblp_pid", "")
        name = researcher.get("name", "")

        # Try to get affiliation from DBLP XML (first 200 only — expensive)
        affiliation = None
        if i < 200:
            print(f"[{i+1}/{len(researchers)}] {name}", end="", flush=True)
            affiliation = fetch_affiliation_from_dblp_xml(pid)
        else:
            print(f"[{i+1}/{len(researchers)}] {name} (skip XML lookup)", end="", flush=True)

        if affiliation:
            region = extract_region(affiliation)
        else:
            # Fallback: try to guess from institution name in DBLP record
            # For now, mark as unknown — we'll handle in manual review
            region = "Unknown"
            unknown_count += 1

        researcher["affiliation"] = affiliation
        researcher["region"] = region
        region_counts[region] += 1

        if region != "Unknown":
            assigned_count += 1
            print(f" → {affiliation} ({region})")
        else:
            print(f" → (unknown)")

        # Polite delay for DBLP XML fetches
        if i < 200:
            time.sleep(2 + random.uniform(0, 1))

    # Save
    output = {
        "metadata": {
            "phase": "assign_geo",
            "total_researchers": len(researchers),
            "region_counts": dict(region_counts),
            "assigned": assigned_count,
            "unknown": unknown_count,
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

    print(f"\nNote: {unknown_count} researchers have unknown region.")
    print("These will need manual review during the case study phase.")
    print("Consider enriching via OpenAlex API or manual lookup for key researchers.")


if __name__ == "__main__":
    run()
