---
id: "arxiv-3043"
title: "Speculative Reconvergence for Improved SIMT Efficiency"
conference: "arXiv 2020"
date: "2020-02"
authors:
  - name: "Sana Damani"
    affiliation: "Georgia Institute of Technology"
    is_industry: false
  - name: "Daniel Johnson"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Mark Stephenson"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Eddie Yan"
    affiliation: "University of Washington"
    is_industry: false
  - name: "Olivier Giroux"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Michael McKeown"
    affiliation: "Esperanto Technologies"
    is_industry: false
  - name: "Steve Keckler"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - CUDA_ecosystem
  - GPU_architecture
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Architecture"
  - "Programming Languages, Systems and Tools"
external_links:
  - name: "ACM Digital Library"
    url: "https://dl.acm.org/doi/10.1145/3368826.3377911"
abstract: "GPUs perform most efficiently when all threads in a warp execute the same sequence of instructions convergently. However, when threads in a warp encounter a divergent branch, the hardware serializes the execution of diverged paths. We consider a class of convergence opportunities wherein multiple th"
url: "https://research.nvidia.com/publication/2020-02_speculative-reconvergence-improved-simt-efficiency"
status: "new"
---

# Speculative Reconvergence for Improved SIMT Efficiency

## 摘要

GPUs perform most efficiently when all threads in a warp execute the same sequence of instructions convergently. However, when threads in a warp encounter a divergent branch, the hardware serializes the execution of diverged paths. We consider a class of convergence opportunities wherein multiple threads are expected to eventually execute a given segment of code, but not all threads arrive at the same time, resulting in serialized duplicate execution of common code subsequences such as function calls and loop bodies. Our goal is to promote convergence by helping threads that execute common code arrive together before allowing execution to proceed. We propose a new user-guided compiler mechanism, Speculative Reconvergence, to help identify and exploit previously untapped convergence opportunities that increase SIMT efficiency and improve performance. For the set of workloads we study, we see improvements ranging from 10% to 3× in both SIMT efficiency and in performance.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
