#!/usr/bin/env python3
"""
Phase 6: Generate charts and a summary report from transition metrics.

Produces:
  - figures/zone_trend.png — Year-over-year zone distribution trend
  - figures/transition_types.png — Transition type distribution (pie/bar)
  - figures/regional_comparison.png — Migration rates by region
  - figures/subfield_stickiness.png — Stickiness by subfield
  - figures/first_crossing_timeline.png — First Zone 2/3 publications by year
  - figures/zone_migration_matrix.png — Sankey or flow diagram data
  - REPORT.md — Summary report with key findings

Reads: data/transition_metrics.json
"""

import json
import sys
import os
from pathlib import Path
from collections import defaultdict

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
FIGURES_DIR = PROJECT_DIR / "figures"
REPORT_FILE = PROJECT_DIR / "REPORT.md"

INPUT_FILE = DATA_DIR / "transition_metrics.json"

# Try to import matplotlib — if not available, generate JSON data for external plotting
try:
    import matplotlib
    matplotlib.use("Agg")  # non-interactive backend
    import matplotlib.pyplot as plt
    import matplotlib.ticker as mticker
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    print("WARNING: matplotlib not available. Will generate chart data as JSON.",
          file=sys.stderr)


# ---------------------------------------------------------------------------
# Chart data preparation
# ---------------------------------------------------------------------------

def prepare_zone_trend_data(aggregate: dict) -> dict:
    """Prepare data for the zone trend line chart."""
    yearly = aggregate["yearly_zone_distribution"]
    years = sorted(yearly.keys(), key=int)
    data = {
        "years": years,
        "zone1_pct": [],
        "zone2_pct": [],
        "zone3_pct": [],
        "total_papers": [],
    }
    for y in years:
        yd = yearly[y]
        zones = yd.get("zone_pct", {})
        data["zone1_pct"].append(round(zones.get("Zone 1", 0) * 100, 1))
        data["zone2_pct"].append(round(zones.get("Zone 2", 0) * 100, 1))
        data["zone3_pct"].append(round(zones.get("Zone 3", 0) * 100, 1))
        data["total_papers"].append(yd.get("total_papers", 0))
    return data


def prepare_transition_type_data(aggregate: dict) -> dict:
    """Prepare data for transition type charts."""
    td = aggregate["transition_type_distribution"]
    tda = aggregate.get("transition_type_distribution_active", td)
    return {
        "all_researchers": td,
        "active_only": tda,
        "total": aggregate["cohort_size"],
        "active": aggregate["active_researchers"],
    }


def prepare_regional_data(aggregate: dict) -> dict:
    """Prepare data for regional comparison chart."""
    regional = aggregate.get("regional_breakdown", {})
    data = {}
    for region, info in regional.items():
        types = info.get("transition_types", {})
        total = info["total"]
        data[region] = {
            "total": total,
            "active": info["active"],
            "stayer_pct": round(types.get("stayer", 0) / total * 100, 1) if total > 0 else 0,
            "infra_shifter_pct": round(types.get("infra_shifter", 0) / total * 100, 1) if total > 0 else 0,
            "full_ai_migrant_pct": round(types.get("full_ai_migrant", 0) / total * 100, 1) if total > 0 else 0,
            "hybrid_pct": round(types.get("hybrid", 0) / total * 100, 1) if total > 0 else 0,
            "gone_quiet_pct": round(types.get("gone_quiet", 0) / total * 100, 1) if total > 0 else 0,
        }
    return data


def prepare_first_crossing_data(aggregate: dict) -> dict:
    """Prepare data for first-crossing timeline chart."""
    z2 = aggregate.get("first_zone2_by_year", {})
    z3 = aggregate.get("first_zone3_by_year", {})
    all_years = sorted(set(list(z2.keys()) + list(z3.keys())), key=int)
    data = {
        "years": all_years,
        "first_zone2": [z2.get(y, 0) for y in all_years],
        "first_zone3": [z3.get(y, 0) for y in all_years],
    }
    return data


