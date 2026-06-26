---
id: "arxiv-2807"
title: "Dynamic Diffuse Global Illumination Resampling"
conference: "arXiv 2021"
date: "2021-12"
authors:
  - name: "Zander Majercik"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Thomas Müller"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Alex Keller"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Derek Nowrouzezahrai"
    affiliation: "McGill University"
    is_industry: false
  - name: "Morgan McGuire"
    affiliation: "Roblox"
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
  - name: "Video"
    url: "https://tom94.net/data/publications/majercik21dynamic/majercik21dynamic.mp4"
abstract: "Interactive global illumination remains a challenge in radiometrically and geometrically complex scenes. Specialized sampling strategies are effective for specular and near-specular transport because the scattering has relatively low directional variance per scattering event. In contrast, the high v"
url: "https://research.nvidia.com/publication/2021-12_dynamic-diffuse-global-illumination-resampling"
status: "new"
---

# Dynamic Diffuse Global Illumination Resampling

## 摘要

Interactive global illumination remains a challenge in radiometrically and geometrically complex scenes. Specialized sampling strategies are effective for specular and near-specular transport because the scattering has relatively low directional variance per scattering event. In contrast, the high variance from transport paths comprising multiple rough glossy or diffuse scattering events remains notoriously difficult to resolve with a small number of samples. We extend unidirectional path tracing to address this by combining screen-space reservoir resampling and sparse world-space probes, significantly improving sample efficiency for transport contributions that terminate on diffuse scattering events. Our experiments demonstrate a clear improvement – at equal time and equal quality – over purely path traced and purely probe-based baselines. Moreover, when combined with commodity denoisers, we are able to interactively render global illumination in complex scenes.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
