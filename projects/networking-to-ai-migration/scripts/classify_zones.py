#!/usr/bin/env python3
"""
Phase 3: Classify each paper into Zone 1 (Classical Networking),
Zone 2 (AI Infrastructure/Systems), or Zone 3 (Pure AI/ML Research).

Uses a two-pass approach:
  1. Venue-based classification (fast, high precision)
  2. Topic-based classification via keyword matching (for edge cases and
     papers at ambiguous venues)

Reads: data/publication_history.json
Writes: data/publication_history_zones.json (same structure + zone field)

Zone definitions:
  Zone 1 = Classical networking (routing, SDN, congestion, transport, measurement, ...)
  Zone 2 = AI infrastructure / systems (LLM serving, distributed training, KV cache, ...)
  Zone 3 = Pure AI/ML research (model architectures, training algorithms, NLP, CV, ...)
"""

import json
import sys
import re
from pathlib import Path
from collections import Counter
from publication_scope import annotate_scope, canonical_publication_id

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
INPUT_FILE = DATA_DIR / "publication_history.json"
OUTPUT_FILE = DATA_DIR / "publication_history_zones.json"

# ---------------------------------------------------------------------------
# Venue → zone mapping
# ---------------------------------------------------------------------------

# Zone 1 venues: classical networking, systems (non-AI focus), measurement
ZONE1_VENUES = {
    # Top networking
    "SIGCOMM", "NSDI", "CoNEXT", "IMC", "HotNets",
    # Other networking
    "INFOCOM", "ICNP", "ANCS", "ANRW", "SOSR", "APNet",
    "MobiCom", "MobiSys", "SenSys", "IPSN",
    "PAM", "TMA", "WWW", "SIGMETRICS", "IFIP Networking",
    "Networking", "NETWORKING",
    # Classical distributed systems (not AI-focused)
    "PODC", "DISC", "OPODIS", "SRDS", "DSN",
    # Security (non-AI)
    "USENIX Security", "ACM CCS", "NDSS", "IEEE S&P",
    # Broad systems venues where networking/classical systems papers appear
    # These are ambiguous — papers get keyword-reviewed below
}

# Zone 2 venues: AI infrastructure, systems for ML, datacenter
ZONE2_VENUES = {
    "OSDI", "SOSP", "EuroSys", "USENIX ATC", "FAST", "ASPLOS",
    "ISCA", "MICRO", "HPCA", "SC", "HPDC", "SoCC",
    "MLSys", "MLSYS",
    "Middleware", "ICAC", "ICDCS", "CLOUD",
}

# Zone 3 venues: Pure AI/ML
ZONE3_VENUES = {
    "ICLR", "ICML", "NeurIPS", "ACL", "EMNLP", "NAACL",
    "AAAI", "IJCAI", "AISTATS", "UAI",
    "CVPR", "ICCV", "ECCV", "BMVC", "WACV",
    "CoRL", "RSS", "ICRA", "IROS",
    "NeurIPS", "NIPS",
    "SIGGRAPH", "SIGGRAPH Asia",
    "KDD", "WSDM", "CIKM", "RecSys",
    "COLT", "ALT",
    "ISCA",  # Already in Zone 2 list above, but we prioritize Zone 3 keywords
}

# Some venues appear in both lists — we resolve by keyword below.
# Remove overlap from ZONE2 if present in ZONE3 (ISCA is an edge case)
ZONE2_VENUES -= ZONE3_VENUES

