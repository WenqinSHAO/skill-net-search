---
id: "arxiv-2804"
title: "Scalar Spatiotemporal Blue Noise Masks"
conference: "arXiv 2021"
date: "2021-12"
authors:
  - name: "Alan Wolfe"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Nathan Morrical"
    affiliation: "NVIDIA and University of Utah"
    is_industry: true
  - name: "Tomas Akenine-Möller"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ravi Ramamoorthi"
    affiliation: "NVIDIA and UC San Diego"
    is_industry: true
topics:
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Graphics"
  - "Real-Time Rendering"
external_links:
  - name: "Blog part 1"
    url: "https://developer.nvidia.com/blog/rendering-in-real-time-with-spatiotemporal-blue-noise-textures-part-1/"
  - name: "Blog part 2"
    url: "https://developer.nvidia.com/blog/rendering-in-real-time-with-spatiotemporal-blue-noise-textures-part-2/"
abstract: "Blue noise error patterns are well suited to human perception, and when applied to stochastic rendering techniques, blue noise masks (blue noise textures) minimize unwanted low-frequency noise in the final image. Current methods of applying blue noise masks at each frame independently produce white "
url: "https://research.nvidia.com/publication/2021-12_scalar-spatiotemporal-blue-noise-masks"
status: "new"
---

# Scalar Spatiotemporal Blue Noise Masks

## 摘要

Blue noise error patterns are well suited to human perception, and when applied to stochastic rendering techniques, blue noise masks (blue noise textures) minimize unwanted low-frequency noise in the final image. Current methods of applying blue noise masks at each frame independently produce white noise frequency spectra temporally. This white noise results in slower integration convergence over time and unstable results when filtered temporally. Unfortunately, achieving temporally stable blue noise distributions is non-trivial since 3D blue noise does not exhibit the desired 2D blue noise properties, and alternative approaches degrade the spatial blue noise qualities. We propose novel blue noise patterns that, when animated, produce values at a pixel that are well distributed over time, converge rapidly for Monte Carlo integration, and are more stable under TAA, while still retaining spatial blue noise properties. To do so, we propose an extension to the well-known void and cluster algorithm that reformulates the underlying energy function to produce spatiotemporal blue noise masks. These masks exhibit blue noise frequency spectra in both the spatial and temporal domains, resulting in visually pleasing error patterns, rapid convergence speeds, and increased stability when filtered temporally. We demonstrate these improvements on a variety of applications, including dithering, stochastic transparency, ambient occlusion, and volumetric rendering. By extending spatial blue noise to spatiotemporal blue noise, we overcome the convergence limitations of prior blue noise works, enabling new applications for blue noise distributions.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
