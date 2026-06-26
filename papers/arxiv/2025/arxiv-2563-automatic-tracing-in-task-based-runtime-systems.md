---
id: "arxiv-2563"
title: "Automatic Tracing in Task-Based Runtime Systems"
conference: "arXiv 2025"
date: "2025-03"
authors:
  - name: "Rohan Yadav"
    affiliation: "Stanford University"
    is_industry: false
  - name: "Michael Bauer"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "David Broman"
    affiliation: "KTH Royal Institute of Technology"
    is_industry: false
  - name: "Michael Garland"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Alex Aiken"
    affiliation: "Stanford University"
    is_industry: false
  - name: "Fredrik Kjolstad"
    affiliation: "Stanford University"
    is_industry: false
topics:
  - CUDA_ecosystem
  - Simulation_HPC
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "High Performance Computing"
  - "Programming Languages, Systems and Tools"
abstract: "Implicitly parallel task-based runtime systems often perform dynamic analysis to discover dependencies in and extract parallelism from sequential programs. Dependence analysis becomes expensive as task granularity drops below a threshold. Tracing techniques have been developed where programmers anno"
url: "https://research.nvidia.com/publication/2025-03_automatic-tracing-task-based-runtime-systems"
status: "new"
---

# Automatic Tracing in Task-Based Runtime Systems

## 摘要

Implicitly parallel task-based runtime systems often perform dynamic analysis to discover dependencies in and extract parallelism from sequential programs. Dependence analysis becomes expensive as task granularity drops below a threshold. Tracing techniques have been developed where programmers annotate repeated program fragments (traces) issued by the application, and the runtime system memoizes the dependence analysis for those fragments, greatly reducing overhead when the fragments are executed again. However, manual trace annotation can be brittle and not easily applicable to complex programs built through the composition of independent components. We introduce Apophenia, a system that automatically traces the dependence analysis of task-based runtime systems, removing the burden of manual annotations from programmers and enabling new and complex programs to be traced. Apophenia identifies traces dynamically through a series of dynamic string analyses, which find repeated program fragments in the stream of tasks issued to the runtime system. We show that Apophenia is able to come between 0.92x–1.03x the performance of manually traced programs, and is able to effectively trace previously untraced programs to yield speedups of between 0.91x–2.82x on the Perlmutter and Eos supercomputers.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
