# Networking Researcher Itineraries, 2018-2026

## Intent

This project studies how researchers who appeared in top networking conferences during 2018-2022 changed, broadened, or maintained their publication portfolios through 2026.

The primary object is not a pre-labeled migration class. The primary object is a **researcher itinerary**: a year-by-year record of the researcher's clean conference publications, with titles, venues, abstracts when available, and identity/context metadata.

The immediate goal is to make the data foundation auditable and bias-resistant before moving to stronger claims about migration, AI shifts, or researcher archetypes.

## Where We Are

Current project stage:

1. The broad cohort definition is fixed for now.
2. The year-by-year itinerary data has been built for the cohort.
3. A high-signal working slice, the **core-99**, is being used to test preprocessing and descriptive analysis choices.
4. Deterministic investigation tables for the first core-99 questions are in place.
5. LLM-driven itinerary summarization is intentionally postponed until the deterministic foundation is reviewed.

Current scope and sample definitions:

- **Broad cohort**: researchers with at least one paper in `SIGCOMM`, `NSDI`, `CoNEXT`, `HotNets`, or `IMC` during `2018-2022`.
- **Current broad cohort size**: `3,571` researchers.
- **Baseline window**: `2018-2022`.
- **Post-baseline window**: `2023-2026`.
- **Current high-signal slice**: the provisional **core-99**, selected as `baseline_top_networking_count > 6` from the cohort-shape review.

This core-99 slice is a derived working sample for deeper review. It does **not** replace the raw cohort.

## Current Methodological Commitments

### Cohort Scope

The cohort is intentionally scoped by elite networking visibility:

- A researcher is in scope if they authored **at least one** paper at SIGCOMM, NSDI, CoNEXT, HotNets, or IMC during **2018-2022**.
- This is an intended bias: the study asks what happened to researchers visibly present in top networking venues, not to every networking-adjacent researcher.
- We are not currently using sliding windows or alternate cohort definitions as the main line of analysis.

### Publication Scope

Records are retained for auditability but excluded from analysis if they are:

- journals/articles,
- CoRR/arXiv records,
- proceedings volumes,
- books, theses, `www`, `data`, and other non-conference DBLP record types,
- missing venue,
- duplicate records for the same researcher.

Executable scope rules live in `scripts/publication_scope.py`.

### Analysis Philosophy

The project does **not** currently treat Zone 1/2/3 labels as the analytical foundation.

Instead, the current ordering is:

1. build auditable raw and clean publication evidence,
2. derive deterministic descriptive attributes,
3. inspect high-signal slices,
4. only later attempt stronger trajectory or migration interpretation.

This is deliberate. It reduces the chance that early rigid labels silently shape the later story.

## Recommended Chaining

A new person or agent should follow the project in this order.

### 1. Broad Cohort Definition

Start here to understand who is in scope and why.

- Script: `scripts/identify_cohort.py`
- Primary output: `data/qualified_cohort.json`

This file defines the broad cohort from the five qualifying networking venues.

### 2. Publication Collection And Scope Filtering

Then inspect how raw DBLP publication records are pulled and filtered into usable conference evidence.

- Script: `scripts/fetch_publications.py`
- Scope rules: `scripts/publication_scope.py`
- Primary output: `data/publication_history.json`

This is the main raw-to-clean transition layer. If something looks wrong later, check here first.

### 3. Itinerary Construction

The itinerary is the main evidence artifact for later analysis.

- Script: `scripts/build_itineraries.py`
- Primary output: `data/researcher_itineraries.json`
- Discovery subset: `data/top100_itineraries.json`

Each itinerary stores year-by-year clean conference publications, plus enriched authorship-position fields.

### 4. Broad Descriptive Audit

Before interpreting researchers, inspect the cohort shape.

- Script: `scripts/analyze_cohort_shape.py`
- Main doc: [COHORT_SHAPE.md](/home/wenqin/net-search/projects/networking-to-ai-migration/COHORT_SHAPE.md)
- Key derived outputs:
  - `data/cohort_shape_high_total_outliers.csv`
  - `data/cohort_shape_total_one_researchers.csv`
  - `data/cohort_shape_candidate_core_network_gt6.csv`

