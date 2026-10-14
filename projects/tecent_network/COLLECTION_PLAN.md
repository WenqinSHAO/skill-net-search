# Collection and analysis plan

The first deliverable is a working publication workbook. Its initial official-program sweep is partial. The desired endpoint is a defensible survey of all publicly discoverable Tencent networking publications, with documented residual gaps.

## 1. Historical and venue coverage

Keep a venue/year ledger with the discovery source, full proceedings denominator where available, number of Tencent candidates, included/excluded decisions, parser failures, and affiliation audit status. A successfully parsed page alone does not establish recall. Distinguish a supported zero-Tencent scan from a failed fetch and from an unattempted year.

Active priority: NSDI, SIGCOMM, CoNEXT/PACMNET, IMC and HotNets for 2019–2026. ICNP and mobile-centric conferences are excluded by user request. Later candidates include INFOCOM/ToN, APNet/ICCCN and relevant systems, security, and AI/HPC venues for communication-focused infrastructure contributions. Search Chinese-language publications and Tencent engineering sources as well as English proceedings. The broader historical objective remains 1998 onward, respecting each venue's existence dates.

The 2026-10-10 extension adds independently discovered CoNEXT 2021 and SIGCOMM poster records, recovers the otherwise empty CoNEXT Angular program pages, compares titles to a separate bibliographic catalog including PACMNET, and screens publicly linked paper PDF headers. Manual checks are retained in `data/manual_checks.json`; residual unmatched catalog records and unavailable URLs remain visible. Keep primary-venue counts separate from posters and affiliated workshops. 2026 is year-to-date, not a completed annual total.

Use three independent discovery routes: proceedings affiliation sweeps; institution-index queries for Tencent and its aliases; and publication lists of Tencent authors and their academic coauthors. Follow citation trails. An author's current Tencent role never makes all of their earlier papers Tencent papers. Funding acknowledgements and product deployment are separate relationships from author affiliation.

### Paper-level reconciliation now implemented

The workbook now exposes `Proceedings_Ledger`, `Completeness` (40 cells), `Unresolved_Queue`, and source/exclusion diagnostics. The ledger joins official listings with an independently collected DBLP/PACMNET inventory and retains publication-type ambiguity. Its program-negative decisions require either complete ordered-author agreement with the bibliography or an explicitly weaker program-only label. PDF negatives require matching title and all expected author names, and remain screening evidence, never exhaustive manual affiliation certification.

An additional 143 NSDI PDFs were successfully screened. FlexWAN's accepted-title/final-title change is linked using the complete ordered author list and retained as a reviewable variant. CoNEXT 2022 poster URLs serving explicitly headed 2020 content are excluded as stale templates. The recent 2026 DBLP refresh returned anti-bot/non-JSON pages, so failed refresh attempts are retained rather than interpreted as empty proceedings.

Next closure batches, in order:

1. Review `Unresolved_Queue` by venue/year, beginning with unsupported early IMC/CoNEXT layouts and catalog-only SIGCOMM records; reconcile accepted lists, final programs and publisher proceedings, including companion posters separately.
2. Inspect final PDFs for author lists, superscripts, current-address footnotes and conflicting program affiliations. Upgrade affiliation decisions only after individual assignments are reviewed; keep Dorado's accepted/program discrepancy open until resolved.
3. Independently audit Tencent researcher and academic collaborator publication lists against the ledger; retain dated employment evidence and every inclusion/exclusion decision.
4. Recheck 2026 proceedings after publication, resolve CoNEXT/PACMNET manifestation links, and only then assess cell-level completeness. The current corpus count is an observed lower bound, not a recall estimate.

## 2. Metadata and affiliation audit

Completed metadata batch (2026-10-14): all 32 primary papers in the user-added official-link section reconcile with the inventory. Full abstracts and individual author assignments are now sourced and reviewed for these 32 papers: 27 against PDF headers, five against publisher deposits. All 16 DOI-bearing records (including the two separately retained posters) match the complete publisher-deposited author order. The compact handoff is `output/tencent_networking_metadata.xlsx`; detailed source checks and discrepancy notes remain in the full workbook. This completes required author/abstract metadata for the reviewed set, not venue-level recall, keywords absent from inaccessible papers, author identity disambiguation, or all manifestation links.

Resolve publisher identifiers and preserve exact titles and author order. Recover abstracts and author/publisher keywords from official pages or PDFs; do not present classification tags or publisher subject categories as author keywords. Preserve source URL, cached artifact, and retrieval date for each enrichment.

