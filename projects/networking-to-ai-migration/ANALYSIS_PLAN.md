# Analysis Plan

This document is a working plan for the next phase. The emphasis is to make the
data foundation solid and auditable first, so later analysis is less likely to
inherit a hidden bias from premature categories, thresholds, or hypotheses.

The plan intentionally separates:

1. **Immediate TODOs**: concrete data checks and artifact improvements.
2. **Near-term descriptive analyses**: neutral summaries that reveal cohort
   shape and data problems.
3. **Later interpretive analyses**: trajectory discovery, conference trend
   discovery, and researcher-field alignment.
4. **Speculative brainstorming**: possible future-looking questions, clearly
   separated from fact-grounded analysis.

## Current Data Foundation

We now have:

1. **Researcher cohort**
   - Rule: at least one paper in SIGCOMM, NSDI, CoNEXT, HotNets, or IMC during
     2018-2022.
   - Current cohort size: 3,571 researchers.

2. **Researcher itineraries**
   - Full clean conference-publication histories for the cohort from 2018-2026.
   - Primary artifact: `data/researcher_itineraries.json`.
   - Discovery subset artifact: `data/top100_itineraries.json`.

The current itinerary file is complete for the defined cohort, but several
fields are still weak or missing:

- abstracts are mostly absent,
- geo/sector labels are incomplete,
- author-role information is now exposed in regenerated itinerary records, but still needs review as a proxy,
- venue families beyond the five qualifying networking venues are not yet
  systematically normalized,
- recent 2023-2026 conference completeness still needs official-page checks.

## Guiding Principle

Do not start from rigid migration labels.

The first task is to organize observable evidence:

- who is in the cohort,
- how strongly each researcher is anchored in the five qualifying networking
  venues,
- what each researcher published year by year,
- what each top networking conference published year by year,
- where the data is incomplete or ambiguous.

Only after that should we derive labels such as trajectory archetypes.

## Immediate TODOs

These are the next concrete implementation tasks.

### TODO 1. Produce Cohort Shape Tables

Create a descriptive artifact, for example
`data/cohort_shape_summary.json` and a readable Markdown/CSV export.

Include:

- distribution of `baseline_top_networking_count`,
- distribution of total clean publication count,
- distribution of clean baseline publication count,
- distribution of clean post-2023 publication count,
- cross-tab of baseline top-networking count versus total clean publication
  count,
- counts by qualifying venue combination.

Important: do not define "core networking researcher" yet. Use these tables to
decide whether any threshold such as `>=3`, `>=5`, or top-k is defensible.
Any threshold should first be represented as a derived slice, not as a rewrite
of the raw cohort.

Current discussion flags from the first cohort-shape run:

- `total clean publications == 1` is a proposed sparse-evidence exclusion for
  trajectory analysis, but the researchers remain in the raw cohort and derived
  CSVs.
- `baseline_top_networking_count > 6` is a provisional candidate core slice for
  inspection. It contains 99 researchers and 5 researchers with total clean
  publications `>100`, so the high-volume profiles are few enough for manual
  review but still not automatically safe.

A derived selected-sample packet now exists for this provisional slice:

- `data/selected_sample_network_gt6_packet.json` contains the full title-level
  evidence grouped by researcher and year.
- `data/selected_sample_network_gt6_summary.csv` contains one compact row per
  researcher.
- `SELECTED_SAMPLE_NETWORK_GT6.md` is a readable review packet.

The packet is title-based only. Before using it for substantive trajectory
claims, venue aliases and noisy title vocabulary should be normalized further.

### TODO 2. Build Core-99 Researcher Attribute Table

For the provisional selected sample `baseline_top_networking_count > 6`, create
one auditable row per researcher. This is the next immediate implementation
step.

Output target:

- `data/core99_researcher_attributes.csv`
- `data/core99_researcher_attributes.json`

Start with observable or directly derived attributes, not migration labels:

- baseline top-networking count,
- post-2023 top-networking count,
- top-networking count by year,
- top-networking trend after baseline: increasing / decreasing / flat /
  inactive,
