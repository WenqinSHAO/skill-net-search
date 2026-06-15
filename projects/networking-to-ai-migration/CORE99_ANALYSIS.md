# Core-99 Analysis: From Static Profiles to Migration Questions

This is the primary narrative for the core-99 high-signal researcher slice. It should be read as a structured interpretation of already-built deterministic artifacts, not as a final migration taxonomy.

The analysis now follows one question-driven path:

1. define the measurement objects,
2. show the shallow aggregate movement with both percentages and paper counts,
3. split the movement into interpretable researcher groups,
4. use named researchers only as evidence-bearing examples,
5. keep PCA and delta plots as supporting views, not as the main story.

Detailed researcher tables and decompositions remain in [CORE99_INVESTIGATION.md](CORE99_INVESTIGATION.md). Per-researcher deterministic attributes are in [CORE99_RESEARCHER_ATTRIBUTES.md](CORE99_RESEARCHER_ATTRIBUTES.md).

## 1. Data Scope and Analysis Cohort

The core-99 is defined as researchers with `baseline_top_networking_count > 6`, meaning at least 7 papers at SIGCOMM, NSDI, CoNEXT, HotNets, or IMC during 2018-2022. This yields 99 researchers.

The feature-vector analysis uses a stricter stability threshold: at least 5 clean papers in both periods.

- Baseline period: 2018-2022.
- Post-baseline period: 2023-2026.
- Core sample: 99 researchers.
- Feature-vector analysis sample: 87 researchers.
- Excluded from feature-vector analysis: 12 researchers with fewer than 5 post-2023 clean papers.

Those 12 researchers are not discarded from the project. They remain part of core-99 and matter substantively, but their post-2023 percentage vectors are too unstable: with fewer than 5 papers, one paper can move a venue-family share by 20 percentage points or more.

| Researcher | Baseline papers | Post-2023 papers | Current interpretation |
|-----------|:---:|:---:|-------|
| Hongqiang Harry Liu | 21 | 3 | Publishing slowed |
| Hari Balakrishnan | 29 | 4 | Reduced academic conference output |
| Ming Zhang 0005 | 12 | 0 | Inactive after 2022 in clean conference data |
| Ankit Singla | 25 | 1 | Near-complete publishing stop in clean conference data |
| Alan Mislove | 28 | 3 | Reduced academic conference output |
| Christoph Dietzel | 14 | 0 | Inactive after 2022 in clean conference data |
| John Sonchack | 15 | 2 | Reduced output |
| Yu Zhou 0008 | 27 | 2 | Reduced output |
| Matt Calder | 14 | 3 | Reduced output |
| Robert Beverly | 12 | 3 | Reduced output |
| Bruce M. Maggs | 14 | 3 | Reduced output |
| Stefano Vissicchio | 7 | 3 | Reduced output |

Open question: these 12 should later be analyzed as a separate low-post-output group, probably with career-stage, industry, retirement, and DBLP-lag checks. They should not be forced into percentage-vector PCA.

## 2. Feature Construction

The analysis uses two related but distinct feature layers.

### 2.1 Static Portfolio Features

For each analyzable researcher, the static profile is a 10-dimensional venue-family percentage vector.

| Family | Examples of venues |
|---|---|
| `qualifying_top_networking` | SIGCOMM, NSDI, CoNEXT, HotNets, IMC |
| `other_networking` | INFOCOM, ICNP, PAM, TMA, ANRW, APNet, IFIP Networking |
| `systems` | OSDI, SOSP, EuroSys, USENIX ATC, ASPLOS, SoCC, MLSys |
| `AI_ML` | ICML, ICLR, NeurIPS, AAAI, CVPR, ICCV, EMNLP, ACL |
| `security_privacy` | USENIX Security, IEEE S&P, CCS, NDSS, PETS |
| `mobile_wireless_iot` | MobiCom, MobiSys, SenSys, UbiComp, IPSN |
| `web_social_hci` | WWW, CHI, ICWSM, WebSci, ISMAR, VR |
| `data_management` | SIGMOD, VLDB, ICDE, CIDR |
| `theory_distributed` | PODC, DISC, SPAA, OPODIS, ICDCS |
| `programming_languages` | PLDI, POPL, OOPSLA, ICSE-adjacent PL venues |

For each period and family:

```text
family_share = papers_in_family / total_clean_papers_in_period * 100
```

This gives three vectors per researcher:

