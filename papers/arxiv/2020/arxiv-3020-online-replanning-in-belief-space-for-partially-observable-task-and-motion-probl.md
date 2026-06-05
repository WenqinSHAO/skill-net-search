---
id: arxiv-3020
title: "Online replanning in belief space for partially observable task and motion problems"
conference: arXiv 2020
date: 2020-05
authors:
  - name: "Caelan Garrett"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Chris Paxton"
    affiliation: ""
    is_industry: false
  - name: "Tomas Lozano-Perez"
    affiliation: ""
    is_industry: false
  - name: "Leslie Kaebling"
    affiliation: ""
    is_industry: false
  - name: "Dieter Fox"
    affiliation: ""
    is_industry: false
topics:
  - Robotics_autonomous
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Robotics"
abstract: "To solve multi-step manipulation tasks in the real world, an autonomous robot must take actions to observe its environment and react to unexpected observations. This may require opening a drawer to observe its contents or moving an object out of the way to examine the space behind it. Upon receiving"
url: "https://research.nvidia.com/publication/2020-05_online-replanning-belief-space-partially-observable-task-and-motion-problems"
status: new
---

# Online replanning in belief space for partially observable task and motion problems

## 摘要

To solve multi-step manipulation tasks in the real world, an autonomous robot must take actions to observe its environment and react to unexpected observations. This may require opening a drawer to observe its contents or moving an object out of the way to examine the space behind it. Upon receiving a new observation, the robot must update its belief about the world and compute a new plan of action. In this work, we present an online planning and execution system for robots faced with these challenges. We perform deterministic cost-sensitive planning in the space of hybrid belief states to select likely-to-succeed observation actions and continuous control actions. After execution and observation, we replan using our new state estimate. We initially enforce that planner reuses the structure of the unexecuted tail of the last plan. This both improves planning efficiency and ensures that the overall policy does not undo its progress towards achieving the goal. Our approach is able to efficiently solve partially observable problems both in simulation and in a real-world kitchen.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
