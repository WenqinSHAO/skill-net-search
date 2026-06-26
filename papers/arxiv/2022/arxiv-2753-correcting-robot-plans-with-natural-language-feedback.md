---
id: "arxiv-2753"
title: "Correcting Robot Plans with Natural Language Feedback"
conference: "arXiv 2022"
date: "2022-06"
authors:
  - name: "Pratyusha Sharma"
    affiliation: "MIT"
    is_industry: false
  - name: "Balakumar Sundaralingam"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Valts Blukis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Chris Paxton"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Tucker Hermans"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Antonio Torralba"
    affiliation: "MIT"
    is_industry: false
  - name: "Jacob Andreas"
    affiliation: "MIT"
    is_industry: false
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
  - name: "Website"
    url: "https://sites.google.com/view/language-costs"
abstract: "When humans design cost or goal specifications for robots, they often produce specifications that are ambiguous, underspecified, or beyond planners' ability to solve. In these cases, corrections provide a valuable tool for human-in-the-loop robot control. Corrections might take the form of new goal "
url: "https://research.nvidia.com/publication/2022-06_correcting-robot-plans-natural-language-feedback"
status: "new"
---

# Correcting Robot Plans with Natural Language Feedback

## 摘要

When humans design cost or goal specifications for robots, they often produce specifications that are ambiguous, underspecified, or beyond planners' ability to solve. In these cases, corrections provide a valuable tool for human-in-the-loop robot control. Corrections might take the form of new goal specifications, new constraints (e.g. to avoid specific objects), or hints for planning algorithms (e.g. to visit specific waypoints). Existing correction methods (e.g. using a joystick or direct manipulation of an end effector) require full teleoperation or real-time interaction. In this paper, we explore natural language as an expressive and flexible tool for robot correction. We describe how to map from natural language sentences to transformations of cost functions. We show that these transformations enable users to correct goals, update robot motions to accommodate additional user preferences, and recover from planning errors. These corrections can be leveraged to get 81% and 93% success rates on tasks where the original planner failed, with either one or two language corrections. Our method makes it possible to compose multiple constraints and generalizes to unseen scenes, objects, and sentences in simulated environments and real-world environments.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