# Known conference name variations (DBLP sometimes uses different names)
VENUE_ALIASES = {
    "USENIX Annual Technical Conference": "USENIX ATC",
    "USENIX Security Symposium": "USENIX Security",
    "ACM Conference on Computer and Communications Security": "ACM CCS",
    "IEEE Symposium on Security and Privacy": "IEEE S&P",
    "Symposium on Operating Systems Principles": "SOSP",
    "ACM Symposium on Operating Systems Principles": "SOSP",
    "Network and Distributed System Security Symposium": "NDSS",
    "Annual Conference on Neural Information Processing Systems": "NeurIPS",
    "Advances in Neural Information Processing Systems": "NeurIPS",
    "International Conference on Learning Representations": "ICLR",
    "International Conference on Machine Learning": "ICML",
    "ACM SIGCOMM Conference": "SIGCOMM",
    "ACM SIGCOMM": "SIGCOMM",
    "USENIX NSDI": "NSDI",
    "Symposium on Networked Systems Design and Implementation": "NSDI",
    "ACM CoNEXT": "CoNEXT",
    "Conference on Emerging Network Experiment and Technology": "CoNEXT",
    "ACM Workshop on Hot Topics in Networks": "HotNets",
    "Internet Measurement Conference": "IMC",
    "ACM Internet Measurement Conference": "IMC",
    "IEEE Conference on Computer Communications": "INFOCOM",
    "IEEE INFOCOM": "INFOCOM",
    "Annual Conference on Computer and Communications Security": "ACM CCS",
    "European Conference on Computer Systems": "EuroSys",
    "European Conference on Machine Learning": "ECML",
    "ACM SIGMETRICS": "SIGMETRICS",
    "SIGMETRICS": "SIGMETRICS",
    "ACM SIGGRAPH": "SIGGRAPH",
    "ACM SIGGRAPH Asia": "SIGGRAPH Asia",
    "Int. Conf. on Automated Planning and Scheduling": "ICAPS",
    "International Conference on Automated Planning and Scheduling": "ICAPS",
    "International World Wide Web Conference": "WWW",
    "The Web Conference": "WWW",
    "IEEE ICDCS": "ICDCS",
    "International Conference on Distributed Computing Systems": "ICDCS",
}


def normalize_venue(name: str) -> str:
    """Normalize venue name to our canonical forms."""
    if not name:
        return ""
    name = name.strip()
    # Check aliases
    if name in VENUE_ALIASES:
        return VENUE_ALIASES[name]
    # Try case-insensitive match
    name_lower = name.lower()
    for alias, canonical in VENUE_ALIASES.items():
        if alias.lower() == name_lower:
            return canonical
    return name


# ---------------------------------------------------------------------------
# Keyword-based topic classification
# ---------------------------------------------------------------------------

ZONE2_KEYWORDS = [
    # LLM serving / inference
    r"\bLLM\s+serv", r"\b(inference|serving)\s+(system|engine|platform|cluster|infra)",
    r"\brequest\s+schedul", r"\bcontinuous\s+batching", r"\bdisaggregat.*inference",
    r"\bspeculative\s+decod", r"\bprefill", r"\bdecode.*stage",
    # KV cache
    r"\bKV\s?[Cc]ache", r"\bkey.?value\s+cache", r"\bKV[Cc]omm",
    r"\bcache\s+(shar|reus|offload|distribut|hierarch)", r"\bprefix\s+cach",
    # Distributed training
    r"\bdistributed\s+train", r"\bdata\s+parallel", r"\bmodel\s+parallel",
    r"\btensor\s+parallel", r"\bpipeline\s+parallel", r"\bZeRO",
    r"\ball.?reduce", r"\bparameter\s+server", r"\bgradient\s+compress",
    r"\bsynchronous\s+train", r"\basynchronous\s+train",
    # GPU cluster / communication
    r"\bGPU\s+cluster", r"\bNCCL", r"\bNVLink", r"\bNVSwitch",
    r"\bRDMA.*GPU", r"\bGPU.*RDMA", r"\bGPU.*(network|communicat|interconnect)",
    r"\bcollective\s+communic", r"\ball.?to.?all", r"\ballreduce",
    # ML deployment / ops
    r"\bmodel\s+deploy", r"\bML\s+pipeline", r"\bMLOps", r"\bmodel\s+serving",
    r"\bTensorRT", r"\bONNX", r"\bmodel\s+quantiz", r"\bmodel\s+compression",
    # MoE
    r"\bmixture.?of.?experts", r"\bMoE\b", r"\bexpert\s+parallel",
    # AI datacenter
    r"\bAI\s+(datacenter|data\s*center|cluster|infra|workload)",
    r"\baccelerator\s+(cluster|network|interconnect)",
    # LLM agent infrastructure
    r"\bagent\s+(communic|collaborat|coordinat|orchestrat)",
    r"\bmulti.?agent\s+(system|framework|platform|communic)",
]

