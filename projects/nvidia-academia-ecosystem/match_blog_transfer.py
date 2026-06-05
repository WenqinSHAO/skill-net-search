#!/usr/bin/env python3
"""Find NVIDIA Technical Blog posts that reference research papers in our database.

Strategy:
1. Use the Atom feed (developer.nvidia.com/blog/feed/?paged=N) to discover ALL posts 2020-2026
2. Filter by date range, fetch full HTML content for each post
3. Match against our paper database by: author overlap, title phrase, project name
4. Create project-specific transfer annotations in projects/nvidia-academia-ecosystem/transfer/
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
INDEX_PATH = REPO_ROOT / "index" / "all_papers.json"
PROJECT_DIR = REPO_ROOT / "projects" / "nvidia-academia-ecosystem"
TRANSFER_DIR = PROJECT_DIR / "transfer"

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
FEED_BASE = "https://developer.nvidia.com/blog/feed/"


def fetch_url(url: str, timeout: int = 20) -> str | None:
    cmd = ["curl", "-s", "--max-time", str(timeout), "-H", f"User-Agent: {USER_AGENT}", url]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout + 5)
        if result.returncode != 0:
            return None
        return result.stdout
    except Exception:
        return None


def load_paper_db() -> list[dict]:
    """Load NVIDIA papers with key matching fields, including authors from paper files."""
    import yaml as _yaml
    with open(INDEX_PATH) as f:
        idx = json.load(f)

    papers = []
    for p in idx["papers"]:
        if "nvidia-research" not in p.get("tags", []):
            continue

        authors = []
        file_path = REPO_ROOT / p.get("file", "")
        if file_path.exists():
            with open(file_path) as f:
                content = f.read()
            fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
            if fm_match:
                try:
                    fm = _yaml.safe_load(fm_match.group(1))
                    if fm and fm.get("authors"):
                        authors = fm["authors"]
                except Exception:
                    pass

        title_words = set(p["title"].lower().split())
        title_keywords = set()
        for phrase in re.finditer(r'[A-Z][a-z]*[A-Z][a-zA-Z]*|[A-Z]{2,}', p["title"]):
            kw = phrase.group().lower()
            if len(kw) > 2:
                title_keywords.add(kw)

        author_names = set()
        for a in authors:
            name = a.get("name", "")
            parts = name.split()
            if parts:
                author_names.add(parts[-1].lower())
                if len(parts) > 1:
                    author_names.add(parts[0].lower())

        papers.append({
            "id": p["id"],
            "title": p["title"],
            "title_lower": p["title"].lower(),
            "title_words": title_words,
            "title_keywords": title_keywords,
            "author_names": author_names,
            "authors": authors,
            "nvidia_url": p.get("nvidia_url", ""),
            "date": p.get("date", ""),
            "conference": p.get("conference", ""),
            "research_areas": p.get("research_areas", []),
        })

    return papers


def fetch_feed_entries(page: int) -> list[dict]:
    """Fetch a single Atom feed page, return post metadata."""
    url = f"{FEED_BASE}?paged={page}"
    xml = fetch_url(url)
    if not xml:
        return []

    posts = []
    entries = re.split(r'<entry>', xml)[1:]
    for entry in entries:
        link_m = re.search(r'<link rel="alternate" type="text/html" href="([^"]+)"', entry)
        if not link_m:
            continue

        title_m = re.search(r'<title[^>]*>(?:<!\[CDATA\[)?([^<\]]*)', entry)
        date_m = re.search(r'<published>([^<]+)</published>', entry)
        author_m = re.search(r'<name>([^<]+)</name>', entry)

        posts.append({
            "title": title_m.group(1).strip() if title_m else "",
            "url": link_m.group(1),
            "date": date_m.group(1)[:10] if date_m else "",
            "author": author_m.group(1).strip() if author_m else "",
        })

    return posts


def discover_blog_posts(start_year: int = 2020, end_year: int = 2026) -> list[dict]:
    """Discover all blog posts in date range via Atom feed pagination."""
    all_posts = []
    seen_urls = set()

    page = 1
    while True:
        entries = fetch_feed_entries(page)
        if not entries:
            print(f"  Feed page {page}: empty, skipping", file=sys.stderr)
            page += 1
            if page > 50:  # safety limit
                break
            continue

        new_count = 0
        oldest_date = entries[-1]["date"]
        for entry in entries:
            if entry["url"] not in seen_urls:
                seen_urls.add(entry["url"])
                all_posts.append(entry)
                new_count += 1

        print(f"  Feed page {page}: {new_count} new posts (total {len(all_posts)}), oldest {oldest_date}", file=sys.stderr)

        # Stop when we've gone past our target window
        if oldest_date < f"{start_year}-01-01":
            print(f"  Reached {oldest_date}, stopping feed discovery", file=sys.stderr)
            break

        page += 1

    # Filter to date range
    filtered = [p for p in all_posts if p["date"] >= f"{start_year}-01-01" and p["date"] <= f"{end_year}-12-31"]
    print(f"  Filtered to {len(filtered)} posts in {start_year}-{end_year}", file=sys.stderr)
    return filtered


def match_post_to_papers(post_html: str, post_meta: dict, papers: list[dict]) -> list[dict]:
    """Check if a blog post references any papers in our database.

    Scoring:
    - Full author name match (blog author in paper's author list): +3
    - Last name match with non-trivial name (>3 chars): +2
    - Last name match with short name (<=3 chars): +1 (needs corroboration)
    - Title phrase >=5 words match: +2
    - Multiple project name matches (>=2): +1
    - Score >= 3 to count as match (or >=2 for title match evidence)
    """
    post_text = post_html.lower()
    post_clean = re.sub(r'<[^>]+>', ' ', post_html).lower()
    post_clean = re.sub(r'\s+', ' ', post_clean)

    blog_author = post_meta.get("author", "").lower().strip()

    matches = []

    for paper in papers:
        evidence_type = []
        score = 0

        # 1. Author overlap
        if blog_author:
            for author in paper.get("authors", []):
                paper_author = author.get("name", "").lower()
                if paper_author and len(paper_author) > 5:
                    # Full name match (bidirectional substring)
                    if paper_author in blog_author or blog_author in paper_author:
                        evidence_type.append("author_overlap")
                        score += 3
                        break

                    # Last name match
                    paper_parts = paper_author.split()
                    blog_parts = blog_author.split()
                    if paper_parts and blog_parts:
                        last_name = paper_parts[-1]
                        blog_last = blog_parts[-1]
                        if last_name == blog_last and len(last_name) > 2:
                            if len(last_name) > 3:
                                evidence_type.append("author_overlap_lastname")
                                score += 2
                            else:
                                # Short last names (Li, Wu, Xu, etc.) need corroboration
                                evidence_type.append("author_overlap_lastname_short")
                                score += 1
                            break

        # 2. Direct paper citation: check for 5+ word title phrases
        title_words = paper["title"].lower().split()
        phrases = []
        for i in range(len(title_words)):
            for j in range(i + 5, min(i + 9, len(title_words) + 1)):
                phrase = ' '.join(title_words[i:j])
                if len(phrase) > 40:
                    phrases.append(phrase)

        phrases.sort(key=len, reverse=True)
        for phrase in phrases[:3]:
            if phrase in post_clean:
                evidence_type.append("title_match")
                score += 2
                break

        # 3. Project/product name match
        project_names = set()
        for m in re.finditer(r'\b([A-Z][a-z]+(?:[A-Z][a-z]+)+)\b', paper["title"]):
            name = m.group(1).lower()
            if len(name) > 6 and name not in {'these', 'their', 'there', 'other', 'which', 'about', 'would', 'could', 'should'}:
                project_names.add(name)
        for m in re.finditer(r'\b([A-Z]{2,}[0-9]*)\b', paper["title"]):
            name = m.group(1).lower()
            if len(name) >= 3:
                project_names.add(name)

        project_matches = 0
        for proj in project_names:
            if len(proj) >= 3 and proj in post_clean:
                count = post_clean.count(proj)
                if count >= 2:
                    project_matches += 1

        if project_matches >= 2:
            evidence_type.append("project_name_match")
            score += 1

        # Score threshold: >= 3 for confident match, or == 2 with title_match evidence
        if score >= 3 or (score == 2 and "title_match" in evidence_type):
            matches.append({
                "paper_id": paper["id"],
                "paper_title": paper["title"],
                "evidence_type": evidence_type,
                "score": score,
                "nvidia_url": paper["nvidia_url"],
            })

    # If too many matches, filter to only the strongest
    if len(matches) > 5:
        matches = [m for m in matches if m["score"] >= 3]

    return matches


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--start-year", type=int, default=2020, help="Start year for posts")
    ap.add_argument("--end-year", type=int, default=2026, help="End year for posts")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--feed-only", action="store_true", help="Only discover posts, don't fetch content")
    args = ap.parse_args()

    # Load paper database
    papers = load_paper_db()
    print(f"Loaded {len(papers)} NVIDIA papers for matching", file=sys.stderr)

    # Discover posts via Atom feed
    print(f"Discovering blog posts {args.start_year}-{args.end_year} via Atom feed...", file=sys.stderr)
    all_posts = discover_blog_posts(args.start_year, args.end_year)
    print(f"Total discovered: {len(all_posts)} posts", file=sys.stderr)

    if args.feed_only:
        # Just dump the discovered posts
        for p in all_posts:
            print(f"{p['date']} | {p['author']} | {p['title'][:80]}")
            print(f"  {p['url']}")
        return

    # Fetch each post and match against papers
    transfer_records = []
    paper_transfer_map = {}

    for i, post in enumerate(all_posts):
        html = fetch_url(post["url"])
        if not html:
            continue

        print(f"[{i+1}/{len(all_posts)}] {post['date']} {post['title'][:70]}...", file=sys.stderr)

        matches = match_post_to_papers(html, post, papers)

        if matches:
            print(f"  Matched {len(matches)} papers: {[(m['paper_id'], m['evidence_type']) for m in matches]}", file=sys.stderr)

            for match in matches:
                pid = match["paper_id"]
                if pid not in paper_transfer_map:
                    paper_transfer_map[pid] = []
                paper_transfer_map[pid].append({
                    "blog_title": post["title"],
                    "blog_url": post["url"],
                    "blog_date": post["date"],
                    "evidence_type": match["evidence_type"],
                })

            transfer_records.append({
                "blog_title": post["title"],
                "blog_url": post["url"],
                "blog_date": post["date"],
                "blog_author": post["author"],
                "matched_papers": matches,
            })

        time.sleep(0.3)

    # Output results
    print(f"\n{'='*60}", file=sys.stderr)
    print(f"Transfer evidence found:", file=sys.stderr)
    print(f"  Blog posts with paper matches: {len(transfer_records)}", file=sys.stderr)
    print(f"  Papers with transfer evidence: {len(paper_transfer_map)}", file=sys.stderr)

    # Show paper-level summary
    for pid, evidences in sorted(paper_transfer_map.items(), key=lambda x: -len(x[1])):
        print(f"  {pid}: {len(evidences)} blog posts", file=sys.stderr)

    # Save results
    if not args.dry_run and transfer_records:
        TRANSFER_DIR.mkdir(parents=True, exist_ok=True)

        output = {
            "source": "NVIDIA Technical Blog",
            "scan_date": time.strftime("%Y-%m-%d"),
            "date_range": f"{args.start_year}-{args.end_year}",
            "posts_scanned": len(all_posts),
            "posts_with_matches": len(transfer_records),
            "papers_with_evidence": len(paper_transfer_map),
            "transfer_records": transfer_records,
            "paper_transfer_map": {pid: ev for pid, ev in paper_transfer_map.items()},
        }

        out_path = TRANSFER_DIR / "blog_transfer_evidence.json"
        with open(out_path, 'w', encoding='utf-8') as f:
            json.dump(output, f, ensure_ascii=False, indent=2)
        print(f"\nSaved to {out_path}", file=sys.stderr)

    if args.dry_run:
        print(json.dumps(transfer_records, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
