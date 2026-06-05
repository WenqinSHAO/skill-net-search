---
id: cvpr-0010
title: "SimAvatar: Simulation-Ready Clothed Gaussian Avatars from Text"
conference: CVPR 2025
date: 2025-06
authors:
  - name: "Xueting Li"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ye Yuan"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Shalini De Mello"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jan Kautz"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Umar Iqbal"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Gilles Daviet"
    affiliation: ""
    is_industry: false
  - name: "Jonathan Leaf"
    affiliation: ""
    is_industry: false
  - name: "Miles Macklin"
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
  - name: "Project page"
    url: "https://nvlabs.github.io/SimAvatar/"
  - name: "ArXiv"
    url: "https://arxiv.org/abs/2412.09545"
  - name: "Video"
    url: "https://www.youtube.com/watch?v=qEwBY7LBW2Y"
abstract: "We introduce SimAvatar, a framework designed to generate simulation-ready clothed 3D human avatars from a text prompt. Current text-driven human avatar generation methods either model hair, clothing, and the human body using a unified geometry or produce hair and garments that are not easily adaptab"
url: "https://research.nvidia.com/publication/2025-06_simavatar-simulation-ready-clothed-gaussian-avatars-text"
status: new
---

# SimAvatar: Simulation-Ready Clothed Gaussian Avatars from Text

## 摘要

We introduce SimAvatar, a framework designed to generate simulation-ready clothed 3D human avatars from a text prompt. Current text-driven human avatar generation methods either model hair, clothing, and the human body using a unified geometry or produce hair and garments that are not easily adaptable for simulation within existing simulation pipelines. The primary challenge lies in representing the hair and garment geometry in a way that allows leveraging established prior knowledge from foundational image diffusion models (e.g., Stable Diffusion) while being simulation-ready using either physics or neural simulators. To address this task, we propose a two-stage framework that combines the flexibility of 3D Gaussians with simulationready hair strands and garment meshes. Specifically, we first employ three text-conditioned 3D generative models to generate garment mesh, body shape and hair strands from the given text prompt. To leverage prior knowledge from foundational diffusion models, we attach 3D Gaussians to the body mesh, garment mesh, as well as hair strands and learn the avatar appearance through optimization. To drive the avatar given a pose sequence, we first apply physics simulators onto the garment meshes and hair strands. We then transfer the motion onto 3D Gaussians through carefully designed mechanisms for each body part. As a result, our synthesized avatars have vivid texture and realistic dynamic motion. To the best of our knowledge, our method is the first to produce highly realistic, fully simulation-ready 3D avatars, surpassing the capabilities of current approaches.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
