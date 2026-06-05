---
id: arxiv-2523
title: "Beyond Behavior Cloning in Autonomous Driving: a Survey of Closed-Loop Training Techniques"
conference: arXiv 2025
date: 2025-12
authors:
  - name: "Peter Karkus"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Maximilian Igl"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yuxiao Chen"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Bertrand Douillard"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Thomas Tian"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Alperen Degirmenci"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Boris Ivanovic"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Marco Pavone"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Kashyap Chitta"
    affiliation: ""
    is_industry: false
  - name: "Jef Packer"
    affiliation: ""
    is_industry: false
  - name: "Alexander Naumann"
    affiliation: ""
    is_industry: false
  - name: "Guillermo Garcia-Cobo"
    affiliation: ""
    is_industry: false
  - name: "Shuhan Tan"
    affiliation: ""
    is_industry: false
  - name: "Alexander Popov"
    affiliation: ""
    is_industry: false
  - name: "Nikolai Smolyanskiy"
    affiliation: ""
    is_industry: false
  - name: "Urs Muller"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Computer Vision
  - Foundation_models
  - Robotics_autonomous
  - Simulation_HPC
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Autonomous Vehicles"
  - "Computer Vision"
  - "Generative AI"
  - "Physical AI"
  - "World Simulation"
abstract: "Behavior cloning, the dominant approach for training autonomous vehicle (AV) policies, suffers from a fundamental gap: policies trained open-loop on temporally independent samples must operate in closed-loop where actions influence future observations. This mismatch can cause covariate shift, compou"
url: "https://research.nvidia.com/publication/2025-12_beyond-behavior-cloning-autonomous-driving-survey-closed-loop-training"
status: new
---

# Beyond Behavior Cloning in Autonomous Driving: a Survey of Closed-Loop Training Techniques

## 摘要

Behavior cloning, the dominant approach for training autonomous vehicle (AV) policies, suffers from a fundamental gap: policies trained open-loop on temporally independent samples must operate in closed-loop where actions influence future observations. This mismatch can cause covariate shift, compounding errors, and poor interactive behavior, among other issues. Closed-loop training mitigates the problem by exposing policies to the consequences of their actions during training. However, the recent shift to end-to-end ("sensor to action'') systems has made closed-loop training significantly more complex, requiring costly high-dimensional rendering and managing sim-to-real gaps. This survey presents a comprehensive taxonomy of closed-loop training techniques for end-to-end driving, organized along three axes: action generation (policy rollouts vs. perturbed demonstrations); environment response generation (real-world data collection, AV simulation, generative video and latent world models); and training objectives (closed-loop imitation, reinforcement learning, and their combinations). We analyze key trade-offs along each axis: on-policy vs. on-expert action generation, environment fidelity vs. cost, and expert vs. reward-based training objectives; as well as coupling factors, such as rollout deviation from the policy, expert, and real world logs; and data type, throughput, and latency requirements. The analysis reveals gaps between current research and industry practice, and points to promising directions for future work.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
