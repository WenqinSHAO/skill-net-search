#!/usr/bin/env python3
"""LLM-based three-axis paper topic classifier for networking research papers.

Uses DeepSeek V4 Flash with JSON mode to classify papers into the
scenario x mechanism x method taxonomy defined in data/taxonomy_v3.json.

Reads: data/new_core_clean_papers.json + data/paper_abstracts.json (optional)
Output: data/paper_topic_labels_v3.json
Progress: data/classification_progress_v3.json

Requires: DS_API_KEY environment variable.
"""

from __future__ import annotations

import json
import os
import random
import sys
import time
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

from openai import OpenAI

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

TAXONOMY_PATH = DATA_DIR / "taxonomy_v3.json"
INPUT_PAPERS = DATA_DIR / "new_core_clean_papers.json"
INPUT_ABSTRACTS = DATA_DIR / "paper_abstracts.json"
OUTPUT_LABELS = DATA_DIR / "paper_topic_labels_v3.json"
PROGRESS_FILE = DATA_DIR / "classification_progress_v3.json"

MODEL = "deepseek-v4-flash"
MAX_WORKERS = 10
CHECKPOINT_INTERVAL = 50
MAX_RETRIES = 4
BASE_DELAY = 1.0
MAX_BACKOFF = 30.0
DEEPSEEK_BASE_URL = "https://api.deepseek.com"


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


def load_taxonomy(path: str | None = None) -> dict[str, Any]:
    """Load the taxonomy JSON. This is the public API for loading the taxonomy."""
    p = Path(path) if path else TAXONOMY_PATH
    return load_json(p, {})


def build_taxonomy_text(taxonomy: dict[str, Any]) -> str:
    """Build the taxonomy description text for the LLM prompt from taxonomy JSON."""
    axes = taxonomy.get("axes", {})
    parts = []
    for axis_key in ["scenario", "mechanism", "method"]:
        axis = axes.get(axis_key, {})
        label = axis.get("label", axis_key)
        min_l = axis.get("min_labels", 1)
        max_l = axis.get("max_labels", 3)
        parts.append(f"### {label} (assign {min_l}-{max_l} labels, multi-label OK)")
        for key, val in axis.get("values", {}).items():
            parts.append(f"- `{key}`: {val['description']}")
        parts.append("")
    return "\n".join(parts)


def build_json_schema_text(taxonomy: dict[str, Any]) -> str:
    """Build the expected JSON output schema text from taxonomy (for prompt inclusion).

    DeepSeek JSON mode enforces valid JSON syntax but not a specific schema,
    so we describe the expected structure in the prompt itself.
    """
    axes = taxonomy.get("axes", {})
    scenario_keys = list(axes.get("scenario", {}).get("values", {}).keys())
    mechanism_keys = list(axes.get("mechanism", {}).get("values", {}).keys())
    method_keys = list(axes.get("method", {}).get("values", {}).keys())

    scenario_enum = ", ".join(f'"{k}"' for k in scenario_keys)
    mechanism_enum = ", ".join(f'"{k}"' for k in mechanism_keys)
    method_enum = ", ".join(f'"{k}"' for k in method_keys)

    return f"""You MUST respond with a single JSON object matching this structure:
{{
  "scenario": [string, ...],    // 1-2 values from: [{scenario_enum}]
  "mechanism": [string, ...],   // 1-3 values from: [{mechanism_enum}]
  "method": [string, ...],      // 0-3 values from: [{method_enum}]
  "evidence": {{
    "scenario": {{"label_key": "brief evidence from title/abstract"}},
    "mechanism": {{"label_key": "brief evidence from title/abstract"}},
    "method": {{"label_key": "brief evidence from title/abstract"}}
  }},
  "confidence": {{
    "scenario": "high|medium|low",
    "mechanism": "high|medium|low",
    "method": "high|medium|low"
  }},
  "uncertain": true or false
}}

Only use label keys from the taxonomy lists above. Never invent new labels.
Return ONLY this JSON object, no markdown fences, no extra text."""


def build_system_prompt(taxonomy: dict[str, Any]) -> str:
    """Build the system prompt including taxonomy and output format."""
    taxonomy_text = build_taxonomy_text(taxonomy)
    schema_text = build_json_schema_text(taxonomy)

    return f"""You are a networking research paper classifier. You classify papers into a three-axis taxonomy.

## Rules

1. Assign 1-2 scenario labels, 1-3 mechanism labels, and 0-3 method labels per paper.
2. Only assign a label when there is clear evidence in the paper title or abstract.
3. For each assigned label, cite the specific words or phrases from the title/abstract.
4. Be conservative: when uncertain, choose the more specific label. Do not assign a label when evidence is absent or ambiguous.
5. Confidence per axis: "high" (explicit keywords in title), "medium" (clear inference from abstract or venue context), "low" (weak signal, guess).
6. Set "uncertain": true when any axis has low confidence or zero required labels.

## Taxonomy

{taxonomy_text}

## Output Format (JSON)

{schema_text}"""


