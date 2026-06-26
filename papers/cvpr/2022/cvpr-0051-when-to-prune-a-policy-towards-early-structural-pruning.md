---
id: "cvpr-0051"
title: "When to Prune? A Policy towards Early Structural Pruning"
conference: "CVPR 2022"
date: "2022-05"
authors:
  - name: "Maying Shen"
    affiliation: ""
    is_industry: false
  - name: "Pavlo Molchanov"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Hongxu Danny Yin"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jose M. Alvarez"
    affiliation: ""
    is_industry: false
topics:
  - Computer Vision
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Computer Vision"
abstract: "Pruning enables appealing reductions in network memory footprint and time complexity. Conventional post training pruning techniques lean towards efficient inference while overlooking the heavy computation for training. Recent exploration of pre-training pruning at initialization hints on training co"
url: "https://research.nvidia.com/publication/2022-05_when-prune-policy-towards-early-structural-pruning"
status: "new"
---

# When to Prune? A Policy towards Early Structural Pruning

## 摘要

Pruning enables appealing reductions in network memory footprint and time complexity. Conventional post training pruning techniques lean towards efficient inference while overlooking the heavy computation for training. Recent exploration of pre-training pruning at initialization hints on training cost reduction via pruning, but suffers noticeable performance degradation. We attempt to combine the benefits of both directions and propose a policy that prunes as early as possible during training without hurting performance. Instead of pruning at initialization, our method exploits initial dense training for few epochs to quickly guide the architecture, while constantly evaluating dominant sub-networks via neuron importance ranking. This unveils dominant sub-networks whose structures turn stable, allowing conventional pruning to be pushed earlier into the training. To do this early, we further introduce an Early Pruning Indicator (EPI) that relies on sub-network architectural similarity and quickly triggers pruning when the sub-network’s architecture stabilizes. Through extensive experiments on ImageNet, we show that EPI empowers a quick tracking of early training epochs suitable for pruning, offering same efficacy as an otherwise “oracle” grid-search that scans through epochs and requires orders of magnitude more compute. Our method yields 1.4% top-1 accuracy boost over state-of-the-art pruning counterparts, cuts down training cost on GPU by 2.4×, hence offers a new efficiency-accuracy boundary for network pruning during training.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
