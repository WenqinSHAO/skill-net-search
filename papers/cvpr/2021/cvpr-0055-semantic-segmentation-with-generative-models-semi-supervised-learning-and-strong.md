---
id: "cvpr-0055"
title: "Semantic Segmentation with Generative Models: Semi-Supervised Learning and Strong Out-of-Domain Generalization"
conference: "CVPR 2021"
date: "2021-06"
authors:
  - name: "Daiqing Li"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Junlin Yang"
    affiliation: "NVIDIA, Yale University"
    is_industry: true
  - name: "Karsten Kreis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Antonio Torralba"
    affiliation: "MIT"
    is_industry: false
  - name: "Sanja Fidler"
    affiliation: "NVIDIA, University of Toronto, Vector Institute"
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
    url: "https://research.nvidia.com/labs/toronto-ai/semanticGAN/"
abstract: "Training deep networks with limited labeled data while achieving a strong generalization ability is key in the quest to reduce human annotation efforts. This is the goal of semi-supervised learning, which exploits more widely available unlabeled data to complement small labeled data sets. In this pa"
url: "https://research.nvidia.com/publication/2021-06_semantic-segmentation-generative-models-semi-supervised-learning-and-strong-out"
status: "new"
---

# Semantic Segmentation with Generative Models: Semi-Supervised Learning and Strong Out-of-Domain Generalization

## 摘要

Training deep networks with limited labeled data while achieving a strong generalization ability is key in the quest to reduce human annotation efforts. This is the goal of semi-supervised learning, which exploits more widely available unlabeled data to complement small labeled data sets. In this paper, we propose a novel framework for discriminative pixel-level tasks using a generative model of both images and labels. Concretely, we learn a generative adversarial network that captures the joint image-label distribution and is trained efficiently using a large set of unlabeled images supplemented with only few labeled ones. We build our architecture on top of StyleGAN2, augmented with a label synthesis branch. Image labeling at test time is achieved by first embedding the target image into the joint latent space via an encoder network and test-time optimization, and then generating the label from the inferred embedding. We evaluate our approach in two important domains: medical image segmentation and part-based face segmentation. We demonstrate strong in-domain performance compared to several baselines, and are the first to showcase extreme out-of-domain generalization, such as transferring from CT to MRI in medical imaging, and photographs of real faces to paintings, sculptures, and even cartoons and animal faces. Project Page: https://research.nvidia.com/labs/toronto-ai/semanticGAN/

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
