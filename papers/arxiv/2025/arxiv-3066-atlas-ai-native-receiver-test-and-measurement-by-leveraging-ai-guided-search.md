---
id: "arxiv-3066"
title: "ATLAS: AI-Native Receiver Test-and-Measurement by Leveraging AI-Guided Search"
conference: "arXiv 2025"
date: "2025-08"
authors:
  - name: "Mauro Belgiovine"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Suyash Pradhan"
    affiliation: "University of Texas at Austin"
    is_industry: false
  - name: "Johannes Lange"
    affiliation: "NI - Test and Measurement Group of Emerson"
    is_industry: false
  - name: "Michael Lohning"
    affiliation: "NI - Test and Measurement Group of Emerson"
    is_industry: false
  - name: "Kaushik Chowdhury"
    affiliation: "University of Texas at Austin"
    is_industry: false
topics:
  - Interconnect_networking
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Telecommunications"
abstract: "Industry adoption of Artificial Intelligence (AI)-native wireless receivers, or even modular, Machine Learning (ML)-aided wireless signal processing blocks, has been slow. The main concern is the lack of explainability of these trained ML models and the significant risks posed to network functionali"
url: "https://research.nvidia.com/publication/2025-08_atlas-ai-native-receiver-test-and-measurement-leveraging-ai-guided-search"
status: "new"
---

# ATLAS: AI-Native Receiver Test-and-Measurement by Leveraging AI-Guided Search

## 摘要

Industry adoption of Artificial Intelligence (AI)-native wireless receivers, or even modular, Machine Learning (ML)-aided wireless signal processing blocks, has been slow. The main concern is the lack of explainability of these trained ML models and the significant risks posed to network functionalities in case of failures, especially since (i) testing on every exhaustive case is infeasible and (ii) the data used for model training may not be available. This paper proposes ATLAS, an AI-guided approach that generates a battery of tests for pre-trained AI-native receiver models and benchmarks the performance against a classical receiver architecture. Using gradient-based optimization, it avoids spanning the exhaustive set of all environment and channel conditions; instead, it generates the next test in an online manner to further probe specific configurations that offer the highest risk of failure. We implement and validate our approach by adopting the well-known DeepRx AI-native receiver model as well as a classical receiver using differentiable tensors in NVIDIA's Sionna environment. ATLAS uncovers specific combinations of mobility, channel delay spread, and noise, where fully and partially trained variants of AI-native DeepRx perform suboptimally compared to the classical receivers. Our proposed method reduces the number of tests required per failure found by 19% compared to grid search for a 3-parameters input optimization problem, demonstrating greater efficiency. In contrast, the computational cost of the grid-based approach scales exponentially with the number of variables, making it increasingly impractical for high-dimensional problems.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
