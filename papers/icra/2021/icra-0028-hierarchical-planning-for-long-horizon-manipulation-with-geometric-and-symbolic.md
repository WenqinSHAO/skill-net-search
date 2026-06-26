---
id: "icra-0028"
title: "Hierarchical Planning for Long-Horizon Manipulation with Geometric and Symbolic Scene Graphs"
conference: "ICRA 2021"
date: "2021-05"
authors:
  - name: "Yifeng Zhu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jonathan Tremblay"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Stan Birchfield"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yuke Zhu"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Robotics"
external_links:
  - name: "arXiv paper"
    url: "https://arxiv.org/abs/2012.07277"
  - name: "project website"
    url: "https://zhuyifengzju.github.io/projects/hierarchical-scene-graph/"
abstract: "We present a visually grounded hierarchical planning algorithm for long-horizon manipulation tasks. Our algorithm offers a joint framework of neuro-symbolic task planning and low-level motion generation conditioned on the specified goal. At the core of our approach is a two-level scene graph represe"
url: "https://research.nvidia.com/publication/2021-05_hierarchical-planning-long-horizon-manipulation-geometric-and-symbolic-scene"
status: "new"
---

# Hierarchical Planning for Long-Horizon Manipulation with Geometric and Symbolic Scene Graphs

## 摘要

We present a visually grounded hierarchical planning algorithm for long-horizon manipulation tasks. Our algorithm offers a joint framework of neuro-symbolic task planning and low-level motion generation conditioned on the specified goal. At the core of our approach is a two-level scene graph representation, namely geometric scene graph and symbolic scene graph. This hierarchical representation serves as a structured, object-centric abstraction of manipulation scenes. Our model uses graph neural networks to process these scene graphs for predicting high-level task plans and low-level motions. We demonstrate that our method scales to long-horizon tasks and generalizes well to novel task goals. We validate our method in a kitchen storage task in both physical simulation and the real world. Our experiments show that our method achieved over 70% success rate and nearly 90% of subgoal completion rate on the real robot while being four orders of magnitude faster in computation time compared to standard search-based task-and-motion planner.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