This is where the provisional `baseline_top_networking_count > 6` working slice came from.

### 5. Core-99 Unified Investigation (Active Analysis Layer)

The core-99 is the current microscope sample. All analysis is consolidated in one document.

- **Primary analysis**: [CORE99_ANALYSIS.md](/home/wenqin/net-search/projects/networking-to-ai-migration/CORE99_ANALYSIS.md) — unified narrative: static baseline → static post-2023 → delta/migration → **forward-looking new-core landscape (§11)**
- **Detailed investigation**: [CORE99_INVESTIGATION.md](/home/wenqin/net-search/projects/networking-to-ai-migration/CORE99_INVESTIGATION.md) — full decompositions, cross-method synthesis, all tables
- **Detailed attributes**: [CORE99_RESEARCHER_ATTRIBUTES.md](/home/wenqin/net-search/projects/networking-to-ai-migration/CORE99_RESEARCHER_ATTRIBUTES.md)
- **Deterministic Q1-Q3 tables**: [CORE99_INVESTIGATION_TABLES.md](/home/wenqin/net-search/projects/networking-to-ai-migration/CORE99_INVESTIGATION_TABLES.md)
- **Author-position audit**: [CORE99_AUTHOR_POSITION_ISSUES.md](/home/wenqin/net-search/projects/networking-to-ai-migration/CORE99_AUTHOR_POSITION_ISSUES.md) (resolved: zero unresolved rows)
- **Selection review**: [SELECTED_SAMPLE_NETWORK_GT6.md](/home/wenqin/net-search/projects/networking-to-ai-migration/SELECTED_SAMPLE_NETWORK_GT6.md)

Key data artifacts:
  - `data/core99_researcher_attributes.json` / `.csv` — per-researcher deterministic attributes
  - `data/core99_investigation_summary.json` — aggregated Q1-Q3 results
  - `data/core99_sys_ai_storage_quadrants.csv` — quadrant analysis (60 researchers in elite sys/AI/storage venues)
  - `data/selected_sample_network_gt6_packet.json` — full title-level evidence for core-99
  - `data/venue_family_map.json` — venue→family mapping (343 mappings, 24 aliases; Q1: 0% unknown, Q2: 2.2%, core-99: 3.6%)

### 6. New-Core Forward-Looking Data Repair (Active, June 2026)

The future-looking direction is active, but the first `post-GPT core` outputs are
now treated as exploratory/provisional. The validated direction is renamed
**new-core**: current leading researchers with at least 7 clean qualifying
top-networking papers in the observed 2023-2026 window.

Why this repair exists:
- the old `post_gpt_core` builder mixed itinerary counts with raw DBLP TOC counts,
- DBLP TOC records included posters, demos, proceedings-volume records, and
  workshops,
- CoNEXT/PACMNET needs the same conference-integrated exception used by the
  core-99 pipeline,
- researcher topic profiles silently skipped DBLP-only complete newcomers,
- 2026 is intentionally included as observed data but remains incomplete.

Current repaired artifacts:
  - `data/pacmnet_toc_papers.json` — PACMNET DBLP TOC records for CoNEXT long-paper evidence
  - `data/new_core_clean_papers.json` — canonical clean-paper table (2,236 main papers) with
    inclusion/exclusion reasons, source tags, and venue-year coverage diagnostics
  - `data/new_core.json` — repaired new-core/stayer/newcomer/dropout split
  - `data/new_core_researcher_profiles.json` / `.csv` — descriptive venue-count/author-role profiles; needs regeneration after the canonical venue completeness repair
  - `data/new_core_topic_profiles.json` / `.csv` — per-researcher topic profiles; stale until topic taxonomy and repaired paper table are re-run together
  - `data/paper_topic_labels_v2.json` — per-paper topic labels from the earlier repaired data; stale after the 2,236-paper completeness repair
  - `data/venue_topic_vectors_v2.json` — venue-year topic feature vectors; stale after the 2,236-paper completeness repair
  - `data/venue_topic_evolution_v2.csv` — CSV of venue-year topic shares; stale after the 2,236-paper completeness repair

