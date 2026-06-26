---
id: "arxiv-2910"
title: "Need for Speed: Experiences Building a Trustworthy System-Level GPU Simulator."
conference: "arXiv 2021"
date: "2021-02"
authors:
  - name: "Oreste Villa"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Daniel Lustig"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Zi Yan"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Evgeny Bolotin"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yaosheng Fu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Niladrish Chatterjee"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ted Jiang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "David Nellans"
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
    url: "https://doi.org/10.1109/HPCA51647.2021.00077"
abstract: "The demands of high-performance computing (HPC) and machine learning (ML) workloads have resulted in the rapid architectural evolution of GPUs over the last decade. The growing memory footprint and diversity of data types in these workloads has required GPUs to embrace micro-architectural heterogene"
url: "https://research.nvidia.com/publication/2021-02_need-speed-experiences-building-trustworthy-system-level-gpu-simulator"
status: "new"
---

# Need for Speed: Experiences Building a Trustworthy System-Level GPU Simulator.

## 摘要

The demands of high-performance computing (HPC) and machine learning (ML) workloads have resulted in the rapid architectural evolution of GPUs over the last decade. The growing memory footprint and diversity of data types in these workloads has required GPUs to embrace micro-architectural heterogeneity and increased memory system sophistication to scale performance. Effective simulation of new architectural features early in the design cycle enables quick and effective exploration of design trade-offs across this increasingly diverse set of workloads. This work provides a retrospective on the design and development of NVArchSim (NVAS), an architectural simulator used within NVIDIA to design and evaluate features that are difficult to appraise using other methodologies due to workload type, size, complexity, or lack of modeling flexibility. We argue that overly precise and/or overly slow architectural models hamper an architect's ability to evaluate new features within a reasonable time frame, hurting productivity. Because of its speed, NVAS is being used to trace and evaluate hundreds of HPC and state-of-the-art ML workloads on single-GPU or multi-GPU systems. By adding component fidelity only when necessary to improve system-level modeling accuracy, NVAS delivers simulation speed orders of magnitude higher than most publicly available GPU simulators while retaining high levels of accuracy and simulation flexibility. Building trustworthy high-level simulation platforms is a difficult exercise in balance and compromise; we share our experiences to help and encourage those in academia who take on the challenge of building GPU simulation platforms.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
