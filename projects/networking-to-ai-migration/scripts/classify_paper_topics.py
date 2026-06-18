#!/usr/bin/env python3
"""Paper topic classification for venue-level and researcher-level topic analysis.

Defines a fine-grained topic taxonomy for networking/AI-infra papers and classifies
papers using keyword matching on titles (LLM classification can be added later).

The taxonomy is designed to distinguish:
  - Classical networking topics (routing, congestion, SDN, measurement)
  - AI infrastructure topics (distributed training, LLM serving, GPU optimization)
  - ML for networking (applying ML to networking problems)
  - Network security, wireless, systems, and other areas

Reads from data/new_core_clean_papers.json (the canonical clean paper table).

Outputs:
  - data/paper_topic_labels_v2.json — per-paper topic labels
  - data/venue_topic_vectors_v2.json — venue-year topic feature vectors
  - data/venue_topic_evolution_v2.csv — CSV for charting

Old v1 outputs (paper_topic_labels.json, venue_topic_vectors.json,
venue_topic_evolution.csv) based on post_gpt_venue_papers.json are retained
for comparison but should not be treated as validated.
"""

import json
import re
import sys
from pathlib import Path
from collections import Counter, defaultdict

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

OUTPUT_PAPER_LABELS = DATA_DIR / "paper_topic_labels_v2.json"
OUTPUT_VENUE_VECTORS = DATA_DIR / "venue_topic_vectors_v2.json"
OUTPUT_VENUE_EVOLUTION = DATA_DIR / "venue_topic_evolution_v2.csv"

# ── Topic Taxonomy ──

