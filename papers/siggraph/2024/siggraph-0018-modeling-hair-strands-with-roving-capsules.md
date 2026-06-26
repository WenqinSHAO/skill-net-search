---
id: "siggraph-0018"
title: "Modeling Hair Strands with Roving Capsules"
conference: "SIGGRAPH 2024"
date: "2024-07"
authors:
  - name: "Alexander Reshetov"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "David Hart"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Graphics"
abstract: "Hair strands can be modeled by sweeping spheres with varying radii along Bézier curves. We ray-trace such shapes by finding intersections of a given ray with a set of capsules dynamically defined at runtime. A substantial performance boost is achieved by systematically eliminating parts of the shape"
url: "https://research.nvidia.com/publication/2024-07_modeling-hair-strands-roving-capsules"
status: "new"
---

# Modeling Hair Strands with Roving Capsules

## 摘要

Hair strands can be modeled by sweeping spheres with varying radii along Bézier curves. We ray-trace such shapes by finding intersections of a given ray with a set of capsules dynamically defined at runtime. A substantial performance boost is achieved by systematically eliminating parts of the shape that are guaranteed not to intersect with the given ray. The new intersector is more than twice faster than the previously leading phantom algorithm. This improvement results in a 30% overall performance increase, which includes traversal, shading, and the rendering system overhead. In addition, we derive a parametric form of the swept sphere shapes. This provides a deeper understanding of the properties of such objects compared to the offset surfaces obtained by sweeping circles orthogonal to a given curve.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
