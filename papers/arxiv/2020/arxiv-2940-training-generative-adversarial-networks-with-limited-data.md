---
id: "arxiv-2940"
title: "Training Generative Adversarial Networks with Limited Data"
conference: "arXiv 2020"
date: "2020-12"
authors:
  - name: "Tero Karras"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Miika Aittala"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Janne Hellsten"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Samuli Laine"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jaakko Lehtinen"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Timo Aila"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Foundation_models
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
  - "Generative AI"
external_links:
  - name: "ArXiv"
    url: "https://arxiv.org/abs/2006.06676"
  - name: "PyTorch implementation"
    url: "https://github.com/NVlabs/stylegan2-ada-pytorch"
  - name: "TensorFlow implementation"
    url: "https://github.com/NVlabs/stylegan2-ada"
  - name: "MetFaces dataset"
    url: "https://github.com/NVlabs/metfaces-dataset"
abstract: "Training generative adversarial networks (GAN) using too little data typically leads to discriminator overfitting, causing training to diverge. We propose an adaptive discriminator augmentation mechanism that significantly stabilizes training in limited data regimes. The approach does not require ch"
url: "https://research.nvidia.com/publication/2020-12_training-generative-adversarial-networks-limited-data"
status: "new"
---

# Training Generative Adversarial Networks with Limited Data

## 摘要

Training generative adversarial networks (GAN) using too little data typically leads to discriminator overfitting, causing training to diverge. We propose an adaptive discriminator augmentation mechanism that significantly stabilizes training in limited data regimes. The approach does not require changes to loss functions or network architectures, and is applicable both when training from scratch and when fine-tuning an existing GAN on another dataset. We demonstrate, on several datasets, that good results are now possible using only a few thousand training images, often matching StyleGAN2 results with an order of magnitude fewer images. We expect this to open up new application domains for GANs. We also find that the widely used CIFAR-10 is, in fact, a limited data benchmark, and improve the record FID from 5.59 to 2.67.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
