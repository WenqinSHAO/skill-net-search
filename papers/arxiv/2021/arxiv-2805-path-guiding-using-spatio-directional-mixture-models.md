---
id: "arxiv-2805"
title: "Path Guiding Using Spatio-Directional Mixture Models"
conference: "arXiv 2021"
date: "2021-12"
authors:
  - name: "Ana Dodik"
    affiliation: "Facebook"
    is_industry: true
  - name: "Marios Papas (Disney Research"
    affiliation: ""
    is_industry: false
  - name: "Studios)"
    affiliation: ""
    is_industry: false
  - name: "Cengiz Öztireli"
    affiliation: "University of Cambridge"
    is_industry: false
  - name: "Thomas Müller"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - CUDA_ecosystem
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Algorithms and Numerical Methods"
  - "Computer Graphics"
external_links:
  - name: "Code"
    url: "https://github.com/anadodik/sdmm-mitsuba"
  - name: "Interactive results viewer"
    url: "https://tom94.net/data/publications/dodik21pathguiding/interactive-viewer/"
  - name: "Video"
    url: "https://tom94.net/data/publications/dodik21pathguiding/dodik21pathguiding.mp4"
abstract: "We propose a learning-based method for light-path construction in path tracing algorithms, which iteratively optimizes and samples from what we refer to as spatio-directional Gaussian mixture models (SDMMs). In particular, we approximate incident radiance as an online-trained 5D mixture that is acce"
url: "https://research.nvidia.com/publication/2021-12_path-guiding-using-spatio-directional-mixture-models"
status: "new"
---

# Path Guiding Using Spatio-Directional Mixture Models

## 摘要

We propose a learning-based method for light-path construction in path tracing algorithms, which iteratively optimizes and samples from what we refer to as spatio-directional Gaussian mixture models (SDMMs). In particular, we approximate incident radiance as an online-trained 5D mixture that is accelerated by a kD-tree. Using the same framework, we approximate BSDFs as pre-trained nD mixtures, where n is the number of BSDF parameters. Such an approach addresses two major challenges in path-guiding models. First, the 5D radiance representation naturally captures correlation between the spatial and directional dimensions. Such correlations are present in e.g. parallax and caustics. Second, by using a tangent-space parameterization of Gaussians, our spatio-directional mixtures can perform approximate product sampling with arbitrarily oriented BSDFs. Existing models are only able to do this by either foregoing anisotropy of the mixture components or by representing the radiance field in local (normal aligned) coordinates, which both make the radiance field more difficult to learn. An additional benefit of the tangent-space parameterization is that each individual Gaussian is mapped to the solid sphere with low distortion near its center of mass. Our method performs especially well on scenes with small, localized luminaires that induce high spatio-directional correlation in the incident radiance.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
