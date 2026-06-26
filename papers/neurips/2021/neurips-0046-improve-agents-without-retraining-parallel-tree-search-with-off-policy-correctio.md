---
id: "neurips-0046"
title: "Improve Agents without Retraining: Parallel Tree Search with Off-Policy Correction"
conference: "NeurIPS 2021"
date: "2021-10"
authors:
  - name: "Gal Dalal"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Assaf Hallak"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Steven Dalton"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Iuri Frosio"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Shie Mannor"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Gal Chechik"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
external_links:
  - name: "Improve Agents without Retraining: Parallel Tree Search with Off-Policy Correct…"
    url: "https://arxiv.org/abs/2107.01715"
abstract: "Tree Search (TS) is crucial to some of the most influential successes in reinforcement learning. Here, we tackle two major challenges with TS that limit its usability: distribution shift&nbsp;and scalability. We first discover and analyze a counter-intuitive phenomenon: action selection through TS a"
url: "https://research.nvidia.com/publication/2021-10_improve-agents-without-retraining-parallel-tree-search-policy-correction"
status: "new"
---

# Improve Agents without Retraining: Parallel Tree Search with Off-Policy Correction

## 摘要

Tree Search (TS) is crucial to some of the most influential successes in reinforcement learning. Here, we tackle two major challenges with TS that limit its usability: distribution shift&nbsp;and scalability. We first discover and analyze a counter-intuitive phenomenon: action selection through TS and a pre-trained value function often leads to lower performance compared to the original pre-trained agent, even when having access to the exact state and reward in future steps. We show this is due to a distribution shift to areas where value estimates are highly inaccurate and analyze this effect using Extreme Value theory. To overcome this problem, we introduce a novel off-policy correction term that accounts for the mismatch between the pre-trained value and its corresponding TS policy by penalizing under-sampled trajectories. We prove that our correction eliminates the above mismatch and bound the probability of sub-optimal action selection. Our correction significantly improves pre-trained Rainbow agents without any further training, often more than doubling their scores on Atari games. Next, we address the scalability issue given by the computational complexity of exhaustive TS that scales exponentially with the tree depth. We introduce Batch-BFS: a GPU breadth-first search that advances all nodes in each depth of the tree simultaneously. Batch-BFS reduces runtime by two orders of magnitude and, beyond inference, enables also training with TS of depths that were not feasible before. We train DQN agents from scratch using TS and show improvement in several Atari games compared to both the original DQN and the more advanced Rainbow. We will share the code upon publication.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