ZONE3_KEYWORDS = [
    # Model architecture / training algorithms
    r"\battention\s+mechanism", r"\btransformer\s+arch",
    r"\bself.?attention", r"\bcross.?attention", r"\bmasked\s+attention",
    r"\bneural\s+network\s+arch", r"\bdeep\s+learning\s+model",
    r"\bpre.?train", r"\bfine.?tun", r"\bpost.?train",
    # Learning paradigms
    r"\breinforcement\s+learn", r"\bRL\b",
    r"\brepresentation\s+learn", r"\bcontrastive\s+learn",
    r"\bself.?supervised\s+learn", r"\bsemi.?supervised\s+learn",
    r"\bfew.?shot\s+learn", r"\bzero.?shot\s+learn",
    r"\bcontinual\s+learn", r"\bcurriculum\s+learn",
    r"\bfederated\s+learn", r"\bdistributed\s+learn",
    # Generative models
    r"\bdiffusion\s+model", r"\bgenerative\s+model",
    r"\bGAN\b", r"\bVAE\b", r"\bauto.?regressive\s+model",
    r"\blarge\s+language\s+model", r"\bLLM\b(?!\s+serv)",
    # NLP-specific
    r"\bnatural\s+language\s+(process|understand|generat)",
    r"\bmachine\s+translat", r"\btext\s+(generat|summariz|classif)",
    r"\btokeni[zs]", r"\bembedding", r"\bword2vec",
    # RLHF / alignment
    r"\bRLHF\b", r"\bDPO\b", r"\bpreference\s+optimiz",
    r"\bconstitutional\s+AI", r"\bAI\s+alignment", r"\bAI\s+safety",
    # Prompt engineering / in-context learning
    r"\bprompt\s+engin", r"\bin.?context\s+learn", r"\bchain.?of.?thought",
    r"\bfew.?shot\s+prompt", r"\binstruction\s+tun",
    # CV-specific
    r"\bobject\s+detect", r"\bimage\s+(classif|segment|recogni|generat)",
    r"\bvideo\s+(understand|generat|analys)",
    # Robotics / embodied
    r"\bembodied\s+AI", r"\brobot\s+learn", r"\bimitation\s+learn",
    r"\bsim.?to.?real",
    # Learning theory
    r"\bgeneralization\s+bound", r"\bPAC\s+learn",
    r"\boptimization\s+(algorithm|method|theory).*(convex|gradient|stochastic)",
    r"\bconvergence\s+(rate|analysis|guarantee)",
]

# Compile patterns for efficiency
ZONE2_PATTERNS = [re.compile(p, re.IGNORECASE) for p in ZONE2_KEYWORDS]
ZONE3_PATTERNS = [re.compile(p, re.IGNORECASE) for p in ZONE3_KEYWORDS]

# Zone 1 keywords — explicit networking topics (for catching networking papers
# at broad venues like ATC or EuroSys)
ZONE1_KEYWORDS = [
    r"\b(routing|BGP|OSPF|MPLS|SDN|software.?defined network)",
    r"\b(congestion\s+control|TCP|UDP|QUIC|flow\s+control|AQM)",
    r"\b(packet\s+(schedul|classif|process|forward|switch))",
    r"\b(network\s+(measure|monitor|telemetr|verif|debug|test))",
    r"\b(switch|router)\s+(arch|design|fabric|pipeline)", r"\bprogrammable\s+(switch|data.?plane)",
    r"\b(P4|OpenFlow|data.?plane|control.?plane|forwarding)",
    r"\b(wireless|5G|LTE|cellular|WiFi|mmWave|radio|spectrum)",
    r"\b(CDN|content\s+delivery|edge\s+(comput|cach)|fog\s+comput)",
    r"\b(DNS|BGP|anycast|multicast|peering|IXP)",
    r"\b(network\s+function|NFV|middlebox|load\s+balanc|proxy|NAT)",
    r"\b(cloud\s+network|datacenter\s+network|DCN|topolog|Clos|fat.?tree)",
    r"\b(transport\s+(protocol|layer)|reliab|loss\s+recovery|FEC)",
    r"\b(network\s+security|DDoS|firewall|IDS|anomaly\s+detect.*network)",
    r"\b(blockchain|consensus|distributed\s+ledger|Byzantine)",
    r"\b(network\s+virtualization|VPN|VLAN|VXLAN|overlay)",
    r"\b(IoT|Internet\s+of\s+Things|sensor\s+network)",
]

