---
id: cvpr-0046
title: "Polymorphic-GAN: Generating Aligned Samples across Multiple Domains with Learned Morph Maps"
conference: CVPR 2022
date: 2022-06
authors:
  - name: "Karsten Kreis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Seung Wook Kim"
    affiliation: ""
    is_industry: false
  - name: "Daiqing Li"
    affiliation: ""
    is_industry: false
  - name: "Antonio Torralba"
    affiliation: ""
    is_industry: false
  - name: "Sanja Fidler"
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
  - name: "Project Website"
    url: "https://research.nvidia.com/labs/toronto-ai/PMGAN/"
abstract: "Modern image generative models show remarkable sample quality when trained on a single domain or class of objects. In this work, we introduce a generative adversarial network that can simultaneously generate aligned image samples from multiple related domains. We leverage the fact that a variety of "
url: "https://research.nvidia.com/publication/2022-06_polymorphic-gan-generating-aligned-samples-across-multiple-domains-learned"
status: new
---

# Polymorphic-GAN: Generating Aligned Samples across Multiple Domains with Learned Morph Maps

## 摘要

Modern image generative models show remarkable sample quality when trained on a single domain or class of objects. In this work, we introduce a generative adversarial network that can simultaneously generate aligned image samples from multiple related domains. We leverage the fact that a variety of object classes share common attributes, with certain geometric differences. We propose Polymorphic-GAN which learns shared features across all domains and a per-domain morph layer to morph shared features according to each domain. In contrast to previous works, our framework allows simultaneous modelling of images with highly varying geometries, such as images of human faces, painted and artistic faces, as well as multiple different animal faces. We demonstrate that our model produces aligned samples for all domains and show how it can be used for applications such as segmentation transfer and cross-domain image editing, as well as training in low-data regimes. Additionally, we apply our Polymorphic-GAN on image-to-image translation tasks and show that we can greatly surpass previous approaches in cases where the geometric differences between domains are large.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
