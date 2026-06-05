---
id: neurips-0027
title: "Syntactic Binding in Diffusion Models: Enhancing Attribute Correspondence through Attention Map Alignment"
conference: NeurIPS 2023
date: 2023-10
authors:
  - name: "Gal Chechik"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Royi Rassin"
    affiliation: ""
    is_industry: false
  - name: "Eran Hirsch"
    affiliation: ""
    is_industry: false
  - name: "Daniel Glickman"
    affiliation: ""
    is_industry: false
  - name: "Shauli Ravfogel"
    affiliation: ""
    is_industry: false
  - name: "Yoav Goldberg"
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
  - name: "Arxiv"
    url: "https://arxiv.org/abs/2306.08877"
abstract: "Text-conditioned image generation models often generate incorrect associations between entities and their visual attributes. This reflects an impaired mapping between linguistic binding of entities and modifiers in the prompt and visual binding of the corresponding elements in the generated image. A"
url: "https://research.nvidia.com/publication/2023-10_syntactic-binding-diffusion-models-enhancing-attribute-correspondence-through"
status: new
---

# Syntactic Binding in Diffusion Models: Enhancing Attribute Correspondence through Attention Map Alignment

## 摘要

Text-conditioned image generation models often generate incorrect associations between entities and their visual attributes. This reflects an impaired mapping between linguistic binding of entities and modifiers in the prompt and visual binding of the corresponding elements in the generated image. As one notable example, a query like ``a yellow tomato and a red lemon'' may incorrectly produce an image of a yellow lemon and a red tomato. To remedy this issue, we propose SynGen, an approach which first syntactically analyses the prompt to identify entities and their modifiers, and then uses a novel loss function that encourages the cross-attention maps to agree with the linguistic binding reflected by the syntax. Specifically, we encourage large overlap between attention maps of entities and their modifiers, and small overlap with other entities and modifier words. The loss is optimized during inference, without retraining the model. Human evaluation on three datasets, including one new and challenging set, demonstrate significant improvements of SynGen compared with current state of the art methods. This work highlights how making use of sentence structure during inference can efficiently and substantially improve the faithfulness of text-to-image generation.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
