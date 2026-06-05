---
id: iclr-0034
title: "Tackling the Generative Learning Trilemma with Denoising Diffusion GANs"
conference: ICLR 2022
date: 2022-03
authors:
  - name: "Karsten Kreis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Arash Vahdat"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Zhisheng Xiao"
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
  - name: "Project Page and Code"
    url: "https://nvlabs.github.io/denoising-diffusion-gan/"
abstract: "A wide variety of deep generative models has been developed in the past decade. Yet, these models often struggle with simultaneously addressing three key requirements including: high sample quality, mode coverage, and fast sampling. We call the challenge imposed by these requirements the generative "
url: "https://research.nvidia.com/publication/2022-03_tackling-generative-learning-trilemma-denoising-diffusion-gans-0"
status: new
---

# Tackling the Generative Learning Trilemma with Denoising Diffusion GANs

## 摘要

A wide variety of deep generative models has been developed in the past decade. Yet, these models often struggle with simultaneously addressing three key requirements including: high sample quality, mode coverage, and fast sampling. We call the challenge imposed by these requirements the generative learning trilemma, as the existing models often trade some of them for others. Particularly, denoising diffusion models have shown impressive sample quality and diversity, but their expensive sampling does not yet allow them to be applied in many real-world applications. In this paper, we argue that slow sampling in these models is fundamentally attributed to the Gaussian assumption in the denoising step which is justified only for small step sizes. To enable denoising with large steps, and hence, to reduce the total number of denoising steps, we propose to model the denoising distribution using a complex multimodal distribution. We introduce denoising diffusion generative adversarial networks (denoising diffusion GANs) that model each denoising step using a multimodal conditional GAN. Through extensive evaluations, we show that denoising diffusion GANs obtain sample quality and diversity competitive with original diffusion models while being 2000×&nbsp;faster on the CIFAR-10 dataset. Compared to traditional GANs, our model exhibits better mode coverage and sample diversity. To the best of our knowledge, denoising diffusion GAN is the first model that reduces sampling cost in diffusion models to an extent that allows them to be applied to real-world applications inexpensively. Project page and code are available here.&nbsp;

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
