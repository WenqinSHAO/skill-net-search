---
id: arxiv-2987
title: "Practical Product Sampling by Fitting and Composing Warps"
conference: arXiv 2020
date: 2020-07
authors:
  - name: "Matt Pharr"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Thomas Müller"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ward Lopes"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "David Hart"
    affiliation: ""
    is_industry: false
  - name: "Morgan McGuire"
    affiliation: ""
    is_industry: false
  - name: "Peter Shirley"
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
  - "Real-Time Rendering"
external_links:
  - name: "Shadertoy"
    url: "https://www.shadertoy.com/view/wljyDz"
  - name: "Presentation Video"
    url: "https://www.youtube.com/embed/LlpC6lTSqV8"
abstract: "We introduce a Monte Carlo importance sampling method for integrands composed of products and show its application to rendering where direct sampling of the product is often difficult. Our method is based on warp functions that operate on the primary samples in [0,1)^n, where each warp approximates "
url: "https://research.nvidia.com/publication/2020-07_practical-product-sampling-fitting-and-composing-warps"
status: new
---

# Practical Product Sampling by Fitting and Composing Warps

## 摘要

We introduce a Monte Carlo importance sampling method for integrands composed of products and show its application to rendering where direct sampling of the product is often difficult. Our method is based on warp functions that operate on the primary samples in [0,1)^n, where each warp approximates sampling a single factor of the product distribution. Our key insight is that individual factors are often well-behaved and inexpensive to fit and sample in primary sample space, which leads to a practical, efficient sampling algorithm. Our sampling approach is unbiased, easy to implement, and compatible with multiple importance sampling. We show the results of applying our warps to projected solid angle sampling of spherical triangles, to sampling bilinear patch light sources, and to sampling glossy BSDFs and area light sources, with efficiency improvements of over 1.6× on real-world scenes.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
