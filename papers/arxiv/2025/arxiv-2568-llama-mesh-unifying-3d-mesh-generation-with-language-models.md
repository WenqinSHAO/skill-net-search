---
id: arxiv-2568
title: "LLaMA-Mesh: Unifying 3D Mesh Generation with Language Models"
conference: arXiv 2025
date: 2025-03
authors:
  - name: "Zhengyi Wang"
    affiliation: ""
    is_industry: false
  - name: "Jonathan Lorraine"
    affiliation: ""
    is_industry: false
  - name: "Yikai Wang"
    affiliation: ""
    is_industry: false
  - name: "Hang Su"
    affiliation: ""
    is_industry: false
  - name: "Jun Zhu"
    affiliation: ""
    is_industry: false
  - name: "Sanja Fidler"
    affiliation: ""
    is_industry: false
  - name: "Xiaohui Zeng"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Computer Vision
  - Foundation_models
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Vision"
  - "Generative AI"
external_links:
  - name: "Project Page"
    url: "https://research.nvidia.com/labs/toronto-ai/LLaMA-Mesh/"
  - name: "Interactive demo"
    url: "https://huggingface.co/spaces/Zhengyi/LLaMA-Mesh"
  - name: "One minute video"
    url: "https://youtu.be/dkH10s0ultY"
  - name: "Model weights"
    url: "https://huggingface.co/Zhengyi/LLaMA-Mesh"
  - name: "Model Code"
    url: "https://github.com/nv-tlabs/LLaMa-Mesh"
abstract: "This work explores expanding the capabilities of large language models (LLMs) pretrained on text to generate 3D meshes within a unified model. This offers key advantages of (1) leveraging spatial knowledge already embedded in LLMs, derived from textual sources like 3D tutorials, and (2) enabling con"
url: "https://research.nvidia.com/publication/2025-03_llama-mesh-unifying-3d-mesh-generation-language-models"
status: new
---

# LLaMA-Mesh: Unifying 3D Mesh Generation with Language Models

## 摘要

This work explores expanding the capabilities of large language models (LLMs) pretrained on text to generate 3D meshes within a unified model. This offers key advantages of (1) leveraging spatial knowledge already embedded in LLMs, derived from textual sources like 3D tutorials, and (2) enabling conversational 3D generation and mesh understanding. A primary challenge is effectively tokenizing 3D mesh data into discrete tokens that LLMs can process seamlessly. To address this, we introduce LLaMA-Mesh, a novel approach that represents the vertex coordinates and face definitions of 3D meshes as plain text, allowing direct integration with LLMs without expanding the vocabulary. We construct a supervised fine-tuning (SFT) dataset enabling pretrained LLMs to (1) generate 3D meshes from text prompts, (2) produce interleaved text and 3D mesh outputs as required, and (3) understand and interpret 3D meshes. Our work is the first to demonstrate that LLMs can be fine-tuned to acquire complex spatial knowledge for 3D mesh generation in a text-based format, effectively unifying the 3D and text modalities. LLaMA-Mesh achieves mesh generation quality on par with models trained from scratch while maintaining strong text generation performance.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
