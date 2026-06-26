---
id: "siggraph-0038"
title: "Live 3D Portrait: Real-Time Radiance Fields for Single-Image Portrait View Synthesis"
conference: "SIGGRAPH 2023"
date: "2023-08"
authors:
  - name: "Alexander Trevithick"
    affiliation: "UC San Diego"
    is_industry: false
  - name: "Matthew Chan"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Michael Stengel"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Eric R. Chan"
    affiliation: "Stanford University"
    is_industry: false
  - name: "Chao Liu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Zhiding Yu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Sameh Khamis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Manmohan Chandraker"
    affiliation: "UC San Diego"
    is_industry: false
  - name: "Ravi Ramamoorthi"
    affiliation: "UC San Diego"
    is_industry: false
  - name: "Koki Nagano"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Computer Vision
  - Foundation_models
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
  - "Computer Vision"
  - "Generative AI"
  - "VR, AR and Display Technology"
external_links:
  - name: "Project"
    url: "https://research.nvidia.com/labs/nxp/lp3d/"
abstract: "We present a one-shot method to infer and render a photorealistic 3D representation from a single unposed image (e.g., face portrait) in real-time. Given a single RGB input, our image encoder directly predicts a canonical triplane representation of a neural radiance field for 3D-aware novel view syn"
url: "https://research.nvidia.com/publication/2023-08_live-3d-portrait-real-time-radiance-fields-single-image-portrait-view-synthesis"
status: "new"
---

# Live 3D Portrait: Real-Time Radiance Fields for Single-Image Portrait View Synthesis

## 摘要

We present a one-shot method to infer and render a photorealistic 3D representation from a single unposed image (e.g., face portrait) in real-time. Given a single RGB input, our image encoder directly predicts a canonical triplane representation of a neural radiance field for 3D-aware novel view synthesis via volume rendering. Our method is fast (24 fps) on consumer hardware, and produces higher quality results than strong GAN-inversion baselines that require test-time optimization. To train our triplane encoder pipeline, we use only synthetic data, showing how to distill the knowledge from a pretrained 3D GAN into a feedforward encoder. Technical contributions include a Vision Transformer-based triplane encoder, a camera data augmentation strategy, and a well-designed loss function for synthetic data training. We benchmark against the state-of-the-art methods, demonstrating significant improvements in robustness and image quality in challenging real-world settings. We showcase our results on portraits of faces (FFHQ) and cats (AFHQ), but our algorithm can also be applied in the future to other categories with a 3D-aware image generator.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
