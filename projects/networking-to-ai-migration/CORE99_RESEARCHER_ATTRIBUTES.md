# Core-99 Researcher Attributes

This is a derived attribute table for the provisional core-99 sample. It keeps the broad cohort intact and adds observable/pre-interpretive fields for review.

## Summary

- Researchers: 99
- Selection rule: baseline_top_networking_count > 6
- Baseline: 2018-2022
- Post-2023 window: 2023-2026
- Median selection baseline top-networking count: 10
- Median clean-itinerary baseline top-networking count: 9
- Baseline count mismatches versus selection count: 9
- Median post-2023 top-networking count: 6
- Median top-networking rate ratio post/base: 0.735
- Median total clean publication count: 38
- Median clean-publication rate ratio post/base: 0.815

## Column Definitions

All labels in this table are deterministic rule-based labels from counts. No LLM is used here.

- Selection baseline top-net: the original count used to select the core-99 sample from the cohort artifact. It is kept only for traceability.
- Clean baseline top-net: current clean itinerary-derived count in SIGCOMM/NSDI/CoNEXT/HotNets/IMC during 2018-2022. Use this for analysis.
- Post-2023 top-net: current clean count in SIGCOMM/NSDI/CoNEXT/HotNets/IMC during 2023-2026.
- Top-net rate ratio: `(post-2023 top-net / 4) / (clean baseline top-net / 5)`.
- Top-net trend: deterministic label from top-net rate ratio. Increased means ratio >= 1.25, decreased means ratio <= 0.75, flat is between those bounds, and zero post-2023 top-net papers is inactive_after_2022.
- Baseline clean pubs and post-2023 clean pubs: all clean conference/workshop papers in each period, not only top-networking papers.
- Clean-pub rate ratio: `(post-2023 clean pubs / 4) / (baseline clean pubs / 5)`.
- Clean-pub trend: deterministic label using the same thresholds as top-net trend, but applied to all clean publications.
- Clean-pub activity coverage: deterministic label from active publication years. Continuous means >=4 active baseline years and >=3 active post-2023 years; post_active means <4 active baseline years but >=3 active post-2023 years; intermittent_post means 2 active post-2023 years; sporadic_post means 1; inactive_after_2022 means 0.
- Authorship placement uses DBLP author order after explicit alias resolution. First/middle/last shares are computed over papers where the scoped researcher is matched in the author list. Single-author papers count as both first and last.
- Author role profile: mostly_lead if first-author share >= 0.5; mostly_senior if last-author share >= 0.5; mostly_collaborator if middle-author share >= 0.5; mixed otherwise; unknown if no matched author positions.

## Distributions

### Top-Networking Rate Change

| Label | Researchers |
|---|---:|
| decreased | 47 |
| flat | 31 |
| increased | 16 |
| inactive_after_2022 | 5 |

### Clean-Publication Rate Change

| Label | Researchers |
|---|---:|
| decreased | 44 |
| flat | 36 |
| increased | 17 |
| inactive_after_2022 | 2 |

### Clean-Publication Activity Coverage

| Label | Researchers |
|---|---:|
| continuous | 83 |
| intermittent_post | 12 |
| sporadic_post | 2 |
| inactive_after_2022 | 2 |

### Qualifying Venue Mix

| Label | Researchers |
|---|---:|
| mixed_3plus | 55 |
| IMC_heavy | 26 |
| SIGCOMM_heavy | 8 |
| NSDI_heavy | 4 |
| mixed_2 | 3 |
| CoNEXT_heavy | 2 |
| HotNets_heavy | 1 |

### Baseline Author-Role Profile

| Label | Researchers |
|---|---:|
| mostly_collaborator | 58 |
| mostly_senior | 33 |
| mostly_lead | 5 |
| mixed | 3 |

### Post-2023 Author-Role Profile

| Label | Researchers |
|---|---:|
| mostly_collaborator | 55 |
| mostly_senior | 40 |
| unknown | 2 |
| mixed | 1 |
| mostly_lead | 1 |

## Researcher Attributes

