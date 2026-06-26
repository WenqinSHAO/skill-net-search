---
id: "arxiv-2911"
title: "Scaling Implicit Parallelism via Dynamic Control Replication"
conference: "arXiv 2021"
date: "2021-02"
authors:
  - name: "Michael Bauer"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Wonchan Lee"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Elliott Slaughter"
    affiliation: "SLAC National Accelerator Laboratory"
    is_industry: false
  - name: "Zhihao Jia"
    affiliation: "Carnegie Mellon University"
    is_industry: false
  - name: "Mario Di Renzo"
    affiliation: "Sapienza University of Rome"
    is_industry: false
  - name: "Manolis Papadakis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Galen Shipman"
    affiliation: "Los Alamos National Laboratory"
    is_industry: false
  - name: "Patrick McCormick"
    affiliation: "Los Alamos National Laboratory"
    is_industry: false
  - name: "Michael Garland"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Alex Aiken"
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
external_links:
  - name: "Legion"
    url: "https://legion.stanford.edu/"
  - name: "Code"
    url: "https://gitlab.com/StanfordLegion/legion"
abstract: "We present dynamic control replication, a run-time program analysis that enables scalable execution of implicitly parallel programs on large machines through a distributed and efficient dynamic dependence analysis. Dynamic control replication distributes dependence analysis by executing multiple cop"
url: "https://research.nvidia.com/publication/2021-02_scaling-implicit-parallelism-dynamic-control-replication"
status: "new"
---

# Scaling Implicit Parallelism via Dynamic Control Replication

## 摘要

We present dynamic control replication, a run-time program analysis that enables scalable execution of implicitly parallel programs on large machines through a distributed and efficient dynamic dependence analysis. Dynamic control replication distributes dependence analysis by executing multiple copies of an implicitly parallel program while ensuring that they still collectively behave as a single execution. By distributing and parallelizing the dependence analysis, dynamic control replication supports efficient, on-the-fly computation of dependences for programs with arbitrary control flow at scale. We describe an asymptotically scalable algorithm for implementing dynamic control replication that maintains the sequential semantics of implicitly parallel programs.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
