# Cohort Shape Summary

This is a descriptive data-foundation summary, not an interpretation of migration or trajectory.

## Cohort

- Researchers: 3571
- Cohort rule: >=1 qualifying top-networking paper in 2018-2022
- Baseline means 2018-2022.
- Post-2023 means 2023-2026.
- Total means 2018-2026.
- Clean publications are in-scope conference/workshop records after excluding journals, CoRR/arXiv, proceedings volumes, and other out-of-scope DBLP record types.

## Baseline Top-Networking Count Distribution

| Count | Researchers |
|---:|---:|
| 1 | 2520 |
| 2 | 558 |
| 3 | 209 |
| 4 | 86 |
| 5 | 67 |
| 6 | 32 |
| 7 | 20 |
| 8 | 18 |
| 9 | 11 |
| 10 | 13 |
| 11 | 12 |
| 12 | 4 |
| 13 | 7 |
| 14 | 2 |
| 15 | 1 |
| 16 | 1 |
| 17 | 3 |
| 18 | 1 |
| 19 | 3 |
| 20 | 2 |
| 23 | 1 |

## Summary Statistics

| Metric | Min | P25 | Median | Mean | P75 | P90 | P95 | P99 | Max |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| baseline_top_networking_count | 1 | 1 | 1 | 1.73 | 2 | 3 | 5 | 11 | 23 |
| baseline_clean_publication_count | 1 | 2 | 6 | 11.45 | 14 | 28 | 39 | 78 | 261 |
| post2023_clean_publication_count | 0 | 0 | 3 | 8.47 | 10 | 21 | 32 | 76 | 244 |
| clean_publication_count | 1 | 3 | 9 | 19.92 | 24 | 48 | 71 | 147 | 505 |
| baseline_active_year_count | 1 | 2 | 3 | 3.2 | 5 | 5 | 5 | 5 | 5 |

## Proposed Scope Flags

- Researchers with total clean publications equal to 1: 425
- These are flagged as likely too sparse for trajectory analysis, though retained in raw cohort artifacts.

## Candidate Core Slice Summaries

| Slice | Researchers | High-total >100 | High-total share | Median total clean pubs |
|---|---:|---:|---:|---:|
| baseline_top_networking_count >= 1 | 3571 | 88 | 0.0246 | 9 |
| baseline_top_networking_count >= 2 | 1051 | 23 | 0.0219 | 16 |
| baseline_top_networking_count >= 3 | 493 | 12 | 0.0243 | 23 |
| baseline_top_networking_count >= 4 | 284 | 10 | 0.0352 | 29.0 |
| baseline_top_networking_count >= 5 | 198 | 9 | 0.0455 | 31.0 |
| baseline_top_networking_count >= 6 | 131 | 7 | 0.0534 | 36 |
| baseline_top_networking_count >= 7 | 99 | 5 | 0.0505 | 38 |
| baseline_top_networking_count >= 10 | 50 | 4 | 0.08 | 43.0 |
| baseline_top_networking_count > 6 | 99 | 5 | 0.0505 | 38 |

## High-Total Publication Outliers

Researchers with total clean publications > 100 are listed in `data/cohort_shape_high_total_outliers.csv`.
These are important to review because common-name profiles, broad cross-domain researchers, or one-off collaborators can bias aggregate analysis.

## Top Qualifying Venue Combinations

| Venue combination | Researchers |
|---|---:|
| NSDI | 886 |
| SIGCOMM | 633 |
| CoNEXT | 569 |
| Unknown | 422 |
| HotNets | 225 |
| IMC | 197 |
| NSDI+SIGCOMM | 192 |
| HotNets+NSDI+SIGCOMM | 66 |
| HotNets+NSDI | 65 |
| CoNEXT+NSDI | 53 |
| CoNEXT+SIGCOMM | 48 |
| HotNets+SIGCOMM | 47 |
| CoNEXT+NSDI+SIGCOMM | 30 |
| CoNEXT+HotNets+NSDI+SIGCOMM | 23 |
| IMC+SIGCOMM | 20 |
| CoNEXT+HotNets | 19 |
| CoNEXT+IMC | 17 |
| CoNEXT+IMC+SIGCOMM | 9 |
| CoNEXT+HotNets+SIGCOMM | 9 |
| CoNEXT+HotNets+IMC+SIGCOMM | 5 |
| HotNets+IMC | 5 |
| HotNets+IMC+NSDI | 5 |
| HotNets+IMC+NSDI+SIGCOMM | 4 |
| CoNEXT+HotNets+IMC+NSDI+SIGCOMM | 4 |
| CoNEXT+HotNets+IMC | 4 |

## Generated Figures

- `figures/cohort_shape/baseline_top_networking_count_distribution.png`
- `figures/cohort_shape/total_clean_publication_histogram.png`
- `figures/cohort_shape/baseline_clean_publication_histogram.png`
- `figures/cohort_shape/post2023_clean_publication_histogram.png`
- `figures/cohort_shape/baseline_networking_vs_total_clean_scatter.png`
- `figures/cohort_shape/baseline_networking_by_total_clean_heatmap.png`
- `figures/cohort_shape/qualifying_venue_combo_top20.png`
