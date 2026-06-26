---
id: "arxiv-2943"
title: "Neural Control Variates"
conference: "arXiv 2020"
date: "2020-11"
authors:
  - name: "Thomas Müller"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Fabrice Rousselle"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Alex Keller"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jan Novák"
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
  - name: "Paper PDF"
    url: "https://tom94.net/data/publications/mueller20neural/mueller20neural.pdf"
  - name: "SIGGRAPH Asia Presentation"
    url: "https://tom94.net/data/publications/mueller20neural/mueller20neural-sigasia.mp4"
  - name: "MCQMC Presentation"
    url: "https://tom94.net/data/publications/mueller20neural/variance-reduction-using-neural-networks.mp4"
  - name: "Paper Video"
    url: "https://tom94.net/data/publications/mueller20neural/mueller20neural.mp4"
  - name: "Interactive Results Viewer"
    url: "https://tom94.net/data/publications/mueller20neural/interactive-viewer/"
abstract: "We propose neural control variates (NCV) for unbiased variance reduction in parametric Monte Carlo integration. So far, the core challenge of applying the method of control variates has been finding a good approximation of the integrand that is cheap to integrate. We show that a set of neural networ"
url: "https://research.nvidia.com/publication/2020-11_neural-control-variates"
status: "new"
---

# Neural Control Variates

## 摘要

We propose neural control variates (NCV) for unbiased variance reduction in parametric Monte Carlo integration. So far, the core challenge of applying the method of control variates has been finding a good approximation of the integrand that is cheap to integrate. We show that a set of neural networks can face that challenge: a normalizing flow that approximates the shape of the integrand and another neural network that infers the solution of the integral equation. We also propose to leverage a neural importance sampler to estimate the difference between the original integrand and the learned control variate. To optimize the resulting parametric estimator, we derive a theoretically optimal, variance-minimizing loss function, and propose an alternative, composite loss for stable online training in practice. When applied to light transport simulation, neural control variates are capable of matching the state-of-the-art performance of other unbiased approaches, while providing means to develop more performant, practical solutions. Specifically, we show that the learned light-field approximation is of sufficient quality for high-order bounces, allowing us to omit the error correction and thereby dramatically reduce the noise at the cost of negligible visible bias.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
