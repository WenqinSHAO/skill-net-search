---
id: "arxiv-2986"
title: "Spatiotemporal reservoir resampling for real-time ray tracing with dynamic direct lighting"
conference: "arXiv 2020"
date: "2020-07"
authors:
  - name: "Benedikt Bitterli"
    affiliation: "Dartmouth College"
    is_industry: false
  - name: "Chris Wyman"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Matt Pharr"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Peter Shirley"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Aaron Lefohn"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Wojciech Jarosz"
    affiliation: "Dartmouth College"
    is_industry: false
topics:
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Graphics"
  - "Real-Time Rendering"
external_links:
  - name: "Technical Paper Video (~500 MB .mp4)"
    url: "https://research.nvidia.com/labs/rtr/publication/bitterli2020spatiotemporal/sig20_ReSTIR_goodQuality.mp4"
  - name: "Technical Paper Supplementary Files (~500 MB .zip)"
    url: "https://research.nvidia.com/labs/rtr/publication/bitterli2020spatiotemporal/sig20_ReSTIR_supplementary.zip"
abstract: "Efficiently rendering direct lighting from millions of dynamic light sources using Monte Carlo integration remains a challenging problem, even for off-line rendering systems. We introduce a new algorithm—ReSTIR—that renders such lighting interactively, at high quality, and without needing to maintai"
url: "https://research.nvidia.com/publication/2020-07_spatiotemporal-reservoir-resampling-real-time-ray-tracing-dynamic-direct"
status: "new"
---

# Spatiotemporal reservoir resampling for real-time ray tracing with dynamic direct lighting

## 摘要

Efficiently rendering direct lighting from millions of dynamic light sources using Monte Carlo integration remains a challenging problem, even for off-line rendering systems. We introduce a new algorithm—ReSTIR—that renders such lighting interactively, at high quality, and without needing to maintain complex data structures. We repeatedly resample a set of candidate light samples and apply further spatial and temporal resampling to leverage information from relevant nearby samples. We derive an unbiased Monte Carlo estimator for this approach, and show that it achieves equal-error 6-60× faster than state-of-the-art methods. A biased estimator reduces noise further and is 35-65× faster, at the cost of some energy loss. We implemented our approach on the GPU, rendering complex scenes containing up to 3.4 million dynamic, emissive triangles in under 50ms per frame while tracing at most 8 rays per pixel.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
