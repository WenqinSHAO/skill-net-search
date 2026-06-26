---
id: "arxiv-2876"
title: "Scaling Probe-Based Real-Time Dynamic Global Illumination for Production"
conference: "arXiv 2021"
date: "2021-05"
authors:
  - name: "Zander Majercik"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Adam Marrs"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Josef Spjut"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Morgan McGuire"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Graphics"
  - "Hyperscale Graphics"
  - "Real-Time Rendering"
external_links:
  - name: "Full-Text PDF"
    url: "https://jcgt.org/published/0010/02/01/paper.pdf"
  - name: "Low-resolution PDF"
    url: "https://jcgt.org/published/0010/02/01/paper-lowres.pdf"
abstract: "We contribute several practical extensions to the probe-based irradiance-field-with-visibility representation [Majercik et al. 2019] [McGuire et al. 2017] to improve image quality, constant and asymptotic performance, memory efficiency, and artist control. We developed these extensions in the proces"
url: "https://research.nvidia.com/publication/2021-05_scaling-probe-based-real-time-dynamic-global-illumination-production"
status: "new"
---

# Scaling Probe-Based Real-Time Dynamic Global Illumination for Production

## 摘要

We contribute several practical extensions to the probe-based irradiance-field-with-visibility representation [Majercik et al. 2019] [McGuire et al. 2017] to improve image quality, constant and asymptotic performance, memory efficiency, and artist control. We developed these extensions in the process of incorporating the previous work into the global illumination solutions of the NVIDIA RTXGI SDK, the Unity and Unreal Engine 4 game engines, and proprietary engines for several commercial games. These extensions include: an intuitive tuning parameter (the self-shadow bias); heuristics to speed transitions in the global illumination; reuse of irradiance data as prefiltered radiance for recursive glossy reflection; a probe state machine to prune work that will not affect the final image; and multiresolution cascaded volumes for large worlds.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
