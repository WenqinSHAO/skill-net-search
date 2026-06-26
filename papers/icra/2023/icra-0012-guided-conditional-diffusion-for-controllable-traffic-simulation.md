---
id: "icra-0012"
title: "Guided Conditional Diffusion for Controllable Traffic Simulation"
conference: "ICRA 2023"
date: "2023-05"
authors:
  - name: "Ziyuan Zhong"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Davis Rempe"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Danfei Xu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yuxiao Chen"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Sushant Veer"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Gerry Che"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Baishakhi Ray"
    affiliation: "Columbia University"
    is_industry: false
  - name: "Marco Pavone"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Foundation_models
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Autonomous Vehicles"
  - "Generative AI"
external_links:
  - name: "Paper"
    url: "https://arxiv.org/abs/2210.17366"
  - name: "Website"
    url: "https://aiasd.github.io/ctg.github.io/"
abstract: "Controllable and realistic traffic simulation is critical for developing and verifying autonomous vehicles. Typical heuristic-based traffic models offer flexible control to make vehicles follow specific trajectories and traffic rules. On the other hand, data-driven approaches generate realistic and "
url: "https://research.nvidia.com/publication/2023-05_guided-conditional-diffusion-controllable-traffic-simulation"
status: "new"
---

# Guided Conditional Diffusion for Controllable Traffic Simulation

## 摘要

Controllable and realistic traffic simulation is critical for developing and verifying autonomous vehicles. Typical heuristic-based traffic models offer flexible control to make vehicles follow specific trajectories and traffic rules. On the other hand, data-driven approaches generate realistic and human-like behaviors, improving transfer from simulated to real-world traffic. However, to the best of our knowledge, no traffic model offers both controllability and realism. In this work, we develop a conditional diffusion model for controllable traffic generation (CTG) that allows users to control desired properties of trajectories at test time (e.g., reach a goal or follow a speed limit) while maintaining realism and physical feasibility through enforced dynamics. The key technical idea is to leverage recent advances from diffusion modeling and differentiable logic to guide generated trajectories to meet rules defined using signal temporal logic (STL). We further extend guidance to multi-agent settings and enable interaction-based rules like collision avoidance. CTG is extensively evaluated on the nuScenes dataset for diverse and composite rules, demonstrating improvement over strong baselines in terms of the controllability-realism tradeoff.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
