#!/usr/bin/env python3
"""Audit NVIDIA Research author-affiliation metadata quality."""

from __future__ import annotations

import json
import re
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[3]
INDEX_PATH = REPO_ROOT / "index" / "all_papers.json"
EXAMPLE_IDS = {"arxiv-2929", "arxiv-2502"}


def split_frontmatter(text: str) -> tuple[str, str] | tuple[None, str]:
    if not text.startswith("---\n"):
        return None, text
    marker = "\n---\n"
    end = text.find(marker, 4)
    if end == -1:
        return None, text
    return text[4:end], text[end + len(marker):]


def top_level_duplicates(frontmatter: str) -> list[str]:
    keys = []
    for line in frontmatter.splitlines():
        if line and not line.startswith(" ") and ":" in line:
            keys.append(line.split(":", 1)[0])
    return sorted({key for key in keys if keys.count(key) > 1})


def load_frontmatter(path: Path) -> tuple[dict | None, str | None, list[str]]:
    text = path.read_text(encoding="utf-8", errors="replace")
    frontmatter, _body = split_frontmatter(text)
    if frontmatter is None:
        return None, "missing frontmatter", []
    duplicates = top_level_duplicates(frontmatter)
    sanitized = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", frontmatter)
    try:
        return yaml.safe_load(sanitized) or {}, None, duplicates
    except Exception as exc:
        return None, str(exc).split("\n", 1)[0], duplicates


def main() -> int:
    index = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    papers = [p for p in index["papers"] if "nvidia-research" in p.get("tags", [])]

    files = 0
    author_total = 0
    blank_affiliations = 0
    papers_with_blank = 0
    nvidia_authors = 0
    industry_authors = 0
    yaml_errors = []
    duplicate_key_files = []
    missing_files = []
    examples = {}

    for paper in papers:
        path = REPO_ROOT / paper.get("file", "")
        if not path.exists():
            missing_files.append((paper.get("id"), paper.get("file")))
            continue
        files += 1
        fm, error, duplicates = load_frontmatter(path)
        if duplicates:
            duplicate_key_files.append((paper.get("id"), paper.get("file"), duplicates))
        if error:
            yaml_errors.append((paper.get("id"), paper.get("file"), error))
            continue

        authors = fm.get("authors") if isinstance(fm.get("authors"), list) else []
        paper_has_blank = False
        for author in authors:
            if not isinstance(author, dict):
                continue
            author_total += 1
            affiliation = (author.get("affiliation") or "").strip()
            is_industry = bool(author.get("is_industry"))
            if not affiliation:
                blank_affiliations += 1
                paper_has_blank = True
            if is_industry:
                industry_authors += 1
            if is_industry or "nvidia" in affiliation.lower():
                nvidia_authors += 1
        if paper_has_blank:
            papers_with_blank += 1
        if paper.get("id") in EXAMPLE_IDS:
            examples[paper["id"]] = authors

    print(f"NVIDIA Research papers in index: {len(papers)}")
    print(f"Paper files found: {files}")
    print(f"Parsed authors: {author_total}")
    print(f"Blank affiliations: {blank_affiliations}")
    print(f"Papers with blank affiliations: {papers_with_blank}")
    print(f"Industry-marked authors: {industry_authors}")
    print(f"NVIDIA-affiliated/marked authors: {nvidia_authors}")
    print(f"Missing files: {len(missing_files)}")
    print(f"YAML parse errors: {len(yaml_errors)}")
    print(f"Files with duplicate top-level frontmatter keys: {len(duplicate_key_files)}")

    if yaml_errors:
        print("\nYAML parse error samples:")
        for item in yaml_errors[:10]:
            print(f"- {item[0]} {item[1]}: {item[2]}")
    if duplicate_key_files:
        print("\nDuplicate-key samples:")
        for paper_id, file_name, duplicates in duplicate_key_files[:10]:
            print(f"- {paper_id} {file_name}: {', '.join(duplicates)}")
    if examples:
        print("\nExample author records:")
        for paper_id in sorted(examples):
            print(f"{paper_id}:")
            for author in examples[paper_id]:
                if isinstance(author, dict):
                    print(
                        f"  - {author.get('name')} | {author.get('affiliation', '')} | "
                        f"is_industry={bool(author.get('is_industry'))}"
                    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
