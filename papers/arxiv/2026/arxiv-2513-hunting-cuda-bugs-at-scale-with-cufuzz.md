---
id: arxiv-2513
title: "Hunting CUDA Bugs at Scale with cuFuzz"
conference: arXiv 2026
date: 2026-03
authors:
  - name: "Mohamed Tarek Ibn Ziad"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Christos Kozyrakis"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - CUDA_ecosystem
  - GPU_architecture
  - Miscellaneous
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Architecture"
  - "Programming Languages, Systems and Tools"
  - "Security"
abstract: "GPUs play an increasingly important role in modern software. However, the heterogeneous host-device execution model and expanding software stack make GPU programs prone to memory-safety and concurrency bugs that evade static analyses. While fuzz-testing, combined with dynamic error checking tools, o"
url: "https://research.nvidia.com/publication/2026-03%5Fhunting-cuda-bugs-scale-cufuzz"
status: new
---

# Hunting CUDA Bugs at Scale with cuFuzz

## 摘要

GPUs play an increasingly important role in modern software. However, the heterogeneous host-device execution model and expanding software stack make GPU programs prone to memory-safety and concurrency bugs that evade static analyses. While fuzz-testing, combined with dynamic error checking tools, offers a plausible solution, it remains underutilized for GPUs. In this work, we identify three main obstacles limiting prior GPU fuzzing efforts: (1) kernel-level fuzzing leading to false positives, (2) lack of device-side coverage-guided feedback, and (3) incompatibility between coverage and sanitization tools. We present cuFuzz, the first CUDA-oriented fuzzer that makes GPU fuzzing practical by addressing these obstacles.&nbsp;

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
