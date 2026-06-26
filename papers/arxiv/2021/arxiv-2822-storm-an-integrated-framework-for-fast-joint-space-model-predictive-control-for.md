---
id: "arxiv-2822"
title: "STORM: An Integrated Framework for Fast Joint-Space Model-Predictive Control for Reactive Manipulation"
conference: "arXiv 2021"
date: "2021-11"
authors:
  - name: "Mohak Bhardwaj"
    affiliation: "University of Washington"
    is_industry: false
  - name: "Balakumar Sundaralingam"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Arsalan Mousavian"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Nathan Ratliff"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Dieter Fox"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Fabio Ramos"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Byron Boots"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Robotics"
external_links:
  - name: "Website"
    url: "https://sites.google.com/view/manipulation-mpc"
  - name: "Code"
    url: "https://github.com/NVlabs/storm"
abstract: "Sampling-based model-predictive control (MPC) is a promising tool for feedback control of robots with complex, non-smooth dynamics, and cost functions. However, the computationally demanding nature of sampling-based MPC algorithms has been a key bottleneck in their application to high-dimensional ro"
url: "https://research.nvidia.com/publication/2021-11_storm-integrated-framework-fast-joint-space-model-predictive-control-reactive"
status: "new"
---

# STORM: An Integrated Framework for Fast Joint-Space Model-Predictive Control for Reactive Manipulation

## 摘要

Sampling-based model-predictive control (MPC) is a promising tool for feedback control of robots with complex, non-smooth dynamics, and cost functions. However, the computationally demanding nature of sampling-based MPC algorithms has been a key bottleneck in their application to high-dimensional robotic manipulation problems in the real world. Previous methods have addressed this issue by running MPC in the task space while relying on a low-level operational space controller for joint control. However, by not using the joint space of the robot in the MPC formulation, existing methods cannot directly account for non-task space related constraints such as avoiding joint limits, singular configurations, and link collisions. In this paper, we develop a system for fast, joint space sampling-based MPC for manipulators that is efficiently parallelized using GPUs. Our approach can handle task and joint space constraints while taking less than 8ms~(125Hz) to compute the next control command. Further, our method can tightly integrate perception into the control problem by utilizing learned cost functions from raw sensor data. We validate our approach by deploying it on a Franka Panda robot for a variety of dynamic manipulation tasks. We study the effect of different cost formulations and MPC parameters on the synthesized behavior and provide key insights that pave the way for the application of sampling-based MPC for manipulators in a principled manner. We also provide highly optimized, open-source code to be used by the wider robot learning and control community.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
