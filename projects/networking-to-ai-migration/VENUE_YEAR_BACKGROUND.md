# Venue-Year Background: I.1/I.2 First Pass

This report materializes the first gate in `ANALYSIS_PLAN.md`: paper-scope definitions and cohort-neutral venue-year background. It uses the repaired top-net paper table and does not yet overlay core-99/new-core cohort labels.

## 1. Scope Audit

| Metric | Count |
|---|---:|
| Total top-net table records | 2429 |
| Included top-net main-paper records | 2236 |
| Excluded records | 193 |

Excluded-record reasons:

| Reason | Count |
|---|---:|
| `non_main_prefix` | 133 |
| `record_type:proceedings` | 41 |
| `editorial` | 11 |
| `conext_workshop_or_summary` | 8 |

## 2. All Top-Net Venues Combined By Year

| Year | Papers | AI infra % | Classical networking % | Measurement % | Wireless/mobile % | Other/uncertain primary % | Gini | Repeat-author paper share % |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 2018 | 181 | 0.3 | 19.4 | 14.8 | 13.7 | 37.0 | 0.141 | 64.1 |
| 2019 | 172 | 0.6 | 25.2 | 12.7 | 10.3 | 36.6 | 0.139 | 68.0 |
| 2020 | 265 | 1.3 | 18.9 | 12.6 | 16.1 | 34.3 | 0.173 | 68.7 |
| 2021 | 248 | 1.3 | 16.0 | 12.9 | 18.0 | 34.3 | 0.148 | 67.7 |
| 2022 | 269 | 1.7 | 16.6 | 15.7 | 12.4 | 36.4 | 0.170 | 74.7 |
| 2023 | 291 | 3.4 | 14.7 | 12.8 | 13.8 | 31.3 | 0.177 | 76.3 |
| 2024 | 314 | 5.4 | 14.1 | 12.6 | 15.9 | 36.9 | 0.189 | 72.6 |
| 2025 | 346 | 6.1 | 17.0 | 12.8 | 13.8 | 30.6 | 0.217 | 77.5 |
| 2026 | 150 | 9.7 | 15.7 | 12.2 | 3.4 | 27.3 | 0.136 | 68.7 |

Description: the combined top-net table provides the field-level yearly baseline. AI infrastructure is low before 2023 and becomes visibly larger after 2023, while the `Other/uncertain` share remains high enough that topic claims should stay provisional.

## 3. Highest AI-Infrastructure Venue-Years

| Rank | Venue | Year | Papers | AI infra % | Other/uncertain primary % | Top topics |
|---:|---|---:|---:|---:|---:|---|
| 1 | NSDI | 2025 | 83 | 10.8 | 26.5 | Other 26.5%; Wireless, Mobile & Sensing 14.5%; Classical Networking 13.1% |
| 2 | SIGCOMM | 2024 | 62 | 10.8 | 24.2 | Other 24.2%; Network Measurement & Telemetry 15.3%; Classical Networking 14.8% |
| 3 | NSDI | 2026 | 150 | 9.7 | 27.3 | Other 27.3%; Classical Networking 15.7%; Networked Systems & Datacenter 13.6% |
| 4 | SIGCOMM | 2025 | 88 | 9.5 | 26.1 | Other 26.1%; Classical Networking 20.6%; Wireless, Mobile & Sensing 15.3% |
| 5 | HotNets | 2024 | 44 | 6.8 | 45.5 | Other 45.5%; Wireless, Mobile & Sensing 18.2%; Classical Networking 14.4% |
| 6 | HotNets | 2023 | 38 | 6.6 | 42.1 | Other 42.1%; Networked Systems & Datacenter 14.5%; Classical Networking 14.0% |
| 7 | NSDI | 2023 | 96 | 6.2 | 24.0 | Other 24.0%; Wireless, Mobile & Sensing 19.1%; Network Measurement & Telemetry 13.9% |
| 8 | NSDI | 2024 | 112 | 6.2 | 33.9 | Other 33.9%; Wireless, Mobile & Sensing 18.0%; Classical Networking 14.0% |
| 9 | CoNEXT | 2025 | 52 | 5.3 | 19.2 | Classical Networking 26.9%; Wireless, Mobile & Sensing 20.8%; Other 19.2% |
| 10 | NSDI | 2022 | 78 | 3.9 | 32.0 | Other 32.0%; Classical Networking 14.7%; Network Measurement & Telemetry 11.5% |

Interpretation: AI-infrastructure signal is not venue-uniform. It is most visible in recent NSDI/SIGCOMM years and some smaller HotNets/CoNEXT years, so researcher-level AI-infra claims should be compared against each author's venue background.

## 4. Most Concentrated Venue-Years By Gini

| Rank | Venue | Year | Papers | Unique authors | Gini | HHI | Top-5 incidence share % | Repeat-author paper share % |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | IMC | 2022 | 76 | 283 | 0.169 | 0.005 | 7.5 | 61.8 |
| 2 | SIGCOMM | 2025 | 88 | 754 | 0.162 | 0.002 | 3.0 | 67.0 |
| 3 | IMC | 2025 | 73 | 314 | 0.140 | 0.004 | 5.7 | 50.7 |
| 4 | NSDI | 2026 | 150 | 1039 | 0.136 | 0.001 | 2.3 | 68.7 |
| 5 | IMC | 2023 | 52 | 220 | 0.130 | 0.005 | 7.4 | 55.8 |
| 6 | IMC | 2020 | 54 | 243 | 0.122 | 0.005 | 6.4 | 46.3 |
| 7 | IMC | 2021 | 54 | 238 | 0.114 | 0.005 | 5.9 | 50.0 |
| 8 | NSDI | 2023 | 96 | 613 | 0.108 | 0.002 | 3.0 | 64.6 |
| 9 | IMC | 2018 | 43 | 207 | 0.106 | 0.005 | 6.8 | 55.8 |
| 10 | NSDI | 2025 | 83 | 551 | 0.102 | 0.002 | 3.1 | 56.6 |

