---
id: "arxiv-3027"
title: "Estimating Silent Data Corruption Rates Using a Two-Level Model"
conference: "arXiv 2020"
date: "2020-04"
authors:
  - name: "Siva Hari"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Paolo Rech"
    affiliation: "Federal University of Rio Grande do Sul"
    is_industry: false
  - name: "Timothy Tsai"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Mark Stephenson"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Arslan Zulfiqar"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Michael B. Sullivan"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Philip Shirvani"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Paul Racunas"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Joel Emer"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Steve Keckler"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - GPU_architecture
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Architecture"
  - "Resilience and Safety"
abstract: "High-performance and safety-critical system architects must accurately evaluate the application-level silent data corruption (SDC) rates of processors to soft errors. Such an evaluation requires error propagation all the way from particle strikes on low-level state up to the program output. Existing"
url: "https://research.nvidia.com/publication/2020-04_estimating-silent-data-corruption-rates-using-two-level-model"
status: "new"
---

# Estimating Silent Data Corruption Rates Using a Two-Level Model

## 摘要

High-performance and safety-critical system architects must accurately evaluate the application-level silent data corruption (SDC) rates of processors to soft errors. Such an evaluation requires error propagation all the way from particle strikes on low-level state up to the program output. Existing approaches that rely on low-level simulations with fault injection cannot evaluate full applications because of their slow speeds, while application-level accelerated fault testing in accelerated particle beams is often impractical. We present a new two-level methodology for application resilience evaluation that overcomes these challenges. The proposed approach decomposes application failure rate estimation into (1) identifying how particle strikes in low-level unprotected state manifest at the architecture-level, and (2) measuring how such architecture-level manifestations propagate to the program output. We demonstrate the effectiveness of this approach on GPU architectures. We also show that using just one of the two steps can overestimate SDC rates and produce different trends---the composition of the two is needed for accurate reliability modeling.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
