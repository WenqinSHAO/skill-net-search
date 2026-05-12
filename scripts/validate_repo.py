#!/usr/bin/env python3
"""Validate shared-layer repository invariants for net-research."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

VALID_STATUSES = {"new", "analyzed", "archived"}
KNOWN_TOPICS = {
    "LLM Serving",
    "LLM Training",
    "AI Observability",
    "AI DCN",
    "Network Measurement",
    "Network Monitoring",
    "Network Security",
    "Distributed Systems",
    "Consensus",
    "Replication",
    "Congestion Control",
    "Transport Protocol",
    "Routing",
    "Edge Computing",
    "CDN",
    "Caching",
    "SDN",
    "NFV",
    "Network Programmability",
    "Wireless",
    "Mobile",
    "IoT",
    "Datacenter Networking",
    "Cloud Computing",
    "Machine Learning for Networks",
    "Learning-based Systems",
}


def split_frontmatter(text: str) -> tuple[list[str], str] | tuple[None, str]:
    if not text.startswith("---\n"):
        return None, text
    marker = "\n---\n"
    end = text.find(marker, 4)
    if end == -1:
        return None, text
    frontmatter = text[4:end].splitlines()
    body = text[end + len(marker):]
    return frontmatter, body


def parse_frontmatter(path: Path) -> tuple[dict, list[str]]:
    issues = []
    data = {}
    content = path.read_text(encoding="utf-8")
    frontmatter, _body = split_frontmatter(content)
    if frontmatter is None:
        return {}, ["missing or malformed YAML frontmatter"]

    i = 0
    while i < len(frontmatter):
        line = frontmatter[i]
        if not line.strip():
            i += 1
            continue
        if re.match(r"^[A-Za-z_][A-Za-z0-9_]*:\s*$", line):
            key = line.split(":", 1)[0]
            items = []
            i += 1
            while i < len(frontmatter) and (
                frontmatter[i].startswith("  - ") or frontmatter[i].startswith("    ")
            ):
                item_line = frontmatter[i]
                if item_line.startswith("  - "):
                    items.append(item_line[4:].strip())
                i += 1
            data[key] = items
            continue
        if ":" in line:
            key, raw = line.split(":", 1)
            data[key.strip()] = raw.strip().strip('"')
        i += 1

    for key in ("id", "title", "conference", "date", "status"):
        if key not in data or not data[key]:
            issues.append(f"missing frontmatter field: {key}")
    return data, issues


def validate_index(workspace: Path) -> list[str]:
    issues = []
    idx_path = workspace / "index" / "all_papers.json"
    if not idx_path.exists():
        return ["missing index/all_papers.json"]

    try:
        index_data = json.loads(idx_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"invalid JSON in index/all_papers.json: {exc}"]

    papers = index_data.get("papers")
    if not isinstance(papers, list):
        return ["index/all_papers.json: papers must be a list"]

    if index_data.get("total_count") != len(papers):
        issues.append(
            f"index total_count mismatch: declared {index_data.get('total_count')} actual {len(papers)}"
        )

    id_counts = Counter(p.get("id") for p in papers if isinstance(p, dict))
    for paper_id, count in sorted(id_counts.items()):
        if paper_id and count > 1:
            issues.append(f"duplicate paper id: {paper_id} ({count} records)")

    file_counts = Counter()
    for paper in papers:
        if not isinstance(paper, dict):
            issues.append("index contains non-object paper record")
            continue
        file_value = paper.get("file", "")
        if not file_value:
            issues.append(f"{paper.get('id', '<unknown>')}: missing file path in index")
            continue
        if "\\" in file_value:
            issues.append(f"{paper.get('id', '<unknown>')}: non-POSIX path in index: {file_value}")
        file_counts[file_value] += 1
        path = workspace / file_value.replace("\\", "/")
        if not path.exists():
            issues.append(f"{paper.get('id', '<unknown>')}: indexed file missing: {file_value}")
            continue

        frontmatter, fm_issues = parse_frontmatter(path)
        for issue in fm_issues:
            issues.append(f"{paper.get('id', '<unknown>')}: {path}: {issue}")
        if not frontmatter:
            continue
        if frontmatter.get("id") and frontmatter["id"] != paper.get("id"):
            issues.append(
                f"{paper.get('id', '<unknown>')}: index/file id mismatch ({paper.get('id')} vs {frontmatter['id']})"
            )
        if frontmatter.get("title") and frontmatter["title"] != paper.get("title"):
            issues.append(f"{paper.get('id', '<unknown>')}: index/file title mismatch")
        if frontmatter.get("conference") and frontmatter["conference"] != paper.get("conference"):
            issues.append(f"{paper.get('id', '<unknown>')}: index/file conference mismatch")
        if frontmatter.get("date") and frontmatter["date"] != paper.get("date"):
            issues.append(f"{paper.get('id', '<unknown>')}: index/file date mismatch")
        if frontmatter.get("status") and frontmatter["status"] not in VALID_STATUSES:
            issues.append(f"{paper.get('id', '<unknown>')}: invalid status {frontmatter['status']}")

        topics = frontmatter.get("topics", [])
        if isinstance(topics, list):
            for topic in topics:
                if topic and topic not in KNOWN_TOPICS:
                    issues.append(f"{paper.get('id', '<unknown>')}: unknown topic {topic}")

    for file_value, count in sorted(file_counts.items()):
        if count > 1:
            issues.append(f"duplicate indexed file path: {file_value} ({count} records)")

    return issues


def main() -> int:
    workspace = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(".").resolve()
    issues = validate_index(workspace)
    if issues:
        print("Validation failed:\n")
        for issue in issues:
            print(f"- {issue}")
        print(f"\nTotal issues: {len(issues)}")
        return 1
    print("Validation passed: no shared-layer invariant violations found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