| View | Definition | Use |
|---|---|---|
| Baseline profile | 2018-2022 family percentages | What the researcher looked like before the observation period |
| Post-2023 profile | 2023-2026 family percentages | Where the researcher's visible conference portfolio landed |
| Delta profile | `post_pct - baseline_pct` | How the portfolio composition changed |

Percentages are used because researchers have very different publication volumes. A 5-paper systems increase means something different for a 10-paper researcher than for a 100-paper researcher. Raw counts are preserved in `data/core99_feature_vectors.json` and are used below whenever a percentage claim could hide volume.

### 2.2 Movement Features and Investigation Groups

The word "migration" is not used here as a final semantic label. In this document it means measurable movement along several axes.

| Feature | Meaning |
|---|---|
| `top_networking_rate_change` | Annualized change in SIGCOMM/NSDI/CoNEXT/HotNets/IMC output |
| `clean_publication_rate_change` | Annualized change in all clean conference output |
| Delta venue-family vector | Where the publication portfolio shifted by venue family |
| Authorship placement | Whether the researcher appears mostly as lead, collaborator, or senior author |

Rate ratios are annualized so the 5-year baseline window and 4-year post-baseline window can be compared:

```text
top_networking_rate_ratio = (post_top_net_count / 4) / (baseline_top_net_count / 5)
clean_publication_rate_ratio = (post_clean_count / 4) / (baseline_clean_count / 5)
```

Trend labels use deterministic thresholds: `increased` if ratio >= 1.25, `decreased` if ratio <= 0.75, `flat` otherwise, and `inactive_after_2022` if the post count is zero.

Limitation: rate labels describe per-year output for a researcher, not the absolute volume represented by a group. A small group can have a strong rate change but low paper volume; a large group can dominate aggregate volume even with modest per-researcher movement. For that reason, the analysis below always pairs rate labels with raw paper counts and group weights.

The main investigation grouping uses the two rate features:

| Group | Top-networking rate | Overall clean-publication rate | Plain meaning |
|---|---|---|---|
| Inv-Q1 | decreased | flat/increased | Top networking declines faster than overall output |
| Inv-Q2 | flat/increased | flat/increased | Strong or stable visible conference presence |
| Inv-Q3 | flat/increased | decreased | Top networking maintained relative to other output |
| Inv-Q4 | decreased | decreased | Broad decline in visible conference output |

Naming rule: this document uses **Inv-Q1** through **Inv-Q4** for the main investigation groups. The sys/AI/storage file `data/core99_sys_ai_storage_quadrants.csv` is a supplementary, orthogonal label set; it should not introduce another unqualified Q1/Q2/Q3/Q4 vocabulary in the main narrative.

## 3. Shallow Observation: Three Ways to Read the Movement

Before PCA or trajectory analysis, the simple aggregate picture is already informative. The gut-level hypothesis might be: top networking researchers are migrating to AI. The first deterministic observation is more cautious: among the analyzable core-99, top-networking participation is not disappearing as a collective, but visibility is being redistributed across researchers and venue families.

There are three measurements to keep separate:

| Measurement | What it answers | What it does not answer |
|---|---|---|
| Unique top-networking papers | How many accepted top-networking papers include at least one core-99 author | It does not count multiple core-99 authors on the same paper |
| Author-paper incidences | How much core-99 author participation appears across papers | It can double-count papers with multiple core-99 authors |
| Normalized portfolio shares | How each researcher's own publication mix changes | It loses absolute publication volume |

### 3.1 Percent Share Movement

| Family | Baseline mean | Post-2023 mean | Mean delta | Baseline median | Post-2023 median |
|--------|:------------:|:-------------:|:------:|:--------------:|:----------------:|
| qualifying_top_networking | 44.3% | 41.1% | -3.1pp | 44.9% | 38.5% |
| other_networking | 21.7% | 17.6% | -4.2pp | 16.7% | 11.8% |
| systems | 10.4% | 13.0% | +2.7pp | 6.7% | 6.7% |
| AI_ML | 2.4% | 4.4% | +2.0pp | 0.0% | 0.0% |
| security_privacy | 5.7% | 7.3% | +1.6pp | 2.8% | 0.0% |
| mobile_wireless_iot | 6.3% | 6.4% | +0.0pp | 0.0% | 0.0% |
| web_social_hci | 2.0% | 4.1% | +2.1pp | 0.0% | 0.0% |

![Aggregate Portfolio](figures/aggregate_portfolio.png)

The median researcher has zero AI_ML papers in both periods. AI_ML expansion exists, but it is concentrated in a minority rather than a cohort-wide shift.

