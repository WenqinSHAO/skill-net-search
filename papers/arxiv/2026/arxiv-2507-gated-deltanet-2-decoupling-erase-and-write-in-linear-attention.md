---
id: arxiv-2507
title: "Gated DeltaNet-2: Decoupling Erase and Write in Linear Attention"
conference: arXiv 2026
date: 2026-05
authors:
  - name: "Ali Hatamizadeh"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jan Kautz"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yejin Choi"
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
  - name: "https://arxiv.org/abs/2605.22791"
    url: "https://arxiv.org/abs/2605.22791"
  - name: "https://github.com/NVlabs/GatedDeltaNet-2"
    url: "https://github.com/NVlabs/GatedDeltaNet-2"
abstract: "Linear attention replaces the unbounded cache of softmax attention with a fixed-size recurrent state, reducing sequence mixing to linear time and decoding to constant memory. The hard part is not just what to forget, but how to edit this compressed memory without scrambling existing associations. De"
url: "https://research.nvidia.com/publication/2026-05%5Fgated-deltanet-2-decoupling-erase-and-write-linear-attention"
status: new
---

# Gated DeltaNet-2: Decoupling Erase and Write in Linear Attention

## 摘要

Linear attention replaces the unbounded cache of softmax attention with a fixed-size recurrent state, reducing sequence mixing to linear time and decoding to constant memory. The hard part is not just what to forget, but how to edit this compressed memory without scrambling existing associations. Delta-rule models subtract the current read before writing a new value, and Kimi Delta Attention (KDA) sharpens forgetting with channel-wise decay. But the active edit still uses a single scalar gate to control two different things: how much old content to erase on the key side and how much new content to commit on the value side. We introduce Gated DeltaNet-2, which generalizes both Gated DeltaNet and KDA by inheriting adaptive forgetting and channel-wise decay while addressing their shared limitation, the scalar tie between erasing and writing. Gated Delta Rule-2 separates these roles with a channel-wise erase gate b_t and a channel-wise write gate w_t, reducing to KDA when both gates collapse to the same scalar and to Gated DeltaNet when the decay also collapses. We derive a fast-weight update view, a chunkwise WY algorithm with channel-wise decay absorbed into asymmetric erase factors, and a gate-aware backward pass that preserves efficient parallel training. At 1.3B parameters trained on 100B FineWeb-Edu tokens, Gated DeltaNet-2 achieves the strongest overall results among Mamba-2, Gated DeltaNet, KDA, and Mamba-3 variants across language modeling, commonsense reasoning, and retrieval. Its advantage is most pronounced on long-context RULER needle-in-a-haystack benchmarks, where it improves the evaluated multi-key retrieval setting and remains strong in both recurrent and hybrid settings.&nbsp;

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
