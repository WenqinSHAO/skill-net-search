# CLAUDE.md

## Orientation

- Read `README.md` for project scope and chaining order.
- `CORE99_ANALYSIS.md` is the primary analysis doc. `CORE99_INVESTIGATION.md` is the detailed reference.
- `ANALYSIS_PLAN.md` tracks what's done, deferred, and planned next.
- The analyzable core-99 is 87 researchers (12 excluded: post-2023 < 5 papers). Investigation groups Inv-Q1–Q4 are the consistent taxonomy.

## Behavioral Rules

### Before writing any analysis claim
1. Query the actual data artifact (JSON/CSV), compute the number, then write.
2. Never copy numbers from memory or from another doc without re-verifying.
3. If a number in a doc and a data artifact disagree, fix the doc — unless the data is provably wrong.

### Before adding a figure
1. Verify axis annotation signs against concrete researcher scores. PCA loading signs are implementation-dependent.
2. Save to `figures/` and add to the figures table in `CORE99_ANALYSIS.md`.
3. Ensure the figure's axis labels match the text interpretation in the doc.

### When modifying data
- `data/venue_family_map.json` is the single source of truth for venue→family resolution. Never hardcode venue families in scripts — load from this file.
- `scripts/publication_scope.py` defines inclusion/exclusion rules. Any change affects all downstream artifacts — re-verify before proceeding.
- After any data change, re-run `build_core99_investigation_tables.py` to regenerate CSVs and markdown.
- After regenerating data that feeds into analysis docs, re-verify all numbers cited in `CORE99_ANALYSIS.md`.

### When modifying scripts
- Scripts with progress files: maintain backward compatibility or delete the old progress file.
- If a script generates markdown output, note which files in its header comment.
- Do not re-run the full DBLP pipeline without explicit request — it's slow (~45 min) and DBLP is unreliable.

### Documentation hygiene
- `CORE99_ANALYSIS.md` is the primary narrative. When findings change, update this first, then propagate to `CORE99_INVESTIGATION.md`.
- `README.md` is the master index. Update it whenever a doc or data artifact is created, renamed, or removed.
- Avoid duplicating the same detailed information across multiple docs — prefer a primary doc with references from others.

### Common mistakes to avoid
- Overloading quadrant labels. The sys/AI/storage quadrants (Q1_net+_overall+, etc.) are a DIFFERENT taxonomy from investigation groups (Inv-Q1 through Inv-Q4). Never mix them without explicit disambiguation.
- Treating "percentage-point increase in qualifying_top_networking share" as "publishing more at elite venues." Inv-Q3's concentration is partly a denominator artifact — verify with raw counts before claiming increase.
- Using the term "migration" or "AI migrant" without specifying what kind (AI infrastructure vs. core AI/ML research). The venue-family analysis only tells WHERE, not WHAT.
- Assuming core-99 is monolithic. Baseline PCA shows a continuous spectrum from "elite-concentrated" to "broad-networking" — these two types start from different places and their trajectories mean different things.