def build_user_message(
    title: str,
    abstract: str | None,
    year: int | None,
    venue: str | None,
) -> str:
    """Build the user message for a single paper."""
    paper_info = f"Title: {title}"
    if venue:
        paper_info += f"\nVenue: {venue}"
    if year:
        paper_info += f"\nYear: {year}"
    if abstract:
        paper_info += f"\nAbstract: {abstract}"
    else:
        paper_info += "\nAbstract: (not available - classify from title only)"

    return f"""## Paper to Classify

{paper_info}

Return a JSON object with the classification. Include ONLY the JSON object, nothing else."""


def parse_json_response(text: str) -> dict[str, Any] | None:
    """Parse JSON from LLM response text, handling markdown fences and edge cases."""
    text = text.strip()
    if not text:
        return None

    # Remove markdown code fences
    if text.startswith("```json"):
        text = text[7:]
    elif text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    text = text.strip()

    # Find the outermost JSON object
    # Handle case where model outputs text before/after JSON
    start = text.find("{")
    end = text.rfind("}")
    if start >= 0 and end > start:
        try:
            return json.loads(text[start:end + 1])
        except json.JSONDecodeError:
            pass

    # Last resort: try parsing the whole thing
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    return None


def validate_labels(result: dict[str, Any], taxonomy: dict[str, Any]) -> dict[str, Any]:
    """Validate that all assigned labels exist in the taxonomy. Filter out hallucinations."""
    axes = taxonomy.get("axes", {})
    for axis_key in ["scenario", "mechanism", "method"]:
        valid = set(axes.get(axis_key, {}).get("values", {}).keys())
        if axis_key in result and isinstance(result[axis_key], list):
            result[axis_key] = [v for v in result[axis_key] if v in valid]
    return result


def classify_with_json_mode(
    client: OpenAI,
    taxonomy: dict[str, Any],
    system_prompt: str,
    title: str,
    abstract: str | None = None,
    year: int | None = None,
    venue: str | None = None,
    retries: int = MAX_RETRIES,
) -> dict[str, Any] | None:
    """Classify a single paper using DeepSeek JSON mode."""
    user_message = build_user_message(title, abstract, year, venue)

    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message},
                ],
                response_format={"type": "json_object"},
                max_tokens=1024,
                temperature=0.1,
            )

            content = response.choices[0].message.content
            if not content:
                if attempt < retries - 1:
                    time.sleep(0.5 * (attempt + 1))
                    continue
                return None

            result = parse_json_response(content)
            if result is None:
                if attempt < retries - 1:
                    time.sleep(0.3 * (attempt + 1))
                    continue
                return None

            # Validate and filter labels
            result = validate_labels(result, taxonomy)

            # Ensure required fields exist
            for field in ["scenario", "mechanism", "method", "evidence", "confidence", "uncertain"]:
                if field not in result:
                    if field in ("scenario", "mechanism"):
                        result[field] = []
                    elif field == "method":
                        result[field] = []
                    elif field == "evidence":
                        result[field] = {"scenario": {}, "mechanism": {}, "method": {}}
                    elif field == "confidence":
                        result[field] = {"scenario": "low", "mechanism": "low", "method": "low"}
                    elif field == "uncertain":
                        result[field] = True

            return result

        except Exception as e:
            error_str = str(e).lower()
            # Check for rate limit errors
            if "rate" in error_str or "429" in error_str:
                if attempt < retries - 1:
                    delay = min(BASE_DELAY * (2 ** attempt), MAX_BACKOFF)
                    delay += random.uniform(0, delay * 0.3)
                    time.sleep(delay)
                    continue
            # Check for server errors
            elif "500" in error_str or "503" in error_str or "server" in error_str:
                if attempt < retries - 1:
                    delay = min(2 ** attempt, 8) + random.uniform(0, 2)
                    time.sleep(delay)
                    continue
            # Connection errors
            elif "connect" in error_str or "timeout" in error_str:
                if attempt < retries - 1:
                    time.sleep(1.0 * (attempt + 1))
                    continue
            else:
                if attempt < retries - 1:
                    time.sleep(0.5 * (attempt + 1))
                    continue

    return None


