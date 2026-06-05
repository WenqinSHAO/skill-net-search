---
id: arxiv-2727
title: "XT-PRAGGMA: Crosstalk Pessimism Reduction Accessible by GPU Gate-level Simulations and Machine Learning"
conference: arXiv 2022
date: 2022-09
authors:
  - name: "Ben Keller"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yanqing Zhang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Brucek Khailany"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Vidya Chhabria"
    affiliation: ""
    is_industry: false
  - name: "Sandeep Vollala"
    affiliation: ""
    is_industry: false
  - name: "Sreedhar Patty"
    affiliation: ""
    is_industry: false
  - name: "Mark Haoxing Ren"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - GPU_architecture
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Circuits and VLSI Design"
external_links:
  - name: "Paper"
    url: "https://dl.acm.org/doi/10.1145/3551901.3556483"
abstract: "Accurate crosstalk-aware timing analysis is critical in nanometer-scale process nodes. While today's VLSI flows rely on static timing analysis (STA) techniques to perform crosstalk-aware timing signoff, these techniques are limited due to their static nature as they use imprecise heuristics such as "
url: "https://research.nvidia.com/publication/2022-09_xt-praggma-crosstalk-pessimism-reduction-accessible-gpu-gate-level-simulations"
status: new
---

# XT-PRAGGMA: Crosstalk Pessimism Reduction Accessible by GPU Gate-level Simulations and Machine Learning

## 摘要

Accurate crosstalk-aware timing analysis is critical in nanometer-scale process nodes. While today's VLSI flows rely on static timing analysis (STA) techniques to perform crosstalk-aware timing signoff, these techniques are limited due to their static nature as they use imprecise heuristics such as arbitrary aggressor filtering and simplified delay calculations. This paper proposes XT-PRAGGMA, a tool that uses GPU-accelerated dynamic gate-level simulations and machine learning to eliminate false aggressors and accurately predict crosstalk-induced delta delays. XT-PRAGGMA reduces STA pessimism and provides crucial information to identify crosstalk-critical nets, which can be considered for accurate SPICE simulation before signoff. The proposed technique is fast (less than two hours to simulate 30,000 vectors on million-gate designs) and reduces falsely-reported total negative slack in timing signoff by 70%.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
