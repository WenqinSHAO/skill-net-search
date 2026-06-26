---
id: "arxiv-2748"
title: "A Position-Free Path Integral for Homogeneous Slabs and Multiple Scattering on Smith Microfacets"
conference: "arXiv 2022"
date: "2022-07"
authors:
  - name: "Benedikt Bitterli"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Eugene d'Eon"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Eugene d&#039;Eon"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Graphics"
abstract: "We consider the problem of multiple scattering on Smith microfacets. This problem is equivalent to computing volumetric light transport in a homogeneous slab. Although the symmetry of the slab allows for significant simplification, fully analytic solutions are scarce and not general enough for most "
url: "https://research.nvidia.com/publication/2022-07_position-free-path-integral-homogeneous-slabs-and-multiple-scattering-smith"
status: "new"
---

# A Position-Free Path Integral for Homogeneous Slabs and Multiple Scattering on Smith Microfacets

## 摘要

We consider the problem of multiple scattering on Smith microfacets. This problem is equivalent to computing volumetric light transport in a homogeneous slab. Although the symmetry of the slab allows for significant simplification, fully analytic solutions are scarce and not general enough for most applications. Standard Monte Carlo simulation, although general, is expensive and leads to variance that must be dealt with. We present the first unbiased, truly position-free path integral for evaluating the BSDF of a homogeneous slab. We collapse the spatially-1D path integral of previous works to a position-free form using an analytical preintegration of collision distances. Evaluation of the resulting path integral, which now contains only directions, reduces to simple recursive manipulation of exponential distributions. Applying Monte Carlo to solve the reduced integration problem leads to lower variance. Our new algorithm allows us to render multiple scattering on Smith microfacets with less variance than prior work, and, in the case of conductors, to do so without any bias. Additionally, our algorithm can also be used to accelerate the rendering of BSDFs containing volumetrically scattering layers, at reduced variance compared to standard Monte Carlo integration.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