def classify_single_paper(
    client: OpenAI,
    taxonomy: dict[str, Any],
    system_prompt: str,
    paper: dict[str, Any],
    abstract: str | None = None,
) -> dict[str, Any]:
    """Classify one paper, returning the result with paper metadata."""
    title = paper.get("title", "")
    venue = paper.get("venue_group") or paper.get("venue", "")
    year = int(paper.get("year") or 0)
    paper_id = paper.get("paper_id", f"{title}|{venue}|{year}")

    evidence_mode = "title_and_abstract" if abstract else "title_only"

    result = classify_with_json_mode(
        client, taxonomy, system_prompt,
        title, abstract=abstract, year=year, venue=venue,
    )

    if result is None:
        return {
            "paper_id": paper_id,
            "title": title,
            "venue": venue,
            "year": year,
            "scenario": [],
            "mechanism": [],
            "method": [],
            "primary_topic": "other",
            "primary_label": "Other",
            "all_topics": {"other": 1.0},
            "multi_topic": False,
            "evidence": {"scenario": {}, "mechanism": {}, "method": {}},
            "confidence": {"scenario": "low", "mechanism": "low", "method": "low"},
            "evidence_mode": evidence_mode,
            "uncertain": True,
            "classification_error": "all_retries_failed",
        }

    mechanism_labels = result.get("mechanism", [])
    primary_topic = mechanism_labels[0] if mechanism_labels else "other"
    mech_values = taxonomy["axes"]["mechanism"]["values"]
    primary_label = mech_values[primary_topic]["label"] if primary_topic != "other" and primary_topic in mech_values else "Other"

    if mechanism_labels:
        all_topics = {m: 1.0 for m in mechanism_labels}
        total = sum(all_topics.values())
        all_topics = {k: round(v / total, 4) for k, v in all_topics.items()}
    else:
        all_topics = {"other": 1.0}

    return {
        "paper_id": paper_id,
        "title": title,
        "venue": venue,
        "year": year,
        "scenario": result.get("scenario", []),
        "mechanism": mechanism_labels,
        "method": result.get("method", []),
        "primary_topic": primary_topic,
        "primary_label": primary_label,
        "all_topics": all_topics,
        "multi_topic": len(mechanism_labels) > 1,
        "evidence": result.get("evidence", {}),
        "confidence": result.get("confidence", {}),
        "evidence_mode": evidence_mode,
        "uncertain": result.get("uncertain", True),
    }


def build_taxonomy_labels(taxonomy: dict[str, Any]) -> dict[str, dict[str, str]]:
    """Build human-readable label lookup from taxonomy."""
    out: dict[str, dict[str, str]] = {}
    for axis_key, axis in taxonomy.get("axes", {}).items():
        out[axis_key] = {}
        for key, val in axis.get("values", {}).items():
            out[axis_key][key] = val["label"]
    return out


