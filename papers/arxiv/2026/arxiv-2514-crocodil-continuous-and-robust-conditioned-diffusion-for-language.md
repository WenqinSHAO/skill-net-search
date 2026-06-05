---
id: arxiv-2514
title: "CRoCoDiL: Continuous and Robust Conditioned Diffusion for Language"
conference: arXiv 2026
date: 2026-03
authors:
  - name: "Roy Uziel"
    affiliation: ""
    is_industry: false
  - name: "Omer Belhasin"
    affiliation: ""
    is_industry: false
  - name: "Itay Levy"
    affiliation: ""
    is_industry: false
  - name: "Akhiad Bercovich"
    affiliation: ""
    is_industry: false
  - name: "Ran El-Yaniv"
    affiliation: ""
    is_industry: false
  - name: "Ran Zilberstein"
    affiliation: ""
    is_industry: false
  - name: "Michael Elad"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - CUDA_ecosystem
  - Foundation_models
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Algorithms and Numerical Methods"
  - "Artificial Intelligence and Machine Learning"
  - "Generative AI"
abstract: "Masked Diffusion Models (MDMs) provide an efficient non-causal alternative to autoregressive generation but often struggle with token dependencies and semantic incoherence due to their reliance on discrete marginal distributions. We address these limitations by shifting the diffusion process into a "
url: "https://research.nvidia.com/publication/2026-03%5Fcrocodil-continuous-and-robust-conditioned-diffusion-language"
status: new
---

# CRoCoDiL: Continuous and Robust Conditioned Diffusion for Language

## 摘要

Masked Diffusion Models (MDMs) provide an efficient non-causal alternative to autoregressive generation but often struggle with token dependencies and semantic incoherence due to their reliance on discrete marginal distributions. We address these limitations by shifting the diffusion process into a continuous sentence-level semantic space. We propose CRoCoDiL -- Continuous and Robust Conditioned Diffusion for Language --&nbsp; a unified fine-tuning approach that jointly trains an encoder–demasker architecture, grounding the MDM demasking in continuous latent representations. This leads to the formation of a novel autoencoder in which the decoding is obtained by an MDM algorithm. Relying on the same framework, we proceed by introducing two unconditional text synthesis algorithms: Continuous-Then-Discrete (ConThenDisc), a hybrid-diffusion approach that first generates latent representations in continuous space and then decodes these to tokens via an MDM, and Continuous-Within-Discrete (ConWithinDisc), a multi-diffusion strategy that refines latent representations throughout the discrete sampling process. Experiments using LLaDA show that our methods achieve superior generation quality and more than x10 faster sampling speeds in an unconditional setting.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
