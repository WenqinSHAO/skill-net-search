---
id: "neurips-0039"
title: "Shape, Light, and Material Decomposition from Images using Monte Carlo Rendering and Denoising"
conference: "NeurIPS 2022"
date: "2022-10"
authors:
  - name: "Jon Hasselgren"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Nikolai Hofmann"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jacob Munkberg"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - Computer Vision
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Graphics"
  - "Computer Vision"
external_links:
  - name: "Project page"
    url: "https://nvlabs.github.io/nvdiffrecmc/"
  - name: "Source code"
    url: "https://github.com/NVlabs/nvdiffrecmc"
  - name: "Arxiv preprint"
    url: "https://arxiv.org/abs/2206.03380"
abstract: "Abstract Recent advances in differentiable rendering have enabled high-quality reconstruction of 3D scenes from multi-view images. Most methods rely on simple rendering algorithms: pre-filtered direct lighting or learned representations of irradiance. We show that a more realistic shading model, inc"
url: "https://research.nvidia.com/publication/2022-10_shape-light-and-material-decomposition-images-using-monte-carlo-rendering-and"
status: "new"
---

# Shape, Light, and Material Decomposition from Images using Monte Carlo Rendering and Denoising

## 摘要

Abstract Recent advances in differentiable rendering have enabled high-quality reconstruction of 3D scenes from multi-view images. Most methods rely on simple rendering algorithms: pre-filtered direct lighting or learned representations of irradiance. We show that a more realistic shading model, incorporating ray tracing and Monte Carlo integration, substantially improves decomposition into shape, materials and lighting. Unfortunately, Monte Carlo integration provides estimates with significant noise, even at large sample counts, which makes gradient-based inverse rendering very challenging. To address this, we incorporate multiple importance sampling and denoising in a novel inverse rendering pipeline. This substantially improves convergence and enables gradient-based optimization at low sample counts. We present an efficient method to jointly reconstruct geometry (explicit triangle meshes), materials, and lighting, which substantially improves material and light separation compared to previous work. We argue that denoising can become an integral part of high quality inverse rendering pipelines.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
