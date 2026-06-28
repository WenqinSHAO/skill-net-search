# I.5 Classification Review

Status: the v3.1 three-axis classifier now passes the project validation gate and the downstream v3 artifacts have been regenerated from the validated labels. This document records the repaired state and the remaining interpretation cautions.

## Current Validation Snapshot

- Classified papers: 2,236 / 2,236.
- Abstract coverage: 2,204 papers (98.6%); 32 title-only papers remain (1.4%).
- Validation blockers: 0 zero-scenario papers, 0 zero-mechanism papers, 0 classification-error rows.
- Title-only uncertainty policy: 0 title-only rows are marked not uncertain.
- Unknown labels remain visible as evidence-quality mass: 459 `unknown_scenario`, 208 `unknown_mechanism`.
- Uncertain labels: 825 papers (36.9%).
- Regenerated artifacts: `data/paper_topic_labels_v3.json`, `data/venue_topic_vectors_v3.json`, `data/venue_topic_evolution_v3.csv`, `data/new_core_topic_profiles.json`.

## Repaired Data Issues

1. **NSDI abstract coverage.** `fetch_paper_abstracts.py` now supports both USENIX paper pages and inline technical-session paper blocks. This fixes the NSDI 2023 page shape. NSDI 2023 now has 96 / 96 official USENIX abstracts matched, with 0 title-only rows.
2. **Unsafe title matches.** OpenAlex/Semantic Scholar title matching requires exact normalized title or high forward title overlap. Rejected title matches are quarantined in `data/abstract_title_match_quarantine.json`.
3. **Retry semantics.** `classify_paper_topics_v3.py` now retries prior `classification_error` rows and rows whose abstract availability changes. It records an `abstract_hash` so future changed abstracts can invalidate stale labels.
4. **Title-only uncertainty.** Title-only rows are deterministically marked uncertain on save.
5. **Validation gate.** `validate_classification_v3.py` writes `data/classification_v3_validation_report.json`; `regenerate_v2_artifacts.py` refuses to regenerate analysis artifacts unless validation passes, except with `--allow-invalid` for debugging.

## Manual Resolutions

Five rows repeatedly failed the LLM API after several retries. They were manually resolved from title+abstract evidence and written back to both `paper_topic_labels_v3.json` and `classification_progress_v3.json`:

- `Hydra: Effective Runtime Network Verification`
- `Hawkeye: Diagnosing RDMA Network Performance Anomalies with PFC Provenance`
- `Bridging Storage and Execution: A Semantic Virtual Bus for On-Demand Application Streaming`
- `Heuristic Analysis from Source Code via Symbolic-Guided Optimization`
- `eXpressSFU: Toward Super-Scalable Video Conferencing with SmartNICs`

These manual rows are conservative and evidence-backed; no `classification_error` flags remain.

## Remaining Interpretation Cautions

The v3.1 output is now usable for the first semantic venue-baseline revisit, but not all axes are equally mature.

- **Scenario and mechanism are the primary axes** for I.2 venue interpretation.
- **Method is secondary.** `systems_building` appears in 1,260 / 2,236 papers (56.4%), so it is still too broad for strong standalone claims.
- **Unknown and uncertain mass should be shown, not hidden.** Venue-year tables should include title-only share, uncertain share, unknown-label share, low-confidence share, and classification-error share.
- **2026 remains incomplete** and should be treated as observed-as-available.

## Recommended Next Use

Proceed to revisit I.2 venue baseline using `venue_topic_vectors_v3.json`, preferably with paper-normalized mechanism shares and the quality fields shown beside every venue-year row. Do not rely on the old Stage-1 keyword topic vectors for substantive topic claims.