TOPICS = {
    "classical_networking": {
        "label": "Classical Networking",
        "description": "Routing, congestion control, BGP, SDN, network architecture, transport protocols, traffic engineering, network virtualization",
        "keywords": [
            "routing", "congestion control", "bgp", "sdn", "software-defined networking",
            "network virtualization", "traffic engineering", "transport protocol",
            "tcp", "quic", "multipath", "flow control", "packet scheduling",
            "network architecture", "internet architecture", "network design",
            "interdomain", "inter-domain", "peering", "internet exchange",
            "anycast", "multicast", "broadcast", "network function",
            "nfv", "service chaining", "middlebox", "load balanc",
            # Additional classical networking keywords
            "packet processing", "packet forwarding", "switch fabric",
            "router", "network topology", "topology design",
            "network protocol", "protocol design",
            "network reliability", "network availability",
            "network resilience", "fault tolerance network",
            "network management", "network configuration",
            "network upgrade", "network migration",
            "wan", "wide area network", "backbone network",
            "isp network", "carrier network",
            "network slicing", "network isolation",
            "overlay network", "underlay network",
            "network policy", "network intent",
            "traffic classification", "traffic identification",
            "packet classification", "packet inspection",
            "dns", "domain name system",
            "bgp security", "rpki", "route hijack",
            # Exclude ML-related (caught by ai_infrastructure)
        ],
        "exclude_keywords": ["ml", "machine learning", "neural", "reinforcement learning"],
    },
    "ai_infrastructure": {
        "label": "AI Infrastructure (Systems for ML)",
        "description": "Distributed training, LLM serving/inference, GPU cluster networking, ML scheduling, collective communication for ML",
        "keywords": [
            # Training systems
            "distributed training", "dnn training", "deep learning training",
            "training of large", "training of dnn", "training of deep",
            "model training", "large model training", "foundation model training",
            "preemptible instances for affordable training",
            # LLM serving & inference
            "llm serving", "llm inference", "model serving", "inference serving",
            "transformer serving", "transformer inference",
            "large language model", "serving large", "serving deep",
            "generative ai serving", "genai serving",
            # GPU/networking for ML
            "gpu cluster", "gpu sharing", "gpu scheduling", "gpu optimization",
            "gpu memory", "collective communication",
            "all-reduce", "allreduce", "all reduce",
            # Distributed ML systems
            "parameter server", "gradient compression", "gradient communication",
            "distributed machine learning", "distributed dl", "distributed deep",
            "federated learning", "federated training",
            # ML systems
            "ml scheduling", "ml system", "deep learning system",
            "ml infrastructure", "ai infrastructure",
            "training acceleration", "training throughput",
            # Parallelism strategies
            "model parallelism", "tensor parallelism", "pipeline parallelism",
            "data parallelism", "hybrid parallelism",
            # Elastic / serverless training
            "elastic training", "serverless training",
            # Model optimization for deployment
            "model compression for serving", "model quantization",
            "kv cache", "kv-cache",
            # LLM deployment
            "llm deployment", "deploying llm", "deploying large model",
            # RL systems
            "rl training", "rl system", "reinforcement learning system",
            "reinforcement learning training",
            # Specific ML architectures in systems context
            "mixture of experts", "moe training", "moe layer",
            "moe inference", "moe model",
            # Emerging
            "diffusion model serving", "diffusion model training",
            "multi-modal training", "multimodal training",
            "embedding model training", "embedding training system",
            # ML for systems (edge case but important)
            "ml-assisted kernel", "ml for kernel",
        ],
    },
    "programmable_dataplane": {
        "label": "Programmable Data Planes & SmartNICs",
        "description": "P4, programmable switches, SmartNICs, RDMA, kernel bypass, DPDK, switch ASICs",
        "keywords": [
            "programmable switch", "programmable data plane", "p4",
            "smartnic", "smart-nic", "rdma", "kernel bypass", "dpdk",
            "ebpf", "xdp", "switch asic", "data plane programm",
            "match-action", "packet processing pipeline", "nic offload",
            "fpga network", "fpga accelerator network",
        ],
    },
    "network_measurement": {
        "label": "Network Measurement & Telemetry",
        "description": "Internet measurement, telemetry, INT, sketching, flow monitoring, performance measurement",
        "keywords": [
            "measurement", "telemetry", "monitoring", "sketch",
            "network tomography", "performance measurement",
            "internet measurement", "topology discovery", "outage detection",
            "censorship measurement", "traffic analysis measurement",
            "flow monitoring", "packet capture", "network probe",
            "latency measurement", "bandwidth measurement",
            "packet loss", "network health", "network visibility",
            "in-band network telemetry", "int", "postcard telemetry",
        ],
    },
    "networked_systems": {
        "label": "Networked Systems & Datacenter",
        "description": "Datacenter networking, cloud networking, CDN, network storage, networked systems infrastructure",
        "keywords": [
            "datacenter network", "data center network", "clos",
            "cloud network", "multi-tenant", "cdn", "content deliver",
            "network storage", "distributed storage network",
            "key-value store network", "replication network",
            "consensus network", "state machine replication network",
            "microservice network", "service mesh",
            "container network", "kubernetes network",
            "serverless network", "function-as-a-service network",
            "network disaggregation", "disaggregated network",
            # Additional systems keywords
            "disaggregated memory", "disaggregated storage",
            "remote memory", "memory pool",
            "distributed system", "distributed systems",
            "serverless computing", "serverless analytic",
            "shuffle architecture", "shuffle service",
            "resource allocation", "resource management",
            "cluster scheduler", "cluster scheduling",
            "workload scheduling", "job scheduling",
            "data processing cluster", "data analytic",
            "stream processing", "batch processing",
            "distributed query", "distributed execution",
            "function orchestration", "function placement",
            "microservice", "service deployment",
            "cloud native", "cloud infrastructure",
            "cloud system", "cloud platform",
            "operating system network", "os network",
            "kernel network", "network stack",
            "host networking", "network interface",
            "nic-cpu", "cpu-nic", "dpu", "data processing unit",
            "smart switch", "programmable network interface",
        ],
    },
    "network_security": {
        "label": "Network Security & Privacy",
        "description": "DDoS defense, network intrusion, traffic analysis for security, censorship circumvention, anonymity",
        "keywords": [
            "ddos", "denial of service", "network attack", "intrusion detect",
            "network security", "firewall", "network intrusion",
            "censorship", "circumvention", "anonymity", "tor",
            "vpn security", "traffic analysis attack", "network forensics",
            "botnet", "malware network", "phishing network",
            "dns security", "bgp security", "rpki",
            "network spoofing", "ip spoofing", "prefix hijack",
            "internet security", "network anomaly detect",
        ],
    },
    "wireless_mobile": {
        "label": "Wireless, Mobile & Sensing",
        "description": "5G/cellular, WiFi, IoT, satellite/LEO, mobile sensing, wireless sensing",
        "keywords": [
            "5g", "cellular", "lte", "radio access", "ran",
            "wifi", "wireless", "iot", "internet of things",
            "satellite", "leo", "low earth orbit", "starlink",
            "mobile sens", "wireless sens", "rf sensing",
            "mmwave", "millimeter wave", "beamforming",
            "mimo", "massive mimo", "antenna",
            "mobicom", "mobisys", "mobile network",
            "edge computing", "mobile edge", "mec",
            "wearable network", "body area network",
            "sensor network", "wsn", "low-power network",
            "lora", "lorawan", "backscatter", "rfid",
        ],
    },
    "ml_for_networking": {
        "label": "ML for Networking",
        "description": "Applying ML/DL to network management, prediction, optimization, anomaly detection, RL for network control",
        "keywords": [
            "ml for network", "machine learning for network",
            "deep learning for network", "reinforcement learning for network",
            "rl-based network", "rl based network",
            "neural network for network", "ai for network",
            "network prediction using", "traffic prediction using",
            "learned congestion", "learned routing",
            "ml-based network", "data-driven network",
            "intelligent network", "cognitive network",
            "network optimization using ml",
        ],
    },
    "network_verification": {
        "label": "Network Verification & Formal Methods",
        "description": "Network configuration verification, data-plane verification, network synthesis, formal methods for networking",
        "keywords": [
            "network verification", "data plane verification",
            "configuration verification", "network synthesis",
            "network correctness", "formal method",
            "network invariant", "header space analysis",
            "network policy verification", "network intent",
            "network reachability", "network provenance",
            "network debugging", "network testing",
            "network fault localization", "network troubleshooting",
        ],
    },
    "video_streaming": {
        "label": "Video Streaming & Content",
        "description": "Video streaming, adaptive bitrate, QoE, content optimization, AR/VR networking",
        "keywords": [
            "video stream", "adaptive bitrate", "abr",
            "video qoe", "quality of experience",
            "video conferencing", "video call", "video telephony",
            "augmented reality network", "virtual reality network",
            "ar network", "vr network", "volumetric video",
            "video analytics", "live streaming",
            "web conference", "zoom network",
        ],
    },
    "other": {
        "label": "Other",
        "description": "Papers that don't clearly match any category above",
        "keywords": [],  # Catch-all
    },
}