- baseline clean publication count,
- post-2023 clean publication count,
- total clean publication count,
- active years in baseline and post-2023,
- qualifying venue mix: SIGCOMM-heavy, NSDI-heavy, IMC-heavy, CoNEXT-heavy,
  HotNets-heavy, or mixed,
- venue portfolio by period,
- venue-family portfolio by period once TODO 4 exists,
- publication-volume change from baseline to post-2023.

Treat these as descriptive attributes. They should help us inspect the core-99
sample without yet deciding who "migrated".

Current artifacts:

- `data/core99_researcher_attributes.json`
- `data/core99_researcher_attributes.csv`
- `CORE99_RESEARCHER_ATTRIBUTES.md`

The first build includes selection-vs-clean baseline count checks,
top-networking count trends, activity patterns, qualifying venue mix, and
author-role summaries where author positions are available.

### TODO 3. Add Author-Role Fields To Itineraries

DBLP publication histories include ordered author lists. The itinerary artifact
should expose the scoped researcher's role per paper:

- author position,
- author count,
- first-author flag,
- last-author flag,
- single-author flag,
- whether the paper is one of the qualifying baseline top-networking papers,
- whether the paper is a post-2023 top-networking paper.

Then derive per-researcher period summaries:

- first-author count/share in baseline,
- last-author count/share in baseline,
- middle-author count/share in baseline,
- first-author count/share post-2023,
- last-author count/share post-2023,
- author-role profile: mostly lead, mostly senior, mixed, mostly collaborator.

This helps distinguish possible students, PIs, middle-author collaborators, and
one-off contributors. It is still only a proxy and should be caveated.

Current status: the itinerary builder now enriches clean paper records with
ordered authors, author count, scoped-author position, first/last/single-author
flags, and author-match confidence. Core-99 attributes already summarize these
fields by baseline and post-2023 periods.

The core-99 author-position audit now has zero unresolved rows after excluding
proceedings-volume records and adding conservative aliases for known name
variants.

### TODO 4. Normalize Venue Families Without Topic Claims

Create a venue-family map that is factual and conservative. This is a
prerequisite for interpreting venue broadening in the core-99 sample.

Examples:

- qualifying_top_networking,
- other_networking,
- systems,
- security_privacy,
- AI_ML,
- data_management,
- hardware_architecture,
- mobile_wireless,
- HCI,
- theory,
- unknown.

This is not a topic trajectory label. It is a venue-context label that helps
structure itineraries and identify venue-portfolio changes.

The map should be manual, inspectable, and allowed to contain `unknown`. Venue
aliases must be normalized before counting, for example `IMC` and `Internet
Measurement Conference` should not silently appear as separate venues.

Current investigation use cases for TODO 4:

1. For researchers whose top-networking rate decreases while all-clean
   publication rate is flat or increasing, identify whether their post-2023
   output moves to adjacent networking, systems, AI/ML, security/privacy,
   mobile/wireless, HCI, data management, or unknown venues.
2. For researchers whose top-networking rate is flat or increasing, summarize
   their venue-family profile, authorship placement profile, and available
   region/sector labels.
3. Quantify whether the five qualifying venues differ in author concentration,
   especially whether IMC is more concentrated than SIGCOMM/NSDI/CoNEXT/HotNets.

Outputs should be deterministic tables first; LLM itinerary interpretation is
explicitly postponed until these descriptive tables are reviewed.

### TODO 5. Core-99 Investigation Tables For Questions 1-3 ✅ COMPLETE

Deterministic investigation tables have been generated for Q1-Q3.

Q1 (top-net decrease, overall flat/increase): 15 researchers. Their post-2023
output shifts partly to adjacent networking venues (TMA, PAM, ANRW), partly to
systems venues, and partly to `unknown` venue-family venues (needs inspection).

Q2 (top-net flat/increase): 44 researchers. US-dominant (23/44), mostly
collaborator roles, mixed venue profiles.

Q3 (author concentration): IMC has highest repeat-author share (24%) and Gini
(0.31). Core-99 accounts for 52% of IMC papers. SIGCOMM and NSDI are less
concentrated.

