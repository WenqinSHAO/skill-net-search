---
id: "cvpr-0049"
title: "BigDatasetGAN: Synthesizing ImageNet with Pixel-wise Annotations"
conference: "CVPR 2022"
date: "2022-06"
authors:
  - name: "Daiqing Li"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Huan Ling"
    affiliation: "NVIDIA, University of Toronto, Vector Institute"
    is_industry: true
  - name: "Seung Wook Kim"
    affiliation: "NVIDIA, University of Toronto, Vector Institute"
    is_industry: true
  - name: "Karsten Kreis"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Adela Barriuso"
    affiliation: ""
    is_industry: false
  - name: "Sanja Fidler"
    affiliation: "NVIDIA, University of Toronto, Vector Institute"
    is_industry: true
  - name: "Antonio Torralba"
    affiliation: "MIT"
    is_industry: false
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
    url: "https://research.nvidia.com/labs/toronto-ai/big-datasetgan/"
abstract: "Annotating images with pixel-wise labels is a time-consuming and costly process. Recently, DatasetGAN showcased a promising alternative - to synthesize a large labeled dataset via a generative adversarial network (GAN) by exploiting a small set of manually labeled, GAN-generated images. Here, we sca"
url: "https://research.nvidia.com/publication/2022-06_bigdatasetgan-synthesizing-imagenet-pixel-wise-annotations"
status: "new"
---

# BigDatasetGAN: Synthesizing ImageNet with Pixel-wise Annotations

## 摘要

Annotating images with pixel-wise labels is a time-consuming and costly process. Recently, DatasetGAN showcased a promising alternative - to synthesize a large labeled dataset via a generative adversarial network (GAN) by exploiting a small set of manually labeled, GAN-generated images. Here, we scale DatasetGAN to ImageNet scale of class diversity. We take image samples from the class-conditional generative model BigGAN trained on ImageNet, and manually annotate 5 images per class, for all 1k classes. By training an effective feature segmentation architecture on top of BigGAN, we turn BigGAN into a labeled dataset generator. We further show that VQGAN can similarly serve as a dataset generator, leveraging the already annotated data. We create a new ImageNet benchmark by labeling an additional set of 8k real images and evaluate segmentation performance in a variety of settings. Through an extensive ablation study we show big gains in leveraging a large generated dataset to train different supervised and self-supervised backbone models on pixel-wise tasks. Furthermore, we demonstrate that using our synthesized datasets for pre-training leads to improvements over standard ImageNet pre-training on several downstream datasets, such as PASCAL-VOC, MS-COCO, Cityscapes and chest X-ray, as well as tasks (detection, segmentation). Our benchmark will be made public and maintain a leaderboard for this challenging task. Project Page: https://research.nvidia.com/labs/toronto-ai/big-datasetgan/

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
