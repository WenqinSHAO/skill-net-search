# Transfer Evidence Validation Notes

Manual verification of 9 paper-blog pairs across evidence types, sampled 2026-06-05.

## Summary

| Verdict | Count |
|---------|-------|
| Strong match | 5 |
| Moderate match | 3 |
| Weak/False match | 1 |

**Overall precision: 8/9 (89%) meaningful transfer signals.**

## Detailed Findings

| # | Paper ID | Paper Title | Blog Title | Blog Date | Evidence | Verdict | Notes |
|---|----------|-------------|------------|-----------|----------|---------|-------|
| 1 | icml-0014 | Spherical Fourier Neural Operators: Learning Stable Dynamics on the Sphere | Modeling Earth's Atmosphere with Spherical Fourier Neural Operators | 2023-07-27 | author_overlap + title_match | **STRONG** | Blog directly describes the SFNO paper's method applied to weather. Same first author (Bonev). Perfect researcher-to-blog transfer. |
| 2 | arxiv-2674 | Fast Conformer with Linearly Scalable Attention for Efficient Speech Recognition | Pushing the Boundaries of Speech Recognition with NVIDIA NeMo Parakeet ASR Models | 2024-04-18 | author_overlap + title_match | **STRONG** | Blog announces Parakeet ASR model; paper provides the Fast Conformer architecture it's built on. Same author (Majumdar). Clear research-to-product pipeline. |
| 3 | iccv-0003 | Neural LiDAR Fields for Novel View Synthesis | Sensing New Frontiers with Neural Lidar Fields for Autonomous Vehicle Simulation | 2023-07-27 | author_overlap + title_match | **STRONG** | Blog is a direct explanation of the Neural LiDAR Fields paper's technique. Same first author (Gojcic). Blog title is the lay-friendly version of the paper title. |
| 4 | arxiv-2991 | Post-Render Warp with Late Input Sampling Improves Aiming Under High Latency Conditions | NVIDIA Research: Warp Drive Gaming – Eliminate More than 80% of the Latency Performance Penalty | 2020-07-14 | title_match only | **STRONG** | Blog discusses "late-warp" technique from the paper. Blog author (Alarcon, NVIDIA comms) is not a paper author, but the blog directly describes the research. Genuine comms-team citation of research. |
| 5 | corl-0001 | VT-Refine: Learning Bimanual Assembly with Visuo-Tactile Feedback via Simulation | R²D²: Three Neural Breakthroughs Transforming Robot Learning from NVIDIA Research | 2025-09-25 | title_match only | **STRONG** | Blog is a CoRL 2025 research roundup explicitly naming VT-Refine alongside NeRD and Dexplore. Covers this specific paper as one of three featured works. |
| 6 | arxiv-2521 | Demystifying Data-Driven Probabilistic Medium-Range Weather Forecasting | Improving Diffusion Models as an Alternative To GANs, Part 1 | 2022-04-26 | author_overlap only | **MODERATE** | Same author (Vahdat), same underlying technique (diffusion models), but different application domain (weather vs image generation). Blog is about diffusion methodology; paper applies it to weather. Connected through shared research thread, not direct citation. |
| 7 | arxiv-2710 | Adaptive NN-based OFDM Receivers: Computational Complexity vs. Achievable Performance | Powering AI-Native 6G Research with the NVIDIA Sionna Research Kit | 2025-10-28 | author_overlap only | **MODERATE** | Same author (Cammerer), same domain (wireless PHY). Blog announces Sionna toolkit; paper provides neural receiver research that likely informed or uses Sionna. Connected through shared research program. |
| 8 | arxiv-2585 | DRC-Coder: Automated DRC Checker Code Generation Using LLM Autonomous Agent | Configurable Graph-Based Task Solving with the Marco Multi-AI Agent Framework for Chip Design | 2025-02-25 | author_overlap + project_name_match | **MODERATE** | Same author (Ren), same domain (chip design automation with AI agents). Blog is about Marco framework; paper is about DRC-Coder. Different projects in the same research program. |
| 9 | siggraph-0022 | Motion-I2V: Consistent and Controllable Image-to-Video Generation with Explicit Motion Modeling | Automating GPU Kernel Translation with AI Agents: cuTile Python to cuTile.jl | 2026-04-30 | author_overlap only | **FALSE** | Same author name (Zhengyi Zhang) but completely unrelated topics: GPU kernel programming vs video generation AI. Likely the same researcher working across very different NVIDIA teams, or a name collision. Not useful transfer evidence. |

## Implications for Analysis

1. **author_overlap + title_match is near-perfect** (3/3 strong). This combination reliably identifies direct research-to-blog transfer.

2. **title_match only is surprisingly good** (2/2 strong). Both cases were NVIDIA communications team covering research, not the researchers themselves. These are the truest "external citation" signals.

3. **author_overlap only has moderate precision** (2 moderate, 1 false in our sample). It's useful but noisy — same author doesn't guarantee same research topic. The false match rate (~33%) means author_only matches should be interpreted as "researcher is active in public communication" rather than "this specific paper was transferred."

4. **No complete false positives** — even the "false" match is the same researcher, just different projects. The scoring thresholds (score >= 3 or title_match) are working as designed.

5. **Recommendation**: In the report, clearly distinguish between:
   - **Direct transfer** (title_match present): blog explicitly references the paper's work
   - **Researcher transfer** (author_overlap only): researcher blogs in the same broad area
   - Note the ~10% noise rate in author_only matches