Full tables in `CORE99_INVESTIGATION_TABLES.md` and `CORE99_INVESTIGATION.md`.

### TODO 5b. Core-99 Quadrant Analysis ✅ COMPLETE

60 of 99 core-99 researchers publish in top-tier systems (OSDI/SOSP/EuroSys/
ATC/ASPLOS/SoCC/MLSys), AI (ICML/ICLR/NeurIPS/AAAI/AISTATS/CVPR/ICCV/ECCV),
and storage (FAST) venues. Split into four quadrants by two axes:

- Q1 (net+ overall+): 30 researchers — strong all-around
- Q2 (net- overall+): 8 researchers — portfolio shift candidates
- Q3 (net+ overall-): 4 researchers — concentrating on networking
- Q4 (net- overall-): 18 researchers — broad decline

Data: `data/core99_sys_ai_storage_quadrants.csv`.
Analysis: `CORE99_INVESTIGATION.md#quadrant-analysis`.

### TODO 6. Core-99 Baseline/Post-2023 Topic Discovery Packet

Build a topic-discovery packet for the core-99 sample. The goal is to discover
research nature clusters from evidence, not to impose fixed labels.

Output target:

- `data/core99_topic_discovery_packet.json`
- `CORE99_TOPIC_DISCOVERY.md`

Paper-level evidence should be grouped by period:

- baseline: 2018-2022,
- post-2023: 2023-2026.

For each paper include:

- title,
- abstract if available,
- venue and normalized venue family,
- year,
- author-role flags for the scoped researcher,
- whether it is a qualifying top-networking paper.

Discovery procedure:

1. Build paper-level text features from baseline titles/abstracts.
2. Cluster or LLM-summarize papers into tentative nature clusters.
3. Name clusters manually from representative titles.
4. Repeat for post-2023 papers.
5. Represent each researcher as a distribution over clusters by period.

Candidate cluster names may include routing/control, measurement, programmable
networks, cloud/datacenter, wireless/IoT, video/streaming, security/privacy,
ML-for-networking, AI/LLM systems, and pure AI/ML. These names are hypotheses
to validate, not fixed ontology at the start.

### TODO 7. Core-99 Researcher Characterization Table

After TODO 2-5 exist, derive auditable researcher-level characterizations for
core-99.

Possible fields:

- baseline primary nature cluster,
- baseline secondary nature clusters,
- post-2023 primary nature cluster,
- post-2023 secondary nature clusters,
- cluster distribution delta,
- continued top-networking presence,
- venue-family broadening,
- AI/ML presence during baseline,
- AI/ML or LLM-systems presence post-2023,
- confidence / evidence sufficiency.

Avoid single hard labels like "AI migrant" at this stage. Prefer profile and
delta fields such as `baseline_profile`, `post2023_profile`, and
`profile_delta`.

### TODO 8. Track Abstract Availability Explicitly

Because abstracts may be missing unevenly, every paper and every itinerary
packet should expose:

- `has_abstract`,
- abstract source,
- abstract coverage by researcher,
- abstract coverage by venue-year.

LLM summaries should be told when they are title-only. Do not mix title-only and
title-plus-abstract cases silently.

### TODO 9. Build Outlier / Data-Quality Tables

Use data-driven cutoffs from TODO 1 rather than hard-coded definitions.

Candidate outlier views:

- low baseline top-networking count plus high total clean publication count,
- very high DBLP publication count,
- very high excluded-record count,
- suspicious generic names or DBLP names that look non-personal,
- researchers whose clean itinerary is too sparse for interpretation,
- researchers with missing or weak geo/sector data.

These tables support manual review before broad-cohort interpretation. For the
core-99 slice, the five high-total `>100` researchers have been manually
confirmed as legitimate networking researchers and should remain included.

### TODO 10. Replace Fixed Top-100 Assumption With Parameterized Slices

The current `top100_itineraries.json` is useful as a temporary discovery file,
but "top 100" should not be treated as a methodological commitment.

Create parameterized slices:

- top `N` by baseline top-networking count,
- top `N` by total clean publication count,
- top `N` by post-2023 clean publication count,
- researchers above candidate baseline-count thresholds.

Recommended initial `N` values for exploration:

- 50,
- 100,
- 200.

These are convenience slices for review and LLM context management, not claims
about who is "top" in a substantive sense.

### TODO 11. Build Top-List Overlap Tables

Compare overlap among parameterized slices.

At minimum:

- baseline-networking-count rank versus total-clean-publication rank,
- baseline-networking-count rank versus post-2023-clean-publication rank,
- total-clean-publication rank versus post-2023-clean-publication rank.

Outputs should include:

- overlap counts,
- Jaccard overlap,
- names unique to each list,
- researchers with low baseline networking count but very high total
  publication count.

This directly addresses the concern that some researchers have only one
qualifying networking paper but hundreds of total publications.

### TODO 12. Construct Comparison Groups After Core-99 Stabilizes

After the core-99 preprocessing and labels are reviewed, construct comparison
groups to test whether observed patterns are specific to the high-signal core or
appear more broadly. Candidate comparison groups:

- inclusive networking sample: all researchers with `baseline_top_networking_count >= 1`
  after sparse-evidence filtering,
- near-core sample: researchers just below the core threshold, for example
  `3 <= baseline_top_networking_count <= 6`,
- complementary sample: broad cohort excluding core-99,
- alternative scoping sample: researchers with repeated top-networking activity
  plus post-2023 publication activity,
- high-total low-networking sample: possible broad systems/AI researchers who
  touched networking once.

The comparison groups should reuse the same preprocessing pipeline: clean count
attributes, top-networking trends, author-role summaries, venue-family counts,
and topic-discovery profiles. Do not compare groups until the core-99 attribute
definitions are stable.

### TODO 13. Clarify Geo And Sector Feasibility

Geo and sector should be treated as optional first-order context labels, not as
required for early itinerary analysis.

Need to decide:

- whether region is based on current/last-known affiliation only,
- whether any affiliation history is available or feasible,
- whether sector labels are reliable enough to use,
- what confidence levels to attach.

If no reliable source exists for sector, keep `sector = Unknown` rather than
forcing a label.

### TODO 14. Build Conference Itineraries

Create venue-year itinerary artifacts for the five qualifying top networking
venues:

- SIGCOMM,
- NSDI,
- CoNEXT,
- HotNets,
- IMC.

Each venue-year should include:

- paper title,
- authors,
- abstract if available,
- source URL,
- whether the record came from DBLP or official conference pages.

Start with 2018-2022, where venue-year paper counts have been checked. Then
extend to 2023-2026 with official-page validation.

### TODO 15. Do Not Regenerate Narrative Conclusions Yet

Do not update `REPORT.md` as a substantive findings report until:

- core-99 attribute tables exist,
- author-role fields are added,
- venue-family mapping is audited,
- topic-discovery clusters are reviewed,
- abstract coverage is known,
- broader-cohort validation strategy is clear,
- conference itinerary completeness is checked.

## Analytical Objects

The project should analyze three related objects.

### Researchers

Neutral questions:

- Who entered the cohort?
- How strongly are they anchored in the qualifying networking venues?
- What did they publish year by year?
- How broad is their venue portfolio?
- How much evidence is available for each researcher?

Avoid deciding upfront whether a researcher is a "stayer", "migrant", or
"AI embracer".

### Conferences

Neutral questions:

- How did each qualifying venue's paper-title/abstract themes evolve over time?
- Which themes appear, disappear, grow, shrink, split, or merge?
- Do different venues evolve differently?
- Are changes driven by recurring authors, new entrants, or both?

Avoid hypothesis-loaded questions at this stage, such as "Did NSDI become
AI-infrastructure-heavy?" Those can be revisited later as validation questions
if a discovered pattern suggests them.

### Researcher-Field Alignment

Neutral questions:

- How do researcher itineraries compare with the venue-year itineraries?
- Are individual researchers moving differently from the conference trend?
- Are recurring authors associated with emerging venue themes?
- Are some researchers consistently present in stable themes?