### 3.2 Absolute Paper Counts and Core-99 Coverage

The count table below uses author-paper incidences for the 87 analyzable researchers. It answers: how much author participation from these researchers appears in each venue family?

| Family | Baseline incidences | Post-2023 incidences | Change | Annualized baseline | Annualized post |
|---|---:|---:|---:|---:|---:|
| qualifying_top_networking | 906 | 619 | -287 | 181.2/year | 154.8/year |
| other_networking | 655 | 307 | -348 | 131.0/year | 76.8/year |
| systems | 270 | 253 | -17 | 54.0/year | 63.2/year |
| AI_ML | 78 | 109 | +31 | 15.6/year | 27.2/year |
| security_privacy | 148 | 110 | -38 | 29.6/year | 27.5/year |
| mobile_wireless_iot | 161 | 102 | -59 | 32.2/year | 25.5/year |
| web_social_hci | 65 | 93 | +28 | 13.0/year | 23.2/year |

The top-networking denominator matters. During 2018-2022, the accepted-paper cache has 1,146 unique papers across SIGCOMM, NSDI, CoNEXT, HotNets, and IMC. The full core-99 appears on 589 of them, or 51.4%; the 87 analyzable researchers appear on 569, or 49.7%.

For 2023-2026, this project does not yet have the same all-accepted-paper denominator for the five venues. Within the itinerary data, the 87 analyzable researchers appear on 451 unique post-2023 top-networking papers, which is 112.8 unique papers/year, almost the same as their baseline 113.8 unique papers/year. The full core-99 appears on 456 unique post-2023 top-networking papers.

So the cleanest current reading is:

- As a collective, core-99 still appears on many top-networking papers after 2022.
- The author-paper incidence rate drops, suggesting fewer repeated/core-99 author participations per year.
- The distribution shifts: some researchers fall out sharply, while the stable core accounts for a larger share of post-2023 top-networking participation.
- AI_ML and web/HCI grow in absolute count; systems grows in annualized count but not total count because the post window is shorter.

This is why the analysis below focuses on redistribution and group mechanisms, not just total decline.

## 4. Question 1: Who Is Falling Out of Top Networking?

The biggest visible phenomenon is that many core-99 researchers lose presence at the five qualifying networking venues.

Among the 87 analyzable researchers:

| Group | N | Researcher share | Baseline clean share | Post clean share | Baseline top-net share | Post top-net share | Main count movement |
|-------|--:|---:|---:|---:|---:|---:|---|
| Inv-Q1: top-net down, clean flat/up | 15 | 17.2% | 16.0% | 17.6% | 17.7% | 11.6% | top-net 160->72, other-networking -23, systems +7, web/HCI +12 |
| Inv-Q4: top-net down, clean down | 28 | 32.2% | 34.6% | 21.0% | 32.5% | 16.5% | top-net 294->102, other-networking -187, broad volume decline |

Together, Inv-Q1 and Inv-Q4 contain 43 researchers, or 49.4% of the analyzable core-99. They contribute 50.2% of baseline top-networking author-paper incidences but only 28.1% post-2023. This is the core redistribution signal: the falling-out groups lose top-networking weight, while the stable groups take a larger post-2023 share.

### 4.1 Inv-Q1: Substitution Rather Than Simple Exit

Inv-Q1 researchers have decreasing top-networking rate but flat or increasing annualized clean-publication rate. Their average delta profile is the clearest portfolio shift in the analysis:

| Group | N | Mean delta vector | Count movement | Interpretation |
|-------|--:|--------------|---|-----------|
| Inv-Q1 | 15 | qualifying -24.6pp, other +8.7pp, systems +8.0pp | qualifying 160->72, systems 30->37, web/HCI 4->16 | Losing qualifying venue share and replacing part of it elsewhere |

Delta values are percentage-point changes in each researcher's own portfolio, so dimensions have the same unit and can be compared as composition changes. They do not directly encode absolute paper volume. A high-volume and low-volume researcher can have the same delta if their internal mix changes similarly. This is why the mean-delta row is paired with count movement and representative examples; outlier sensitivity remains a reason to inspect medians and per-researcher heatmaps before making stronger claims.

![Delta by Investigation Group](figures/delta_by_inv_group.png)

This is the best current candidate group for a "where did they go?" question. The current venue-family evidence says the answer is heterogeneous: adjacent measurement venues, systems venues, web/HCI, security, theory, and some workshop/poster venues. It does not yet support a clean story such as "they moved to AI."