ZONE1_PATTERNS = [re.compile(p, re.IGNORECASE) for p in ZONE1_KEYWORDS]


def match_keywords(text: str, patterns: list[re.Pattern]) -> int:
    """Count how many patterns match the text."""
    if not text:
        return 0
    count = 0
    for p in patterns:
        if p.search(text):
            count += 1
    return count


def classify_by_venue(venue: str) -> str | None:
    """
    Classify by venue only. Returns 'Zone 1', 'Zone 2', 'Zone 3', or None
    if venue is not in our mapping (needs keyword classification).
    """
    venue = normalize_venue(venue)
    if not venue:
        return None

    if venue in ZONE3_VENUES:
        return "Zone 3"
    if venue in ZONE2_VENUES:
        return "Zone 2"
    if venue in ZONE1_VENUES:
        return "Zone 1"

    # Heuristic: if venue name contains certain keywords
    venue_lower = venue.lower()
    for kw in ["iclr", "icml", "neurips", "nips", "acl", "emnlp",
                "naacl", "aaai", "ijcai", "cvpr", "iccv", "eccv"]:
        if kw in venue_lower:
            return "Zone 3"
    for kw in ["osdi", "sosp", "eurosys", "atc", "fast", "mlsys",
                "asplos", "isca", "micro", "hpdc", "socc"]:
        if kw in venue_lower:
            return "Zone 2"
    for kw in ["sigcomm", "nsdi", "conext", "imc", "hotnets", "infocom",
                "icnp", "mobicom", "mobisys", "sensys"]:
        if kw in venue_lower:
            return "Zone 1"

    return None  # Unknown venue — use keywords


