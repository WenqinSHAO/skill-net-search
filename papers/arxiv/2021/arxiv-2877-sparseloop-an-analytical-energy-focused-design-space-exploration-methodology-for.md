---
id: "arxiv-2877"
title: "Sparseloop: An Analytical, Energy-Focused Design Space Exploration Methodology for Sparse Tensor Accelerators"
conference: "arXiv 2021"
date: "2021-04"
authors:
  - name: "Yannan Nellie Wu"
    affiliation: "MIT"
    is_industry: false
  - name: "Po-An Tsai"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Angshuman Parashar"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Vivienne Sze"
    affiliation: "MIT"
    is_industry: false
  - name: "Joel Emer"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - GPU_architecture
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Architecture"
external_links:
  - name: "IEEE Digital Library"
    url: "https://ieeexplore.ieee.org/document/9408213"
abstract: "This paper presents Sparseloop, the first infrastructure that implements an analytical design space exploration methodology for sparse tensor accelerators. Sparseloop comprehends a wide set of architecture specifications including various sparse optimization features such as compressed tensor storag"
url: "https://research.nvidia.com/publication/2021-04_sparseloop-analytical-energy-focused-design-space-exploration-methodology"
status: "new"
---

# Sparseloop: An Analytical, Energy-Focused Design Space Exploration Methodology for Sparse Tensor Accelerators

## 摘要

This paper presents Sparseloop, the first infrastructure that implements an analytical design space exploration methodology for sparse tensor accelerators. Sparseloop comprehends a wide set of architecture specifications including various sparse optimization features such as compressed tensor storage. Using these specifications, Sparseloop can calculate a design's energy efficiency while accounting for both optimization savings and metadata overhead at each storage and compute level of the architecture using stochastic tensor density models. We validate Sparseloop on a well-known accelerator design and achieve ~99% accuracy in terms of runtime activities (e.g., compressed memory accesses). We also present a case study that highlights the key factors (e.g., uncompressed traffic, data density) that affect sparse optimization features' impact on energy efficiency. Tool available at: https://github.com/NVlabs/timeloop.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
