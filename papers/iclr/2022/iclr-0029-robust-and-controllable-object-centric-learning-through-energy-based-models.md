---
id: "iclr-0029"
title: "Robust and Controllable Object-Centric Learning through Energy-based Models"
conference: "ICLR 2022"
date: "2022-10"
authors:
  - name: "Ruixiang Zhang"
    affiliation: "Stanford University"
    is_industry: false
  - name: "Tong Che"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Boris Ivanovic"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Renhao Wang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Marco Pavone"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yoshua Bengio"
    affiliation: "University of Montreal"
    is_industry: false
  - name: "Liam Paull"
    affiliation: "University of Montreal"
    is_industry: false
topics:
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Autonomous Vehicles"
abstract: "Humans are remarkably good at understanding and reasoning about complex visual scenes. The capability to decompose low-level observations into discrete objects allows us to build a grounded abstract representation and identify the compositional structure of the world. Accordingly, it is a crucial st"
url: "https://research.nvidia.com/publication/2022-10_robust-and-controllable-object-centric-learning-through-energy-based-models"
status: "new"
---

# Robust and Controllable Object-Centric Learning through Energy-based Models

## 摘要

Humans are remarkably good at understanding and reasoning about complex visual scenes. The capability to decompose low-level observations into discrete objects allows us to build a grounded abstract representation and identify the compositional structure of the world. Accordingly, it is a crucial step for machine learning models to be capable of inferring objects and their properties from visual scenes without explicit supervision. However, existing works on object-centric representation learning either rely on tailor-made neural network modules or strong probabilistic assumptions in the underlying generative and inference processes. In this work, we present \ours, a conceptually simple and general approach to learning object-centric representations through an energy-based model. By forming a permutation-invariant energy function using vanilla attention blocks readily available in Transformers, we can infer object-centric latent variables via gradient-based MCMC methods where permutation equivariance is automatically guaranteed. We show that \ours can be easily integrated into existing architectures and can effectively extract high-quality object-centric representations, leading to better segmentation accuracy and competitive downstream task performance. Further, empirical evaluations show that \ ours learned representations are robust against distribution shift. Finally, we demonstrate the effectiveness of \ours in systematic compositional generalization, by re-composing learned energy functions for novel scene generation and manipulation.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
