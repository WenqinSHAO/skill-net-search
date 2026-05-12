# Phase Disaggregation

## Why This Comparison Matters

Phase disaggregation is one of the cleanest architectural lines in the project because all three papers agree on the same basic diagnosis:

- prefill and decode stress hardware differently
- colocating them forces an avoidable compromise
- KV is the state object that couples the two phases

What changes across the line is not the diagnosis, but how far each paper is willing to push the boundary outward and what infrastructure assumptions it is willing to make.

The comparison set is:

- `isca24-001` Splitwise
- `osdi24-002` DistServe
- `arxiv26-001` Prefill-as-a-Service

## Common Problem Frame

All three papers react to the same structural pressure:

- prefill is compute-heavy and bursty
- decode is memory-heavy and latency-sensitive
- the system wants specialization without losing control of the KV handoff

That means phase disaggregation is fundamentally a question of execution architecture, not of local cache efficiency.

## Architectural Progression

### Splitwise: specialization first

Splitwise is the earliest and cleanest statement of the hardware-specialization view.

Its main move is:

- isolate prefill and decode onto different machine types
- accept state transfer as the price of better phase specialization

The design is still relatively early in KV abstraction. KV matters because it is the transferred state, but the paper is not yet building a KV-centric storage or scheduling platform around it.

Best read:

- an argument for phase-specific hardware mapping
- a cluster design paper

### DistServe: SLO-driven service decomposition

DistServe sharpens the same idea by making latency objectives explicit:

- TTFT for prefill
- TPOT for decode

Its main move is:

- treat prefill and decode as different service domains
- optimize resource allocation and placement around the KV handoff

Compared with Splitwise, DistServe is less about hardware heterogeneity per se and more about service objectives under latency constraints. It makes the inter-stage KV boundary operationally central.

Best read:

- an SLO-aware serving architecture
- a paper where KV becomes an inter-stage interface

### Prefill-as-a-Service: disaggregation as deployment elasticity

PrfaaS pushes the boundary much further outward.

Its main move is:

- externalize prefill as a selectively used remote service
- allow cross-cluster or cross-datacenter separation
- rely on model-side KV footprint reduction and bandwidth-aware selection to keep this feasible

Compared with DistServe, the key difference is not just "more disaggregation." It is a different deployment ambition:

- DistServe mainly restructures the serving cluster
- PrfaaS asks how far the phase boundary can move in a heterogeneous and variable infrastructure environment

Best read:

- an elasticity and deployment-boundary paper
- a paper where network realism becomes a first-class constraint

## Benchmark Regime

These papers are comparable, but only if the benchmark framing is kept disciplined.

### Shared comparison axes

- throughput or goodput
- TTFT / TPOT or related latency objectives
- transfer overhead
- cost or cost-normalized efficiency
- hardware or cluster utilization

### Important differences

Splitwise emphasizes:

- throughput
- cost
- power
- machine-type specialization

DistServe emphasizes:

- service under TTFT and TPOT constraints
- goodput under SLO pressure
- placement under cluster bandwidth constraints

PrfaaS emphasizes:

- throughput under bursty, skewed workloads
- cost-normalized throughput
- P90 TTFT
- feasibility under modest WAN or cross-cluster bandwidth

This means a simple "paper X is faster than paper Y" reading would be wrong. The more correct interpretation is that each paper expands the disaggregation argument under a harder operational regime.

## Comparative Judgment

### What Splitwise gets right

- identifies phase asymmetry early and clearly
- makes the case for specialization without requiring a fully KV-centric platform
- establishes the right evaluation family for later phase-boundary work

Main limitation:

- it is earlier and narrower in its view of KV as a system object

### What DistServe adds

- turns phase splitting into an explicit serving architecture
- makes KV transfer the central coupling interface
- ties the architecture to TTFT/TPOT objectives rather than only coarse efficiency

Main limitation:

- still works mostly within a tighter serving-cluster view than later deployment papers

### What PrfaaS adds

- treats disaggregation as elastic deployment rather than only cluster decomposition
- brings heterogeneous infrastructure and bandwidth realism to the foreground
- shows that model-side KV efficiency can unlock wider service boundaries

Main limitation:

- the design’s attractiveness depends more heavily on network conditions, workload skew, and selective invocation policy

## Productization View

If the question is "which paper is closest to a practical product architecture?" the answer depends on the deployment target.

For tightly managed clusters:

- DistServe is the most direct architectural template

For environments seeking cross-cluster elasticity or more modular service boundaries:

- PrfaaS is the more ambitious template

For understanding the core architectural idea with less systems surface area:

- Splitwise is the clearest conceptual starting point

The broader lesson is that phase disaggregation becomes more compelling as KV becomes easier to move or cheaper to reconstruct, but more operationally complex as the network boundary widens.

## Project Takeaway

This line of work establishes one of the central claims of the whole project:

**once KV becomes the state that binds prefill and decode, KV architecture is inseparable from execution architecture.**

The progression from Splitwise to DistServe to PrfaaS can be read as:

1. recognize the phase mismatch
2. formalize the phase boundary as a serving interface
3. push that interface outward until deployment elasticity, bandwidth, and workload skew become the new limiting factors

That makes phase disaggregation the right first comparative branch for the project, because it defines the macro serving architecture that later retrieval, storage-tier, and reuse systems inherit.