Representative examples, chosen to cover different Inv-Q1 mechanisms rather than to imply they represent the whole group:

| Researcher | Why this example | Baseline topic/venue pattern | Post-2023 topic/venue pattern | Caution |
|---|---|---|---|---|
| Yibo Zhu 0001 | Strong systems/AI-infra substitution | NSDI/SIGCOMM plus distributed DNN training systems | EuroSys/OSDI/ATC/NSDI work on DNN training, MoE training, LLM serving | Looks like AI infrastructure/systems, not core AI migration |
| Ihsan Ayyub Qazi | AI/HCI-adjacent growth inside falling-out group | CoNEXT/SIGCOMM networking plus WWW/CHI access work | WWW/CHI/ACL/EMNLP work on affordability, accessibility, deepfakes, healthcare LLMs | The clearest AI-adjacent case in Inv-Q1, but HCI/web framed |
| Laurent Vanbever | Still networking-centered despite top-net decline | Network control, routing, monitoring, BGP, network verification | BGP, network monitoring, packet scheduling, privacy/security-adjacent networking | More venue redistribution than topic exit |
| Alex C. Snoeren | Systems/security/network measurement mix | IMC/SIGCOMM, VPNs, congestion, datacenter SDN, security | SIGCOMM/IMC plus ASPLOS/SOSP/ATC on FPGA, RPCs, infrastructure | Broad systems/networking blend |

Open question requiring paper-topic analysis: for Inv-Q1, are these researchers still doing networking topics in less selective or adjacent venues, or are they changing research questions? Venue family alone cannot answer that.

### 4.2 Inv-Q4: Broad Decline, Not a Clear Destination

Inv-Q4 researchers decline in both top-networking and overall clean conference output:

| Group | N | Mean delta vector | Count movement | Interpretation |
|-------|--:|--------------|---|-----------|
| Inv-Q4 | 28 | qualifying -5.8pp, other -5.3pp, security +5.0pp | clean 866->360, qualifying 294->102, other 292->105 | Output decreases broadly; composition shifts less sharply than Inv-Q1 |

This group should not be described as migration without more evidence. The visible pattern is lower conference publication volume. Possible explanations include industry moves, seniority changes, retirement, journal publishing, missing recent data, or genuine topic movement to venues not yet captured well.

Representative examples:

| Researcher | Why this example | Baseline topic/venue pattern | Post-2023 topic/venue pattern | Caution |
|---|---|---|---|---|
| Vyas Sekar | Large broad decline but still networking/security systems | NSDI/SIGCOMM/IMC on network policies, telemetry, programmable switches, security | Fewer papers, still network telemetry, switch resource augmentation, cyber-security adjacent work | Decline is not simple field exit |
| Robert Soulé | Moves toward systems/distributed protocols while output drops | Programmable data planes, traffic engineering, distributed coordination | SoCC/Middleware/CIDR/DBPL, quantum networking, OS/database systems | Looks like topic broadening plus lower volume |
| Aaron Schulman | Wireless/security infrastructure profile with lower volume | IMC/NSDI/SIGCOMM/MobiCom/security on wireless, failures, security | MobiCom/security/PAM/ASPLOS on sensing, base stations, physical-layer security | Needs career/institution context |
| Mohammad Alizadeh | High-profile networking/systems researcher with reduced volume | Congestion control, datacenter systems, video analytics, road-network AI/data work | Still NSDI/SIGCOMM plus ICML/ICDE/video/network systems | Lower volume, not clean migration away |

Open question: what explains broad decline among Inv-Q4? This needs institution/sector/career-stage labels and possibly non-conference output checks.

## 5. Question 2: Who Remains Strong in Top Networking?

The counterpattern is the group that remains flat or increasing in top-networking rate.

Among the 87 analyzable researchers:

| Group | N | Researcher share | Baseline clean share | Post clean share | Baseline top-net share | Post top-net share | Main count movement |
|-------|--:|---:|---:|---:|---:|---:|---|
| Inv-Q2: top-net flat/up, clean flat/up | 37 | 42.5% | 40.9% | 55.8% | 42.1% | 63.2% | top-net 381->391, AI_ML +38, systems +3, other-networking -88 |
| Inv-Q3: top-net flat/up, clean down | 7 | 8.0% | 8.5% | 5.6% | 7.8% | 8.7% | clean 213->96, other-networking -50, systems -16 |

