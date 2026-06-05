#!/usr/bin/env python3
"""NVIDIA Academia-Ecosystem Analysis: domain, collaboration, and product transfer report.

Produces 14 charts (PNG), 3 structured JSON analysis files, and prints a summary report.
See ANALYSIS_PLAN.md for the full design.

Usage:
  python analyze_transfer.py          # full run
  python analyze_transfer.py --skip-plots  # JSON + stdout only
"""

from __future__ import annotations

import json
import re
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=1.1)

# --- Paths ---
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
INDEX_PATH = REPO_ROOT / "index" / "all_papers.json"
PAPERS_DIR = REPO_ROOT / "papers"
TRANSFER_PATH = Path(__file__).resolve().parent / "transfer" / "blog_transfer_evidence.json"
VERIFIED_TRANSFER_PATH = Path(__file__).resolve().parent / "analysis" / "verified_transfers.json"
FIGURES_DIR = Path(__file__).resolve().parent / "figures"
ANALYSIS_DIR = Path(__file__).resolve().parent / "analysis"

# --- Constants ---
GPT_THRESHOLD = 2022.5
ERA_PRE, ERA_POST = "Pre-GPT (2020–2022)", "Post-GPT (2023–2026)"
COLOR_NVIDIA = "#76B900"
COLOR_ACADEMIC = "#E69F00"
COLOR_TRANSFER = "#009E73"
COLOR_GRAY = "#999999"
COLOR_PRE = "#5DADE2"
COLOR_POST = "#E74C3C"

TOP_DOMAINS = 15
TOP_SCHOLARS = 30
TOP_PRODUCTS = 20
TOP_VENUES = 10

# --- Product name dictionary ---
KNOWN_PRODUCTS = {
    "nemotron", "tensorrt", "cuda", "isaac", "megatron", "omniverse",
    "nim", "cuquantum", "drive", "sionna", "flare", "earth-2", "nemo",
    "dynamo", "cosmos", "alpamayo", "bionemo", "deepstream", "cuopt",
    "triton", "nccl", "cutlass", "modulus", "morpheus", "monai",
    "rapids", "cuvs", "warp", "rtx", "dlss", "doca", "spectrum-x",
    "bluefield", "maxine", "riva", "clara", "metropolis", "holoscan",
    "groot", "parakeet", "jarvis", "isaac sim", "isaac lab",
    "cuda tile", "cutile", "tensorrt-llm", "nvfp4", "blackwell",
    "dgx", "jetson", "nvlink", "nvbandwidth", "nvsentinel",
}

# Canonical display names (lowercase key -> proper display name)
PRODUCT_DISPLAY = {
    "cuda": "CUDA", "tensorrt": "TensorRT", "tensorrt-llm": "TensorRT-LLM",
    "nemo": "NeMo", "parakeet": "NeMo Parakeet", "jarvis": "Jarvis",
    "isaac": "Isaac", "isaac sim": "Isaac Sim", "isaac lab": "Isaac Lab",
    "cuquantum": "cuQuantum", "cuopt": "cuOpt", "cutile": "cuTile",
    "cuvs": "cuVS", "cutlass": "CUTLASS", "nccl": "NCCL",
    "sionna": "Sionna", "flare": "FLARE", "nvfp4": "NVFP4",
    "rtx": "RTX", "dlss": "DLSS", "doca": "DOCA", "groot": "GR00T",
    "nvlink": "NVLink", "nvbandwidth": "NVBandwidth", "dgx": "DGX",
    "nvsentinel": "NVSentinel", "bionemo": "BioNeMo",
    "blackwell": "Blackwell", "monai": "MONAI", "rapids": "RAPIDS",
    "nim": "NIM", "maxine": "Maxine", "riva": "Riva", "clara": "Clara",
    # These map cleanly with .title()
}


# Research area to domain mapping (from enrich_nvidia_papers.py)
RESEARCH_AREA_TO_DOMAIN = {
    "Artificial Intelligence and Machine Learning": "AI & Machine Learning",
    "Computer Vision": "Computer Vision",
    "Computer Graphics": "Graphics & Rendering",
    "Robotics": "Robotics & Autonomous",
    "Autonomous Vehicles": "Robotics & Autonomous",
    "Generative AI": "Foundation Models",
    "Computer Architecture": "GPU Architecture",
    "Circuits and VLSI Design": "GPU Architecture",
    "High Performance Computing": "Simulation & HPC",
    "Networking": "Interconnect & Networking",
    "Natural Language Processing": "Foundation Models",
    "Speech Processing": "Foundation Models",
    "Machine Translation": "Foundation Models",
    "Real-Time Rendering": "Graphics & Rendering",
    "VR, AR and Display Technology": "Graphics & Rendering",
    "Programming Languages, Systems and Tools": "CUDA Ecosystem",
    "Algorithms and Numerical Methods": "CUDA Ecosystem",
    "Esports": "Applied Perception",
    "Applied Perception": "Applied Perception",
    "Human Computer Interaction": "Applied Perception",
    "Climate Simulation": "Simulation & HPC",
    "World Simulation": "Simulation & HPC",
    "Quantum Computing": "Quantum Computing",
    "Medical": "Medical Imaging",
    "Telecommunications": "Interconnect & Networking",
    "Storage and Systems": "Data Systems",
    "Physical AI": "Robotics & Autonomous",
    "Hyperscale Graphics": "Graphics & Rendering",
    "Computational Photography and Imaging": "Computer Vision",
    "Resilience and Safety": "Robotics & Autonomous",
    "Security": "Miscellaneous",
    "3D Deep Learning": "Computer Vision",
}


