---
id: siggraph-0005
title: "GAIA: Generative Animatable Interactive Avatars with Expression-conditioned Gaussians"
conference: SIGGRAPH 2025
date: 2025-08
authors:
  - name: "Tianye Li"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Omer Shapira"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Seonwook Park"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Michael Stengel"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Koki Nagano"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Shalini De Mello"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Zhengming Yu"
    affiliation: ""
    is_industry: false
  - name: "Jingxiang Sun"
    affiliation: ""
    is_industry: false
  - name: "Matthew Chan"
    affiliation: ""
    is_industry: false
  - name: "Xin Li"
    affiliation: ""
    is_industry: false
  - name: "Wenping Wang"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Foundation_models
  - Graphics_rendering
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
  - "Generative AI"
  - "VR, AR and Display Technology"
external_links:
  - name: "Project Page"
    url: "https://research.nvidia.com/labs/amri/projects/gaia/"
  - name: "Video"
    url: "https://research.nvidia.com/labs/amri/projects/gaia/media/videos/sig25_gaia_video.mp4"
abstract: "3D generative models of faces trained on in-the-wild image collections have improved greatly in recent times, offering better visual fidelity and view consistency. Making such generative models animatable is a hard yet rewarding task, with applications in virtual AI agents, character animation, and "
url: "https://research.nvidia.com/publication/2025-08_gaia-generative-animatable-interactive-avatars-expression-conditioned-gaussians"
status: new
---

# GAIA: Generative Animatable Interactive Avatars with Expression-conditioned Gaussians

## 摘要

3D generative models of faces trained on in-the-wild image collections have improved greatly in recent times, offering better visual fidelity and view consistency. Making such generative models animatable is a hard yet rewarding task, with applications in virtual AI agents, character animation, and telepresence. However, it is not trivial to learn a well-behaved animation model with the generative setting, as the learned latent space aims to best capture the data distribution, often omitting details such as dynamic appearance and entangling animation with other factors that affect controllability. We present GAIA: Generative Animatable Interactive Avatars, which is able to generate high-fidelity 3D head avatars for both realistic animation and rendering. To achieve consistency during animation, we learn to generate Gaussians embedded in an underlying morphable model for human heads via a shared UV parameterization. For modeling realistic animation, we further design the generator to learn expression-conditioned details for both geometric deformation and dynamic appearance. Finally, facing an inevitable entanglement problem between facial identity and expression, we propose a novel two-branch architecture that encourages the generator to disentangle identity and expression. On existing benchmarks, GAIA achieves state-of-the-art performance in visual quality as well as realistic animation. The generated Gaussian-based avatar supports highly efficient animation and rendering, making it readily available for interactive animation and appearance editing.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
