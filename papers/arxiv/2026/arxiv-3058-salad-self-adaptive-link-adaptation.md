---
id: "arxiv-3058"
title: "SALAD: Self-Adaptive Link Adaptation"
conference: "arXiv 2026"
date: "2026-03"
authors:
  - name: "Reinhard Wiesmayr"
    affiliation: "ETH Zurich, NVIDIA"
    is_industry: true
  - name: "Lorenzo Maggi"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Sebastian Cammerer"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jakob Hoydis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Fayçal Aït Aoudia"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Alex Keller"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - Interconnect_networking
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Telecommunications"
abstract: "Adapting the modulation and coding scheme (MCS) to the wireless link quality is critical for maximizing spectral efficiency while ensuring reliability. We propose SALAD (selfadaptive link adaptation), an algorithm that exclusively leverages ACK/NACK feedback to reliably track the evolution of the si"
url: "https://research.nvidia.com/publication/2026-03_salad-self-adaptive-link-adaptation"
status: "new"
---

# SALAD: Self-Adaptive Link Adaptation

## 摘要

Adapting the modulation and coding scheme (MCS) to the wireless link quality is critical for maximizing spectral efficiency while ensuring reliability. We propose SALAD (selfadaptive link adaptation), an algorithm that exclusively leverages ACK/NACK feedback to reliably track the evolution of the signalto-interference-plus-noise ratio (SINR), achieving high spectral efficiency while keeping the long-term block error rate (BLER) near a desired target. SALAD infers the SINR by minimizing the cross-entropy loss between received ACK/NACKs and predicted BLER values. Based on this inference, SALAD selects the MCS via hypothesis testing: if the SINR is likely underestimated, a higher MCS is selected to accelerate link adaptation under improving channel conditions. To prevent BLER drift from its long-term target, SALAD incorporates a feedback control loop that adjusts the instantaneous BLER target. Over-theair experiments on a 5G testbed demonstrate that SALAD consistently outperforms the industry-standard outer-loop link adaptation (OLLA). With a single set of parameters, SALAD achieves up to 15% higher throughput and spectral efficiency than multiple OLLA variants across different traffic regimes, while meeting the BLER target.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
