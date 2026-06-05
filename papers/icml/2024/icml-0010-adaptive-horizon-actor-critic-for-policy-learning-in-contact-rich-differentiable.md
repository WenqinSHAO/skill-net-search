---
id: icml-0010
title: "Adaptive Horizon Actor-Critic for Policy Learning in Contact-Rich Differentiable Simulation"
conference: ICML 2024
date: 2024-07
authors:
  - name: "Jie Xu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ignat Georgiev"
    affiliation: ""
    is_industry: false
  - name: "Krishnan Srinivasan"
    affiliation: ""
    is_industry: false
  - name: "Eric Heiden"
    affiliation: ""
    is_industry: false
  - name: "Animesh Garg"
    affiliation: ""
    is_industry: false
topics:
  - Robotics_autonomous
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Robotics"
external_links:
  - name: "Project Website"
    url: "https://adaptive-horizon-actor-critic.github.io/"
abstract: "Model-Free Reinforcement Learning (MFRL), leveraging the policy gradient theorem, has demonstrated considerable success in continuous control tasks. However, these approaches are plagued by high gradient variance due to zeroth-order gradient estimation, resulting in suboptimal policies. Conversely, "
url: "https://research.nvidia.com/publication/2024-07_adaptive-horizon-actor-critic-policy-learning-contact-rich-differentiable"
status: new
---

# Adaptive Horizon Actor-Critic for Policy Learning in Contact-Rich Differentiable Simulation

## 摘要

Model-Free Reinforcement Learning (MFRL), leveraging the policy gradient theorem, has demonstrated considerable success in continuous control tasks. However, these approaches are plagued by high gradient variance due to zeroth-order gradient estimation, resulting in suboptimal policies. Conversely, First-Order Model-Based Reinforcement Learning~(FO-MBRL) methods employing differentiable simulation provide gradients with reduced variance but are susceptible to bias in scenarios involving stiff dynamics, such as physical contact. This paper investigates the source of this bias and introduces Adaptive Horizon Actor-Critic (AHAC), an FO-MBRL algorithm that reduces gradient bias by adapting the model-based horizon to avoid stiff dynamics. Empirical findings reveal that AHAC outperforms MFRL baselines, attaining 40% more reward across a set of locomotion tasks and efficiently scaling to high-dimensional control environments with improved wall-clock-time efficiency.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