Inspect PDF author blocks and superscripts to reconcile author-to-affiliation assignments. Preserve joint appointments, internships, publication-time affiliations, explicit unaffiliated status, and current-address footnotes separately. Use department/laboratory units as attributes of parent universities where evidence supports that relationship; avoid counting one university multiple times because its department and key laboratory are both listed.

Match DBLP person IDs or ORCIDs using bibliographic and dated affiliation evidence. Homonyms remain unresolved until checked. Institution aliases, campuses, countries, and regions need their own reviewed evidence. Institution geography is not author nationality.

## 3. Scope, topics, and versions

Assign multiple reviewed area tags, including overlapping DCN and AI infrastructure where appropriate. Separate technical mechanisms (RDMA, congestion control, routing, telemetry) from workloads (LLM training, inference, real-time media). Read abstracts and relevant paper sections for ambiguous cases. Retain exclusions with reasons.

Link preprint, workshop, conference, and journal versions. Keep all manifestations in the inventory but use work families for research-output counts and publication instances for venue analysis. Similar titles alone do not justify merging distinct works.

## 4. Analysis after the data audit

Produce area-by-year publication counts, Tencent-to-institution edges, and area-specific collaboration tables. Report full and fractional counts together. Identify repeat partnerships and the evidence for person-level continuity. Map institutional geography only after country/region enrichment, showing missing geography explicitly.

For the global picture, report the observed corpus, coverage by venue/year, metadata completeness, missing affiliations, and identity confidence beside every network view. Coauthorship supports an observed research connection; it does not establish funding, a formal partnership, leadership, or technology transfer. Those require separate evidence.

## Completion criteria

- Every planned venue/year has an explicit audit state and no silent collection failure.
- Discovery routes are reconciled and independently checked for missed papers.
- Each included publication has a primary source, ordered authors, and individually evidenced affiliations or an explicit unresolved flag.
- Abstracts, keyword gaps, institution normalization, geographic evidence, and author identities are quantified.
- Scope decisions and topic assignments are reviewable; version families are reconciled before aggregate counting.
- The workbook rebuilds from cached evidence plus reviewed overrides, and structural/reader checks pass.
- Residual gaps are stated; exhaustive coverage is claimed only where the evidence supports it.


## Offical Programm or paper links

### SIGCOMM
- 2026: https://conferences.sigcomm.org/sigcomm/2026/accepted/
  - Dorado: Scaling SmartNIC Session Tables on Commodity DDRs
  - XFir: Accelerating New-Flow Setup on Host Servers of a Large Cloud Network
  - Rethinking Cloud Optimization: Volatility-Driven for Better Outcomes
  - DistDPU: A Disaggregated DPU Architecture for High-Performance and Cost-Efficient AI Clouds
  - CubeTrace: Microscopic Network Tracing for Heterogeneous Cloud Gateways
  - Pegasus: A Data Center Network for Bare-Metal AI Cloud
- 2025: https://conferences.sigcomm.org/sigcomm/2025/accepted-papers/
  - Fornax: A Hardware-Centric Session Management in Large Public Cloud Network
  - PreTE: Traffic Engineering with Predictive Failures
  - Astral: A Datacenter Infrastructure for Large Language Model Training at Scale
- 2024: https://conferences.sigcomm.org/sigcomm/2024/accepted-papers/
  - Turbo: Efficient Communication Framework for Large-scale Data Processing Cluster
  - MegaTE: Extending WAN Traffic Engineering to Millions of Endpoints in Virtualized Cloud
- 2023: https://conferences.sigcomm.org/sigcomm/2023/list-accepted.html
  - FlexWAN: Software Hardware Co-design for Flexible and Cost-Effective Optical Backbones
  - TENSOR: Lightweight BGP Non-Stop Routing
- 2022: https://conferences.sigcomm.org/sigcomm/2022/program.html
  - NA
- 2021: https://conferences.sigcomm.org/sigcomm/2021/program.html
  - NA
- 2020: https://conferences.sigcomm.org/sigcomm/2020/program.html
  - NA
- 2019: https://conferences.sigcomm.org/sigcomm/2019/program.html
  - NA

