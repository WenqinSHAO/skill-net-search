# Analysis Plan

This document is the project planning surface for the next phase. The project
has moved beyond the initial narrow question of "did top networking researchers
migrate to AI?" The broader empirical goal is now:

> Understand how top-tier networking research activity is changing, and how
> old and current leading researchers are positioned within that change.

The plan below intentionally separates the data apparatus, venue background
analysis, researcher cohort analysis, and migration/directional-change analysis.
This should reduce hidden bias from premature trajectory labels, fragile
quadrants, or topic categories that are too coarse for a networking audience.

## Current Status Snapshot

### Stable Cohort Definitions

- **Broad baseline cohort**: all researchers with at least one paper in
  SIGCOMM, NSDI, CoNEXT, HotNets, or IMC during 2018-2022.
- **core-99**: researchers with at least 7 clean qualifying top-networking
  papers during 2018-2022.
- **new-core**: researchers with at least 7 clean qualifying top-networking
  papers during the observed 2023-2026 window.
- **Qualifying top-networking venues**: SIGCOMM, NSDI, CoNEXT, HotNets, IMC.
  CoNEXT 2023 onward uses PACMNET long-paper evidence where appropriate.

### Completed Data Foundation

- Per-venue/per-year paper counts for 2018-2022 were checked; CoNEXT 2022's
  28-paper count was manually confirmed from the official program.
- Researcher itineraries exist for the broad baseline cohort.
- `data/venue_family_map.json` is the source of truth for broad venue-family
  normalization.
- `data/core99_researcher_attributes.json` / `.csv` contain deterministic
  core-99 researcher attributes, including author-position summaries.
- `data/new_core_clean_papers.json` is the repaired canonical clean-paper table
  for new-core work.
- `data/new_core.json` contains the repaired new-core split:
  - new-core: 115
  - stayers: 43
  - newcomers: 72
  - dropouts: 56
  - complete newcomers outside the broad baseline cohort: 9
- `data/paper_topic_labels_v2.json`, `data/venue_topic_vectors_v2.json`, and
  `data/venue_topic_evolution_v2.csv` contain the first keyword-based
  top-networking paper-topic vectors.
- `data/new_core_topic_profiles.json` / `.csv` contain topic profiles for all
  171 stayers/newcomers/dropouts.

### Important Caveats That Remain

- 2026 is observed-as-available and incomplete.
- Current paper-topic labels are keyword-based; the "Other" rate is high enough
  that the taxonomy should be treated as a first pass, not a final ontology.
- `classical_networking` is too broad for the next phase. A networking audience
  needs finer categories such as routing, congestion/transport, measurement,
  datacenter/WAN, wireless/mobile, security, verification, programmable
  dataplanes, video/QoE, and AI infrastructure.
- Region/sector labels are context labels, not causal explanations. Coverage
  and confidence need explicit tracking.
- Quadrant definitions based on rate-ratio thresholds are now deprecated as a
  primary narrative device. They may remain as diagnostic artifacts.

## Re-Oriented Analysis Structure

The analysis should proceed in this order:

1. **Part I: Data Apparatus And Feature Spaces**
   Define the paper scope, venue scope, feature vectors, count features, and
   topic taxonomy. This is the methodological foundation.

2. **Part II: Venue Evolution Before Researcher Evolution**
   Analyze how top networking venues changed by year and venue. This provides
   the background drift against which researcher trajectories should be read.

3. **Part III: Researcher Cohorts And Profiles**
   Analyze core-99, new-core, stayers, newcomers, and dropouts using the same
   feature definitions. Keep "who", "what", and "how" separate.

4. **Part IV: Directional Movement / Migration**
   Treat migration as one downstream analysis, not the frame for the entire
   project. Include both moving-out and moving-in views.

5. **Part V: Synthesis And Open Questions**
   Separate data-supported observations, evidence-based interpretations, and
   unresolved questions.

## Part I: Data Apparatus And Feature Spaces

Part I should be completed before adding more interpretive narrative. Its job
is to make all later analyses comparable and auditable.

### I.1 Paper Scope

Define each paper universe explicitly:

- **Qualifying top-networking papers**: clean main papers at SIGCOMM, NSDI,
  CoNEXT, HotNets, and IMC.
- **Broad clean conference papers**: deduplicated conference papers used for
  venue-family portfolio analysis.
