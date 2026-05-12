# eurosys25-001 — HCache

## Why it matters in this project

HCache matters because it frames reusable LLM state as something that can be restored from intermediate activations rather than only recomputed from tokens or reloaded as raw KV.

## Architectural role

**Role**: state-restoration architecture for reusable contexts.

This places HCache between simple cache eviction and full context recomputation. It broadens the restoration design space:

- recompute from tokens
- reload/offload KV
- reconstruct from intermediate activation state

## Benchmarking structure

### Scenario

- reusable contexts in multi-round conversation and RAG-style workloads
- limited GPU cache capacity

### Workload shape

- repeated contextual states across user requests
- restoration after eviction

### Metrics

- TTFT
- storage overhead
- restoration efficiency versus KV offload and token recomputation

The reported shape is especially useful: faster than offload in TTFT while also consuming less storage, and far faster than full recomputation.

## Comparison use

Compare HCache with:

- LMCache
- CacheGen
- KV restoration/offload systems

The key question is not whether it compresses KV more. The question is which restoration path the architecture chooses.

## Project takeaway

HCache suggests that reusable serving state does not have to be treated as raw KV alone; **restoration representation** can itself be a systems design choice.
