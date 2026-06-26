---
id: "siggraph-0007"
title: "Radiance Surfaces: Optimizing Surface Representations with a 5D Radiance Field Loss"
conference: "SIGGRAPH 2025"
date: "2025-07"
authors:
  - name: "Ziyi Zhang"
    affiliation: "École Polytechnique Fédérale de Lausanne (EPFL) and NVIDIA"
    is_industry: true
  - name: "Nicolas Roussel"
    affiliation: "École Polytechnique Fédérale de Lausanne (EPFL)"
    is_industry: false
  - name: "Thomas Müller"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Tizian Zeltner"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Merlin Nimier-David"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Fabrice Rousselle"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Wenzel Jakob"
    affiliation: "École Polytechnique Fédérale de Lausanne (EPFL) and NVIDIA"
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
  - "Real-Time Rendering"
external_links:
  - name: "Project Page"
    url: "https://rgl.epfl.ch/publications/Zhang2025Radiance"
abstract: "We present a fast and simple technique to convert images into a radiance surface-based scene representation. Building on existing radiance volume reconstruction algorithms, we introduce a subtle yet impactful modification of the loss function requiring changes to only a few lines of code: instead of"
url: "https://research.nvidia.com/publication/2025-07_radiance-surfaces-optimizing-surface-representations-5d-radiance-field-loss"
status: "new"
---

# Radiance Surfaces: Optimizing Surface Representations with a 5D Radiance Field Loss

## 摘要

We present a fast and simple technique to convert images into a radiance surface-based scene representation. Building on existing radiance volume reconstruction algorithms, we introduce a subtle yet impactful modification of the loss function requiring changes to only a few lines of code: instead of integrating the radiance field along rays and supervising the resulting images, we project the training images into the scene to directly supervise the spatio-directional radiance field. The primary outcome of this change is the complete removal of alpha blending and ray marching from the image formation model, instead moving these steps into the loss computation. In addition to promoting convergence to surfaces, this formulation assigns explicit semantic meaning to 2D subsets of the radiance field, turning them into well-defined radiance surfaces. We finally extract a level set from this representation, which results in a high-quality radiance surface model. Our method retains much of the speed and quality of the baseline algorithm. For instance, a suitably modified variant of Instant NGP maintains comparable computational efficiency, while achieving an average PSNR that is only 0.1 dB lower. Most importantly, our method generates explicit surfaces in place of an exponential volume, doing so with a level of simplicity not seen in prior work.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