def load_all_data():
    """Phase 1: Load, clean, and cross-reference all data sources."""
    import yaml as _yaml

    # --- 1.1 Load index ---
    with open(INDEX_PATH) as f:
        idx = json.load(f)

    nv_papers_raw = []
    for p in idx["papers"]:
        tags = p.get("tags", [])
        if isinstance(tags, str):
            m = re.search(r'\[(.*)\]', tags)
            tags = [t.strip().strip("'\"") for t in m.group(1).split(",")] if m else []
        if "nvidia-research" not in tags:
            continue
        nv_papers_raw.append(p)

    papers = []
    for p in nv_papers_raw:
        # Normalize tags
        tags = p.get("tags", [])
        if isinstance(tags, str):
            m = re.search(r'\[(.*)\]', tags)
            tags = [t.strip().strip("'\"") for t in m.group(1).split(",")] if m else []
        # Parse date
        date_str = p.get("date", "")
        year = 0
        month = 0
        if date_str and "-" in date_str:
            parts = date_str.split("-")
            try:
                year = int(parts[0])
                month = int(parts[1]) if len(parts) > 1 else 0
            except ValueError:
                pass
        # Venue group
        conf = p.get("conference", "")
        venue_group = re.sub(r'\s*\d{4}$', '', conf).strip() if conf else "Unknown"
        # Research areas -> domains
        research_areas = p.get("research_areas", [])
        domains = set()
        for ra in research_areas:
            domain = RESEARCH_AREA_TO_DOMAIN.get(ra)
            if domain:
                domains.add(domain)
        if not domains:
            domains.add("AI & Machine Learning")
        # Topics
        topics = p.get("topics", [])
        if isinstance(topics, str):
            topics = [topics]

        papers.append({
            "id": p["id"],
            "title": p["title"],
            "conference": conf,
            "venue_group": venue_group,
            "date": date_str,
            "year": year,
            "month": month,
            "era": ERA_PRE if year <= GPT_THRESHOLD else ERA_POST if year > 0 else "Unknown",
            "topics": topics,
            "domains": sorted(domains),
            "research_areas": research_areas,
            "abstract": p.get("abstract", ""),
            "is_industry": p.get("is_industry", True),
            "file": p.get("file", ""),
        })

    print(f"Loaded {len(papers)} NVIDIA papers from index", file=sys.stderr)

    # --- 1.2 Build known-NVIDIA author set from ALL 1060 papers ---
    known_nvidia = set()
    all_papers = idx["papers"]
    broken_yaml_ids = set()

    for p in all_papers:
        file_path = REPO_ROOT / p.get("file", "")
        if not file_path.exists():
            continue
        try:
            with open(file_path) as f:
                content = f.read()
            fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
            if not fm_match:
                continue
            fm = _yaml.safe_load(fm_match.group(1))
            if not fm or not isinstance(fm.get("authors"), list):
                continue
            for a in fm["authors"]:
                if not isinstance(a, dict):
                    continue
                name = a.get("name", "")
                if not name:
                    continue
                is_ind = a.get("is_industry", False)
                aff = (a.get("affiliation") or "").lower()
                if is_ind or "nvidia" in aff:
                    known_nvidia.add(name.lower())
        except Exception:
            broken_yaml_ids.add(p["id"])
            continue

    print(f"Known NVIDIA authors: {len(known_nvidia)}", file=sys.stderr)

    # --- 1.3 Load author data from YAML for the 891 papers ---
    paper_authors = {}
    skipped_authors = 0
    unknown_lead = 0

    for p in papers:
        file_path = REPO_ROOT / p["file"]
        if not file_path.exists() or p["id"] in broken_yaml_ids:
            skipped_authors += 1
            paper_authors[p["id"]] = {
                "authors": [], "lead_type": "unknown",
                "is_solo_nvidia": False, "num_nvidia": 0, "num_academic": 0,
                "first_author": "", "first_author_is_nvidia": False,
            }
            unknown_lead += 1
            continue
        try:
            with open(file_path) as f:
                content = f.read()
            fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
            if not fm_match:
                skipped_authors += 1
                unknown_lead += 1
                paper_authors[p["id"]] = {
                    "authors": [], "lead_type": "unknown",
                    "is_solo_nvidia": False, "num_nvidia": 0, "num_academic": 0,
                    "first_author": "", "first_author_is_nvidia": False,
                }
                continue
            fm = _yaml.safe_load(fm_match.group(1))
            if not fm or not isinstance(fm.get("authors"), list):
                skipped_authors += 1
                unknown_lead += 1
                paper_authors[p["id"]] = {
                    "authors": [], "lead_type": "unknown",
                    "is_solo_nvidia": False, "num_nvidia": 0, "num_academic": 0,
                    "first_author": "", "first_author_is_nvidia": False,
                }
                continue

            authors = []
            for a in fm["authors"]:
                if not isinstance(a, dict):
                    continue
                name = (a.get("name") or "").strip()
                if not name:
                    continue
                authors.append({
                    "name": name,
                    "name_lower": name.lower(),
                    "is_nvidia": name.lower() in known_nvidia,
                    "affiliation": a.get("affiliation", ""),
                })

            if not authors:
                unknown_lead += 1
                paper_authors[p["id"]] = {
                    "authors": [], "lead_type": "unknown",
                    "is_solo_nvidia": False, "num_nvidia": 0, "num_academic": 0,
                    "first_author": "", "first_author_is_nvidia": False,
                }
                continue

            first = authors[0]
            nv_count = sum(1 for a in authors if a["is_nvidia"])
            ac_count = len(authors) - nv_count
            lead = "nvidia_led" if first["is_nvidia"] else "academic_led"

            paper_authors[p["id"]] = {
                "authors": authors,
                "lead_type": lead,
                "is_solo_nvidia": nv_count == len(authors),
                "num_nvidia": nv_count,
                "num_academic": ac_count,
                "first_author": first["name"],
                "first_author_is_nvidia": first["is_nvidia"],
            }
        except Exception:
            skipped_authors += 1
            unknown_lead += 1
            paper_authors[p["id"]] = {
                "authors": [], "lead_type": "unknown",
                "is_solo_nvidia": False, "num_nvidia": 0, "num_academic": 0,
                "first_author": "", "first_author_is_nvidia": False,
            }

    # Attach author data to papers
    for p in papers:
        pa = paper_authors.get(p["id"], {})
        p["authors"] = pa.get("authors", [])
        p["lead_type"] = pa.get("lead_type", "unknown")
        p["is_solo_nvidia"] = pa.get("is_solo_nvidia", False)
        p["num_nvidia_authors"] = pa.get("num_nvidia", 0)
        p["num_academic_authors"] = pa.get("num_academic", 0)
        p["first_author"] = pa.get("first_author", "")
        p["first_author_is_nvidia"] = pa.get("first_author_is_nvidia", False)

    print(f"Author data: {len(papers) - skipped_authors} papers parsed, "
          f"{skipped_authors} skipped, {unknown_lead} unknown lead", file=sys.stderr)

    # --- 1.4 Load transfer evidence (use agent-verified data if available) ---
    verified_transfers = None
    if VERIFIED_TRANSFER_PATH.exists():
        with open(VERIFIED_TRANSFER_PATH) as f:
            verified_transfers = json.load(f)

    # Also load original transfer data for blog counts etc.
    transfer_data = None
    if TRANSFER_PATH.exists():
        with open(TRANSFER_PATH) as f:
            transfer_data = json.load(f)

    # Attach verified transfer evidence to papers
    verified_map = verified_transfers.get("paper_transfers", {}) if verified_transfers else {}
    for p in papers:
        pid = p["id"]
        ev_list = verified_map.get(pid, [])
        p["has_transfer"] = len(ev_list) > 0
        p["transfer_count"] = len(ev_list)
        evidence_types = set()
        products = set()
        for ev in ev_list:
            strength = ev.get("strength", "")
            if strength == "DIRECT":
                evidence_types.add("direct_transfer")
            elif strength == "MODERATE":
                evidence_types.add("moderate_transfer")
            for prod in ev.get("products", []):
                products.add(prod)
        p["evidence_types"] = list(evidence_types)
        p["transfer_products"] = list(products)

    transfer_paper_count = sum(1 for p in papers if p["has_transfer"])
    print(f"Transfer evidence: {transfer_paper_count} papers with blog matches", file=sys.stderr)

    # Print load summary
    lead_counts = Counter(p["lead_type"] for p in papers)
    print(f"  NVIDIA-led: {lead_counts.get('nvidia_led', 0)}, "
          f"Academic-led: {lead_counts.get('academic_led', 0)}, "
          f"Unknown: {lead_counts.get('unknown', 0)}", file=sys.stderr)
    print(f"  Total skipped: {skipped_authors} (broken YAML / missing authors)", file=sys.stderr)

    return papers, transfer_data, known_nvidia


