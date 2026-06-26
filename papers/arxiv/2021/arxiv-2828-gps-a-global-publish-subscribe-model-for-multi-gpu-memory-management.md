---
id: "arxiv-2828"
title: "GPS: A Global Publish-Subscribe Model for Multi-GPU Memory Management"
conference: "arXiv 2021"
date: "2021-10"
authors:
  - name: "Harini Muthukrishnan"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Daniel Lustig"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "David Nellans"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Thomas Wenisch"
    affiliation: "University of Michigan"
    is_industry: false
topics:
  - GPU_architecture
  - Interconnect_networking
  - Simulation_HPC
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Architecture"
  - "High Performance Computing"
  - "Networking"
external_links:
  - name: "ACM Digital Library"
    url: "https://dl.acm.org/doi/10.1145/3466752.3480088"
abstract: "Suboptimal management of memory and bandwidth is one of the primary causes of low performance on systems comprising multiple GPUs. Existing memory management solutions like Unified Memory (UM) offer simplified programming but come at the cost of performance: applications can even exhibit slowdown wi"
url: "https://research.nvidia.com/publication/2021-10_gps-global-publish-subscribe-model-multi-gpu-memory-management"
status: "new"
---

# GPS: A Global Publish-Subscribe Model for Multi-GPU Memory Management

## 摘要

Suboptimal management of memory and bandwidth is one of the primary causes of low performance on systems comprising multiple GPUs. Existing memory management solutions like Unified Memory (UM) offer simplified programming but come at the cost of performance: applications can even exhibit slowdown with increasing GPU count due to their inability to leverage system resources effectively. To solve this challenge, we propose GPS, a HW/SW multi-GPU memory management technique that efficiently orchestrates inter-GPU communication using proactive data transfers. GPS offers the programmability advantage of multi-GPU shared memory with the performance of GPU-local memory. To enable this, GPS automatically tracks the data accesses performed by each GPU, maintains duplicate physical replicas of shared regions in each GPU’s local memory, and pushes updates to the replicas in all consumer GPUs. GPS is compatible within the existing NVIDIA GPU memory consistency model but takes full advantage of its relaxed nature to deliver high performance. We evaluate GPS in the context of a 4-GPU system with varying interconnects and show that GPS achieves an average speedup of 3.0× relative to the performance of a single GPU, outperforming the next best available multi-GPU memory management technique by 2.3× on average. In a 16-GPU system, using a future PCIe 6.0 interconnect, we demonstrate a 7.9× average strong scaling speedup over single-GPU performance, capturing 80% of the available opportunity.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