### NSDI
- 2026: https://www.usenix.org/conference/nsdi26/technical-sessions
  - BLADE: Adaptive Wi-Fi Contention Control for Next-Generation Real-Time Communication
  - MirrorNet: High-fidelity and Scalable Network Emulation for Software-defined WAN
  - DDoS Detection at the Scale of One Hundred Tbps
  - SwiftEP: Accelerating MoE Inference with Buffer Fusion and TMA Offloading
  - From Source to Solution: Tackling Packet Losses in Large-scale Cloud Gaming Systematically and Precisely
  - A Composable Emulation Framework for Whitebox Switches
  - Harp: Improving VPC Network Availability via Efficient Failure Detection and Rerouting in Tencent Cloud
  - Cost-effective and Reliable Global Internet Peering with Programmable Switches
- 2025: https://www.usenix.org/conference/nsdi25/technical-sessions
  - Holmes: Localizing Irregularities in LLM Training with Mega-scale GPU Clusters
  - Unlocking ECMP Programmability for Precise Traffic Control
- 2024: https://www.usenix.org/conference/nsdi24/technical-sessions
  - Pudica: Toward Near-Zero Queuing Delay in Congestion Control for Cloud Gaming
  - Hairpin: Rethinking Packet Loss Recovery in Edge-based Interactive Video Streaming
  - AUGUR: Practical Mobile Multipath Transport Service for Low Tail Latency in Real-Time Streaming
- 2023: https://www.usenix.org/conference/nsdi23/technical-sessions
  - Boomerang: Metadata-Private Messaging under Hardware Trust
  - Enabling High Quality Real-Time Communications with Adaptive Frame-Rate
- 2022: https://www.usenix.org/conference/nsdi22/technical-sessions
  - Detecting Ephemeral Optical Events with OpTel
  - Elixir: A High-performance and Low-cost Approach to Managing Hardware/Software Hybrid Flow Tables Considering Flow Burstiness
- 2021: https://www.usenix.org/conference/nsdi21/technical-sessions
  - Accessing Cloud with Disaggregated Software-Defined Router
- 2020: https://www.usenix.org/conference/nsdi20/technical-sessions
  - NA
- 2019: https://www.usenix.org/conference/nsdi19/technical-sessions
  - NA

### IMC
- 2026: https://conferences.sigcomm.org/imc/2026/accepted-papers/
  - NA
- 2025: https://conferences.sigcomm.org/imc/2025/accepted-papers/
  - NA
- 2024: https://conferences.sigcomm.org/imc/2024/accepted-papers/
  - NA
- 2023: https://conferences.sigcomm.org/imc/2023/program/
  - NA
- 2022: https://conferences.sigcomm.org/imc/2022/program/
  - NA
- 2021: https://conferences.sigcomm.org/imc/2021/accepted/
  - NA
- 2020: https://conferences.sigcomm.org/imc/2020/accepted/
  - NA
- 2019: https://conferences.sigcomm.org/imc/2019/accepted/
  - NA

### CoNEXT
- 2026: https://conferences.sigcomm.org/co-next/2026/#!/accepted-papers
  - NA
- 2025: https://conferences.sigcomm.org/co-next/2025/#!/program
  - NA
- 2024: https://conferences.sigcomm.org/co-next/2024/#!/accepted-papers
  - NA
- 2023: https://conferences.sigcomm.org/co-next/2023/#!/accepted-papers
  - NA
- 2022: https://conferences.sigcomm.org/co-next/2022/#!/program
  - NA
- 2021: https://conferences.sigcomm.org/co-next/2021/#!/program
  - Discovering Obscure Looking Glass Sites on the Web to Facilitate Internet Measurement Research
- 2020: https://conferences.sigcomm.org/co-next/2020/#!/program
  - NA
- 2019: https://conferences.sigcomm.org/co-next/2019/#!/program
  - NA

### HotNets
- 2026: https://conferences.sigcomm.org/hotnets/2026/program.html
  - NA
- 2025: https://conferences.sigcomm.org/hotnets/2025/program.html
  - NA
- 2024: https://conferences.sigcomm.org/hotnets/2024/program.html
  - NA
- 2023: https://conferences.sigcomm.org/hotnets/2023/program.html
  - NA
- 2022: https://conferences.sigcomm.org/hotnets/2022/program.html
  - NA
- 2021: https://conferences.sigcomm.org/hotnets/2021/program.html
  - NA
- 2020: https://conferences.sigcomm.org/hotnets/2020/program.html
  - NA
- 2019: https://conferences.sigcomm.org/hotnets/2019/program.html
  - NA
