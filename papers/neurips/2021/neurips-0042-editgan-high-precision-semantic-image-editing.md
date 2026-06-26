---
id: "neurips-0042"
title: "EditGAN: High-Precision Semantic Image Editing"
conference: "NeurIPS 2021"
date: "2021-12"
authors:
  - name: "Huan Ling"
    affiliation: "NVIDIA, University of Toronto, Vector Institute"
    is_industry: true
  - name: "Karsten Kreis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Daiqing Li"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Seung Wook Kim"
    affiliation: "NVIDIA, University of Toronto, Vector Institute"
    is_industry: true
  - name: "Antonio Torralba"
    affiliation: "MIT"
    is_industry: false
  - name: "Sanja Fidler"
    affiliation: "NVIDIA, University of Toronto, Vector Institute"
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
    url: "https://research.nvidia.com/labs/toronto-ai/editGAN/"
abstract: "Generative adversarial networks (GANs) have recently found applications in image editing. However, most GAN based image editing methods often require large scale datasets with semantic segmentation annotations for training, only provide high level control, or merely interpolate between different ima"
url: "https://research.nvidia.com/publication/2021-12_editgan-high-precision-semantic-image-editing"
status: "new"
---

# EditGAN: High-Precision Semantic Image Editing

## 摘要

Generative adversarial networks (GANs) have recently found applications in image editing. However, most GAN based image editing methods often require large scale datasets with semantic segmentation annotations for training, only provide high level control, or merely interpolate between different images. Here, we propose EditGAN, a novel method for high quality, high precision semantic image editing, allowing users to edit images by modifying their highly detailed part segmentation masks, e.g., drawing a new mask for the headlight of a car. EditGAN builds on a GAN framework that jointly models images and their semantic segmentations, requiring only a handful of labeled examples, making it a scalable tool for editing. Specifically, we embed an image into the GAN latent space and perform conditional latent code optimization according to the segmentation edit, which effectively also modifies the image. To amortize optimization, we find editing vectors in latent space that realize the edits. The framework allows us to learn an arbitrary number of editing vectors, which can then be directly applied on other images at interactive rates. We experimentally show that EditGAN can manipulate images with an unprecedented level of detail and freedom, while preserving full image quality.We can also easily combine multiple edits and perform plausible edits beyond EditGAN training data. We demonstrate EditGAN on a wide variety of image types and quantitatively outperform several previous editing methods on standard editing benchmark tasks.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
