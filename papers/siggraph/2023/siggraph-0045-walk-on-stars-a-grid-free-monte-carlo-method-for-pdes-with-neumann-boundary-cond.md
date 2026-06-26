---
id: "siggraph-0045"
title: "Walk on Stars: A Grid-Free Monte Carlo Method for PDEs with Neumann Boundary Conditions"
conference: "SIGGRAPH 2023"
date: "2023-08"
authors:
  - name: "Rohan Sawhney"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Bailey Miller"
    affiliation: "CMU"
    is_industry: false
  - name: "Ioannis Gkioulekas"
    affiliation: "CMU"
    is_industry: false
  - name: "Keenan Crane"
    affiliation: "CMU"
    is_industry: false
topics:
  - AI & Machine Learning
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
abstract: "Grid-free Monte Carlo methods based on the walk on spheres (WoS) algorithm solve fundamental partial differential equations (PDEs) like the Poisson equation without discretizing the problem domain, nor approximating functions a finite basis. Such methods hence avoid aliasing in the solution, and eva"
url: "https://research.nvidia.com/publication/2023-08_walk-stars-grid-free-monte-carlo-method-pdes-neumann-boundary-conditions"
status: "new"
---

# Walk on Stars: A Grid-Free Monte Carlo Method for PDEs with Neumann Boundary Conditions

## 摘要

Grid-free Monte Carlo methods based on the walk on spheres (WoS) algorithm solve fundamental partial differential equations (PDEs) like the Poisson equation without discretizing the problem domain, nor approximating functions a finite basis. Such methods hence avoid aliasing in the solution, and evade the many challenges of mesh generation. Yet for problems with complex geometry, practical grid-free methods have been largely limited to basic Dirichlet boundary conditions. This paper introduces the walk on stars (WoSt) method, which solves linear elliptic PDEs with arbitrary mixed Neumann and Dirichlet boundary conditions. The key insight is that one can efficiently simulate reflecting Brownian motion (which models Neumann conditions) by replacing the balls used by WoS with star-shaped domains; we identify such domains by locating the closest visible point on the geometric silhouette. Overall, WoSt retains many attractive features of other gridfree Monte Carlo methods, such as progressive evaluation, trivial parallel implementation, and logarithmic scaling relative to geometric complexity.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
