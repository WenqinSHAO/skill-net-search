#!/usr/bin/env python3
"""
Phase 5: Compute transition metrics.

For each researcher, computes year-by-year zone distributions,
classifies them into transition types, and produces aggregate statistics
with regional, industry/academic, and subfield breakdowns.

Reads: data/publication_history_zones.json (or _geo.json if Phase 4 ran)
Writes: data/transition_metrics.json
"""

import json
import sys
from pathlib import Path
from collections import Counter, defaultdict

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

# Try to load geo-enriched data first, fall back to zones-only
INPUT_FILE_GEO = DATA_DIR / "publication_history_geo.json"
INPUT_FILE_ZONES = DATA_DIR / "publication_history_zones.json"
INPUT_FILE = INPUT_FILE_GEO if INPUT_FILE_GEO.exists() else INPUT_FILE_ZONES

OUTPUT_FILE = DATA_DIR / "transition_metrics.json"

BASELINE_START = 2018
BASELINE_END = 2022
OBSERVATION_START = 2023
OBSERVATION_END = 2026

# Transition type thresholds
STAYER_THRESHOLD = 0.8   # ≥80% Zone 1 → stayer
INFRA_SHIFT_THRESHOLD = 0.3  # ≥30% Zone 2, <20% Zone 3 → infra-shifter
FULL_MIGRANT_THRESHOLD = 0.3  # ≥30% Zone 3 → full AI migrant
HYBRID_THRESHOLD = 0.2   # ≥20% both Zone 1 AND Zone 3 → hybrid
GONE_QUIET_THRESHOLD = 2  # <2 papers total 2023–2026 → gone quiet


# ---------------------------------------------------------------------------
# Per-researcher metrics
# ---------------------------------------------------------------------------

def compute_researcher_metrics(researcher: dict) -> dict:
    """
    Compute transition metrics for a single researcher.

    Returns a dict with:
      - yearly_zone_distribution: {year: {Zone1: N, Zone2: N, Zone3: N}}
      - baseline_zone_pct: {Zone1: pct, Zone2: pct, Zone3: pct}
      - observation_zone_pct: {Zone1: pct, Zone2: pct, Zone3: pct}
      - transition_type: stayer | infra_shifter | full_ai_migrant | hybrid | gone_quiet
      - first_zone2_year: int or None
      - first_zone3_year: int or None
      - total_papers_baseline: int
      - total_papers_observation: int
    """
    all_papers = researcher.get("papers", [])
    audit_counts = Counter()
    yearly: dict[int, dict[str, int]] = defaultdict(lambda: {"Zone 1": 0, "Zone 2": 0, "Zone 3": 0})

    for paper in all_papers:
        if not paper.get("included_in_analysis", True):
            audit_counts[f"excluded:{paper.get('exclusion_reason') or 'unknown'}"] += 1
            continue

        zone = paper.get("zone", "Unclassified")
        if zone not in {"Zone 1", "Zone 2", "Zone 3"}:
            audit_counts[f"zone:{zone}"] += 1
            continue

        year = paper.get("year", 0)
        if year and year >= BASELINE_START:
            yearly[year][zone] += 1

    # Baseline period (2018–2022)
    baseline_zones = {"Zone 1": 0, "Zone 2": 0, "Zone 3": 0}
    for y in range(BASELINE_START, BASELINE_END + 1):
        for z in ["Zone 1", "Zone 2", "Zone 3"]:
            baseline_zones[z] += yearly.get(y, {}).get(z, 0)

    total_baseline = sum(baseline_zones.values())

    # Observation period (2023–2026)
    obs_zones = {"Zone 1": 0, "Zone 2": 0, "Zone 3": 0}
    for y in range(OBSERVATION_START, OBSERVATION_END + 1):
        for z in ["Zone 1", "Zone 2", "Zone 3"]:
            obs_zones[z] += yearly.get(y, {}).get(z, 0)

    total_obs = sum(obs_zones.values())

    # Percentages
    baseline_pct = {}
    obs_pct = {}
    for z in ["Zone 1", "Zone 2", "Zone 3"]:
        baseline_pct[z] = baseline_zones[z] / total_baseline if total_baseline > 0 else 0
        obs_pct[z] = obs_zones[z] / total_obs if total_obs > 0 else 0

    # First Zone 2 / Zone 3 year
    first_z2 = None
    first_z3 = None
    for y in sorted(yearly.keys()):
        if first_z2 is None and yearly[y].get("Zone 2", 0) > 0:
            first_z2 = y
        if first_z3 is None and yearly[y].get("Zone 3", 0) > 0:
            first_z3 = y

    # Transition type classification
    if total_obs < GONE_QUIET_THRESHOLD:
        transition_type = "gone_quiet"
    elif obs_pct["Zone 1"] >= STAYER_THRESHOLD:
        transition_type = "stayer"
    elif obs_pct["Zone 3"] >= FULL_MIGRANT_THRESHOLD and obs_pct["Zone 2"] < obs_pct["Zone 3"]:
        transition_type = "full_ai_migrant"
    elif obs_pct["Zone 2"] >= INFRA_SHIFT_THRESHOLD:
        transition_type = "infra_shifter"
    elif obs_pct["Zone 1"] >= HYBRID_THRESHOLD and obs_pct["Zone 3"] >= HYBRID_THRESHOLD:
        transition_type = "hybrid"
    elif obs_pct["Zone 3"] >= INFRA_SHIFT_THRESHOLD:
        transition_type = "full_ai_migrant"
    elif obs_pct["Zone 2"] > 0.1:
        transition_type = "infra_shifter"
    else:
        transition_type = "stayer"

    return {
        "yearly_zone_distribution": {
            str(y): yearly[y] for y in sorted(yearly.keys())
        },
        "baseline_zone_pct": baseline_pct,
        "observation_zone_pct": obs_pct,
        "transition_type": transition_type,
        "first_zone2_year": first_z2,
        "first_zone3_year": first_z3,
        "total_papers_baseline": total_baseline,
        "total_papers_observation": total_obs,
        "audit_counts": dict(audit_counts),
    }