The point is to distinguish possible individual movement from conference scope
change.

## Itinerary Data Model

The current itinerary structure should evolve toward a unified paper-count and
paper-evidence model rather than separate "baseline anchor" and "activity"
sections.

### Researcher Identity

Keep factual fields:

- `name`,
- `dblp_pid`,
- `affiliation`,
- `country_code`,
- `region`,
- `sector`,
- confidence/source fields for geo and sector.

Notes:

- Current DBLP data does not provide affiliation history.
- Current geo labels are last-known/current affiliation proxies from OpenAlex or
  manual carry-forward.
- Region may change over time in reality; unless affiliation history is added,
  do not interpret it as historical region.
- Sector should remain `Unknown` unless source quality is acceptable.

### Paper Counts And Venue Counts

Use a unified count structure:

```json
{
  "paper_counts": {
    "by_year": {"2018": 3, "2019": 4},
    "by_venue": {"SIGCOMM": 2, "NSDI": 1},
    "by_venue_family": {"qualifying_top_networking": 3, "systems": 2},
    "by_year_and_venue_family": {
      "2018": {"qualifying_top_networking": 2, "systems": 1}
    }
  }
}
```

Definitions:

- **Qualifying venues** means only the five cohort-defining venues:
  SIGCOMM, NSDI, CoNEXT, HotNets, IMC.
- **Qualifying papers** means papers in those five venues during 2018-2022.
- **Baseline years active** means the set/count of years from 2018-2022 in
  which the researcher had at least one qualifying paper. This differs from
  `baseline_top_networking_count`, which is the number of qualifying papers.
- **Venue distribution** means a dictionary of venue or venue-family counts,
  optionally broken down by year.

### Raw Evidence

Each itinerary should include raw paper evidence:

- title,
- venue,
- year,
- authors,
- author role,
- abstract when available,
- source URL,
- abstract/source coverage flags.

Abstracts must be handled carefully. If only some papers have abstracts, LLM or
manual reviewers must know which evidence is title-only.

### Derived Later

Do not store these as first-order labels until the evidence review supports
them:

- trajectory summary,
- trajectory archetype,
- researcher-field alignment type,
- speculative future direction,
- confidence / ambiguity notes.

## Researcher-Level Review Questions

These can be asked together in a single LLM/manual trajectory-summary call, but
the prompt should remain evidence-grounded and neutral.

For each researcher:

- What are the main recurring publication themes visible in the itinerary?
- Which themes appear continuous across years?
- Which themes appear newly introduced or reduced?
- Does publication activity change after 2023?
- Does venue-family breadth change after 2023?
- Are changes sustained across multiple years or one-off?
- Is there enough evidence to infer a trajectory?
- What are the main ambiguity or data-quality caveats?

The prompt should not ask "is this person migrating to AI?" at the discovery
stage.

## Conference-Level Review Questions

For each venue-year and venue over time:

- What themes are visible from titles/abstracts?
- Which themes recur across multiple years?
- Which themes newly appear?
- Which themes fade?
- Are changes gradual or abrupt?
- Are changes concentrated in a few authors/labs/institutions or broad across
  many authors?
- Is the evidence title-only or title-plus-abstract?

Specific hypotheses can be tested later, but initial discovery should avoid
leading labels.

## First-Order Researcher Labels

First-order labels should be factual or low-inference.

### Already Present Or Planned

- `name`,
- `dblp_pid`,
- `baseline_top_networking_count`,
- `clean_publication_count`,
- `clean_publication_count_by_year`,
- `qualifying_venues`,
- `qualifying_papers`,
- `affiliation`,
- `country_code`,
- `region`,
- `sector`.

### Candidate Low-Inference Labels

These should be computed only after the descriptive distributions are reviewed.

#### Networking Anchor Strength

Based on `baseline_top_networking_count`, but bins should be chosen after TODO
1. Possible bins may be:

- one-off,
- recurring,
- core,
- elite.

Do not hard-code these until the observed distribution is known.

#### Networking Publication Share

Baseline qualifying papers divided by all clean baseline papers.

This helps distinguish:

