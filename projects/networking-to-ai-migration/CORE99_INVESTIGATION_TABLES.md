# Core-99 Investigation Tables

Deterministic tables for the first three investigation questions. No LLM interpretation is used here.

## Question 1: Top-Net Decrease, Overall Flat/Increase

- Researchers in slice: 15
- Slice rule: `top_networking_rate_change = decreased` and `clean_publication_rate_change in {flat, increased}`.

### Aggregate Venue-Family Shift

- Baseline families: qualifying_top_networking (160), other_networking (115), theory_distributed (39), systems (30), security_privacy (24), mobile_wireless_iot (16), AI_ML (6), programming_languages (4), web_social_hci (4), unknown (3)
- Post-2023 families: other_networking (92), qualifying_top_networking (72), theory_distributed (38), systems (37), security_privacy (21), web_social_hci (16), mobile_wireless_iot (13), AI_ML (9), programming_languages (3), data_management (1)

Top post-2023 venues in this slice:

| Venue | Papers |
|---|---:|
| NSDI | 25 |
| IMC | 23 |
| SIGCOMM | 16 |
| TMA | 12 |
| PAM | 11 |
| ANRW | 9 |
| HotNets | 8 |
| INFOCOM | 8 |
| OPODIS | 7 |
| IFIP Networking | 6 |
| SIGCOMM Posters and Demos | 5 |
| USENIX Security | 5 |
| SPAA | 5 |
| WWW | 5 |
| MobiCom | 5 |

## Question 2: Top-Net Flat/Increase Profiles

- Researchers in slice: 44
- Slice rule: `top_networking_rate_change in {flat, increased}`.

### Profile Distributions

#### Top-net trend

| Label | Researchers |
|---|---:|
| flat | 28 |
| increased | 16 |

#### Qualifying venue mix

| Label | Researchers |
|---|---:|
| mixed_3plus | 26 |
| IMC_heavy | 6 |
| SIGCOMM_heavy | 6 |
| NSDI_heavy | 4 |
| mixed_2 | 1 |
| CoNEXT_heavy | 1 |

#### Baseline author role

| Label | Researchers |
|---|---:|
| mostly_collaborator | 25 |
| mostly_senior | 14 |
| mixed | 3 |
| mostly_lead | 2 |

#### Post-2023 author role

| Label | Researchers |
|---|---:|
| mostly_collaborator | 22 |
| mostly_senior | 22 |

#### Region

| Label | Researchers |
|---|---:|
| US | 23 |
| China | 7 |
| Unknown | 6 |
| Europe | 6 |
| Other | 2 |

#### Sector

| Label | Researchers |
|---|---:|
| Unknown | 44 |

## Question 3: Baseline Top-Venue Author Concentration

Computed from `data/raw_dblp_papers.json` for 2018-2022 accepted papers in the five qualifying venues.

| Venue | Papers | Unique authors | Repeat-author share >=2 | Gini | HHI | Core-99 paper share |
|---|---:|---:|---:|---:|---:|---:|
| SIGCOMM | 237 | 1098 | 0.2022 | 0.2363 | 0.0014 | 0.6582 |
| NSDI | 295 | 1343 | 0.1817 | 0.2045 | 0.0011 | 0.4915 |
| CoNEXT | 207 | 802 | 0.1546 | 0.1499 | 0.0016 | 0.3575 |
| HotNets | 139 | 487 | 0.1663 | 0.1859 | 0.0028 | 0.5755 |
| IMC | 268 | 847 | 0.2397 | 0.3089 | 0.0022 | 0.5224 |

## Output Files

- `data/core99_investigation_summary.json`
- `data/core99_researcher_venue_family_transitions.csv`
- `data/core99_topnet_decrease_clean_flat_or_increase.csv`
- `data/core99_topnet_flat_or_increase_profiles.csv`
- `data/top_venue_author_concentration_2018_2022.csv`
- `data/venue_family_map.json`
