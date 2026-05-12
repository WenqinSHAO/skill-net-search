# Search Plan

## Goal

Fill the two main gaps left by the current repo:

1. beyond-prefix reuse methods that are not yet in the shared DB
2. cost-model evidence for the storage-versus-computation trade

## Priority Papers To Search And Likely Import

Status note:

- the first import batch is done for `PRKV`, `CentroidKV`, `SamKV`, `HySparse`, and `NOSA`
- the next search pass should therefore move from “find the obvious missing papers” to “fill the evidence gaps that matter for the final argument”

### 1. PRKV

Status:

- imported as `arxiv25-006`

Why:

- retrieval-plus-page-structure paper that appears repeatedly as a missing comparison point
- useful for understanding hybrid retrieval/reuse designs under offloading

Primary source:

- OpenReview: `PRKV: Page Restruct KV Cache for High Accuracy and Efficiency LLM Generation`
- https://openreview.net/forum?id=7FM0GBFhe5

### 2. CentroidKV

Status:

- imported as `arxiv25-007`

Why:

- explicit KV clustering / centroid merge approach
- directly relevant to “reuse beyond exact prefix” because it exploits similarity structure rather than exact identity

Primary source:

- OpenReview: `CentroidKV: Efficient Long-Context LLM Inference via KV Cache Clustering`
- https://openreview.net/forum?id=T3EeupQhGj

### 3. SamKV

Status:

- imported as `arxiv25-008`

Why:

- directly addresses multiple-context KV cache rather than one causal stream
- useful for the “beyond prefix” and “future sparse attention” parts of this project

Primary source:

- AAAI 2026: `Sparse Attention Across Multiple-Context KV Cache`
- https://ojs.aaai.org/index.php/AAAI/article/view/40266

### 4. HySparse

Status:

- imported as `arxiv26-004`

Why:

- combines sparse attention with KV cache sharing
- directly relevant to whether new attention architectures encourage cache reuse

Primary source to fetch next:

- arXiv 2602.03560: `HySparse: A Hybrid Sparse Attention Architecture with Oracle Token Selection and KV Cache Sharing`

### 5. NOSA

Status:

- imported as `arxiv25-010`

Why:

- native/offloadable sparse attention
- may provide a cleaner bridge between sparse attention and practical KV reuse or movement

Primary source to fetch next:

- arXiv 2510.13602: `NOSA: Native and Offloadable Sparse Attention`

## Secondary Candidates

These are not central reuse papers, but they may be useful as boundary cases or counterpoints:

- `Mustafar: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference`
- `RetroAttention`
- `DeltaKV: Residual-Based KV Cache Compression via Long-Range Similarity`
- `ClusterKV`

Use them only if the project needs stronger evidence on how compression or sparse kernels change reuse economics.

## Search Themes

### Theme 1. Beyond-prefix reuse mechanisms

Search for:

- `KV cache reuse semantic similarity LLM`
- `cross-request KV sharing approximate reuse`
- `cross-model KV reuse LLM`
- `agent KV communication LLM`

### Theme 2. Sparse attention as reuse enabler

Search for:

- `KV cache sharing sparse attention`
- `multiple-context KV cache sparse attention`
- `hybrid sparse attention KV cache reuse`
- `native offloadable sparse attention KV cache`

### Theme 3. Economic viability

Search for:

- current HBM / GPU memory cost trends
- DRAM versus SSD / NVMe cost per GB
- object storage versus local NVMe cost for persistent reusable state
- transfer bandwidth and latency by tier
- inference compute cost or TTFT cost that reuse actually avoids

## What To Gather For The Cost Model

For each storage tier:

- approximate cost per GB
- usable bandwidth
- latency regime
- operational locality constraints

For each reuse style:

- storage footprint retained
- extra transfer introduced
- compute avoided
- latency saved
- quality or correctness risk

The project should then compare:

- exact prefix reuse
- approximate semantic reuse
- cross-model selective recomputation
- agent/protocol-level state exchange

using the same cost-template rather than four unrelated narratives.

## Immediate Next Evidence Needs

1. Source-grounded per-paper notes for the five newly imported papers.
2. A clearer cost model for:
   - GPU/HBM residency
   - host DRAM persistence
   - local NVMe or SSD persistence
   - remote-object or distributed-cache persistence
3. Additional evidence on whether sparse attention genuinely encourages reuse, or merely reduces the need for reuse by shrinking the active state.
