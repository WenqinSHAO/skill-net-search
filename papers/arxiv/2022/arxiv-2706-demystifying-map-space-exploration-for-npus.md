---
id: "arxiv-2706"
title: "Demystifying Map Space Exploration for NPUs"
conference: "arXiv 2022"
date: "2022-11"
authors:
  - name: "Sheng-Chun Kao"
    affiliation: "Georgia Institute of Technology"
    is_industry: false
  - name: "Angshuman Parashar"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Po-An Tsai"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Tushar Krishna"
    affiliation: "Georgia Institute of Technology"
    is_industry: false
topics:
  - AI & Machine Learning
  - CUDA_ecosystem
  - GPU_architecture
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Architecture"
  - "Programming Languages, Systems and Tools"
external_links:
  - name: "IEEE Digital Library"
    url: "https://ieeexplore.ieee.org/document/9975389"
abstract: "Map Space Exploration is the problem of finding optimized mappings of a Deep Neural Network (DNN) model on an accelerator. It is known to be extremely computationally expensive, and there has been active research looking at both heuristics and learning-based methods to make the problem computational"
url: "https://research.nvidia.com/publication/2022-11_demystifying-map-space-exploration-npus"
status: "new"
---

# Demystifying Map Space Exploration for NPUs

## 摘要

Map Space Exploration is the problem of finding optimized mappings of a Deep Neural Network (DNN) model on an accelerator. It is known to be extremely computationally expensive, and there has been active research looking at both heuristics and learning-based methods to make the problem computationally tractable. However, while there are dozens of mappers out there (all empirically claiming to find better mappings than others), the research community lacks systematic insights on how different search techniques navigate the map-space and how different mapping axes contribute to the accelerator’s performance and efficiency. Such insights are crucial to developing mapping frameworks for emerging DNNs that are increasingly irregular (due to neural architecture search) and sparse, making the corresponding map spaces much more complex. In this work, rather than proposing yet another mapper, we do a first-of-its-kind apples-to-apples comparison of search techniques leveraged by different mappers. Next, we extract the learnings from our study and propose two new techniques that can augment existing mappers — warm-start and sparsity-aware — that demonstrate speedups, scalability, and robustness across&nbsp;diverse DNN models.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