def classify_paper(paper: dict) -> str:
    """
    Classify a single in-scope paper into Zone 1/2/3, or Unclassified.

    Excluded records are kept in the output for auditability but are not part
    of transition metrics. Broad systems venues require AI-workload evidence
    before being treated as Zone 2.
    """
    annotate_scope(paper)
    if not paper.get("included_in_analysis", False):
        paper["classification_reason"] = paper.get("exclusion_reason")
        paper["zone_confidence"] = "excluded"
        return "Excluded"

    venue = paper.get("venue", "")
    venue_zone = classify_by_venue(venue)

    title = paper.get("title", "")
    abstract = paper.get("abstract", "")
    text = f"{title} {abstract}"

    z1_score = match_keywords(text, ZONE1_PATTERNS)
    z2_score = match_keywords(text, ZONE2_PATTERNS)
    z3_score = match_keywords(text, ZONE3_PATTERNS)

    if venue_zone == "Zone 3":
        if z2_score > z3_score and z2_score >= 2:
            paper["classification_reason"] = "ai_venue_with_infra_keywords"
            paper["zone_confidence"] = "medium"
            return "Zone 2"
        paper["classification_reason"] = "ai_ml_venue"
        paper["zone_confidence"] = "medium" if not abstract else "high"
        return "Zone 3"

    if venue_zone == "Zone 2":
        if z3_score > z2_score and z3_score > z1_score and z3_score >= 2:
            paper["classification_reason"] = "systems_venue_with_pure_ai_keywords"
            paper["zone_confidence"] = "medium"
            return "Zone 3"
        if z2_score >= 1 and z2_score >= z1_score:
            paper["classification_reason"] = "systems_venue_with_ai_infra_keywords"
            paper["zone_confidence"] = "medium" if not abstract else "high"
            return "Zone 2"
        if z1_score >= 1:
            paper["classification_reason"] = "systems_venue_with_networking_keywords"
            paper["zone_confidence"] = "medium"
            return "Zone 1"
        paper["classification_reason"] = "ambiguous_systems_venue_no_ai_signal"
        paper["zone_confidence"] = "low"
        return "Unclassified"

    if venue_zone == "Zone 1":
        if z2_score > z1_score and z2_score >= 2:
            paper["classification_reason"] = "networking_venue_with_ai_infra_keywords"
            paper["zone_confidence"] = "medium"
            return "Zone 2"
        if z3_score > z1_score and z3_score > z2_score and z3_score >= 2:
            paper["classification_reason"] = "networking_venue_with_pure_ai_keywords"
            paper["zone_confidence"] = "medium"
            return "Zone 3"
        paper["classification_reason"] = "networking_venue"
        paper["zone_confidence"] = "medium"
        return "Zone 1"

    scores = {"Zone 1": z1_score, "Zone 2": z2_score, "Zone 3": z3_score}
    best = max(scores, key=scores.get)
    if scores[best] == 0:
        paper["classification_reason"] = "unknown_venue_no_keyword_signal"
        paper["zone_confidence"] = "low"
        return "Unclassified"

    paper["classification_reason"] = "unknown_venue_keyword_match"
    paper["zone_confidence"] = "low" if not abstract else "medium"
    return best


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def run():
    """Run zone classification on all papers."""
    if not INPUT_FILE.exists():
        print(f"ERROR: {INPUT_FILE} not found. Run Phase 2 first.",
              file=sys.stderr)
        sys.exit(1)

    with open(INPUT_FILE) as f:
        data = json.load(f)

    researchers = data.get("researchers", [])
    print("=" * 60)
    print("Phase 3: Classify Papers into Zones 1/2/3")
    print("=" * 60)
    print(f"Researchers to process: {len(researchers)}")
    print()

    total_papers = 0
    analysis_papers = 0
    zone_counts = Counter()
    exclusion_counts = Counter()
    duplicate_count = 0
    edge_cases = []  # Papers where venue zone != final zone

    for i, researcher in enumerate(researchers):
        seen_analysis_ids = set()
        for paper in researcher.get("papers", []):
            total_papers += 1
            annotate_scope(paper)
            venue_zone = classify_by_venue(paper.get("venue", "")) or "Unknown"

            if paper.get("included_in_analysis", False):
                analysis_id = canonical_publication_id(paper)
                if analysis_id in seen_analysis_ids:
                    paper["included_in_analysis"] = False
                    paper["exclusion_reason"] = "duplicate_publication"
                    duplicate_count += 1
                else:
                    seen_analysis_ids.add(analysis_id)

            if not paper.get("included_in_analysis", False):
                final_zone = "Excluded"
                paper["classification_reason"] = paper.get("exclusion_reason")
                paper["zone_confidence"] = "excluded"
                exclusion_counts[paper.get("exclusion_reason") or "unknown"] += 1
            else:
                final_zone = classify_paper(paper)
                analysis_papers += 1

            paper["zone"] = final_zone
            paper["venue_zone"] = venue_zone
            zone_counts[final_zone] += 1

            if (paper.get("included_in_analysis", False) and venue_zone != "Unknown"
                    and venue_zone != final_zone):
                edge_cases.append({
                    "title": paper["title"],
                    "venue": paper["venue"],
                    "venue_zone": venue_zone,
                    "final_zone": final_zone,
                    "researcher": researcher["name"],
                })

    # Save
    output = {
        "metadata": {
            "phase": "classify_zones",
            "total_papers": total_papers,
            "analysis_papers": analysis_papers,
            "zone_counts": dict(zone_counts),
            "exclusion_counts": dict(exclusion_counts),
            "duplicate_count": duplicate_count,
            "edge_cases_count": len(edge_cases),
        },
        "researchers": researchers,
        "edge_cases": edge_cases[:50],  # Keep first 50 for review
    }

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\nOutput saved to {OUTPUT_FILE}")
    print(f"\nZone distribution:")
    for zone in ["Zone 1", "Zone 2", "Zone 3", "Unclassified", "Excluded"]:
        count = zone_counts[zone]
        pct = 100 * count / total_papers if total_papers > 0 else 0
        bar = "█" * int(pct / 2)
        print(f"  {zone}: {count:5d} papers ({pct:5.1f}%) {bar}")

    print(f"\nEdge cases (venue zone ≠ final zone): {len(edge_cases)}")
    if edge_cases:
        print("Sample edge cases:")
        for ec in edge_cases[:10]:
            print(f"  [{ec['venue_zone']}→{ec['final_zone']}] {ec['title'][:80]}")
            print(f"    Venue: {ec['venue']} | Researcher: {ec['researcher']}")


if __name__ == "__main__":
    run()