The volume table changes how the investigation labels should be read. Inv-Q2 has the real stable-top-networking weight: 42.5% of researchers but 63.2% of post-2023 top-networking author-paper incidences. Inv-Q3 has a rising qualifying share in percentage terms, but raw top-networking count still declines from 71 to 54 because total output contracts sharply.

### 5.1 Inv-Q2: Stable Core With Mild Expansion

Inv-Q2 is the strongest visible conference-presence group. These researchers maintain both top-networking and overall clean-publication rates.

| Group | N | Mean delta vector | Count movement | Interpretation |
|-------|--:|--------------|---|-----------|
| Inv-Q2 | 37 | other -6.5pp, AI_ML +3.7pp, qualifying +2.6pp | qualifying 381->391, AI_ML 51->89, systems 186->189 | Maintains networking while adding AI_ML and holding systems steady |

The key point is that Inv-Q2 is not a migration-away group. It is better described as the stable core: still strong in top networking, with some AI_ML and systems broadening.

Representative examples:

| Researcher | Why this example | Baseline topic/venue pattern | Post-2023 topic/venue pattern | Caution |
|---|---|---|---|---|
| Ion Stoica | AI_ML expansion from already high AI/systems base | NSDI/OSDI/ICML/MobiCom on distributed systems, analytics, RL, graph systems | ICML/MLSys/NSDI on LLM inference, DNN serving, cloud robotics, lakehouse systems | Not a new migrant; already broad and AI-heavy |
| Aditya Akella | New AI_ML venue presence while retaining NSDI/SIGCOMM | Programmable NICs, RDMA, distributed systems, datacenter networking | ICML/NSDI/ASPLOS/MICRO on ML collective scheduling, kernels, SmartNICs | Looks like AI infrastructure plus systems |
| Kai Chen 0005 | Strong systems increase and top-net increase | Datacenter networking, RDMA, congestion control, deep RL for DCN | NSDI/SIGCOMM/EuroSys plus LLM inference, DNN training, federated/graph learning | AI/sys growth coexists with stronger top networking |
| Jiaqi Gao | Clear AI_ML increase from zero baseline | SIGCOMM/NSDI-heavy networking baseline | AAAI/AI_ML plus continued SIGCOMM/NSDI presence | Needs paper-level topic labeling before interpretation |

Open question requiring paper-topic analysis: among stable top-networking researchers, are the new systems/AI_ML papers about AI infrastructure, classical distributed systems, measurement, wireless, or core ML? Venue family gives location, not topic.

### 5.2 Inv-Q3: Concentration by Subtraction

Inv-Q3 looks like increased concentration in qualifying top-networking venues in percentage terms:

| Group | N | Mean delta vector | Count movement | Interpretation |
|-------|--:|--------------|---|-----------|
| Inv-Q3 | 7 | qualifying +22.7pp, other -15.0pp, systems -4.3pp | clean 213->96, qualifying 71->54, other 63->13 | Qualifying share rises because other output contracts faster |

This is not stronger top-networking output in raw count. The top-networking share rises partly by denominator effect.

Representative examples:

| Researcher | Why this example | Baseline topic/venue pattern | Post-2023 topic/venue pattern | Caution |
|---|---|---|---|---|
| Ran Ben Basat | Extreme focusing plus AI_ML signal | Measurement algorithms, sketches, programmable-switch measurement, INFOCOM/ICNP/CoNEXT | SIGCOMM/HotNets/NSDI plus ICML/NeurIPS on distributed learning/quantization | Both concentration and AI_ML appear; needs topic review |
| Harsha V. Madhyastha | Maintains top networking while total output falls | NSDI/IMC/HotNets style networked systems and measurement | Smaller set with continued NSDI/IMC/SIGCOMM presence | Could be focus, not growth |
| Manya Ghobadi | Systems-heavy baseline with maintained top networking | SIGCOMM/NSDI/HotNets plus cloud/systems networking | HotNets/NSDI/SIGCOMM with more selective output | Denominator effect likely important |

Open question: for Inv-Q3, are they deliberately focusing on elite networking, or are they simply publishing less outside the five venues? Raw-count sensitivity and paper-topic review are needed.

## 6. Question 3: Is There an AI_ML or Systems Migration Signal?

There is AI_ML and systems movement, but it is not the dominant aggregate story.

### 6.1 AI_ML Expansion

Only 9 of the 87 analyzable researchers have AI_ML expansion greater than 10 percentage points:

