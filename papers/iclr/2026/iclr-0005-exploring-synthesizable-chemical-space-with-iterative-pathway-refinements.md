---
id: "iclr-0005"
title: "Exploring Synthesizable Chemical Space with Iterative Pathway Refinements"
conference: "ICLR 2026"
date: "2026-01"
authors:
  - name: "Seul Lee"
    affiliation: "KAIST"
    is_industry: false
  - name: "Karsten Kreis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Srimukh Prasad Veccham"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Meng Liu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Danny Reidenbach"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Saee Paliwal"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Weili Nie"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Arash Vahdat"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Foundation_models
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Generative AI"
abstract: "A well-known pitfall of molecular generative models is that they are not guaranteed to generate synthesizable molecules. Existing solutions for this problem often struggle to effectively navigate exponentially large combinatorial space of synthesizable molecules and suffer from poor coverage. To add"
url: "https://research.nvidia.com/publication/2026-01%5Fexploring-synthesizable-chemical-space-iterative-pathway-refinements"
status: "new"
---

# Exploring Synthesizable Chemical Space with Iterative Pathway Refinements

## 摘要

A well-known pitfall of molecular generative models is that they are not guaranteed to generate synthesizable molecules. Existing solutions for this problem often struggle to effectively navigate exponentially large combinatorial space of synthesizable molecules and suffer from poor coverage. To address this problem, we introduce ReaSyn, an iterative generative pathway refinement framework that obtains synthesizable analogs to input molecules by projecting them onto synthesizable space. Specifically, we propose a simple synthetic pathway representation that allows for generating pathways in both bottom-up and top-down traversal of synthetic trees. We design ReaSyn so that both bottom-up and top-down pathways can be sampled with a single unified autoregressive model. ReaSyn can thus iteratively refine subtrees of generated synthetic trees in a bidirectional manner. Further, we introduce a discrete flow model that refines the generated pathway at the entire pathway level with edit operations: insertion, deletion, and substitution. The iterative refinement cycle of (1) bottom-up decoding, (2) top-down decoding, and (3) holistic editing constitutes a powerful pathway reasoning strategy, allowing the model to explore the vast space of synthesizable molecules. Experimentally, ReaSyn achieves the highest reconstruction rate and pathway diversity in synthesizable molecule reconstruction and the highest optimization performance in synthesizable goal-directed molecular optimization, and significantly outperforms previous synthesizable projection methods in synthesizable hit expansion. These results highlight ReaSyn's superior ability to navigate combinatorially-large synthesizable chemical space.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
