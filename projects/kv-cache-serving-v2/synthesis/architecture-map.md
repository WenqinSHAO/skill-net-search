# Architecture Map

## Central Question

Once KV becomes central, what are the main architectural pieces and what interface does each one control?

The most important framing for this project is that the field is no longer optimizing one monolithic "KV cache problem." It is partitioning the problem into different interfaces, each with its own failure mode, benchmark style, and productization burden.

## Layering View

The current paper set suggests a useful stack:

1. substrate: how KV is laid out, stored, and encoded
2. boundary: how KV crosses phase or storage boundaries
3. control plane: how the system decides placement, retention, and routing
4. protocol/workflow: how KV is reused across executions, models, or agents

This layering matters because many papers operate on different levels of the stack and therefore should not be compared as if they were substitutes.

## Piece 1: Local KV Memory Layout

Interface controlled:

- how KV is allocated, addressed, and packed within a serving node

Main problems:

- fragmentation
- dynamic growth/shrink
- local sharing feasibility

Representative papers:

- `sosp23-001` PagedAttention / vLLM

Architectural note:

This piece defines the local substrate that many later systems assume. If this layer is weak, the rest of the architecture inherits avoidable internal waste.

## Piece 2: Restoration / Reuse Materialization

Interface controlled:

- how prior contextual state is made available again after it leaves the fast path

Main problems:

- recomputation cost
- restoration latency
- storage overhead

Representative papers:

- `arxiv23-002` CacheGen
- `eurosys25-001` HCache
- `arxiv25-001` LMCache

Architectural note:

This piece is about bringing useful state back into service after it has left the immediate GPU path. It sits between storage and live execution.

## Piece 3: Retrieval / Offloading Boundary

Interface controlled:

- what subset of KV is brought back, when, and at what granularity

Main problems:

- transfer overhead
- accuracy under constrained budgets
- retrieval trigger frequency

Representative papers:

- `osdi24-001` InfiniGen
- `iclr26-002` IceCache
- `iclr26-004` LouisKV
- `neurips25-008` HiFC

Architectural note:

This is one of the most active branches because retrieval policy has to jointly manage performance, accuracy, and orchestration overhead. Long-input and long-output workloads stress this interface differently.

## Piece 4: Phase Boundary

Interface controlled:

- how prefill-produced KV is handed over to decode

Main problems:

- phase interference
- transfer boundary placement
- network assumptions
- phase-specific scaling

Representative papers:

- `isca24-001` Splitwise
- `osdi24-002` DistServe
- `arxiv26-001` Prefill-as-a-Service

Architectural note:

This piece turns KV from an intra-request tensor state into an inter-service handoff object. Once this interface is externalized, transport, placement, and SLO coupling become first-order concerns.

## Piece 5: Storage Tier Architecture

Interface controlled:

- where KV resides across GPU / DRAM / SSD / remote memory

Main problems:

- cost
- bandwidth
- latency stability
- tier coordination

Representative papers:

- `fast25-001` Mooncake
- `neurips25-008` HiFC

Architectural note:

This piece is where architecture stops being about one tactic and becomes about a memory hierarchy. The main question is no longer "can we offload?" but "what role should each tier play under real workload pressure?"

## Piece 6: Routing / Scheduler Locality

Interface controlled:

- which request goes where under reuse, load, and SLO pressure

Main problems:

- cache affinity versus load balancing
- hotspots
- scaling overhead
- workload uncertainty

Representative papers:

- `arxiv26-002` DualMap
- `nsdi26-020` JITServe
- `fast25-001` Mooncake
- `nsdi26-049` Seshat

Architectural note:

This piece elevates KV to cluster control state. Routing and admission decisions become partly predictions about future cache value and locality, not just current queue length.

## Piece 7: Reuse / Sharing Compatibility

Interface controlled:

- when one execution’s KV can be reused by another execution

Main problems:

- exact versus approximate reuse
- semantic drift
- cross-model compatibility
- quality loss

Representative papers:

- `arxiv25-004` KVShare
- `arxiv25-005` SemShareKV
- `nsdi26-008` DroidSpeak
- `arxiv-2501` Q-KVComm

Architectural note:

This piece asks a qualitatively different question from classical cache management: not merely where to place KV, but when two executions can be considered compatible enough to share it.

## Piece 8: Program / Workflow Awareness

Interface controlled:

- whether the system optimizes isolated requests or larger workflows/programs

Main problems:

- future reuse prediction
- stalled-agent cache occupancy
- end-to-end program latency

Representative papers:

- `arxiv25-002` KVFlow
- `arxiv25-003` Tokencake
- `nsdi26-061` Agentix

Architectural note:

This piece matters because agentic or multi-stage applications create delayed and repeated reuse opportunities that per-request schedulers do not naturally capture.

## Piece 9: Compression / Retention Policy

Interface controlled:

- what remains in memory and in what representation

Main problems:

- compression fidelity
- token/head importance
- long-horizon quality
- compute overhead

Representative papers:

- `iclr26-001` KVTC
- `neurips25-003` PolarQuant
- `neurips25-006` Ada-KV
- `neurips25-007` KeyDiff
- `iclr26-005` TRIM-KV
- `neurips25-011` ChunkKV
- `arxiv26-003` Joint Encoding of KV-Cache Blocks

Architectural note:

These papers change the representation itself. They are often judged by quality-at-budget rather than end-to-end serving elasticity, which is why direct comparison to service-architecture papers can be misleading.

## Main Architectural Problems Emerging Across Papers

Across the current scope, the recurring structural problems look like this:

1. **How should live KV be represented locally?**
2. **When should KV be moved versus recomputed versus compressed?**
3. **Where should the prefill/decode boundary live?**
4. **How many storage or memory tiers should participate?**
5. **How should scheduling incorporate cache locality and future reuse?**
6. **What makes two executions compatible enough for reuse?**
7. **Can workflows and agent programs be optimized as KV producers/consumers rather than isolated requests?**

These questions are already enough to organize most of the project.

## Working Observation

Not all papers operate at the same architectural layer.

That matters because a "better method" in one piece may not compete directly with a method in another piece. Some are:

- substrate papers
- boundary papers
- scheduler papers
- representation papers
- workflow papers

This map should be the base for choosing which comparison clusters deserve deeper treatment.

## Practical Comparison Rule

For the next synthesis stage, compare papers only within the same dominant interface unless the point of the comparison is precisely to show an architectural transition.

Good comparisons:

- `isca24-001` vs `osdi24-002` vs `arxiv26-001`
- `osdi24-001` vs `iclr26-002` vs `iclr26-004` vs `neurips25-008`
- `arxiv25-004` vs `arxiv25-005` vs `nsdi26-008` vs `arxiv-2501`

Bad comparisons:

- `sosp23-001` directly against `nsdi26-008`
- `iclr26-005` directly against `fast25-001`

Those papers can still appear in one narrative, but not as substitutes for one another.