# ---------------------------------------------------------------------------
# Aggregate metrics
# ---------------------------------------------------------------------------

def compute_aggregate_metrics(researchers: list[dict]) -> dict:
    """Compute aggregate statistics across the cohort."""
    total = len(researchers)
    active = [r for r in researchers if r["metrics"]["transition_type"] != "gone_quiet"]
    total_active = len(active)

    # Transition type distribution
    type_counts = Counter(r["metrics"]["transition_type"] for r in researchers)
    type_counts_active = Counter(r["metrics"]["transition_type"] for r in active)

    # Yearly zone distribution (all researchers)
    yearly_agg: dict[int, dict[str, int]] = defaultdict(lambda: {"Zone 1": 0, "Zone 2": 0, "Zone 3": 0})
    yearly_researcher_count: dict[int, int] = defaultdict(int)

    for r in researchers:
        for year_str, zones in r["metrics"]["yearly_zone_distribution"].items():
            year = int(year_str)
            for z, count in zones.items():
                yearly_agg[year][z] += count
            yearly_researcher_count[year] += 1

    # Year-over-year migration rates
    yearly_migration = {}
    for year in sorted(yearly_agg.keys()):
        total_papers = sum(yearly_agg[year].values())
        yearly_migration[year] = {
            "total_papers": total_papers,
            "zone_pct": {
                z: yearly_agg[year][z] / total_papers if total_papers > 0 else 0
                for z in ["Zone 1", "Zone 2", "Zone 3"]
            },
        }

    # Regional breakdown
    regional = {}
    for region in ["US", "Europe", "China", "Other", "Unknown"]:
        region_researchers = [r for r in researchers if r.get("region", "Unknown") == region]
        if not region_researchers:
            continue
        region_active = [r for r in region_researchers
                         if r["metrics"]["transition_type"] != "gone_quiet"]

        regional[region] = {
            "total": len(region_researchers),
            "active": len(region_active),
            "transition_types": dict(Counter(
                r["metrics"]["transition_type"] for r in region_researchers
            )),
            "transition_types_active": dict(Counter(
                r["metrics"]["transition_type"] for r in region_active
            )),
        }

    # Year-over-year first-crossing counts
    first_z2_by_year = Counter(
        r["metrics"]["first_zone2_year"] for r in researchers
        if r["metrics"]["first_zone2_year"] is not None
    )
    first_z3_by_year = Counter(
        r["metrics"]["first_zone3_year"] for r in researchers
        if r["metrics"]["first_zone3_year"] is not None
    )

    return {
        "cohort_size": total,
        "active_researchers": total_active,
        "gone_quiet": type_counts.get("gone_quiet", 0),
        "transition_type_distribution": dict(type_counts),
        "transition_type_distribution_active": dict(type_counts_active),
        "yearly_zone_distribution": {
            str(y): yearly_migration[y] for y in sorted(yearly_migration.keys())
        },
        "first_zone2_by_year": {str(y): c for y, c in sorted(first_z2_by_year.items())},
        "first_zone3_by_year": {str(y): c for y, c in sorted(first_z3_by_year.items())},
        "regional_breakdown": regional,
    }


