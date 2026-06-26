---
id: "siggraph-0065"
title: "Fast Volume Rendering with Spatiotemporal Reservoir Resampling"
conference: "SIGGRAPH 2021"
date: "2021-11"
authors:
  - name: "Daqi Lin"
    affiliation: "University of Utah"
    is_industry: false
  - name: "Chris Wyman"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Cem Yuksel"
    affiliation: "University of Utah"
    is_industry: false
topics:
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Graphics"
  - "Real-Time Rendering"
abstract: "Volume rendering under complex, dynamic lighting is challenging, especially if targeting real-time. To address this challenge, we extend a recent direct illumination sampling technique, spatiotemporal reservoir resampling, to multi-dimensional path space for volumetric media. By fully evaluating jus"
url: "https://research.nvidia.com/publication/2021-11_fast-volume-rendering-spatiotemporal-reservoir-resampling"
status: "new"
---

# Fast Volume Rendering with Spatiotemporal Reservoir Resampling

## 摘要

Volume rendering under complex, dynamic lighting is challenging, especially if targeting real-time. To address this challenge, we extend a recent direct illumination sampling technique, spatiotemporal reservoir resampling, to multi-dimensional path space for volumetric media. By fully evaluating just a single path sample per pixel, our volumetric path tracer shows unprecedented convergence. To achieve this, we properly estimate the chosen sample’s probability via approximate perfect importance sampling with spatiotemporal resampling. A key observation is recognizing that applying cheaper, biased techniques to approximate scattering along candidate paths (during resampling) does not add bias when shading. This allows us to combine transmittance evaluation techniques: cheap approximations where evaluations must occur many times for reuse, and unbiased methods for final, per-pixel evaluation. With this reformulation, we achieve low-noise, interactive volumetric path tracing with arbitrary dynamic lighting, including volumetric emission, and maintain interactive performance even on high-resolution volumes. When paired with denoising, our low-noise sampling helps preserve smaller-scale volumetric details.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
