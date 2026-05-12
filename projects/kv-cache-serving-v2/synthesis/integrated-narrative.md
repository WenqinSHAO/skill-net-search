# Integrated Narrative

## Goal

This note connects the project’s four main comparative branches into one end-to-end reading of the field:

- why KV became architecturally central
- how the main serving interfaces changed
- how different branches solve different parts of the same systems problem
- where the field appears to be heading next

The purpose is not to replace the branch notes. It is to connect them into one coherent research story.

## Core Claim

The project’s current evidence supports one central reading:

**KV cache stopped being a local runtime optimization and became a first-class systems object once it started governing latency, memory footprint, transfer cost, scheduling, and compute reuse at the same time.**

This is not one transition but a sequence of architectural expansions.

## Stage 1: KV As Local Memory Pressure

The earliest stable problem is local pressure:

- sequence length grows
- batch size grows
- decode-time memory cost grows with the live cache

At this stage, the main question is still local:

- how do we pack KV efficiently?
- how do we preserve quality under a smaller live budget?

This is the natural home of:

- local layout/substrate work such as `sosp23-001`
- retention/eviction work such as `Ada-KV`, `KeyDiff`, and `TRIM-KV`
- low-bit or coding-based compression such as `PolarQuant` and `KVTC`

Architecturally, KV is still mostly a node-local resource problem.

## Stage 2: KV As A Boundary Between Execution Phases

The second transition happens when the field realizes that prefill and decode do not merely stress the same resources at different intensities. They occupy different resource regimes and have different service objectives.

This is the architectural shift established by the phase-disaggregation line:

- `Splitwise`
- `DistServe`
- `Prefill-as-a-Service`

In this stage, KV becomes the state object that crosses the prefill/decode boundary.

That changes the main question from:

- how do we run inference efficiently inside one engine?

to:

- where should the phase boundary live?
- how expensive is KV handoff?
- how much deployment elasticity is worth the transfer cost?

This is the point where KV architecture becomes execution architecture.

## Stage 3: KV As A Managed Multi-Tier Resource

Once the cache is too large to remain fully resident on GPU, the next architectural pressure is no longer only local packing or phase separation. It is state mobility:

- what should remain live?
- what should move out?
- what should be restored?
- what physical path should that movement use?

This is where the retrieval/offloading line and the storage-tier line become central:

- `InfiniGen`
- `IceCache`
- `LouisKV`
- `HiFC`
- `Mooncake`

The key insight is that "offload KV" is not one design. The system must choose both:

- a logical retrieval policy
- a physical storage and transfer path

This is also where benchmark discipline becomes essential. Some papers are mainly about:

- quality under tight token budgets

while others are mainly about:

- latency, throughput, or storage-path viability

So the correct synthesis is not "which one wins?" but "which layer of the movement problem is each paper solving?"

## Stage 4: KV As Cluster Control State

The next transition is that KV begins to influence not just where state lives, but how the serving system reasons globally.

This is the architectural step reflected in:

- `Mooncake`
- `DualMap`
- `JITServe`
- `Seshat`

At this stage, the main questions become:

- should requests be routed toward reusable state?
- how should admission control reflect cache scarcity?
- how should the scheduler reason about locality, transfer cost, and future reuse?

This is an important change in kind. KV is no longer merely data managed by the scheduler. It becomes part of what the scheduler optimizes over.

## Stage 5: KV As A Substitute For Repeated Computation

The reuse/sharing branch reveals the next conceptual shift:

- KV is not only expensive state to preserve
- it is potentially valuable intermediate computation that can replace future prefill work

This branch proceeds through a widening series of reuse contracts:

1. reusable state outside the local engine (`LMCache`)
2. approximate reuse across requests (`KVShare`)
3. semantic similarity as the reuse boundary (`SemShareKV`)
4. partial cross-model reuse with selective recomputation (`DroidSpeak`)
5. representation exchange between agents (`Q-KVComm`)

