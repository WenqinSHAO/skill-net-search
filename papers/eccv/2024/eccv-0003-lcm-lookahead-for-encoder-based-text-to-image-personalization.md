---
id: eccv-0003
title: "LCM-Lookahead for Encoder-based Text-to-Image Personalization"
conference: ECCV 2024
date: 2024-04
authors:
  - name: "Gal Chechik"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Rinon Gal"
    affiliation: ""
    is_industry: false
  - name: "Or Lichter"
    affiliation: ""
    is_industry: false
  - name: "Elad Richardson"
    affiliation: ""
    is_industry: false
  - name: "Or Patashnik"
    affiliation: ""
    is_industry: false
  - name: "Amit H Bermano"
    affiliation: ""
    is_industry: false
  - name: "Daniel Cohen-Or"
    affiliation: ""
    is_industry: false
topics:
  - Computer Vision
  - Foundation_models
  - Graphics_rendering
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Graphics"
  - "Computer Vision"
  - "Generative AI"
external_links:
  - name: "Project Page"
    url: "https://lcm-lookahead.github.io/"
abstract: "Recent advancements in diffusion models have introduced fast sampling methods that can effectively produce high-quality images in just one or a few denoising steps. Interestingly, when these are distilled from existing diffusion models, they often maintain alignment with the original model, retainin"
url: "https://research.nvidia.com/publication/2024-04_lcm-lookahead-encoder-based-text-image-personalization"
status: new
---

# LCM-Lookahead for Encoder-based Text-to-Image Personalization

## 摘要

Recent advancements in diffusion models have introduced fast sampling methods that can effectively produce high-quality images in just one or a few denoising steps. Interestingly, when these are distilled from existing diffusion models, they often maintain alignment with the original model, retaining similar outputs for similar prompts and seeds. These properties present opportunities to leverage fast sampling methods as a shortcut-mechanism, using them to create a preview of denoised outputs through which we can backpropagate image-space losses. In this work, we explore the potential of using such shortcut-mechanisms to guide the personalization of text-to-image models to specific facial identities. We focus on encoder-based personalization approaches, and demonstrate that by augmenting their training with a lookahead identity loss, we can achieve higher identity fidelity, without sacrificing layout diversity or prompt alignment.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
