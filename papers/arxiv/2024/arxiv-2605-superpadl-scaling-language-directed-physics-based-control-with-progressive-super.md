---
id: arxiv-2605
title: "SuperPADL: Scaling Language-Directed Physics-Based Control with Progressive Supervised Distillation"
conference: arXiv 2024
date: 2024-07
authors:
topics:
  - Foundation_models
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Generative AI"
abstract: "Physically-simulated models for human motion can generate high-quality responsive character animations, often in real-time. Natural language serves as a flexible interface for controlling these models, allowing expert and non-expert users to quickly create and edit their animations. Many recent phys"
url: "https://research.nvidia.com/publication/2024-07_superpadl-scaling-language-directed-physics-based-control-progressive"
status: new
---

# SuperPADL: Scaling Language-Directed Physics-Based Control with Progressive Supervised Distillation

## 摘要

Physically-simulated models for human motion can generate high-quality responsive character animations, often in real-time. Natural language serves as a flexible interface for controlling these models, allowing expert and non-expert users to quickly create and edit their animations. Many recent physics-based animation methods, including those that use text interfaces, train control policies using reinforcement learning (RL). However, scaling these methods beyond several hundred motions has remained challenging. Meanwhile, kinematic animation models are able to successfully learn from thousands of diverse motions by leveraging supervised learning methods. Inspired by these successes, in this work we introduce SuperPADL, a scalable framework for physics-based text-to-motion that leverages both RL and supervised learning to train controllers on thousands of diverse motion clips. SuperPADL is trained in stages using progressive distillation, starting with a large number of specialized experts using RL. These experts are then iteratively distilled into larger, more robust policies using a combination of reinforcement learning and supervised learning. Our trained SuperPADL controller runs in real time on a consumer GPU, and can reproduce motions with high fidelity from a dataset of over 5000 skills. Moreover, our policy can naturally transition between skills, allowing for users to interactively craft complicated animations. We experimentally demonstrate that SuperPADL significantly outperforms RL-based baselines at this large data scale.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
