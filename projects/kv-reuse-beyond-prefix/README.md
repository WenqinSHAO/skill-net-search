# KV Reuse Beyond Prefix

## Intent

This project studies a narrower question than `kv-cache-serving-v2`:

**How are people pushing KV reuse beyond plain exact prefix reuse, and when does that storage-for-computation trade actually make sense?**

The goal is to answer:

- how current systems maximize the storage-for-computation trade via KV reuse
- whether the trade still looks worthwhile when storage and transfer are expensive
- how reuse goes beyond exact prefix identity
- what is traded away when systems use approximate, semantic, cross-model, or agent-level reuse
- how emerging sparse-attention or computational-sparsity designs may further encourage KV sharing
- what the likely future of reusable model-native state looks like

## Scope

In scope:

- exact prefix reuse when it is part of a larger reusable-state architecture
- approximate reuse across requests
- semantic reuse across similar prompts
- cross-model reuse
- agent-to-agent or workflow-level KV exchange
- serving infrastructure that makes reuse practical
- sparse-attention or clustering methods that widen reuse or make reusable KV cheaper
- rough economics of compute saved versus storage/transfer required

Out of scope by default:

- generic KV compression papers with no reuse angle
- pure retrieval/offloading papers unless they materially change the reuse contract
- generic attention-sparsity papers with no KV reuse or reusable-state implication

## Reusable Seed Set From The Current Repo

### Exact or infrastructure-mediated reuse

- `arxiv23-002` CacheGen
- `eurosys25-001` HCache
- `arxiv25-001` LMCache

### Beyond exact prefix reuse inside one serving surface

- `arxiv25-004` KVShare
- `arxiv25-005` SemShareKV
- `arxiv25-006` PRKV
- `arxiv25-007` CentroidKV
- `arxiv25-008` SamKV

### Workflow / repeated-structure context

- `arxiv25-002` KVFlow
- `arxiv25-003` Tokencake

### Cross-model and agent-level reuse

- `nsdi26-008` DroidSpeak
- `arxiv-2501` Q-KVComm
- `nsdi26-061` Agentix

### Serving-infrastructure enablers

- `fast25-001` Mooncake
- `arxiv26-002` DualMap
- `nsdi26-020` JITServe

### Sparse-attention or structured-sparsity enablers

- `arxiv26-004` HySparse
- `arxiv25-010` NOSA

These papers already exist in the shared DB and most already have project-specific notes in `kv-cache-serving-v2`.

## Reusable Project Material

The most reusable existing synthesis files are:

- `projects/kv-cache-serving-v2/synthesis/reuse-sharing.md`
- `projects/kv-cache-serving-v2/synthesis/integrated-narrative.md`
- `projects/kv-cache-serving-v2/synthesis/people.md`

The most reusable per-paper project notes are:

- `arxiv25-001.md`
- `arxiv25-004.md`
- `arxiv25-005.md`
- `nsdi26-008.md`
- `arxiv-2501.md`
- `arxiv25-002.md`
- `arxiv25-003.md`

The first newly imported beyond-prefix additions that still need project-specific notes here are:

- `arxiv25-006` PRKV
- `arxiv25-007` CentroidKV
- `arxiv25-008` SamKV
- `arxiv25-010` NOSA
- `arxiv26-004` HySparse

## Working Rule

This project should stay narrower than `kv-cache-serving-v2`.

If a paper only helps explain generic KV memory pressure but does not change the reuse contract, it belongs here only as background, not as a central anchor.
