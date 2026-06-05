#!/usr/bin/env python3
"""Parse NVIDIA Research publications page HTML to extract paper records.

Usage:
  python parse_nvidia_page.py <html_file> [--year YYYY]

The HTML is fetched via SearXNG web_url_read and saved to files.
This script parses those files and outputs JSON filter records.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


def parse_publications(html: str, default_year: int = 2025) -> list[dict]:
    """Extract publication records from NVIDIA Research page HTML."""
    papers = []

    # Find publication entries
    # Pattern: <a href="/publication/YYYY-MM_slug">Title</a>
    # Followed by author names on the next line(s)

    # Split by publication links
    pub_pattern = re.compile(
        r'<a href="(/publication/(\d{4})-(\d{2})_[^"]+)">([^<]+)</a>',
        re.IGNORECASE
    )

    # Also capture venue/event tags that appear before some entries
    # Pattern: * [<a href="...">VENUE</a>] followed by publication link

    # Find all publication entries with surrounding context
    lines = html.split('\n')

    current_venue = None

    for i, line in enumerate(lines):
        # Check for venue/event tag
        venue_match = re.search(r'<a href="[^"]*f%5B\d%5D=publication%5Fevents[^"]*">([^<]+)</a>', line)
        if venue_match:
            current_venue = venue_match.group(1)
            continue

        # Check for publication link
        pub_match = pub_pattern.search(line)
        if pub_match:
            url = pub_match.group(1)
            year = int(pub_match.group(2))
            month = pub_match.group(3)
            title = pub_match.group(4)

            # Collect authors from following lines
            authors = []
            # Get the rest of this line after the link
            rest_of_line = line[pub_match.end():].strip()
            if rest_of_line:
                authors.extend(parse_authors(rest_of_line))

            # Check next few lines for additional authors
            for j in range(i + 1, min(i + 5, len(lines))):
                next_line = lines[j].strip()
                if not next_line or '<a href="/publication/' in next_line:
                    break
                if '<a href="/person/' in next_line:
                    authors.extend(parse_authors(next_line))
                elif next_line and not next_line.startswith('<') and not next_line.startswith('*'):
                    # Plain text authors
                    authors.extend([a.strip() for a in next_line.split(',') if a.strip()])

            venue = current_venue if current_venue else "Unknown"
            # Reset venue for next entry unless it's a year heading
            current_venue = None

            papers.append({
                "title": title,
                "url": f"https://research.nvidia.com{url}",
                "year": year,
                "month": month,
                "authors": authors,
                "venue_tag": venue,
                "nvidia_authors": [],  # We'll determine this later
                "academic_authors": [],  # We'll determine this later
            })

    return papers


def parse_authors(text: str) -> list[str]:
    """Extract author names from text containing person links or plain names."""
    authors = []

    # Extract names from /person/ links
    person_pattern = re.compile(r'<a href="/person/[^"]*">([^<]+)</a>')
    for match in person_pattern.finditer(text):
        authors.append(match.group(1))

    # Also extract plain text author names (comma-separated)
    # Remove HTML tags first
    clean = re.sub(r'<[^>]+>', '', text)
    for name in clean.split(','):
        name = name.strip()
        if name and len(name) > 1 and not name.startswith('*') and not name.startswith('<'):
            if name not in authors:
                authors.append(name)

    return authors


def main():
    if len(sys.argv) < 2:
        print("Usage: python parse_nvidia_page.py <html_file> [--year YYYY]")
        sys.exit(1)

    html_file = sys.argv[1]
    year = None

    for i, arg in enumerate(sys.argv):
        if arg == '--year' and i + 1 < len(sys.argv):
            year = int(sys.argv[i + 1])

    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()

    papers = parse_publications(html, default_year=year or 2025)

    print(json.dumps(papers, ensure_ascii=False, indent=2))
    print(f"\nTotal: {len(papers)} papers extracted", file=sys.stderr)


if __name__ == '__main__':
    main()