def extract_products(text: str) -> set[str]:
    """Extract NVIDIA product names from text, returning canonical display names."""
    found = set()
    text_lower = text.lower()
    for prod in KNOWN_PRODUCTS:
        if prod in text_lower:
            # Use canonical display name if available, otherwise .title()
            if prod in PRODUCT_DISPLAY:
                found.add(PRODUCT_DISPLAY[prod])
            elif "-" in prod:
                found.add(prod.upper())
            else:
                found.add(prod.title())
    # Regex fallback for uncategorized (e.g., "NVIDIA Sionna Research")
    for m in re.finditer(r'(?:NVIDIA|Nvidia)\s+([A-Z][a-zA-Z0-9]+(?:\s+[A-Z][a-zA-Z0-9]+)?)', text):
        name = m.group(1).strip()
        name_lower = name.lower()
        if len(name) > 2 and name_lower not in {"the", "and", "for", "with", "blog", "research", "technical"}:
            found.add(name)
    # Merge variants: strip trailing "Research" if the base product is already present
    merged = set()
    for name in found:
        if name.endswith(" Research"):
            base = name[:-9]
            if base in found:
                continue  # drop "X Research" variant when "X" already present
        merged.add(name)
    return merged


# ====================================================================
# Phase 2: Domain Analysis
# ====================================================================

def build_domain_analysis(papers):
    """Compute domain statistics."""
    # Domain paper counts
    domain_counter = Counter()
    domain_yearly = defaultdict(Counter)
    domain_era = defaultdict(Counter)
    venue_domain = defaultdict(Counter)

    for p in papers:
        year = p["year"]
        era = p["era"]
        venue = p["venue_group"]
        for d in p["domains"]:
            domain_counter[d] += 1
            if year > 0:
                domain_yearly[year][d] += 1
            domain_era[era][d] += 1
            venue_domain[venue][d] += 1

    results = {
        "domain_distribution": dict(domain_counter.most_common()),
        "domain_by_year": {str(y): dict(domain_yearly[y]) for y in sorted(domain_yearly)},
        "domain_by_era": {era: dict(domain_era[era]) for era in [ERA_PRE, ERA_POST]},
        "top_domains": [d for d, _ in domain_counter.most_common(TOP_DOMAINS)],
    }

    # Growth deltas (pre vs post GPT)
    growth = []
    for domain in domain_counter:
        pre = domain_era.get(ERA_PRE, {}).get(domain, 0)
        post = domain_era.get(ERA_POST, {}).get(domain, 0)
        delta = post - pre
        pct = (delta / pre * 100) if pre > 0 else (float('inf') if post > 0 else 0)
        growth.append({"domain": domain, "pre_gpt": pre, "post_gpt": post, "delta": delta, "pct_change": pct})
    growth.sort(key=lambda x: -x["delta"])
    results["domain_growth"] = growth

    # Venue-domain matrix
    top_venues = sorted(venue_domain.keys(),
                        key=lambda v: sum(venue_domain[v].values()), reverse=True)[:TOP_VENUES]
    results["venue_domain_matrix"] = {}
    for v in top_venues:
        results["venue_domain_matrix"][v] = dict(venue_domain[v])

    return results


