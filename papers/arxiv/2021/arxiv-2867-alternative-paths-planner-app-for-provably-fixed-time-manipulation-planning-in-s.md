---
id: "arxiv-2867"
title: "Alternative Paths Planner (APP) for Provably Fixed-time Manipulation Planning in Semi-structured Environments"
conference: "arXiv 2021"
date: "2021-05"
authors:
  - name: "Fahad Islam"
    affiliation: "Carnegie Mellon University"
    is_industry: false
  - name: "Chris Paxton"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Clemens Eppner"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Bryan Peele"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Maxim Likhachev"
    affiliation: "Carnegie Mellon University"
    is_industry: false
  - name: "Dieter Fox"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - CUDA_ecosystem
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Algorithms and Numerical Methods"
  - "Robotics"
external_links:
  - name: "ArXiv version"
    url: "https://arxiv.org/abs/2012.14970"
abstract: "In many applications, including logistics and manufacturing, robot manipulators operate in semi-structured environments alongside humans or other robots. These environments are largely static, but they may contain some movable obstacles that the robot must avoid. Manipulation tasks in these applicat"
url: "https://research.nvidia.com/publication/2021-05_alternative-paths-planner-app-provably-fixed-time-manipulation-planning-semi"
status: "new"
---

# Alternative Paths Planner (APP) for Provably Fixed-time Manipulation Planning in Semi-structured Environments

## 摘要

In many applications, including logistics and manufacturing, robot manipulators operate in semi-structured environments alongside humans or other robots. These environments are largely static, but they may contain some movable obstacles that the robot must avoid. Manipulation tasks in these applications are often highly repetitive, but require fast and reliable motion planning capabilities, often under strict time constraints. Existing preprocessing-based approaches are beneficial when the environments are highly-structured, but their performance degrades in the presence of movable obstacles, since these are not modelled a priori. We propose a novel preprocessing-based method called Alternative Paths Planner (APP) that provides provably fixed-time planning guarantees in semi-structured environments. APP plans a set of alternative paths offline such that, for any configuration of the movable obstacles, at least one of the paths from this set is collision-free. During online execution, a collision-free path can be looked up efficiently within a few microseconds. We evaluate APP on a 7 DoF robot arm in semi-structured domains of varying complexity and demonstrate that APP is several orders of magnitude faster than state-of-the-art motion planners for each domain. We further validate this approach with real-time experiments on a robotic manipulator.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
