---
id: "arxiv-2780"
title: "Model Predictive Control for Fluid Human-to-Robot Handovers"
conference: "arXiv 2022"
date: "2022-04"
authors:
  - name: "Wei Yang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Balakumar Sundaralingam"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Chris Paxton"
    affiliation: "Meta"
    is_industry: true
  - name: "Iretiayo Akinola"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yu-Wei Chao"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Maya Cakmak"
    affiliation: "University of Washington"
    is_industry: false
  - name: "Dieter Fox"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - Applied_perception
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Human Computer Interaction"
  - "Robotics"
external_links:
  - name: "arXiv"
    url: "https://arxiv.org/abs/2204.00134"
  - name: "Project"
    url: "https://sites.google.com/nvidia.com/mpc-for-handover"
abstract: "Human-robot handover is a fundamental yet challenging task in human-robot interaction and collaboration. Recently, remarkable progressions have been made in human-to-robot handovers of unknown objects by using learning-based grasp generators. However, how to responsively generate smooth motions to t"
url: "https://research.nvidia.com/publication/2022-04_model-predictive-control-fluid-human-robot-handovers"
status: "new"
---

# Model Predictive Control for Fluid Human-to-Robot Handovers

## 摘要

Human-robot handover is a fundamental yet challenging task in human-robot interaction and collaboration. Recently, remarkable progressions have been made in human-to-robot handovers of unknown objects by using learning-based grasp generators. However, how to responsively generate smooth motions to take an object from a human is still an open question. Specifically, planning motions that take human comfort into account is not a part of the human-robot handover process in most prior works. In this paper, we propose to generate smooth motions via an efficient model-predictive control (MPC) framework that integrates perception and complex domain-specific constraints into the optimization problem. We introduce a learning-based grasp reachability model to select candidate grasps which maximize the robot’s manipulability, giving it more freedom to satisfy these constraints. Finally, we integrate a neural net force/torque classifier that detects contact events from noisy data. We conducted human-to-robot handover experiments on a diverse set of objects with several users (N=4) and performed a systematic evaluation of each module. The study shows that the users preferred our MPC approach over the baseline system by a large margin.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
