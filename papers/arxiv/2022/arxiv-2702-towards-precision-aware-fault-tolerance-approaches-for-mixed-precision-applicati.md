---
id: "arxiv-2702"
title: "Towards Precision-Aware Fault Tolerance Approaches for Mixed-Precision Applications"
conference: "arXiv 2022"
date: "2022-11"
authors:
  - name: "Bo Fang"
    affiliation: "Pacific Northwest National Laboratory"
    is_industry: false
  - name: "Siva Hari"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Timothy Tsai"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Xinyi Li"
    affiliation: "University of Utah"
    is_industry: false
  - name: "Ganesh Gopalakrishnan"
    affiliation: "University of Utah"
    is_industry: false
  - name: "Ignacio Laguna"
    affiliation: "Lawrence Livermore National Laboratory"
    is_industry: false
  - name: "Kevin Barker"
    affiliation: "Pacific Northwest National Laboratory"
    is_industry: false
  - name: "Ang Li"
    affiliation: "Pacific Northwest National Laboratory"
    is_industry: false
topics:
  - GPU_architecture
  - Robotics_autonomous
  - Simulation_HPC
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Architecture"
  - "High Performance Computing"
  - "Resilience and Safety"
external_links:
  - name: "IEEE Digital Library"
    url: "https://ieeexplore.ieee.org/document/10024043"
abstract: "Graphics Processing Units (GPUs), the dominantly adopted accelerators in HPC systems, are susceptible to a transient hardware fault. A new generation of GPUs features mixed-precision architectures such as NVIDIA Tensor Cores to accelerate matrix multiplications. While widely adapted, how they would "
url: "https://research.nvidia.com/publication/2022-11_towards-precision-aware-fault-tolerance-approaches-mixed-precision-applications"
status: "new"
---

# Towards Precision-Aware Fault Tolerance Approaches for Mixed-Precision Applications

## 摘要

Graphics Processing Units (GPUs), the dominantly adopted accelerators in HPC systems, are susceptible to a transient hardware fault. A new generation of GPUs features mixed-precision architectures such as NVIDIA Tensor Cores to accelerate matrix multiplications. While widely adapted, how they would behave under transient hardware faults remain unclear. In this study, we conduct large-scale fault injection experiments on GEMM kernels implemented with different floating-point data types on the V100 and A100 Tensor Cores and show distinct error resilience characteristics for the GEMMS with different formats. We plan to explore this space in the future by building precision-aware floating-point fault tolerance techniques for applications such as DNNs that exercise low-precision computations.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
