---
id: arxiv-2547
title: "Score-based Diffusion Models in Function Space"
conference: arXiv 2025
date: 2025-07
authors:
  - name: "Nikola Kovachki"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jean Kossaifi"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Karsten Kreis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jan Kautz"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Arash Vahdat"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jae Hyun Lim"
    affiliation: ""
    is_industry: false
  - name: "Ricardo Baptista"
    affiliation: ""
    is_industry: false
  - name: "Christopher Beckham"
    affiliation: ""
    is_industry: false
  - name: "Kamyar Azizzadenesheli"
    affiliation: ""
    is_industry: false
  - name: "Vikram Voleti"
    affiliation: ""
    is_industry: false
  - name: "Jiaming Song"
    affiliation: ""
    is_industry: false
  - name: "Christopher Pal"
    affiliation: ""
    is_industry: false
  - name: "Anima Anandkumar"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Foundation_models
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Generative AI"
abstract: "Diffusion models have recently emerged as a powerful framework for generative modeling. They consist of a forward process that perturbs input data with Gaussian white noise and a reverse process that learns a score function to generate samples by denoising. Despite their tremendous success, they are"
url: "https://research.nvidia.com/publication/2025-07_score-based-diffusion-models-function-space"
status: new
---

# Score-based Diffusion Models in Function Space

## 摘要

Diffusion models have recently emerged as a powerful framework for generative modeling. They consist of a forward process that perturbs input data with Gaussian white noise and a reverse process that learns a score function to generate samples by denoising. Despite their tremendous success, they are mostly formulated on finite-dimensional spaces, e.g., Euclidean, limiting their applications to many domains where the data has a functional form, such as in scientific computing and 3D geometric data analysis. This work introduces a mathematically rigorous framework called Denoising Diffusion Operators (DDOs) for training diffusion models in function space. In DDOs, the forward process perturbs input functions gradually using a Gaussian process. The generative process is formulated by a function-valued annealed Langevin dynamic. Our approach requires an appropriate notion of the score for the perturbed data distribution, which we obtain by generalizing denoising score matching to function spaces that can be infinite-dimensional. We show that the corresponding discretized algorithm generates accurate samples at a fixed cost independent of the data resolution. We theoretically and numerically verify the applicability of our approach on a set of function-valued problems, including generating solutions to the Navier-Stokes equation viewed as the push-forward distribution of forcings from a Gaussian Random Field (GRF), as well as volcano InSAR and MNIST-SDF.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