- **Networking-related papers**: papers in networking venues or system papers
  whose title/abstract indicates a networking problem.
- **Excluded records**: posters, demos, proceedings-volume records, workshops,
  editorials, keynotes, and other non-main-paper records.

Required outputs:

- A short scope table in `README.md`.
- A machine-readable scope manifest, likely
  `data/analysis_scope_manifest.json`.
- A check script or report that counts included/excluded records by source,
  venue, and year.

### I.2 Venue Scope And Venue-Year Background

Venue analysis should precede researcher analysis. For each qualifying venue
and year, compute:

- total clean paper count,
- author count and repeat-author concentration,
- topic vector over the fine networking taxonomy,
- old-core/new-core/stayer/newcomer/dropout authorship incidence,
- coverage status, especially for 2026.

This gives the "inflation baseline": a researcher-level change should be read
relative to what the venue itself is doing.

Required outputs:

- `data/venue_year_background.json`
- `data/venue_year_background.csv`
- venue-year figures for paper counts, topic shares, and author concentration

### I.3 Broad Researcher Profile Vector

This vector describes the researcher's overall venue-family composition. It is
useful for broad cross-domain movement, not for fine networking-topic claims.

Candidate dimensions:

- qualifying_top_networking,
- other_networking,
- systems,
- AI_ML,
- security_privacy,
- data_management,
- hardware_architecture,
- mobile_wireless,
- HCI,
- theory,
- unknown.

For each researcher and period compute:

- baseline vector: 2018-2022 normalized shares,
- post vector: observed 2023-2026 normalized shares,
- delta vector: post minus baseline,
- absolute counts by dimension,
- evidence sufficiency flags.

Important rule: keep composition vectors separate from absolute volume. A
researcher can have a large compositional change with small absolute volume, or
a stable composition with large absolute growth.

### I.4 Volume And Authorship Feature Set

Volume and role features should not be hidden inside composition vectors.

Core features:

- total clean paper count by period,
- qualifying top-networking paper count by period,
- broad clean conference paper count by period,
- active years by period,
- first-author, middle-author, last-author, and single-author counts/shares,
- average author-list size,
- coauthor overlap and repeated-collaboration counts.

These features answer "how much activity and what role", not "what topic".

### I.5 Fine Networking-Topic Vector

This is the largest missing apparatus piece. It should classify networking
research topics at a granularity meaningful to networking researchers.

Initial taxonomy candidates:

- routing/control plane,
- congestion/transport,
- datacenter/WAN/cloud networking,
- measurement/telemetry,
- wireless/mobile/IoT/sensing,
- security/privacy/censorship,
- verification/formal methods/configuration,
- programmable dataplanes/SmartNIC/RDMA,
- video/QoE/streaming/content delivery,
- networked systems and distributed infrastructure,
- AI infrastructure / systems for ML,
- ML for networking,
- other/uncertain.

Design principles:

- Prefer multi-label topic vectors over single hard labels.
- Keep `other/uncertain` explicit rather than forcing classification.
- Use title-only labels only when abstracts are unavailable, and expose that
  evidence mode.
- Evaluate the taxonomy by inspecting representative papers per class and
  venue-year distributions.

Required outputs:

- `data/network_topic_taxonomy.json`
- `data/network_paper_topic_labels.json`
- `data/researcher_network_topic_vectors.json`
- `data/venue_network_topic_vectors.json`
- an audit report with examples, uncertain cases, and confusion risks

### I.6 Evidence Quality Flags

Every vector should carry enough quality metadata to prevent over-reading:

- paper count denominator,
- abstract coverage,
- 2026 coverage status,
- topic classification method,
- confidence / uncertain-topic share,
- source mixture: DBLP, PACMNET, official page, manual correction,
- author-position match confidence.

## Part II: Venue Evolution

Questions:

- How did each qualifying top-networking venue's topic mix change from
  2018-2026?
- Is 2023 a visible break point, or is the change gradual?
- Is AI infrastructure broad across venues or concentrated in SIGCOMM/NSDI?
- Are changes driven by new authors, recurring authors, or both?
- Are some venues more concentrated communities than others, such as IMC?

This part should be written before researcher trajectory claims so that
researcher changes can be interpreted relative to venue drift.

## Part III: Researcher Cohorts And Profiles

### Who

For each cohort/slice, describe who the researchers are:

- name and DBLP PID,
- institution/region/sector where available,
- career-stage proxy,
- baseline and post activity volume,
- author-role profile,
- evidence sufficiency.

Needed artifact:

- a reusable researcher-introduction template for core-99 and new-core.

### What

Use the broad profile vector and fine networking-topic vector:

- baseline profile,
- post profile,
- delta profile,
- absolute-volume companion table,
- comparison to venue background.

This replaces the current tendency to overuse quadrant labels.

### How

Analyze collaboration and authorship:

- do core people publish separate papers or clustered papers?
- are stayers and newcomers coauthoring?
- are AI-infrastructure papers concentrated in labs or broadly distributed?
- does first-author vs last-author position change the interpretation?

## Part IV: Directional Movement / Migration

Migration should be a separate downstream analysis.

It should include:

- moving-out view: where core-99 activity went after 2023,
- moving-in view: where new-core researchers were before 2023,
- directional vector changes after venue-background adjustment,
- cases of stable networking, adjacent-networking substitution, AI
  infrastructure expansion, systems broadening, broad output decline, and
  low-evidence ambiguity.

Avoid hard labels such as "AI migrant" unless the evidence is strong and the
definition is explicit.

## Deprecated Or Demoted Items

### Quadrant Taxonomies

The Inv-Q1/Q2/Q3/Q4 and sys/AI/storage quadrants were useful exploratory
scaffolds, but they should not lead the next narrative. Problems:

- `top_networking_rate_ratio` is sensitive to 2026 incompleteness and period
  denominator choices.
- Quadrants conflate volume, composition, and venue-background drift.
- Thresholds create sharp labels near arbitrary boundaries.

Keep these artifacts as diagnostics:

- `CORE99_INVESTIGATION_TABLES.md`
- `data/core99_sys_ai_storage_quadrants.csv`

But use vector + volume + venue-background-adjusted views as the main line.

### Top-100 As Method

Top-100 slices are convenience samples for inspection or LLM context, not a
substantive scoping principle. Prefer explicit thresholds, parameterized slices,
or cohort definitions tied to the analysis question.

### Narrow AI-Migration Framing

"AI migration" remains one useful entry question, but the main project now
studies top-networking research evolution. AI infrastructure is one trajectory
among several, and is often a networking/systems problem rather than core AI.

## Immediate Next Work

1. **Write the detailed Part I implementation plan for review.**
   - Define exact artifacts, schemas, and validation checks.
   - Decide what can be built from existing artifacts and what requires new
     enrichment.

2. **Refactor report/narrative structure after Part I is accepted.**
   - Venue evolution should come before researcher evolution.
   - core-99 and new-core should reuse the same feature spaces.
   - Migration should become a later section.

3. **Build the fine networking-topic taxonomy.**
   - Start with keyword/regex + manual audit.
   - Prepare for LLM classification once abstract coverage is known.

4. **Add venue-year background artifacts.**
   - Topic mix, paper count, author concentration, cohort incidence.

5. **Add volume/authorship companion views for every composition vector.**
   - Prevent percentage-only interpretations.

## Historical Completed Work Index

Primary documents:

- `README.md` — project index and artifact chain.
- `CORE99_ANALYSIS.md` — current primary narrative, including repaired
  new-core §11.
- `CORE99_INVESTIGATION.md` — detailed reference tables and diagnostics.
- `CORE99_INVESTIGATION_TABLES.md` — deterministic Q1-Q3 tables.
- `CORE99_RESEARCHER_ATTRIBUTES.md` — core-99 attribute table explanation.
- `CORE99_REPORT_zh_reader_facing.html` — Chinese reader-facing report.

Key scripts:

- `scripts/publication_scope.py`
- `scripts/build_core99_attributes.py`
- `scripts/build_core99_investigation_tables.py`
- `scripts/fetch_pacmnet_tocs.py`
- `scripts/build_new_core.py`
- `scripts/classify_paper_topics.py`
- `scripts/build_new_core_topic_profiles.py`

Key artifacts:

- `data/researcher_itineraries.json`
- `data/core99_researcher_attributes.json`
- `data/core99_investigation_summary.json`
- `data/venue_family_map.json`
- `data/new_core_clean_papers.json`
- `data/new_core.json`
- `data/paper_topic_labels_v2.json`
- `data/venue_topic_vectors_v2.json`
- `data/venue_topic_evolution_v2.csv`
- `data/new_core_topic_profiles.json`
