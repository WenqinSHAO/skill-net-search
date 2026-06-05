---
id: neurips-0001
title: "Policy Optimized Text-to-Image Pipeline Design"
conference: NeurIPS 2025
date: 2025-12
authors:
  - name: "Gal Chechik"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Shie Mannor"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Uri Gadot"
    affiliation: ""
    is_industry: false
  - name: "Rinon Gal"
    affiliation: ""
    is_industry: false
  - name: "Yftah Zisser"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Graphics_rendering
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
external_links:
  - name: "Arxiv"
    url: "https://arxiv.org/abs/2505.21478"
abstract: "Text-to-image generation has evolved beyond single monolithic models to complex multi-component pipelines. These combine fine-tuned generators, adapters, upscaling blocks and even editing steps, leading to significant improvements in image quality. However, their effective design requires substantia"
url: "https://research.nvidia.com/publication/2025-12_policy-optimized-text-image-pipeline-design"
status: new
---

# Policy Optimized Text-to-Image Pipeline Design

## 摘要

Text-to-image generation has evolved beyond single monolithic models to complex multi-component pipelines. These combine fine-tuned generators, adapters, upscaling blocks and even editing steps, leading to significant improvements in image quality. However, their effective design requires substantial expertise. Recent approaches have shown promise in automating this process through large language models (LLMs), but they suffer from two critical limitations: extensive computational requirements from generating images with hundreds of predefined pipelines, and poor generalization beyond memorized training examples. We introduce a novel reinforcement learning-based framework that addresses these inefficiencies. Our approach first trains an ensemble of reward models capable of predicting image quality scores directly from prompt-workflow combinations, eliminating the need for costly image generation during training. We then implement a two-phase training strategy: initial workflow vocabulary training followed by GRPO-based optimization that guides the model toward higher-performing regions of the workflow space. Additionally, we incorporate a classifier-free guidance based enhancement technique that extrapolates along the path between the initial and GRPO-tuned models, further improving output quality. We validate our approach through a set of comparisons, showing that it can successfully create new flows with greater diversity and lead to superior image quality compared to existing baselines.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
