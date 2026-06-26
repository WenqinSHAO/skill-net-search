---
id: "arxiv-2571"
title: "CorrFill: Enhancing Faithfulness in Reference-based Inpainting with Correspondence Guidance in Diffusion Models"
conference: "arXiv 2025"
date: "2025-02"
authors:
  - name: "Kuan-Hung Liu"
    affiliation: "National Yang Ming Chiao Tung University"
    is_industry: false
  - name: "Cheng-Kun Yang"
    affiliation: "National Taiwan University"
    is_industry: false
  - name: "Min-Hung Chen"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yu-Lun Liu"
    affiliation: "National Yang Ming Chiao Tung University"
    is_industry: false
  - name: "Yen-Yu Lin"
    affiliation: "National Yang Ming Chiao Tung University"
    is_industry: false
topics:
  - AI & Machine Learning
  - Applied_perception
  - Computer Vision
  - Foundation_models
  - Graphics_rendering
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Applied Perception"
  - "Artificial Intelligence and Machine Learning"
  - "Computer Graphics"
  - "Computer Vision"
  - "Generative AI"
external_links:
  - name: "arXiv"
    url: "https://arxiv.org/abs/2501.02355"
  - name: "Code"
    url: "https://github.com/khliu0000/CorrFill"
  - name: "Project page"
    url: "https://corrfill.github.io/"
abstract: "In the task of reference-based image inpainting, an additional reference image is provided to restore a damaged target image to its original state. The advancement of diffusion models, particularly Stable Diffusion, allows for simple formulations in this task. However, existing diffusion-based metho"
url: "https://research.nvidia.com/publication/2025-02_corrfill-enhancing-faithfulness-reference-based-inpainting-correspondence"
status: "new"
---

# CorrFill: Enhancing Faithfulness in Reference-based Inpainting with Correspondence Guidance in Diffusion Models

## 摘要

In the task of reference-based image inpainting, an additional reference image is provided to restore a damaged target image to its original state. The advancement of diffusion models, particularly Stable Diffusion, allows for simple formulations in this task. However, existing diffusion-based methods often lack explicit constraints on the correlation between the reference and damaged images, resulting in lower faithfulness to the reference images in the inpainting results. In this work, we propose CorrFill, a training-free module designed to enhance the awareness of geometric correlations between the reference and target images. This enhancement is achieved by guiding the inpainting process with correspondence constraints estimated during inpainting, utilizing attention masking in self-attention layers and an objective function to update the input tensor according to the constraints. Experimental results demonstrate that CorrFill significantly enhances the performance of multiple baseline diffusion-based methods, including state-of-the-art approaches, by emphasizing faithfulness to the reference images.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
