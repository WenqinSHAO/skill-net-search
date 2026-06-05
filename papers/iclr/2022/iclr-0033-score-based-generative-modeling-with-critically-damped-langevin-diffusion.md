---
id: iclr-0033
title: "Score-Based Generative Modeling with Critically-Damped Langevin Diffusion"
conference: ICLR 2022
date: 2022-03
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
  - name: "Project Page and Code"
    url: "https://nv-tlabs.github.io/CLD-SGM/"
abstract: "Score-based generative models (SGMs) have demonstrated remarkable synthesis quality. SGMs rely on a diffusion process that gradually perturbs the data towards a tractable distribution, while the generative model learns to denoise. The complexity of this denoising task is, apart from the data distrib"
url: "https://research.nvidia.com/publication/2022-03_score-based-generative-modeling-critically-damped-langevin-diffusion"
status: new
---

# Score-Based Generative Modeling with Critically-Damped Langevin Diffusion

## 摘要

Score-based generative models (SGMs) have demonstrated remarkable synthesis quality. SGMs rely on a diffusion process that gradually perturbs the data towards a tractable distribution, while the generative model learns to denoise. The complexity of this denoising task is, apart from the data distribution itself, uniquely determined by the diffusion process. We argue that current SGMs employ overly simplistic diffusions, leading to unnecessarily complex denoising processes, which limit generative modeling performance. Based on connections to statistical mechanics, we propose a novel critically-damped Langevin diffusion (CLD) and show that CLD-based SGMs achieve superior performance. CLD can be interpreted as running a joint diffusion in an extended space, where the auxiliary variables can be considered "velocities" that are coupled to the data variables as in Hamiltonian dynamics. We derive a novel score matching objective for CLD and show that the model only needs to learn the score function of the conditional distribution of the velocity given data, an easier task than learning scores of the data directly. We also derive a new sampling scheme for efficient synthesis from CLD-based diffusion models. We find that CLD outperforms previous SGMs in synthesis quality for similar network architectures and sampling compute budgets. We show that our novel sampler for CLD significantly outperforms solvers such as Euler--Maruyama. Our framework provides new insights into score-based denoising diffusion models and can be readily used for high-resolution image synthesis.&nbsp;Project page and code available here.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
