---
id: "arxiv-2600"
title: "Signatures Meet Dynamic Programming: Generalizing Bellman Equations for Trajectory Following"
conference: "arXiv 2024"
date: "2024-07"
authors:
  - name: "Motoya Ohnishi"
    affiliation: "University of Washington"
    is_industry: false
  - name: "Iretiayo Akinola"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jie Xu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ajay Mandlekar"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Fabio Ramos"
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
  - name: "Paper"
    url: "https://proceedings.mlr.press/v242/ohnishi24a.html"
abstract: "Path signatures have been proposed as a powerful representation of paths that efficiently captures the path’s analytic and geometric characteristics, having useful algebraic properties including fast concatenation of paths through tensor products. Signatures have recently been widely adopted in mach"
url: "https://research.nvidia.com/publication/2024-07_signatures-meet-dynamic-programming-generalizing-bellman-equations-trajectory"
status: "new"
---

# Signatures Meet Dynamic Programming: Generalizing Bellman Equations for Trajectory Following

## 摘要

Path signatures have been proposed as a powerful representation of paths that efficiently captures the path’s analytic and geometric characteristics, having useful algebraic properties including fast concatenation of paths through tensor products. Signatures have recently been widely adopted in machine learning problems for time series analysis. In this work we establish connections between value functions typically used in optimal control and intriguing properties of path signatures. These connections motivate our novel control framework with signature transforms that efficiently generalizes the Bellman equation to the space of trajectories. We analyze the properties and advantages of the framework, termed signature control. In particular, we demonstrate that (i) it can naturally deal with varying/adaptive time steps; (ii) it propagates higher-level information more efficiently than value function updates; (iii) it is robust to dynamical system misspecification over long rollouts. As a specific case of our framework, we devise a model predictive control method for path tracking. This method generalizes integral control, being suitable for problems with unknown disturbances. The proposed algorithms are tested in simulation, with differentiable physics models including typical control and robotics tasks such as point-mass, curve following for an ant model, and a robotic manipulator.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
