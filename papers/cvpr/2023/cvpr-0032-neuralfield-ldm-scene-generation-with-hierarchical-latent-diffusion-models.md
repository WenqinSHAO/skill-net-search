---
id: cvpr-0032
title: "NeuralField-LDM: Scene Generation with Hierarchical Latent Diffusion Models"
conference: CVPR 2023
date: 2023-06
authors:
  - name: "Karsten Kreis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Seung Wook Kim"
    affiliation: ""
    is_industry: false
  - name: "Bradley Brown"
    affiliation: ""
    is_industry: false
  - name: "Kangxue Yin"
    affiliation: ""
    is_industry: false
  - name: "Katja Schwarz"
    affiliation: ""
    is_industry: false
  - name: "Daiqing Li"
    affiliation: ""
    is_industry: false
  - name: "Robin Rombach"
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
    url: "https://research.nvidia.com/labs/toronto-ai/NFLDM/"
abstract: "Automatically generating high-quality real world 3D scenes is of enormous interest for applications such as virtual reality and robotics simulation. Towards this goal, we introduce NeuralField-LDM, a generative model capable of synthesizing complex 3D environments. We leverage Latent Diffusion Model"
url: "https://research.nvidia.com/publication/2023-06_neuralfield-ldm-scene-generation-hierarchical-latent-diffusion-models"
status: new
---

# NeuralField-LDM: Scene Generation with Hierarchical Latent Diffusion Models

## 摘要

Automatically generating high-quality real world 3D scenes is of enormous interest for applications such as virtual reality and robotics simulation. Towards this goal, we introduce NeuralField-LDM, a generative model capable of synthesizing complex 3D environments. We leverage Latent Diffusion Models that have been successfully utilized for efficient high-quality 2D content creation. We first train a scene auto-encoder to express a set of image and pose pairs as a neural field, represented as density and feature voxel grids that can be projected to produce novel views of the scene. To further compress this representation, we train a latent-autoencoder that maps the voxel grids to a set of latent representations. A hierarchical diffusion model is then fit to the latents to complete the scene generation pipeline. We achieve a substantial improvement over existing state-of-the-art scene generation models. Additionally, we show how NeuralField-LDM can be used for a variety of 3D content creation applications, including conditional scene generation, scene inpainting and scene style manipulation.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
