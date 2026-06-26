---
id: "corl-0019"
title: "Task-Relevant Failure Detection for Trajectory Predictors in Autonomous Vehicles"
conference: "CoRL 2022"
date: "2022-12"
authors:
  - name: "Alec Farid"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Sushant Veer"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Boris Ivanovic"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Karen Leung"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Marco Pavone"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Computer Vision
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Autonomous Vehicles"
  - "Computer Vision"
  - "Resilience and Safety"
external_links:
  - name: "Paper"
    url: "https://openreview.net/forum?id=oPRhm0Aben_"
abstract: "In modern autonomy stacks, prediction modules are paramount to planning motions in the presence of other mobile agents. However, failures in prediction modules can mislead the downstream planner into making unsafe decisions. Indeed, the high uncertainty inherent to the task of trajectory forecasting"
url: "https://research.nvidia.com/publication/2022-12_task-relevant-failure-detection-trajectory-predictors-autonomous-vehicles"
status: "new"
---

# Task-Relevant Failure Detection for Trajectory Predictors in Autonomous Vehicles

## 摘要

In modern autonomy stacks, prediction modules are paramount to planning motions in the presence of other mobile agents. However, failures in prediction modules can mislead the downstream planner into making unsafe decisions. Indeed, the high uncertainty inherent to the task of trajectory forecasting ensures that such mispredictions occur frequently. Motivated by the need to improve safety of autonomous vehicles without compromising on their performance, we develop a probabilistic run-time monitor that detects when a harmful prediction failure occurs, i.e., a task-relevant failure detector. We achieve this by propagating trajectory prediction errors to the planning cost to reason about their impact on the AV. Furthermore, our detector comes equipped with performance measures on the false-positive and the false-negative rate and allows for data-free calibration. In our experiments we compared our detector with various others and found that our detector has the highest area under the receiver operator characteristic curve.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
