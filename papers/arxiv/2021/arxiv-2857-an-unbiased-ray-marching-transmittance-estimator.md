---
id: arxiv-2857
title: "An Unbiased Ray-Marching Transmittance Estimator"
conference: arXiv 2021
date: 2021-06
authors:
  - name: "Markus Kettunen"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Eugene d&#039;Eon"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jan Novák"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jacopo Pantaleoni"
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
abstract: "We present an in-depth analysis of the sources of variance in state-of-the-art unbiased volumetric transmittance estimators, and propose several new methods for improving their efficiency. These combine to produce a single estimator that is universally optimal relative to prior work, with up to seve"
url: "https://research.nvidia.com/publication/2021-06_unbiased-ray-marching-transmittance-estimator"
status: new
---

# An Unbiased Ray-Marching Transmittance Estimator

## 摘要

We present an in-depth analysis of the sources of variance in state-of-the-art unbiased volumetric transmittance estimators, and propose several new methods for improving their efficiency. These combine to produce a single estimator that is universally optimal relative to prior work, with up to several orders of magnitude lower variance at the same cost, and has zero variance for any ray with non-varying extinction. We first reduce the variance of truncated power-series estimators using a novel efficient application of U-statistics. We then greatly reduce the average expansion order of the power series and redistribute density evaluations to filter the optical depth estimates with an equidistant sampling comb. Combined with the use of an online control variate built from a sampled mean density estimate, the resulting estimator effectively performs ray marching most of the time while using rarely-sampled higher order terms to correct the bias.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