Interpretation: concentration should be read with paper count. Smaller venues can show high concentration because a few repeated authors cover a larger share of papers. Gini, HHI, top-k share, and repeat-author share should be read together rather than as one decisive metric.

## 5. Coverage And Count Mismatches

The `expected_total_from_venue_totals` column comes from the existing venue totals artifact. Mismatches in this section compare clean included main papers with raw TOC-like totals, so they are diagnostics, not automatic errors. A separate `TOPNET_VENUE_COMPLETENESS.md` audit checks raw fetched coverage before cleaning.

| Venue | Year | Observed included papers | Expected total | Status | Excluded records in repaired table |
|---|---:|---:|---:|---|---:|
| SIGCOMM | 2018 | 40 | 41 | `below_expected_total` | 1 |
| SIGCOMM | 2019 | 32 | 33 | `below_expected_total` | 1 |
| SIGCOMM | 2020 | 53 | 54 | `below_expected_total` | 1 |
| SIGCOMM | 2021 | 55 | 56 | `below_expected_total` | 1 |
| SIGCOMM | 2022 | 55 | 56 | `below_expected_total` | 1 |
| SIGCOMM | 2023 | 71 | 108 | `below_expected_total` | 37 |
| SIGCOMM | 2024 | 62 | 63 | `below_expected_total` | 1 |
| SIGCOMM | 2025 | 88 | 89 | `below_expected_total` | 1 |
| SIGCOMM | 2026 | 0 |  | `unavailable_or_not_indexed` | 0 |
| NSDI | 2018 | 40 | 41 | `below_expected_total` | 1 |
| NSDI | 2019 | 49 | 50 | `below_expected_total` | 1 |
| NSDI | 2020 | 65 | 66 | `below_expected_total` | 1 |
| NSDI | 2021 | 59 | 60 | `below_expected_total` | 1 |
| NSDI | 2022 | 78 | 79 | `below_expected_total` | 1 |
| NSDI | 2023 | 96 | 97 | `below_expected_total` | 1 |
| NSDI | 2024 | 112 | 113 | `below_expected_total` | 1 |
| NSDI | 2025 | 83 | 84 | `below_expected_total` | 1 |
| NSDI | 2026 | 150 | 151 | `below_expected_total` | 1 |
| CoNEXT | 2018 | 32 | 33 | `below_expected_total` | 1 |
| CoNEXT | 2019 | 32 | 33 | `below_expected_total` | 1 |
| CoNEXT | 2020 | 63 | 64 | `below_expected_total` | 1 |
| CoNEXT | 2021 | 49 | 51 | `below_expected_total` | 2 |
| CoNEXT | 2022 | 28 | 29 | `below_expected_total` | 1 |
| CoNEXT | 2023 | 34 | 41 | `below_expected_total` | 10 |
| CoNEXT | 2024 | 40 | 49 | `below_expected_total` | 13 |
| CoNEXT | 2025 | 52 | 78 | `below_expected_total` | 30 |
| CoNEXT | 2026 | 0 |  | `unavailable_or_not_indexed` | 0 |
| HotNets | 2018 | 26 | 27 | `below_expected_total` | 1 |
| HotNets | 2019 | 20 | 21 | `below_expected_total` | 1 |
| HotNets | 2020 | 30 | 31 | `below_expected_total` | 1 |
| HotNets | 2021 | 31 | 32 | `below_expected_total` | 1 |
| HotNets | 2022 | 32 | 33 | `below_expected_total` | 1 |
| HotNets | 2023 | 38 | 39 | `below_expected_total` | 1 |
| HotNets | 2024 | 44 | 45 | `below_expected_total` | 1 |
| HotNets | 2025 | 50 | 51 | `below_expected_total` | 1 |
| HotNets | 2026 | 0 |  | `unavailable_or_not_indexed` | 0 |
| IMC | 2018 | 43 | 44 | `below_expected_total` | 1 |
| IMC | 2019 | 39 | 40 | `below_expected_total` | 1 |
| IMC | 2020 | 54 | 55 | `below_expected_total` | 1 |
| IMC | 2021 | 54 | 55 | `below_expected_total` | 1 |
| IMC | 2022 | 76 | 77 | `below_expected_total` | 1 |
| IMC | 2023 | 52 | 64 | `below_expected_total` | 12 |
| IMC | 2024 | 56 | 85 | `below_expected_total` | 29 |
| IMC | 2025 | 73 | 100 | `below_expected_total` | 27 |
| IMC | 2026 | 0 |  | `unavailable_or_not_indexed` | 0 |

## 6. What Can Be Said Now

Data-supported observations:

1. The repaired top-net table contains 2236 included main-paper records and 193 excluded non-main records.
2. Raw DBLP TOC coverage and clean main-paper scope are distinct: one audits data fetch completeness; the other defines the analyzable paper universe.
3. Venue-year background can now be described without researcher cohort labels, but topic shares remain Stage-1 diagnostics.
4. Author concentration varies by venue-year and needs multiple metrics; no single concentration number should drive interpretation.

Interpretive cautions:

- This is a Stage-1 topic view based on title keyword rules. It is appropriate for scoping and anomaly detection, not final semantic claims.
- Cohort overlays such as core-99/new-core/stayer/newcomer/dropout are intentionally deferred until this venue baseline is reviewed.
- 2026 remains incomplete; missing venue-years should not be interpreted as topical absence.
