---
id: "icml-0001"
title: "GenMol: A Drug Discovery Generalist with Discrete Diffusion"
conference: "ICML 2025"
date: "2025-07"
authors:
  - name: "Seul Lee"
    affiliation: "KAIST"
    is_industry: false
  - name: "Karsten Kreis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Srimukh Prasad Veccham"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Meng Liu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Danny Reidenbach"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yuxing Peng"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Saee Paliwal"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Weili Nie"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Arash Vahdat"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Foundation_models
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Generative AI"
abstract: "Drug discovery is a complex process that involves multiple stages and tasks. However, existing molecular generative models can only tackle some of these tasks. We present Generalist Molecular generative model (GenMol), a versatile framework that uses only a single discrete diffusion model to handle "
url: "https://research.nvidia.com/publication/2025-07_genmol-drug-discovery-generalist-discrete-diffusion"
status: "new"
---

# GenMol: A Drug Discovery Generalist with Discrete Diffusion

## 摘要

Drug discovery is a complex process that involves multiple stages and tasks. However, existing molecular generative models can only tackle some of these tasks. We present Generalist Molecular generative model (GenMol), a versatile framework that uses only a single discrete diffusion model to handle diverse drug discovery scenarios. GenMol generates Sequential Attachment-based Fragment Embedding (SAFE) sequences through non-autoregressive bidirectional parallel decoding, thereby allowing the utilization of a molecular context that does not rely on the specific token ordering while having better sampling efficiency. GenMol uses fragments as basic building blocks for molecules and introduces fragment remasking, a strategy that optimizes molecules by regenerating masked fragments, enabling effective exploration of chemical space. We further propose molecular context guidance (MCG), a guidance method tailored for masked discrete diffusion of GenMol. GenMol significantly outperforms the previous GPT-based model in de novo generation and fragment-constrained generation, and achieves state-of-the-art performance in goal-directed hit generation and lead optimization. These results demonstrate that GenMol can tackle a wide range of drug discovery tasks, providing a unified and versatile approach for molecular design. Our code is available at https://github.com/NVIDIA-Digital-Bio/genmol.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
