---
id: siggraph-0054
title: "Inverse Global Illumination using a Neural Radiometric Prior"
conference: SIGGRAPH 2023
date: 2023-05
authors:
  - name: "Jan Novák"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Fabrice Rousselle"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Saeed Hadadan"
    affiliation: ""
    is_industry: false
  - name: "Geng Lin"
    affiliation: ""
    is_industry: false
  - name: "Matthias Zwicker"
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
    url: "https://research.nvidia.com/labs/rtr/inverse_global_illumination/"
abstract: "Inverse rendering methods that account for global illumination are becoming more popular, but current methods require evaluating and automatically differentiating millions of path integrals by tracing multiple light bounces, which remains expensive and prone to noise. Instead, this paper proposes a "
url: "https://research.nvidia.com/publication/2023-05_inverse-global-illumination-using-neural-radiometric-prior"
status: new
---

# Inverse Global Illumination using a Neural Radiometric Prior

## 摘要

Inverse rendering methods that account for global illumination are becoming more popular, but current methods require evaluating and automatically differentiating millions of path integrals by tracing multiple light bounces, which remains expensive and prone to noise. Instead, this paper proposes a radiometric prior as a simple alternative to building complete path integrals in a traditional differentiable path tracer, while still correctly accounting for global illumination. Inspired by the Neural Radiosity technique, we use a neural network as a radiance function, and we introduce a prior consisting of the norm of the residual of the rendering equation in the inverse rendering loss. We train our radiance network and optimize scene parameters simultaneously using a loss consisting of both a photometric term between renderings and the mutli-view input images, and our radiometric prior (the residual term). This residual term enforces a physical constraint on the optimization that ensures that the radiance field accounts for global illumination. We compare our method to a vanilla differentiable path tracer, and more advanced techniques such as Path Replay Backpropagation. Despite the simplicity of our approach, we can recover scene parameters with comparable and in some cases better quality, at considerably lower computation times.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
