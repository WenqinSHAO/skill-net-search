# Driving Forces

## Central Question

Why did KV cache evolve from an internal transformer runtime artifact into a first-class systems and architecture design object?

The short answer is that KV stops behaving like temporary scratch state once serving scales along three axes at the same time:

- longer contexts
- higher concurrency
- more repeated or shared context across executions

At that point, KV becomes large, expensive to move, expensive to rebuild, and often partially reusable. That combination is what makes it architecturally important.

## Main Pressure Sources

### 1. Memory footprint becomes dominant

KV grows with sequence length and batch size.

This means the serving bottleneck is often no longer only model weights or compute throughput. The transient state itself becomes large enough to determine:

- effective batch size
- usable context length
- whether requests can remain colocated
- whether reuse is economically worth pursuing

This is the pressure behind substrate and memory-efficiency papers such as:

- `sosp23-001` PagedAttention
- `neurips25-003` PolarQuant
- `neurips25-006` Ada-KV
- `neurips25-011` ChunkKV

### 2. Compute and memory are asymmetric across phases

Prefill and decode stress hardware differently.

That asymmetry creates pressure for:

- phase splitting
- heterogeneous hardware assignment
- explicit KV transfer boundaries

This is where KV becomes not just memory state but a handoff object between execution regimes. Papers such as:

- `isca24-001` Splitwise
- `osdi24-002` DistServe
- `arxiv26-001` Prefill-as-a-Service

do not mainly reduce KV size. They expose the fact that the prefill/decode boundary is itself a systems design decision.

### 3. Reuse opportunities increase with workload complexity

As deployments shift from stateless single-turn chat to:

- multi-turn sessions
- RAG
- repeated templates
- multi-agent workflows
- cross-model orchestration

the same or similar context increasingly appears multiple times.

That creates pressure to treat KV as reusable state rather than disposable byproduct.

This pressure is especially visible in:

- `arxiv25-001` LMCache
- `arxiv25-004` KVShare
- `arxiv25-005` SemShareKV
- `nsdi26-008` DroidSpeak
- `arxiv-2501` Q-KVComm
- `nsdi26-061` Agentix

The field is no longer asking only "how do we fit one request?" It is asking "how much repeated contextual work is structurally unnecessary?"

### 4. Offloading alone is not enough

Once KV no longer fits on fast memory, the system must choose among:

- recomputation
- offloading
- retrieval
- compression
- eviction
- restoration from other state

This creates an entire new design space around movement, granularity, and budgeted accuracy.

This is the pressure behind a large fraction of the project:

- `arxiv23-002` CacheGen
- `eurosys25-001` HCache
- `osdi24-001` InfiniGen
- `iclr26-002` IceCache
- `iclr26-004` LouisKV
- `iclr26-005` TRIM-KV
- `neurips25-008` HiFC

The key shift is that "swap KV out" becomes too crude a description. Systems now need explicit policies for what to preserve, what to move, what to rebuild, and what to discard.

### 5. Scheduling becomes KV-aware

As KV grows in importance, the scheduler can no longer only reason about:

- tokens
- requests
- GPUs

It must also reason about:

- cache locality
- reuse probability
- transfer overhead
- long-term retention value
- placement under SLO constraints

Representative papers:

- `fast25-001` Mooncake
- `arxiv26-002` DualMap
- `nsdi26-020` JITServe
- `nsdi26-049` Seshat

Once scheduling is KV-aware, the cache is no longer local implementation detail. It becomes part of cluster resource accounting.

### 6. Product systems force operational realism

Production systems add pressures that toy benchmarks understate:

- bursty workloads
- skewed request lengths
- finite storage tiers
- hotspots
- multi-tenant contention
- deployment heterogeneity
- confidentiality and control concerns

The most useful papers here are not necessarily the most novel algorithmically. They are the ones that force the design to survive realistic serving conditions:

- `fast25-001` Mooncake
- `atc25-001` KVCache in the Wild
- `sigcomm25-003` SCX

These papers matter because they constrain what a plausible product architecture can actually absorb.

### 7. Model-side changes can move the system boundary

If model architectures reduce KV footprint or restructure attention enough, system designs that were once infeasible become feasible:

- broader disaggregation
- cheaper transport
- longer retention windows
- more aggressive reuse

This means the KV problem is jointly shaped by:

- hardware
- system architecture
- runtime policy
- model architecture

## Evolution Hypothesis

The pressure seems to evolve roughly like this:

1. local memory waste becomes intolerable
2. reusable state becomes too expensive to ignore
3. offloading creates retrieval and restoration problems
4. disaggregation makes KV a networked systems object
5. agentic and multi-model workflows make KV a shareable intermediate representation

## Working Historical Reading

The project’s current evidence supports a rough progression:

1. **Local memory pressure** forces better in-node allocation and compaction.
2. **Long-context serving pressure** forces offload, restoration, and selective retrieval.
3. **Phase asymmetry** forces service decomposition between prefill and decode.
4. **Platform pressure** forces tiered KV architecture and KV-aware scheduling.
5. **Reuse pressure** forces systems to treat KV as a reusable or shareable intermediate representation.
6. **Agentic and multi-model pressure** begins to turn KV into a protocol object rather than only a cache object.

This progression is useful because it explains why newer papers often look qualitatively different from earlier ones. They are not merely improving the same knob. They are solving for a later stage in the pressure stack.

## Speculative Forward Pressure

Likely next-stage pressure points:

- KV-aware serving across heterogeneous clusters and datacenters
- stronger coupling between model-side KV reduction and deployment architecture
- reuse across model families rather than only across requests
- security / isolation constraints on reusable KV infrastructure
- workload-aware global memory services for agent ecosystems

The most plausible next shift is that KV becomes managed at a larger scope than one model service:

- cross-service memory layers
- cluster-level reuse registries
- model-family-specific compatibility layers
- stronger scheduling against future reuse rather than current occupancy alone

If that happens, the boundary between "cache policy," "serving scheduler," and "workflow runtime" will blur further. That is where papers like `nsdi26-061` Agentix and `nsdi26-008` DroidSpeak are most interesting: they may be early signals of the next architectural turn, not just isolated tricks.

## What To Verify Next

- Which of these pressures appear first in the literature timeline?
- Which ones actually drive the biggest architectural changes?
- Which are still speculative rather than already stabilized?
