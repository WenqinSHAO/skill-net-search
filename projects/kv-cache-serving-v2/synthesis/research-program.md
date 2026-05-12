# Research Program

## Goal

The next stage of this project is no longer paper coverage. It is structured synthesis.

The synthesis should proceed in four layers:

1. driving forces
2. architectural decomposition
3. in-depth comparative analysis on selected architectural pieces
4. author / affiliation analysis

This sequence is good because it moves from:

- why KV becomes structurally important
- to where the system boundary shifts
- to how competing approaches differ
- to who is driving the field

It also avoids a common failure mode in paper surveys: comparing techniques before clarifying whether they even solve the same architectural problem.

## Judgment

The flow is right. The only refinement is that step 2 should not merely catalog components. It should identify the interface each component controls, because many papers in this project are really arguments about where the interface should move:

- inside one GPU runtime
- between GPU and host/storage tiers
- between prefill and decode services
- between requests routed through one serving fabric
- between different models or agents

That refinement makes step 3 much cleaner, because it prevents false comparisons between:

- a local-memory substrate paper and a scheduler paper
- a retrieval paper and a retention paper
- a same-model reuse system and a cross-model reuse system

## Proposed Flow

### 1. Driving Forces and Historical Motivation

Core question:

- why did KV cache move from an internal optimization detail to a first-class design object?

This section should track the pressure coming from:

- hardware asymmetry
- memory capacity limits
- bandwidth and transfer costs
- longer contexts
- higher concurrency
- multi-turn reuse
- agentic / multi-model workflows
- disaggregated serving
- model-side architectural shifts that reduce or restructure KV footprint

Desired output:

- one coherent narrative of the forces
- a rough timeline of how the pressure evolves
- speculative next-stage pressures
- a mapping from each pressure to the papers where it becomes architecturally explicit

### 2. Architectural Pieces and Interfaces

Core question:

- once KV becomes central, what are the main system pieces people start isolating and optimizing?

The useful refinement here is:

- do not only list components
- also identify the interface each component controls

Examples:

- local memory layout
- retrieval boundary
- prefill/decode transfer boundary
- cache placement and routing interface
- reuse/sharing compatibility interface
- restoration interface
- scheduler and workload-observation interface

Desired output:

- a map of the architectural pieces
- the main unsolved problems under each piece
- which papers define or reshape each piece
- which pieces are substrate, which are boundaries, and which are control planes

### 3. Deep Comparative Analysis

Core question:

- for a few important architectural pieces, how do approaches actually differ in assumptions, mechanisms, workload fit, and productization potential?

This section should be selective rather than exhaustive.

Good candidate comparison clusters:

- phase disaggregation: Splitwise vs DistServe vs PrfaaS
- retrieval/offloading: InfiniGen vs IceCache vs LouisKV vs HiFC
- reuse/sharing: LMCache vs KVShare vs SemShareKV vs DroidSpeak vs Q-KVComm
- retention/compression: Ada-KV vs KeyDiff vs TRIM-KV vs KVTC vs ChunkKV vs PolarQuant vs Joint Encoding

Each comparative note should include:

- problem framing
- workload regime
- system assumption
- benchmark setting and whether it is actually comparable
- implementation burden
- operational/productization fit
- likely failure modes

### 4. Author / Affiliation Analysis

Core question:

- who is repeatedly identifying the right problems early, and who is shaping the field through systems, architecture, or deployment work?

This should not be a vanity list. It should identify:

- researchers who repeatedly define important problem statements
- institutions producing foundational mechanisms
- institutions pushing productizable systems
- relationships between academic and industrial agendas

Desired output:

- clusters of authors / institutions by contribution style
- early signals of who is driving which branch of the field
- a distinction between recurring problem definers, mechanism builders, and deployment builders

## Working Principle

The project should not jump directly into a grand final report.

Instead:

1. build one synthesis file per layer
2. stabilize arguments and comparison axes
3. only later collapse them into one integrated insight report

## Immediate Execution Order

1. Strengthen `driving-forces.md` so it carries the historical argument of why KV became central.
2. Strengthen `architecture-map.md` so each major paper family has a clean place in the design space.
3. Use `comparative-plan.md` to choose the first two serious comparison clusters.
4. Delay strong claims in `people.md` until affiliations are enriched enough to support them.

This means the next deliverable should not yet be a final report. It should be:

- one solid motivation narrative
- one solid architecture map
- one first comparative essay
- one disciplined methodology for people analysis
