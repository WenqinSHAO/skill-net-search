---
id: "siggraph-0053"
title: "Recursive Control Variates for Inverse Rendering"
conference: "SIGGRAPH 2023"
date: "2023-05"
authors:
  - name: "Baptiste Nicolet"
    affiliation: "École Polytechnique Fédérale de Lausanne (EPFL) and NVIDIA"
    is_industry: true
  - name: "Fabrice Rousselle"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jan Novák"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Alexander Keller"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Wenzel Jakob"
    affiliation: "École Polytechnique Fédérale de Lausanne (EPFL)"
    is_industry: false
  - name: "Thomas Müller"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
external_links:
  - name: "Project page"
    url: "https://rgl.epfl.ch/publications/Nicolet2023Recursive"
abstract: "We present a method for reducing errors---variance and bias---in physically based differentiable rendering (PBDR). Typical applications of PBDR repeatedly render a scene as part of an optimization loop involving gradient descent. The actual change introduced by each gradient descent step is often re"
url: "https://research.nvidia.com/publication/2023-05_recursive-control-variates-inverse-rendering"
status: "new"
---

# Recursive Control Variates for Inverse Rendering

## 摘要

We present a method for reducing errors---variance and bias---in physically based differentiable rendering (PBDR). Typical applications of PBDR repeatedly render a scene as part of an optimization loop involving gradient descent. The actual change introduced by each gradient descent step is often relatively small, causing a significant degree of redundancy in this computation. We exploit this redundancy by formulating a gradient estimator that employs a \emph{recursive control variate}, which leverages information from previous optimization steps. The control variate reduces variance in gradients, and, perhaps more importantly, alleviates issues that arise from differentiating %non-$\L^2$ loss functions with respect to noisy inputs, a common cause of drift to bad local minima or divergent optimizations. We experimentally evaluate our approach on a variety of path-traced scenes containing surfaces and volumes and observe that primal rendering efficiency improves by a factor of up to 10.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
