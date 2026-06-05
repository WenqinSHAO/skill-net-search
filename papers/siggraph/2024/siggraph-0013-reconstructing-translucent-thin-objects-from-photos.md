---
id: siggraph-0013
title: "Reconstructing Translucent Thin Objects from Photos"
conference: SIGGRAPH 2024
date: 2024-11
authors:
  - name: "Lifan Wu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Eugene d&#039;Eon"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Andrea Weidlich"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Xi Deng"
    affiliation: ""
    is_industry: false
  - name: "Bruce Walter"
    affiliation: ""
    is_industry: false
  - name: "Ravi Ramamoorthi"
    affiliation: ""
    is_industry: false
  - name: "Steve Marschner"
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
abstract: "The joint reconstruction of shape and appearance for translucent objects from real-world data poses a challenge in computer graphics, especially when dealing with complex layered materials like leaves or paper. The traditional assumption of diffuse transmittance falls short, and more accurate Monte-"
url: "https://research.nvidia.com/publication/2024-11_reconstructing-translucent-thin-objects-photos"
status: new
---

# Reconstructing Translucent Thin Objects from Photos

## 摘要

The joint reconstruction of shape and appearance for translucent objects from real-world data poses a challenge in computer graphics, especially when dealing with complex layered materials like leaves or paper. The traditional assumption of diffuse transmittance falls short, and more accurate Monte-Carlo-based models are often needed to reproduce their appearance. To accurately capture the translucent appearance, an acquisition system needs to be carefully designed. Additionally, there are three challenges for inverse rendering: First, a large number of unknown parameters make the optimization problem difficult. Second, the Monte Carlo (MC) renderer introduces noise, which the optimization is sensitive to, especially when dealing with complex material models such as rough dielectric surfaces and highly scattering participating media. Last, MC estimators using long light paths (up to 32 bounces in our case) create a large computation graph in memory, making the gradient back-propagation costly. To address those challenges, we present an affordable and fast acquisition pipeline that can capture spatially varying reflectance and transmission at the same time, using a two-phase optimization. We first initialize the geometry with the traditional vision method and then fit a simple and fast appearance model. Thereafter, we use the estimated parameters to initialize a second optimization using a more expensive volumetric model, which converges faster and more reliably from this favorable starting position. We also introduce a way to analyze each parameter’s sensitivity to the noise in the measurements, which can be used in optimally selecting useful measurements for optimization. Furthermore, instead of iterating on the camera system, we also introduce a weighted L2 loss as an alternative for selecting useful pixels from existing measurements.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
