# Retrieval And Offloading

## Why This Comparison Matters

This branch is one of the easiest places to make bad comparisons.

All four papers respond to the same broad condition:

- KV no longer fits comfortably in fast device memory

But they do not all solve the same subproblem.

- `osdi24-001` InfiniGen asks how to predict and fetch the useful working set.
- `iclr26-002` IceCache asks how to structure retrieval so quality survives tight budgets.
- `iclr26-004` LouisKV asks how to trigger retrieval and choose retrieval units without drowning in orchestration overhead.
- `neurips25-008` HiFC asks what storage path and tier architecture make large KV footprints sustainable at all.

So this comparison must separate:

- retrieval policy
- retrieval unit / structure
- storage path
- workload geometry

Otherwise the conclusions become vague or wrong.

## Common Problem Frame

Once KV spills beyond GPU memory, the system faces a three-way tradeoff:

1. keep more KV live, which hurts capacity
2. move KV back on demand, which hurts bandwidth and latency
3. keep less KV, which risks quality degradation or recomputation cost

The retrieval/offloading line is about designing the policy and structure between those extremes.

## Architectural Progression

### InfiniGen: working-set prediction

InfiniGen is the early architectural bridge from generic offloading to selective retrieval.

Its main move is:

- do not pull back all offloaded KV
- predict which subset matters for the next generation step
- treat KV service as a working-set prediction problem

That is a conceptual shift. The problem is no longer only "where do I store KV?" but "what is the next useful slice of KV?"

Best read:

- an early retrieval-policy paper
- a movement/prefetch design under offloading

### IceCache: structured semantic retrieval

IceCache sharpens the retrieval story by adding a more explicit structure between raw offloaded KV and live execution.

Its main move is:

- cluster semantically related tokens
- retrieve more meaningful contiguous regions
- preserve quality under tight token budgets

Compared with InfiniGen, the design is less about generic important-token prediction and more about giving retrieval a structured semantic unit.

Best read:

- a quality-at-budget retrieval paper
- a structured retrieval-layer design

### LouisKV: trigger and granularity discipline

LouisKV is the most explicit paper in this branch about retrieval overhead itself.

Its main move is:

- avoid overly frequent retrieval
- avoid overly coarse retrieval
- use semantically meaningful boundaries
- distinguish long-input and long-output settings

Compared with IceCache, the key addition is not just another retrieval structure. It is a sharper statement that retrieval policy must be workload-shape aware and systems-overhead aware.

Best read:

- a retrieval-trigger and retrieval-granularity paper
- a workload-geometry-aware retrieval design

### HiFC: retrieval depends on storage architecture

HiFC is adjacent to the same branch, but it is not primarily a semantic retrieval-policy paper.

Its main move is:

- make flash/SSD a serious KV tier
- use a direct SSD-to-GPU path
- reduce dependence on large DRAM expansion pools

Compared with the other three papers, HiFC changes the lower storage path more than the higher retrieval semantics. It belongs in this comparison because it changes what offloading and recovery are economically feasible.

Best read:

- a storage-tier architecture paper
- a direct-path swapping design for large KV footprints

## Benchmark Regime

This branch requires the strictest benchmark discipline in the whole project.

### Shared comparison axes

- latency or throughput under constrained GPU KV budget
- accuracy or quality retention against fuller-KV baselines
- transfer overhead
- retrieval efficiency
- memory-budget efficiency

### Critical benchmark differences

InfiniGen emphasizes:

- dynamic important-state retrieval
- long-generation serving
- performance gains from selective prefetch instead of full restoration

IceCache emphasizes:

- long-context quality under tight KV budgets
- semantic structure in retrieval
- quality-at-budget, not only speed

LouisKV emphasizes:

- long-input short-output
- short-input long-output
- long-input long-output
- retrieval overhead induced by bad trigger/granularity choices

HiFC emphasizes:

- throughput and latency stability under sustained swapping
- long-context pressure
- cost and viability of flash-based expansion

This means there is no single scalar leaderboard for this branch.

## Comparative Judgment

### What InfiniGen gets right

- identifies the retrieval problem early as selective working-set movement
- shows that full restoration is often too expensive
- reframes KV management as prediction under offloading

Main limitation:

- the retrieval unit and evaluation structure are less refined than later work

### What IceCache adds

- makes the retrieval structure itself more meaningful
- frames success as quality preservation under budget, not only data movement reduction
- highlights that offloading systems can fail by retrieving the wrong semantic working set, not just by retrieving too much

Main limitation:

- it is less explicit than LouisKV about how workload geometry changes the retrieval problem

### What LouisKV adds

- makes retrieval frequency and granularity first-class system costs
- distinguishes long-input and long-output regimes
- avoids collapsing all long-context serving into one benchmark family

Main limitation:

- its argument is strongest where those workload distinctions matter; it is less about broad storage-tier redesign

### What HiFC adds

- shows that retrieval/offloading feasibility depends on the storage path, not only on the retrieval policy
- expands the design space beyond DRAM-backed offload
- brings cost and practical memory expansion into the discussion

Main limitation:

- it is only partially comparable to the semantic retrieval papers because it solves more of the tier-architecture problem than the retrieval-policy problem

## Productization View

If the question is "which approach looks easiest to operationalize?" the answer again depends on the actual bottleneck.

If the problem is selective recovery under offload:

- InfiniGen is the cleanest conceptual starting point

If the problem is quality loss under tight long-context budgets:

- IceCache is more directly relevant

If the problem is retrieval overhead in diverse long-sequence regimes:

- LouisKV is the strongest systems guide

If the problem is affordable large-capacity KV expansion:

- HiFC is the relevant architectural reference

The deeper lesson is that "offloading" is not one thing. A product system must choose both:

- the physical memory path
- the logical retrieval policy

and the papers in this branch distribute those responsibilities differently.

## Project Takeaway

This line of work establishes the second central claim of the project:

**once KV leaves fast memory, the hard problem is no longer merely capacity expansion; it is deciding what to bring back, when to bring it back, and through which storage path.**

The progression can be read as:

1. recognize that full restore is too expensive
2. impose more structure on what counts as a useful retrieval unit
3. make retrieval triggers sensitive to workload geometry and orchestration overhead
4. redesign the storage path so larger KV working sets are economically and operationally viable

That is why this branch sits naturally after phase disaggregation in the project: once the execution boundary is clear, retrieval/offloading explains how the state behind that boundary is kept usable at scale.
