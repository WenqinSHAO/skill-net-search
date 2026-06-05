---
id: iclr-0008
title: "LongVILA: Scaling Long-Context Visual Language Models for Long Videos"
conference: ICLR 2025
date: 2025-04
authors:
  - name: "Yukang Chen"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Ligeng Zhu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Pavlo Molchanov"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jan Kautz"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yuke Zhu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Song Han"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Fuzhao Xue"
    affiliation: ""
    is_industry: false
  - name: "Dacheng Li"
    affiliation: ""
    is_industry: false
  - name: "Qinghao Hu"
    affiliation: ""
    is_industry: false
  - name: "Xiuyu Li"
    affiliation: ""
    is_industry: false
  - name: "Yunhao Fang"
    affiliation: ""
    is_industry: false
  - name: "Haotian Tang"
    affiliation: ""
    is_industry: false
  - name: "Shang Yang"
    affiliation: ""
    is_industry: false
  - name: "Zhijian Liu"
    affiliation: ""
    is_industry: false
  - name: "Ethan He"
    affiliation: ""
    is_industry: false
  - name: "Hongxu Yin"
    affiliation: ""
    is_industry: false
  - name: "Linxi Fan"
    affiliation: ""
    is_industry: false
  - name: "Yao Lu (Jason)"
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
  - name: "Code and models"
    url: "https://github.com/NVlabs/VILA/tree/main/longvila"
abstract: "Long-context capability is critical for multi-modal foundation models, especially for long video understanding. We introduce LongVILA, a full-stack solution for long-context visual-language models by co-designing the algorithm and system. For model training, we upgrade existing VLMs to support long "
url: "https://research.nvidia.com/publication/2025-04_longvila-scaling-long-context-visual-language-models-long-videos"
status: new
---

# LongVILA: Scaling Long-Context Visual Language Models for Long Videos

## 摘要

Long-context capability is critical for multi-modal foundation models, especially for long video understanding. We introduce LongVILA, a full-stack solution for long-context visual-language models by co-designing the algorithm and system. For model training, we upgrade existing VLMs to support long video understanding by incorporating two additional stages, i.e., long context extension and long video supervised fine-tuning. However, training on long video is computationally and memory intensive. We introduce the long-context Multi-Modal Sequence Parallelism (MM-SP) system that efficiently parallelizes long video training and inference, enabling 2M context length training on 256 GPUs without any gradient checkpointing. LongVILA efficiently extends the number of video frames of VILA from 8 to 2048, achieving 99.8% accuracy in 6,000-frame (more than 1 million tokens) video needle-in-a-haystack. LongVILA-7B demonstrates strong accuracy on 9 popular video benchmarks, e.g. 65.1% VideoMME with subtitle. Besides, MM-SP is 2.1x - 5.7x faster than ring style sequence parallelism and 1.1x - 1.4x faster than Megatron with a hybrid context and tensor parallelism. Moreover, it seamlessly integrates with Hugging Face Transformers.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