- networking-centered researchers,
- broad prolific researchers with some networking presence,
- one-off collaborators.

#### Career-Stage Proxy

Approximate from:

- first DBLP publication year,
- first clean conference publication year,
- first qualifying top-networking paper year.

This is useful but must be caveated.

#### Author-Role Proxy

Use author order in qualifying papers and possibly all clean papers:

- first-author share,
- last-author share,
- middle-author share,
- single-author count.

This is imperfect but may help separate junior researchers, senior PIs, and
collaborators.

#### Institution Type / Sector

Values may include:

- academia,
- industry,
- government lab,
- nonprofit,
- mixed,
- unknown.

Only use sector labels if source quality is acceptable. Otherwise, keep sector
unknown and proceed without sector analysis.

#### Mobility

Institution or sector changes over time.

This is desirable but likely later work because affiliation history is not
available from DBLP.

## Expected Data Gaps

### Abstracts

Current itineraries are mostly title/venue based. Abstract enrichment may be
needed for:

- selected researcher itinerary summaries,
- conference-year itinerary summaries,
- ambiguous or high-impact cases.

Track coverage explicitly to avoid bias from uneven abstract availability.

### Geography And Sector

Geo labels currently cover only the original core subset unless a new broad
geo-enrichment pass is run. Sector is not yet reliable.

Regional or sector analysis should wait until coverage and confidence improve.

### Author Order

DBLP has ordered author lists, but the itinerary artifact should expose the
scoped researcher's position and role flags.

### 2023-2026 Conference Completeness

DBLP may lag for recent conference years. Conference-level trend analysis should
compare DBLP against official program pages.

### DBLP Disambiguation And Common-Name Anomalies

Some researchers have one qualifying networking paper but hundreds of total
papers. These may be legitimate broad researchers, common-name disambiguation
issues, or collaboration artifacts.

Outlier tables should be reviewed before interpretation.

## Further Analysis Directions

These are directional questions for later. They should not dictate the immediate
data foundation work.

### Trajectory Discovery

After descriptive tables and itinerary packets exist:

1. Summarize researcher itineraries without predefined migration labels.
2. Compare summaries to discover candidate trajectory archetypes.
3. Validate candidate archetypes on larger slices.
4. Track uncertainty and ambiguous cases.

### Conference Trend Discovery

After conference itineraries and abstract coverage are sufficient:

1. Summarize each venue-year.
2. Compare across years within a venue.
3. Compare across venues.
4. Identify whether changes are broad field shifts, venue-specific shifts, or
   author-composition shifts.

### Researcher-Field Alignment

After researcher and conference summaries exist:

1. Compare individual itineraries with venue trends.
2. Identify researchers who appear earlier than a venue-level pattern.
3. Identify researchers whose work remains stable while venue themes change.
4. Separate individual movement from conference scope drift where possible.

### Speculative Future-Looking Work

It may be interesting later to ask:

- which researchers to watch in 2027,
- which themes may continue growing,
- what a researcher or venue might work on next.

This should be explicitly labeled as speculative and separated from
fact-grounded analysis. It should not be part of the core empirical claims.

## Practical First Analysis Batch

Status of the immediate next batch:

1. ✅ Cohort shape artifacts as broad baseline context.
2. ✅ `core99_researcher_attributes` with count, trend, venue, and activity attributes.
3. ✅ Author-role fields added to researcher itineraries; first/last/middle-author patterns summarized for core-99.
4. ✅ Venue aliases normalized; venue-family mapping built (still has `unknown` entries).
5. ✅ Deterministic core-99 investigation tables for questions Q1-Q3.
5b. ✅ Core-99 quadrant analysis (Q1-Q4) for elite sys/AI/storage venues.
6. ✅ Paper-topic classification implemented (keyword-based, 11 categories, 35% "Other" rate). LLM-based refinement still needed.
7. ✅ Researcher topic profiles built for stayers/newcomers/dropouts. Formal clustering deferred.
8. ⬜ Abstract-coverage fields — needed before LLM topic classification.
9. ⬜ Outlier/data-quality tables for broad-cohort validation.
10. ⬜ Parameterized top-k and threshold slices after core-99 attributes are stable.
11. ⬜ Comparison groups reusing the same preprocessing pipeline.
12. ✅ Conference itineraries for the five qualifying venues (2018-2026 paper data with authors fetched via DBLP TOC API; CoNEXT 2023-2025 incomplete due to PACMNET).

