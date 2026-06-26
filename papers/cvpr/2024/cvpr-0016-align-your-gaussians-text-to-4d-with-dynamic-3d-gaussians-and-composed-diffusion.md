---
id: "cvpr-0016"
title: "Align Your Gaussians: Text-to-4D with Dynamic 3D Gaussians and Composed Diffusion Models"
conference: "CVPR 2024"
date: "2024-06"
authors:
  - name: "Huan Ling"
    affiliation: "NVIDIA, Vector Institute, University of Toronto"
    is_industry: true
  - name: "Seung Wook Kim"
    affiliation: "NVIDIA, Vector Institute, University of Toronto"
    is_industry: true
  - name: "Antonio Torralba"
    affiliation: "MIT"
    is_industry: false
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
    url: "https://research.nvidia.com/labs/toronto-ai/AlignYourGaussians/"
abstract: "Text-guided diffusion models have revolutionized image and video generation and have also been successfully used for optimization-based 3D object synthesis. Here, we instead focus on the underexplored text-to-4D setting and synthesize dynamic, animated 3D objects using score distillation methods wit"
url: "https://research.nvidia.com/publication/2024-06_align-your-gaussians-text-4d-dynamic-3d-gaussians-and-composed-diffusion-models"
status: "new"
---

# Align Your Gaussians: Text-to-4D with Dynamic 3D Gaussians and Composed Diffusion Models

## 摘要

Text-guided diffusion models have revolutionized image and video generation and have also been successfully used for optimization-based 3D object synthesis. Here, we instead focus on the underexplored text-to-4D setting and synthesize dynamic, animated 3D objects using score distillation methods with an additional temporal dimension. Compared to previous work, we pursue a novel compositional generation-based approach, and combine text-to-image, text-to-video, and 3D-aware multiview diffusion models to provide feedback during 4D object optimization, thereby simultaneously enforcing temporal consistency, high-quality visual appearance and realistic geometry. Our method, called Align Your Gaussians (AYG), leverages dynamic 3D Gaussian Splatting with deformation fields as 4D representation. Crucial to AYG is a novel method to regularize the distribution of the moving 3D Gaussians and thereby stabilize the optimization and induce motion. We also propose a motion amplification mechanism as well as a new autoregressive synthesis scheme to generate and combine multiple 4D sequences for longer generation. These techniques allow us to synthesize vivid dynamic scenes, outperform previous work qualitatively and quantitatively and achieve state-of-the-art text-to-4D performance. Due to the Gaussian 4D representation, different 4D animations can be seamlessly combined, as we demonstrate. AYG opens up promising avenues for animation, simulation and digital content creation as well as synthetic data generation.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
