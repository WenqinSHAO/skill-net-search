---
id: ispd-0005
title: "AutoDMP: Automated DREAMPlace-based Macro Placement"
conference: ISPD 2023
date: 2023-03
authors:
  - name: "Ben Keller"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Brucek Khailany"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Anthony Agnesina"
    affiliation: ""
    is_industry: false
  - name: "Puranjay Rajvanshi"
    affiliation: ""
    is_industry: false
  - name: "Tian Yang"
    affiliation: ""
    is_industry: false
  - name: "Geraldo Pradipta"
    affiliation: ""
    is_industry: false
  - name: "Austin Jiao"
    affiliation: ""
    is_industry: false
  - name: "Mark Haoxing Ren"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - GPU_architecture
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Circuits and VLSI Design"
external_links:
  - name: "GitHub repo"
    url: "https://github.com/NVlabs/AutoDMP"
abstract: "Macro placement is a critical very large-scale integration (VLSI) physical design problem that significantly impacts the design powerperformance-area (PPA) metrics. This paper proposes AutoDMP, a methodology that leverages DREAMPlace, a GPU-accelerated placer, to place macros and standard cells conc"
url: "https://research.nvidia.com/publication/2023-03_autodmp-automated-dreamplace-based-macro-placement"
status: new
---

# AutoDMP: Automated DREAMPlace-based Macro Placement

## 摘要

Macro placement is a critical very large-scale integration (VLSI) physical design problem that significantly impacts the design powerperformance-area (PPA) metrics. This paper proposes AutoDMP, a methodology that leverages DREAMPlace, a GPU-accelerated placer, to place macros and standard cells concurrently in conjunction with automated parameter tuning using a multi-objective hyperparameter optimization technique. As a result, we can generate high-quality predictable solutions, improving the macro placement quality of academic benchmarks compared to baseline results generated from academic and commercial tools. AutoDMP is also computationally efficient, optimizing a design with 2.7 million cells and 320 macros in 3 hours on a single NVIDIA DGX Station A100. This work demonstrates the promise and potential of combining GPU-accelerated algorithms and ML techniques for VLSI design automation

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
