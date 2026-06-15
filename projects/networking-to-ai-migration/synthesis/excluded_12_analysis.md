# Excluded-12 Analysis: Low Post-2023 Output Researchers

These 12 researchers are part of core-99 (≥7 top-networking papers during 2018-2022) but were excluded from feature-vector analysis because they have fewer than 5 clean post-2023 conference papers. Their percentage-based venue-family vectors would be unstable, but their substantive importance for the "what happened to top networking researchers?" question is high — they include some of the biggest names in the field.

This analysis uses deterministic attributes from `data/core99_researcher_attributes.json` to add context beyond the raw count table in CORE99_ANALYSIS.md §1.

## Categories

### 1. Complete Stop (0 post-2023 clean papers)

| Researcher | BL clean | BL top-net | Author role (BL) | Last known affiliation | Notes |
|-----------|:--------:|:----------:|:-----------------:|----------------------|-------|
| Ming Zhang 0005 | 12 | 11 | mostly_senior | Alibaba (China) | Industry researcher at Alibaba (Ming Zhang); he moved to Alibaba and stopped academic publishing. Industry exit — stopped publishing after moving to Alibaba. |
| Christoph Dietzel | 14 | 7 | mostly_collaborator | Max Planck Institute for Informatics | Completely inactive after 2022. May have left academia or moved to industry. |

Both are classified `inactive_after_2022` and have zero post-2023 papers at any venue. Ming Zhang 0005's identity has been verified: DBLP PID 73/1844-5 confirms he is a networking researcher who moved to Alibaba (China) and stopped academic publishing after 2022. This is a clean industry exit, not a DBLP identity error.

### 2. Near-Complete Stop, Likely Industry (1 post-2023 clean paper)

| Researcher | BL clean | BL top-net | Post top-net | Last known affiliation | Notes |
|-----------|:--------:|:----------:|:------------:|----------------------|-------|
| Ankit Singla | 25 | 10 | 0-top-net, 1-clean | Google (Switzerland) | At Google. One paper post-2023 (not at a qualifying venue since it shows as top-net=0). Career transition to industry. |

Ankit Singla is the clearest industry-exit case. His post-2023 paper is not at a qualifying networking venue.

### 3. Sharp Decline, Reduced Academic Output (2-3 post-2023 clean papers)

Eight researchers fall into this category. They still publish occasionally but at sharply reduced volume.

| Researcher | BL clean | BL top-net | Post clean | Post top-net | BL author role | Post author role | Likely affiliation | Notes |
|-----------|:--------:|:----------:|:----------:|:------------:|:---------------:|:-----------------:|-------------------|-------|
| Hongqiang Harry Liu | 21 | 20 | 3 | 2 (1 NSDI, 1 SIGCOMM) | mostly_collaborator | mostly_collaborator | Uber AI (US) | Industry researcher at Uber AI. Still publishes occasionally at SIGCOMM/NSDI. |
| Hari Balakrishnan | 29 | 11 | 4 | 2 (1 HotNets, 1 SIGCOMM) | mostly_senior | mostly_senior | MIT (listed as Univ. of Kerala — DBLP disambiguation error for MIT CSAIL researcher) | Senior professor, reduced conference output. Has 1 CVPR paper post-2023 — possible research direction broadening. The "University of Kerala" affiliation in the data is clearly a DBLP identity error. |
| Alan Mislove | 28 | 9 | 3 | 2 (2 IMC) | mostly_collaborator | mostly_collaborator | Northeastern University | Reduced output. Post-2023 papers at IMC and USENIX Security — still networking/security focused. |
| John Sonchack | 15 | 8 | 2 | 0 | mostly_collaborator | mostly_collaborator | Princeton University | No top-networking papers post-2023 at all. Post papers at OSDI and PADL — possible systems shift. |
| Matt Calder | 14 | 12 | 3 | 3 (2 IMC, 1 HotNets) | mostly_collaborator | mostly_collaborator | Meta (US) | Still 100% networking — just fewer papers. All 3 post papers at top networking venues. May be a data completeness issue (missing papers). |
| Yu Zhou 0008 | 27 | 7 | 2 | 2 (1 NSDI, 1 SIGCOMM) | mostly_collaborator | mostly_collaborator | National University of Singapore | Reduced output, still at top networking venues. |
| Robert Beverly | 12 | 8 | 3 | 1 (1 IMC) | mostly_collaborator | mixed | Lawrence Berkeley National Lab | Moved from Naval Postgraduate School to LBNL. Post papers at IMC, IEEE S&P, NDSS — security broadening. |
| Bruce M. Maggs | 14 | 7 | 3 | 2 (1 HotNets, 1 NSDI) | mostly_collaborator | mostly_collaborator | Duke University | Senior researcher (Emeritus at Duke, formerly Akamai VP). Reduced output consistent with career stage. |

