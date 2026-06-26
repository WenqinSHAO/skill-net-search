---
id: "arxiv-3071"
title: "OASIS: Object-Aware Page Management for Multi-GPU Systems"
conference: "arXiv 2025"
date: "2025-02"
authors:
  - name: "Yueqi Wang"
    affiliation: "University of Pittsburgh"
    is_industry: false
  - name: "Bingyao Li"
    affiliation: "University of Pittsburgh"
    is_industry: false
  - name: "Mohamed Tarek Ibn Ziad"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Lieven Eeckhout"
    affiliation: "Ghent University"
    is_industry: false
  - name: "Jun Yang"
    affiliation: "University of Pittsburgh"
    is_industry: false
  - name: "Aamer Jaleel"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Xulong Tang"
    affiliation: "University of Pittsburgh"
    is_industry: false
topics:
  - GPU_architecture
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Architecture"
abstract: "The ever-growing need for high-performance computing has driven the popularity of employing multi-GPU systems. Modern multi-GPU systems employ unified virtual memory (UVM) to manage page placement and migration. However, the page management in UVM is application object agnostic. In this paper, we ch"
url: "https://research.nvidia.com/publication/2025-02_oasis-object-aware-page-management-multi-gpu-systems"
status: "new"
---

# OASIS: Object-Aware Page Management for Multi-GPU Systems

## 摘要

The ever-growing need for high-performance computing has driven the popularity of employing multi-GPU systems. Modern multi-GPU systems employ unified virtual memory (UVM) to manage page placement and migration. However, the page management in UVM is application object agnostic. In this paper, we characterize the page access behaviors in relation to the application objects, and reveal that the beneficial page management policy varies according to (i) the different data objects within the same application, and (ii) the different execution phases of the same object. This motivates the need for dynamic and proactive page management in multi-GPU systems. To this end, we propose OASIS, which dynamically identifies object patterns during the execution and proactively determines the appropriate page management policies for these objects at runtime. Experimental results show that OASIS improves the performance over uniformly adopting on-touch migration, access counter-based migration, and duplication by an average of 64%, 35%, and 42%, respectively. Moreover, OASIS achieves a 12% performance improvement over the state-of-the-art technique (i.e., GRIT) while having significantly lower design complexity.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
