---
id: "arxiv-2783"
title: "Characterizing and Mitigating Soft Errors in GPU DRAM"
conference: "arXiv 2022"
date: "2022-03"
authors:
  - name: "Michael B. Sullivan"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Nirmal R. Saxena"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Mike O'Connor"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Donghyuk Lee"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Paul Racunas"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Saurabh Hukerikar"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Timothy Tsai"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Siva Kumar Sastry Hari"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Stephen W. Keckler"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Mike O&#039;Connor"
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
external_links:
  - name: "IEEE Digital Library"
    url: "https://ieeexplore.ieee.org/document/9744333"
abstract: "While graphics processing units (GPUs) are used in high-reliability systems,wide GPU dynamic random-access memory (DRAM) interfaces make error protection difficult, as wide-device correction through error checking and correcting (ECC) is expensive and impractical. This challenge is compounded by wor"
url: "https://research.nvidia.com/publication/2022-03_characterizing-and-mitigating-soft-errors-gpu-dram"
status: "new"
---

# Characterizing and Mitigating Soft Errors in GPU DRAM

## 摘要

While graphics processing units (GPUs) are used in high-reliability systems,wide GPU dynamic random-access memory (DRAM) interfaces make error protection difficult, as wide-device correction through error checking and correcting (ECC) is expensive and impractical. This challenge is compounded by worsening relative rates of multibit DRAM errors and increasing GPU memory capacities. This work uses high-energy neutron beam tests to inform the design and evaluation of GPU DRAM error-protection mechanisms. Based on observed locality in multibit error patterns, we propose several novel ECC schemes to decrease the silent data corruption (SDC) risk by up to five orders of magnitude relative to single-bit-error-correcting and double-bit-error-detecting (SECDED) ECC, while also reducing the number of uncorrectable errors by up to 7.87x. We compare novel binary and symbol-based ECC organizations that differ in their design complexity and hardware overheads, ultimately recommending two promising organizations. These schemes replace SEC-DED ECC with no additional redundancy, likely no performance degradation, and modest area and complexity costs.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
