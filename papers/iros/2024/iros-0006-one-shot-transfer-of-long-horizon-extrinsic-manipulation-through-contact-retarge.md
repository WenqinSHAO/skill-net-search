---
id: "iros-0006"
title: "One-Shot Transfer of Long-Horizon Extrinsic Manipulation Through Contact Retargeting"
conference: "IROS 2024"
date: "2024-04"
authors:
  - name: "Albert Wu"
    affiliation: ""
    is_industry: false
  - name: "Ruocheng Wang"
    affiliation: ""
    is_industry: false
  - name: "Sirui Chen"
    affiliation: ""
    is_industry: false
  - name: "Clemens Eppner"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "C Karen Liu"
    affiliation: ""
    is_industry: false
topics:
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Robotics"
external_links:
  - name: "Project Website"
    url: "https://stanford-tml.github.io/extrinsic-manipulation/"
  - name: "arXiv"
    url: "https://arxiv.org/abs/2404.07468"
abstract: "Extrinsic manipulation, the use of environment contacts to achieve manipulation objectives, enables strategies that are otherwise impossible with a parallel jaw gripper. However, orchestrating a long-horizon sequence of contact interactions between the robot, object, and environment is notoriously c"
url: "https://research.nvidia.com/publication/2024-04_one-shot-transfer-long-horizon-extrinsic-manipulation-through-contact"
status: "new"
---

# One-Shot Transfer of Long-Horizon Extrinsic Manipulation Through Contact Retargeting

## 摘要

Extrinsic manipulation, the use of environment contacts to achieve manipulation objectives, enables strategies that are otherwise impossible with a parallel jaw gripper. However, orchestrating a long-horizon sequence of contact interactions between the robot, object, and environment is notoriously challenging due to the scene diversity, large action space, and difficult contact dynamics. We observe that most extrinsic manipulation are combinations of short-horizon primitives, each of which depend strongly on initializing from a desirable contact configuration to succeed. Therefore, we propose to generalize one extrinsic manipulation trajectory to diverse objects and environments by retargeting contact requirements. We prepare a single library of robust short-horizon, goal-conditioned primitive policies, and design a framework to compose state constraints stemming from contacts specifications of each primitive. Given a test scene and a single demo prescribing the primitive sequence, our method enforces the state constraints on the test scene and find intermediate goal states using inverse kinematics. The goals are then tracked by the primitive policies. Using a 7+1 DoF robotic arm-gripper system, we achieved an overall success rate of 80.5% on hardware over 4 long-horizon extrinsic manipulation tasks, each with up to 4 primitives. Our experiments cover 10 objects and 6 environment configurations. We further show empirically that our method admits a wide range of demonstrations, and that contact retargeting is indeed the key to successfully combining primitives for long-horizon extrinsic manipulation.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
