---
id: "arxiv-2941"
title: "The Architectural Implications of Distributed Reinforcement Learning on CPU-GPU Systems"
conference: "arXiv 2020"
date: "2020-12"
authors:
  - name: "Ahmet Inci"
    affiliation: "CMU"
    is_industry: false
  - name: "Evgeny Bolotin"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yaosheng Fu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Gal Dalal"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Shie Mannor"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "David Nellans"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Diana Marculescu"
    affiliation: "UT Austin"
    is_industry: false
topics:
  - GPU_architecture
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Architecture"
external_links:
  - name: "EMC2"
    url: "https://www.emc2-ai.org/assets/docs/virtual-20/emc2-virtual20-paper-10.pdf"
abstract: "With deep reinforcement learning (RL) methods achieving results that exceed human capabilities in games, robotics, and simulated environments, continued scaling of RL training is crucial to its deployment in solving complex real-world problems. However, improving the performance scalability and powe"
url: "https://research.nvidia.com/publication/2020-12_architectural-implications-distributed-reinforcement-learning-cpu-gpu-systems"
status: "new"
---

# The Architectural Implications of Distributed Reinforcement Learning on CPU-GPU Systems

## 摘要

With deep reinforcement learning (RL) methods achieving results that exceed human capabilities in games, robotics, and simulated environments, continued scaling of RL training is crucial to its deployment in solving complex real-world problems. However, improving the performance scalability and power efﬁciency of RL training through understanding the architectural implications of CPU-GPU systems remains an open problem. In this work we investigate and improve the performance and power efﬁciency of distributed RL training on CPU-GPU systems by approaching the problem not solely from the GPU microarchitecture perspective but following a holistic system-level analysis approach. We quantify the overall hardware utilization on a state-of-the-art distributed RL training framework and empirically identify the bottlenecks caused by GPU microarchitectural, algorithmic, and system-level design choices. We show that the GPU microarchitecture itself is well-balanced for state-of-the-art RL frameworks, but further investigation reveals that the number of actors running the environment interactions and the amount of hardware resources available to them are the primary performance and power efﬁciency limiters. To this end, we introduce a new system design metric, CPU/GPU ratio, and show how to ﬁnd the optimal balance between CPU and GPU resources when designing scalable and efﬁcient CPU-GPU systems for RL training.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