Current repaired count snapshot from `scripts/fetch_pacmnet_tocs.py` plus
`scripts/build_new_core.py`:
- **new-core**: 124 researchers
- **stayers**: 46 researchers also in core-99
- **newcomers**: 78 researchers not in core-99
- **dropouts**: 53 core-99 researchers below the new-core threshold
- **complete newcomers outside broad cohort**: 12

Interpretive topic findings from the earlier new-core pass are now stale because the canonical venue completeness repair changed the clean paper table from 2,170 to 2,236 papers and changed the new-core split. Rebuild topic labels and researcher profiles after the networking-topic taxonomy is repaired.

Important caveat remains: 2026 venue coverage is observed-as-available rather
than complete. NSDI 2026 is indexed and complete; SIGCOMM, CoNEXT/PACMNET, HotNets, and IMC 2026 are not yet available in the canonical DBLP TOC source. Existing topic-profile artifacts are stale until rebuilt from the 2,236-paper table.

Old exploratory artifacts retained for comparison:
  - `data/post_gpt_core.json`
  - `data/post_gpt_venue_papers.json`
  - `data/paper_topic_labels.json` (v1)
  - `data/venue_topic_vectors.json` (v1)
  - `data/researcher_topic_profiles.json` (v1)

### 7. Data Apparatus And Venue-Year Background (Diagnostic, June 2026)

The reorganized analysis now starts with explicit paper scopes and cohort-neutral
venue background before returning to researcher interpretation. Current I.2
outputs are diagnostic only for topic interpretation: venue-year raw coverage is now repaired and audited, while the Stage-1 topic classifier remains inadequate for substantive venue-evolution claims.

Scope terminology:
- **total papers**: all in-scope conference papers attached to a researcher after deduplication and record cleaning
- **net papers**: total papers that are networking-related
- **top-net papers**: net papers in SIGCOMM, NSDI, CoNEXT, HotNets, or IMC
- **author-summed count**: researcher-paper incidences; coauthored papers can count once per scoped researcher
- **unique-paper count**: paper union; coauthored papers count once

Current I.1/I.2 artifacts:
  - [TOPNET_VENUE_COMPLETENESS.md](/home/wenqin/net-search/projects/networking-to-ai-migration/TOPNET_VENUE_COMPLETENESS.md) — raw TOC completeness audit for top-networking venue-years
  - [VENUE_YEAR_BACKGROUND.md](/home/wenqin/net-search/projects/networking-to-ai-migration/VENUE_YEAR_BACKGROUND.md) — diagnostic table/text report; clean-vs-raw count differences are expected scope distinctions
  - `data/analysis_scope_manifest.json` — canonical scope definitions and aggregation modes
  - `data/analysis_scope_audit.json` / `.csv` — inclusion/exclusion audit from repaired top-net table
  - `data/venue_year_background.json` / `.csv` — diagnostic cohort-neutral all-top-net-year and venue-year background rows
  - `data/venue_year_topic_vectors_stage1.json` — Stage-1 keyword topic vectors for debugging only; not analysis-ready
  - `data/venue_year_author_concentration.csv` — unique authors, repeat-author share, top-k share, Gini, HHI

Important: these are venue-background diagnostics. They intentionally do **not**
yet overlay core-99/new-core/stayer/newcomer/dropout labels. The raw top-net
venue completeness gate is now satisfied for available DBLP TOCs. The v3.1
semantic classifier now passes validation and can be used to revisit the I.2
venue baseline, with quality fields kept visible.

### 8. Three-Axis Paper Classification (Validated, June 2026)

The current three-axis LLM-based classifier uses DeepSeek V4 Flash and taxonomy v3.1. Each paper is labeled across three dimensions:

- **Scenario** (13 values): the network deployment context (dcn_ai_training,
  dcn_ai_inference, dcn_cloud, dcn_storage, dcn_mixed, dcn_general, wan,
  wireless, interconnect, edge, cdn, internet_core, and unknown scenario)
- **Mechanism** (20 values): the networking function studied (routing,
  traffic_engineering, congestion_control, flow_scheduling, resource_allocation,
  topology_design, transport_design, measurement_telemetry, security,
  coordination, collective_comm, app_scheduling, plus v3.1 additions such as
  packet processing/network programming, DNS/naming, video/QoE/streaming,
  sensing/localization, policy/censorship/economics, reliability/resilience,
  experimentation/tooling, and unknown mechanism)
