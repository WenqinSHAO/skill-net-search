# I.5 Classification Review

Status: the v3 three-axis classifier is a promising draft, but it is not analysis-ready.

## Executive Findings

- Classified papers: 2236 / 2236.
- Abstract coverage: 1518 papers (67.9%); 718 missing.
- Missing abstracts are overwhelmingly NSDI: {'NSDI': 699, 'IMC': 16, 'CoNEXT': 2, 'HotNets': 1}.
- Missing abstracts without DOI: 709; with DOI: 9.
- Validation blockers: 40 zero-scenario papers, 50 zero-mechanism papers, 37 classification errors.
- Uncertain labels: 1355 papers (60.6%).
- Title-only labels: 718 papers (32.1%); 84 of those are marked not uncertain.
- Suspect title-source abstract matches: 8 / 68.

## Method Review

The three-axis design is directionally better than the prior flat keyword taxonomy because it separates deployment context, networking mechanism, and method. However, the current axes are not yet clean enough for a networking-audience analysis.

Main concerns:

1. Scenario mixes deployment domain and workload. For example, `dcn_ai_training`, `dcn_cloud`, `interconnect`, `cdn`, and `internet_core` are not mutually comparable dimensions.
2. Mechanism is missing common networking categories that appear in top venues, such as packet processing/programming, naming/DNS, content/video/QoE, sensing/localization, network economics/policy/censorship, reliability/resilience, and experimentation/testbed/tooling.
3. Method labels mix technique with artifact maturity. `systems_building` becomes a broad default and is assigned to nearly half the papers, which limits interpretability.
4. The prompt instruction `when uncertain, choose the more specific label` conflicts with the project principle of not forcing labels. It likely contributes to over-specific low-confidence labels.
5. Downstream vectors normalize by assigned labels per axis, not by paper denominator plus no-label/uncertain shares. That hides missing-label and uncertainty mass.

## Abstract Coverage Diagnosis

The missing-abstract problem is mostly not random:

- NSDI: 699
- IMC: 16
- CoNEXT: 2
- HotNets: 1

Root cause in the pre-fix run: DBLP-derived NSDI records have no DOI in `new_core_clean_papers.json`, so OpenAlex DOI lookup cannot work. The fallback title search recovered only a small number of NSDI abstracts. USENIX technical-session pages provide abstracts; the repaired fetcher now uses those pages.

Secondary issue: title-based matching is too lenient. A few OpenAlex title matches use short source titles or low forward overlap, which can attach the wrong abstract.

## Label Quality Risks

- `validate_classification_v3.py` fails, so the v3 output should not be described as passed or completed.
- 37 papers are fallback `all_retries_failed` rows and should be re-run before aggregation.
- 84 title-only papers are marked not uncertain. This is too optimistic unless the title explicitly contains all assigned evidence.
- The mechanism distribution is dominated by `measurement_telemetry`; this may be plausible for IMC-heavy slices but should be checked with venue-year examples.
- `systems_building` appears too broad and should either be narrowed or treated as an evidence-quality/artifact flag rather than a method topic.

## Recommended Fix Order

1. Do not use v3 topic profiles or venue vectors for interpretation yet.
2. Add a USENIX NSDI abstract fetch path keyed by NSDI year/title.
3. Tighten title-match validation: require high forward overlap or exact normalized title match; quarantine short-title subset matches.
4. Re-run the 37 failed classifications and all papers affected by suspect abstracts.
5. Revise taxonomy before full reclassification: add missing mechanism categories; split method from artifact/evidence flags; add explicit `unknown/insufficient_evidence` handling.
6. Regenerate venue and researcher vectors with quality denominators: title-only share, no-label share, low-confidence share, and uncertainty share.


## Proposed Fix Plan

### Phase A: Repair Abstract Evidence

Goal: reduce title-only classification before changing taxonomy.

Concrete changes:

1. `fetch_paper_abstracts.py` now includes a USENIX path for NSDI:
   - fetches year pages such as `https://www.usenix.org/conference/nsdi24/technical-sessions`,
   - follows paper presentation links and parses titles/abstracts,
   - matches by normalized title against NSDI rows in `new_core_clean_papers.json`,
   - records `source: usenix_nsdi_page`, `source_url`, and title-match score.
2. Title-based matching for OpenAlex/Semantic Scholar is now tightened:
   - require exact normalized title match, or forward title overlap >= 0.75,
   - reject short source-title subset matches unless the normalized titles are exact,
   - quarantine suspect matches rather than silently using them.
3. Add/extend abstract audit output after rerun:
   - abstract coverage by venue/year,
   - missing-with-DOI vs missing-without-DOI,
   - suspect title matches,
   - source distribution.

Acceptance criteria:

- NSDI missing abstracts should drop sharply; if USENIX pages are parseable, target >90% NSDI abstract coverage.
- Suspect title-source matches should be zero or explicitly quarantined.
- `paper_abstracts.json` should distinguish true missing abstracts from rejected unsafe matches.

### Phase B: Repair Taxonomy And Prompt

Goal: preserve the three-axis idea while making labels meaningful to networking researchers.

Concrete changes:

1. Taxonomy v3.1 keeps the three high-level axes, but refines their semantics:
   - **scenario** = deployment/domain context only,
   - **mechanism** = networking problem/function,
   - **method** = technical approach only,
   - move artifact maturity such as `systems_building` into a separate evidence/artifact flag or make it much narrower.
2. Taxonomy v3.1 adds missing mechanism categories before reclassification:
   - packet processing / network programming,
   - DNS / naming / resolution,
   - video / QoE / streaming,
   - sensing / localization / RF,
   - censorship / policy / economics,
   - reliability / resilience / fault tolerance,
   - testbed / experimentation / tooling.
3. Taxonomy v3.1 adds explicit insufficient-evidence handling:
   - `unknown_scenario` or no scenario with reason,
   - `unknown_mechanism` or no mechanism with reason,
   - no forced labels when title/abstract does not support a category.
4. `classify_paper_topics_v3.py` prompt language has been updated:
   - removes “when uncertain, choose the more specific label,”
   - require title-only classifications to be uncertain unless evidence is explicit in the title,
   - require each evidence phrase to quote or paraphrase actual title/abstract text.

Acceptance criteria:

- `validate_classification_v3.py` passes, or the validator is deliberately revised to allow explicit `unknown_*` labels.
- Zero-label papers are explained by explicit insufficient-evidence labels rather than silent empty axes.
- `systems_building` no longer dominates method labels by default.

### Phase C: Reclassify And Validate

Goal: produce analysis-ready paper labels.

Concrete changes:

1. Re-run only affected papers first:
   - the 37 `all_retries_failed` rows,
   - suspect title-abstract matches,
   - all papers whose abstract changed after USENIX fetch.
2. Run full reclassification only after taxonomy/prompt is accepted.
3. `validate_classification_v3.py` now includes stricter quality gates:
   - validation pass/fail,
   - title-only share,
   - low-confidence share per axis,
   - uncertain share,
   - zero/unknown label share,
   - distribution by venue/year.

Acceptance criteria:

- No retry-failure fallback rows in final labels.
- Validation report passes.
- Quality metrics are saved as data artifacts and linked from README.

### Phase D: Regenerate Vectors With Quality Denominators

Goal: make venue/researcher topic vectors interpretable without hiding uncertainty.

Concrete changes:

1. `regenerate_v2_artifacts.py` should be run only after validation passes.
2. It now emits paper-normalized topic shares as well as assigned-label-normalized shares.
3. It now attaches quality fields to every vector:
   - paper count,
   - abstract coverage,
   - title-only share,
   - low-confidence share,
   - uncertain share,
   - unknown/no-label share.

