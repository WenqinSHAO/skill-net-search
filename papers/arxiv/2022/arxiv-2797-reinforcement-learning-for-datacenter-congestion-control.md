---
id: "arxiv-2797"
title: "Reinforcement Learning for Datacenter Congestion Control"
conference: "arXiv 2022"
date: "2022-02"
authors:
  - name: "Chen Tessler"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yuval Shpigelman"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Gal Dalal"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Amit Mendelbaum"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Doron Kazakov"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Benjamin Fuhrer"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Gal Chechik"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Shie Mannor"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Interconnect_networking
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Networking"
abstract: "We approach the task of network congestion control in datacenters using Reinforcement Learning (RL). Successful congestion control algorithms can dramatically improve latency and overall network throughput. Until today, no such learning-based algorithms have shown practical potential in this domain."
url: "https://research.nvidia.com/publication/2022-02_reinforcement-learning-datacenter-congestion-control"
status: "new"
---

# Reinforcement Learning for Datacenter Congestion Control

## 摘要

We approach the task of network congestion control in datacenters using Reinforcement Learning (RL). Successful congestion control algorithms can dramatically improve latency and overall network throughput. Until today, no such learning-based algorithms have shown practical potential in this domain. Evidently, the most popular recent deployments rely on rule-based heuristics that are tested on a predetermined set of benchmarks. Consequently, these heuristics do not generalize well to newly-seen scenarios. Contrarily, we devise an RL-based algorithm with the aim of generalizing to different configurations of real-world datacenter networks. We overcome challenges such as partial-observability, non-stationarity, and multi-objectiveness. We further propose a policy gradient algorithm that leverages the analytical structure of the reward function to approximate its derivative and improve stability. We show that this scheme outperforms alternative popular RL approaches, and generalizes to scenarios that were not seen during training. Our experiments, conducted on a realistic simulator that emulates communication networks' behavior, exhibit improved performance concurrently on the multiple considered metrics compared to the popular algorithms deployed today in real datacenters. Our algorithm is being productized to replace heuristics in some of the largest datacenters in the world.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