## Adjusted Immediate Priorities

### Priority 1: Investigate Unknown Venue Families ✅ COMPLETE

343 venue mappings and 24 aliases. Q1: 0% unknown, Q2: 2.2% unknown, core-99: 3.6% unknown. Script loads from `data/venue_family_map.json`.

### Priority 2: Q2 Researcher-Level Venue-Family Tracing ✅ COMPLETE (via PCA + delta)

Superseded by the feature vector analysis. The PCA/delta analysis covers all 87 analyzable core-99 researchers and decomposes Q2 patterns (Inv-Q2: top-net →/↑, clean →/↑) in detail. The mean Q2 delta vector shows mild other_networking shedding (−6.5pp) with AI_ML expansion (+3.7pp) and qualifying_top_networking concentration (+2.6pp).

### Priority 3: Abstract Coverage Audit

Flag which core-99 papers have abstracts vs title-only. Track coverage by researcher and by venue-year. Prerequisite for topic discovery. **Still needed** — abstract availability is unknown.

---

## Next Phase: Core-99 Deepening (June 2026)

The PCA + delta vector analysis has proven more informative and efficient than the manually crafted four-quadrant taxonomy for understanding researcher trajectories. The next phase should consolidate around this approach and extend it in three directions.

### Current State Summary

What we know from the core-99 analysis (87 analyzable researchers):

- **Dominant story**: The primary variation is networking venue composition (qualifying_top_networking vs. other_networking). 62.5% of total shift energy is in this axis.
- **Falling out (49%)**: 43 researchers (Inv-Q1 + Inv-Q4) are losing presence at the five elite qualifying venues. Two mechanisms: substitution down to adjacent venues (Inv-Q1) and proportional decline (Inv-Q4).
- **Concentrating (8%)**: 7 researchers (Inv-Q3) are increasing qualifying_top_networking share, but mostly by cutting everything else — denominator artifact, not genuine increase.
- **Stable (43%)**: 37 researchers (Inv-Q2) maintain both top-net and overall output with mild portfolio adjustments.
- **AI_ML expansion**: Concentrated in 9 individuals, not a broad trend. Half are new entrants from zero base.
- **PCA/delta resolved**: Correlation 0.88. Disagreement fully explained by family-level PCA loadings.

### Phase A: Simplify and Unify the Core-99 Analysis ✅ COMPLETE

The analysis has been consolidated into CORE99_ANALYSIS.md as the primary narrative doc, with CORE99_INVESTIGATION.md as the detailed reference. Sys/AI quadrant analysis is deprecated as a primary grouping.

### Phase B: Paper-Topic Analysis for Key Subgroups ✅ COMPLETE (keyword-based)

Paper-topic classification implemented for all 2,248 venue papers across 11 categories. Title-level inspection confirmed that AI-infra expanders are doing systems-for-ML, not core AI research. Keyword classifier has 35% "Other" rate — LLM-based refinement planned.

### Phase C: Recompute Profiles for 2023-2026 ✅ COMPLETE

Post-GPT core built: 113 researchers (40 stayers, 73 newcomers, 59 dropouts). Cross-referenced with core-99. Conference-level topic evolution quantified. Researcher topic profiles built for all three groups. See CORE99_ANALYSIS.md §11 for full findings.

### Phase D: Additional Suggestions — Partially Complete

- **D1** (raw-count sensitivity): ⬜ Deferred.
- **D2** (career-stage proxy): ⬜ Deferred.
- **D3** (conference-level topic evolution): ✅ Complete — venue-year topic vectors built, AI infra growth at NSDI (2-3% → 10-11%) and SIGCOMM (0-2% → 10%) quantified.
- **D4** (comparison groups): ⬜ Deferred.
