---
id: iros-0011
title: "Joint Space Control via Deep Reinforcement Learning"
conference: IROS 2021
date: 2021-09
authors:
  - name: "Balakumar Sundaralingam"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jonathan Tremblay"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Stan Birchfield"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Visak Kumar"
    affiliation: ""
    is_industry: false
  - name: "David Hoeller"
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
external_links:
  - name: "arXiv paper"
    url: "https://arxiv.org/abs/2011.06332"
  - name: "video"
    url: "https://www.youtube.com/watch?v=ICfve-GTTp8"
abstract: "The dominant way to control a robot manipulator uses hand-crafted differential equations leveraging some form of inverse kinematics / dynamics. We propose a simple, versatile joint-level controller that dispenses with differential equations entirely. A deep neural network, trained via model-free rei"
url: "https://research.nvidia.com/publication/2021-09_joint-space-control-deep-reinforcement-learning"
status: new
---

# Joint Space Control via Deep Reinforcement Learning

## 摘要

The dominant way to control a robot manipulator uses hand-crafted differential equations leveraging some form of inverse kinematics / dynamics. We propose a simple, versatile joint-level controller that dispenses with differential equations entirely. A deep neural network, trained via model-free reinforcement learning, is used to map from task space to joint space. Experiments show the method capable of achieving similar error to traditional methods, while greatly simplifying the process by automatically handling redundancy, joint limits, and acceleration / deceleration profiles. The basic technique is extended to avoid obstacles by augmenting the input to the network with information about the nearest obstacles. Results are shown both in simulation and on a real robot via sim-to-real transfer of the learned policy. We show that it is possible to achieve sub-centimeter accuracy, both in simulation and the real world, with a moderate amount of training.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
