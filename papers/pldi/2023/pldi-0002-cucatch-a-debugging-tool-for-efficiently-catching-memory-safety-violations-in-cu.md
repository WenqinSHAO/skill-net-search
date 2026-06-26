---
id: "pldi-0002"
title: "cuCatch: A Debugging Tool for Efficiently Catching Memory Safety Violations in CUDA Applications"
conference: "PLDI 2023"
date: "2023-06"
authors:
  - name: "Mohamed Tarek Ibn Ziad"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Sana Damani"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Aamer Jaleel"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Stephen W. Keckler"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Mark Stephenson"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - CUDA_ecosystem
  - Miscellaneous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Programming Languages, Systems and Tools"
  - "Security"
external_links:
  - name: "ACM Digital Library"
    url: "https://dl.acm.org/doi/10.1145/3591225"
abstract: "CUDA, OpenCL, and OpenACC are the primary means of writing general-purpose software for NVIDIA GPUs, all of which are subject to the same well-documented memory safety vulnerabilities currently plaguing software written in C and C++. One can argue that the GPU execution environment makes software de"
url: "https://research.nvidia.com/publication/2023-06_cucatch-debugging-tool-efficiently-catching-memory-safety-violations-cuda"
status: "new"
---

# cuCatch: A Debugging Tool for Efficiently Catching Memory Safety Violations in CUDA Applications

## 摘要

CUDA, OpenCL, and OpenACC are the primary means of writing general-purpose software for NVIDIA GPUs, all of which are subject to the same well-documented memory safety vulnerabilities currently plaguing software written in C and C++. One can argue that the GPU execution environment makes software development more error prone. Unlike C and C++, CUDA features multiple, distinct memory spaces to map to the GPU’s unique memory hierarchy, and a typical CUDA program has thousands of concurrently executing threads. Furthermore, the CUDA platform has fewer guardrails than CPU platforms that have been forced to incrementally adjust to a barrage of security attacks. Unfortunately, the peculiarities of the GPU make it difficult to directly port memory safety solutions from the CPU space.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
