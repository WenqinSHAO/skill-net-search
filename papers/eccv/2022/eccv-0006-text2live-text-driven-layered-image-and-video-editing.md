---
id: "eccv-0006"
title: "Text2LIVE: Text-Driven Layered Image and Video Editing"
conference: "ECCV 2022"
date: "2022-10"
authors:
  - name: "Omer Bar-Tal"
    affiliation: "Weizmann Institute of Science"
    is_industry: false
  - name: "Dolev Ofri-Amar"
    affiliation: "Weizmann Institute of Science"
    is_industry: false
  - name: "Rafail Fridman"
    affiliation: "Weizmann Institute of Science"
    is_industry: false
  - name: "Yoni Kasten"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Tali Dekel"
    affiliation: "Weizmann Institute of Science"
    is_industry: false
topics:
  - Computer Vision
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Vision"
external_links:
  - name: "Project Page"
    url: "https://text2live.github.io/"
abstract: "We present a method for zero-shot, text-driven appearance manipulation in natural images and videos. Specifically, given an input image or video and a target text prompt, our goal is to edit the appearance of existing objects (e.g., object's texture) or augment the scene with new visual effects (e.g"
url: "https://research.nvidia.com/publication/2022-10_text2live-text-driven-layered-image-and-video-editing"
status: "new"
---

# Text2LIVE: Text-Driven Layered Image and Video Editing

## 摘要

We present a method for zero-shot, text-driven appearance manipulation in natural images and videos. Specifically, given an input image or video and a target text prompt, our goal is to edit the appearance of existing objects (e.g., object's texture) or augment the scene with new visual effects (e.g., smoke, fire) in a semantically meaningful manner. Our framework trains a generator using an&nbsp;internal dataset&nbsp;of training examples, extracted from a single input (image or video and target text prompt), while leveraging an&nbsp;external&nbsp;pre-trained CLIP model to establish our losses. Rather than directly generating the edited output, our key idea is to generate an&nbsp;edit layer&nbsp;(color+opacity) that is composited over the original input. This allows us to constrain the generation process and maintain high fidelity to the original input via novel text-driven losses that are applied directly to the edit layer. Our method neither relies on a pre-trained generator nor requires user-provided edit masks. Thus, it can perform localized, semantic edits on high-resolution natural images and videos across a variety of objects and scenes. &nbsp;

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
