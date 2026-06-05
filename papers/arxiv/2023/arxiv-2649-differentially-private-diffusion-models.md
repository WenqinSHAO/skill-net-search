---
id: arxiv-2649
title: "Differentially Private Diffusion Models"
conference: arXiv 2023
date: 2023-08
authors:
  - name: "Arash Vahdat"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Karsten Kreis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Tim Dockhorn"
    affiliation: ""
    is_industry: false
  - name: "Tianshi Cao"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Computer Vision
  - Foundation_models
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Vision"
  - "Generative AI"
external_links:
  - name: "Project Website"
    url: "https://research.nvidia.com/labs/toronto-ai/DPDM/"
abstract: "While modern machine learning models rely on increasingly large training datasets, data is often limited in privacy-sensitive domains. Generative models trained with differential privacy (DP) on sensitive data can sidestep this challenge, providing access to synthetic data instead. We build on the r"
url: "https://research.nvidia.com/publication/2023-08_differentially-private-diffusion-models"
status: new
---

# Differentially Private Diffusion Models

## 摘要

While modern machine learning models rely on increasingly large training datasets, data is often limited in privacy-sensitive domains. Generative models trained with differential privacy (DP) on sensitive data can sidestep this challenge, providing access to synthetic data instead. We build on the recent success of diffusion models (DMs) and introduce Differentially Private Diffusion Models (DPDMs), which enforce privacy using differentially private stochastic gradient descent (DP-SGD). We investigate the DM parameterization and the sampling algorithm, which turn out to be crucial ingredients in DPDMs, and propose noise multiplicity, a powerful modification of DP-SGD tailored to the training of DMs. We validate our novel DPDMs on image generation benchmarks and achieve state-of-the-art performance in all experiments. Moreover, on standard benchmarks, classifiers trained on DPDM-generated synthetic data perform on par with task-specific DP-SGD-trained classifiers, which has not been demonstrated before for DP generative models. Project page and code: https://research.nvidia.com/labs/toronto-ai/DPDM/

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
