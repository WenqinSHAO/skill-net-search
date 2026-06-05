---
id: arxiv-2829
title: "Characterizing and Mitigating Soft Errors in GPU DRAM"
conference: arXiv 2021
date: 2021-10
authors:
  - name: "Michael B. Sullivan"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Mike O&#039;Connor"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Donghyuk Lee"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Siva Hari"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Steve Keckler"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Nirmal Saxena"
    affiliation: ""
    is_industry: false
  - name: "Paul Racunas"
    affiliation: ""
    is_industry: false
  - name: "Saurabh Hukerikar"
    affiliation: ""
    is_industry: false
  - name: "Timothy Tsai"
    affiliation: ""
    is_industry: false
topics:
  - GPU_architecture
  - Robotics_autonomous
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Architecture"
  - "Resilience and Safety"
external_links:
  - name: "ACM Digital Library"
    url: "https://dl.acm.org/doi/10.1145/3466752.3480111"
abstract: "GPUs are used in high-reliability systems, including high-performance computers and autonomous vehicles. Because GPUs employ a high-bandwidth, wide-interface to DRAM and fetch each memory access from a single DRAM device, implementing full-device correction through ECC is expensive and impractical. "
url: "https://research.nvidia.com/publication/2021-10_characterizing-and-mitigating-soft-errors-gpu-dram-0"
status: new
---

# Characterizing and Mitigating Soft Errors in GPU DRAM

## 摘要

GPUs are used in high-reliability systems, including high-performance computers and autonomous vehicles. Because GPUs employ a high-bandwidth, wide-interface to DRAM and fetch each memory access from a single DRAM device, implementing full-device correction through ECC is expensive and impractical. This challenge is compounded by worsening relative rates of multi-bit DRAM errors and increasing GPU memory capacities. This paper first presents high-energy neutron beam testing results for the HBM2 memory on a compute-class GPU. These results uncovered unexpected intermittent errors that we determine to be caused by cell damage from the high-intensity beam. As these errors are an artifact of the testing apparatus, we provide best-practice guidance on how to identify and filter them from the results of beam testing campaigns. Second, we use the soft error beam testing results to inform the design and evaluation of system-level error protection mechanisms by reporting the relative error rates and error patterns from soft errors in GPU DRAM. We observe locality in the multi-bit errors, which we attribute to the underlying structure of the HBM2 memory. Based on these error patterns, we propose several novel ECC schemes to decrease the silent data corruption risk by up to five orders of magnitude relative to SEC-DED ECC, while also reducing the number of uncorrectable errors by up to 7.87 ×. We compare novel binary and symbol-based ECC organizations that differ in their design complexity, hardware overheads, and permanent error correction abilities, ultimately recommending two promising organizations. These schemes replace SEC-DED ECC with no additional redundancy, likely no performance impacts, and modest area and complexity costs.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
