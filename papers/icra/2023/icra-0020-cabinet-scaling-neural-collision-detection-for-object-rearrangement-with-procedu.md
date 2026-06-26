---
id: "icra-0020"
title: "CabiNet: Scaling Neural Collision Detection for Object Rearrangement with Procedural Scene Generation"
conference: "ICRA 2023"
date: "2023-05"
authors:
  - name: "Adithya Murali"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Arsalan Mousavian"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Clemens Eppner"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Adam Fishman"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Dieter Fox"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Robotics"
external_links:
  - name: "Project Website"
    url: "https://cabinet-object-rearrangement.github.io/"
abstract: "We address the important problem of generalizing robotic rearrangement to clutter without any explicit object models. We first generate over 650K cluttered scenes— orders of magnitude more than prior work—in diverse everyday environments, such as cabinets and shelves. We render synthetic partial poi"
url: "https://research.nvidia.com/publication/2023-05_cabinet-scaling-neural-collision-detection-object-rearrangement-procedural"
status: "new"
---

# CabiNet: Scaling Neural Collision Detection for Object Rearrangement with Procedural Scene Generation

## 摘要

We address the important problem of generalizing robotic rearrangement to clutter without any explicit object models. We first generate over 650K cluttered scenes— orders of magnitude more than prior work—in diverse everyday environments, such as cabinets and shelves. We render synthetic partial point clouds from this data and use it to train our&nbsp;CabiNet&nbsp;model architecture.&nbsp;CabiNet&nbsp;is a collision model that accepts object and scene point clouds, captured from a single-view depth observation, and predicts collisions for&nbsp;SE(3)&nbsp;object poses in the scene. Our representation has a fast inference speed of 7micro-seconds/query with nearly 20% higher performance than baseline approaches in challenging environments. We use this collision model in conjunction with a Model Predictive Path Integral (MPPI) planner to generate collision-free trajectories for picking and placing in clutter.&nbsp;CabiNet&nbsp;also predicts waypoints, computed from the scene’s signed distance field (SDF), that allows the robot to navigate tight spaces during rearrangement. This improves rearrangement performance by nearly 35% compared to baselines. We systematically evaluate our approach, procedurally generate simulated experiments, and demonstrate that our approach directly transfers to the real world, despite training exclusively in simulation. Robot experiments in completely unknown scenes and objects are shown in the supplementary video.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