Acceptance criteria:

- `venue_topic_vectors_v3.json`, `venue_topic_evolution_v3.csv`, and `new_core_topic_profiles.json` are regenerated after validation passes.
- Reports distinguish observed topic movement from evidence-quality movement.

## Handoff For Rerun Agent

A less capable agent can run the repaired pipeline, but should not change taxonomy, prompt, or interpretation logic. Safe sequence:

1. Run `python3 projects/networking-to-ai-migration/scripts/fetch_paper_abstracts.py`.
2. Run `python3 projects/networking-to-ai-migration/scripts/audit_classification_v3_quality.py` and inspect abstract coverage plus `data/abstract_title_match_quarantine.json`.
3. If abstract coverage and quarantine look acceptable, run `python3 projects/networking-to-ai-migration/scripts/classify_paper_topics_v3.py`. The script will ignore stale v3.0 progress because taxonomy is now v3.1.
4. Run `python3 projects/networking-to-ai-migration/scripts/validate_classification_v3.py`. Stop if it fails.
5. Only if validation passes, run `python3 projects/networking-to-ai-migration/scripts/regenerate_v2_artifacts.py`.

Do not write analysis narrative from v3 artifacts until validation passes and quality denominators are reviewed.

## Example Suspect Abstract Matches

| Year | Venue | Paper title | Source title | Forward overlap |
|---:|---|---|---|---:|
| 2018 | IMC | Three Bits Suffice: Explicit Support for Passive Measurement of Internet Latency in QUIC and TCP | Pluginizing QUIC | 0.067 |
| 2018 | IMC | LDplayer: DNS Experimentation at Scale | LDplayer | 0.2 |
| 2018 | IMC | 403 Forbidden: A Global View of CDN Geoblocking | 403 Forbidden | 0.25 |
| 2018 | IMC | Coming of Age: A Longitudinal Study of TLS Deployment | Coming of Age | 0.375 |
| 2018 | IMC | In the IP of the Beholder: Strategies for Active IPv6 Topology Discovery | In the IP of the Beholder | 0.455 |
| 2018 | IMC | Pushing the Boundaries with bdrmapIT: Mapping Router Ownership at Internet Scale | Pushing the Boundaries with bdrmapIT | 0.455 |
| 2018 | IMC | A Long Way to the Top: Significance, Structure, and Stability of Internet Top Lists | A Long Way to the Top | 0.462 |
| 2018 | IMC | Characterizing the Internet Host Population Using Deep Learning: A Universal and Lightweight Numerical Embedding | Characterizing the Internet Host Population Using Deep Learning | 0.571 |

## Example Zero-Mechanism Papers

| Year | Venue | Title | Evidence mode | Error |
|---:|---|---|---|---|
| 2018 | HotNets | Gearing up for the 21st century space race | title_and_abstract |  |
| 2018 | HotNets | Learning Food Quality and Safety from Wireless Stickers | title_and_abstract |  |
| 2018 | SIGCOMM | p4v: practical verification for programmable data planes | title_and_abstract | all_retries_failed |
| 2019 | HotNets | Autogenerating Fast Packet-Processing Code Using Program Synthesis | title_and_abstract | all_retries_failed |
| 2019 | HotNets | Do Switches Dream of Machine Learning?: Toward In-Network Classification | title_and_abstract | all_retries_failed |
| 2019 | HotNets | Event-Driven Packet Processing | title_and_abstract | all_retries_failed |
| 2019 | HotNets | Robustifying Network Protocols with Adversarial Examples | title_and_abstract | all_retries_failed |
| 2019 | IMC | ECON: Modeling the network to improve application performance | title_and_abstract | all_retries_failed |
| 2019 | NSDI | Towards Programming the Radio Environment with Large Arrays of Inexpensive Antennas | title_only |  |
| 2020 | CoNEXT | A modular compiler for network programming languages | title_and_abstract | all_retries_failed |
