---
id: "arxiv-2908"
title: "Reduced Precision DWC: An Efficient Hardening Strategy for Mixed-Precision Architectures"
conference: "arXiv 2021"
date: "2021-03"
authors:
  - name: "Fernando F. dos Santos"
    affiliation: "Universidade Federal do Rio Grande do Sul (UFRGS)"
    is_industry: false
  - name: "Marcelo Brandalero"
    affiliation: "Brandenburg University of Texchnology Cottbus-Senftenberg (B-TU)"
    is_industry: false
  - name: "Michael B. Sullivan"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Pedro M. Basso"
    affiliation: "Universidade Federal do Rio Grande do Sul (UFRGS)"
    is_industry: false
  - name: "Michael Hubner"
    affiliation: "Brandenburg University of Texchnology Cottbus-Senftenberg (B-TU)"
    is_industry: false
  - name: "Luigi Carro"
    affiliation: "Universidade Federal do Rio Grande do Sul (UFRGS)"
    is_industry: false
  - name: "Paolo Rech"
    affiliation: "Politecnico di Torino"
    is_industry: false
topics:
  - GPU_architecture
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Architecture"
  - "Resilience and Safety"
external_links:
  - name: "IEEE Digital Library"
    url: "https://ieeexplore.ieee.org/abstract/document/9354571"
abstract: "Duplication with Comparison (DWC) is an effective software-level solution to improve the reliability of computing devices. However, it introduces performance and energy consumption overheads that could be unsuitable for high-performance computing or real-time safety-critical applications. In this ar"
url: "https://research.nvidia.com/publication/2021-03_reduced-precision-dwc-efficient-hardening-strategy-mixed-precision"
status: "new"
---

# Reduced Precision DWC: An Efficient Hardening Strategy for Mixed-Precision Architectures

## 摘要

Duplication with Comparison (DWC) is an effective software-level solution to improve the reliability of computing devices. However, it introduces performance and energy consumption overheads that could be unsuitable for high-performance computing or real-time safety-critical applications. In this article, we present Reduced-Precision Duplication with Comparison (RP-DWC) as a means to lower the overhead of DWC by executing the redundant copy in reduced precision. RP-DWC is particularly suitable for modern mixed-precision architectures, such as NVIDIA GPUs, that feature dedicated functional units for computing with programmable accuracy. We discuss the benefits and challenges associated with RP-DWC and show that the intrinsic difference between the mixed-precision copies allows for detecting most, but not all, errors. However, as the undetected faults are the ones that fall into the difference between precisions, they are the ones that produce a much smaller impact on the application output and, thus, might be tolerated. We investigate RP-DWC impact into fault detection, performance, and energy consumption on Volta GPUs. Through fault injection and beam experiment, using three microbenchmarks and four real applications, we show that RP-DWC achieves an excellent coverage (up to 86 percent) with minimal overheads (as low as 0.1 percent time and 24 percent energy consumption overhead).

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