### 4. Barely Under Threshold (3 papers, closest to inclusion)

| Researcher | BL clean | BL top-net | Post clean | Post top-net | BL author role | Post author role | Likely affiliation | Notes |
|-----------|:--------:|:----------:|:----------:|:------------:|:---------------:|:-----------------:|-------------------|-------|
| Stefano Vissicchio | 7 | 7 | 3 | 3 (2 SIGCOMM, 1 NSDI) | mostly_collaborator | mostly_collaborator | University College London | Only 7 baseline papers — was already the lowest-volume core-99 member by total clean count. His post-2023 is 100% qualifying top-networking (3/3 papers). With 1 more paper he would have been included. Should be flagged as a borderline exclusion — his concentration in top venues is high post-2023. |

## Aggregate Patterns

- **Industry exit**: At least 4 of 12 are clearly industry researchers: Hongqiang Harry Liu (Uber AI), Ankit Singla (Google), Ming Zhang 0005 (Alibaba — confirmed via DBLP PID 73/1844-5), and Matt Calder (Meta — confirmed via personal website). Industry publication norms differ from academia, and low conference output may not reflect research inactivity.
- **Senior career stage**: Hari Balakrishnan, Bruce M. Maggs, and possibly Alan Mislove are senior enough that reduced first-hand publishing is expected — they may be advising students who are lead authors.
- **Resolved data issues**: Ming Zhang 0005 confirmed as Alibaba researcher (not a DBLP collision — stopped publishing after industry move). Matt Calder confirmed at Meta. Hari Balakrishnan's DBLP affiliation ("University of Kerala") is still a known error.
- **Still networking**: Among those who do publish post-2023, most papers are still at networking venues (SIGCOMM, NSDI, IMC, HotNets). The decline is in volume, not in topic direction.
- **Only 3 of 12 have zero papers at all** (Ming Zhang 0005, Christoph Dietzel, possibly Ankit Singla with effectively 0). The other 9 are still publishing, just below the 5-paper threshold needed for stable percentage vectors.

## Implications for Core-99 Analysis

1. **The exclusion threshold hides industry transitions.** Ming Zhang 0005 (Alibaba), Ankit Singla (Google), Hongqiang Harry Liu (Uber AI), and Matt Calder (Meta) are industry researchers — they are not "leaving networking" as much as moving to industry research roles where conference publishing is deprioritized.

2. **The exclusion threshold also hides seniority effects.** Hari Balakrishnan's 29→4 paper drop looks dramatic, but as a senior professor he may be shifting to advisory/editorial roles while students lead papers.

3. **Stefano Vissicchio is a borderline case.** He should be treated as nearly-analyzable — his post-2023 papers are 100% at qualifying top-networking venues. His exclusion is purely a mechanical consequence of the <5 threshold, not a substantive difference from the analyzable group.

4. **These 12 accounted for 23% of baseline top-networking incidences** (160/906 from the §3.2 table — approximately). Their removal from the analyzable sample means the feature-vector analysis is based on researchers who remained *active enough to measure*, which systematically excludes the most extreme decline cases.

## Recommendation for Follow-Up

1. **Manual verification**: Ming Zhang 0005 confirmed as Alibaba researcher (DBLP PID 73/1844-5, stopped publishing after industry move). Hari Balakrishnan DBLP identity still needs correction.
2. **Career-stage annotation**: Add first-publication-year as a proxy for career stage, to test whether decline is age/experience-correlated.
3. **Industry flag**: Add an industry/academia flag for all 99 researchers (currently the `sector` field is "Unknown" for nearly all).
4. **Sensitivity run**: Include Stefano Vissicchio in the analyzable set (he has 3 post papers, all at qualifying venues) to test whether the borderline cases meaningfully affect group composition.
