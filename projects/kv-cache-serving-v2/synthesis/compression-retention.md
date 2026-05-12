# Compression And Retention

## Why This Comparison Matters

This branch is the easiest one to over-simplify.

Many papers here appear to solve the same problem:

- reduce KV memory footprint

But they do so at different points in the lifecycle of KV state:

- keep less state live through eviction or retention policy
- keep the same state in fewer bits through quantization
- encode or compress larger semantic units
- exploit redundancy across blocks or even across requests

So this branch should not be read as one flat competition. It is better understood as several subfamilies that answer different questions about what should be preserved and in what representation.

The comparison set here is:

- `neurips25-006` Ada-KV
- `neurips25-007` KeyDiff
- `iclr26-005` TRIM-KV
- `neurips25-003` PolarQuant
- `iclr26-001` KVTC
- `neurips25-011` ChunkKV
- `arxiv26-003` Joint Encoding of KV-Cache Blocks

## Common Problem Frame

All papers in this branch respond to the same pressure:

- live KV is too expensive to keep in full fidelity under long context or high concurrency

But the design choices differ immediately:

1. Should the system keep fewer tokens?
2. Should it keep all tokens in a cheaper representation?
3. Should it compress larger semantic or structural units?
4. Should it exploit redundancy only within one cache, or also across caches?

This is why the branch is better viewed as a representation-and-retention design space than as one algorithm family.

## Subfamily 1: Retention / Eviction

These papers treat KV pressure as a budget-allocation problem over live state.

### Ada-KV: analytical adaptive allocation

Ada-KV’s main move is:

- adapt budget allocation across attention structure
- avoid uniform treatment of tokens or heads
- treat retention as an optimization problem under fixed memory budget

Best read:

- an adaptive eviction-policy paper
- a design where allocation logic is the main intelligence

### KeyDiff: lightweight heuristic retention

KeyDiff’s main move is:

- use key similarity as a training-free retention signal
- stay simple enough for constrained settings

Best read:

- a low-complexity heuristic eviction paper
- a useful anchor for the simpler end of the retention design space

### TRIM-KV: learned retention

TRIM-KV’s main move is:

- learn token utility at creation time
- preserve likely long-term value before retrieval is ever needed
- compete on quality under bounded memory rather than throughput alone

Best read:

- a learned retention paper
- an architectural counterpoint to retrieval-first systems

## Subfamily 2: Low-Bit Or Coding-Based Representation

These papers keep state but change the representation aggressively.

### PolarQuant: key-side quantization

PolarQuant’s main move is:

- quantize KV, especially keys, while managing outlier sensitivity
- reduce memory footprint without relying on token dropping

Best read:

- a quantization-first design
- a representation-efficiency paper with runtime consequences

### KVTC: transform coding for reusable state

KVTC’s main move is:

- treat KV compression as a coding problem
- target reusable or stale state that must remain accessible in compact form

Best read:

- a transform/coding-based compression paper
- a design that is closer to signal compression than to pruning

## Subfamily 3: Semantic Or Structural Compression Units

These papers argue that the unit of preservation should be larger or more structured than one token.

### ChunkKV: semantic-chunk preservation

ChunkKV’s main move is:

- compress or preserve at the semantic-chunk level
- argue that semantic units matter more than isolated tokens

Best read:

- a semantic-unit compression paper
- a bridge between retention logic and representation logic

### Joint Encoding: cross-block redundancy exploitation

Joint Encoding’s main move is:

- encode similar KV blocks jointly
- preserve standard cache structure while exploiting broader redundancy
- move toward concurrency-aware scalable compression

Best read:

- a block-level shared-encoding paper
- a design that begins to globalize compression across requests or blocks

## Benchmark Regime

This branch cannot be compared with one metric family.

### Shared comparison axes

- accuracy or task quality under memory pressure
- memory reduction or compression ratio
- runtime overhead
- robustness in tighter memory regimes

### Critical differences

Ada-KV, KeyDiff, and TRIM-KV emphasize:

- quality under fixed KV budget
- long-context or long-horizon retention
- live-memory management rather than storage compression alone

PolarQuant emphasizes:

- low-bit memory reduction
- quantization error versus decoding/runtime cost

KVTC emphasizes:

- compression ratio
- quality retention on reusable or stale state
- coding-oriented comparison against quantization or SVD-like baselines

ChunkKV emphasizes:

- semantic-unit preservation
- compression-ratio-matched comparisons
- throughput effects from structured reuse

Joint Encoding emphasizes:

- scalability under concurrent serving
- cross-block redundancy
- accuracy and compression together under higher system concurrency

This means there are really three benchmark families:

1. **live-memory retention under fixed budget**
2. **representation compression of preserved state**
3. **global or structural redundancy exploitation**

## Comparative Judgment

### What the retention papers establish

Ada-KV, KeyDiff, and TRIM-KV make a clean point:

- some systems solve KV pressure by deciding what should remain live, not by moving or encoding everything later

Within that subfamily:

- `KeyDiff` is the lightweight heuristic anchor
- `Ada-KV` is the analytical adaptive-allocation anchor
- `TRIM-KV` is the learned-retention anchor

The key distinction is where the system places intelligence:

- simple similarity heuristic
- analytical budget allocation
- learned future-utility estimation

### What the representation papers establish

PolarQuant and KVTC show that memory reduction is not only about dropping state.

- `PolarQuant` changes precision
- `KVTC` changes coding basis and compact representation

These are especially relevant when the state should remain recoverable or reusable rather than simply discarded.

### What the structured-unit papers establish

ChunkKV and Joint Encoding argue that token-wise treatment is too narrow.

- `ChunkKV` says semantic chunks are the more faithful unit
- `Joint Encoding` says redundant blocks across larger scopes can be encoded together

This is important because it starts to connect local compression with broader serving structure, especially when concurrency or reuse creates repeated patterns.

## Productization View

If the question is "which approaches are easiest to absorb into serving systems?" the answer depends on the operational target.

For bounded live-memory management with minimal extra infrastructure:

- KeyDiff and Ada-KV are the most direct references

For higher-quality retention under severe memory pressure:

- TRIM-KV is the strongest retention-side reference

For systems that must preserve reusable or cold state compactly:

- KVTC is more relevant than eviction-only methods

For systems willing to use low-bit representation aggressively:

- PolarQuant is the obvious anchor

For larger structural compression opportunities:

- ChunkKV and Joint Encoding are more forward-looking, especially where serving concurrency or reuse exposes repeated higher-level units

## Relationship To Other Branches

This branch connects back to the rest of the project in a precise way.

Compared with retrieval/offloading:

- retrieval/offloading asks what to bring back later
- compression/retention asks what to keep or how to store it better in the first place

Compared with reuse/sharing:

- reuse/sharing asks when saved state can substitute for recomputation across executions
- compression/retention asks how that state can remain affordable enough to preserve

So this branch is not isolated. It is the representation side of the broader KV-serving problem.

## Project Takeaway

This line of work establishes the fourth central claim of the project:

**KV efficiency is not one decision about “less memory.” It is a layered choice about what to retain, what to encode, what unit to preserve, and what redundancy scope to exploit.**

The progression can be read as:

1. decide which live state deserves the scarce budget
2. compress preserved state more effectively
3. move from token-wise treatment to semantic or structural units
4. exploit broader redundancy when concurrency or reuse makes it worthwhile

That makes this branch the natural complement to retrieval and reuse: it determines how cheaply useful state can remain available before the system must fall back to transfer or recomputation.
