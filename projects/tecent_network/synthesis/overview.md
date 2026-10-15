# Portfolio synthesis

Analysis snapshot: 2026-10-15. The [illustrated HTML report](../output/tencent_networking_report.html) is the main deliverable; [analysis results](../data/analysis_results.json) and [reviewed paper annotations](../data/analysis_papers.json) are its reproducible foundation.

## Scope and denominator

The descriptive set contains 32 user-reviewed primary papers (18 NSDI, 13 SIGCOMM, one CoNEXT), not all Tencent networking research. The two posters are separate. Hestia is a boundary candidate; a networking-core sensitivity view uses 31 papers. Empty venue/year observations and the dated 2026 endpoint are not completeness certificates.

## Main findings

- One-primary-topic partition: DCN/AI infrastructure 8 (25.0%); cloud gateways/offload 7 (21.9%); interactive media/QoE 6 (18.8%); WAN/optical 5 (15.6%); measurement/operations 3 (9.4%); security/privacy 2 (6.3%); cloud-resource optimization 1 (3.1%). Rounding can prevent displayed percentages from summing exactly to 100%.
- Five papers explicitly address AI workloads: Holmes, Astral, SwiftEP, DistDPU and Pegasus. Turbo is general data analytics; P-ECMP/Harp are general datacenter control/reliability. A broad DCN category must not inflate AI-specific shares.
- Academic/research institutions appear on 31 of 32 papers; LADR is Tencent-only. This is a publication-authorship observation, not the distribution of internal R&D effort.
- There are 35 represented academic/research institutions and 96 deduplicated paper–institution ties. Fractional institutional credits sum to 31 because the Tencent-only paper has no academic edge.
- Tsinghua appears on 19 papers, Peking and Michigan on seven each. International presence occurs on 20 papers, with US institutions on 19. These counts overlap and do not measure funding or contribution ownership.

## Interpretation

The strongest unifying theme is operational bottleneck removal: improve resource use, control tail behavior and make heterogeneous infrastructure easier to diagnose. Production experience is an important evidence source, but benchmark/deployment results do not establish comparative market share or a causal business moat. Results have different baselines and cannot be multiplied or added into one savings figure.

Academic connections are more concrete than anonymous partnership labels but less specific than task-level roles. Explicit internships and equal-contribution markers are recorded in [role evidence](../data/analysis_role_evidence.json). They support credited participation, not a general division of labor between universities and Tencent.

## Unresolved

Detailed contribution ownership, global person identities, exact campus geography, comparative economics and Tencent's future roadmap remain unestablished. Five primary final PDFs remain unacquired. The report labels future research directions as hypotheses and records source conflicts and geographic limitations rather than hiding them.
