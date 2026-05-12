# Comparative Plan

## Goal

Select a small number of architectural pieces for deeper comparative analysis rather than comparing every paper to every other paper.

The purpose of this file is not only to choose topics. It is to force disciplined comparisons where workload, metric, and deployment assumptions line up well enough to support a real judgment.

## Comparison Method

Each comparison should normalize around the following questions:

1. What exact architectural interface is the paper moving?
2. What workload geometry is it evaluated on?
3. What metric regime dominates the evaluation?
4. What hidden infrastructure assumptions does it rely on?
5. What would be hard to productize?

In practice, that means a paper comparison is only strong if the benchmark scenarios are close enough that the reported wins mean similar things.

## Cluster 1: Phase Disaggregation

Papers:

- Splitwise
- DistServe
- PrfaaS

Main question:

- how far can the prefill/decode boundary be pushed outward, and under what network and workload assumptions?

Comparison axes:

- deployment boundary
- hardware specialization
- transfer dependency
- SLO target
- operational elasticity
- bandwidth sensitivity
- whether the design assumes tightly managed serving clusters

Benchmark normalization:

- compare under TTFT / TPOT or goodput-oriented service metrics
- keep network assumptions explicit
- separate synthetic cluster studies from papers with stronger product context

## Cluster 2: Retrieval / Offloading

Papers:

- InfiniGen
- IceCache
- LouisKV
- HiFC

Main question:

- when KV does not fit, what is the most effective combination of retrieval policy, granularity, and storage path?

Comparison axes:

- retrieval trigger
- retrieval unit
- long-input vs long-output fit
- quality-at-budget
- transfer path and implementation burden
- orchestration overhead
- whether retrieval is selective, predictive, or reactive

Benchmark normalization:

- keep long-input and long-output workloads separate
- distinguish quality metrics from latency/throughput metrics
- track whether the baseline is naive swapping, prior retrieval, or recomputation

## Cluster 3: Reuse / Sharing

Papers:

- LMCache
- KVShare
- SemShareKV
- DroidSpeak
- Q-KVComm

Main question:

- what kinds of executions can share KV, and what compatibility assumptions does each system require?

Comparison axes:

- exact vs approximate reuse
- same-model vs cross-model
- service-layer reuse vs communication-layer reuse
- quality degradation
- productization friction
- compatibility contract
- whether reuse is explicit, inferred, or semantically mediated

Benchmark normalization:

- compare TTFT and throughput gains separately
- make quality loss visible, not averaged away
- note whether the reuse opportunity comes from repeated prefixes, multi-tenant workloads, or multi-model/agent programs

## Cluster 4: Compression / Retention

Papers:

- KVTC
- PolarQuant
- Ada-KV
- KeyDiff
- TRIM-KV
- ChunkKV
- Joint Encoding

Main question:

- how do systems decide whether to compress, quantize, retain selectively, or exploit higher-level redundancy?

Comparison axes:

- unit of compression
- learned vs heuristic vs coding-based
- benchmark regime
- low-memory robustness
- runtime overhead
- quality degradation shape under tighter memory budgets
- whether the method is local-only or system-coordinated

Benchmark normalization:

- compare at matched memory budgets where possible
- separate perplexity/accuracy preservation from end-to-end serving speed
- note whether the method targets long-context retention, live decode memory, or cold-state storage

## Recommended Order

1. phase disaggregation
2. retrieval / offloading
3. reuse / sharing
4. compression / retention

Reason:

- the first two define the macro serving architecture
- the latter two are easier to place once the serving boundary is already clear

## Immediate Recommendation

Write the first full comparative essay on **phase disaggregation** first.

Reason:

- it is the cleanest architectural family
- the workload and metric regime are relatively coherent
- it creates a stable macro-architecture frame for later retrieval and reuse comparisons

Then write **retrieval / offloading** second, because that is where benchmark discipline matters most and where the project already has several strong anchor papers.
