---
id: arxiv-2749
title: "Spatiotemporal Blue Noise Masks"
conference: arXiv 2022
date: 2022-07
authors:
  - name: "Tomas Akenine-Möller"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Alan Wolfe"
    affiliation: ""
    is_industry: false
  - name: "Nathan Morrical"
    affiliation: ""
    is_industry: false
  - name: "Ravi Ramamoorthi"
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
abstract: "Blue noise error patterns are well suited to human perception, and when applied to stochastic rendering techniques, blue noise masks can minimize unwanted low-frequency noise in the final image. Current methods of applying different blue noise masks to each rendered frame result in either white nois"
url: "https://research.nvidia.com/publication/2022-07_spatiotemporal-blue-noise-masks"
status: new
---

# Spatiotemporal Blue Noise Masks

## 摘要

Blue noise error patterns are well suited to human perception, and when applied to stochastic rendering techniques, blue noise masks can minimize unwanted low-frequency noise in the final image. Current methods of applying different blue noise masks to each rendered frame result in either white noise frequency spectra temporally, and thus poor convergence and stability, or lower quality spatially. We propose novel blue noise masks that retain high quality blue noise spatially,&nbsp;yet when animated produce values at each pixel that are well distributed over time. To do so, we create scalar valued masks by modifying the energy function of the void and cluster algorithm. To create uniform and nonuniform vector valued masks, we make the same modifications to the&nbsp;blue-noise dithered sampling&nbsp;algorithm. These masks exhibit blue noise frequency spectra in both the spatial and&nbsp;temporal domains, resulting in visually pleasing error patterns, rapid&nbsp;convergence speeds, and increased stability when filtered temporally.&nbsp;Since masks can be initialized with arbitrary sample sets, these&nbsp;improvements can be used on a large variety of problems, both uniformly and importance sampled. We demonstrate these improvements in volumetric rendering, ambient occlusion,&nbsp;and stochastic convolution. By extending spatial blue noise to spatiotemporal blue noise, we overcome the&nbsp;convergence limitations of prior blue noise works, enabling new applications&nbsp;for blue noise distributions. Usable masks and source code can be found at https://github.com/NVIDIAGameWorks/SpatiotemporalBlueNoiseSDK.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