| Researcher | Selection baseline top-net | Clean baseline top-net | Post-2023 top-net | Top-net rate ratio | Top-net trend | Baseline clean pubs | Post-2023 clean pubs | Clean-pub rate ratio | Clean-pub trend | Clean-pub activity coverage | All-clean authorship baseline | All-clean authorship post | Top-net authorship baseline | Top-net authorship post | Venue mix | Baseline top venues | Post top venues |
|---|---:|---:|---:|---:|---|---:|---:|---:|---|---|---|---|---|---|---|---|---|
| Vyas Sekar | 23 | 22 | 6 | 0.341 | decreased | 49 | 18 | 0.459 | decreased | continuous | F:0.0 M:0.4082 L:0.5918 (mostly_senior) | F:0.0 M:0.2778 L:0.7222 (mostly_senior) | F:0.0 M:0.4545 L:0.5455 (mostly_senior) | F:0.0 M:0.6667 L:0.3333 (mostly_collaborator) | mixed_3plus | NSDI:6; SIGCOMM:6; IMC:5; HotNets:3; CoNEXT:2 | NSDI:4; IMC:1; HotNets:1 |
| Mohammad Alizadeh | 20 | 20 | 12 | 0.75 | decreased | 53 | 18 | 0.425 | decreased | continuous | F:0.0 M:0.7925 L:0.2075 (mostly_collaborator) | F:0.0 M:0.7778 L:0.2222 (mostly_collaborator) | F:0.0 M:0.85 L:0.15 (mostly_collaborator) | F:0.0 M:0.8333 L:0.1667 (mostly_collaborator) | mixed_3plus | SIGCOMM:10; NSDI:7; HotNets:3 | NSDI:8; SIGCOMM:4 |
| Hongqiang Harry Liu | 20 | 20 | 2 | 0.125 | decreased | 21 | 3 | 0.179 | decreased | sporadic_post | F:0.0476 M:0.8095 L:0.1429 (mostly_collaborator) | F:0.0 M:1.0 L:0.0 (mostly_collaborator) | F:0.0 M:0.85 L:0.15 (mostly_collaborator) | F:0.0 M:1.0 L:0.0 (mostly_collaborator) | SIGCOMM_heavy | SIGCOMM:15; NSDI:5 | NSDI:1; SIGCOMM:1 |
| Arvind Krishnamurthy | 19 | 19 | 14 | 0.921 | flat | 36 | 30 | 1.042 | flat | continuous | F:0.0 M:0.6667 L:0.3333 (mostly_collaborator) | F:0.0 M:0.8 L:0.2 (mostly_collaborator) | F:0.0 M:0.7895 L:0.2105 (mostly_collaborator) | F:0.0 M:0.7857 L:0.2143 (mostly_collaborator) | mixed_3plus | NSDI:9; SIGCOMM:6; HotNets:4 | SIGCOMM:6; NSDI:6; HotNets:2 |
| Kimberly C. Claffy | 19 | 19 | 13 | 0.855 | flat | 39 | 23 | 0.737 | decreased | continuous | F:0.0 M:0.4615 L:0.5385 (mostly_senior) | F:0.0 M:0.5217 L:0.4783 (mostly_collaborator) | F:0.0 M:0.3684 L:0.6316 (mostly_senior) | F:0.0 M:0.3077 L:0.6923 (mostly_senior) | IMC_heavy | IMC:16; CoNEXT:2; SIGCOMM:1 | IMC:9; SIGCOMM:3; HotNets:1 |
| Laurent Vanbever | 19 | 19 | 10 | 0.658 | decreased | 34 | 26 | 0.956 | flat | continuous | F:0.0 M:0.3235 L:0.6765 (mostly_senior) | F:0.0 M:0.16 L:0.84 (mostly_senior) | F:0.0 M:0.3158 L:0.6842 (mostly_senior) | F:0.0 M:0.1 L:0.9 (mostly_senior) | mixed_3plus | NSDI:7; HotNets:6; SIGCOMM:5; IMC:1 | NSDI:4; HotNets:3; SIGCOMM:2; IMC:1 |
| Amin Vahdat | 18 | 18 | 8 | 0.556 | decreased | 25 | 15 | 0.75 | decreased | continuous | F:0.0 M:0.12 L:0.88 (mostly_senior) | F:0.0667 M:0.0 L:1.0 (mostly_senior) | F:0.0 M:0.0556 L:0.9444 (mostly_senior) | F:0.0 M:0.0 L:1.0 (mostly_senior) | mixed_3plus | SIGCOMM:10; NSDI:7; HotNets:1 | SIGCOMM:5; NSDI:3 |
| Aditya Akella | 17 | 17 | 13 | 0.956 | flat | 36 | 35 | 1.215 | flat | continuous | F:0.0 M:0.5 L:0.5 (mostly_senior) | F:0.0 M:0.3529 L:0.6471 (mostly_senior) | F:0.0 M:0.5294 L:0.4706 (mostly_collaborator) | F:0.0 M:0.3846 L:0.6154 (mostly_senior) | mixed_3plus | NSDI:10; HotNets:4; SIGCOMM:2; CoNEXT:1 | NSDI:10; SIGCOMM:2; HotNets:1 |
| Minlan Yu | 17 | 16 | 15 | 1.172 | flat | 35 | 24 | 0.857 | flat | continuous | F:0.0 M:0.4857 L:0.5143 (mostly_senior) | F:0.0 M:0.4348 L:0.5652 (mostly_senior) | F:0.0 M:0.5 L:0.5 (mostly_senior) | F:0.0 M:0.4286 L:0.5714 (mostly_senior) | mixed_3plus | SIGCOMM:8; HotNets:3; NSDI:2; CoNEXT:2; IMC:1 | NSDI:9; SIGCOMM:4; PACMNET:1; HotNets:1 |
| Ethan Katz-Bassett | 17 | 17 | 10 | 0.735 | decreased | 30 | 14 | 0.583 | decreased | continuous | F:0.0 M:0.5333 L:0.4667 (mostly_collaborator) | F:0.0 M:0.6429 L:0.3571 (mostly_collaborator) | F:0.0 M:0.5294 L:0.4706 (mostly_collaborator) | F:0.0 M:0.6 L:0.4 (mostly_collaborator) | mixed_3plus | IMC:9; SIGCOMM:3; HotNets:3; NSDI:1; CoNEXT:1 | IMC:5; SIGCOMM:3; HotNets:2 |
| Srinivasan Seshan | 16 | 15 | 8 | 0.667 | decreased | 20 | 17 | 1.062 | flat | continuous | F:0.0 M:0.4 L:0.6 (mostly_senior) | F:0.0 M:0.4706 L:0.5294 (mostly_senior) | F:0.0 M:0.4 L:0.6 (mostly_senior) | F:0.0 M:0.375 L:0.625 (mostly_senior) | mixed_3plus | HotNets:5; SIGCOMM:5; NSDI:3; CoNEXT:1; IMC:1 | NSDI:5; SIGCOMM:2; IMC:1 |
| Sylvia Ratnasamy | 15 | 15 | 13 | 1.083 | flat | 21 | 23 | 1.369 | increased | continuous | F:0.0 M:0.7143 L:0.2857 (mostly_collaborator) | F:0.0 M:0.8261 L:0.1739 (mostly_collaborator) | F:0.0 M:0.7333 L:0.2667 (mostly_collaborator) | F:0.0 M:0.8462 L:0.1538 (mostly_collaborator) | mixed_3plus | NSDI:6; HotNets:5; SIGCOMM:4 | HotNets:7; NSDI:3; SIGCOMM:3 |
| Georgios Smaragdakis | 14 | 14 | 9 | 0.804 | flat | 23 | 32 | 1.739 | increased | continuous | F:0.0 M:0.6957 L:0.3043 (mostly_collaborator) | F:0.0 M:0.5 L:0.5 (mostly_senior) | F:0.0 M:0.6429 L:0.3571 (mostly_collaborator) | F:0.0 M:0.6667 L:0.3333 (mostly_collaborator) | IMC_heavy | IMC:9; CoNEXT:3; HotNets:1; SIGCOMM:1 | IMC:9 |
| Anja Feldmann | 14 | 13 | 6 | 0.577 | decreased | 31 | 24 | 0.968 | flat | continuous | F:0.0645 M:0.1935 L:0.7419 (mostly_senior) | F:0.0 M:0.625 L:0.375 (mostly_collaborator) | F:0.0769 M:0.3846 L:0.5385 (mostly_senior) | F:0.0 M:0.5 L:0.5 (mostly_senior) | IMC_heavy | IMC:8; CoNEXT:5 | IMC:6 |
| Ion Stoica | 13 | 13 | 12 | 1.154 | flat | 83 | 73 | 1.099 | flat | continuous | F:0.0361 M:0.3373 L:0.6506 (mostly_senior) | F:0.0137 M:0.4247 L:0.5753 (mostly_senior) | F:0.0 M:0.1538 L:0.8462 (mostly_senior) | F:0.0 M:0.0833 L:0.9167 (mostly_senior) | NSDI_heavy | NSDI:9; SIGCOMM:3; HotNets:1 | NSDI:8; HotNets:3; SIGCOMM:1 |
| Xin Jin 0008 | 13 | 13 | 21 | 2.019 | increased | 37 | 39 | 1.318 | increased | continuous | F:0.0541 M:0.5405 L:0.4054 (mostly_collaborator) | F:0.0 M:0.4103 L:0.5897 (mostly_senior) | F:0.0769 M:0.3077 L:0.6154 (mostly_senior) | F:0.0 M:0.2381 L:0.7619 (mostly_senior) | mixed_3plus | SIGCOMM:7; NSDI:4; CoNEXT:2 | NSDI:14; SIGCOMM:7 |
| Gianni Antichi | 13 | 13 | 11 | 1.058 | flat | 30 | 28 | 1.167 | flat | continuous | F:0.0333 M:0.7 L:0.2667 (mostly_collaborator) | F:0.0 M:0.7692 L:0.2308 (mostly_collaborator) | F:0.0 M:0.8462 L:0.1538 (mostly_collaborator) | F:0.0 M:0.7778 L:0.2222 (mostly_collaborator) | mixed_3plus | CoNEXT:4; SIGCOMM:3; NSDI:3; HotNets:2; IMC:1 | NSDI:4; SIGCOMM:3; HotNets:2; PACMNET:2 |
| Scott Shenker | 13 | 13 | 13 | 1.25 | increased | 27 | 24 | 1.111 | flat | continuous | F:0.0 M:0.1852 L:0.8148 (mostly_senior) | F:0.0 M:0.4583 L:0.5417 (mostly_senior) | F:0.0 M:0.0769 L:0.9231 (mostly_senior) | F:0.0 M:0.4615 L:0.5385 (mostly_senior) | mixed_3plus | HotNets:5; NSDI:4; SIGCOMM:4 | HotNets:6; SIGCOMM:4; NSDI:3 |
| Ryan Beckett | 13 | 13 | 15 | 1.442 | increased | 21 | 18 | 1.071 | flat | continuous | F:0.2381 M:0.7619 L:0.0 (mostly_collaborator) | F:0.0556 M:0.8889 L:0.0556 (mostly_collaborator) | F:0.3077 M:0.6923 L:0.0 (mostly_collaborator) | F:0.0 M:0.9333 L:0.0667 (mostly_collaborator) | mixed_3plus | SIGCOMM:5; HotNets:4; NSDI:4 | NSDI:9; HotNets:3; SIGCOMM:3 |
| Alex C. Snoeren | 13 | 13 | 7 | 0.673 | decreased | 23 | 15 | 0.815 | flat | continuous | F:0.0 M:0.6957 L:0.3043 (mostly_collaborator) | F:0.0 M:0.7333 L:0.2667 (mostly_collaborator) | F:0.0 M:0.6154 L:0.3846 (mostly_collaborator) | F:0.0 M:0.7143 L:0.2857 (mostly_collaborator) | mixed_3plus | IMC:6; SIGCOMM:3; NSDI:2; HotNets:1; CoNEXT:1 | SIGCOMM:4; IMC:2; NSDI:1 |
| Gautam Akiwate | 13 | 13 | 3 | 0.288 | decreased | 17 | 7 | 0.515 | decreased | continuous | F:0.1765 M:0.8235 L:0.0 (mostly_collaborator) | F:0.0 M:1.0 L:0.0 (mostly_collaborator) | F:0.2308 M:0.7692 L:0.0 (mostly_collaborator) | F:0.0 M:1.0 L:0.0 (mostly_collaborator) | IMC_heavy | IMC:12; SIGCOMM:1 | IMC:2; SIGCOMM:1 |
| Stefan Schmid 0001 | 12 | 12 | 3 | 0.312 | decreased | 134 | 89 | 0.83 | flat | continuous | F:0.0373 M:0.403 L:0.5672 (mostly_senior) | F:0.0225 M:0.3371 L:0.6404 (mostly_senior) | F:0.0833 M:0.5 L:0.4167 (mostly_collaborator) | F:0.0 M:0.6667 L:0.3333 (mostly_collaborator) | CoNEXT_heavy | CoNEXT:9; IMC:1; NSDI:1; SIGCOMM:1 | NSDI:3 |
| Jennifer Rexford | 12 | 12 | 4 | 0.417 | decreased | 37 | 10 | 0.338 | decreased | continuous | F:0.0 M:0.4865 L:0.5135 (mostly_senior) | F:0.0 M:0.5 L:0.5 (mostly_senior) | F:0.0 M:0.6667 L:0.3333 (mostly_collaborator) | F:0.0 M:0.75 L:0.25 (mostly_collaborator) | mixed_3plus | SIGCOMM:5; NSDI:3; HotNets:2; CoNEXT:1; IMC:1 | NSDI:2; HotNets:1; SIGCOMM:1 |
| Narseo Vallina-Rodriguez | 12 | 12 | 1 | 0.104 | decreased | 23 | 7 | 0.38 | decreased | continuous | F:0.0 M:0.6087 L:0.3913 (mostly_collaborator) | F:0.0 M:0.5714 L:0.4286 (mostly_collaborator) | F:0.0 M:0.5 L:0.5 (mostly_senior) | F:0.0 M:0.0 L:1.0 (mostly_senior) | IMC_heavy | IMC:11; HotNets:1 | IMC:1 |
| Matt Calder | 12 | 12 | 3 | 0.312 | decreased | 14 | 3 | 0.268 | decreased | intermittent_post | F:0.1429 M:0.7143 L:0.1429 (mostly_collaborator) | F:0.0 M:0.6667 L:0.3333 (mostly_collaborator) | F:0.0833 M:0.75 L:0.1667 (mostly_collaborator) | F:0.0 M:0.6667 L:0.3333 (mostly_collaborator) | mixed_3plus | IMC:5; SIGCOMM:3; NSDI:2; HotNets:2 | IMC:2; HotNets:1 |
| Ang Chen 0001 | 11 | 11 | 9 | 1.023 | flat | 42 | 26 | 0.774 | flat | continuous | F:0.0 M:0.6667 L:0.3333 (mostly_collaborator) | F:0.0385 M:0.4231 L:0.5769 (mostly_senior) | F:0.0 M:0.6364 L:0.3636 (mostly_collaborator) | F:0.0 M:0.3333 L:0.6667 (mostly_senior) | mixed_2 | NSDI:6; HotNets:5 | NSDI:4; HotNets:3; SIGCOMM:2 |
| Ravi Netravali | 11 | 11 | 14 | 1.591 | increased | 32 | 21 | 0.82 | flat | continuous | F:0.1562 M:0.3125 L:0.5312 (mostly_senior) | F:0.0 M:0.5238 L:0.4762 (mostly_collaborator) | F:0.1818 M:0.2727 L:0.5455 (mostly_senior) | F:0.0 M:0.6429 L:0.3571 (mostly_collaborator) | NSDI_heavy | NSDI:7; CoNEXT:1; SIGCOMM:1; HotNets:1; IMC:1 | NSDI:12; HotNets:1; SIGCOMM:1 |
| Junchen Jiang | 11 | 11 | 9 | 1.023 | flat | 27 | 24 | 1.111 | flat | continuous | F:0.0741 M:0.4815 L:0.4444 (mixed) | F:0.0 M:0.4583 L:0.5417 (mostly_senior) | F:0.0909 M:0.3636 L:0.5455 (mostly_senior) | F:0.0 M:0.6667 L:0.3333 (mostly_collaborator) | SIGCOMM_heavy | SIGCOMM:7; NSDI:3; IMC:1 | NSDI:6; SIGCOMM:2; IMC:1 |
| Mattijs Jonker | 11 | 11 | 6 | 0.682 | decreased | 24 | 21 | 1.094 | flat | continuous | F:0.125 M:0.6667 L:0.2083 (mostly_collaborator) | F:0.0 M:0.7 L:0.3 (mostly_collaborator) | F:0.1818 M:0.6364 L:0.1818 (mostly_collaborator) | F:0.0 M:0.8 L:0.2 (mostly_collaborator) | IMC_heavy | IMC:11 | IMC:5; PACMNET:1 |
| Alberto Dainotti | 11 | 11 | 12 | 1.364 | increased | 24 | 18 | 0.938 | flat | continuous | F:0.0 M:0.625 L:0.375 (mostly_collaborator) | F:0.0 M:0.5 L:0.5 (mostly_senior) | F:0.0 M:0.6364 L:0.3636 (mostly_collaborator) | F:0.0 M:0.5 L:0.5 (mostly_senior) | IMC_heavy | IMC:9; NSDI:1; CoNEXT:1 | IMC:9; NSDI:2; SIGCOMM:1 |
| Omid Abari | 11 | 11 | 2 | 0.227 | decreased | 26 | 12 | 0.577 | decreased | continuous | F:0.0 M:0.5385 L:0.4615 (mostly_collaborator) | F:0.0 M:0.3333 L:0.6667 (mostly_senior) | F:0.0 M:0.4545 L:0.5455 (mostly_senior) | F:0.0 M:0.5 L:0.5 (mostly_senior) | mixed_2 | HotNets:6; SIGCOMM:5 | NSDI:1; SIGCOMM:1 |
| Geoffrey M. Voelker | 11 | 11 | 4 | 0.455 | decreased | 25 | 12 | 0.6 | decreased | continuous | F:0.0 M:0.88 L:0.12 (mostly_collaborator) | F:0.0 M:0.6667 L:0.3333 (mostly_collaborator) | F:0.0 M:0.9091 L:0.0909 (mostly_collaborator) | F:0.0 M:0.75 L:0.25 (mostly_collaborator) | IMC_heavy | IMC:11 | IMC:4 |
| Hari Balakrishnan | 11 | 11 | 2 | 0.227 | decreased | 29 | 4 | 0.172 | decreased | intermittent_post | F:0.0 M:0.3793 L:0.6207 (mostly_senior) | F:0.0 M:0.25 L:0.75 (mostly_senior) | F:0.0 M:0.1818 L:0.8182 (mostly_senior) | F:0.0 M:0.5 L:0.5 (mostly_senior) | mixed_3plus | NSDI:5; SIGCOMM:4; HotNets:2 | HotNets:1; SIGCOMM:1 |
| Michael Schapira | 11 | 11 | 3 | 0.341 | decreased | 26 | 5 | 0.24 | decreased | intermittent_post | F:0.0385 M:0.4615 L:0.5385 (mostly_senior) | F:0.0 M:0.8 L:0.2 (mostly_collaborator) | F:0.0 M:0.4545 L:0.5455 (mostly_senior) | F:0.0 M:1.0 L:0.0 (mostly_collaborator) | mixed_3plus | HotNets:5; SIGCOMM:4; NSDI:1; CoNEXT:1 | NSDI:1; HotNets:1; SIGCOMM:1 |
| Rachit Agarwal 0001 | 11 | 11 | 4 | 0.455 | decreased | 18 | 12 | 0.833 | flat | intermittent_post | F:0.0556 M:0.5556 L:0.3889 (mostly_collaborator) | F:0.0 M:0.5833 L:0.4167 (mostly_collaborator) | F:0.0 M:0.6364 L:0.3636 (mostly_collaborator) | F:0.0 M:0.25 L:0.75 (mostly_senior) | mixed_3plus | NSDI:6; SIGCOMM:4; HotNets:1 | NSDI:2; SIGCOMM:2 |
| Justine Sherry | 11 | 11 | 7 | 0.795 | flat | 15 | 10 | 0.833 | flat | continuous | F:0.0 M:0.4 L:0.6 (mostly_senior) | F:0.0 M:0.6 L:0.4 (mostly_collaborator) | F:0.0 M:0.4545 L:0.5455 (mostly_senior) | F:0.0 M:0.4286 L:0.5714 (mostly_senior) | mixed_3plus | SIGCOMM:4; IMC:3; NSDI:2; HotNets:2 | HotNets:2; NSDI:2; SIGCOMM:2; IMC:1 |
| Ming Zhang 0005 | 11 | 11 | 0 | 0.0 | inactive_after_2022 | 12 | 0 | 0.0 | inactive_after_2022 | inactive_after_2022 | F:0.0 M:0.5 L:0.5 (mostly_senior) | unknown | F:0.0 M:0.5455 L:0.4545 (mostly_collaborator) | unknown | SIGCOMM_heavy | SIGCOMM:10; NSDI:1 | [] |
| Georg Carle | 10 | 9 | 2 | 0.278 | decreased | 97 | 59 | 0.76 | flat | continuous | F:0.0 M:0.1546 L:0.8454 (mostly_senior) | F:0.0 M:0.1207 L:0.8793 (mostly_senior) | F:0.0 M:0.2222 L:0.7778 (mostly_senior) | F:0.0 M:0.0 L:1.0 (mostly_senior) | IMC_heavy | IMC:6; CoNEXT:2; SIGCOMM:1 | PACMNET:1; IMC:1 |
| Feng Qian 0001 | 10 | 10 | 13 | 1.625 | increased | 58 | 46 | 0.991 | flat | continuous | F:0.0517 M:0.7414 L:0.2069 (mostly_collaborator) | F:0.0 M:0.8 L:0.2 (mostly_collaborator) | F:0.0 M:0.8 L:0.2 (mostly_collaborator) | F:0.0 M:0.8333 L:0.1667 (mostly_collaborator) | mixed_3plus | SIGCOMM:4; CoNEXT:2; IMC:2; NSDI:2 | NSDI:6; SIGCOMM:5; IMC:1; PACMNET:1 |
| Dave Levin | 10 | 9 | 4 | 0.556 | decreased | 30 | 15 | 0.625 | decreased | continuous | F:0.0333 M:0.4333 L:0.5667 (mostly_senior) | F:0.0 M:0.6 L:0.4 (mostly_collaborator) | F:0.0 M:0.7778 L:0.2222 (mostly_collaborator) | F:0.0 M:0.75 L:0.25 (mostly_collaborator) | mixed_2 | SIGCOMM:5; IMC:4 | SIGCOMM:3; HotNets:1 |
| Ramesh Govindan | 10 | 10 | 9 | 1.125 | flat | 28 | 16 | 0.714 | decreased | continuous | F:0.0357 M:0.4286 L:0.5714 (mostly_senior) | F:0.0 M:0.625 L:0.375 (mostly_collaborator) | F:0.0 M:0.5 L:0.5 (mostly_senior) | F:0.0 M:0.8889 L:0.1111 (mostly_collaborator) | mixed_3plus | SIGCOMM:4; NSDI:3; CoNEXT:2; IMC:1 | NSDI:4; SIGCOMM:3; HotNets:1; IMC:1 |
| Stefan Savage | 10 | 10 | 4 | 0.5 | decreased | 25 | 15 | 0.75 | decreased | continuous | F:0.08 M:0.72 L:0.24 (mostly_collaborator) | F:0.0 M:0.6667 L:0.3333 (mostly_collaborator) | F:0.0 M:0.7 L:0.3 (mostly_collaborator) | F:0.0 M:0.75 L:0.25 (mostly_collaborator) | IMC_heavy | IMC:10 | IMC:4 |
| Manya Ghobadi | 10 | 10 | 8 | 1.0 | flat | 25 | 13 | 0.65 | decreased | continuous | F:0.04 M:0.72 L:0.28 (mostly_collaborator) | F:0.0 M:0.5385 L:0.4615 (mostly_collaborator) | F:0.0 M:0.7 L:0.3 (mostly_collaborator) | F:0.0 M:0.375 L:0.625 (mostly_senior) | SIGCOMM_heavy | SIGCOMM:6; HotNets:2; NSDI:2 | HotNets:3; NSDI:3; SIGCOMM:2 |
| David R. Choffnes | 10 | 10 | 6 | 0.75 | decreased | 24 | 13 | 0.677 | decreased | continuous | F:0.0 M:0.7083 L:0.2917 (mostly_collaborator) | F:0.0 M:0.6923 L:0.3077 (mostly_collaborator) | F:0.0 M:0.7 L:0.3 (mostly_collaborator) | F:0.0 M:0.6667 L:0.3333 (mostly_collaborator) | IMC_heavy | IMC:8; SIGCOMM:2 | IMC:6 |
| Vincent Liu 0001 | 10 | 10 | 10 | 1.25 | increased | 18 | 17 | 1.181 | flat | continuous | F:0.0 M:0.5556 L:0.4444 (mostly_collaborator) | F:0.0 M:0.5882 L:0.4118 (mostly_collaborator) | F:0.0 M:0.4 L:0.6 (mostly_senior) | F:0.0 M:0.8 L:0.2 (mostly_collaborator) | SIGCOMM_heavy | SIGCOMM:6; HotNets:2; NSDI:2 | NSDI:5; SIGCOMM:4; HotNets:1 |
| Philip Brighten Godfrey | 10 | 10 | 12 | 1.5 | increased | 18 | 18 | 1.25 | increased | continuous | F:0.0 M:0.7778 L:0.2222 (mostly_collaborator) | F:0.0 M:0.8824 L:0.1176 (mostly_collaborator) | F:0.0 M:0.8 L:0.2 (mostly_collaborator) | F:0.0 M:1.0 L:0.0 (mostly_collaborator) | mixed_3plus | HotNets:5; NSDI:3; CoNEXT:1; SIGCOMM:1 | NSDI:5; HotNets:4; SIGCOMM:2; PACMNET:1 |
| Alan Mislove | 10 | 9 | 2 | 0.278 | decreased | 28 | 3 | 0.134 | decreased | continuous | F:0.0 M:0.5714 L:0.4286 (mostly_collaborator) | F:0.3333 M:0.6667 L:0.3333 (mostly_collaborator) | F:0.0 M:0.5556 L:0.4444 (mostly_collaborator) | F:0.5 M:0.5 L:0.5 (mostly_lead) | IMC_heavy | IMC:6; SIGCOMM:2; HotNets:1 | IMC:2 |
| Oliver Gasser | 10 | 10 | 7 | 0.875 | flat | 15 | 16 | 1.333 | increased | continuous | F:0.1333 M:0.8667 L:0.0 (mostly_collaborator) | F:0.0 M:0.4286 L:0.5714 (mostly_senior) | F:0.1 M:0.9 L:0.0 (mostly_collaborator) | F:0.0 M:0.6 L:0.4 (mostly_collaborator) | IMC_heavy | IMC:9; CoNEXT:1 | IMC:5; PACMNET:2 |
| Ankit Singla | 10 | 10 | 1 | 0.125 | decreased | 25 | 1 | 0.05 | decreased | sporadic_post | F:0.0 M:0.32 L:0.68 (mostly_senior) | F:0.0 M:1.0 L:0.0 (mostly_collaborator) | F:0.0 M:0.2 L:0.8 (mostly_senior) | F:0.0 M:1.0 L:0.0 (mostly_collaborator) | mixed_3plus | HotNets:4; NSDI:2; IMC:2; CoNEXT:1; SIGCOMM:1 | SIGCOMM:1 |
| Behnaz Arzani | 10 | 10 | 10 | 1.25 | increased | 12 | 11 | 1.146 | flat | continuous | F:0.25 M:0.6667 L:0.0833 (mostly_collaborator) | F:0.0909 M:0.5455 L:0.3636 (mostly_collaborator) | F:0.3 M:0.6 L:0.1 (mostly_collaborator) | F:0.1 M:0.5 L:0.4 (mostly_collaborator) | mixed_3plus | NSDI:4; HotNets:3; SIGCOMM:2; IMC:1 | NSDI:5; HotNets:3; SIGCOMM:2 |
| Gareth Tyson | 9 | 9 | 7 | 0.972 | flat | 61 | 61 | 1.25 | increased | continuous | F:0.0 M:0.5902 L:0.4098 (mostly_collaborator) | F:0.0 M:0.5082 L:0.4918 (mostly_collaborator) | F:0.0 M:0.6667 L:0.3333 (mostly_collaborator) | F:0.0 M:0.2857 L:0.7143 (mostly_senior) | IMC_heavy | IMC:6; SIGCOMM:2; CoNEXT:1 | IMC:6; NSDI:1 |
| Thomas C. Schmidt | 9 | 9 | 4 | 0.556 | decreased | 69 | 27 | 0.489 | decreased | continuous | F:0.0 M:0.8261 L:0.1739 (mostly_collaborator) | F:0.0 M:0.5385 L:0.4615 (mostly_collaborator) | F:0.0 M:1.0 L:0.0 (mostly_collaborator) | F:0.0 M:1.0 L:0.0 (mostly_collaborator) | IMC_heavy | IMC:6; CoNEXT:3 | IMC:2; PACMNET:1; SIGCOMM:1 |
| Matthias Wählisch | 9 | 9 | 5 | 0.694 | decreased | 56 | 19 | 0.424 | decreased | continuous | F:0.0 M:0.0179 L:0.9821 (mostly_senior) | F:0.0 M:0.0556 L:0.9444 (mostly_senior) | F:0.0 M:0.0 L:1.0 (mostly_senior) | F:0.0 M:0.25 L:0.75 (mostly_senior) | IMC_heavy | IMC:6; CoNEXT:3 | IMC:3; PACMNET:1; SIGCOMM:1 |
| Oliver Hohlfeld | 9 | 9 | 6 | 0.833 | flat | 47 | 17 | 0.452 | decreased | continuous | F:0.1064 M:0.4468 L:0.4681 (mixed) | F:0.0 M:0.4118 L:0.5882 (mostly_senior) | F:0.0 M:0.5556 L:0.4444 (mostly_collaborator) | F:0.0 M:0.1667 L:0.8333 (mostly_senior) | IMC_heavy | IMC:6; CoNEXT:2; SIGCOMM:1 | IMC:4; SIGCOMM:1; HotNets:1 |
| Ennan Zhai | 9 | 9 | 27 | 3.75 | increased | 19 | 36 | 2.368 | increased | continuous | F:0.0526 M:0.7895 L:0.1579 (mostly_collaborator) | F:0.0 M:0.6111 L:0.3889 (mostly_collaborator) | F:0.1111 M:0.8889 L:0.0 (mostly_collaborator) | F:0.0 M:0.4815 L:0.5185 (mostly_senior) | SIGCOMM_heavy | SIGCOMM:7; NSDI:2 | SIGCOMM:14; NSDI:13 |
| Kyle Jamieson | 9 | 9 | 6 | 0.833 | flat | 26 | 22 | 1.058 | flat | continuous | F:0.0385 M:0.2308 L:0.7692 (mostly_senior) | F:0.0 M:0.381 L:0.619 (mostly_senior) | F:0.0 M:0.2222 L:0.7778 (mostly_senior) | F:0.0 M:0.6 L:0.4 (mostly_collaborator) | mixed_3plus | SIGCOMM:4; NSDI:3; HotNets:2 | NSDI:3; HotNets:1; PACMNET:1; IMC:1 |
| Zakir Durumeric | 9 | 9 | 7 | 0.972 | flat | 19 | 23 | 1.513 | increased | continuous | F:0.0 M:0.3684 L:0.6316 (mostly_senior) | F:0.087 M:0.1304 L:0.7826 (mostly_senior) | F:0.0 M:0.2222 L:0.7778 (mostly_senior) | F:0.2857 M:0.1429 L:0.5714 (mostly_senior) | IMC_heavy | IMC:7; SIGCOMM:2 | IMC:3; NSDI:2; SIGCOMM:2 |
| Yibo Zhu 0001 | 9 | 9 | 4 | 0.556 | decreased | 17 | 14 | 1.029 | flat | continuous | F:0.0 M:0.9412 L:0.0588 (mostly_collaborator) | F:0.0 M:0.9231 L:0.0769 (mostly_collaborator) | F:0.0 M:1.0 L:0.0 (mostly_collaborator) | F:0.0 M:1.0 L:0.0 (mostly_collaborator) | mixed_3plus | NSDI:5; SIGCOMM:3; HotNets:1 | NSDI:2; SIGCOMM:2 |
| Anirudh Sivaraman | 9 | 9 | 6 | 0.833 | flat | 17 | 12 | 0.882 | flat | continuous | F:0.0 M:0.6471 L:0.3529 (mostly_collaborator) | F:0.0 M:0.4167 L:0.5833 (mostly_senior) | F:0.0 M:0.5556 L:0.4444 (mostly_collaborator) | F:0.0 M:0.3333 L:0.6667 (mostly_senior) | mixed_3plus | NSDI:4; HotNets:2; SIGCOMM:2; CoNEXT:1 | SIGCOMM:3; HotNets:2; NSDI:1 |
| Matthew Luckie | 9 | 8 | 4 | 0.625 | decreased | 19 | 9 | 0.592 | decreased | continuous | F:0.2632 M:0.7368 L:0.0 (mostly_collaborator) | F:0.2222 M:0.5556 L:0.2222 (mostly_collaborator) | F:0.375 M:0.625 L:0.0 (mostly_collaborator) | F:0.25 M:0.75 L:0.0 (mostly_collaborator) | IMC_heavy | IMC:5; CoNEXT:2; SIGCOMM:1 | IMC:4 |
| Balakrishnan Chandrasekaran 0002 | 9 | 9 | 4 | 0.556 | decreased | 17 | 11 | 0.809 | flat | continuous | F:0.0 M:0.9412 L:0.0588 (mostly_collaborator) | F:0.0 M:1.0 L:0.0 (mostly_collaborator) | F:0.0 M:1.0 L:0.0 (mostly_collaborator) | F:0.0 M:1.0 L:0.0 (mostly_collaborator) | mixed_3plus | IMC:5; HotNets:1; CoNEXT:1; SIGCOMM:1; NSDI:1 | NSDI:3; HotNets:1 |
| Ran Ben Basat | 8 | 8 | 7 | 1.094 | flat | 41 | 12 | 0.366 | decreased | continuous | F:0.6829 M:0.2927 L:0.0244 (mostly_lead) | F:0.2727 M:0.5455 L:0.1818 (mostly_collaborator) | F:0.5 M:0.5 L:0.0 (mostly_lead) | F:0.0 M:0.6667 L:0.3333 (mostly_collaborator) | mixed_3plus | CoNEXT:4; SIGCOMM:2; IMC:1; HotNets:1 | SIGCOMM:2; HotNets:2; NSDI:2; PACMNET:1 |
| Roland van Rijswijk-Deij | 8 | 8 | 1 | 0.156 | decreased | 33 | 16 | 0.606 | decreased | continuous | F:0.0303 M:0.7273 L:0.2424 (mostly_collaborator) | F:0.0 M:0.5 L:0.5 (mostly_senior) | F:0.0 M:0.75 L:0.25 (mostly_collaborator) | F:0.0 M:0.0 L:1.0 (mostly_senior) | IMC_heavy | IMC:7; CoNEXT:1 | IMC:1 |
| Matteo Varvello | 8 | 8 | 10 | 1.562 | increased | 29 | 20 | 0.862 | flat | continuous | F:0.2069 M:0.5862 L:0.2069 (mostly_collaborator) | F:0.1053 M:0.7895 L:0.1053 (mostly_collaborator) | F:0.25 M:0.5 L:0.25 (mostly_collaborator) | F:0.0 M:1.0 L:0.0 (mostly_collaborator) | mixed_3plus | IMC:4; CoNEXT:3; HotNets:1 | IMC:8; PACMNET:1; SIGCOMM:1 |
| Mosharaf Chowdhury | 8 | 8 | 5 | 0.781 | flat | 24 | 21 | 1.094 | flat | continuous | F:0.0417 M:0.5417 L:0.4167 (mostly_collaborator) | F:0.0 M:0.4286 L:0.5714 (mostly_senior) | F:0.0 M:0.625 L:0.375 (mostly_collaborator) | F:0.0 M:0.4 L:0.6 (mostly_senior) | NSDI_heavy | NSDI:5; SIGCOMM:3 | NSDI:3; HotNets:2 |
| Aurojit Panda | 8 | 8 | 7 | 1.094 | flat | 24 | 21 | 1.094 | flat | continuous | F:0.0 M:0.9167 L:0.0833 (mostly_collaborator) | F:0.0 M:0.8571 L:0.1429 (mostly_collaborator) | F:0.0 M:0.875 L:0.125 (mostly_collaborator) | F:0.0 M:0.8571 L:0.1429 (mostly_collaborator) | mixed_3plus | SIGCOMM:3; HotNets:3; NSDI:2 | HotNets:5; SIGCOMM:1; NSDI:1 |
| Ying Zhang 0022 | 8 | 8 | 23 | 3.594 | increased | 16 | 29 | 2.266 | increased | continuous | F:0.0 M:0.375 L:0.625 (mostly_senior) | F:0.0 M:0.7143 L:0.2857 (mostly_collaborator) | F:0.0 M:0.5 L:0.5 (mostly_senior) | F:0.0 M:0.6818 L:0.3182 (mostly_collaborator) | SIGCOMM_heavy | SIGCOMM:6; NSDI:2 | SIGCOMM:12; NSDI:7; IMC:2; PACMNET:1; HotNets:1 |
| Ítalo Cunha | 8 | 8 | 3 | 0.469 | decreased | 33 | 6 | 0.227 | decreased | intermittent_post | F:0.0 M:0.9091 L:0.0909 (mostly_collaborator) | F:0.0 M:0.8333 L:0.1667 (mostly_collaborator) | F:0.0 M:1.0 L:0.0 (mostly_collaborator) | F:0.0 M:0.6667 L:0.3333 (mostly_collaborator) | IMC_heavy | IMC:6; CoNEXT:1; HotNets:1 | IMC:3 |
| Haitham Hassanieh | 8 | 8 | 6 | 0.938 | flat | 22 | 15 | 0.852 | flat | continuous | F:0.0909 M:0.5 L:0.4545 (mostly_collaborator) | F:0.0 M:0.3333 L:0.6667 (mostly_senior) | F:0.125 M:0.375 L:0.5 (mostly_senior) | F:0.0 M:0.5 L:0.5 (mostly_senior) | NSDI_heavy | NSDI:6; SIGCOMM:2 | NSDI:3; HotNets:2; SIGCOMM:1 |
| Fadel Adib | 8 | 8 | 5 | 0.781 | flat | 16 | 20 | 1.562 | increased | continuous | F:0.0 M:0.125 L:0.875 (mostly_senior) | F:0.0 M:0.1 L:0.9 (mostly_senior) | F:0.0 M:0.0 L:1.0 (mostly_senior) | F:0.0 M:0.0 L:1.0 (mostly_senior) | mixed_3plus | SIGCOMM:4; HotNets:2; NSDI:2 | SIGCOMM:4; NSDI:1 |
| Robert Soulé | 8 | 8 | 0 | 0.0 | inactive_after_2022 | 25 | 10 | 0.5 | decreased | continuous | F:0.0 M:0.44 L:0.56 (mostly_senior) | F:0.1 M:0.5 L:0.4 (mostly_collaborator) | F:0.0 M:0.5 L:0.5 (mostly_senior) | unknown | mixed_3plus | NSDI:3; HotNets:2; CoNEXT:2; SIGCOMM:1 | [] |
| Olivier Bonaventure | 8 | 8 | 2 | 0.312 | decreased | 29 | 7 | 0.302 | decreased | continuous | F:0.0345 M:0.1034 L:0.8966 (mostly_senior) | F:0.0 M:0.0 L:1.0 (mostly_senior) | F:0.0 M:0.25 L:0.75 (mostly_senior) | F:0.0 M:0.0 L:1.0 (mostly_senior) | mixed_3plus | CoNEXT:3; HotNets:2; IMC:2; SIGCOMM:1 | NSDI:1; PACMNET:1 |
| Nate Foster | 8 | 8 | 3 | 0.469 | decreased | 23 | 7 | 0.38 | decreased | continuous | F:0.0435 M:0.7391 L:0.2609 (mostly_collaborator) | F:0.0 M:0.4286 L:0.5714 (mostly_senior) | F:0.0 M:0.625 L:0.375 (mostly_collaborator) | F:0.0 M:0.0 L:1.0 (mostly_senior) | mixed_3plus | NSDI:3; SIGCOMM:3; HotNets:1; CoNEXT:1 | SIGCOMM:2; HotNets:1 |
| Harsha V. Madhyastha | 8 | 8 | 7 | 1.094 | flat | 18 | 9 | 0.625 | decreased | continuous | F:0.0556 M:0.5556 L:0.3889 (mostly_collaborator) | F:0.0 M:0.3333 L:0.6667 (mostly_senior) | F:0.0 M:0.625 L:0.375 (mostly_collaborator) | F:0.0 M:0.2857 L:0.7143 (mostly_senior) | mixed_3plus | NSDI:4; HotNets:2; IMC:2 | IMC:3; NSDI:3; SIGCOMM:1 |
| Daehyeok Kim | 8 | 8 | 7 | 1.094 | flat | 11 | 16 | 1.818 | increased | continuous | F:0.4545 M:0.5455 L:0.0 (mostly_collaborator) | F:0.0625 M:0.8125 L:0.125 (mostly_collaborator) | F:0.625 M:0.375 L:0.0 (mostly_lead) | F:0.1429 M:0.5714 L:0.2857 (mostly_collaborator) | mixed_3plus | NSDI:4; SIGCOMM:3; HotNets:1 | NSDI:4; HotNets:2; SIGCOMM:1 |
| Aaron Schulman | 8 | 8 | 0 | 0.0 | inactive_after_2022 | 17 | 8 | 0.588 | decreased | continuous | F:0.0 M:0.4706 L:0.5294 (mostly_senior) | F:0.0 M:0.25 L:0.75 (mostly_senior) | F:0.0 M:0.5 L:0.5 (mostly_senior) | unknown | IMC_heavy | IMC:6; NSDI:1; SIGCOMM:1 | [] |
| Srinivas Narayana | 8 | 8 | 5 | 0.781 | flat | 12 | 12 | 1.25 | increased | continuous | F:0.0 M:0.8333 L:0.1667 (mostly_collaborator) | F:0.0 M:0.8182 L:0.1818 (mostly_collaborator) | F:0.0 M:0.75 L:0.25 (mostly_collaborator) | F:0.0 M:0.75 L:0.25 (mostly_collaborator) | mixed_3plus | SIGCOMM:4; HotNets:3; NSDI:1 | SIGCOMM:2; HotNets:1; NSDI:1; PACMNET:1 |
| John Sonchack | 8 | 8 | 0 | 0.0 | inactive_after_2022 | 15 | 2 | 0.167 | decreased | intermittent_post | F:0.2 M:0.8 L:0.0 (mostly_collaborator) | F:0.0 M:1.0 L:0.0 (mostly_collaborator) | F:0.125 M:0.875 L:0.0 (mostly_collaborator) | unknown | mixed_3plus | SIGCOMM:4; NSDI:3; CoNEXT:1 | [] |
| Robert Beverly | 8 | 8 | 1 | 0.156 | decreased | 12 | 3 | 0.312 | decreased | intermittent_post | F:0.0833 M:0.6667 L:0.25 (mostly_collaborator) | F:0.3333 M:0.3333 L:0.3333 (mixed) | F:0.125 M:0.75 L:0.125 (mostly_collaborator) | F:0.0 M:1.0 L:0.0 (mostly_collaborator) | IMC_heavy | IMC:6; CoNEXT:1; NSDI:1 | IMC:1 |
| Kai Chen 0005 | 7 | 7 | 13 | 2.321 | increased | 41 | 53 | 1.616 | increased | continuous | F:0.0 M:0.561 L:0.439 (mostly_collaborator) | F:0.0 M:0.283 L:0.717 (mostly_senior) | F:0.0 M:0.4286 L:0.5714 (mostly_senior) | F:0.0 M:0.3077 L:0.6923 (mostly_senior) | mixed_3plus | SIGCOMM:3; NSDI:2; CoNEXT:2 | NSDI:8; SIGCOMM:5 |
| Jianping Wu | 7 | 7 | 6 | 1.071 | flat | 50 | 34 | 0.85 | flat | continuous | F:0.06 M:0.24 L:0.7 (mostly_senior) | F:0.0294 M:0.4118 L:0.5882 (mostly_senior) | F:0.0 M:0.4286 L:0.5714 (mostly_senior) | F:0.0 M:0.5 L:0.5 (mostly_senior) | mixed_3plus | CoNEXT:2; IMC:2; HotNets:1; NSDI:1; SIGCOMM:1 | NSDI:3; SIGCOMM:3 |
| Zaoxing Liu | 7 | 7 | 10 | 1.786 | increased | 20 | 19 | 1.188 | flat | continuous | F:0.3 M:0.65 L:0.05 (mostly_collaborator) | F:0.0 M:0.4211 L:0.5789 (mostly_senior) | F:0.1429 M:0.7143 L:0.1429 (mostly_collaborator) | F:0.0 M:0.4 L:0.6 (mostly_senior) | mixed_3plus | SIGCOMM:3; NSDI:2; CoNEXT:1; IMC:1 | NSDI:4; HotNets:2; SIGCOMM:2; IMC:2 |
| Jiaqi Gao | 7 | 7 | 10 | 1.786 | increased | 18 | 21 | 1.458 | increased | continuous | F:0.1667 M:0.7778 L:0.0556 (mostly_collaborator) | F:0.15 M:0.8 L:0.05 (mostly_collaborator) | F:0.2857 M:0.7143 L:0.0 (mostly_collaborator) | F:0.1111 M:0.8889 L:0.0 (mostly_collaborator) | SIGCOMM_heavy | SIGCOMM:6; NSDI:1 | SIGCOMM:6; NSDI:3; PACMNET:1 |
| Dongsu Han | 7 | 6 | 5 | 1.042 | flat | 19 | 18 | 1.184 | flat | continuous | F:0.0 M:0.2632 L:0.7368 (mostly_senior) | F:0.0 M:0.2778 L:0.7222 (mostly_senior) | F:0.0 M:0.1667 L:0.8333 (mostly_senior) | F:0.0 M:0.6 L:0.4 (mostly_collaborator) | CoNEXT_heavy | CoNEXT:4; SIGCOMM:2 | SIGCOMM:3; HotNets:2 |
| Deepak Vasisht | 7 | 7 | 6 | 1.071 | flat | 15 | 21 | 1.75 | increased | continuous | F:0.2 M:0.4667 L:0.3333 (mixed) | F:0.0 M:0.4286 L:0.5714 (mostly_senior) | F:0.4286 M:0.4286 L:0.1429 (mixed) | F:0.0 M:0.3333 L:0.6667 (mostly_senior) | mixed_3plus | SIGCOMM:3; NSDI:2; CoNEXT:1; HotNets:1 | NSDI:3; SIGCOMM:2; HotNets:1 |
| John S. Heidemann | 7 | 7 | 4 | 0.714 | decreased | 22 | 13 | 0.739 | decreased | continuous | F:0.0 M:0.3182 L:0.6818 (mostly_senior) | F:0.0 M:0.3077 L:0.6923 (mostly_senior) | F:0.0 M:0.5714 L:0.4286 (mostly_collaborator) | F:0.0 M:0.0 L:1.0 (mostly_senior) | IMC_heavy | IMC:6; SIGCOMM:1 | IMC:4 |
| Yu Zhou 0008 | 7 | 7 | 2 | 0.357 | decreased | 27 | 2 | 0.093 | decreased | intermittent_post | F:0.2222 M:0.7407 L:0.037 (mostly_collaborator) | F:0.0 M:1.0 L:0.0 (mostly_collaborator) | F:0.4286 M:0.5714 L:0.0 (mostly_collaborator) | F:0.0 M:1.0 L:0.0 (mostly_collaborator) | mixed_3plus | SIGCOMM:4; CoNEXT:2; NSDI:1 | NSDI:1; SIGCOMM:1 |
| Ihsan Ayyub Qazi | 7 | 7 | 2 | 0.357 | decreased | 13 | 15 | 1.442 | increased | continuous | F:0.0769 M:0.6923 L:0.2308 (mostly_collaborator) | F:0.0 M:0.7333 L:0.2667 (mostly_collaborator) | F:0.1429 M:0.7143 L:0.1429 (mostly_collaborator) | F:0.0 M:0.5 L:0.5 (mostly_senior) | mixed_3plus | CoNEXT:4; SIGCOMM:1; HotNets:1; IMC:1 | SIGCOMM:1; IMC:1 |
| David Walker 0001 | 7 | 7 | 5 | 0.893 | flat | 15 | 7 | 0.583 | decreased | continuous | F:0.0 M:0.1333 L:0.8667 (mostly_senior) | F:0.0 M:0.4286 L:0.5714 (mostly_senior) | F:0.0 M:0.2857 L:0.7143 (mostly_senior) | F:0.0 M:0.6 L:0.4 (mostly_collaborator) | mixed_3plus | SIGCOMM:3; NSDI:3; HotNets:1 | NSDI:3; HotNets:1; SIGCOMM:1 |
| Vasileios Giotsas | 7 | 7 | 3 | 0.536 | decreased | 15 | 5 | 0.417 | decreased | intermittent_post | F:0.2 M:0.6667 L:0.2 (mostly_collaborator) | F:0.0 M:0.8 L:0.2 (mostly_collaborator) | F:0.1429 M:0.7143 L:0.1429 (mostly_collaborator) | F:0.0 M:1.0 L:0.0 (mostly_collaborator) | IMC_heavy | IMC:5; NSDI:1; SIGCOMM:1 | IMC:3 |
| Bradley Huffaker | 7 | 7 | 2 | 0.357 | decreased | 13 | 7 | 0.673 | decreased | continuous | F:0.0 M:1.0 L:0.0 (mostly_collaborator) | F:0.1429 M:0.8571 L:0.0 (mostly_collaborator) | F:0.0 M:1.0 L:0.0 (mostly_collaborator) | F:0.5 M:0.5 L:0.0 (mostly_lead) | IMC_heavy | IMC:5; CoNEXT:2 | IMC:2 |
| Venkat Arun | 7 | 7 | 7 | 1.25 | increased | 10 | 8 | 1.0 | flat | continuous | F:0.6 M:0.4 L:0.0 (mostly_lead) | F:0.125 M:0.75 L:0.125 (mostly_collaborator) | F:0.5714 M:0.4286 L:0.0 (mostly_lead) | F:0.1429 M:0.7143 L:0.1429 (mostly_collaborator) | mixed_3plus | NSDI:3; SIGCOMM:2; HotNets:2 | NSDI:5; HotNets:2 |
| Ali Abedi 0002 | 7 | 7 | 2 | 0.357 | decreased | 13 | 5 | 0.481 | decreased | intermittent_post | F:0.5385 M:0.3846 L:0.0769 (mostly_lead) | F:0.6 M:0.4 L:0.0 (mostly_lead) | F:0.7143 M:0.2857 L:0.0 (mostly_lead) | F:1.0 M:0.0 L:0.0 (mostly_lead) | HotNets_heavy | HotNets:5; SIGCOMM:2 | HotNets:2 |
| Prateesh Goyal | 7 | 7 | 4 | 0.714 | decreased | 12 | 5 | 0.521 | decreased | continuous | F:0.5833 M:0.4167 L:0.0 (mostly_lead) | F:0.0 M:1.0 L:0.0 (mostly_collaborator) | F:0.5714 M:0.4286 L:0.0 (mostly_lead) | F:0.0 M:1.0 L:0.0 (mostly_collaborator) | mixed_3plus | SIGCOMM:4; NSDI:2; HotNets:1 | SIGCOMM:3; NSDI:1 |
| Bruce M. Maggs | 7 | 7 | 2 | 0.357 | decreased | 14 | 3 | 0.268 | decreased | intermittent_post | F:0.0 M:0.8571 L:0.1429 (mostly_collaborator) | F:0.0 M:0.6667 L:0.3333 (mostly_collaborator) | F:0.0 M:0.8571 L:0.1429 (mostly_collaborator) | F:0.0 M:0.5 L:0.5 (mostly_senior) | mixed_3plus | IMC:4; HotNets:1; SIGCOMM:1; NSDI:1 | HotNets:1; NSDI:1 |
| Ingmar Poese | 7 | 7 | 2 | 0.357 | decreased | 9 | 6 | 0.833 | flat | intermittent_post | F:0.0 M:0.8889 L:0.1111 (mostly_collaborator) | F:0.0 M:0.8333 L:0.1667 (mostly_collaborator) | F:0.0 M:1.0 L:0.0 (mostly_collaborator) | F:0.0 M:1.0 L:0.0 (mostly_collaborator) | mixed_3plus | IMC:4; CoNEXT:2; NSDI:1 | NSDI:1; SIGCOMM:1 |
| Debopam Bhattacherjee | 7 | 7 | 4 | 0.714 | decreased | 8 | 8 | 1.25 | increased | continuous | F:0.75 M:0.25 L:0.0 (mostly_lead) | F:0.0 M:0.4286 L:0.5714 (mostly_senior) | F:0.7143 M:0.2857 L:0.0 (mostly_lead) | F:0.0 M:0.6667 L:0.3333 (mostly_collaborator) | mixed_3plus | HotNets:3; IMC:2; CoNEXT:1; NSDI:1 | HotNets:2; IMC:1; PACMNET:1 |
| Christoph Dietzel | 7 | 7 | 0 | 0.0 | inactive_after_2022 | 14 | 0 | 0.0 | inactive_after_2022 | inactive_after_2022 | F:0.0714 M:0.8571 L:0.0714 (mostly_collaborator) | unknown | F:0.1429 M:0.7143 L:0.1429 (mostly_collaborator) | unknown | mixed_3plus | IMC:4; CoNEXT:2; SIGCOMM:1 | [] |
| Stefano Vissicchio | 7 | 7 | 3 | 0.536 | decreased | 7 | 3 | 0.536 | decreased | continuous | F:0.0 M:0.8571 L:0.1429 (mostly_collaborator) | F:0.0 M:0.6667 L:0.3333 (mostly_collaborator) | F:0.0 M:0.8571 L:0.1429 (mostly_collaborator) | F:0.0 M:0.6667 L:0.3333 (mostly_collaborator) | mixed_3plus | HotNets:2; NSDI:2; SIGCOMM:2; CoNEXT:1 | SIGCOMM:2; NSDI:1 |