def prepare_subfield_data(subfield_stickiness: dict) -> dict:
    """Prepare data for subfield stickiness chart."""
    return {
        sf: {
            "stickiness": round(info["stickiness"], 3),
            "flight_rate": round(info["flight_rate"], 3),
            "total": info["total"],
            "stayer": info["stayer"],
            "infra_shifter": info["infra_shifter"],
            "full_ai_migrant": info["full_ai_migrant"],
            "hybrid": info["hybrid"],
            "gone_quiet": info["gone_quiet"],
        }
        for sf, info in subfield_stickiness.items()
    }


# ---------------------------------------------------------------------------
# Matplotlib chart generation
# ---------------------------------------------------------------------------

def generate_charts_matplotlib(data: dict):
    """Generate all charts using matplotlib."""
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    # Chart 1: Zone trend over time
    fig, ax = plt.subplots(figsize=(12, 6))
    trend = data["zone_trend"]
    years = [int(y) for y in trend["years"]]
    ax.plot(years, trend["zone1_pct"], "o-", color="#2E86AB", linewidth=2,
            markersize=6, label="Zone 1 (Classical Networking)")
    ax.plot(years, trend["zone2_pct"], "s--", color="#F18F01", linewidth=2,
            markersize=6, label="Zone 2 (AI Infrastructure)")
    ax.plot(years, trend["zone3_pct"], "^:", color="#C73E1D", linewidth=2,
            markersize=6, label="Zone 3 (Pure AI/ML)")
    ax.axvline(x=2022.5, color="gray", linestyle="--", alpha=0.5, linewidth=1)
    ax.text(2022.7, ax.get_ylim()[1] * 0.95, "ChatGPT\nNov 2022",
            fontsize=9, color="gray", alpha=0.8)
    ax.set_xlabel("Year", fontsize=12)
    ax.set_ylabel("% of Papers", fontsize=12)
    ax.set_title("Networking Researchers' Publication Zones Over Time", fontsize=14)
    ax.legend(fontsize=11, loc="upper left")
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 100)
    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "zone_trend.png", dpi=150)
    plt.close(fig)
    print("  → figures/zone_trend.png")

    # Chart 2: Transition type distribution
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    tt = data["transition_types"]
    labels = ["Stayers", "Infra-shifters", "Full AI migrants", "Hybrid", "Gone quiet"]
    colors = ["#2E86AB", "#F18F01", "#C73E1D", "#7B2D8E", "#95A5A6"]

    # All researchers
    all_vals = [
        tt["all_researchers"].get("stayer", 0),
        tt["all_researchers"].get("infra_shifter", 0),
        tt["all_researchers"].get("full_ai_migrant", 0),
        tt["all_researchers"].get("hybrid", 0),
        tt["all_researchers"].get("gone_quiet", 0),
    ]
    wedges1, texts1, autotexts1 = ax1.pie(
        all_vals, labels=labels, autopct="%1.1f%%",
        colors=colors, startangle=90,
        textprops={"fontsize": 10}
    )
    ax1.set_title(f"All Researchers (n={tt['total']})", fontsize=12)

    # Active only
    active_vals = [
        tt["active_only"].get("stayer", 0),
        tt["active_only"].get("infra_shifter", 0),
        tt["active_only"].get("full_ai_migrant", 0),
        tt["active_only"].get("hybrid", 0),
        tt["active_only"].get("gone_quiet", 0),
    ]
    wedges2, texts2, autotexts2 = ax2.pie(
        active_vals, labels=labels, autopct="%1.1f%%",
        colors=colors, startangle=90,
        textprops={"fontsize": 10}
    )
    ax2.set_title(f"Active Researchers Only (n={tt['active']})", fontsize=12)

    fig.suptitle("Transition Type Distribution", fontsize=14, y=1.02)
    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "transition_types.png", dpi=150)
    plt.close(fig)
    print("  → figures/transition_types.png")

    # Chart 3: Regional comparison
    reg = data["regional"]
    regions = list(reg.keys())
    categories = ["stayer_pct", "infra_shifter_pct", "full_ai_migrant_pct",
                  "hybrid_pct", "gone_quiet_pct"]
    cat_labels = ["Stayers", "Infra-shifters", "Full AI migrants", "Hybrid", "Gone quiet"]

    fig, ax = plt.subplots(figsize=(12, 6))
    x = range(len(regions))
    width = 0.15
    for i, (cat, label) in enumerate(zip(categories, cat_labels)):
        vals = [reg[r].get(cat, 0) for r in regions]
        bars = ax.bar([xi + i * width for xi in x], vals, width, label=label,
                      color=colors[i])
    ax.set_xticks([xi + 2 * width for xi in x])
    ax.set_xticklabels(regions, fontsize=11)
    ax.set_ylabel("% of Researchers", fontsize=12)
    ax.set_title("Transition Types by Region", fontsize=14)
    ax.legend(fontsize=10, loc="upper right")
    ax.grid(True, alpha=0.2, axis="y")
    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "regional_comparison.png", dpi=150)
    plt.close(fig)
    print("  → figures/regional_comparison.png")

    # Chart 4: First-crossing timeline
    fc = data["first_crossing"]
    years = [int(y) for y in fc["years"]]
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar([y - 0.2 for y in years], fc["first_zone2"], width=0.4,
           color="#F18F01", label="First Zone 2 publication")
    ax.bar([y + 0.2 for y in years], fc["first_zone3"], width=0.4,
           color="#C73E1D", label="First Zone 3 publication")
    ax.set_xlabel("Year", fontsize=12)
    ax.set_ylabel("Number of Researchers", fontsize=12)
    ax.set_title("First-Time Zone Crossing by Year", fontsize=14)
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.2, axis="y")
    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "first_crossing_timeline.png", dpi=150)
    plt.close(fig)
    print("  → figures/first_crossing_timeline.png")

    # Chart 5: Subfield stickiness
    sf = data["subfield"]
    subfields = list(sf.keys())
    stickiness_vals = [sf[s]["stickiness"] * 100 for s in subfields]
    flight_vals = [sf[s]["flight_rate"] * 100 for s in subfields]

    fig, ax = plt.subplots(figsize=(12, 7))
    y_pos = range(len(subfields))
    bar_height = 0.35
    ax.barh([y + bar_height/2 for y in y_pos], stickiness_vals, bar_height,
            color="#2E86AB", label="% Stayed (stayer + infra-shifter)")
    ax.barh([y - bar_height/2 for y in y_pos], flight_vals, bar_height,
            color="#C73E1D", label="% Left (full AI migrant + hybrid)")
    ax.set_yticks(y_pos)
    ax.set_yticklabels(subfields, fontsize=10)
    ax.set_xlabel("% of Researchers", fontsize=12)
    ax.set_title("Subfield Stickiness: Who Stays vs. Who Leaves?", fontsize=14)
    ax.legend(fontsize=10, loc="lower right")
    ax.grid(True, alpha=0.2, axis="x")
    fig.tight_layout()
    fig.savefig(FIGURES_DIR / "subfield_stickiness.png", dpi=150)
    plt.close(fig)
    print("  → figures/subfield_stickiness.png")

    # Save chart data as JSON for external use
    chart_data_file = FIGURES_DIR / "chart_data.json"
    with open(chart_data_file, "w") as f:
        json.dump(data, f, indent=2)
    print(f"  → figures/chart_data.json")


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