# ---------------------------------------------------------------------------
# Subfield analysis
# ---------------------------------------------------------------------------
# We assign each researcher a *dominant subfield* based on their baseline
# (2018-2022) Zone 1 papers. A researcher may work across multiple subfields;
# the dominant subfield is simply the one with the most keyword matches.
# Subfields only apply to Zone 1 researchers — Zone 2/3 shifters are already
# classified by their migration pattern, not by networking subfield.

SUBFIELD_KEYWORDS = {
    # --- Core networking architecture ---
    "Routing & Topology": [
        "routing", "BGP", "OSPF", "IS-IS", "IGP", "EGP", "path selection",
        "route", "topology", "peering", "IXP", "interdomain", "prefix",
        "anycast", "multicast", "anycast routing", "traffic engineering",
        "MPLS", "segment routing", "source routing", "network topology",
    ],
    "Transport & Congestion": [
        "TCP", "UDP", "QUIC", "congestion control", "flow control",
        "transport protocol", "loss recovery", "AQM", "BBR", "bufferbloat",
        "retransmission", "multipath TCP", "MPTCP", "SCTP", "reliable transport",
        "rate control", "fairness", "bottleneck",
    ],
    "SDN & Data Plane": [
        "SDN", "software-defined network", "P4", "programmability",
        "OpenFlow", "data plane", "programmable switch", "match-action",
        "packet processing", "packet scheduling", "switch pipeline",
        "network programmability", "NFV", "network function virtualization",
        "service function chaining", "middlebox", "virtual network function",
        "network slicing", "network disaggregation",
    ],
    "Network Measurement & Monitoring": [
        "measurement", "monitoring", "telemetry", "traffic analysis",
        "network tomography", "sketch", "network performance", "latency",
        "bandwidth", "throughput", "packet loss", "traceroute", "ping",
        "network debugging", "network diagnostic", "traffic matrix",
        "passive measurement", "active measurement", "network visibility",
        "INT", "in-band network telemetry", "network observability",
    ],
    "Wireless & Mobile": [
        "wireless", "5G", "LTE", "cellular", "WiFi", "mmWave", "mobile",
        "radio", "spectrum", "MIMO", "beamforming", "OFDM", "physical layer",
        "RAN", "radio access", "mobile edge", "handover", "mobility",
        "sensor network", "IoT", "Internet of Things", "LoRa", "BLE",
        "Bluetooth", "ZigBee", "RFID", "backscatter",
    ],
    "Network Security & Privacy": [
        "firewall", "DDoS", "intrusion detection", "anomaly detection",
        "network security", "attack", "vulnerability", "exploit", "malware",
        "botnet", "phishing", "spoofing", "hijack", "censorship",
        "privacy", "anonymity", "Tor", "VPN", "encryption", "TLS",
        "authentication", "authorization", "access control",
        "network forensics", "threat detection", "security policy",
    ],
    "Datacenter & Cloud Networking": [
        "datacenter", "data center", "DCN", "cloud network", "cloud computing",
        "fat-tree", "Clos", "datacenter topology", "server rack", "ToR switch",
        "leaf-spine", "multitenant", "tenant", "virtual machine", "VM placement",
        "resource allocation", "elastic", "auto-scaling", "serverless",
        "cloud native", "container", "Kubernetes",
    ],
    "Network Verification & Synthesis": [
        "network verification", "formal verification", "network synthesis",
        "configuration synthesis", "correctness", "network configuration",
        "control plane verification", "data plane verification",
        "reachability", "policy analysis", "intent-based networking",
        "network modeling", "network calculus",
    ],
    "Content Delivery & Streaming": [
        "CDN", "content delivery", "video stream", "bitrate", "adaptive",
        "DASH", "WebRTC", "cache", "caching", "content distribution",
        "peer-to-peer", "P2P", "video conferencing", "live streaming",
        "edge caching", "web performance", "DNS", "HTTP", "web",
        "anycast CDN", "content placement",
    ],
    "Distributed Systems & Consensus": [
        "consensus", "blockchain", "BFT", "Byzantine", "distributed ledger",
        "replication", "state machine replication", "Paxos", "Raft",
        "distributed coordination", "distributed storage", "distributed database",
        "fault tolerance", "consistency", "CRDT", "gossip protocol",
        "distributed algorithm", "leader election", "atomic broadcast",
        "total order", "distributed commit",
    ],
    "Network Hardware & Architecture": [
        "switch ASIC", "switch chip", "FPGA", "SmartNIC", "network card",
        "NIC", "programmable NIC", "hardware offload", "TCAM", "packet buffer",
        "switch fabric", "crossbar", "network processor", "line rate",
        "hardware acceleration", "router architecture", "switch architecture",
        "memory bandwidth", "PCIe", "interconnect",
    ],
    "AI/ML Applied to Networks": [
        "machine learning.*network", "deep learning.*network", "RL.*network",
        "reinforcement learning.*routing", "neural network.*traffic",
        "ML.*classification.*traffic", "learning.*congestion",
        "AI.*network management", "learning-based.*network",
    ],
}

