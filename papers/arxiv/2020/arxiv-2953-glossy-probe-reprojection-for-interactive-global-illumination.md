---
id: arxiv-2953
title: "Glossy Probe Reprojection for Interactive Global Illumination"
conference: arXiv 2020
date: 2020-11
authors:
  - name: "Chris Wyman"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Simon Rodriguez"
    affiliation: ""
    is_industry: false
  - name: "Thomas Leimkühler"
    affiliation: ""
    is_industry: false
  - name: "Siddhant Prakash"
    affiliation: ""
    is_industry: false
  - name: "Peter Shirley"
    affiliation: ""
    is_industry: false
  - name: "George Drettakis"
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
abstract: "Recent rendering advances dramatically reduce the cost of global illumination. But even with hardware acceleration, complex light paths with multiple glossy interactions are still expensive; our new algorithm stores these paths in precomputed light probes and reprojects them at runtime to provide in"
url: "https://research.nvidia.com/publication/2020-11_glossy-probe-reprojection-interactive-global-illumination"
status: new
---

# Glossy Probe Reprojection for Interactive Global Illumination

## 摘要

Recent rendering advances dramatically reduce the cost of global illumination. But even with hardware acceleration, complex light paths with multiple glossy interactions are still expensive; our new algorithm stores these paths in precomputed light probes and reprojects them at runtime to provide interactivity. Combined with traditional light maps for diffuse lighting our approach interactively renders all light paths in static scenes with opaque objects. Naively reprojecting probes with glossy lighting is memory-intensive, requires efficient access to the correctly reflected radiance, and exhibits problems at occlusion boundaries in glossy reflections. Our solution addresses all these issues. To minimize memory, we introduce an adaptive light probe parameterization that allocates increased resolution for shinier surfaces and regions of higher geometric complexity. To efficiently sample glossy paths, our novel gathering algorithm reprojects probe texels in a view-dependent manner using efficient reflection estimation and a fast rasterization-based search. Naive probe reprojection often sharpens glossy reflections at occlusion boundaries, due to changes in parallax. To avoid this, we split the convolution induced by the BRDF into two steps: we precompute probes using a lower material roughness and apply an adaptive bilateral filter at runtime to reproduce the original surface roughness. Combining these elements, our algorithm interactively renders complex scenes while fitting in the memory, bandwidth, and computation constraints of current hardware.&nbsp;&nbsp;

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
