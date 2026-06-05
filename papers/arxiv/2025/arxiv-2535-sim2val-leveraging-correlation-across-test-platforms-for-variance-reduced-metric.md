---
id: arxiv-2535
title: "Sim2Val: Leveraging Correlation Across Test Platforms for Variance-Reduced Metric Estimation"
conference: arXiv 2025
date: 2025-09
authors:
  - name: "Rachel Luo"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Heng Yang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Michael Watson"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Apoorva Sharma"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Sushant Veer"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Marco Pavone"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Edward Schmerling"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Robotics_autonomous
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Autonomous Vehicles"
  - "Physical AI"
  - "Resilience and Safety"
  - "Robotics"
external_links:
  - name: "Paper"
    url: "https://arxiv.org/abs/2506.20553"
abstract: "Learning-based robotic systems demand rigorous validation to assure reliable performance, but extensive real-world testing is often prohibitively expensive, and if conducted may still yield insufficient data for high-confidence guarantees. In this work we introduce Sim2Val, a general estimation fram"
url: "https://research.nvidia.com/publication/2025-09_sim2val-leveraging-correlation-across-test-platforms-variance-reduced-metric"
status: new
---

# Sim2Val: Leveraging Correlation Across Test Platforms for Variance-Reduced Metric Estimation

## 摘要

Learning-based robotic systems demand rigorous validation to assure reliable performance, but extensive real-world testing is often prohibitively expensive, and if conducted may still yield insufficient data for high-confidence guarantees. In this work we introduce Sim2Val, a general estimation framework that leverages paired data across test platforms, e.g., paired simulation and real-world observations, to achieve better estimates of real-world metrics via the method of control variates. By incorporating cheap and abundant auxiliary measurements (for example, simulator outputs) as control variates for costly real-world samples, our method provably reduces the variance of Monte Carlo estimates and thus requires significantly fewer real-world samples to attain a specified confidence bound on the mean performance. We provide theoretical analysis characterizing the variance and sample-efficiency improvement, and demonstrate empirically in autonomous driving and quadruped robotics settings that our approach achieves high-probability bounds with markedly improved sample efficiency. Our technique can lower the real-world testing burden for validating the performance of the stack, thereby enabling more efficient and cost-effective experimental evaluation of robotic systems.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