This is the part of the field where the storage-versus-computation trade becomes explicit. The main question is no longer only:

- how do we store KV cheaply?

It becomes:

- when is stored intermediate state cheaper and better than regenerating it?

That is why this branch cannot be treated as a side algorithm family. It is tightly coupled to:

- persistence
- routing
- compatibility control
- system-level accounting of storage, transfer, and recompute cost

## Stage 6: KV As A Possible Protocol Object

The most forward-looking papers in scope suggest one further transition.

This is not yet fully stabilized, but the signal is visible:

- `DroidSpeak` treats KV as partially reusable across model boundaries
- `Q-KVComm` treats KV-like internal representations as an agent communication medium
- `Agentix` and related workflow papers suggest larger execution structures than one isolated request

Project-level inference:

The field may be moving from "KV as cache" toward "KV as a standardized or semi-standardized intermediate representation."

This is still a hypothesis, not a settled conclusion. But it is supported by the directional logic of the newest reuse papers.

## How The Branches Fit Together

The four comparative branches are not parallel topics. They connect as one layered architecture.

### Phase disaggregation

Defines the macro execution boundary:

- where prefill stops
- where decode begins
- where KV must cross

### Retrieval / offloading

Defines how large state remains usable once it no longer fits the fast path:

- what is retained locally
- what is fetched back
- how the transfer path is organized

### Reuse / sharing

Defines when preserved state can replace future computation:

- across requests
- across engines
- across models
- potentially across agents

### Compression / retention

Defines how cheaply useful state can be kept available in the first place:

- what is evicted
- what is kept
- what is compressed
- what redundancy scope is exploited

These are not competing narratives. They are different layers of one system problem.

## Verified Versus Inferred Claims

The project should keep the following distinction explicit.

### Directly source-backed

- `DistServe` explicitly frames disaggregation around TTFT/TPOT goals and cluster-bandwidth-aware placement.
- `Mooncake` explicitly presents a KVCache-centric architecture with disaggregated cache, global cache, and scheduler under SLOs and real deployment scale.
- `LouisKV` explicitly distinguishes long-input short-output, short-input long-output, and long-input long-output regimes, and ties retrieval to semantic boundaries and temporal locality.
- `IceCache` explicitly combines semantic token clustering with offloading and reports high accuracy retention under tight token budgets.
- `TRIM-KV` explicitly positions itself against quantization, offloading, and heuristic eviction, and learns token retention at creation time for bounded-memory settings.
- `DroidSpeak` explicitly enables reuse across fine-tuned model variants of the same architecture through selective recomputation and pipelined reuse.

### Project-level inference

- the field evolves through the six-stage sequence above
- KV is becoming a protocol object rather than only a cache object
- the most important future competition may be over compatibility contracts, not only compression ratio or retrieval efficiency

These inferences are reasonable given the paper set, but they should remain labeled as synthesis rather than raw paper fact.

## Where The Field Seems To Be Going

The current scope suggests four likely next pressure points:

1. **wider-scope reuse**
   - across more heterogeneous model families, not just fine-tuned variants with the same architecture
2. **stronger coupling between model design and serving architecture**
   - model-side KV footprint changes alter how far disaggregation and reuse can go
3. **global memory services**
   - KV persistence, placement, and retrieval become more explicitly cluster- or workflow-scoped
4. **compatibility and isolation**
   - if KV becomes more shareable, serving systems will need stronger correctness, isolation, and operational guardrails

This is the point where a people/institutions analysis will become more meaningful: we can ask not just who publishes most, but who is defining these next pressure points early.

## Current Best Summary

The cleanest one-paragraph summary of the project so far is:

**The field is moving from managing KV as local inference residue toward managing KV as a first-class systems asset: first as scarce live memory, then as transferred state across service boundaries, then as globally scheduled multi-tier state, and increasingly as reusable intermediate computation across requests, models, and possibly agents.**

That is the main narrative the project can now defend.