- **Method** (10 values): the research approach used (sdn, programmable_dataplane,
  formal_verification, virtualization, hardware_acceleration, ml_based,
  optimization_theoretic, systems_building, empirical_measurement,
  simulation_emulation)

The taxonomy is the single source of truth at `data/taxonomy_v3.json`.
Current version is v3.1: it adds explicit unknown labels and missing networking mechanism categories from the I.5 review.

Current validated pipeline: `fetch_paper_abstracts.py` -> `classify_paper_topics_v3.py` -> `validate_classification_v3.py` -> `regenerate_v2_artifacts.py`. `regenerate_v2_artifacts.py` now refuses to run unless validation passes, unless `--allow-invalid` is used for debugging only.

Current v3.1 validation snapshot (2,236 papers, DeepSeek V4 Flash):
- 2,204 papers have title+abstract evidence (98.6%); 32 are title-only (1.4%).
- Validation passes: zero missing scenario/mechanism labels, zero classification-error rows, zero title-only-not-uncertain rows.
- NSDI 2023 abstracts are repaired from the official USENIX inline technical-sessions page: 96/96 matched, 0 title-only.
- Regenerated artifacts: `data/paper_topic_labels_v3.json`, `data/venue_topic_vectors_v3.json`, `data/venue_topic_evolution_v3.csv`, and `data/new_core_topic_profiles.json`.
- Remaining caution: the method axis is still broad. `systems_building` appears in 1,260 papers (56.4%), so first-pass venue baseline interpretation should emphasize scenario/mechanism and treat method as secondary evidence.

### 9. Project Plan And Status

For the evolving TODO list and sequencing logic, read:

- [ANALYSIS_PLAN.md](/home/wenqin/net-search/projects/networking-to-ai-migration/ANALYSIS_PLAN.md)

This is the best place to check what is considered current, provisional, completed, or intentionally deferred.

## Script Roles

The main scripts and their current roles are:

| Script | Current role |
|---|---|
| `scripts/identify_cohort.py` | Build the broad researcher cohort from the five qualifying venues |
| `scripts/fetch_publications.py` | Fetch DBLP publication histories for scoped researchers |
| `scripts/publication_scope.py` | Define executable clean/excluded publication rules |
| `scripts/build_itineraries.py` | Build year-by-year clean itineraries with authorship-position fields |
| `scripts/analyze_cohort_shape.py` | Produce broad cohort-shape summaries and candidate slices |
| `scripts/build_selected_sample_packet.py` | Export the provisional `network > 6` selected-sample evidence packet |
| `scripts/build_core99_attributes.py` | Build deterministic observable attributes for the core-99 |
| `scripts/audit_core99_author_positions.py` | Audit author-position match coverage and alias issues |
| `scripts/build_core99_investigation_tables.py` | Build deterministic tables for the first core-99 investigation questions |
| `scripts/build_comparison_cohort.py` | Build 2013-2017 comparison cohort for regression-to-the-mean check |
| `scripts/fetch_pacmnet_tocs.py` | Fetch PACMNET TOC records for CoNEXT long-paper evidence |
| `scripts/build_new_core.py` | Build repaired new-core cohort and canonical clean paper table |
| `scripts/build_new_core_profiles.py` | Build descriptive venue-count/author-role profiles; rerun after canonical venue completeness repair |
| `scripts/build_new_core_topic_profiles.py` | 🆕 Build researcher topic profiles from canonical clean paper table (active) |
| `scripts/fetch_topnet_venue_year_papers.py` | 🆕 Fetch paginated canonical top-net venue-year DBLP TOC records |
| `scripts/audit_topnet_venue_completeness.py` | 🆕 Audit raw TOC completeness vs clean main-paper scope |
| `scripts/build_scope_and_venue_background.py` | 🆕 Build I.1 scope manifest/audit and I.2 cohort-neutral venue-year background artifacts |
| `scripts/classify_paper_topics.py` | Paper topic classifier: keyword-based v2 by default; auto-delegates to v3 LLM classifier when taxonomy_v3.json exists |
| `scripts/classify_paper_topics_v3.py` | 🆕 Three-axis LLM-based classifier (DeepSeek V4 Flash JSON mode) — scenario × mechanism × method |
| `scripts/fetch_paper_abstracts.py` | 🆕 Fetch paper abstracts from USENIX NSDI pages plus OpenAlex/Semantic Scholar APIs; quarantines unsafe title matches |
| `scripts/regenerate_v2_artifacts.py` | 🆕 Orchestrator: regenerate all downstream artifacts from v3 paper labels |
| `scripts/validate_classification_v3.py` | 🆕 Post-classification validation: label coverage, distribution sanity, confidence checks |
| `scripts/audit_classification_v3_quality.py` | 🆕 I.5 review audit: abstract coverage, title-match risk, zero-label/error cases |
| `scripts/build_post_gpt_core.py` | ⛔ DEPRECATED — old post-GPT core builder; retained for comparison only |
| `scripts/build_researcher_topic_profiles.py` | ⛔ DEPRECATED — old itinerary-based topic profiles; retained for comparison only |
| `scripts/classify_zones.py` | Legacy/auxiliary conservative paper tagging, not current analytical foundation |
| `scripts/compute_metrics.py` | Legacy/auxiliary aggregate metrics |
| `scripts/generate_charts.py` | Legacy chart/report generation |
| `scripts/regenerate_charts.py` | Regenerate PCA/delta figures with consistent styling |