def main() -> None:
    api_key = os.environ.get("DS_API_KEY")
    if not api_key:
        print("ERROR: DS_API_KEY environment variable is not set.")
        print("Set it with: export DS_API_KEY=sk-...")
        sys.exit(1)

    taxonomy = load_taxonomy(str(TAXONOMY_PATH))
    if not taxonomy:
        print(f"ERROR: Taxonomy file {TAXONOMY_PATH} not found or empty.")
        sys.exit(1)

    print(f"Loaded taxonomy v{taxonomy.get('version', 'unknown')}")
    for axis_key in ["scenario", "mechanism", "method"]:
        axis = taxonomy["axes"][axis_key]
        n = len(axis["values"])
        print(f"  {axis['label']}: {n} values")

    # Pre-build the system prompt (same for all papers, includes taxonomy + schema)
    system_prompt = build_system_prompt(taxonomy)

    # Load papers
    clean_data = load_json(INPUT_PAPERS, {"papers": []})
    all_papers = clean_data.get("papers", [])
    papers = [p for p in all_papers if p.get("included_in_new_core_scope")]
    print(f"Loaded {len(papers)} included papers from {INPUT_PAPERS}")

    # Load abstracts
    abstracts_data = load_json(INPUT_ABSTRACTS, {"abstracts": {}})
    abstracts = abstracts_data.get("abstracts", {})
    abstract_count = sum(1 for a in abstracts.values() if a.get("abstract"))
    print(f"Loaded abstracts: {abstract_count} with content from {INPUT_ABSTRACTS}")

    # Load progress
    progress = load_json(PROGRESS_FILE, {"classified": {}})
    classified = progress.get("classified", {})

    pending = [p for p in papers if p["paper_id"] not in classified]
    print(f"Already classified: {len(classified)}")
    print(f"Pending: {len(pending)}")

    if not pending:
        print("All papers already classified.")
        return

    taxonomy_labels = build_taxonomy_labels(taxonomy)

    # Initialize client
    client = OpenAI(api_key=api_key, base_url=DEEPSEEK_BASE_URL, max_retries=2)

    print(f"Classifying with {MAX_WORKERS} concurrent workers, model={MODEL}")
    print("Press Ctrl+C to stop -- progress is saved every 50 papers.\n")

    def classify_one(paper: dict[str, Any]) -> tuple[str, dict[str, Any]]:
        """Wrapper: classify a single paper (called from thread pool)."""
        thread_client = OpenAI(api_key=api_key, base_url=DEEPSEEK_BASE_URL, max_retries=2)
        paper_id = paper["paper_id"]
        abs_info = abstracts.get(paper_id, {})
        abstract = abs_info.get("abstract") if abs_info else None
        result = classify_single_paper(thread_client, taxonomy, system_prompt, paper, abstract=abstract)
        return paper_id, result

    done = 0
    uncertain_count = 0

    try:
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = {}
            for i, paper in enumerate(pending):
                future = executor.submit(classify_one, paper)
                futures[future] = paper["paper_id"]
                if i % MAX_WORKERS == 0 and i > 0:
                    time.sleep(0.1)

            for future in as_completed(futures):
                paper_id = futures[future]
                try:
                    pid, result = future.result()
                    classified[pid] = result
                    done += 1
                    if result.get("uncertain"):
                        uncertain_count += 1

                    scenario_str = "+".join(result.get("scenario", [])) or "?"
                    mech_str = "+".join(result.get("mechanism", [])) or "?"
                    conf = result.get("confidence", {})
                    conf_str = f"s{conf.get('scenario','?')[0]}m{conf.get('mechanism','?')[0]}t{conf.get('method','?')[0]}"
                    mode = "A" if result.get("evidence_mode") == "title_and_abstract" else "T"
                    print(f"  [{done}/{len(pending)}] {mode} {conf_str} [{scenario_str}] [{mech_str}] {result['title'][:70]}")

                except Exception as e:
                    done += 1
                    uncertain_count += 1
                    classified[paper_id] = {
                        "paper_id": paper_id,
                        "title": "ERROR",
                        "scenario": [], "mechanism": [], "method": [],
                        "primary_topic": "other", "primary_label": "Other",
                        "all_topics": {"other": 1.0}, "multi_topic": False,
                        "evidence": {}, "confidence": {"scenario": "low", "mechanism": "low", "method": "low"},
                        "evidence_mode": "title_only",
                        "uncertain": True, "classification_error": str(e),
                    }
                    print(f"  [{done}/{len(pending)}] ERROR: {paper_id[:70]}: {e}")

                if done % CHECKPOINT_INTERVAL == 0:
                    save_output(classified, taxonomy, taxonomy_labels, system_prompt)
                    print(f"  --- checkpoint {len(classified)} papers saved ---")

    except KeyboardInterrupt:
        print("\nInterrupted. Saving progress...")
        save_output(classified, taxonomy, taxonomy_labels, system_prompt)
        print(f"Saved {len(classified)} classified papers. Resume by running again.")
        return

    save_output(classified, taxonomy, taxonomy_labels, system_prompt)

    total = len(classified)
    abs_count = sum(1 for r in classified.values() if r.get("evidence_mode") == "title_and_abstract")
    zero_mech = sum(1 for r in classified.values() if not r.get("mechanism"))
    zero_scenario = sum(1 for r in classified.values() if not r.get("scenario"))

    print(f"\n{'='*60}")
    print(f"Classification complete: {total} papers")
    print(f"  Model: {MODEL}")
    print(f"  With abstracts: {abs_count} ({abs_count/total*100:.1f}%)" if total else "")
    print(f"  Uncertain: {uncertain_count} ({uncertain_count/total*100:.1f}%)" if total else "")
    print(f"  Zero mechanism labels: {zero_mech}")
    print(f"  Zero scenario labels: {zero_scenario}")

    for axis_key, axis_label in [("scenario", "Scenario"), ("mechanism", "Mechanism"), ("method", "Method")]:
        counts: Counter[str] = Counter()
        for r in classified.values():
            for label in r.get(axis_key, []):
                counts[label] += 1
        print(f"\n  {axis_label} distribution (top 10):")
        for label, count in counts.most_common(10):
            pct = count / total * 100 if total else 0
            human = taxonomy_labels.get(axis_key, {}).get(label, label)
            print(f"    {label} ({human}): {count} ({pct:.1f}%)")


