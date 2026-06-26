# Top Networking Venue Completeness Audit

Status: usable as the paper-scope foundation for the next analysis step, with 2026 venue availability caveats.

## Scope Distinction

- Raw TOC coverage checks whether DBLP returned all records for a venue-year TOC.
- Clean main-paper scope excludes proceedings volumes, posters, demos, editorials, and workshop summaries.
- Therefore clean main-paper counts can be lower than raw TOC totals without implying missing data.

## Summary

| Metric | Count |
|---|---:|
| Venue-years audited | 45 |
| Raw TOC complete venue-years | 41 |
| Not yet available/indexed venue-years | 4 |
| Venue-years with raw-fetch concerns | 0 |
| Observed merged records | 2429 |
| Clean main-paper records | 2236 |
| Excluded non-main records | 193 |

Raw fetch status counts:

| Status | Venue-years |
|---|---:|
| `not_yet_available` | 4 |
| `raw_toc_complete` | 41 |

## Venue-Year Audit

| Venue | Year | Raw status | Conf records/total | PACMNET records/total | Observed merged | Clean main | Excluded | Exclusion breakdown |
|---|---:|---|---:|---:|---:|---:|---:|---|
| SIGCOMM | 2018 | `raw_toc_complete` | 41/41 |  | 41 | 40 | 1 | record_type:proceedings:1 |
| NSDI | 2018 | `raw_toc_complete` | 41/41 |  | 41 | 40 | 1 | record_type:proceedings:1 |
| CoNEXT | 2018 | `raw_toc_complete` | 33/33 |  | 33 | 32 | 1 | record_type:proceedings:1 |
| HotNets | 2018 | `raw_toc_complete` | 27/27 |  | 27 | 26 | 1 | record_type:proceedings:1 |
| IMC | 2018 | `raw_toc_complete` | 44/44 |  | 44 | 43 | 1 | record_type:proceedings:1 |
| SIGCOMM | 2019 | `raw_toc_complete` | 33/33 |  | 33 | 32 | 1 | record_type:proceedings:1 |
| NSDI | 2019 | `raw_toc_complete` | 50/50 |  | 50 | 49 | 1 | record_type:proceedings:1 |
| CoNEXT | 2019 | `raw_toc_complete` | 33/33 |  | 33 | 32 | 1 | record_type:proceedings:1 |
| HotNets | 2019 | `raw_toc_complete` | 21/21 |  | 21 | 20 | 1 | record_type:proceedings:1 |
| IMC | 2019 | `raw_toc_complete` | 40/40 |  | 40 | 39 | 1 | record_type:proceedings:1 |
| SIGCOMM | 2020 | `raw_toc_complete` | 54/54 |  | 54 | 53 | 1 | record_type:proceedings:1 |
| NSDI | 2020 | `raw_toc_complete` | 66/66 |  | 66 | 65 | 1 | record_type:proceedings:1 |
| CoNEXT | 2020 | `raw_toc_complete` | 64/64 |  | 64 | 63 | 1 | record_type:proceedings:1 |
| HotNets | 2020 | `raw_toc_complete` | 31/31 |  | 31 | 30 | 1 | record_type:proceedings:1 |
| IMC | 2020 | `raw_toc_complete` | 55/55 |  | 55 | 54 | 1 | record_type:proceedings:1 |
| SIGCOMM | 2021 | `raw_toc_complete` | 56/56 |  | 56 | 55 | 1 | record_type:proceedings:1 |
| NSDI | 2021 | `raw_toc_complete` | 60/60 |  | 60 | 59 | 1 | record_type:proceedings:1 |
| CoNEXT | 2021 | `raw_toc_complete` | 51/51 |  | 51 | 49 | 2 | conext_workshop_or_summary:1; record_type:proceedings:1 |
| HotNets | 2021 | `raw_toc_complete` | 32/32 |  | 32 | 31 | 1 | record_type:proceedings:1 |
| IMC | 2021 | `raw_toc_complete` | 55/55 |  | 55 | 54 | 1 | record_type:proceedings:1 |
| SIGCOMM | 2022 | `raw_toc_complete` | 56/56 |  | 56 | 55 | 1 | record_type:proceedings:1 |
| NSDI | 2022 | `raw_toc_complete` | 79/79 |  | 79 | 78 | 1 | record_type:proceedings:1 |
| CoNEXT | 2022 | `raw_toc_complete` | 29/29 |  | 29 | 28 | 1 | record_type:proceedings:1 |
| HotNets | 2022 | `raw_toc_complete` | 33/33 |  | 33 | 32 | 1 | record_type:proceedings:1 |
| IMC | 2022 | `raw_toc_complete` | 77/77 |  | 77 | 76 | 1 | record_type:proceedings:1 |
| SIGCOMM | 2023 | `raw_toc_complete` | 108/108 |  | 108 | 71 | 37 | non_main_prefix:36; record_type:proceedings:1 |
| NSDI | 2023 | `raw_toc_complete` | 97/97 |  | 97 | 96 | 1 | record_type:proceedings:1 |
| CoNEXT | 2023 | `raw_toc_complete` | 17/17 | 27/27 | 44 | 34 | 10 | non_main_prefix:6; editorial:3; record_type:proceedings:1 |
| HotNets | 2023 | `raw_toc_complete` | 39/39 |  | 39 | 38 | 1 | record_type:proceedings:1 |
| IMC | 2023 | `raw_toc_complete` | 64/64 |  | 64 | 52 | 12 | non_main_prefix:11; record_type:proceedings:1 |
| SIGCOMM | 2024 | `raw_toc_complete` | 63/63 |  | 63 | 62 | 1 | record_type:proceedings:1 |
| NSDI | 2024 | `raw_toc_complete` | 113/113 |  | 113 | 112 | 1 | record_type:proceedings:1 |
| CoNEXT | 2024 | `raw_toc_complete` | 17/17 | 36/36 | 53 | 40 | 13 | non_main_prefix:8; editorial:4; record_type:proceedings:1 |
| HotNets | 2024 | `raw_toc_complete` | 45/45 |  | 45 | 44 | 1 | record_type:proceedings:1 |
| IMC | 2024 | `raw_toc_complete` | 85/85 |  | 85 | 56 | 29 | non_main_prefix:28; record_type:proceedings:1 |
| SIGCOMM | 2025 | `raw_toc_complete` | 89/89 |  | 89 | 88 | 1 | record_type:proceedings:1 |
| NSDI | 2025 | `raw_toc_complete` | 84/84 |  | 84 | 83 | 1 | record_type:proceedings:1 |
| CoNEXT | 2025 | `raw_toc_complete` | 28/28 | 54/54 | 82 | 52 | 30 | non_main_prefix:18; conext_workshop_or_summary:7; editorial:4; record_type:proceedings:1 |
| HotNets | 2025 | `raw_toc_complete` | 51/51 |  | 51 | 50 | 1 | record_type:proceedings:1 |
| IMC | 2025 | `raw_toc_complete` | 100/100 |  | 100 | 73 | 27 | non_main_prefix:26; record_type:proceedings:1 |
| SIGCOMM | 2026 | `not_yet_available` | 0/0 |  | 0 | 0 | 0 | none |
| NSDI | 2026 | `raw_toc_complete` | 151/151 |  | 151 | 150 | 1 | record_type:proceedings:1 |
| CoNEXT | 2026 | `not_yet_available` | 0/0 | 0/0 | 0 | 0 | 0 | none |
| HotNets | 2026 | `not_yet_available` | 0/0 |  | 0 | 0 | 0 | none |
| IMC | 2026 | `not_yet_available` | 0/0 |  | 0 | 0 | 0 | none |

## Current Judgment

The top-networking venue data is complete enough for paper-scope and venue-background work through the available DBLP TOCs. The unresolved caveat is availability, not partial fetching: SIGCOMM, CoNEXT, HotNets, IMC, and PACMNET 2026 are not yet indexed/available in the local DBLP TOC source, while NSDI 2026 is available and complete.

Topic classification and researcher trajectory analysis should use `clean_main_records`; completeness checks should use the raw TOC columns.
