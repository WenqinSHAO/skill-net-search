#!/usr/bin/env python3
"""
Shared-layer paper importer for net-research.

This script is intentionally narrow:
  - ingest filter records
  - canonicalize fields
  - deduplicate against the shared index
  - write or update canonical shared paper files
  - maintain index/all_papers.json

It does not manage project-level notes, summaries, or synthesis.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import unicodedata
from collections import Counter
from datetime import date
from pathlib import Path

SKIP_PREFIXES = ("a ", "an ", "the ", "towards ", "toward ")

CONF_CANONICAL = {
    "nsdi": "NSDI",
    "sigcomm": "SIGCOMM",
    "osdi": "OSDI",
    "conext": "CoNEXT",
    "imc": "IMC",
    "atc": "USENIX ATC",
    "eurosys": "EuroSys",
    "fast": "FAST",
    "sosp": "SOSP",
    "isca": "ISCA",
    "iclr": "ICLR",
    "icml": "ICML",
    "neurips": "NeurIPS",
    "arxiv": "arXiv",
}

TOPIC_ALIASES = {
    "llm serving": "LLM Serving",
    "llm_serving": "LLM Serving",
    "llm training": "LLM Training",
    "llm_training": "LLM Training",
    "ai observability": "AI Observability",
    "ai_observability": "AI Observability",
    "ai dcn": "AI DCN",
    "ai_dcn": "AI DCN",
    "network measurement": "Network Measurement",
    "network_measurement": "Network Measurement",
    "network monitoring": "Network Monitoring",
    "network_monitoring": "Network Monitoring",
    "network security": "Network Security",
    "network_security": "Network Security",
    "distributed systems": "Distributed Systems",
    "distributed_systems": "Distributed Systems",
    "consensus": "Consensus",
    "replication": "Replication",
    "congestion control": "Congestion Control",
    "congestion_control": "Congestion Control",
    "transport protocol": "Transport Protocol",
    "transport_protocol": "Transport Protocol",
    "routing": "Routing",
    "edge computing": "Edge Computing",
    "edge_computing": "Edge Computing",
    "cdn": "CDN",
    "caching": "Caching",
    "sdn": "SDN",
    "nfv": "NFV",
    "network programmability": "Network Programmability",
    "network_programmability": "Network Programmability",
    "wireless": "Wireless",
    "mobile": "Mobile",
    "iot": "IoT",
    "datacenter networking": "Datacenter Networking",
    "datacenter_networking": "Datacenter Networking",
    "cloud computing": "Cloud Computing",
    "cloud_computing": "Cloud Computing",
    "machine learning for networks": "Machine Learning for Networks",
    "machine_learning_for_networks": "Machine Learning for Networks",
    "learning-based systems": "Learning-based Systems",
    "learning_based_systems": "Learning-based Systems",
}

INDUSTRY_KEYWORDS = {
    "alibaba", "microsoft", "google", "meta", "bytedance", "tencent",
    "huawei", "amazon", "intel", "nvidia", "apple", "ibm", "oracle",
    "cisco", "juniper", "cloudflare", "fastly", "netflix",
}


def levenshtein_distance(s: str, t: str) -> int:
    if s == t:
        return 0
    if not s:
        return len(t)
    if not t:
        return len(s)
    prev = list(range(len(t) + 1))
    curr = [0] * (len(t) + 1)
    for i, cs in enumerate(s, 1):
        curr[0] = i
        for j, ct in enumerate(t, 1):
            cost = 0 if cs == ct else 1
            curr[j] = min(prev[j] + 1, curr[j - 1] + 1, prev[j - 1] + cost)
        prev, curr = curr, prev
    return prev[len(t)]


def similarity(a: str, b: str) -> float:
    if not a or not b:
        return 0.0
    return 1.0 - levenshtein_distance(a, b) / max(len(a), len(b))


def conference_abbr(name: str) -> str:
    cleaned = re.sub(r"\s+", " ", name.strip())
    base = re.sub(r"\s+\d{4}$", "", cleaned, flags=re.IGNORECASE).lower()
    reverse = {v.lower(): k for k, v in CONF_CANONICAL.items()}
    if base in reverse:
        return reverse[base]
    compact = base.replace(" ", "")
    if compact in CONF_CANONICAL:
        return compact
    raise ValueError(f"Unsupported conference name: {name}")


def conference_label(abbr: str, year: int) -> str:
    if abbr not in CONF_CANONICAL:
        raise ValueError(f"Unsupported conference abbreviation: {abbr}")
    return f"{CONF_CANONICAL[abbr]} {year}"


def normalize_title(title: str) -> str:
    text = title.lower().strip()
    for prefix in SKIP_PREFIXES:
        if text.startswith(prefix):
            text = text[len(prefix):]
            break
    return re.sub(r"[^a-z0-9]", "", text)


def slugify(title: str) -> str:
    slug = unicodedata.normalize("NFC", title)
    slug = slug.encode("ascii", "ignore").decode("ascii")
    if not slug.strip():
        return hashlib.md5(title.encode("utf-8")).hexdigest()[:12]
    slug = re.sub(r"[^a-z0-9\s-]", "", slug.lower())
    slug = re.sub(r"[-\s]+", "-", slug).strip("-")
    slug = slug[:80].strip("-")
    return slug or hashlib.md5(title.encode("utf-8")).hexdigest()[:12]


def normalize_path_string(path: str) -> str:
    return path.replace("\\", "/")


def parse_authors(raw_authors: str) -> list[dict]:
    authors = []
    for piece in raw_authors.split(";"):
        name = piece.strip()
        if not name:
            continue
        lowered = name.lower()
        authors.append({
            "name": name,
            "affiliation": "",
            "is_industry": any(token in lowered for token in INDUSTRY_KEYWORDS),
        })
    return authors


def canonicalize_topics(topics_raw: list[str]) -> list[str]:
    if not topics_raw:
        return ["Distributed Systems"]
    result = []
    seen = set()
    for topic in topics_raw:
        candidate = TOPIC_ALIASES.get(topic.strip().lower(), topic.strip())
        if candidate and candidate not in seen:
            seen.add(candidate)
            result.append(candidate)
    return result or ["Distributed Systems"]


def make_tags(topics: list[str]) -> list[str]:
    return [topic.lower().replace(" ", "-") for topic in topics]


def extract_year(record: dict) -> int:
    date_value = record.get("date", "")
    if not date_value or len(date_value) < 4:
        raise ValueError(f"Record missing date/year: {record.get('id', '<unknown>')}")
    return int(date_value[:4])


def next_sequence(existing_papers: list[dict], venue_abbr: str, year: int) -> int:
    max_seq = 0
    prefix = f"{venue_abbr}{str(year)[-2:]}-"
    for paper in existing_papers:
        paper_id = paper.get("id", "")
        if not paper_id.startswith(prefix):
            continue
        try:
            max_seq = max(max_seq, int(paper_id.split("-")[1]))
        except (IndexError, ValueError):
            continue
    return max_seq + 1


def split_external_ids(arxiv_value: str) -> list[str]:
    if not arxiv_value:
        return []
    return [part.strip() for part in arxiv_value.split("/") if part.strip()]


def choose_preferred_url(existing_url: str, new_url: str) -> str:
    if not new_url:
        return existing_url
    if not existing_url:
        return new_url
    if "arxiv.org" in existing_url and "arxiv.org" not in new_url:
        return new_url
    return existing_url


def merge_authors(existing_authors: list[dict], new_authors: list[dict]) -> list[dict]:
    merged = {}
    for author in existing_authors + new_authors:
        name = author.get("name", "").strip()
        if not name:
            continue
        current = merged.get(name)
        if current is None:
            merged[name] = {
                "name": name,
                "affiliation": author.get("affiliation", ""),
                "is_industry": bool(author.get("is_industry", False)),
            }
            continue
        if not current.get("affiliation") and author.get("affiliation"):
            current["affiliation"] = author["affiliation"]
        current["is_industry"] = bool(current["is_industry"] or author.get("is_industry", False))
    return [merged[name] for name in sorted(merged)]


def merge_record(existing: dict, raw: dict) -> dict:
    merged = dict(existing)
    merged["title"] = max(existing.get("title", ""), raw.get("raw_title", "").strip(), key=len)
    old_abs = existing.get("abstract", "") or ""
    new_abs = (raw.get("abstract") or "").strip()
    merged["abstract"] = max(old_abs, new_abs, key=len)
    merged["url"] = choose_preferred_url(existing.get("url", ""), raw.get("url", "").strip())
    existing_topics = existing.get("topics", [])
    new_topics = canonicalize_topics(raw.get("topics_raw", []))
    merged["topics"] = canonicalize_topics(existing_topics + new_topics)
    merged["tags"] = make_tags(merged["topics"])
    merged["authors"] = merge_authors(existing.get("authors", []), parse_authors(raw.get("raw_authors", "")))
    merged["is_industry"] = bool(existing.get("is_industry") or raw.get("is_industry"))

    existing_arxiv = split_external_ids(existing.get("arxiv", ""))
    new_arxiv = (raw.get("arxiv_id") or "").strip()
    if new_arxiv and new_arxiv not in existing_arxiv:
        existing_arxiv.append(new_arxiv)
    merged["arxiv"] = " / ".join(existing_arxiv)
    merged["status"] = "analyzed" if merged.get("abstract") else existing.get("status", "new")
    return merged


def build_new_record(raw: dict, paper_id: str, venue_abbr: str, year: int) -> dict:
    topics = canonicalize_topics(raw.get("topics_raw", []))
    authors = parse_authors(raw.get("raw_authors", ""))
    abstract = (raw.get("abstract") or "").strip()
    return {
        "id": paper_id,
        "title": raw["raw_title"].strip(),
        "conference": conference_label(venue_abbr, year),
        "date": f"{year}-03",
        "authors": authors,
        "topics": topics,
        "tags": make_tags(topics),
        "abstract": abstract,
        "arxiv": (raw.get("arxiv_id") or "").strip(),
        "url": (raw.get("url") or "").strip(),
        "status": "analyzed" if abstract else "new",
        "is_industry": bool(raw.get("is_industry")) or any(a["is_industry"] for a in authors),
    }


def render_frontmatter(record: dict) -> str:
    lines = [
        "---",
        f'id: {record["id"]}',
        f'title: {json.dumps(record["title"], ensure_ascii=False)}',
        f'conference: {json.dumps(record["conference"], ensure_ascii=False)}',
        f'date: "{record["date"]}"',
        "authors:",
    ]
    for author in record.get("authors", []):
        lines.extend([
            f'  - name: {json.dumps(author.get("name", ""), ensure_ascii=False)}',
            f'    affiliation: {json.dumps(author.get("affiliation", ""), ensure_ascii=False)}',
            f'    is_industry: {str(bool(author.get("is_industry", False))).lower()}',
        ])
    lines.append("topics:")
    for topic in record.get("topics", []):
        lines.append(f"  - {topic}")
    lines.append("tags:")
    for tag in record.get("tags", []):
        lines.append(f"  - {tag}")
    lines.extend([
        f'arxiv: {json.dumps(record.get("arxiv", ""), ensure_ascii=False)}',
        f'url: {json.dumps(record.get("url", ""), ensure_ascii=False)}',
        f'status: {record.get("status", "new")}',
        "---",
        "",
    ])
    return "\n".join(lines)


def default_body(record: dict) -> str:
    abstract = record.get("abstract", "")
    abstract_block = abstract if abstract else "[(待补充)]"
    return "\n".join([
        f"# {record['title']}",
        "",
        "## 摘要",
        "",
        abstract_block,
        "",
        "## Problem",
        "",
        "[(待补充)]",
        "",
        "## Method",
        "",
        "[(待补充)]",
        "",
        "## Evaluation",
        "",
        "[(待补充)]",
        "",
        "## Limitations",
        "",
        "[(待补充)]",
        "",
    ])


def split_markdown_file(path: Path) -> tuple[str | None, str]:
    if not path.exists():
        return None, ""
    content = path.read_text(encoding="utf-8")
    if not content.startswith("---\n"):
        return None, content
    marker = "\n---\n"
    end = content.find(marker, 4)
    if end == -1:
        return None, content
    frontmatter = content[: end + len(marker)]
    body = content[end + len(marker):]
    return frontmatter, body


def write_markdown(path: Path, record: dict) -> None:
    _, existing_body = split_markdown_file(path)
    body = existing_body.strip() or default_body(record).strip()
    text = render_frontmatter(record) + body + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def load_index(idx_path: Path) -> dict:
    if not idx_path.exists():
        return {"last_updated": "", "total_count": 0, "papers": []}
    data = json.loads(idx_path.read_text(encoding="utf-8"))
    papers = data.get("papers", [])
    counts = Counter(p.get("id") for p in papers if p.get("id"))
    duplicates = [paper_id for paper_id, count in counts.items() if count > 1]
    if duplicates:
        raise ValueError(
            "index/all_papers.json contains duplicate IDs; run validator and repair first: "
            + ", ".join(sorted(duplicates))
        )
    return data


def save_index(idx_path: Path, index_data: dict) -> None:
    index_data["last_updated"] = date.today().isoformat()
    index_data["total_count"] = len(index_data["papers"])
    idx_path.parent.mkdir(parents=True, exist_ok=True)
    idx_path.write_text(json.dumps(index_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


class Deduplicator:
    def __init__(self, existing_papers: list[dict]):
        self.by_id = {paper["id"]: dict(paper) for paper in existing_papers}
        self.by_arxiv = {}
        self.by_title = {}
        for paper in existing_papers:
            paper_id = paper["id"]
            for arxiv_id in split_external_ids(paper.get("arxiv", "")):
                self.by_arxiv[arxiv_id] = paper_id
            venue = conference_abbr(paper.get("conference", ""))
            year = extract_year(paper)
            key = (venue, year, normalize_title(paper["title"]))
            self.by_title[key] = paper_id

    def find(self, raw: dict) -> tuple[str, str] | None:
        arxiv_id = (raw.get("arxiv_id") or "").strip()
        if arxiv_id and arxiv_id in self.by_arxiv:
            return self.by_arxiv[arxiv_id], "arxiv_id"

        venue = conference_abbr(raw["conference"])
        year = int(raw["year"])
        key = (venue, year, normalize_title(raw["raw_title"]))
        if key in self.by_title:
            return self.by_title[key], "title_exact"

        for paper_id, existing in self.by_id.items():
            if conference_abbr(existing["conference"]) != venue:
                continue
            if abs(extract_year(existing) - year) > 1:
                continue
            score = similarity(normalize_title(existing["title"]), normalize_title(raw["raw_title"]))
            if score > 0.90:
                return paper_id, f"fuzzy_title ({score:.2f})"
        return None


def resolve_record_path(workspace: Path, record: dict) -> Path:
    file_value = record.get("file", "")
    if file_value:
        return workspace / normalize_path_string(file_value)
    venue = conference_abbr(record["conference"])
    year = extract_year(record)
    filename = f'{record["id"]}-{slugify(record["title"])}.md'
    return workspace / "papers" / venue / str(year) / filename


def upsert_index(index_data: dict, record: dict) -> None:
    for idx, current in enumerate(index_data["papers"]):
        if current["id"] == record["id"]:
            index_data["papers"][idx] = record
            return
    index_data["papers"].append(record)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Import shared-layer conference papers")
    parser.add_argument("--conference", required=True, help="Conference name or abbreviation, e.g. NSDI")
    parser.add_argument("--year", required=True, type=int, help="Publication year, e.g. 2026")
    parser.add_argument("--workspace", default=".", help="Workspace root")
    parser.add_argument("--input", help="Input JSON file containing filter records; defaults to stdin")
    parser.add_argument("--dry-run", action="store_true", help="Validate and preview without writing files")
    return parser.parse_args()


def load_input(args: argparse.Namespace) -> list[dict]:
    if args.input:
        data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    else:
        data = json.load(sys.stdin)
    if not isinstance(data, list):
        raise ValueError("Input must be a JSON array")
    for index, record in enumerate(data, start=1):
        if not isinstance(record, dict):
            raise ValueError(f"Input record #{index} is not an object")
        if not record.get("raw_title"):
            raise ValueError(f"Input record #{index} missing raw_title")
        if not (record.get("url") or record.get("arxiv_id")):
            raise ValueError(f"Input record #{index} must include url or arxiv_id")
    return data


def main() -> int:
    args = parse_args()
    workspace = Path(args.workspace).resolve()
    venue_abbr = conference_abbr(args.conference)
    year = args.year
    raw_records = load_input(args)

    idx_path = workspace / "index" / "all_papers.json"
    index_data = load_index(idx_path)
    dedup = Deduplicator(index_data["papers"])
    seq = next_sequence(index_data["papers"], venue_abbr, year)

    output_records = []
    warnings = []
    new_count = 0
    updated_count = 0

    for raw in raw_records:
        duplicate = dedup.find(raw)
        if duplicate:
            record_id, reason = duplicate
            existing = dedup.by_id[record_id]
            record = merge_record(existing, raw)
            if reason.startswith("fuzzy_title"):
                warnings.append(f"[{record_id}] merged by {reason}: {raw['raw_title']}")
            updated_count += 1
        else:
            record_id = f"{venue_abbr}{str(year)[-2:]}-{seq:03d}"
            seq += 1
            record = build_new_record(raw, record_id, venue_abbr, year)
            new_count += 1
        path = resolve_record_path(workspace, record)
        record["file"] = normalize_path_string(str(path.relative_to(workspace)))
        output_records.append(record)

    if not args.dry_run:
        for record in output_records:
            write_markdown(workspace / record["file"], record)
            upsert_index(index_data, record)
        save_index(idx_path, index_data)

    print(f"\n{'=' * 50}")
    print(f"导入报告 — {conference_label(venue_abbr, year)}")
    print(f"{'=' * 50}")
    print(f"  输入记录数   : {len(raw_records)}")
    print(f"  新增         : {new_count}")
    print(f"  更新（合并） : {updated_count}")
    if warnings:
        print("\n  ⚠  模糊匹配合并：")
        for warning in warnings:
            print(f"  - {warning}")
    if args.dry_run:
        print("\n  [dry-run] 未写入文件")
        for record in output_records[:5]:
            print(f"  - {record['id']} -> {record['file']}")
        if len(output_records) > 5:
            print(f"  ... 共 {len(output_records)} 条")
    print()
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # pragma: no cover
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
