---
id: "cvpr-0036"
title: "Open-Vocabulary Panoptic Segmentation with Text-to-Image Diffusion Models"
conference: "CVPR 2023"
date: "2023-06"
authors:
  - name: "Jiarui Xu"
    affiliation: "University of California at San Diego"
    is_industry: false
  - name: "Sifei Liu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Arash Vahdat"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Wonmin Byeon"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Xiaolong Wang"
    affiliation: "University of California at San Diego"
    is_industry: false
  - name: "Shalini De Mello"
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
  - name: "Project Page"
    url: "https://jerryxu.net/ODISE/"
  - name: "Code"
    url: "https://github.com/NVlabs/ODISE"
  - name: "HuggingFace Demo"
    url: "https://huggingface.co/spaces/xvjiarui/ODISE"
  - name: "ArXiv"
    url: "https://arxiv.org/abs/2303.04803"
  - name: "Video"
    url: "https://www.youtube.com/watch?v=eW2vF8o_7p0"
abstract: "We present ODISE: Open-vocabulary DIffusion-based panoptic SEgmentation, which unifies pre-trained text-image diffusion and discriminative models to perform open-vocabulary panoptic segmentation. Text-to-image diffusion models have the remarkable ability to generate high-quality images with diverse "
url: "https://research.nvidia.com/publication/2023-06_open-vocabulary-panoptic-segmentation-text-image-diffusion-models"
status: "new"
---

# Open-Vocabulary Panoptic Segmentation with Text-to-Image Diffusion Models

## 摘要

We present ODISE: Open-vocabulary DIffusion-based panoptic SEgmentation, which unifies pre-trained text-image diffusion and discriminative models to perform open-vocabulary panoptic segmentation. Text-to-image diffusion models have the remarkable ability to generate high-quality images with diverse open-vocabulary language descriptions. This demonstrates that their internal representation space is highly correlated with open concepts in the real world. Text-image discriminative models like CLIP, on the other hand, are good at classifying images into open-vocabulary labels. We leverage the frozen internal representations of both these models to perform panoptic segmentation of any category in the wild. Our approach outperforms the previous state of the art by significant margins on both open-vocabulary panoptic and semantic segmentation tasks. In particular, with COCO training only, our method achieves 23.4 PQ and 30.0 mIoU on the ADE20K dataset, with 8.3 PQ and 7.9 mIoU absolute improvement over the previous state of the art. We open-source our code and models at https://github.com/NVlabs/ODISE.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