def plot_domain_charts(results, papers):
    """Generate 5 domain analysis charts."""
    domains = results["top_domains"]
    domain_yearly = results["domain_by_year"]
    growth = results["domain_growth"]
    years = sorted(int(y) for y in domain_yearly if y.isdigit())

    # Chart 1: Static distribution
    fig, ax = plt.subplots(figsize=(10, 8))
    pre_counts = [results["domain_by_era"].get(ERA_PRE, {}).get(d, 0) for d in domains]
    post_counts = [results["domain_by_era"].get(ERA_POST, {}).get(d, 0) for d in domains]
    y_pos = range(len(domains))
    ax.barh(y_pos, pre_counts, label=ERA_PRE, color=COLOR_PRE, alpha=0.85)
    ax.barh(y_pos, post_counts, left=pre_counts, label=ERA_POST, color=COLOR_POST, alpha=0.85)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(domains)
    ax.set_xlabel("Paper Count")
    ax.set_title("Domain Distribution (Pre/Post GPT)")
    ax.legend(loc="lower right")
    ax.invert_yaxis()
    plt.tight_layout()
    fig.savefig(FIGURES_DIR / "domain_static_distribution.png", dpi=150)
    plt.close(fig)

    # Chart 2: Temporal stacked area
    fig, ax = plt.subplots(figsize=(12, 6))
    top10 = domains[:10]
    yearly_data = {d: [domain_yearly.get(str(y), {}).get(d, 0) for y in years] for d in top10}
    ax.stackplot(years, *yearly_data.values(), labels=yearly_data.keys(), alpha=0.8)
    ax.axvline(x=GPT_THRESHOLD, color="black", linestyle="--", linewidth=1.5, alpha=0.7)
    ax.text(GPT_THRESHOLD + 0.1, ax.get_ylim()[1] * 0.95, "GPT Moment", fontsize=9, color="black")
    ax.set_xlabel("Year")
    ax.set_ylabel("Paper Count")
    ax.set_title("Research Domain Evolution (2020–2026)")
    ax.legend(loc="upper left", fontsize=8, ncol=2)
    plt.tight_layout()
    fig.savefig(FIGURES_DIR / "domain_temporal_stacked_area.png", dpi=150)
    plt.close(fig)

    # Chart 3: GPT shift scatter
    fig, ax = plt.subplots(figsize=(10, 8))
    for g in growth:
        if g["pre_gpt"] + g["post_gpt"] < 5:
            continue
        ax.scatter(g["pre_gpt"], g["post_gpt"], s=max(20, g["pre_gpt"] + g["post_gpt"]),
                   alpha=0.6, color="#3498DB")
    # Diagonal
    max_val = max(max(g["pre_gpt"], g["post_gpt"]) for g in growth)
    ax.plot([0, max_val], [0, max_val], "k--", alpha=0.3, linewidth=1)
    # Annotate biggest movers
    for g in growth:
        if abs(g["delta"]) >= 30 and g["pre_gpt"] + g["post_gpt"] >= 10:
            ax.annotate(g["domain"], (g["pre_gpt"], g["post_gpt"]),
                        fontsize=8, alpha=0.9,
                        xytext=(5, 5), textcoords="offset points")
    ax.set_xlabel(f"Papers ({ERA_PRE})")
    ax.set_ylabel(f"Papers ({ERA_POST})")
    ax.set_title("Domain Shift: Pre vs Post GPT")
    plt.tight_layout()
    fig.savefig(FIGURES_DIR / "domain_gpt_shift.png", dpi=150)
    plt.close(fig)

    # Chart 4: Key domain trends (line chart)
    fig, ax = plt.subplots(figsize=(12, 6))
    key_domains = ["AI & Machine Learning", "Foundation Models", "Computer Vision",
                   "Robotics & Autonomous", "Graphics & Rendering", "GPU Architecture"]
    colors = ["#3498DB", "#E74C3C", "#2ECC71", "#F39C12", "#9B59B6", "#1ABC9C"]
    for domain, color in zip(key_domains, colors):
        counts = [domain_yearly.get(str(y), {}).get(domain, 0) for y in years]
        ax.plot(years, counts, marker="o", label=domain, color=color, linewidth=2)
    ax.axvline(x=GPT_THRESHOLD, color="black", linestyle="--", linewidth=1.5, alpha=0.6)
    ax.text(GPT_THRESHOLD + 0.1, ax.get_ylim()[1] * 0.95, "GPT", fontsize=9)
    ax.set_xlabel("Year")
    ax.set_ylabel("Paper Count")
    ax.set_title("Key Domain Trends (2020–2026)")
    ax.legend(fontsize=8)
    plt.tight_layout()
    fig.savefig(FIGURES_DIR / "domain_key_trends.png", dpi=150)
    plt.close(fig)

    # Chart 5: Venue-Domain heatmap
    matrix = results["venue_domain_matrix"]
    if matrix:
        heat_domains = domains[:TOP_DOMAINS]
        heat_venues = list(matrix.keys())[:TOP_VENUES]
        heat_data = [[matrix[v].get(d, 0) for d in heat_domains] for v in heat_venues]
        fig, ax = plt.subplots(figsize=(14, 8))
        sns.heatmap(heat_data, annot=True, fmt="d", cmap="YlOrRd",
                    xticklabels=heat_domains, yticklabels=heat_venues,
                    ax=ax, linewidths=0.5, cbar_kws={"label": "Papers"})
        ax.set_title("Research Domain × Publication Venue")
        ax.set_xlabel("Domain")
        ax.set_ylabel("Venue")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        fig.savefig(FIGURES_DIR / "domain_venue_heatmap.png", dpi=150)
        plt.close(fig)


# ====================================================================
# Phase 3: Collaboration Analysis
# ====================================================================