def classify_title(title: str) -> dict:
    """Classify a paper title into one or more topic categories using keyword matching.

    Returns {topic_key: confidence_score} where score is the number of keyword matches.
    """
    title_lower = title.lower()
    scores = {}

    for topic_key, topic_def in TOPICS.items():
        if topic_key == "other":
            continue

        score = 0
        for kw in topic_def["keywords"]:
            if kw.lower() in title_lower:
                score += 1

        # Check exclude keywords
        exclude_hits = 0
        for ex_kw in topic_def.get("exclude_keywords", []):
            if ex_kw.lower() in title_lower:
                exclude_hits += 1

        if score > 0 and exclude_hits == 0:
            scores[topic_key] = score

    # If no match, classify as "other"
    if not scores:
        scores["other"] = 1

    # Normalize to confidence (0-1)
    total = sum(scores.values())
    confidence = {k: v / total for k, v in scores.items()}

    # Get primary topic (highest confidence)
    primary = max(confidence, key=confidence.get)

    return {
        "primary_topic": primary,
        "primary_label": TOPICS[primary]["label"],
        "all_topics": confidence,
        "multi_topic": len(confidence) > 1,
    }


def main():
    print("=" * 60)
    print("Paper Topic Classifier (v2 — repaired new-core data)")
    print("=" * 60)
    print(f"Topics: {len(TOPICS)} categories")
    for k, v in TOPICS.items():
        print(f"  {k}: {v['label']}")
    print()

    # ── Load canonical clean paper table ──
    clean_papers_file = DATA_DIR / "new_core_clean_papers.json"
    if not clean_papers_file.exists():
        print(f"ERROR: {clean_papers_file} not found. Run build_new_core.py first.")
        sys.exit(1)

    with open(clean_papers_file) as f:
        clean_data = json.load(f)

    all_papers = clean_data.get("papers", [])
    print(f"Loaded {len(all_papers)} total records from {clean_papers_file}")

    # Filter to included (clean main) papers only
    clean_papers = [p for p in all_papers if p.get("included_in_new_core_scope")]
    excluded_count = len(all_papers) - len(clean_papers)
    print(f"  {len(clean_papers)} clean main papers, {excluded_count} excluded")

    # ── Classify clean papers ──
    print("\nClassifying papers...")
    paper_labels = {}
    topic_counter = Counter()
    venue_year_topics = defaultdict(lambda: defaultdict(float))  # {venue_year: {topic: share}}

    # Use venue_group for venue-year keys (maps PACMNET → CoNEXT)
    QUALIFYING = {"SIGCOMM", "NSDI", "CoNEXT", "HotNets", "IMC"}

    for paper in clean_papers:
        title = paper.get("title", "")
        venue = paper.get("venue_group", paper.get("venue", ""))  # venue_group preferred
        year = paper.get("year", 0)

        # Dedup by title+venue+year
        key = f"{title}|{venue}|{year}"
        if key in paper_labels:
            continue

        classification = classify_title(title)
        paper_labels[key] = {
            "title": title,
            "venue": venue,
            "year": year,
            **classification,
        }
        topic_counter[classification["primary_topic"]] += 1

        # Accumulate for venue-year vectors (only for qualifying venues)
        if venue in QUALIFYING:
            vy_key = f"{venue}|{year}"
            for topic, conf in classification["all_topics"].items():
                venue_year_topics[vy_key][topic] += conf

    print(f"  Classified {len(paper_labels)} unique clean papers")

    # ── Topic distribution summary ──
    print("\nTopic distribution across all clean qualifying-venue papers:")
    total = sum(topic_counter.values())
    for topic, count in topic_counter.most_common():
        pct = count / total * 100 if total > 0 else 0
        print(f"  {TOPICS[topic]['label']}: {count} ({pct:.1f}%)")

    # ── Build venue-year topic vectors ──
    print("\nBuilding venue-year topic feature vectors...")
    topic_list = list(TOPICS.keys())

    venue_vectors = []
    for vy_key in sorted(venue_year_topics.keys()):
        venue, year_str = vy_key.split("|")
        year = int(year_str)
        topic_counts = venue_year_topics[vy_key]
        total_weight = sum(topic_counts.values())

        vector = {}
        for topic in topic_list:
            weight = topic_counts.get(topic, 0)
            vector[topic] = round(weight / total_weight * 100, 2) if total_weight > 0 else 0.0

        # Get primary topic for this venue-year
        primary_topic = max(vector, key=vector.get) if vector else "other"

        venue_vectors.append({
            "venue": venue,
            "year": year,
            "primary_topic": primary_topic,
            "primary_label": TOPICS[primary_topic]["label"],
            "topic_shares": vector,
            "paper_count": int(total_weight),
        })

    # ── Save paper-level labels ──
    print(f"\nSaving paper topic labels (v2)...")
    with open(OUTPUT_PAPER_LABELS, "w") as f:
        json.dump({
            "metadata": {
                "phase": "topic_classification_v2",
                "method": "keyword_matching",
                "input_source": "data/new_core_clean_papers.json",
                "topics": {k: v["label"] for k, v in TOPICS.items()},
                "total_papers": len(paper_labels),
            },
            "topic_distribution": {TOPICS[k]["label"]: v for k, v in topic_counter.most_common()},
            "papers": list(paper_labels.values()),
        }, f, indent=2, ensure_ascii=False)
    print(f"  Wrote {OUTPUT_PAPER_LABELS}")

    # ── Save venue-year topic vectors ──
    print(f"Saving venue-year topic vectors (v2)...")
    with open(OUTPUT_VENUE_VECTORS, "w") as f:
        json.dump({
            "metadata": {
                "phase": "topic_classification_v2",
                "input_source": "data/new_core_clean_papers.json",
                "topics": {k: v["label"] for k, v in TOPICS.items()},
                "venue_years": len(venue_vectors),
            },
            "venue_vectors": sorted(venue_vectors, key=lambda x: (x["venue"], x["year"])),
        }, f, indent=2, ensure_ascii=False)
    print(f"  Wrote {OUTPUT_VENUE_VECTORS}")

    # ── Save CSV for easy charting ──
    print(f"Saving venue topic evolution CSV...")
    with open(OUTPUT_VENUE_EVOLUTION, "w") as f:
        headers = ["venue", "year"] + topic_list + ["paper_count"]
        f.write(",".join(headers) + "\n")
        for vv in sorted(venue_vectors, key=lambda x: (x["venue"], x["year"])):
            row = [vv["venue"], str(vv["year"])]
            row.extend([str(vv["topic_shares"].get(t, 0)) for t in topic_list])
            row.append(str(vv["paper_count"]))
            f.write(",".join(row) + "\n")
    print(f"  Wrote {OUTPUT_VENUE_EVOLUTION} (v2)")

    # ── By-venue topic evolution summary ──
    print("\n=== By-Venue Topic Evolution ===")
    for venue_name in sorted(set(v["venue"] for v in venue_vectors)):
        venue_data = [v for v in venue_vectors if v["venue"] == venue_name]
        venue_data.sort(key=lambda x: x["year"])
        print(f"\n{venue_name}:")
        for vv in venue_data:
            top3 = sorted(vv["topic_shares"].items(), key=lambda x: -x[1])[:3]
            top3_str = ", ".join(f"{TOPICS[t]['label']}({s:.0f}%)" for t, s in top3)
            print(f"  {vv['year']}: {vv['paper_count']} papers → {top3_str}")

    print("\nDone.")


if __name__ == "__main__":
    main()