## Main Artifacts

The most important artifacts are grouped below by role.

### Broad Cohort And Raw Foundation

| File | Meaning |
|---|---|
| `data/qualified_cohort.json` | Broad cohort selected from top networking venues |
| `data/publication_history.json` | Full DBLP publication records with scope metadata |
| `data/publication_history_zones.json` | Auxiliary conservative paper tags |
| `data/publication_history_geo.json` | Publication records plus geography metadata |
| `data/researcher_itineraries.json` | Primary year-by-year raw evidence artifact |
| `data/top100_itineraries.json` | Discovery subset ranked by baseline top-networking count |

### Broad Audit And Slice Construction

| File | Meaning |
|---|---|
| [COHORT_SHAPE.md](/home/wenqin/net-search/projects/networking-to-ai-migration/COHORT_SHAPE.md) | Readable broad cohort-shape review |
| `data/cohort_shape_candidate_core_network_gt6.csv` | Provisional high-signal slice used to define the core-99 |
| [SELECTED_SAMPLE_NETWORK_GT6.md](/home/wenqin/net-search/projects/networking-to-ai-migration/SELECTED_SAMPLE_NETWORK_GT6.md) | Readable packet for the provisional selected sample |
| `data/selected_sample_network_gt6_packet.json` | Title-level evidence for the selected sample |

### Core-99 Foundation

| File | Meaning |
|---|---|
| [CORE99_RESEARCHER_ATTRIBUTES.md](/home/wenqin/net-search/projects/networking-to-ai-migration/CORE99_RESEARCHER_ATTRIBUTES.md) | Readable deterministic attribute summary for the core-99 |
| `data/core99_researcher_attributes.csv` | Spreadsheet-friendly core-99 attributes |
| `data/core99_researcher_attributes.json` | Full structured core-99 attributes |
| [CORE99_AUTHOR_POSITION_ISSUES.md](/home/wenqin/net-search/projects/networking-to-ai-migration/CORE99_AUTHOR_POSITION_ISSUES.md) | Authorship-position audit report |

### Core-99 Investigation

| File | Meaning |
|---|---|
| [CORE99_INVESTIGATION_TABLES.md](/home/wenqin/net-search/projects/networking-to-ai-migration/CORE99_INVESTIGATION_TABLES.md) | Deterministic investigation results for current questions |
| `data/core99_investigation_summary.json` | Structured summary of current investigation tables |
| `data/core99_researcher_venue_family_transitions.csv` | Baseline/post venue-family transitions per researcher |
| `data/core99_topnet_decrease_clean_flat_or_increase.csv` | Slice for researchers whose top-net decreases while overall output stays flat/increases |
| `data/core99_topnet_flat_or_increase_profiles.csv` | Slice for researchers with flat/increased top-net presence |
| `data/top_venue_author_concentration_2018_2022.csv` | Venue concentration metrics for the five qualifying conferences |
| `data/venue_family_map.json` | Current conservative venue-family normalization |
| `data/core99_sys_ai_storage_quadrants.csv` | Quadrant split for core-99 researchers who publish in top-tier systems/AI/storage venues |