def build_collaboration_analysis(papers):
    """Compute academic collaboration statistics."""
    lead_counter = Counter()
    lead_yearly = defaultdict(Counter)
    lead_domain = defaultdict(Counter)
    solo_count = 0
    collab_count = 0
    academic_author_counter = Counter()
    institution_counter = Counter()
    total_nv = 0
    total_ac = 0
    author_paper_count = 0

    for p in papers:
        lt = p["lead_type"]
        lead_counter[lt] += 1
        if p["year"] > 0:
            lead_yearly[p["year"]][lt] += 1
        for d in p["domains"]:
            lead_domain[d][lt] += 1
        if p["is_solo_nvidia"]:
            solo_count += 1
        if p["num_academic_authors"] > 0:
            collab_count += 1
        total_nv += p["num_nvidia_authors"]
        total_ac += p["num_academic_authors"]
        author_paper_count += len(p["authors"])

        for a in p["authors"]:
            if not a["is_nvidia"]:
                academic_author_counter[a["name"]] += 1
            aff = a.get("affiliation", "")
            if aff and aff.lower() != "nvidia" and aff.lower() not in ("", "tbd"):
                institution_counter[aff] += 1

    avg_nv = total_nv / len(papers) if papers else 0
    avg_ac = total_ac / len(papers) if papers else 0

    results = {
        "lead_type_distribution": dict(lead_counter),
        "solo_nvidia_papers": solo_count,
        "collaborative_papers": collab_count,
        "lead_type_by_year": {str(y): dict(lead_yearly[y]) for y in sorted(lead_yearly)},
        "lead_type_by_domain": {d: dict(lead_domain[d]) for d in lead_domain},
        "domains_most_academic": sorted(
            lead_domain.keys(),
            key=lambda d: lead_domain[d].get("academic_led", 0) / max(sum(lead_domain[d].values()), 1),
            reverse=True
        )[:10],
        "top_academic_collaborators": [
            {"name": name, "papers": count}
            for name, count in academic_author_counter.most_common(TOP_SCHOLARS)
        ],
        "top_institutions": [
            {"name": name, "papers": count}
            for name, count in institution_counter.most_common(20)
        ],
        "avg_nvidia_authors_per_paper": round(avg_nv, 1),
        "avg_academic_authors_per_paper": round(avg_ac, 1),
    }
    return results


def plot_collaboration_charts(results, papers):
    """Generate 4 collaboration charts."""
    # Chart 6: Lead type pie
    fig, ax = plt.subplots(figsize=(7, 7))
    lt = results["lead_type_distribution"]
    labels = [f"NVIDIA-led\n({lt.get('nvidia_led', 0)})",
              f"Academic-led\n({lt.get('academic_led', 0)})",
              f"Unknown\n({lt.get('unknown', 0)})"]
    sizes = [lt.get("nvidia_led", 0), lt.get("academic_led", 0), lt.get("unknown", 0)]
    colors_pie = [COLOR_NVIDIA, COLOR_ACADEMIC, COLOR_GRAY]
    wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors_pie,
                                       autopct="%1.1f%%", startangle=90,
                                       explode=(0.02, 0.05, 0.1))
    for at in autotexts:
        at.set_fontsize(10)
        at.set_fontweight("bold")
    ax.set_title("Paper Leadership: NVIDIA vs Academic First Author")
    plt.tight_layout()
    fig.savefig(FIGURES_DIR / "collaboration_lead_pie.png", dpi=150)
    plt.close(fig)

    # Chart 7: Temporal split
    fig, ax = plt.subplots(figsize=(10, 6))
    yearly = results["lead_type_by_year"]
    years = sorted(int(y) for y in yearly if y.isdigit())
    nv_vals = [yearly[str(y)].get("nvidia_led", 0) for y in years]
    ac_vals = [yearly[str(y)].get("academic_led", 0) for y in years]
    unk_vals = [yearly[str(y)].get("unknown", 0) for y in years]
    ax.bar(years, nv_vals, label="NVIDIA-led", color=COLOR_NVIDIA, alpha=0.85)
    ax.bar(years, ac_vals, bottom=nv_vals, label="Academic-led", color=COLOR_ACADEMIC, alpha=0.85)
    ax.bar(years, unk_vals, bottom=[a + b for a, b in zip(nv_vals, ac_vals)],
           label="Unknown", color=COLOR_GRAY, alpha=0.5)
    ax.axvline(x=GPT_THRESHOLD, color="black", linestyle="--", linewidth=1.5, alpha=0.6)
    ax.set_xlabel("Year")
    ax.set_ylabel("Paper Count")
    ax.set_title("Leadership Composition Over Time")
    ax.legend()
    plt.tight_layout()
    fig.savefig(FIGURES_DIR / "collaboration_temporal_split.png", dpi=150)
    plt.close(fig)

    # Chart 8: By domain
    domain_data = results["lead_type_by_domain"]
    top_domains_collab = sorted(domain_data.keys(),
                                key=lambda d: sum(domain_data[d].values()), reverse=True)[:TOP_DOMAINS]
    fig, ax = plt.subplots(figsize=(10, 8))
    y_pos = range(len(top_domains_collab))
    nv_d = [domain_data[d].get("nvidia_led", 0) for d in top_domains_collab]
    ac_d = [domain_data[d].get("academic_led", 0) for d in top_domains_collab]
    ax.barh(y_pos, nv_d, label="NVIDIA-led", color=COLOR_NVIDIA, alpha=0.85)
    ax.barh(y_pos, ac_d, left=nv_d, label="Academic-led", color=COLOR_ACADEMIC, alpha=0.85)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(top_domains_collab)
    ax.set_xlabel("Paper Count")
    ax.set_title("Leadership by Research Domain")
    ax.legend(loc="lower right")
    ax.invert_yaxis()
    plt.tight_layout()
    fig.savefig(FIGURES_DIR / "collaboration_by_domain.png", dpi=150)
    plt.close(fig)

    # Chart 9: Top scholars
    scholars = results["top_academic_collaborators"][:TOP_SCHOLARS]
    fig, ax = plt.subplots(figsize=(10, 10))
    names = [s["name"] for s in reversed(scholars)]
    counts = [s["papers"] for s in reversed(scholars)]
    ax.barh(names, counts, color=COLOR_ACADEMIC, alpha=0.85)
    ax.set_xlabel("Co-authored Papers")
    ax.set_title("Top 30 Academic Collaborators")
    plt.tight_layout()
    fig.savefig(FIGURES_DIR / "collaboration_top_scholars.png", dpi=150)
    plt.close(fig)