| Researcher | Delta AI_ML | AI_ML papers baseline -> post | Group | Current read |
|-----------|:------:|---:|---|---------|
| Aditya Akella | +29pp | 0 -> 10 | Inv-Q2 | New AI_ML venue presence from zero baseline |
| Daehyeok Kim | +25pp | 0 -> 4 | Inv-Q2 | New AI_ML venue presence from zero baseline |
| Jiaqi Gao | +25pp | 0 -> 5 | Inv-Q2 | New AI_ML venue presence from zero baseline |
| Ihsan Ayyub Qazi | +24pp | 3 -> 7 | Inv-Q1 | Already had AI_ML presence, expanded further |
| John S. Heidemann | +23pp | 0 -> 3 | Inv-Q4 | New AI_ML venue presence, but overall output down |
| Ion Stoica | +22pp | 24 -> 37 | Inv-Q2 | Already AI_ML-heavy at baseline, expanded further |
| Dongsu Han | +17pp | 1 -> 4 | Inv-Q2 | Expansion from small baseline |
| Jianping Wu | +14pp | 2 -> 6 | Inv-Q2 | Expansion from small baseline |
| Ran Ben Basat | +13pp | 2 -> 2 | Inv-Q3 | Share rises despite flat AI_ML count due to smaller denominator |

The absolute-count column matters. Some large percentage-point changes are only a few papers; Ran Ben Basat's AI_ML share rises even though AI_ML count is flat.

### 6.2 Systems Expansion

Systems movement is also concentrated in a small number of people. It should be discussed alongside AI_ML because many apparent AI shifts are actually AI infrastructure or distributed systems shifts.

| Researcher | Delta systems | Systems papers baseline -> post | Group | Current read |
|---|---:|---:|---|---|
| Yibo Zhu 0001 | +36pp | 6 -> 10 | Inv-Q1 | Distributed training and LLM serving systems |
| Robert Soulé | +34pp | 4 -> 5 | Inv-Q4 | Systems/distributed protocols grow in share while total output falls |
| Alex C. Snoeren | +25pp | 2 -> 5 | Inv-Q1 | FPGA/NIC offload, RPC, infrastructure systems |
| Kai Chen 0005 | +20pp | 5 -> 17 | Inv-Q2 | EuroSys/NSDI/SIGCOMM systems and AI infrastructure |
| Mosharaf Chowdhury | +20pp | 9 -> 12 | Inv-Q2 | MLSys/OSDI style systems for ML/distributed computing |
| Gianni Antichi | +16pp | 2 -> 6 | Inv-Q2 | ASPLOS/EuroSys systems growth |
| Arvind Krishnamurthy | +14pp | 13 -> 15 | Inv-Q2 | Systems remains high and slightly grows |

Open TODO: summarize the actual paper topics for AI_ML and systems expanders with title/abstract evidence. The current venue-family label can say where papers appeared, not whether the work is core AI, AI infrastructure, systems, or networking using ML.

## 7. Deeper Structure: Static Profiles and Trajectories

The group analysis above gives the main narrative. PCA and trajectory figures add structure: they show that core-99 researchers started from different baseline positions, so the same post-2023 movement can mean different things.

### 7.1 Baseline Static Profile

PCA on baseline profiles explains 67% of variance in the first two components.

- PC1 separates elite-venue-concentrated researchers from broad-networking researchers: `qualifying_top_networking` loads negatively and `other_networking` loads positively.
- PC2 separates networking-pure researchers from systems/mobile-engaged researchers.

![PCA Baseline Labeled](figures/pca_baseline_labeled.png)

Important limitation: PCA coordinates are computed from percentage profiles, not raw paper counts. Distance from the origin means the researcher's venue-family composition is unusual relative to the sample; it does not mean the researcher publishes more papers. Publication volume must be read from the count tables, not from PCA position or vector norm.

Visualization note: this plot should be regenerated with labels aligned to the Inv-Q taxonomy or to the representative examples used in this document. Avoid sys/AI/storage quadrant legends here because that taxonomy is supplementary and can confuse the main analysis flow.

Representative baseline positions:

| Researcher | Why selected | Baseline read | Topic hint |
|---|---|---|---|
| Behnaz Arzani | Elite-concentrated endpoint | Very high qualifying-top-networking share | Datacenter/network reliability and systems networking |
| Debopam Bhattacherjee | Elite-concentrated endpoint and later large trajectory move | LEO/satellite networking and top-networking concentration | Space/LEO networking and measurements |
| Georg Carle | Broad-networking endpoint | Large adjacent-networking share | Measurement/security/network operations |
| Stefan Schmid 0001 | Broad and high-volume endpoint | Very broad adjacent networking plus theory/distributed systems | Network algorithms, distributed systems, theory-adjacent networking |
| Ion Stoica | Systems-engaged endpoint | Large systems and AI_ML baseline component | Distributed systems, data/ML systems |

