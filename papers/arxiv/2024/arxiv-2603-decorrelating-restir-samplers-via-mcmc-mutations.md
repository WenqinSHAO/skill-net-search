---
id: arxiv-2603
title: "Decorrelating ReSTIR Samplers via MCMC Mutations"
conference: arXiv 2024
date: 2024-07
authors:
  - name: "Daqi Lin"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Markus Kettunen"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Benedikt Bitterli"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ravi Ramamoorthi"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Chris Wyman"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Matt Pharr"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Rohan Sawhney"
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
external_links:
  - name: "Paper"
    url: "https://dl.acm.org/doi/10.1145/3629166"
abstract: "Monte Carlo rendering algorithms often utilize correlations between pixels to improve efficiency and enhance image quality. For real-time applications in particular, repeated reservoir resampling offers a powerful framework to reuse samples both spatially in an image and temporally across multiple f"
url: "https://research.nvidia.com/publication/2024-07_decorrelating-restir-samplers-mcmc-mutations"
status: new
---

# Decorrelating ReSTIR Samplers via MCMC Mutations

## 摘要

Monte Carlo rendering algorithms often utilize correlations between pixels to improve efficiency and enhance image quality. For real-time applications in particular, repeated reservoir resampling offers a powerful framework to reuse samples both spatially in an image and temporally across multiple frames. While such techniques achieve equal-error up to 100× faster for real-time direct lighting [Bitterli et al. 2020] and global illumination [Ouyang et al. 2021; Lin et al. 2021], they are still far from optimal. For instance, spatiotemporal resampling often introduces noticeable correlation artifacts, while reservoirs holding more than one sample suffer from impoverishment in the form of duplicate samples. We demonstrate how interleaving Markov Chain Monte Carlo (MCMC) mutations with reservoir resampling helps alleviate these issues, especially in scenes with glossy materials and difficult-to-sample lighting. Moreover, our approach does not introduce any bias, and in practice, we find considerable improvement in image quality with just a single mutation per reservoir sample in each frame.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