# ====================================================================
# Phase 4: Transfer Analysis
# ====================================================================

def build_transfer_analysis(papers, transfer_data):
    """Compute product transfer statistics."""
    evidence_counter = Counter()
    evidence_era = defaultdict(Counter)
    domain_transfer = defaultdict(lambda: {"total": 0, "transferred": 0})
    product_counter = Counter()
    transfer_scholar_counter = Counter()
    transfer_scholar_nv = {}
    transfer_yearly = Counter()
    paper_yearly = Counter()

    for p in papers:
        year = p["year"]
        if year > 0:
            paper_yearly[year] += 1
        for d in p["domains"]:
            domain_transfer[d]["total"] += 1
            if p["has_transfer"]:
                domain_transfer[d]["transferred"] += 1
        if p["has_transfer"]:
            if year > 0:
                transfer_yearly[year] += 1
            for et in p["evidence_types"]:
                evidence_counter[et] += 1
                if p["era"] in (ERA_PRE, ERA_POST):
                    evidence_era[p["era"]][et] += 1
            for prod in p["transfer_products"]:
                product_counter[prod] += 1
            for a in p["authors"]:
                transfer_scholar_counter[a["name"]] += 1
                transfer_scholar_nv[a["name"]] = a["is_nvidia"]

    # Count unique blogs from verified transfer data
    verified_map = {}
    if VERIFIED_TRANSFER_PATH.exists():
        with open(VERIFIED_TRANSFER_PATH) as f:
            vf = json.load(f)
        verified_map = vf.get("paper_transfers", {})

    unique_blog_urls = set()
    for pids, evs in verified_map.items():
        for ev in evs:
            if ev.get("url"):
                unique_blog_urls.add(ev["url"])
    total_blogs = len(unique_blog_urls)

    results = {
        "summary": {
            "total_papers": len(papers),
            "papers_with_transfer": sum(1 for p in papers if p["has_transfer"]),
            "transfer_rate": round(sum(1 for p in papers if p["has_transfer"]) / len(papers) * 100, 1),
            "total_blog_posts": total_blogs,
            "total_match_pairs": sum(len(v) for v in verified_map.values()),
        },
        "evidence_type_distribution": dict(evidence_counter),
        "evidence_by_era": {era: dict(evidence_era[era]) for era in [ERA_PRE, ERA_POST]},
        "transfer_by_domain": [
            {"domain": d, "total": v["total"], "transferred": v["transferred"],
             "rate": round(v["transferred"] / v["total"] * 100, 1) if v["total"] > 0 else 0}
            for d, v in sorted(domain_transfer.items(), key=lambda x: -x[1]["total"])
        ],
        "transfer_by_year": {str(y): transfer_yearly[y] for y in sorted(transfer_yearly)},
        "paper_by_year": {str(y): paper_yearly[y] for y in sorted(paper_yearly)},
        "top_products": [
            {"product": p, "paper_count": c}
            for p, c in product_counter.most_common(TOP_PRODUCTS)
        ],
        "top_transfer_scholars": [
            {"name": name, "is_nvidia": transfer_scholar_nv.get(name, False),
             "transferred_papers": count}
            for name, count in transfer_scholar_counter.most_common(TOP_SCHOLARS)
        ],
    }
    # Best transfer rate domains
    results["domains_highest_transfer_rate"] = sorted(
        results["transfer_by_domain"], key=lambda x: -x["rate"]
    )[:10]
    # Avg blogs per transferred paper
    n_transferred = max(results["summary"]["papers_with_transfer"], 1)
    results["summary"]["avg_blogs_per_transferred_paper"] = round(results["summary"]["total_match_pairs"] / n_transferred, 1)

    return results