## Current Investigation Questions

The current deterministic investigation layer is centered on these questions:

1. For core-99 researchers whose top-networking rate decreases while overall clean publication output is flat or increasing, where does the output go?
2. For core-99 researchers whose top-networking rate is flat or increasing, what profiles do they have in terms of venue mix and authorship placement?
3. Are some qualifying conferences, especially IMC, more concentrated communities than the others?
4. How should these deterministic findings shape later comparison-group construction beyond the core-99?

LLM-driven itinerary summarization is a later step, not the current foundation.

## Recommended Entry Points

If you are new to the repo, use this order:

1. Read this `README.md`.
2. Read [ANALYSIS_PLAN.md](/home/wenqin/net-search/projects/networking-to-ai-migration/ANALYSIS_PLAN.md).
3. Read [COHORT_SHAPE.md](/home/wenqin/net-search/projects/networking-to-ai-migration/COHORT_SHAPE.md).
4. Read [CORE99_RESEARCHER_ATTRIBUTES.md](/home/wenqin/net-search/projects/networking-to-ai-migration/CORE99_RESEARCHER_ATTRIBUTES.md).
5. Read [CORE99_INVESTIGATION_TABLES.md](/home/wenqin/net-search/projects/networking-to-ai-migration/CORE99_INVESTIGATION_TABLES.md).
6. Then inspect the underlying CSV/JSON artifacts if a specific claim needs verification.

If something looks inconsistent, check `data/publication_history.json`, `scripts/publication_scope.py`, and `scripts/build_itineraries.py` before changing higher-level analysis.

## Running The Main Pipeline

The original main pipeline remains available:

```bash
bash scripts/run_pipeline.sh
```

In practice, the current work has also been using targeted rebuilds of specific derived artifacts after scope-rule or attribute changes.

## Open Work

Near-term open work:

- revisit I.2 venue baseline using validated v3.1 semantic vectors, with quality fields shown beside every venue-year row,
- design conference evolution charts from `data/venue_topic_evolution_v3.csv` / `data/venue_topic_vectors_v3.json`,
- run formal clustering of researcher topic profiles (PCA + k-means on `data/new_core_topic_profiles.json`),
- run regression-to-the-mean check with 2013-2017 comparison cohort (`build_comparison_cohort.py`),
- add career-stage proxy and author-role analysis for newcomers (author-role data in `new_core_researcher_profiles.json`),
- strengthen geo and especially sector labels,
- build comparison groups beyond the core-99 (near-core sample, broad cohort),
- further audit the method axis, especially `systems_building`, before making strong method-level claims.

Completed June 2026:

- ✅ Top-net venue completeness repaired for available DBLP TOCs (124 new-core researchers; 46/78/53 split)
- ✅ PACMNET TOC integration for CoNEXT 2023-2025 long-paper evidence
- ✅ Topic taxonomy v3.1 validated: 2,236 papers classified with zero validation errors
- ✅ Abstract coverage repaired to 2,204 / 2,236 papers (98.6%); NSDI 2023 is 96/96 from official USENIX inline abstracts
- ✅ Semantic venue/researcher vectors regenerated after validation passed
- ✅ Documentation consistency restored for the venue-completeness and topic-classification checkpoints (README.md, ANALYSIS_PLAN.md, I5_CLASSIFICATION_REVIEW.md)

Old exploratory outputs (deprecated but retained for comparison):
  - `data/post_gpt_core.json` (113/40/73/59)
  - `data/paper_topic_labels.json`, `venue_topic_vectors.json`, `venue_topic_evolution.csv` (v1)
  - `data/researcher_topic_profiles.json`, `data/post_gpt_core_profiles.csv` (v1)
