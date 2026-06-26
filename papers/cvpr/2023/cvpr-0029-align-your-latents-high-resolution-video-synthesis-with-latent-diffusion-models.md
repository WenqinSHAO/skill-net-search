---
id: "cvpr-0029"
title: "Align your Latents: High-Resolution Video Synthesis with Latent Diffusion Models"
conference: "CVPR 2023"
date: "2023-06"
authors:
  - name: "Andreas Blattmann"
    affiliation: "LMU Munich"
    is_industry: false
  - name: "Robin Rombach"
    affiliation: "LMU Munich"
    is_industry: false
  - name: "Huan Ling"
    affiliation: "NVIDIA, Vector Institute, University of Toronto"
    is_industry: true
  - name: "Tim Dockhorn"
    affiliation: "NVIDIA, University of Waterloo, Vector Institute"
    is_industry: true
  - name: "Seung Wook Kim"
    affiliation: "NVIDIA, Vector Institute, University of Toronto"
    is_industry: true
  - name: "Sanja Fidler"
    affiliation: "NVIDIA, Vector Institute, University of Toronto"
    is_industry: true
  - name: "Karsten Kreis"
    affiliation: "NVIDIA"
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
    url: "https://research.nvidia.com/labs/toronto-ai/VideoLDM/"
abstract: "Latent Diffusion Models (LDMs) enable high-quality image synthesis while avoiding excessive compute demands by training a diffusion model in a compressed lower-dimensional latent space. Here, we apply the LDM paradigm to high-resolution video generation, a particularly resource-intensive task. We fi"
url: "https://research.nvidia.com/publication/2023-06_align-your-latents-high-resolution-video-synthesis-latent-diffusion-models"
status: "new"
---

# Align your Latents: High-Resolution Video Synthesis with Latent Diffusion Models

## 摘要

Latent Diffusion Models (LDMs) enable high-quality image synthesis while avoiding excessive compute demands by training a diffusion model in a compressed lower-dimensional latent space. Here, we apply the LDM paradigm to high-resolution video generation, a particularly resource-intensive task. We first pre-train an LDM on images only; then, we turn the image generator into a video generator by introducing a temporal dimension to the latent space diffusion model and fine-tuning on encoded image sequences, i.e., videos. Similarly, we temporally align diffusion model upsamplers, turning them into temporally consistent video super resolution models. We focus on two relevant real-world applications: Simulation of in-the-wild driving data and creative content creation with text-to-video modeling. In particular, we validate our Video LDM on real driving videos of resolution 512 x 1024, achieving state-of-the-art performance. Furthermore, our approach can easily leverage off-the-shelf pre-trained image LDMs, as we only need to train a temporal alignment model in that case. Doing so, we turn the publicly available, state-of-the-art text-to-image LDM Stable Diffusion into an efficient and expressive text-to-video model with resolution up to 1280 x 2048. We show that the temporal layers trained in this way generalize to different fine-tuned text-to-image LDMs. Utilizing this property, we show the first results for personalized text-to-video generation, opening exciting directions for future content creation. Project page: https://research.nvidia.com/labs/toronto-ai/VideoLDM/

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
