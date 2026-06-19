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
  - `data/new_core_clean_papers.json` — canonical clean-paper table (2,170 main papers) with
    inclusion/exclusion reasons, source tags, and venue-year coverage diagnostics
  - `data/new_core.json` — repaired new-core/stayer/newcomer/dropout split
  - `data/new_core_researcher_profiles.json` / `.csv` — descriptive venue-count/author-role profiles for all 171 researchers
  - `data/new_core_topic_profiles.json` / `.csv` — per-researcher topic profiles from canonical clean table (all 171)
  - `data/paper_topic_labels_v2.json` — per-paper topic labels from repaired data (2,170 papers)
  - `data/venue_topic_vectors_v2.json` — venue-year topic feature vectors from repaired data
  - `data/venue_topic_evolution_v2.csv` — CSV of venue-year topic shares for charting

Current repaired count snapshot from `scripts/fetch_pacmnet_tocs.py` plus
`scripts/build_new_core.py`:
- **new-core**: 115 researchers
- **stayers**: 43 researchers also in core-99
- **newcomers**: 72 researchers not in core-99
- **dropouts**: 56 core-99 researchers below the new-core threshold
- **complete newcomers outside broad cohort**: 9

Key corrected findings (replacing old exploratory numbers from incomplete data):
- **Stay AI infra share**: 7.5% (+7.0pp delta) at qualifying venues
- **Newcomer current top-venue mix**: 8.9% AI infra and 23.6% classical networking; deltas are baseline-fragile because 52/72 newcomers have fewer than 5 baseline qualifying papers
- **Dropout AI infra share**: 2.4% (+1.8pp delta)
- **AI infra at NSDI**: 1-4% (2018-2022) → 6-11% (2023-2026)
- **AI infra at SIGCOMM**: 0-2% (2018-2022) → 10-11% (2024-2025)
- **Who writes AI-infra papers**: 55% involve stayers, 39% involve newcomers, 34% involve researchers outside both groups
- **Newcomers are NOT simply "AI researchers invading networking"** — their current qualifying-venue portfolios contain substantial classical networking as well as AI infra

Important caveat remains: 2026 venue coverage is observed-as-available rather
than complete (only NSDI 2026 present). Topic classification is keyword-based with 34.5% "Other" rate.

Old exploratory artifacts retained for comparison:
  - `data/post_gpt_core.json`
  - `data/post_gpt_venue_papers.json`
  - `data/paper_topic_labels.json` (v1)
  - `data/venue_topic_vectors.json` (v1)
  - `data/researcher_topic_profiles.json` (v1)

### 7. Project Plan And Status

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
| `scripts/build_new_core_profiles.py` | Build descriptive venue-count/author-role profiles for all 171 new-core split researchers |
| `scripts/build_new_core_topic_profiles.py` | 🆕 Build researcher topic profiles from canonical clean paper table (active) |
| `scripts/classify_paper_topics.py` | 🆕 Keyword-based paper topic classifier v2 — reads from new_core_clean_papers.json |
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

- refine paper topic classification with LLM (keyword classifier has 34.5% "Other" rate; v2 data on repaired clean paper table ready as input),
- run formal clustering of researcher topic profiles (PCA + k-means on `data/new_core_topic_profiles.json`),
- run regression-to-the-mean check with 2013-2017 comparison cohort (`build_comparison_cohort.py`),
- add career-stage proxy and author-role analysis for newcomers (author-role data in `new_core_researcher_profiles.json`),
- strengthen geo and especially sector labels,
- build comparison groups beyond the core-99 (near-core sample, broad cohort),
- audit abstract coverage before LLM-based topic classification,
- build conference evolution charts (stacked area plots from `data/venue_topic_evolution_v2.csv`),
- refine topic taxonomy: split `classical_networking` into routing/control, congestion/transport, SDN/NFV, etc. per ANALYSIS_PLAN.md Repair Principle 5.

Completed June 2026:

- ✅ New-core data foundation repaired (115 researchers, 43/72/56 split, canonical clean paper table)
- ✅ PACMNET TOC integration for CoNEXT 2023-2025 long-paper evidence
- ✅ Topic classification rebuilt on repaired clean paper table (v2: 2,170 papers)
- ✅ Researcher topic profiles rebuilt for all 171 stayers/newcomers/dropouts (including 9 DBLP-only complete newcomers)
- ✅ Conference-level topic evolution re-quantified (NSDI: 1-4% → 6-11% AI infra; SIGCOMM: 0-2% → 10-11%)
- ✅ AI-infra authorship re-analyzed (55% involve stayers, 39% involve newcomers, 31% cross-generational collaboration)
- ✅ Newcomer mixed current-portfolio pattern identified (substantial classical networking and AI infra in post-2023 qualifying venues; longitudinal deltas are baseline-fragile)
- ✅ CORE99_ANALYSIS.md §11 updated with repaired counts and corrected findings
- ✅ Documentation consistency restored (README.md, ANALYSIS_PLAN.md, CORE99_ANALYSIS.md)

Old exploratory outputs (deprecated but retained for comparison):
  - `data/post_gpt_core.json` (113/40/73/59)
  - `data/paper_topic_labels.json`, `venue_topic_vectors.json`, `venue_topic_evolution.csv` (v1)
  - `data/researcher_topic_profiles.json`, `data/post_gpt_core_profiles.csv` (v1)
