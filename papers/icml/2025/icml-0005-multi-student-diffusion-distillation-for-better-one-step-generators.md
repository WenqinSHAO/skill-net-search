---
id: "icml-0005"
title: "Multi-student Diffusion Distillation for Better One-step Generators"
conference: "ICML 2025"
date: "2025-03"
authors:
  - name: "Yanke Song"
    affiliation: "NVIDIA, Harvard University"
    is_industry: true
  - name: "Jonathan Lorraine"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Weili Nie"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Karsten Kreis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "James Lucas"
    affiliation: "NVIDIA"
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
  - name: "Project Page"
    url: "https://research.nvidia.com/labs/toronto-ai/MSD/"
  - name: "Project Talk"
    url: "https://youtu.be/D03xFeHyLkE?si=nS1HRxmGpj8cI_yF"
abstract: "Diffusion models achieve high-quality sample generation at the cost of a lengthy multistep inference procedure. To overcome this, diffusion distillation techniques produce student generators capable of matching or surpassing the teacher in a single step. However, the student model’s inference speed "
url: "https://research.nvidia.com/publication/2025-03_multi-student-diffusion-distillation-better-one-step-generators"
status: "new"
---

# Multi-student Diffusion Distillation for Better One-step Generators

## 摘要

Diffusion models achieve high-quality sample generation at the cost of a lengthy multistep inference procedure. To overcome this, diffusion distillation techniques produce student generators capable of matching or surpassing the teacher in a single step. However, the student model’s inference speed is limited by the size of the teacher architecture, preventing real-time generation for computationally heavy applications. In this work, we introduce Multi-Student Distillation (MSD), a framework to distill a conditional teacher diffusion model into multiple single-step generators. Each student generator is responsible for a subset of the conditioning data, thereby obtaining higher generation quality for the same capacity. MSD trains multiple distilled students, allowing smaller sizes and, therefore, faster inference. Also, MSD offers a lightweight quality boost over single-student distillation with the same architecture. We demonstrate MSD is effective by training multiple same-sized or smaller students on single-step distillation using distribution matching and adversarial distillation techniques. With smaller students, MSD gets competitive results with faster inference for single-step generation. Using 4 same-sized students, MSD sets a new state-of-the-art for one-step image generation: FID 1.20 on ImageNet-64×64 and 8.20 on zero-shot COCO2014. Accepted to ICML 2025.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