This matters because a decline in qualifying venue share means different things depending on the starting point. Losing 25 percentage points from an 80% qualifying baseline is not the same as losing 25 points from a broad-networking baseline.

### 7.2 Trajectory View in Shared PCA Space

The shared baseline/post projection and trajectory view are best read together, so the trajectory figure is the primary visualization here. Each arrow shows one researcher's movement from baseline to post-2023 using the baseline PCA axes.

![PCA Trajectories](figures/pca_trajectories_shared.png)

Visualization note: the next version of this figure should label the same representative researchers used in Sections 4-6, so the reader can follow the same characters through the narrative rather than seeing a fresh cherry-picked set at each plot.

Largest movements currently visible:

| Researcher | Delta PC1 | Delta PC2 | Direction | Current read |
|-----------|------:|------:|-----------|-------|
| Debopam Bhattacherjee | +50 | +20 | Toward broad-networking | From highly qualifying-concentrated to more adjacent-networking mix |
| Ingmar Poese | +47 | +22 | Toward broad-networking | Similar broadening away from qualifying concentration |
| Ran Ben Basat | -51 | 0 | Toward elite-concentrated | Focuses more sharply on qualifying venues |
| Robert Soulé | -2 | +49 | Toward systems/mobile | Moves toward systems-heavy portfolio |
| Aaron Schulman | +36 | +29 | Broad + systems/mobile | Large qualifying drop with compensation elsewhere |
| Ihsan Ayyub Qazi | +28 | +29 | Broad + systems/mobile | Qualifying share declines while AI_ML/web_social_hci rises |
| Ravi Netravali | -22 | -32 | Elite + networking-pure | Stronger top-networking focus |

The largest movements are along networking-composition axes, not primarily along an AI_ML axis. AI_ML is visible in individual deltas, but it does not define the main low-dimensional structure.

## 8. Delta Diagnostics: Why Trajectories Are Not Enough

The trajectory plot is good for seeing where researchers moved in two dominant PCA dimensions. It is not enough for three reasons:

1. PCA hides small but substantively important families if they explain little variance.
2. Two researchers can move similarly in PCA space while shifting through different venue families.
3. AI_ML, security, and web/HCI can be under-visible in the first two PCs because they are sparse.

That is why the delta heatmap remains useful for researcher-level inspection.

![Delta Heatmap](figures/delta_heatmap.png)

Delta PCA is retained as a secondary diagnostic, not as a central narrative figure.

![Delta PCA Biplot](figures/delta_pca_biplot.png)

Visualization note: the current biplot is harder to interpret than the group tables and trajectory figure. If kept, it should be regenerated to highlight the same representative researchers or to explicitly highlight different movement patterns such as top-net substitution, broad decline, AI_ML expansion, and systems expansion.

## 9. Current Findings, Stated Conservatively

The current core-99 analysis supports these claims:

1. Core-99 is not monolithic. Baseline profiles range from elite-venue-concentrated to broad-networking to systems-engaged.
2. The first aggregate signal is not cohort-wide AI_ML or systems migration. The larger signal is redistribution: unique-paper core-99 presence in top networking is roughly stable annualized, but top-networking author-paper incidence and adjacent-networking incidence drop, while AI_ML, systems share, and web/HCI gains are smaller and concentrated.
3. A large individual-level falling-out phenomenon exists: 43 of 87 analyzable researchers lose top-networking presence. Inv-Q1 looks like substitution away from top networking; Inv-Q4 looks more like broad publication-volume decline.
4. The falling-out pattern should currently be described as degradation or redistribution from top-networking visibility for part of the old core, not as proven topic migration or collective disappearance from top networking.
5. Inv-Q2 remains the stable core: top networking is maintained, AI_ML count grows, and systems remains large. This group is where AI infrastructure and systems broadening should be checked carefully.
6. Inv-Q3 is best read cautiously as concentration by contraction, not automatic strengthening, because raw clean output falls sharply.
7. AI_ML expansion is real for 9 researchers, and strong systems-share moves are visible for researchers such as Yibo Zhu 0001, Robert Soulé, Alex C. Snoeren, Kai Chen 0005, Mosharaf Chowdhury, Gianni Antichi, and Arvind Krishnamurthy. Both AI_ML and systems movement need paper-topic review before semantic labels are assigned.

