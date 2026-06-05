---
id: icra-0003
title: "SPOT: SE(3) Pose Trajectory Diffusion for Object-Centric Manipulation"
conference: ICRA 2025
date: 2025-05
authors:
  - name: "Bowen Wen"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jie Xu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yashraj Narang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yuke Zhu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Stan Birchfield"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Cheng-Chun Hsu"
    affiliation: ""
    is_industry: false
  - name: "Joydeep Biswas"
    affiliation: ""
    is_industry: false
topics:
  - Computer Vision
  - Robotics_autonomous
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Vision"
  - "Robotics"
external_links:
  - name: "paper"
    url: "https://arxiv.org/abs/2411.00965"
  - name: "webpage"
    url: "https://nvlabs.github.io/object_centric_diffusion/"
abstract: "We introduce SPOT, an object-centric imitation learning framework. The key idea is to capture each task by an object-centric representation, specifically the SE(3) object pose trajectory relative to the target. This approach decouples embodiment actions from sensory inputs, facilitating learning fro"
url: "https://research.nvidia.com/publication/2025-05_spot-se3-pose-trajectory-diffusion-object-centric-manipulation"
status: new
---

# SPOT: SE(3) Pose Trajectory Diffusion for Object-Centric Manipulation

## 摘要

We introduce SPOT, an object-centric imitation learning framework. The key idea is to capture each task by an object-centric representation, specifically the SE(3) object pose trajectory relative to the target. This approach decouples embodiment actions from sensory inputs, facilitating learning from various demonstration types, including both action-based and action-less human hand demonstrations, as well as cross-embodiment generalization. Additionally, object pose trajectories inherently capture planning constraints from demonstrations without the need for manually-crafted rules. To guide the robot in executing the task, the object trajectory is used to condition a diffusion policy. We systematically evaluate our method on simulation and real-world tasks. In real-world evaluation, using only eight demonstrations shot on an iPhone, our approach completed all tasks while fully complying with task constraints.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
