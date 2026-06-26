---
id: "ispd-0003"
title: "DREAM-GAN: Advancing DREAMPlace towards Commercial-Quality using Generative Adversarial Learning"
conference: "ISPD 2023"
date: "2023-03"
authors:
  - name: "Yi-Chen Lu"
    affiliation: "Georgia Institute of Technology"
    is_industry: false
  - name: "Haoxing"
    affiliation: "Mark) Ren (NVIDIA"
    is_industry: true
  - name: "Hao-Hsiang Hsiao"
    affiliation: "Georgia Institute of Technology"
    is_industry: false
  - name: "Sung Kyu Lim"
    affiliation: "Georgia Institute of Technology"
    is_industry: false
topics:
  - AI & Machine Learning
  - GPU_architecture
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Circuits and VLSI Design"
abstract: "DREAMPlace is a renowned open-source placer that provides GPUacceleratable infrastructure for placements of Very-Large-ScaleIntegration (VLSI) circuits. However, due to its limited focus on wirelength and density, existing placement solutions of DREAMPlace are not applicable to industrial design flo"
url: "https://research.nvidia.com/publication/2023-03_dream-gan-advancing-dreamplace-towards-commercial-quality-using-generative"
status: "new"
---

# DREAM-GAN: Advancing DREAMPlace towards Commercial-Quality using Generative Adversarial Learning

## 摘要

DREAMPlace is a renowned open-source placer that provides GPUacceleratable infrastructure for placements of Very-Large-ScaleIntegration (VLSI) circuits. However, due to its limited focus on wirelength and density, existing placement solutions of DREAMPlace are not applicable to industrial design flows. To improve DREAMPlace towards commercial-quality without knowing the black-boxed algorithms of the tools, in this paper, we present DREAM-GAN, a placement optimization framework that advances DREAMPlace using generative adversarial learning. At each placement iteration, aside from optimizing the wirelength and density objectives of the vanilla DREAMPlace, DREAM-GAN computes and optimizes a differentiable loss that denotes the similarity score between the underlying placement and the tool-generated placements in commercial databases. Experimental results on 5 commercial and OpenCore designs using an industrial design flow implemented by Synopsys ICC2 not only demonstrate that DREAM-GAN significantly improves the vanilla DREAMPlace at the placement stage across each benchmark, but also show that the improvements last firmly to the post-route stage, where we observe improvements by up to 8.3% in wirelength and 7.4% in total power

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
