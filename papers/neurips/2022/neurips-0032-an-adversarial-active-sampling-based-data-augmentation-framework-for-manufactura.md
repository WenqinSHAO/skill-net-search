---
id: "neurips-0032"
title: "An Adversarial Active Sampling-based Data Augmentation Framework for Manufacturable Chip Design"
conference: "NeurIPS 2022"
date: "2022-12"
authors:
  - name: "Mingjie Liu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Haoyu Yang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Zongyi Li"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Kumara Sastry"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Saumyadip Mukhopadhyay"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Selim Dogru"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Anima Anandkumar"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "David Z. Pan"
    affiliation: "University of Texas at Austin"
    is_industry: false
  - name: "Brucek Khailany"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Mark Haoxing Ren"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - GPU_architecture
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Circuits and VLSI Design"
external_links:
  - name: "arXiv"
    url: "https://arxiv.org/abs/2210.15765"
abstract: "Lithography modeling is a crucial problem in chip design to ensure a chip design mask is manufacturable. It requires rigorous simulations of optical and chemical models that are computationally expensive. Recent developments in machine learning have provided alternative solutions in replacing the ti"
url: "https://research.nvidia.com/publication/2022-12_adversarial-active-sampling-based-data-augmentation-framework-manufacturable"
status: "new"
---

# An Adversarial Active Sampling-based Data Augmentation Framework for Manufacturable Chip Design

## 摘要

Lithography modeling is a crucial problem in chip design to ensure a chip design mask is manufacturable. It requires rigorous simulations of optical and chemical models that are computationally expensive. Recent developments in machine learning have provided alternative solutions in replacing the time-consuming lithography simulations with deep neural networks. However, the considerable accuracy drop still impedes its industrial adoption. Most importantly, the quality and quantity of the training dataset directly affect the model performance. To tackle this problem, we propose a litho-aware data augmentation (LADA) framework to resolve the dilemma of limited data and improve the machine learning model performance. First, we pretrain the neural networks for lithography modeling and a gradient-friendly StyleGAN2 generator. We then perform adversarial active sampling to generate informative and synthetic in-distribution mask designs. These synthetic mask images will augment the original limited training dataset used to finetune the lithography model for improved performance. Experimental results demonstrate that LADA can successfully exploits the neural network capacity by narrowing down the performance gap between the training and testing data instances. &nbsp;

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