## 10. Open Questions for the Next Analysis Layer

These questions should shape the next work. Some require new derived data and should not be answered from venue-family vectors alone.

| Question | Why it matters | Needed evidence |
|---|---|---|
| For Inv-Q1, what are they actually working on after falling out of top networking? | Distinguishes topic migration from venue/prestige drift | Paper titles/abstracts, topic labels, possibly LLM-assisted itinerary summaries |
| For Inv-Q2, what topics keep them strong in top networking? | Tests whether the stable core is classical networking, AI infra, systems, measurement, or mixed | Top-networking paper-level topic analysis |
| Are Inv-Q1 and Inv-Q2 topic profiles different, or mainly venue-placement different? | This is the substantive migration question | Comparable topic vectors by group and period |
| For AI_ML and systems expanders, is the work core AI, AI infrastructure, networking systems, or classical systems? | Venue family alone cannot distinguish these | Title/abstract-level classification |
| Given falling out is large, who are the new post-2023 top-networking core researchers? | The field may be renewing even if old core members decline | Build 2023-2026 top-networking cohort and compare to 2018-2022 core |
| Where were the new top-networking core researchers during 2018-2022? | Separates junior emergence from late migration into networking | Backward itineraries and authorship placement |
| Are the newcomers first authors, senior authors, or collaborators? | Distinguishes student/junior entry from PI/lab expansion | Author-position features for the new cohort |
| How much of Inv-Q3 is denominator artifact? | Prevents overstating concentration | Raw-count sensitivity, not only rate ratios and percentages |
| Does conference-level topic composition change in parallel? | Researcher movement may reflect venue trend shifts | Per-conference, per-year topic profiles |

## 11. Next Steps

Near-term work should be question-driven:

1. Build paper-topic packets for Inv-Q1, Inv-Q2, Inv-Q3, AI_ML expanders, and systems expanders.
2. Add an abstract coverage audit before relying on LLM topic summaries.
3. Run raw-count sensitivity for Inv-Q1 to Inv-Q4.
4. Construct the 2023-2026 top-networking core and compare it against the current core-99.
5. Add authorship-placement summaries for newcomers, not just incumbent core-99 researchers.
6. Regenerate the PCA/trajectory figures with consistent labels for the representative researchers used in this document.

LLM-driven itinerary analysis should enter after the topic packets and evidence questions are explicit. The first LLM task should be descriptive summarization with citations to titles/venues, not final migration labeling.

## Related Documents

- [CORE99_INVESTIGATION.md](CORE99_INVESTIGATION.md) - Detailed investigation tables, decompositions, quadrant analysis, and researcher-level notes
- [CORE99_RESEARCHER_ATTRIBUTES.md](CORE99_RESEARCHER_ATTRIBUTES.md) - Per-researcher deterministic attribute definitions
- [ANALYSIS_PLAN.md](ANALYSIS_PLAN.md) - Full project plan and TODO list
- [README.md](README.md) - Master project index

## Data Artifacts

| Artifact | Description |
|----------|-------------|
| `data/core99_feature_vectors.json` | 87 analyzable researchers: baseline/post-2023/delta profiles plus PCA/t-SNE coordinates |
| `data/core99_researcher_attributes.json` | Deterministic attributes for all 99 core researchers |
| `data/core99_investigation_summary.json` | Investigation Q1-Q3 aggregates |
| `data/core99_sys_ai_storage_quadrants.csv` | Supplementary top-tier systems/AI/storage venue quadrant analysis |
| `data/venue_family_map.json` | Venue-to-family mappings and aliases |

## Figures

| Figure | Content |
|--------|---------|
| `figures/aggregate_portfolio.png` | Mean baseline vs post-2023 portfolio |
| `figures/delta_magnitude_decomposition.png` | Supplementary venue-family shift magnitude diagnostic; not the primary volume view |
| `figures/delta_by_inv_group.png` | Mean delta vectors by investigation group |
| `figures/pca_baseline_labeled.png` | Baseline PCA with researcher labels at extremes; should be regenerated with consistent labels |
| `figures/pca_trajectories_shared.png` | Arrow trajectories from baseline to post-2023; primary PCA movement figure |
| `figures/pca_baseline_post_shared.png` | Baseline vs post-2023 in shared PCA space; supplementary after trajectory figure |
| `figures/delta_heatmap.png` | All 87 researchers by 10 family deltas |
| `figures/delta_pca_biplot.png` | Delta PCA diagnostic; needs clearer labels if retained |
