---
id: arxiv-2664
title: "Refining Obstacle Perception Safety Zones via Maneuver-Based Decomposition"
conference: arXiv 2023
date: 2023-06
authors:
  - name: "Yuxiao Chen"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ed Schmerling"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Karen Leung"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Marco Pavone"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Sever Topan"
    affiliation: ""
    is_industry: false
  - name: "Jonas Nilsson"
    affiliation: ""
    is_industry: false
  - name: "Michael Cox"
    affiliation: ""
    is_industry: false
topics:
  - Robotics_autonomous
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Autonomous Vehicles"
  - "Resilience and Safety"
external_links:
  - name: "Paper"
    url: "https://arxiv.org/abs/2308.06337"
abstract: "A critical task for developing safe autonomous driving stacks is to determine whether an obstacle is safety-critical, i.e., poses an imminent threat to the autonomous vehicle. Our previous work showed that Hamilton Jacobi reachability theory can be applied to compute interaction-dynamics-aware perce"
url: "https://research.nvidia.com/publication/2023-06_refining-obstacle-perception-safety-zones-maneuver-based-decomposition"
status: new
---

# Refining Obstacle Perception Safety Zones via Maneuver-Based Decomposition

## 摘要

A critical task for developing safe autonomous driving stacks is to determine whether an obstacle is safety-critical, i.e., poses an imminent threat to the autonomous vehicle. Our previous work showed that Hamilton Jacobi reachability theory can be applied to compute interaction-dynamics-aware perception safety zones that better inform an ego vehicle’s perception module which obstacles are considered safety-critical. For completeness, these zones are typically larger than absolutely necessary, forcing the perception module to pay attention to a larger collection of objects for the sake of conservatism. As an improvement, we propose a maneuver-based decomposition of our safety zones that leverages information about the ego maneuver to reduce the zone volume. In particular, we propose a “temporal convolution” operation that produces safety zones for specific ego maneuvers, thus limiting the ego’s behavior to reduce the size of the safety zones. We show with numerical experiments that maneuver-based zones are significantly smaller (up to 76% size reduction) than the baseline while maintaining completeness.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
