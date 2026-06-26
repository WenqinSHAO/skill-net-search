---
id: "iclr-0027"
title: "GPViT: A High Resolution Non-Hierarchical Vision Transformer with Group Propagation"
conference: "ICLR 2023"
date: "2023-05"
authors:
  - name: "Chenhongyi Yang"
    affiliation: "University of Edinburgh"
    is_industry: false
  - name: "Jiarui Xu"
    affiliation: "University of California at San Diego"
    is_industry: false
  - name: "Shalini De Mello"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Elliot J. Crowley"
    affiliation: "University of Edinburgh"
    is_industry: false
  - name: "Xiaolong Wang"
    affiliation: "University of California at San Diego"
    is_industry: false
topics:
  - AI & Machine Learning
  - Computer Vision
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Vision"
external_links:
  - name: "Code"
    url: "https://github.com/ChenhongyiYang/GPViT"
  - name: "ArXiv"
    url: "https://arxiv.org/abs/2212.06795"
abstract: "We present the Group Propagation Vision Transformer (GPViT): a novel non- hierarchical (i.e. non-pyramidal) transformer model designed for general visual recognition with high-resolution features. High-resolution features (or tokens) are a natural fit for tasks that involve perceiving fine-grained d"
url: "https://research.nvidia.com/publication/2023-05_gpvit-high-resolution-non-hierarchical-vision-transformer-group-propagation"
status: "new"
---

# GPViT: A High Resolution Non-Hierarchical Vision Transformer with Group Propagation

## 摘要

We present the Group Propagation Vision Transformer (GPViT): a novel non- hierarchical (i.e. non-pyramidal) transformer model designed for general visual recognition with high-resolution features. High-resolution features (or tokens) are a natural fit for tasks that involve perceiving fine-grained details such as detection and segmentation, but exchanging global information between these features is expensive in memory and computation because of the way self-attention scales. We provide a highly efficient alternative Group Propagation Block (GP Block) to exchange global information. In each GP Block, features are first grouped to- gether by a fixed number of learnable group tokens; we then perform Group Propagation where global information is exchanged between the grouped fea- tures; finally, global information in the updated grouped features is returned back to the image features through a transformer decoder. We evaluate GPViT on a variety of visual recognition tasks including image classification, semantic seg- mentation, object detection, and instance segmentation. Our method achieves significant performance gains over previous works across all tasks, especially on tasks that require high-resolution outputs, for example, our GPViT-L3 out- performs Swin Transformer-B by 2.0 mIoU on ADE20K semantic segmentation with only half as many parameters. Code and pre-trained models are available at https://github.com/ChenhongyiYang/GPViT.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
