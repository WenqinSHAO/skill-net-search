---
id: "siggraph-0023"
title: "Stabler Neo-Hookean Simulation: Absolute Eigenvalue Filtering for Projected Newton"
conference: "SIGGRAPH 2024"
date: "2024-06"
authors:
  - name: "Honglin Chen"
    affiliation: "Columbia University"
    is_industry: false
  - name: "Hsueh-Ti Derek Liu"
    affiliation: "Roblox Research, University of British Columbia"
    is_industry: false
  - name: "David I.W. Levin"
    affiliation: "NVIDIA, University of Toronto"
    is_industry: true
  - name: "Changxi Zheng"
    affiliation: "Columbia University"
    is_industry: false
  - name: "Alec Jacobson"
    affiliation: "Adobe Research, University of Toronto"
    is_industry: true
topics:
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Graphics"
abstract: "Volume-preserving hyperelastic materials are widely used to model near-incompressible materials such as rubber and soft tissues. However, the numerical simulation of volume-preserving hyperelastic materials is notoriously challenging within this regime due to the non-convexity of the energy function"
url: "https://research.nvidia.com/publication/2024-06_stabler-neo-hookean-simulation-absolute-eigenvalue-filtering-projected-newton"
status: "new"
---

# Stabler Neo-Hookean Simulation: Absolute Eigenvalue Filtering for Projected Newton

## 摘要

Volume-preserving hyperelastic materials are widely used to model near-incompressible materials such as rubber and soft tissues. However, the numerical simulation of volume-preserving hyperelastic materials is notoriously challenging within this regime due to the non-convexity of the energy function. In this work, we identify the pitfalls of the popular eigenvalue clamping strategy for projecting Hessian matrices to positive semi-definiteness during Newton's method. We introduce a novel eigenvalue filtering strategy for projected Newton's method to stabilize the optimization of Neo-Hookean energy and other volume-preserving variants under high Poisson's ratio (near 0.5) and large initial volume change. Our method only requires a single line of code change in the existing projected Newton framework, while achieving significant improvement in both stability and convergence speed. We demonstrate the effectiveness and efficiency of our eigenvalue projection scheme on a variety of challenging examples and over different deformations on a large dataset.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
