# KV Reuse Beyond Prefix Plan

## Goal

Keep this project focused on one narrow question:

**How are current systems pushing KV reuse beyond exact prefix reuse, and when does the storage-for-computation trade actually pay off?**

This file is the main execution tracker for the project. Going forward, work should primarily update:

- `PLAN.md`
- `ANALYSIS.md`

The smaller files under `synthesis/` are now supporting notes rather than the main working surface.

## Main Questions

### 1. How do current systems maximize the storage-for-computation trade via KV reuse?

Status:

- partially addressed

Current evidence base:

- `CacheGen`
- `HCache`
- `LMCache`
- `KVShare`
- `SemShareKV`
- `DroidSpeak`
- `Q-KVComm`
- `PRKV`
- `CentroidKV`
- `SamKV`
- `NOSA`
- `HySparse`
- `Prompt Cache`
- `Cost-Efficient Serving of LLM Agents via Test-Time Plan Caching`
- `LRAgent`
- `Don't Break the Cache`

What remains:

- sharper comparison of which systems primarily save compute, which primarily save memory, and which do both
- stronger separation between:
  - app-level reusable objects
  - runtime-level reusable KV state

### 2. Is KV reuse still worthwhile when storage and transfer are expensive?

Status:

- not yet well answered

Current evidence:

- architectural arguments exist in `LMCache`, `Mooncake`, `NOSA`, and related serving papers
- the repo does not yet have a proper cost model tying storage price, transfer cost, and compute avoided together

What remains:

- gather source-backed storage-tier cost and transfer assumptions
- build one common cost template across reuse styles

### 3. How does reuse go beyond exact prefix reuse?

Status:

- strongly addressed structurally

Current ladder:

1. exact reusable cache infrastructure
2. approximate cross-request reuse
3. semantic reuse
4. app-logic-guided modular or plan-level reuse
5. structured retained-state reuse
6. multi-context sparse reuse
7. cross-model reuse
8. inter-agent representation exchange

What remains:

- make the comparison more explicit around correctness risk and quality degradation

### 4. What are the tradeoffs of those beyond-prefix tricks?

Status:

- partially addressed

Main tradeoff categories already identified:

- quality risk
- compatibility assumptions
- retrieval and transfer overhead
- orchestration complexity
- additional persistent-state footprint
- application/framework integration burden

What remains:

- turn these into a consistent comparison table or structured narrative

### 5. How do people share KV across models and agents?

Status:

- structurally addressed, but still narrow in evidence

Current anchors:

- `DroidSpeak`
- `Q-KVComm`
- `LRAgent`
- `Agentix`

What remains:

- determine whether there are stronger heterogeneous-model reuse papers beyond same-architecture or fine-tuned-variant reuse

### 6. Do emerging attention mechanisms and computational sparsity encourage KV sharing?

Status:

- newly opened, not yet fully answered

Current anchors:

- `SamKV`
- `NOSA`
- `HySparse`
- `CentroidKV`

What remains:

- separate two possibilities:
  - sparse attention makes reuse easier by shrinking or structuring retained state
  - sparse attention reduces the need for reuse by lowering the active-state burden directly

### 7. Does context engineering create better cache boundaries than runtime-only reuse policies can see?

Status:

- newly opened and already relevant

Current anchors:

- `arxiv23-003` Prompt Cache
- `arxiv25-011` Cost-Efficient Serving of LLM Agents via Test-Time Plan Caching
- `arxiv26-006` Don't Break the Cache
- `arxiv26-005` LRAgent

Why this matters:

- app logic may identify reusable prompt modules better than generic runtime heuristics
- system prompts, tool schemas, cached intermediate results, and reusable plan templates may expose higher-value cache boundaries
- multi-agent frameworks may know which intermediate artifacts will be consumed by many downstream steps

What remains:

- integrate this layer cleanly with the KV-focused reuse ladder
- separate:
  - prompt-module caching
  - plan/result caching
  - true KV-state sharing

### 8. What is the likely future of reusable model-native state?

Status:

- hypothesis stage

Current hypothesis:

- the field may move from KV as cache to KV as reusable intermediate representation or protocol object

Evidence currently supporting that direction:

- `DroidSpeak`
- `Q-KVComm`
- `SamKV`
- `HySparse`
- `LRAgent`

What remains:

- verify whether additional papers or system designs support this trend strongly enough

## Current Scope

### Central papers already in shared DB

- `arxiv23-002` CacheGen
- `arxiv23-003` Prompt Cache
- `eurosys25-001` HCache
- `arxiv25-001` LMCache
- `arxiv25-004` KVShare
- `arxiv25-005` SemShareKV
- `nsdi26-008` DroidSpeak
- `arxiv-2501` Q-KVComm
- `nsdi26-061` Agentix
- `arxiv25-006` PRKV
- `arxiv25-007` CentroidKV
- `arxiv25-008` SamKV
- `arxiv25-010` NOSA
- `arxiv25-011` Cost-Efficient Serving of LLM Agents via Test-Time Plan Caching
- `arxiv26-004` HySparse
- `arxiv26-005` LRAgent
- `arxiv26-006` Don't Break the Cache

### Important infrastructure/context papers

- `fast25-001` Mooncake
- `arxiv26-002` DualMap
- `nsdi26-020` JITServe

## Immediate Next Steps

1. Consolidate the current project understanding into `ANALYSIS.md`.
2. Build one explicit reuse-contract ladder with tradeoffs and likely deployment fit.
3. Add a clearer discussion of when reusable objects live above raw KV:
   - prompt modules
   - reusable plans
   - intermediate artifacts
4. Add one dedicated section on storage-versus-computation economics and mark exactly what is still evidence-poor.
5. Search for one or two strong additional papers only if they materially improve:
   - heterogeneous-model reuse
   - sparse-attention-enabled reuse
   - cost-model evidence
   - app-level cache-boundary design

## Search Backlog

High priority only if current analysis still feels under-supported:

- stronger heterogeneous cross-model reuse work
- stronger cost-model evidence for storage tiers
- one or two boundary-case sparse-attention papers where reuse is made easier or less necessary
- stronger papers on context engineering that explicitly shape reusable prompt or intermediate-state boundaries

Secondary:

- `Mustafar`
- `DeltaKV`
- `ClusterKV`

These are useful only if the analysis needs sharper contrast with compression-only or sparsity-only approaches.
