---
id: "siggraph-0047"
title: "Encoder-based Domain Tuning for Fast Personalization of Text-to-Image Models"
conference: "SIGGRAPH 2023"
date: "2023-08"
authors:
  - name: "Rinon Gal"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Moab Arar"
    affiliation: "Tel-Aviv University"
    is_industry: false
  - name: "Yuval Atzmon"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Amit H. Bermano"
    affiliation: "Tel-Aviv University"
    is_industry: false
  - name: "Gal Chechik"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Daniel Cohen-Or"
    affiliation: "Tel-Aviv University"
    is_industry: false
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
  - name: "Project Page"
    url: "https://tuning-encoder.github.io/"
  - name: "Arxiv"
    url: "https://arxiv.org/abs/2302.12228"
abstract: "Text-to-image personalization aims to teach a pre-trained diffusion model to reason about novel, user provided concepts, embedding them into new scenes guided by natural language prompts. However, current personalization approaches struggle with lengthy training times, high storage requirements or l"
url: "https://research.nvidia.com/publication/2023-08_encoder-based-domain-tuning-fast-personalization-text-image-models"
status: "new"
---

# Encoder-based Domain Tuning for Fast Personalization of Text-to-Image Models

## 摘要

Text-to-image personalization aims to teach a pre-trained diffusion model to reason about novel, user provided concepts, embedding them into new scenes guided by natural language prompts. However, current personalization approaches struggle with lengthy training times, high storage requirements or loss of identity. To overcome these limitations, we propose an encoder-based domain-tuning approach. Our key insight is that by underfitting on a large set of concepts from a given domain, we can improve generalization and create a model that is more amenable to quickly adding novel concepts from the same domain. Specifically, we employ two components: First, an encoder that takes as an input a single image of a target concept from a given domain, e.g., a specific face, and learns to map it into a word-embedding representing the concept. Second, a set of regularized weight-offsets for the text-to-image model that learn how to effectively injest additional concepts. Together, these components are used to guide the learning of unseen concepts, allowing us to personalize a model using only a single image and as few as 5 training steps --- accelerating personalization from dozens of minutes to seconds, while preserving quality.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
