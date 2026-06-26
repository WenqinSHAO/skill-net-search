---
id: "arxiv-2741"
title: "Unbiased Inverse Volume Rendering With Differential Trackers"
conference: "arXiv 2022"
date: "2022-07"
authors:
  - name: "Merlin Nimier-David"
    affiliation: "EPFL"
    is_industry: false
  - name: "Thomas Müller"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Alex Keller"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Wenzel Jakob"
    affiliation: "EPFL"
    is_industry: false
topics:
  - AI & Machine Learning
  - CUDA_ecosystem
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Algorithms and Numerical Methods"
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
abstract: "Volumetric representations are popular in inverse rendering because they have a simple parameterization, are smoothly varying, and transparently handle topology changes.&nbsp;However, incorporating the full volumetric transport of light is costly and challenging, often leading practitioners to imple"
url: "https://research.nvidia.com/publication/2022-07_unbiased-inverse-volume-rendering-differential-trackers"
status: "new"
---

# Unbiased Inverse Volume Rendering With Differential Trackers

## 摘要

Volumetric representations are popular in inverse rendering because they have a simple parameterization, are smoothly varying, and transparently handle topology changes.&nbsp;However, incorporating the full volumetric transport of light is costly and challenging, often leading practitioners to implement simplified models, such as purely emissive and absorbing volumes with "baked" lighting.&nbsp;One such challenge is the efficient estimation of the gradients of the volume's appearance with respect to its scattering and absorption parameters.&nbsp;We show that the straightforward approach—differentiating a volumetric free-flight sampler—can lead to biased and high-variance gradients, hindering optimization.&nbsp;Instead, we propose using a new sampling strategy: differential ratio tracking, which is unbiased, yields low-variance gradients, and runs in linear time.&nbsp;Differential ratio tracking combines ratio tracking and reservoir sampling to estimate gradients by sampling distances proportional to the unweighted transmittance rather than the usual extinction-weighted transmittance.&nbsp;In addition, we observe local minima when optimizing scattering parameters to reproduce dense volumes or surfaces.&nbsp;We show that these local minima can be overcome by bootstrapping the optimization from nonphysical emissive volumes that are easily optimized.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
