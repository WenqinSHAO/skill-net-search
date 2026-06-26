---
id: "arxiv-2719"
title: "Augmenting Legacy Networks for Flexible Inference."
conference: "arXiv 2022"
date: "2022-10"
authors:
  - name: "Jason Clemons"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Iuri Frosio"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Maying Shen"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jose M. Alvarez"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Steve Keckler"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
abstract: "Abstract.&nbsp;Once deployed in the field, Deep Neural Networks (DNNs) run on devices with widely different compute capabilities and whose computational load varies over time. Dynamic network architectures are one of the existing techniques developed to handle the varying computational load in real-"
url: "https://research.nvidia.com/publication/2022-10_augmenting-legacy-networks-flexible-inference"
status: "new"
---

# Augmenting Legacy Networks for Flexible Inference.

## 摘要

Abstract.&nbsp;Once deployed in the field, Deep Neural Networks (DNNs) run on devices with widely different compute capabilities and whose computational load varies over time. Dynamic network architectures are one of the existing techniques developed to handle the varying computational load in real-time deployments. Here we introduce LeAF (Legacy Augmentation for Flexible inference), a novel paradigm to augment the key-phases of a pre-trained DNN with alternative, trainable, shallow phases that can be executed in place of the original ones. At run time, LeAF allows changing the network architecture without any computational overhead, to effectively handle different loads. LeAF-ResNet50 has a storage overhead of less than 14% with respect to the legacy DNN; its accuracy varies from the original accuracy of 76.1% to 64.8% while requiring 4 to 0.68 GFLOPs, in line with state-of-the-art results obtained with non-legacy and less flexible methods. We examine how LeAF’s dynamic routing strategy impacts the accuracy and the use of the available computational resources as a function of the compute capability and load of the device, with particular attention to the case of an unpredictable batch size. We show that the optimal configurations for a given network can indeed vary based on the system metrics (such as latency or FLOPs), batch size and compute capability of the machine.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
