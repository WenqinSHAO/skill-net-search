# Benchmarking

## Why This File Exists

Many papers in this project appear to address “KV cache efficiency,” but they benchmark very different system regimes. Later comparison will be misleading unless those regimes are made explicit.

## Primary Benchmarking Families

### 1. Phase-disaggregation / deployment papers

Representative papers:

- Splitwise
- DistServe
- Prefill-as-a-Service

Typical scenario:

- serving clusters
- prefill/decode decomposition
- heterogeneous hardware or network placement

Typical workload assumptions:

- request arrival processes
- latency SLOs
- phase imbalance
- bandwidth/transfer constraints

Typical metrics:

- throughput
- TTFT
- TPOT
- SLO satisfaction
- cost
- power

Comparison warning:

- do not compare these papers to retrieval/eviction papers using only headline speedup

### 2. Retrieval / offloading papers

Representative papers:

- InfiniGen
- IceCache
- LouisKV
- PRKV

Typical scenario:

- KV does not fit on device
- some KV remains off device
- the system must retrieve or prefetch subsets efficiently

Typical workload assumptions:

- long-context inference
- long-output reasoning or long input-output workloads
- constrained on-GPU KV budgets

Typical metrics:

- latency or speedup
- accuracy retention versus full-cache baseline
- budget efficiency
- transfer / orchestration overhead

Comparison warning:

- these papers differ in retrieval unit, trigger policy, and workload shape
- long-input and long-output regimes should be distinguished explicitly

### 3. Retention / eviction papers

Representative papers:

- Ada-KV
- KeyDiff
- TRIM-KV

Typical scenario:

- fixed memory budget
- no assumption that offloaded KV is cheaply retrievable

Typical workload assumptions:

- long-horizon generation
- reasoning tasks
- memory-bounded inference

Typical metrics:

- task accuracy under memory budget
- robustness in low-memory regime
- sometimes latency overhead

Comparison warning:

- these papers optimize what remains in cache, not how remote KV is retrieved

### 4. Reuse / sharing papers

Representative papers:

- LMCache
- KVShare
- SemShareKV
- DroidSpeak
- Q-KVComm

Typical scenario:

- shared prefixes or related prompts
- repeated or overlapping context across requests, workflows, or models

Typical workload assumptions:

- multi-request reuse
- multi-tenant reuse
- multi-agent or multi-model coordination

Typical metrics:

- TTFT reduction
- throughput gain
- reuse hit rate or effective sharing gain
- quality degradation under approximate reuse

Comparison warning:

- same-model prefix reuse and cross-model reuse are not the same regime

## Comparison Rules For Later Synthesis

When comparing two papers later, first classify them by:

1. architectural family
2. workload shape
3. main evaluation metric

Only then compare methods directly.

## Current Useful Pairings

### Phase-disaggregation

- Splitwise vs DistServe vs PrfaaS

Main axis:

- how far the phase boundary is pushed
- what network assumptions are required
- whether comparison centers on throughput, SLOs, or deployment elasticity

### Retrieval/offloading

- InfiniGen vs IceCache vs LouisKV

Main axis:

- retrieval trigger
- retrieval unit granularity
- quality under constrained KV budget
- long-input versus long-output workloads

### Retention/eviction

- Ada-KV vs KeyDiff vs TRIM-KV

Main axis:

- importance estimation method
- low-memory quality
- reasoning robustness

### Reuse/sharing

- LMCache vs KVShare vs SemShareKV vs DroidSpeak

Main axis:

- exact reuse versus approximate reuse
- same-model versus cross-model reuse
- scheduler dependence versus representation dependence