# For researchers where no specific subfield keywords match, assign by
# conference patterns or broader topic inference
BROAD_SUBFIELD_HINTS = {
    # Conference → likely subfield
    "IMC": "Network Measurement & Monitoring",
    "HotNets": "Networking Systems & Architecture",
    "SIGCOMM": "Networking Systems & Architecture",
    "NSDI": "Networking Systems & Architecture",
    "CoNEXT": "Networking Systems & Architecture",
    "INFOCOM": "Networking Systems & Architecture",
}

# "Networking Systems & Architecture" is our catch-all for researchers
# whose work spans general network systems design that doesn't fit
# a narrow subcategory. It's distinct from "Other" — the researcher
# IS a networking researcher, just not in one of the narrow subfields.

def tag_subfield(title: str, abstract: str = "", venue: str = "") -> str:
    """
    Tag a paper with a networking subfield based on title/abstract keywords.

    If no specific keywords match, tries venue-based hints.
    Falls back to "Networking Systems & Architecture" — a catch-all for
    general networking systems work (not "Other"/garbage).
    """
    text = f"{title} {abstract}".lower()
    scores = {}
    for subfield, keywords in SUBFIELD_KEYWORDS.items():
        score = sum(1 for kw in keywords if kw.lower() in text)
        if score > 0:
            scores[subfield] = score

    if scores:
        return max(scores, key=scores.get)

    # No keywords matched — try venue hint
    if venue:
        for conf, subfield in BROAD_SUBFIELD_HINTS.items():
            if conf.lower() in venue.lower():
                return subfield

    # Catch-all: this IS a networking paper (Zone 1), just not in a narrow subfield
    return "Networking Systems & Architecture"


