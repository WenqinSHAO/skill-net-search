---
id: "arxiv-2747"
title: "A bidirectional formulation for Walk on Spheres"
conference: "arXiv 2022"
date: "2022-07"
authors:
  - name: "Yang Qi"
    affiliation: "Dartmouth College"
    is_industry: false
  - name: "Dario Seyb"
    affiliation: "Dartmouth College"
    is_industry: false
  - name: "Benedikt Bitterli"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Wojciech Jarosz"
    affiliation: "Dartmouth College"
    is_industry: false
topics:
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Graphics"
abstract: "Numerically solving partial differential equations (PDEs) is central to many applications in computer graphics and scientific modeling. Conventional methods for solving PDEs often need to discretize the space first, making them less efficient for complex geometry. Unlike conventional methods, the wa"
url: "https://research.nvidia.com/publication/2022-07_bidirectional-formulation-walk-spheres"
status: "new"
---

# A bidirectional formulation for Walk on Spheres

## 摘要

Numerically solving partial differential equations (PDEs) is central to many applications in computer graphics and scientific modeling. Conventional methods for solving PDEs often need to discretize the space first, making them less efficient for complex geometry. Unlike conventional methods, the walk on spheres (WoS) algorithm recently introduced to graphics is a grid-free Monte Carlo method that can provide numerical solutions of Poisson equations without discretizing space. We draw analogies between WoS and classical rendering algorithms, and find that the WoS algorithm is conceptually equivalent to forward path tracing. Inspired by similar approaches in light transport, we propose a novel WoS reformulation that operates in the reverse direction, starting at source points and estimating the Green's function at “sensor” points. Implementations of this algorithm show improvement over classical WoS in solving Poisson equation with sparse sources. Our approach opens exciting avenues for future algorithms for PDE estimation which, analogous to light transport, connect WoS walks starting from sensors and sources and combine different strategies for robust solution algorithms in all cases.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
