---
id: arxiv-2508
title: "Nemotron-Labs-Diffusion: A Tri-Mode Language Model Unifying Autoregressive, Diffusion, and Self-Speculation Decoding"
conference: arXiv 2026
date: 2026-05
authors:
  - name: "Yonggan Fu"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Pavlo Molchanov"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Lexington Whalen"
    affiliation: ""
    is_industry: false
  - name: "Abhinav Garg"
    affiliation: ""
    is_industry: false
  - name: "Chengyue Wu"
    affiliation: ""
    is_industry: false
  - name: "Maksim Khadkevich"
    affiliation: ""
    is_industry: false
  - name: "Nicolai Oswald"
    affiliation: ""
    is_industry: false
  - name: "Enze Xie"
    affiliation: ""
    is_industry: false
  - name: "Daniel Egert"
    affiliation: ""
    is_industry: false
  - name: "Sharath Turuvekere Sreenivas"
    affiliation: ""
    is_industry: false
  - name: "Shizhe Diao"
    affiliation: ""
    is_industry: false
  - name: "Chenhan Yu"
    affiliation: ""
    is_industry: false
  - name: "Ye Yu"
    affiliation: ""
    is_industry: false
  - name: "Weijia Chen"
    affiliation: ""
    is_industry: false
  - name: "Sajad Norouzi"
    affiliation: ""
    is_industry: false
  - name: "Jingyu Liu"
    affiliation: ""
    is_industry: false
  - name: "Shiyi Lan"
    affiliation: ""
    is_industry: false
  - name: "Ligeng Zhu"
    affiliation: ""
    is_industry: false
  - name: "Jin Wang"
    affiliation: ""
    is_industry: false
  - name: "Jindong Jiang"
    affiliation: ""
    is_industry: false
  - name: "Morteza Mardani"
    affiliation: ""
    is_industry: false
  - name: "Mehran Maghoumi"
    affiliation: ""
    is_industry: false
  - name: "Song Han"
    affiliation: ""
    is_industry: false
  - name: "Ante Jukić"
    affiliation: ""
    is_industry: false
  - name: "Nima Tajbakhsh"
    affiliation: ""
    is_industry: false
  - name: "Jan Kautz"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Foundation_models
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Natural Language Processing"
external_links:
  - name: "HF collection"
    url: "https://huggingface.co/collections/nvidia/nemotron-labs-diffusion"
abstract: "We introduce Nemotron-Labs-Diffusion, a tri-mode language model (LM) that unifies AR, diffusion, and self-speculation decoding within a single architecture. Trained with a joint AR-diffusion objective, Nemotron-Labs-Diffusion can switch modes to sustain high throughput across deployment settings and"
url: "https://research.nvidia.com/publication/2026-05%5Fnemotron-labs-diffusion-tri-mode-language-model-unifying-autoregressive"
status: new
---

# Nemotron-Labs-Diffusion: A Tri-Mode Language Model Unifying Autoregressive, Diffusion, and Self-Speculation Decoding

## 摘要

We introduce Nemotron-Labs-Diffusion, a tri-mode language model (LM) that unifies AR, diffusion, and self-speculation decoding within a single architecture. Trained with a joint AR-diffusion objective, Nemotron-Labs-Diffusion can switch modes to sustain high throughput across deployment settings and concurrency levels. Our study shows that (1) AR and diffusion objectives are complementary: diffusion improves lookahead planning, while AR provides left-to-right linguistic priors. (2) In self-speculation mode, diffusion drafts while AR verifies, outperforming multi-token prediction (MTP) methods in both acceptance rate and real-device efficiency. (3) A speed-of-light analysis further demonstrates diffusion’s long-term potential, with up to 76.5% more tokens per forward pass than self-speculation under an optimal sampler. Scaling to 3B, 8B, and 14B parameters, our Nemotron-Labs-Diffusion family, including base, instruct, and vision-language models, consistently outperforms state-of-the-art open-source AR and diffusion LMs in both accuracy and speed. For example, Nemotron-Labs-Diffusion-8B decodes 5.9×more tokens per forward than Qwen3-8B with better accuracy, translating to 4× higher throughput on SPEED-Bench with SGLang on a GB200 GPU.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
