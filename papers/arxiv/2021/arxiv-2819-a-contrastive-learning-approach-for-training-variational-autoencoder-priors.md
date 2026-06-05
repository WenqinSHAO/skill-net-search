---
id: arxiv-2819
title: "A Contrastive Learning Approach for Training Variational Autoencoder Priors"
conference: arXiv 2021
date: 2021-11
authors:
  - name: "Jan Kautz"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Arash Vahdat"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jyoti Aneja"
    affiliation: ""
    is_industry: false
  - name: "Alexander Schwing"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Computer Vision
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Vision"
abstract: "Variational autoencoders (VAEs) are one of the powerful likelihood-based generative models with applications in many domains. However, they struggle to generate high-quality images, especially when samples are obtained from the prior without any tempering. One explanation for VAEs' poor generative q"
url: "https://research.nvidia.com/publication/2021-11_contrastive-learning-approach-training-variational-autoencoder-priors"
status: new
---

# A Contrastive Learning Approach for Training Variational Autoencoder Priors

## 摘要

Variational autoencoders (VAEs) are one of the powerful likelihood-based generative models with applications in many domains. However, they struggle to generate high-quality images, especially when samples are obtained from the prior without any tempering. One explanation for VAEs' poor generative quality is the prior hole problem: the prior distribution fails to match the aggregate approximate posterior. Due to this mismatch, there exist areas in the latent space with high density under the prior that do not correspond to any encoded image. Samples from those areas are decoded to corrupted images. To tackle this issue, we propose an energy-based prior defined by the product of a base prior distribution and a reweighting factor, designed to bring the base closer to the aggregate posterior. We train the reweighting factor by noise contrastive estimation, and we generalize it to hierarchical VAEs with many latent variable groups. Our experiments confirm that the proposed noise contrastive priors improve the generative performance of state-of-the-art VAEs by a large margin on the MNIST, CIFAR-10, CelebA 64, and CelebA HQ 256 datasets. Our method is simple and can be applied to a wide variety of VAEs to improve the expressivity of their prior distribution.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
