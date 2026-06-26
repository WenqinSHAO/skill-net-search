---
id: "arxiv-2849"
title: "Rearchitecting Spatiotemporal Resampling for Production"
conference: "arXiv 2021"
date: "2021-07"
authors:
  - name: "Chris Wyman"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Alexey Panteleev"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Graphics"
external_links:
  - name: "Sample code available as part of RTXDI"
    url: "https://developer.nvidia.com/rtxdi"
  - name: "Denoiser code available as part of NRD (we used NRD&#039;s ReLAX algorithm)"
    url: "https://developer.nvidia.com/nvidia-rt-denoiser"
abstract: "Recent work by Bitterli et al. introduced a real-time, many-light algorithm for rendering dynamic direct illumination from millions of lights by iteratively applying resampled importance sampling using weighted reservoir sampling. While enabling new levels of lighting complexity in real-time, the to"
url: "https://research.nvidia.com/publication/2021-07_rearchitecting-spatiotemporal-resampling-production"
status: "new"
---

# Rearchitecting Spatiotemporal Resampling for Production

## 摘要

Recent work by Bitterli et al. introduced a real-time, many-light algorithm for rendering dynamic direct illumination from millions of lights by iteratively applying resampled importance sampling using weighted reservoir sampling. While enabling new levels of lighting complexity in real-time, the total cost remained beyond the budgets of even the most computationally demanding games. We introduce key algorithmic improvements developed while productizing this method that collectively reduce lighting costs by up to 7x, dramatically improve memory coherence, shrink the required ray budget, increase rendering quality, and expose parameters that enable trading quality for performance.&nbsp;

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
