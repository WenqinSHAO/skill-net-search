---
id: "arxiv-2624"
title: "MedPart: A Multi-Level Evolutionary Differentiable Hypergraph Partitioner"
conference: "arXiv 2024"
date: "2024-03"
authors:
  - name: "Rongjian Liang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Anthony Agnesina"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Mark Haoxing Ren"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - GPU_architecture
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Circuits and VLSI Design"
external_links:
  - name: "MedPart"
    url: "https://confluence.nvidia.com/display/NVRAVR/EDPart%3A+Evolutionary+Differentiable+Hypergraph+Partitioning?preview=/2124023845/2729722999/MedPart__Multi_Level_Evolutionary_Differentiable_Hypergraph_Partitioner__Final_%20(1).pdf"
abstract: "State-of-the-art hypergraph partitioners, such as hMETIS, usually adopt a multi-level paradigm for efficiency and scalability. How\u0002ever, they are prone to getting trapped in local minima due to their reliance on refinement heuristics and overlooking global struc\u0002tural information during coarsening. "
url: "https://research.nvidia.com/publication/2024-03_medpart-multi-level-evolutionary-differentiable-hypergraph-partitioner"
status: "new"
---

# MedPart: A Multi-Level Evolutionary Differentiable Hypergraph Partitioner

## 摘要

State-of-the-art hypergraph partitioners, such as hMETIS, usually adopt a multi-level paradigm for efficiency and scalability. However, they are prone to getting trapped in local minima due to their reliance on refinement heuristics and overlooking global structural information during coarsening. SpecPart, the most advanced academic hypergraph partitioning refinement method, improves partitioning by leveraging spectral information. Still, its success depends heavily on the quality of initial input solutions. This work introduces MedPart, a multi-level evolutionary differentiable hypergraph partitioner. MedPart follows the multi-level paradigm but addresses its limitations by using fast spectral coarsening and introducing a novel evolutionary differentiable algorithm to optimize each coarsening level. Moreover, by analogy between hypergraph partitioning and deep graph learning, our evolutionary differentiable algorithm can be accelerated with deep graph learning toolkits on GPUs. Experiments on public benchmarks consistently show MedPart outperforming hMETIS and achieving up to a 30% improvement in cut size for some benchmarks compared to the best-published solutions, including those from SpecPart—moreover, MedPart’s runtime scales linearly with the number of hyperedges.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
