# Comparative

## Comparison Angles

This file is for direct cross-paper comparisons rather than summaries.

### Angle 1: Same goal, different mechanism

Questions:

- Which papers all reduce KV footprint, but do so via compression vs eviction vs storage tiering?
- Which papers all reduce prefill cost, but do so via reuse vs sharing vs system restructuring?

### Angle 2: Same mechanism, different deployment scope

Questions:

- Which mechanisms only work on a single node?
- Which survive in disaggregated or distributed settings?
- Which depend on model homogeneity or architecture compatibility?

### Angle 3: State reuse versus state movement

Questions:

- Does the paper avoid recomputation by reusing KV?
- Or does it accept movement/offload cost to preserve state?
- Where is the break-even point implied by the evaluation?

### Angle 4: Local optimization versus serving primitive

Questions:

- Is the contribution a local tensor/storage optimization?
- Or does it make KV a first-class scheduling or architectural primitive?

## Early Pairings To Compare

- DistServe vs Mooncake
- LMCache vs KVFlow
- DroidSpeak vs Q-KVComm
- Ada-KV vs KeyDiff
- KVTC vs ChunkKV
- HCache vs HiFC

## Open Tensions

- Reuse quality risk versus prefill savings
- Compression ratio versus downstream quality stability
- Locality/affinity versus global load balancing
- Simple cache heuristics versus system-wide coordination