def generate_report(data: dict, aggregate: dict, top_migrants: list,
                    top_infra: list, subfield: dict):
    """Generate a markdown report with key findings."""
    tt = data["transition_types"]
    total = tt["total"]
    active = tt["active"]
    trend = data["zone_trend"]
    reg = data["regional"]

    lines = []
    def w(s=""):
        lines.append(s)

    w("# Networking → AI Migration: Quantitative Analysis")
    w()
    w(f"*Generated from DBLP publication data, 2018–2026*")
    w()
    w("## Executive Summary")
    w()
    w(f"Out of **{total}** top networking researchers (≥3 papers at SIGCOMM/NSDI/CoNEXT/HotNets/IMC during 2018–2022), "
      f"**{active}** remained active in publishing during 2023–2026.")
    w()
    w("### Key Findings")
    w()
    # Dynamic findings based on data
    stayer_pct = tt["all_researchers"].get("stayer", 0) / total * 100
    infra_pct = tt["all_researchers"].get("infra_shifter", 0) / total * 100
    migrant_pct = tt["all_researchers"].get("full_ai_migrant", 0) / total * 100
    hybrid_pct = tt["all_researchers"].get("hybrid", 0) / total * 100
    quiet_pct = tt["all_researchers"].get("gone_quiet", 0) / total * 100
    total_moved = infra_pct + migrant_pct + hybrid_pct

    w(f"1. **{stayer_pct:.1f}%** of researchers stayed in classical networking (≥80% Zone 1 publications)")
    w(f"2. **{total_moved:.1f}%** of researchers shifted toward AI — "
      f"{infra_pct:.1f}% to AI infrastructure, {migrant_pct:.1f}% to pure AI/ML, {hybrid_pct:.1f}% hybrid")
    w(f"3. **{quiet_pct:.1f}%** of researchers published fewer than 2 papers in 2023–2026 (\"gone quiet\")")
    w()

    # Trend analysis
    years = [int(y) for y in trend["years"]]
    if len(years) >= 2:
        first_year_z1 = trend["zone1_pct"][0]
        last_year_z1 = trend["zone1_pct"][-1]
        first_year_z2 = trend["zone2_pct"][0]
        last_year_z2 = trend["zone2_pct"][-1]
        first_year_z3 = trend["zone3_pct"][0]
        last_year_z3 = trend["zone3_pct"][-1]
        w("### Temporal Trends")
        w()
        w(f"- Zone 1 (classical networking) went from **{first_year_z1:.1f}%** ({years[0]}) to **{last_year_z1:.1f}%** ({years[-1]})")
        w(f"- Zone 2 (AI infrastructure) went from **{first_year_z2:.1f}%** to **{last_year_z2:.1f}%**")
        w(f"- Zone 3 (pure AI/ML) went from **{first_year_z3:.1f}%** to **{last_year_z3:.1f}%**")
        w()

    # Regional comparison
    w("### Regional Differences")
    w()
    w("| Region | Total | Active | Stayers | Infra-shift | Full AI migrant | Hybrid | Gone quiet |")
    w("|--------|-------|--------|---------|-------------|-----------------|--------|------------|")
    for region in ["US", "Europe", "China", "Other", "Unknown"]:
        if region in reg:
            r = reg[region]
            w(f"| {region} | {r['total']} | {r['active']} | "
              f"{r['stayer_pct']:.1f}% | {r['infra_shifter_pct']:.1f}% | "
              f"{r['full_ai_migrant_pct']:.1f}% | {r['hybrid_pct']:.1f}% | "
              f"{r['gone_quiet_pct']:.1f}% |")
    w()

    # Subfield analysis
    w("### Subfield Stickiness")
    w()
    w("| Subfield | N | Stickiness | Stayed | Left | Gone quiet |")
    w("|----------|---|------------|--------|------|------------|")
    for sf_name, sf_info in subfield.items():
        w(f"| {sf_name} | {sf_info['total']} | "
          f"{sf_info['stickiness']*100:.0f}% | "
          f"{sf_info['stayer'] + sf_info['infra_shifter']} | "
          f"{sf_info['full_ai_migrant'] + sf_info['hybrid']} | "
          f"{sf_info['gone_quiet']} |")
    w()

    # Top migrants
    w("### Notable Full AI Migrants (Top 15)")
    w()
    for i, r in enumerate(top_migrants[:15]):
        w(f"{i+1}. **{r['name']}** — {r['zone3_pct']*100:.0f}% Zone 3 papers")
        for p in r.get("sample_z3_papers", [])[:3]:
            w(f"   - {p}")
    w()

    # Top infra shifters
    w("### Notable Infra-Shifters (Top 15)")
    w()
    for i, r in enumerate(top_infra[:15]):
        w(f"{i+1}. **{r['name']}** — {r['zone2_pct']*100:.0f}% Zone 2 papers")
        for p in r.get("sample_z2_papers", [])[:3]:
            w(f"   - {p}")
    w()

    # Charts
    w("## Charts")
    w()
    w("![Zone Trend](figures/zone_trend.png)")
    w()
    w("![Transition Types](figures/transition_types.png)")
    w()
    w("![Regional Comparison](figures/regional_comparison.png)")
    w()
    w("![First Crossing Timeline](figures/first_crossing_timeline.png)")
    w()
    w("![Subfield Stickiness](figures/subfield_stickiness.png)")
    w()

    # Methodology
    w("## Methodology")
    w()
    w("### Cohort Definition")
    w(f"- Researchers with ≥3 papers at SIGCOMM, NSDI, CoNEXT, HotNets, or IMC during 2018–2022")
    w(f"- Full publication records fetched from DBLP for 2018–2026")
    w()
    w("### Zone Classification")
    w("- **Zone 1** (Classical Networking): Traditional networking topics and venues")
    w("- **Zone 2** (AI Infrastructure): LLM serving, distributed training, KV cache, GPU cluster networking")
    w("- **Zone 3** (Pure AI/ML): Model architectures, training algorithms, NLP, CV, RL")
    w()
    w("### Transition Types")
    w("- **Stayer**: ≥80% Zone 1 publications in 2023–2026")
    w("- **Infra-shifter**: ≥30% Zone 2, <20% Zone 3")
    w("- **Full AI migrant**: ≥30% Zone 3")
    w("- **Hybrid**: ≥20% both Zone 1 and Zone 3")
    w("- **Gone quiet**: <2 papers total in 2023–2026")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def run():
    """Run Phase 6: generate charts and report."""
    if not INPUT_FILE.exists():
        print(f"ERROR: {INPUT_FILE} not found. Run Phase 5 first.",
              file=sys.stderr)
        sys.exit(1)

    with open(INPUT_FILE) as f:
        metrics_data = json.load(f)

    aggregate = metrics_data.get("aggregate", {})
    subfield_stickiness = metrics_data.get("subfield_stickiness", {})
    top_migrants = metrics_data.get("top_full_migrants", [])
    top_infra = metrics_data.get("top_infra_shifters", [])

    print("=" * 60)
    print("Phase 6: Generate Charts and Report")
    print("=" * 60)

    # Prepare chart data
    print("\nPreparing chart data...")
    data = {
        "zone_trend": prepare_zone_trend_data(aggregate),
        "transition_types": prepare_transition_type_data(aggregate),
        "regional": prepare_regional_data(aggregate),
        "first_crossing": prepare_first_crossing_data(aggregate),
        "subfield": prepare_subfield_data(subfield_stickiness),
    }

    # Generate charts
    if HAS_MATPLOTLIB:
        print("\nGenerating charts with matplotlib...")
        generate_charts_matplotlib(data)
    else:
        print("\nSkipping chart generation (matplotlib not available).")
        print("Chart data saved to figures/chart_data.json")
        FIGURES_DIR.mkdir(parents=True, exist_ok=True)
        with open(FIGURES_DIR / "chart_data.json", "w") as f:
            json.dump(data, f, indent=2)

    # Generate report
    print("\nGenerating report...")
    report = generate_report(data, aggregate, top_migrants, top_infra,
                             data["subfield"])

    with open(REPORT_FILE, "w") as f:
        f.write(report)
    print(f"  → {REPORT_FILE}")

    print("\nDone!")


if __name__ == "__main__":
    run()
