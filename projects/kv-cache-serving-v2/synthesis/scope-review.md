# Scope Review

## Goal of This Review

Before starting per-paper project notes, verify whether the current seed set already covers the most important and newest work under the present project intent:

- KV cache reuse and sharing
- KV compression, quantization, eviction, and retrieval
- tiered memory and disaggregated KV serving
- serving-system designs where KV state is a first-class resource

This is not trying to collect every adjacent long-context paper. It is trying to complete the project scope with high-signal papers first.

## Current Assessment

The current seed set is strong, but it is still missing several papers that are important under the project’s own scope.

The gaps fall into two groups:

1. Important papers already present in the local shared database but not yet included in `kv-cache-serving-v2`
2. Newer papers not yet imported into the local database

## Scope Completion Status

Completed in this pass:

- added the key local-database scope expansions to `kv-cache-serving-v2/README.md`
- imported `LouisKV` as `iclr26-004`
- imported `Cache What Lasts` / `TRIM-KV` as `iclr26-005`

This means the project now has a materially better baseline scope for starting per-paper analysis.

## Group A: Add From Local Database

These are already available locally and should likely be added to the project scope.

### Foundational and system-defining

- `sosp23-001` PagedAttention
  - Why add: foundational for modern KV-aware serving; needed historical anchor
- `arxiv23-002` CacheGen
  - Why add: early KV compression/streaming baseline
- `isca24-001` Splitwise
  - Why add: phase splitting and state transfer; useful predecessor to disaggregation work
- `osdi24-001` InfiniGen
  - Why add: direct KV disaggregation paper

### Important mechanism/system papers

- `sigcomm25-003` SCX
  - Why add: stateless KV-cache encoding for confidential serving; distinctive systems angle
- `neurips25-004` Sim-LLM
  - Why add: inter-task KV reuse, clearly on-scope
- `arxiv26-001` Prefill-as-a-Service
  - Why add: prefill/KV service decomposition is highly relevant to architecture evolution
- `arxiv26-002` DualMap
  - Why add: cache affinity vs load balancing is central to distributed KV serving

### Likely include, depending on desired breadth

- `icml26-001` Queueing-Theoretic Framework for Stability Analysis of LLM Inference with KV Cache Memory Constraints
  - Why add: not a mechanism paper, but relevant if the project wants system-level reasoning about KV-constrained serving
- `nsdi26-010` HydraServe
  - Why add: serverless cold start interacts with prefill/KV reuse, but it is one step more adjacent

## Group B: Missing From Local Database

These are recent, clearly relevant candidates that should be searched/imported before deeper project analysis.

### High-priority recent additions

- `LouisKV: Efficient KV Cache Retrieval for Long Input-Output Sequences`
  - Source: ICLR 2026 Poster, OpenReview
  - Why add: directly targets KV retrieval for long input-output reasoning workloads
- `Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs` (TRIM-KV)
  - Source: ICLR 2026 Poster, OpenReview
  - Why add: strong eviction/retention paper; belongs in the memory-bounded KV branch

### Medium-priority recent additions

- `PRKV: Page Restruct KV Cache for High Accuracy and Efficiency LLM Generation`
  - Source: OpenReview submission
  - Why add: directly relevant to KV retrieval/offloading systems
  - Why not top priority: lower confidence until venue outcome is clearer
- `CentroidKV: Efficient Long-Context LLM Inference via KV Cache Clustering`
  - Source: TMLR under review, OpenReview
  - Why add: relevant clustering-based compression/retrieval angle
  - Why not top priority: under review, not yet an established anchor

### Low-priority / likely defer

- `FlowKV`
  - Useful if multi-turn conversational cache isolation becomes a dedicated subtopic
  - Less central than the current reuse/sharing/system papers
- `Identify Critical KV Cache in LLM Inference from an Output Perturbation Perspective`
  - Interesting theoretical framing, but not clearly a must-have before core system analysis
- `KVLinC`, `RoPK`, `GaugeKV`
  - Relevant frontier compression/pruning papers, but likely second-wave additions after the project covers the core system and retrieval branches

## Recommended Immediate Scope Expansion

### Add now from local database

- `sosp23-001`
- `arxiv23-002`
- `isca24-001`
- `osdi24-001`
- `sigcomm25-003`
- `neurips25-004`
- `arxiv26-001`
- `arxiv26-002`

### Search and import next

- `LouisKV`
- `Cache What Lasts` / `TRIM-KV`

### Defer decision until after first comparative pass

- `icml26-001`
- `nsdi26-010`
- `PRKV`
- `CentroidKV`

## Search Plan To Complete Scope

Use a staged search strategy rather than a broad keyword dump.

### Stage 1: accepted-venue sweep

Check primary venues that already appear in project scope:

- ICLR 2026
- NSDI 2026
- SIGCOMM 2025
- OSDI 2024
- EuroSys 2025
- FAST 2025
- ATC 2025
- NeurIPS 2025

Search strings:

- `"KV cache" site:openreview.net ICLR 2026`
- `"KV cache" site:neurips.cc 2025`
- `"KV cache" site:usenix.org NSDI 2026`
- `"KV cache" site:acm.org SIGCOMM 2025`

### Stage 2: arXiv sweep for 2025-2026

Search combinations of:

- `"KV cache" LLM serving`
- `"KV cache reuse" LLM`
- `"KV cache retrieval" LLM`
- `"KV cache compression" LLM`
- `"KV cache offloading" LLM`
- `"prefill" KV cache serving`
- `"cache affinity" distributed LLM serving`

Then filter by:

- explicit KV state management
- clear serving or memory-system consequence
- enough novelty beyond already included papers

### Stage 3: citation-neighborhood expansion

Once `LouisKV` and `TRIM-KV` are imported:

1. inspect their related work / baselines
2. look for recurring omitted papers
3. only add those that create a real missing branch in the comparative picture

## Working Rule For Scope Completion

Only add a paper if at least one of the following is true:

1. it is a clear anchor for one branch of the project taxonomy
2. it changes the timeline of the field in a meaningful way
3. it is necessary as a comparison baseline for several included papers
4. it introduces a genuinely different mechanism or systems design

If none of those are true, keep it out for now.