def plot_transfer_charts(results, papers):
    """Generate 5 transfer charts."""
    # Chart 10: Transfer strength by era (verified: DIRECT vs MODERATE)
    fig, ax = plt.subplots(figsize=(8, 5))
    ev_era = results["evidence_by_era"]
    ev_types = ["direct_transfer", "moderate_transfer"]
    ev_labels = ["Direct Transfer\n(blog = paper + product)", "Moderate Transfer\n(blog = same research line)"]
    pre_vals = [ev_era.get(ERA_PRE, {}).get(et, 0) for et in ev_types]
    post_vals = [ev_era.get(ERA_POST, {}).get(et, 0) for et in ev_types]
    x_pos = range(len(ev_types))
    width = 0.35
    ax.bar([x - width / 2 for x in x_pos], pre_vals, width, label=ERA_PRE, color=COLOR_PRE, alpha=0.85)
    ax.bar([x + width / 2 for x in x_pos], post_vals, width, label=ERA_POST, color=COLOR_POST, alpha=0.85)
    ax.set_xticks(x_pos)
    ax.set_xticklabels(ev_labels)
    ax.set_ylabel("Paper Count")
    ax.set_title("Verified Transfer Strength by Era (Agent-Reviewed)")
    ax.legend()
    plt.tight_layout()
    fig.savefig(FIGURES_DIR / "transfer_evidence_types.png", dpi=150)
    plt.close(fig)

    # Chart 11: Transfer by domain
    domain_list = results["transfer_by_domain"][:TOP_DOMAINS]
    fig, ax = plt.subplots(figsize=(10, 8))
    domains_d = [d["domain"] for d in reversed(domain_list)]
    transferred = [d["transferred"] for d in reversed(domain_list)]
    not_transferred = [d["total"] - d["transferred"] for d in reversed(domain_list)]
    ax.barh(domains_d, transferred, label="With Transfer Evidence", color=COLOR_TRANSFER, alpha=0.85)
    ax.barh(domains_d, not_transferred, left=transferred,
            label="No Transfer Evidence", color=COLOR_GRAY, alpha=0.4)
    # Annotate rates
    for i, d in enumerate(reversed(domain_list)):
        if d["total"] > 0:
            ax.text(d["total"] + 5, i, f"{d['rate']}%", va="center", fontsize=8)
    ax.set_xlabel("Paper Count")
    ax.set_title("Transfer Evidence Coverage by Research Domain")
    ax.legend(loc="lower right")
    plt.tight_layout()
    fig.savefig(FIGURES_DIR / "transfer_by_domain.png", dpi=150)
    plt.close(fig)

    # Chart 12: Top products
    products = results["top_products"][:TOP_PRODUCTS]
    fig, ax = plt.subplots(figsize=(10, 8))
    prod_names = [p["product"] for p in reversed(products)]
    prod_counts = [p["paper_count"] for p in reversed(products)]
    ax.barh(prod_names, prod_counts, color=COLOR_TRANSFER, alpha=0.85)
    ax.set_xlabel("Associated Paper Count")
    ax.set_title("Top Products Associated with Research Papers")
    plt.tight_layout()
    fig.savefig(FIGURES_DIR / "transfer_top_products.png", dpi=150)
    plt.close(fig)

    # Chart 13: Transfer temporal
    fig, ax = plt.subplots(figsize=(10, 6))
    paper_yearly = results["paper_by_year"]
    transfer_yearly = results["transfer_by_year"]
    years = sorted(int(y) for y in paper_yearly if y.isdigit())
    paper_vals = [paper_yearly.get(str(y), 0) for y in years]
    transfer_vals = [transfer_yearly.get(str(y), 0) for y in years]
    ax.plot(years, paper_vals, marker="o", label="Papers Published", color="#3498DB", linewidth=2)
    ax.plot(years, transfer_vals, marker="s", label="Papers with Blog Transfer", color=COLOR_TRANSFER, linewidth=2)
    ax.axvline(x=GPT_THRESHOLD, color="black", linestyle="--", linewidth=1.5, alpha=0.6)
    ax.text(GPT_THRESHOLD + 0.1, max(paper_vals) * 0.95, "GPT", fontsize=9)
    ax.set_xlabel("Year")
    ax.set_ylabel("Paper Count")
    ax.set_title("Research Output vs Blog Transfer Evidence")
    ax.legend()
    plt.tight_layout()
    fig.savefig(FIGURES_DIR / "transfer_temporal.png", dpi=150)
    plt.close(fig)

    # Chart 14: Transfer scholar contribution
    scholars = results["top_transfer_scholars"][:25]
    fig, ax = plt.subplots(figsize=(10, 9))
    names = [s["name"] for s in reversed(scholars)]
    counts = [s["transferred_papers"] for s in reversed(scholars)]
    colors_s = [COLOR_NVIDIA if s["is_nvidia"] else COLOR_ACADEMIC for s in reversed(scholars)]
    ax.barh(names, counts, color=colors_s, alpha=0.85)
    # Legend
    from matplotlib.patches import Patch
    legend_elements = [Patch(facecolor=COLOR_NVIDIA, label="NVIDIA"),
                       Patch(facecolor=COLOR_ACADEMIC, label="Academic")]
    ax.legend(handles=legend_elements, loc="lower right")
    ax.set_xlabel("Transferred Paper Count")
    ax.set_title("Top 25 Scholars by Transfer Evidence")
    plt.tight_layout()
    fig.savefig(FIGURES_DIR / "transfer_scholar_contribution.png", dpi=150)
    plt.close(fig)


# ====================================================================
# Phase 5: Summary Report
# ====================================================================

