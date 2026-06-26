---
id: "arxiv-2687"
title: "Implementing Reinforcement Learning Datacenter Congestion Control in NVIDIA NICs"
conference: "arXiv 2023"
date: "2023-01"
authors:
  - name: "Benjamin Fuhrer"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yuval Shpigelman"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Chen Tessler"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Shie Mannor"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Gal Chechik"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Eitan Zahavy"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Gal Dalal"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - Interconnect_networking
  - Simulation_HPC
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "High Performance Computing"
  - "Networking"
abstract: "As communication protocols evolve, datacenter network utilization increases. As a result, congestion is more frequent, causing higher latency and packet loss. Combined with the increasing complexity of workloads, manual design of congestion control (CC) algorithms becomes extremely difficult. This c"
url: "https://research.nvidia.com/publication/2023-01_implementing-reinforcement-learning-datacenter-congestion-control-nvidia-nics"
status: "new"
---

# Implementing Reinforcement Learning Datacenter Congestion Control in NVIDIA NICs

## 摘要

As communication protocols evolve, datacenter network utilization increases. As a result, congestion is more frequent, causing higher latency and packet loss. Combined with the increasing complexity of workloads, manual design of congestion control (CC) algorithms becomes extremely difficult. This calls for the development of AI approaches to replace the human effort. Unfortunately, it is currently not possible to deploy AI models on network devices due to their limited computational capabilities. Here, we offer a solution to this problem by building a computationally-light solution based on a recent reinforcement learning CC algorithm [arXiv:2207.02295]. We reduce the inference time of RL-CC by x500 by distilling its complex neural network into decision trees. This transformation enables real-time inference within the&nbsp;μ-sec decision-time requirement, with a negligible effect on quality. We deploy the transformed policy on NVIDIA NICs in a live cluster. Compared to popular CC algorithms used in production, RL-CC is the only method that performs well on all benchmarks tested over a large range of number of flows. It balances multiple metrics simultaneously: bandwidth, latency, and packet drops. These results suggest that data-driven methods for CC are feasible, challenging the prior belief that handcrafted heuristics are necessary to achieve optimal performance.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
