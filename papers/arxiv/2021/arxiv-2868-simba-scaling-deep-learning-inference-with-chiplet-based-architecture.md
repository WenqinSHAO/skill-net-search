---
id: "arxiv-2868"
title: "Simba: scaling deep-learning inference with chiplet-based architecture"
conference: "arXiv 2021"
date: "2021-05"
authors:
  - name: "Yakun Sophia Shao"
    affiliation: "UC Berkeley"
    is_industry: false
  - name: "Jason Clemons"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Rangharajan Venkatesan"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Brian Zimmer"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Matt Fojtik"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ted Jiang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ben Keller"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Alicia Klinefelter"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Nathaniel Pinckney"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Priyanka Raina"
    affiliation: "Stanford"
    is_industry: false
  - name: "Stephen Tell"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yanqing Zhang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "William Dally"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Joel Emer"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Tom Gray"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Brucek Khailany"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Steve Keckler"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - GPU_architecture
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Circuits and VLSI Design"
  - "Computer Architecture"
external_links:
  - name: "Published manuscript (ACM Digital Library)"
    url: "https://dl.acm.org/doi/10.1145/3460227"
abstract: "Package-level integration using multi-chip-modules (MCMs) is a promising approach for building large-scale systems. Compared to a large monolithic die, an MCM combines many smaller chiplets into a larger system, substantially reducing fabrication and design costs. Current MCMs typically only contain"
url: "https://research.nvidia.com/publication/2021-05_simba-scaling-deep-learning-inference-chiplet-based-architecture"
status: "new"
---

# Simba: scaling deep-learning inference with chiplet-based architecture

## 摘要

Package-level integration using multi-chip-modules (MCMs) is a promising approach for building large-scale systems. Compared to a large monolithic die, an MCM combines many smaller chiplets into a larger system, substantially reducing fabrication and design costs. Current MCMs typically only contain a handful of coarse-grained large chiplets due to the high area, performance, and energy overheads associated with inter-chiplet communication. This work investigates and quantifies the costs and benefits of using MCMs with finegrained chiplets for deep learning inference, an application domain with large compute and on-chip storage requirements. To evaluate the approach, we architected, implemented, fabricated, and tested Simba, a 36-chiplet prototype MCM system for deep-learning inference. Each chiplet achieves 4 TOPS peak performance, and the 36-chiplet MCM package achieves up to 128 TOPS and up to 6.1 TOPS/W. The MCM is configurable to support a flexible mapping of DNN layers to the distributed compute and storage units. To mitigate inter-chiplet communication overheads, we introduce three tiling optimizations that improve data locality. These optimizations achieve up to 16% speedup compared to the baseline layer mapping. Our evaluation shows that Simba can process 1988 images/s running ResNet-50 with a batch size of one, delivering an inference latency of 0.50 ms.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
