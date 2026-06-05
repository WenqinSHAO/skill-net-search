---
id: cvpr-0006
title: "Make It Count: Text-to-Image Generation with an Accurate Number of Objects"
conference: CVPR 2025
date: 2025-06
authors:
  - name: "Yoad Tewel"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Gal Chechik"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Lital Binyamin"
    affiliation: ""
    is_industry: false
  - name: "Eran Hirsch"
    affiliation: ""
    is_industry: false
  - name: "Royi Rassin"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Foundation_models
  - Graphics_rendering
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
  - "Generative AI"
external_links:
  - name: "Arxiv"
    url: "https://arxiv.org/abs/2406.10210"
  - name: "project page"
    url: "https://make-it-count-paper.github.io/"
abstract: "Despite the unprecedented success of text-to-image diffusion models, controlling the number of depicted objects using text is surprisingly hard. This is important for various applications from technical documents, to children's books to illustrating cooking recipes. Generating object-correct counts "
url: "https://research.nvidia.com/publication/2025-06_make-it-count-text-image-generation-accurate-number-objects"
status: new
---

# Make It Count: Text-to-Image Generation with an Accurate Number of Objects

## 摘要

Despite the unprecedented success of text-to-image diffusion models, controlling the number of depicted objects using text is surprisingly hard. This is important for various applications from technical documents, to children's books to illustrating cooking recipes. Generating object-correct counts is fundamentally challenging because the generative model needs to keep a sense of separate identity for every instance of the object, even if several objects look identical or overlap, and then carry out a global computation implicitly during generation. It is still unknown if such representations exist. To address count-correct generation, we first identify features within the diffusion model that can carry the object identity information. We then use them to separate and count instances of objects during the denoising process and detect over-generation and under-generation. We fix the latter by training a model that predicts both the shape and location of a missing object, based on the layout of existing ones, and show how it can be used to guide denoising with correct object count. Our approach, CountGen, does not depend on external source to determine object layout, but rather uses the prior from the diffusion model itself, creating prompt-dependent and seed-dependent layouts. Evaluated on two benchmark datasets, we find that CountGen strongly outperforms the count-accuracy of existing baselines.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
