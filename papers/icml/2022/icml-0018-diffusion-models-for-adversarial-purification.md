---
id: icml-0018
title: "Diffusion Models for Adversarial Purification"
conference: ICML 2022
date: 2022-07
authors:
  - name: "Chaowei Xiao"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Arash Vahdat"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Weili Nie"
    affiliation: ""
    is_industry: false
  - name: "Brandon Guo"
    affiliation: ""
    is_industry: false
  - name: "Yujia Huang"
    affiliation: ""
    is_industry: false
  - name: "Anima Anandkumar"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Foundation_models
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Generative AI"
abstract: "Adversarial purification refers to a class of defense methods that remove adversarial perturbations using a generative model. These methods do not make assumptions on the form of attack and the classification model, and thus can defend pre-existing classifiers against unseen threats. However, their "
url: "https://research.nvidia.com/publication/2022-07_diffusion-models-adversarial-purification"
status: new
---

# Diffusion Models for Adversarial Purification

## 摘要

Adversarial purification refers to a class of defense methods that remove adversarial perturbations using a generative model. These methods do not make assumptions on the form of attack and the classification model, and thus can defend pre-existing classifiers against unseen threats. However, their performance currently falls behind adversarial training methods. In this work, we propose&nbsp;DiffPure&nbsp;that uses diffusion models for adversarial purification: Given an adversarial example, we first diffuse it with a small amount of noise following a forward diffusion process, and then recover the clean image through a reverse generative process. To evaluate our method against strong adaptive attacks in an efficient and scalable way, we propose to use the adjoint method to compute full gradients of the reverse generative process. Extensive experiments on three image datasets including CIFAR-10, ImageNet, and CelebA-HQ with three classifier architectures including ResNet, WideResNet, and ViT demonstrate that our method achieves state-of-the-art results, outperforming current adversarial training and adversarial purification methods, often by a large margin. Code is available at our project page.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
