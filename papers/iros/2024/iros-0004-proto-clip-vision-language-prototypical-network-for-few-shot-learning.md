---
id: "iros-0004"
title: "Proto-CLIP: Vision-Language Prototypical Network for Few-Shot Learning"
conference: "IROS 2024"
date: "2024-10"
authors:
  - name: "Jishnu Jaykumar P"
    affiliation: "The University of Texas at Dallas"
    is_industry: false
  - name: "Kamalesh Palanisamy"
    affiliation: "The University of Texas at Dallas"
    is_industry: false
  - name: "Yu-Wei Chao"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Xinya Du"
    affiliation: "The University of Texas at Dallas"
    is_industry: false
  - name: "Yu Xiang"
    affiliation: "The University of Texas at Dallas"
    is_industry: false
topics:
  - Computer Vision
  - Robotics_autonomous
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Vision"
  - "Robotics"
external_links:
  - name: "Project Site"
    url: "https://irvlutd.github.io/Proto-CLIP"
abstract: "We propose a novel framework for few-shot learning by leveraging large-scale vision-language models such as CLIP. Motivated by unimodal prototypical networks for few-shot learning, we introduce Proto-CLIP which utilizes image prototypes and text prototypes for few-shot learning. Specifically, Proto-"
url: "https://research.nvidia.com/publication/2024-10_proto-clip-vision-language-prototypical-network-few-shot-learning"
status: "new"
---

# Proto-CLIP: Vision-Language Prototypical Network for Few-Shot Learning

## 摘要

We propose a novel framework for few-shot learning by leveraging large-scale vision-language models such as CLIP. Motivated by unimodal prototypical networks for few-shot learning, we introduce Proto-CLIP which utilizes image prototypes and text prototypes for few-shot learning. Specifically, Proto-CLIP adapts the image and text encoder embeddings from CLIP in a joint fashion using few-shot examples. The embeddings from the two encoders are used to compute the respective prototypes of image classes for classification. During adaptation, we propose aligning the image and text prototypes of the corresponding classes. Such alignment is beneficial for few-shot classification due to the reinforced contributions from both types of prototypes. Proto-CLIP has both training-free and fine-tuned variants. We demonstrate the effectiveness of our method by conducting experiments on benchmark datasets for few-shot learning, as well as in the real world for robot perception. The project page can be found at https://irvlutd.github.io/Proto-CLIP.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