def save_output(
    classified: dict[str, dict[str, Any]],
    taxonomy: dict[str, Any],
    labels: dict[str, dict[str, str]],
    system_prompt: str = "",
) -> None:
    """Save progress and final output."""
    save_json(PROGRESS_FILE, {
        "metadata": {
            "model": MODEL,
            "api": "deepseek",
            "taxonomy_version": taxonomy.get("version"),
            "total_classified": len(classified),
        },
        "classified": classified,
    })

    papers_list = sorted(
        classified.values(),
        key=lambda r: (r.get("year", 0), r.get("venue", ""), r.get("title", "")),
    )

    scenario_counts: Counter[str] = Counter()
    mechanism_counts: Counter[str] = Counter()
    method_counts: Counter[str] = Counter()
    venue_year_counts: dict[str, dict[str, dict[str, float]]] = defaultdict(
        lambda: defaultdict(lambda: defaultdict(float))
    )

    for r in papers_list:
        vy_key = f"{r.get('venue', '?')}|{r.get('year', 0)}"
        for s in r.get("scenario", []):
            scenario_counts[s] += 1
            venue_year_counts[vy_key]["scenario"][s] += 1
        for m in r.get("mechanism", []):
            mechanism_counts[m] += 1
            venue_year_counts[vy_key]["mechanism"][m] += 1
        for m in r.get("method", []):
            method_counts[m] += 1
            venue_year_counts[vy_key]["method"][m] += 1

    venue_vectors = []
    for vy_key in sorted(venue_year_counts.keys()):
        venue, year_str = vy_key.split("|")
        year = int(year_str)
        axis_counts = venue_year_counts[vy_key]
        vector = {}
        for axis_key in ["scenario", "mechanism", "method"]:
            axis_total = sum(axis_counts.get(axis_key, {}).values())
            for key in taxonomy["axes"][axis_key]["values"]:
                count = axis_counts.get(axis_key, {}).get(key, 0)
                vector[f"{axis_key}_{key}"] = round(
                    count / axis_total * 100, 2
                ) if axis_total > 0 else 0.0

        venue_vectors.append({
            "venue": venue,
            "year": year,
            "paper_count": sum(1 for r in papers_list
                             if f"{r.get('venue', '?')}|{r.get('year', 0)}" == vy_key),
            "topic_shares": vector,
        })

    output = {
        "metadata": {
            "phase": "topic_classification_v3",
            "method": "llm_json_mode",
            "model": MODEL,
            "api": "deepseek",
            "taxonomy_version": taxonomy.get("version"),
            "input_source": "data/new_core_clean_papers.json",
            "abstract_source": "data/paper_abstracts.json",
            "total_papers": len(papers_list),
        },
        "taxonomy": taxonomy,
        "label_distributions": {
            "scenario": dict(scenario_counts.most_common()),
            "mechanism": dict(mechanism_counts.most_common()),
            "method": dict(method_counts.most_common()),
        },
        "venue_vectors": sorted(venue_vectors, key=lambda x: (x["venue"], x["year"])),
        "papers": papers_list,
    }
    save_json(OUTPUT_LABELS, output)


def classify_title(
    title: str,
    abstract: str | None = None,
    taxonomy: dict[str, Any] | None = None,
    venue: str | None = None,
    year: int | None = None,
) -> dict[str, Any]:
    """Classify a single paper by title (+ optional abstract).

    This is the primary public API. Returns a dict with backward-compatible fields
    (primary_topic, primary_label, all_topics, multi_topic) plus new v3 fields
    (scenario, mechanism, method, evidence, confidence, evidence_mode).

    Requires DS_API_KEY in environment.
    """
    if taxonomy is None:
        taxonomy = load_taxonomy(str(TAXONOMY_PATH))

    api_key = os.environ.get("DS_API_KEY")
    if not api_key:
        raise RuntimeError("DS_API_KEY environment variable is not set")

    client = OpenAI(api_key=api_key, base_url=DEEPSEEK_BASE_URL, max_retries=2)
    system_prompt = build_system_prompt(taxonomy)
    return classify_single_paper(
        client, taxonomy, system_prompt,
        {"title": title, "venue": venue or "", "year": year or 0, "paper_id": f"api:{title[:50]}"},
        abstract=abstract,
    )


def matched_keywords(title: str) -> dict[str, list[str]]:
    """Backward-compatible shim. In v3, returns empty dict (no keywords)."""
    return {}


if __name__ == "__main__":
    main()
