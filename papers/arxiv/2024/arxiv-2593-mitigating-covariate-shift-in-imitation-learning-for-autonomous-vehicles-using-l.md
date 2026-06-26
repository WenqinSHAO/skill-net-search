---
id: "arxiv-2593"
title: "Mitigating Covariate Shift in Imitation Learning for Autonomous Vehicles Using Latent Space Generative World Models"
conference: "arXiv 2024"
date: "2024-09"
authors:
  - name: "Alexander Popov"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Alperen Degirmenci"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "David Wehr"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Shashank Hegde"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ryan Oldja"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Alexey Kamenev"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Bertrand Douillard"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "David Nistér"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Urs Muller"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ruchi Bhargava"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Stan Birchfield"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Nikolai Smolyanskiy"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - Applied_perception
  - Computer Vision
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Applied Perception"
  - "Autonomous Vehicles"
  - "Computer Vision"
abstract: "We propose the use of latent space generative world models to address the covariate shift problem in autonomous driving. A world model is a neural network capable of predicting an agent's next state given past states and actions. By leveraging a world model during training, the driving policy effect"
url: "https://research.nvidia.com/publication/2024-09_mitigating-covariate-shift-imitation-learning-autonomous-vehicles-using-latent"
status: "new"
---

# Mitigating Covariate Shift in Imitation Learning for Autonomous Vehicles Using Latent Space Generative World Models

## 摘要

We propose the use of latent space generative world models to address the covariate shift problem in autonomous driving. A world model is a neural network capable of predicting an agent's next state given past states and actions. By leveraging a world model during training, the driving policy effectively mitigates covariate shift without requiring an excessive amount of training data. During end-to-end training, our policy learns how to recover from errors by aligning with states observed in human demonstrations, so that at runtime it can recover from perturbations outside the training distribution. Additionally, we introduce a novel transformer-based perception encoder that employs multi-view cross-attention and a learned scene query. We present qualitative and quantitative results, demonstrating significant improvements upon prior state of the art in closed-loop testing in the CARLA simulator, as well as showing the ability to handle perturbations in both CARLA and NVIDIA's DRIVE Sim.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
