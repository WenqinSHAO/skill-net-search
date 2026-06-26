---
id: "arxiv-2668"
title: "CuRobo: Parallelized Collision-Free Robot Motion Generation"
conference: "arXiv 2023"
date: "2023-05"
authors:
  - name: "Balakumar Sundaralingam"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Siva Hari"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Adam Fishman"
    affiliation: "University of Washington"
    is_industry: false
  - name: "Caelan Garrett"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Karl Van Wyk"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Valts Blukis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Alexander Millane"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Helen Oleynikova"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ankur Handa"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Fabio Ramos"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Nathan Ratliff"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Dieter Fox"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - GPU_architecture
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Architecture"
  - "Robotics"
external_links:
  - name: "Published manuscript (IEEE Digital Library)"
    url: "https://ieeexplore.ieee.org/document/10160765"
abstract: "This paper explores the problem of collision-free motion generation for manipulators by formulating it as a global motion optimization problem. We develop a parallel optimization technique to solve this problem and demonstrate its effectiveness on massively parallel GPUs. We show that combining simp"
url: "https://research.nvidia.com/publication/2023-05_curobo-parallelized-collision-free-robot-motion-generation"
status: "new"
---

# CuRobo: Parallelized Collision-Free Robot Motion Generation

## 摘要

This paper explores the problem of collision-free motion generation for manipulators by formulating it as a global motion optimization problem. We develop a parallel optimization technique to solve this problem and demonstrate its effectiveness on massively parallel GPUs. We show that combining simple optimization techniques with many parallel seeds leads to solving difficult motion generation problems within 53ms on average, 62x faster than SOTA trajectory optimization methods. We achieve SOTA performance by combining L-BFGS step direction estimation with a novel parallel noisy line search scheme and a particle-based optimization solver. To further aid trajectory optimization, we develop a parallel geometric planner that is at least 28x faster than SOTA RRTConnect implementations. We also introduce a collision-free IK solver that can solve over 9000 queries/s. We are releasing our GPU-accelerated library CuRobo that contains core components for robot motion generation.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
