---
id: arxiv-2917
title: "Parasitic-Aware Analog Circuit Sizing with Graph Neural Networks and Bayesian Optimization"
conference: arXiv 2021
date: 2021-02
authors:
  - name: "Walker Turner"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Brucek Khailany"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Mingjie Liu"
    affiliation: ""
    is_industry: false
  - name: "George Kokai"
    affiliation: ""
    is_industry: false
  - name: "David Z. Pan"
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
  - name: "Parasitic-Aware Analog Circuit Sizing with Graph Neural Networks and Bayesian O…"
    url: "https://ieeexplore.ieee.org/document/9474253"
abstract: "Layout parasitics significantly impact the performance of analog integrated circuits, leading to discrepancies between schematic and post-layout performance and requiring several iterations to achieve design convergence. Prior work has accounted for parasitic effects during the initial design phase "
url: "https://research.nvidia.com/publication/2021-02_parasitic-aware-analog-circuit-sizing-graph-neural-networks-and-bayesian"
status: new
---

# Parasitic-Aware Analog Circuit Sizing with Graph Neural Networks and Bayesian Optimization

## 摘要

Layout parasitics significantly impact the performance of analog integrated circuits, leading to discrepancies between schematic and post-layout performance and requiring several iterations to achieve design convergence. Prior work has accounted for parasitic effects during the initial design phase but relies on automated layout generation for estimating parasitics. In this work, we leverage recent developments in parasitic prediction using graph neural networks to eliminate the need for in-the-loop layout generation. We propose an improved surrogate performance model using parasitic graph embeddings from the pre-trained parasitic prediction network. We further leverage dropout as an efficient prediction of uncertainty for Bayesian optimization to automate transistor sizing. Experimental results demonstrate the proposed surrogate model has 20% better R2 prediction score and improves optimization convergence by 3.7 times and 2.1 times compared to conventional Gaussian process regression and neural network based Bayesian linear regression, respectively. Furthermore, the inclusion of parasitic prediction in the optimization loop could guarantee satisfaction of all design constraints, while schematic-only optimization fail numerous constraints if verified with parasitic estimations.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
