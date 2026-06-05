---
id: arxiv-2757
title: "FreeSOLO: Learning to Segment Objects without Annotations"
conference: arXiv 2022
date: 2022-06
authors:
  - name: "Zhiding Yu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Shalini De Mello"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jan Kautz"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Xinlong Wang"
    affiliation: ""
    is_industry: false
  - name: "Anima Anandkumar"
    affiliation: ""
    is_industry: false
  - name: "Chunhua Shen"
    affiliation: ""
    is_industry: false
  - name: "Jose M. Alvarez"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Computer Vision
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Vision"
external_links:
  - name: "Code"
    url: "https://github.com/NVlabs/FreeSOLO"
  - name: "ArXiv"
    url: "https://arxiv.org/abs/2202.12181"
abstract: "Instance segmentation is a fundamental vision task that aims to recognize and segment each object in an image. However, it requires costly annotations such as bounding boxes and segmentation masks for learning. In this work, we propose a fully unsupervised learning method that learns class-agnostic "
url: "https://research.nvidia.com/publication/2022-06_freesolo-learning-segment-objects-without-annotations"
status: new
---

# FreeSOLO: Learning to Segment Objects without Annotations

## 摘要

Instance segmentation is a fundamental vision task that aims to recognize and segment each object in an image. However, it requires costly annotations such as bounding boxes and segmentation masks for learning. In this work, we propose a fully unsupervised learning method that learns class-agnostic instance segmentation without any annotations. We present FreeSOLO, a self-supervised instance segmentation framework built on top of the simple instance segmentation method SOLO. Our method also presents a novel localization-aware pre-training framework, where objects can be discovered from complicated scenes in an unsupervised manner. FreeSOLO achieves 9.8% AP50 on the challenging COCO dataset, which even outperforms several segmentation proposal methods that use manual annotations. For the first time, we demonstrate unsupervised class-agnostic instance segmentation successfully. FreeSOLO's box localization significantly outperforms state-of-the-art unsupervised object detection/discovery methods, with about 100% relative improvements in COCO AP. FreeSOLO further demonstrates superiority as a strong pre-training method, outperforming state-of-the-art self-supervised pre-training methods by +9.8% AP when fine-tuning instance segmentation with only 5% COCO masks.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
