---
id: arxiv-2848
title: "Cooperative Profile Guided Optimization"
conference: arXiv 2021
date: 2021-07
authors:
  - name: "Mark Stephenson"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Steve Keckler"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ram Rangan"
    affiliation: ""
    is_industry: false
topics:
  - CUDA_ecosystem
  - Graphics_rendering
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Graphics"
  - "Programming Languages, Systems and Tools"
  - "Real-Time Rendering"
external_links:
  - name: "Wiley Online Library"
    url: "https://onlinelibrary.wiley.com/doi/abs/10.1111/cgf.14382"
abstract: "Existing feedback-driven optimization frameworks are not suitable for video games, which tend to push the limits of performance of gaming platforms and have real-time constraints that preclude all but the simplest execution profiling. While Profile Guided Optimization (PGO) is a well-established opt"
url: "https://research.nvidia.com/publication/2021-07_cooperative-profile-guided-optimization"
status: new
---

# Cooperative Profile Guided Optimization

## 摘要

Existing feedback-driven optimization frameworks are not suitable for video games, which tend to push the limits of performance of gaming platforms and have real-time constraints that preclude all but the simplest execution profiling. While Profile Guided Optimization (PGO) is a well-established optimization approach, existing PGO techniques are ill-suited for games for a number of reasons, particularly because heavyweight profiling makes interactive applications unresponsive. Adaptive optimization frameworks continually collect metrics that guide code specialization optimizations during program execution but have similarly high overheads. We emulate a system, which we call Cooperative PGO, in which the gaming platform collects piecemeal profiles by sampling in both time and space during actual gameplay across many users; stitches the piecemeal profiles together statistically; and creates policies to guide future gameplay. We introduce a three-level hierarchical profiler that is well-suited to graphics APIs, that commonly operates with no overhead and occasionally introduces an average overhead of less than 0.5% during periods of active profiling. This paper examines the practicality of Cooperative PGO using three PGOs as case studies. A PGO that exploits likely zeros is particularly effective, achieving an average speedup of 5%, with a maximum speedup of 15%, over a highly-tuned baseline.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
