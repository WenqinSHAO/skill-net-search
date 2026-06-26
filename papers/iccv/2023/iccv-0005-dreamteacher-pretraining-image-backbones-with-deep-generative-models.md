---
id: "iccv-0005"
title: "DreamTeacher: Pretraining Image Backbones with Deep Generative Models"
conference: "ICCV 2023"
date: "2023-10"
authors:
  - name: "Daiqing Li"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Huan Ling"
    affiliation: "NVIDIA, Vector Institute, University of Toronto"
    is_industry: true
  - name: "Amlan Kar"
    affiliation: "NVIDIA, Vector Institute, University of Toronto"
    is_industry: true
  - name: "David Acuna"
    affiliation: "NVIDIA, Vector Institute, University of Toronto"
    is_industry: true
  - name: "Seung Wook Kim"
    affiliation: "NVIDIA, Vector Institute, University of Toronto"
    is_industry: true
  - name: "Karsten Kreis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Antonio Torralba"
    affiliation: "MIT"
    is_industry: false
  - name: "Sanja Fidler"
    affiliation: "NVIDIA, Vector Institute, University of Toronto"
    is_industry: true
topics:
  - AI & Machine Learning
  - Computer Vision
  - Foundation_models
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Vision"
  - "Generative AI"
external_links:
  - name: "Project Website"
    url: "https://research.nvidia.com/labs/toronto-ai/DreamTeacher/"
abstract: "In this work, we introduce a self-supervised feature representation learning framework DreamTeacher that utilizes generative networks for pre-training downstream image backbones. We propose to distill knowledge from a trained generative model into standard image backbones that have been well enginee"
url: "https://research.nvidia.com/publication/2023-10_dreamteacher-pretraining-image-backbones-deep-generative-models"
status: "new"
---

# DreamTeacher: Pretraining Image Backbones with Deep Generative Models

## 摘要

In this work, we introduce a self-supervised feature representation learning framework DreamTeacher that utilizes generative networks for pre-training downstream image backbones. We propose to distill knowledge from a trained generative model into standard image backbones that have been well engineered for specific perception tasks. We investigate two types of knowledge distillation: 1) distilling learned generative features onto target image backbones as an alternative to pretraining these backbones on large labeled datasets such as ImageNet, and 2) distilling labels obtained from generative networks with task heads onto logits of target backbones. We perform extensive analyses on multiple generative models, dense prediction benchmarks, and several pre-training regimes. We empirically find that our DreamTeacher significantly outperforms existing self-supervised representation learning approaches across the board. Unsupervised ImageNet pre-training with DreamTeacher leads to significant improvements over ImageNet classification pre-training on downstream datasets, showcasing generative models, and diffusion generative models specifically, as a promising approach to representation learning on large, diverse datasets without requiring manual annotation.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
