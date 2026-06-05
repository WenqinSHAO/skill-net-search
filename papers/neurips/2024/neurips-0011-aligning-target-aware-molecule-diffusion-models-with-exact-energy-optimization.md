---
id: neurips-0011
title: "Aligning Target-Aware Molecule Diffusion Models with Exact Energy Optimization"
conference: NeurIPS 2024
date: 2024-12
authors:
  - name: "Tomas Geffner"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Karsten Kreis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Arash Vahdat"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Siyi Gu"
    affiliation: ""
    is_industry: false
  - name: "Minkai Xu"
    affiliation: ""
    is_industry: false
  - name: "Alexander Powers"
    affiliation: ""
    is_industry: false
  - name: "Weili Nie"
    affiliation: ""
    is_industry: false
  - name: "Jure Leskovec"
    affiliation: ""
    is_industry: false
  - name: "Stefano Ermon"
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
external_links:
  - name: "arXiv"
    url: "https://arxiv.org/abs/2407.01648"
abstract: "Generating ligand molecules for specific protein targets, known as structure-based drug design, is a fundamental problem in therapeutics development and biological discovery. Recently, target-aware generative models, especially diffusion models, have shown great promise in modeling protein-ligand in"
url: "https://research.nvidia.com/publication/2024-12_aligning-target-aware-molecule-diffusion-models-exact-energy-optimization"
status: new
---

# Aligning Target-Aware Molecule Diffusion Models with Exact Energy Optimization

## 摘要

Generating ligand molecules for specific protein targets, known as structure-based drug design, is a fundamental problem in therapeutics development and biological discovery. Recently, target-aware generative models, especially diffusion models, have shown great promise in modeling protein-ligand interactions and generating candidate drugs. However, existing models primarily focus on learning the chemical distribution of all drug candidates, which lacks effective steerability on the chemical quality of model generations. In this paper, we propose a novel and general alignment framework to align pretrained target diffusion models with preferred functional properties, named AliDiff. AliDiff shifts the target-conditioned chemical distribution towards regions with higher binding affinity and structural rationality, specified by user-defined reward functions, via the preference optimization approach. To avoid the overfitting problem in common preference optimization objectives, we further develop an improved Exact Energy Preference Optimization method to yield an exact and efficient alignment of the diffusion models, and provide the closed-form expression for the converged distribution. Empirical studies on the CrossDocked2020 benchmark show that AliDiff can generate molecules with state-of-the-art binding energies with up to -7.07 Avg. Vina Score, while maintaining strong molecular properties.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
