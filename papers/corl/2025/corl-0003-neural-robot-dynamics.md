---
id: corl-0003
title: "Neural Robot Dynamics"
conference: CoRL 2025
date: 2025-09
authors:
  - name: "Jie Xu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Iretiayo Akinola"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yashraj Narang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Eric Heiden"
    affiliation: ""
    is_industry: false
  - name: "Dieter Fox"
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
    url: "https://neural-robot-dynamics.github.io/"
  - name: "Code"
    url: "https://github.com/NVlabs/neural-robot-dynamics"
abstract: "Accurate and efficient simulation of modern robots remains challenging due to their high degrees of freedom and intricate mechanisms. Neural simulators have emerged as a promising alternative to traditional analytical simulators, capable of efficiently predicting complex dynamics and adapting to rea"
url: "https://research.nvidia.com/publication/2025-09_neural-robot-dynamics"
status: new
---

# Neural Robot Dynamics

## 摘要

Accurate and efficient simulation of modern robots remains challenging due to their high degrees of freedom and intricate mechanisms. Neural simulators have emerged as a promising alternative to traditional analytical simulators, capable of efficiently predicting complex dynamics and adapting to real-world data; however, existing neural simulators typically require application-specific training and fail to generalize to novel tasks and/or environments, primarily due to inadequate representations of the global state. In this work, we address the problem of learning generalizable neural simulators for robots that are structured as articulated rigid bodies. We propose NeRD (Neural Robot Dynamics), learned robot-specific dynamics models for predicting future states for articulated rigid bodies under contact constraints. NeRD uniquely replaces the low-level dynamics and contact solvers in an analytical simulator and employs a robot-centric and spatially-invariant simulation state representation. We integrate the learned NeRD models as an interchangeable backend solver within a state-of-the-art robotics simulator. We conduct extensive experiments to show that the NeRD simulators are stable and accurate over a thousand simulation steps; generalize across tasks and environment configurations; enable policy learning exclusively in a neural engine; and, unlike most classical simulators, can be fine-tuned from real-world data to bridge the gap between simulation and reality.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
