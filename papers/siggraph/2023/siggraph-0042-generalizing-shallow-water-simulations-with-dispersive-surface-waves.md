---
id: "siggraph-0042"
title: "Generalizing Shallow Water Simulations with Dispersive Surface Waves"
conference: "SIGGRAPH 2023"
date: "2023-08"
authors:
  - name: "Stefan Jeschke"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Chris Wojtan"
    affiliation: "IST Austria"
    is_industry: false
topics:
  - AI & Machine Learning
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
abstract: "This paper introduces a novel method for simulating large bodies of water as a height field. At the start of each time step,we partition the waves into a bulk flow (which approximately satisfies the assumptions of the shallow water equations) and surface waves (which approximately satisfy the assump"
url: "https://research.nvidia.com/publication/2023-08_generalizing-shallow-water-simulations-dispersive-surface-waves"
status: "new"
---

# Generalizing Shallow Water Simulations with Dispersive Surface Waves

## 摘要

This paper introduces a novel method for simulating large bodies of water as a height field. At the start of each time step,we partition the waves into a bulk flow (which approximately satisfies the assumptions of the shallow water equations) and surface waves (which approximately satisfy the assumptions of Airy wave theory). We then solve the two wave regimes separately using appropriate state-of-the-art techniques, and re-combine the resulting wave velocities at the end of each step. This strategy leads to the first heightfield wave model capable of simulating complex interactions between both deep and shallow water effects, like the waves from a boat wake sloshing up onto a beach, or a dam break producing wave interference patterns and eddies.We also analyze the numerical dispersion created by our method and derive an exact correction factor for waves at a&nbsp; constant water depth, giving us a numerically perfect re-creation of theoretical water wave dispersion patterns.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
