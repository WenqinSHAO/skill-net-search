---
id: "arxiv-2652"
title: "An Approximate Mie Scattering Function for Fog and Cloud Rendering"
conference: "arXiv 2023"
date: "2023-08"
authors:
  - name: "Johannes Jendersie"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Eugene d'Eon"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Eugene d&#039;Eon"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Graphics"
  - "Real-Time Rendering"
abstract: "The Mie phase function describes the complex shapes that arise when light is scattered by water droplets. Inconvenient tables of data are required to include Mie scattering in a path tracer. To avoid this complexity, analytic models such as Cornette-Shanks (CS) or Henyey-Greenstein (HG) mixtures are"
url: "https://research.nvidia.com/publication/2023-08_approximate-mie-scattering-function-fog-and-cloud-rendering"
status: "new"
---

# An Approximate Mie Scattering Function for Fog and Cloud Rendering

## 摘要

The Mie phase function describes the complex shapes that arise when light is scattered by water droplets. Inconvenient tables of data are required to include Mie scattering in a path tracer. To avoid this complexity, analytic models such as Cornette-Shanks (CS) or Henyey-Greenstein (HG) mixtures are often used instead, resulting in a lack of accuracy for fog, clouds, skies and tissue. We show that a blend of HG and Draine's phase function can accurately match 95% of the Mie phase function over a wide range of droplet sizes. We provide a practical parameter fit for this mapping and derive analytic CDF inversion of the Draine (and CS) phase function, to produce a parametric approximation with fully analytic evaluation and sampling. In this talk we describe our fitting procedure, sampling derivations, and compare the proposed model to several others.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
