---
id: "icra-0010"
title: "Receding Horizon Planning with Rule Hierarchies for Autonomous Vehicles"
conference: "ICRA 2023"
date: "2023-05"
authors:
  - name: "Sushant Veer"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Karen Leung"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ryan Cosner"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yuxiao Chen"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Marco Pavone"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Autonomous Vehicles"
  - "Resilience and Safety"
external_links:
  - name: "Paper"
    url: "https://arxiv.org/abs/2212.03323"
abstract: "Autonomous vehicles must often contend with conflicting planning requirements, e.g., safety and comfort could be at odds with each other if avoiding a collision calls for slamming the brakes. To resolve such conflicts, assigning importance ranking to rules (i.e., imposing a rule hierarchy) has been "
url: "https://research.nvidia.com/publication/2023-05_receding-horizon-planning-rule-hierarchies-autonomous-vehicles"
status: "new"
---

# Receding Horizon Planning with Rule Hierarchies for Autonomous Vehicles

## 摘要

Autonomous vehicles must often contend with conflicting planning requirements, e.g., safety and comfort could be at odds with each other if avoiding a collision calls for slamming the brakes. To resolve such conflicts, assigning importance ranking to rules (i.e., imposing a rule hierarchy) has been proposed, which, in turn, induces rankings on trajectories based on the importance of the rules they satisfy. On one hand, imposing rule hierarchies can enhance interpretability, but introduce combinatorial complexity to planning; while on the other hand, differentiable reward structures can be leveraged by modern gradient-based optimization tools, but are less interpretable and unintuitive to tune. In this paper, we present an approach to equivalently express rule hierarchies as differentiable reward structures amenable to modern gradient-based optimizers, thereby, achieving the best of both worlds. We achieve this by formulating rank-preserving reward functions that are monotonic in the rank of the trajectories induced by the rule hierarchy; i.e., higher ranked trajectories receive higher reward. Equipped with a rule hierarchy and its corresponding rank-preserving reward function, we develop a two-stage planner that can efficiently resolve conflicting planning requirements. We demonstrate that our approach can generate motion plans in 7-10 Hz for various challenging road navigation and intersection negotiation scenarios.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
