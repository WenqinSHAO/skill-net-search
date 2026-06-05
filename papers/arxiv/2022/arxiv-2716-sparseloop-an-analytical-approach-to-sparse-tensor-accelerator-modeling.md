---
id: arxiv-2716
title: "Sparseloop: An Analytical Approach to Sparse Tensor Accelerator Modeling"
conference: arXiv 2022
date: 2022-10
authors:
  - name: "Po-An Tsai"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Angshuman Parashar"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Joel Emer"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yannan Nellie Wu"
    affiliation: ""
    is_industry: false
  - name: "Vivienne Sze"
    affiliation: ""
    is_industry: false
topics:
  - GPU_architecture
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Architecture"
external_links:
  - name: "IEEE Digital Library"
    url: "https://ieeexplore.ieee.org/document/9923807"
abstract: "In recent years, many accelerators have been proposed to efficiently process sparse tensor algebra applications (e.g., sparse neural networks). However, these proposals are single points in a large and diverse design space. The lack of systematic description and modeling support for these sparse ten"
url: "https://research.nvidia.com/publication/2022-10_sparseloop-analytical-approach-sparse-tensor-accelerator-modeling"
status: new
---

# Sparseloop: An Analytical Approach to Sparse Tensor Accelerator Modeling

## 摘要

In recent years, many accelerators have been proposed to efficiently process sparse tensor algebra applications (e.g., sparse neural networks). However, these proposals are single points in a large and diverse design space. The lack of systematic description and modeling support for these sparse tensor accelerators impedes hardware designers from efficient and effective design space exploration. This paper first presents a unified taxonomy to systematically describe the diverse sparse tensor accelerator design space. Based on the proposed taxonomy, it then introduces Sparseloop, the first fast, accurate, and flexible analytical modeling framework to enable early-stage evaluation and exploration of sparse tensor accelerators. Sparseloop comprehends a large set of architecture specifications, including various dataflows and sparse acceleration features (e.g., elimination of zero-based compute). Using these specifications, Sparseloop evaluates a design’s processing speed and energy efficiency while accounting for data movement and compute incurred by the employed dataflow, including the savings and overhead introduced by the sparse acceleration features using stochastic density models. Across representative accelerator designs and workloads, Sparseloop achieves over 2000× faster modeling speed than cycle-level simulations, maintains relative performance trends, and achieves 0.1% to 8% average error. The paper also presents example use cases of Sparseloop in different accelerator design flows to reveal important design insights.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