def print_summary_report(domain_results, collab_results, transfer_results):
    """Print a structured summary report to stdout."""
    s = transfer_results["summary"]
    growth = domain_results["domain_growth"]

    print("\n" + "=" * 80)
    print("  NVIDIA Academia-Ecosystem Analysis Report (2020–2026)")
    print("=" * 80)

    # 1. Domain Landscape
    print("\n1. DOMAIN LANDSCAPE")
    print("-" * 40)
    print("   Top research domains:")
    for i, (domain, count) in enumerate(domain_results["domain_distribution"].items()):
        if i >= 10:
            break
        print(f"     {domain}: {count} papers")
    print(f"\n   Biggest post-GPT surges (pre vs post 2022):")
    surge_count = 0
    for g in growth:
        if g["pre_gpt"] > 0 and g["post_gpt"] > 0 and g["delta"] > 0:
            print(f"     {g['domain']}: {g['pre_gpt']} → {g['post_gpt']} (+{g['pct_change']:.0f}%)")
            surge_count += 1
            if surge_count >= 8:
                break
    new_post = [g for g in growth if g["pre_gpt"] == 0 and g["post_gpt"] > 0]
    if new_post:
        print(f"\n   New post-GPT domains:")
        for g in new_post[:5]:
            print(f"     {g['domain']}: {g['post_gpt']} papers (0 pre-GPT)")

    # 2. Academic Collaboration
    print("\n2. ACADEMIC COLLABORATION")
    print("-" * 40)
    lt = collab_results["lead_type_distribution"]
    total_known = lt.get("nvidia_led", 0) + lt.get("academic_led", 0)
    print(f"   NVIDIA-led (first author): {lt.get('nvidia_led', 0)} ({lt.get('nvidia_led', 0) / total_known * 100:.1f}%)")
    print(f"   Academic-led (first author): {lt.get('academic_led', 0)} ({lt.get('academic_led', 0) / total_known * 100:.1f}%)")
    print(f"   Solo NVIDIA (no external co-authors): {collab_results['solo_nvidia_papers']}")
    print(f"   Collaborative papers: {collab_results['collaborative_papers']}")
    print(f"   Avg NVIDIA authors/paper: {collab_results['avg_nvidia_authors_per_paper']}")
    print(f"   Avg academic authors/paper: {collab_results['avg_academic_authors_per_paper']}")
    print(f"\n   Domains with highest academic participation:")
    for d in collab_results["domains_most_academic"][:5]:
        dd = collab_results["lead_type_by_domain"].get(d, {})
        ac = dd.get("academic_led", 0)
        total = sum(dd.values())
        print(f"     {d}: {ac}/{total} academic-led ({ac / total * 100:.0f}%)")
    print(f"\n   Top academic collaborators:")
    for i, scholar in enumerate(collab_results["top_academic_collaborators"][:10]):
        print(f"     {scholar['name']}: {scholar['papers']} papers")

    # 3. Product Transfer
    print("\n3. PRODUCT TRANSFER")
    print("-" * 40)
    print(f"   Papers with blog transfer evidence: {s['papers_with_transfer']}/{s['total_papers']} ({s['transfer_rate']}%)")
    print(f"   Blog posts scanned: {s['total_blog_posts']}")
    print(f"   Total paper-match pairs: {s['total_match_pairs']}")
    print(f"   Avg blogs per transferred paper: {s['avg_blogs_per_transferred_paper']}")
    print(f"\n   Evidence breakdown:")
    for ev, count in transfer_results["evidence_type_distribution"].items():
        print(f"     {ev}: {count}")
    print(f"\n   Top products by associated papers:")
    for prod in transfer_results["top_products"][:10]:
        print(f"     {prod['product']}: {prod['paper_count']} papers")
    print(f"\n   Domains with highest transfer rates:")
    for d in transfer_results["domains_highest_transfer_rate"][:5]:
        print(f"     {d['domain']}: {d['transferred']}/{d['total']} ({d['rate']}%)")
    print(f"\n   Top transfer-contributing scholars:")
    for s in transfer_results["top_transfer_scholars"][:10]:
        tag = "NVIDIA" if s["is_nvidia"] else "Academic"
        print(f"     {s['name']} ({tag}): {s['transferred_papers']} papers")

    # 4. GPT Moment Shift
    print("\n4. GPT MOMENT SHIFT (pre-2022 vs post-2022)")
    print("-" * 40)
    total_papers_pre = sum(1 for p in papers if p["year"] > 0 and p["year"] <= 2022)
    total_papers_post = sum(1 for p in papers if p["year"] > 2022)
    print(f"   Total papers (unique): {total_papers_pre} pre-GPT → {total_papers_post} post-GPT")
    pre_transfer = sum(1 for p in papers if p["has_transfer"] and p["year"] > 0 and p["year"] <= 2022)
    post_transfer = sum(1 for p in papers if p["has_transfer"] and p["year"] > 2022)
    print(f"   Papers with transfer: {pre_transfer} pre-GPT → {post_transfer} post-GPT")
    print(f"\n   Domain composition shift (top gainers):")
    for g in growth[:5]:
        print(f"     {g['domain']}: {g['pre_gpt']} → {g['post_gpt']} (+{g['delta']})")
    print(f"\n   Transfer rate shift:")
    pre_rate = pre_transfer / max(total_papers_pre, 1) * 100
    post_rate = post_transfer / max(total_papers_post, 1) * 100
    print(f"     Pre-GPT: {pre_rate:.1f}% | Post-GPT: {post_rate:.1f}%")

    print(f"\n{'=' * 80}")
    print(f"Figures saved to: {FIGURES_DIR}")
    print(f"Analysis JSON saved to: {ANALYSIS_DIR}")
    print("=" * 80 + "\n")


# ====================================================================
# Main
# ====================================================================

def main():
    import argparse
    ap = argparse.ArgumentParser(description="NVIDIA Academia-Ecosystem Analysis")
    ap.add_argument("--skip-plots", action="store_true", help="Skip chart generation")
    args = ap.parse_args()

    FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    ANALYSIS_DIR.mkdir(parents=True, exist_ok=True)

    # Phase 1
    global papers
    print("Phase 1: Loading data...", file=sys.stderr)
    papers, transfer_data, known_nvidia = load_all_data()

    # Phase 2
    print("Phase 2: Domain analysis...", file=sys.stderr)
    domain_results = build_domain_analysis(papers)
    with open(ANALYSIS_DIR / "domain_analysis.json", "w") as f:
        json.dump(domain_results, f, ensure_ascii=False, indent=2)
    if not args.skip_plots:
        plot_domain_charts(domain_results, papers)
        print("  5 charts saved", file=sys.stderr)

    # Phase 3
    print("Phase 3: Collaboration analysis...", file=sys.stderr)
    collab_results = build_collaboration_analysis(papers)
    with open(ANALYSIS_DIR / "collaboration_analysis.json", "w") as f:
        json.dump(collab_results, f, ensure_ascii=False, indent=2)
    if not args.skip_plots:
        plot_collaboration_charts(collab_results, papers)
        print("  4 charts saved", file=sys.stderr)

    # Phase 4
    print("Phase 4: Transfer analysis...", file=sys.stderr)
    transfer_results = build_transfer_analysis(papers, transfer_data)
    with open(ANALYSIS_DIR / "transfer_analysis.json", "w") as f:
        json.dump(transfer_results, f, ensure_ascii=False, indent=2)
    if not args.skip_plots:
        plot_transfer_charts(transfer_results, papers)
        print("  5 charts saved", file=sys.stderr)

    # Phase 5
    print_summary_report(domain_results, collab_results, transfer_results)

    print("Done.", file=sys.stderr)


if __name__ == "__main__":
    main()
