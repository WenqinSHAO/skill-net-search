---
id: arxiv-2607
title: "Walkin’ Robin: Walk on Stars with Robin Boundary Conditions"
conference: arXiv 2024
date: 2024-07
authors:
  - name: "Bailey Miller"
    affiliation: ""
    is_industry: false
  - name: "Rohan Sawhney"
    affiliation: ""
    is_industry: false
  - name: "Keenan Crane"
    affiliation: ""
    is_industry: false
  - name: "Ioannis Gkioulekas"
    affiliation: ""
    is_industry: false
topics:
  - Graphics_rendering
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Graphics"
external_links:
  - name: "Project Page"
    url: "https://research.nvidia.com/labs/prl/publication/miller2024wost/"
abstract: "Numerous scientific and engineering applications require solving boundary value problems (BVPs) like the Laplace and Poisson equations on geometrically intricate domains. We describe a unified Monte Carlo approach to solving elliptic BVPs with Dirichlet, Neumann and Robin boundary conditions using t"
url: "https://research.nvidia.com/publication/2024-07_walkin-robin-walk-stars-robin-boundary-conditions"
status: new
---

# Walkin’ Robin: Walk on Stars with Robin Boundary Conditions

## 摘要

Numerous scientific and engineering applications require solving boundary value problems (BVPs) like the Laplace and Poisson equations on geometrically intricate domains. We describe a unified Monte Carlo approach to solving elliptic BVPs with Dirichlet, Neumann and Robin boundary conditions using the walk on stars algorithm, which unlike conventional numerical methods, does not require any cumbersome finite element mesh generation or global solves. Similar to Monte Carlo rendering, we simulate independent random walks in domains with partially absorbing and reflecting boundaries using a mix of ray intersection and distance queries---our key contribution is the development of a pointwise estimator with bounded walk throughput, which can have orders of magnitude less error in its solution estimate than previous grid-free techniques for BVPs like the walk on boundary method. We also develop bidirectional and boundary value caching strategies to further reduce the variance of our estimator. Our approach is trivial to parallelize, scales favorably with increasing geometric detail, and allows for progressive and view-dependent evaluation.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
