---
id: iclr-0032
title: "Accelerated Policy Learning with Parallel Differentiable Simulation"
conference: ICLR 2022
date: 2022-05
authors:
  - name: "Jie Xu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yashraj Narang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Fabio Ramos"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Viktor Makoviychuk"
    affiliation: ""
    is_industry: false
  - name: "Wojciech Matusik"
    affiliation: ""
    is_industry: false
  - name: "Animesh Garg"
    affiliation: ""
    is_industry: false
  - name: "Miles Macklin"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Graphics_rendering
  - Robotics_autonomous
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
  - "Robotics"
external_links:
  - name: "Project Website"
    url: "https://short-horizon-actor-critic.github.io/"
  - name: "Paper"
    url: "https://openreview.net/forum?id=ZSKRQMvttc"
  - name: "Code"
    url: "https://github.com/NVlabs/DiffRL"
  - name: "Talk"
    url: "https://iclr.cc/virtual/2022/poster/6923"
abstract: "Deep reinforcement learning can generate complex control policies, but requires large amounts of training data to work effectively. Recent work has attempted to address this issue by leveraging differentiable simulators. However, inherent problems such as local minima and exploding/vanishing numeric"
url: "https://research.nvidia.com/publication/2022-05_accelerated-policy-learning-parallel-differentiable-simulation"
status: new
---

# Accelerated Policy Learning with Parallel Differentiable Simulation

## 摘要

Deep reinforcement learning can generate complex control policies, but requires large amounts of training data to work effectively. Recent work has attempted to address this issue by leveraging differentiable simulators. However, inherent problems such as local minima and exploding/vanishing numerical gradients prevent these methods from being generally applied to control tasks with complex contact-rich dynamics, such as humanoid locomotion in classical RL benchmarks. In this work we present a high-performance differentiable simulator and a new policy learning algorithm (SHAC) that can effectively leverage simulation gradients, even in the presence of non-smoothness. Our learning algorithm alleviates problems with local minima through a smooth critic function, avoids vanishing/exploding gradients through a truncated learning window, and allows many physical environments to be run in parallel. We evaluate our method on classical RL control tasks, and show substantial improvements in sample efficiency and wall-clock time over state-of-the-art RL and differentiable simulation-based algorithms. In addition, we demonstrate the scalability of our method by applying it to the challenging high-dimensional problem of muscle-actuated locomotion with a large action space, achieving a greater than 17x reduction in training time over the best-performing established RL algorithm.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