def compute_subfield_stickiness(researchers: list[dict]) -> dict:
    """Analyze which subfields are most 'sticky' (researchers stay in networking)."""
    subfield_migration: dict[str, Counter] = defaultdict(Counter)

    for r in researchers:
        # Determine dominant subfield from baseline papers
        baseline_papers = [p for p in r.get("papers", [])
                          if p.get("included_in_analysis", True)
                          and BASELINE_START <= p.get("year", 0) <= BASELINE_END
                          and p.get("zone") == "Zone 1"]

        if not baseline_papers:
            continue

        subfield_counts = Counter(
            tag_subfield(p["title"], venue=p.get("venue", "")) for p in baseline_papers
        )
        dominant_subfield = subfield_counts.most_common(1)[0][0]

        transition = r["metrics"]["transition_type"]
        subfield_migration[dominant_subfield][transition] += 1

    # Convert to stickiness score (% stayer + infra_shifter / total)
    subfield_stickiness = {}
    for subfield, counts in subfield_migration.items():
        total = sum(counts.values())
        # "sticky" = stayed in networking or moved to AI infra (still systems)
        sticky = counts.get("stayer", 0) + counts.get("infra_shifter", 0)
        left = counts.get("full_ai_migrant", 0) + counts.get("hybrid", 0)
        subfield_stickiness[subfield] = {
            "total": total,
            "stayer": counts.get("stayer", 0),
            "infra_shifter": counts.get("infra_shifter", 0),
            "full_ai_migrant": counts.get("full_ai_migrant", 0),
            "hybrid": counts.get("hybrid", 0),
            "gone_quiet": counts.get("gone_quiet", 0),
            "stickiness": sticky / total if total > 0 else 0,
            "flight_rate": left / total if total > 0 else 0,
        }

    return dict(sorted(subfield_stickiness.items(),
                       key=lambda x: x[1]["stickiness"], reverse=True))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def run():
    """Run Phase 5: compute transition metrics."""
    if not INPUT_FILE.exists():
        print(f"ERROR: No input file found.", file=sys.stderr)
        sys.exit(1)

    print(f"Loading data from {INPUT_FILE}...")
    with open(INPUT_FILE) as f:
        data = json.load(f)

    researchers = data.get("researchers", [])
    print("=" * 60)
    print("Phase 5: Compute Transition Metrics")
    print("=" * 60)
    print(f"Researchers: {len(researchers)}")
    print(f"Baseline: {BASELINE_START}–{BASELINE_END}")
    print(f"Observation: {OBSERVATION_START}–{OBSERVATION_END}")
    print()

    # Step 1: Per-researcher metrics
    print("Step 1: Computing per-researcher metrics...")
    for r in researchers:
        r["metrics"] = compute_researcher_metrics(r)

    # Step 2: Aggregate metrics
    print("Step 2: Computing aggregate metrics...")
    aggregate = compute_aggregate_metrics(researchers)

    # Step 3: Subfield stickiness
    print("Step 3: Computing subfield stickiness...")
    subfield_stickiness = compute_subfield_stickiness(researchers)

    # Step 4: Top migrants (for case study selection)
    print("Step 4: Identifying top migrants...")
    full_migrants = sorted(
        [r for r in researchers if r["metrics"]["transition_type"] == "full_ai_migrant"],
        key=lambda r: r["metrics"]["observation_zone_pct"]["Zone 3"],
        reverse=True,
    )
    infra_shifters = sorted(
        [r for r in researchers if r["metrics"]["transition_type"] == "infra_shifter"],
        key=lambda r: r["metrics"]["observation_zone_pct"]["Zone 2"],
        reverse=True,
    )

    # Save output
    output = {
        "metadata": {
            "phase": "compute_metrics",
            "baseline_start": BASELINE_START,
            "baseline_end": BASELINE_END,
            "observation_start": OBSERVATION_START,
            "observation_end": OBSERVATION_END,
        },
        "aggregate": aggregate,
        "subfield_stickiness": subfield_stickiness,
        "top_full_migrants": [
            {
                "name": r["name"],
                "dblp_pid": r["dblp_pid"],
                "region": r.get("region", "Unknown"),
                "zone3_pct": r["metrics"]["observation_zone_pct"]["Zone 3"],
                "first_z3_year": r["metrics"]["first_zone3_year"],
                "sample_z3_papers": [
                    p["title"] for p in r.get("papers", [])
                    if p.get("included_in_analysis", True) and p.get("zone") == "Zone 3" and p.get("year", 0) >= OBSERVATION_START
                ][:5],
            }
            for r in full_migrants[:30]
        ],
        "top_infra_shifters": [
            {
                "name": r["name"],
                "dblp_pid": r["dblp_pid"],
                "region": r.get("region", "Unknown"),
                "zone2_pct": r["metrics"]["observation_zone_pct"]["Zone 2"],
                "first_z2_year": r["metrics"]["first_zone2_year"],
                "sample_z2_papers": [
                    p["title"] for p in r.get("papers", [])
                    if p.get("included_in_analysis", True) and p.get("zone") == "Zone 2" and p.get("year", 0) >= OBSERVATION_START
                ][:5],
            }
            for r in infra_shifters[:30]
        ],
        "researchers": researchers,
    }

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\nOutput saved to {OUTPUT_FILE}")

    # Summary
    print("\n" + "=" * 60)
    print("Transition Summary")
    print("=" * 60)

    td = aggregate["transition_type_distribution"]
    total = aggregate["cohort_size"]
    active = aggregate["active_researchers"]

    print(f"\nCohort: {total} researchers ({active} active in 2023–2026)")
    print(f"\nTransition types (% of total / % of active):")
    type_labels = {
        "stayer": "Stayers (≥80% Zone 1)",
        "infra_shifter": "Infra-shifters (≥30% Zone 2)",
        "full_ai_migrant": "Full AI migrants (≥30% Zone 3)",
        "hybrid": "Hybrid (Zone 1 + Zone 3)",
        "gone_quiet": "Gone quiet (<2 papers 2023–26)",
    }
    for ttype, label in type_labels.items():
        count = td.get(ttype, 0)
        pct_total = 100 * count / total if total > 0 else 0
        bar = "█" * int(pct_total / 2)
        if ttype == "gone_quiet":
            active_text = " n/a active"
        else:
            pct_active = 100 * count / active if active > 0 else 0
            active_text = f"{pct_active:5.1f}% active"
        print(f"  {label}: {count:4d} ({pct_total:5.1f}% total, {active_text}) {bar}")

    print(f"\nYearly zone distribution:")
    yearly = aggregate["yearly_zone_distribution"]
    for year in sorted(yearly.keys(), key=int):
        yd = yearly[year]
        tp = yd.get("total_papers", 0)
        zones = yd.get("zone_pct", {})
        print(f"  {year}: {tp:4d} papers | "
              f"Z1: {zones.get('Zone 1', 0)*100:5.1f}% | "
              f"Z2: {zones.get('Zone 2', 0)*100:5.1f}% | "
              f"Z3: {zones.get('Zone 3', 0)*100:5.1f}%")

    print(f"\nFirst Zone 2/3 crossing by year:")
    for year in sorted(aggregate["first_zone2_by_year"].keys(), key=int):
        z2 = aggregate["first_zone2_by_year"].get(year, 0)
        z3 = aggregate["first_zone3_by_year"].get(year, 0)
        if z2 or z3:
            print(f"  {year}: {z2:3d} researchers first published in Zone 2, "
                  f"{z3:3d} in Zone 3")

    print(f"\nRegional breakdown:")
    for region, info in aggregate["regional_breakdown"].items():
        print(f"  {region}: {info['total']} researchers ({info['active']} active)")
        for ttype, count in info["transition_types"].items():
            pct = 100 * count / info["total"] if info["total"] > 0 else 0
            print(f"    {ttype}: {count} ({pct:.0f}%)")

    print(f"\nSubfield stickiness (high = researchers stayed in networking):")
    for subfield, info in subfield_stickiness.items():
        print(f"  {subfield:<25s}: stickiness={info['stickiness']:.2f} "
              f"({info['stayer']} stay, {info['full_ai_migrant']} left, "
              f"{info['gone_quiet']} quiet, n={info['total']})")

    # Top migrants
    print(f"\nTop full AI migrants (for case study selection):")
    for r in full_migrants[:10]:
        print(f"  {r['name']:<40s} Z3={r['metrics']['observation_zone_pct']['Zone 3']:.0%} "
              f"first Z3={r['metrics']['first_zone3_year']} "
              f"region={r.get('region', '?')}")

    print(f"\nTop infra-shifters (for case study selection):")
    for r in infra_shifters[:10]:
        print(f"  {r['name']:<40s} Z2={r['metrics']['observation_zone_pct']['Zone 2']:.0%} "
              f"first Z2={r['metrics']['first_zone2_year']} "
              f"region={r.get('region', '?')}")

    return output


if __name__ == "__main__":
    run()
