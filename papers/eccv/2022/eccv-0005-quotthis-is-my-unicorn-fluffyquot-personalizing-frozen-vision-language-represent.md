---
id: eccv-0005
title: "&quot;This is my unicorn, Fluffy&quot;: Personalizing frozen vision-language representations"
conference: ECCV 2022
date: 2022-11
authors:
  - name: "Eli Meirom"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Gal Chechik"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yuval Atzmon"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Niv Cohen"
    affiliation: ""
    is_industry: false
  - name: "Rinon Gal"
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
abstract: "Large Vision &amp; Language models pretrained on web-scale data provide representations that are invaluable for numerous V&amp;L problems. However, it is unclear how they can be used for reasoning about user-specific visual concepts in unstructured language. This problem arises in multiple domains, "
url: "https://research.nvidia.com/publication/2022-11_my-unicorn-fluffy-personalizing-frozen-vision-language-representations"
status: new
---

# &quot;This is my unicorn, Fluffy&quot;: Personalizing frozen vision-language representations

## 摘要

Large Vision &amp; Language models pretrained on web-scale data provide representations that are invaluable for numerous V&amp;L problems. However, it is unclear how they can be used for reasoning about user-specific visual concepts in unstructured language. This problem arises in multiple domains, from personalized image retrieval to personalized interaction with smart devices. We introduce a new learning setup called Personalized Vision &amp; Language (PerVL) with two new benchmark datasets for retrieving and segmenting user-specific "personalized" concepts "in the wild". In PerVL, one should learn personalized concepts (1) independently of the downstream task (2) allowing a pretrained model to reason about them with free language, and (3) does not require personalized negative examples. We propose an architecture for solving PerVL that operates by extending the input vocabulary of a pretrained model with new word embeddings for the new personalized concepts. The model can then reason about them by simply using them in a sentence. We demonstrate that our approach learns personalized visual concepts from a few examples and can effectively apply them in image retrieval and semantic segmentation using rich textual queries.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
