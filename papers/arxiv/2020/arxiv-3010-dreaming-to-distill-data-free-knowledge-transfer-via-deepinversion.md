---
id: "arxiv-3010"
title: "Dreaming to Distill: Data-free Knowledge Transfer via DeepInversion"
conference: "arXiv 2020"
date: "2020-06"
authors:
  - name: "Hongxu Danny Yin"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Pavlo Molchanov"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jose M. Alvarez"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Zhizhong Li"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Arun Mallya"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Derek Hoiem"
    affiliation: "University of Illinois at Urbana-Champaign"
    is_industry: false
  - name: "Niraj K. Jha"
    affiliation: "Princeton University"
    is_industry: false
  - name: "Jan Kautz"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - Computer Vision
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Vision"
abstract: "We introduce DeepInversion, a new method for synthesizing images from the image distribution used to train a deep neural network. We “invert” a trained network (teacher) to synthesize class-conditional input images starting from random noise, without using any additional information on the training "
url: "https://research.nvidia.com/publication/2020-06_dreaming-distill-data-free-knowledge-transfer-deepinversion"
status: "new"
---

# Dreaming to Distill: Data-free Knowledge Transfer via DeepInversion

## 摘要

We introduce DeepInversion, a new method for synthesizing images from the image distribution used to train a deep neural network. We “invert” a trained network (teacher) to synthesize class-conditional input images starting from random noise, without using any additional information on the training dataset. Keeping the teacher fixed, our method optimizes the input while regularizing the distribution of intermediate feature maps using information stored in the batch normalization layers of the teacher. Further, we improve the diversity of synthesized images using Adaptive DeepInversion, which maximizes the Jensen-Shannon divergence between the teacher and student network logits. The resulting synthesized images from networks trained on the CIFAR-10 and ImageNet datasets demonstrate high fidelity and degree of realism, and help enable a new breed of data-free applications – ones that do not require any real images or labeled data. We demonstrate the applicability of our proposed method to three tasks of immense practical importance – (i) data-free network pruning, (ii) data-free knowledge transfer, and (iii) data-free continual learning. Code is available at https: //github.com/NVlabs/DeepInversion.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
