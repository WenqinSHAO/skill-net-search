---
id: iros-0001
title: "ACGD: Visual Multitask Policy Learning with Asymmetric Critic Guided Distillation"
conference: IROS 2025
date: 2025-10
authors:
  - name: "Jie Xu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Krishnan Srinivasan"
    affiliation: ""
    is_industry: false
  - name: "Henry Ang"
    affiliation: ""
    is_industry: false
  - name: "Eric Heiden"
    affiliation: ""
    is_industry: false
  - name: "Dieter Fox"
    affiliation: ""
    is_industry: false
  - name: "Jeannette Bohg"
    affiliation: ""
    is_industry: false
  - name: "Animesh Garg"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Robotics_autonomous
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Robotics"
external_links:
  - name: "Project Website"
    url: "https://critic-guided-distillation.github.io/"
abstract: "ACGD introduces a novel approach to visual multitask policy learning by leveraging asymmetric critics to guide the distillation process. Our method trains single-task expert policies and their corresponding critics using privileged state information. These experts are then used to distill a unified "
url: "https://research.nvidia.com/publication/2025-10_acgd-visual-multitask-policy-learning-asymmetric-critic-guided-distillation"
status: new
---

# ACGD: Visual Multitask Policy Learning with Asymmetric Critic Guided Distillation

## 摘要

ACGD introduces a novel approach to visual multitask policy learning by leveraging asymmetric critics to guide the distillation process. Our method trains single-task expert policies and their corresponding critics using privileged state information. These experts are then used to distill a unified multi-task student policy that can generalize across diverse tasks. The student policy employs a VQ-VAE architecture with a transformer-based encoder and decoder, enabling it to predict discrete action tokens from image observations and robot states. We evaluate ACGD on three challenging multi-task domains—MyoDex, BiDex, and OpDex—and demonstrate significant improvements over baseline methods such as BC-RNN+DAgger, ACT, and MT-PPO. ACGD achieves a 10-15% performance boost across various dexterous manipulation benchmarks, showcasing its effectiveness in scaling to high degrees of freedom and complex visuomotor tasks.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
