---
id: "arxiv-2820"
title: "NVIDIA NeMo Neural Machine Translation Systems for English-German and English-Russian News and Biomedical Tasks at WMT21"
conference: "arXiv 2021"
date: "2021-11"
authors:
  - name: "Sandeep Subramanian"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Oleksii Hrinchuk"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Virginia Adams"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Oleksii Kuchaiev"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - Foundation_models
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Machine Translation"
external_links:
  - name: "Paper"
    url: "https://arxiv.org/abs/2111.08634"
abstract: "This paper provides an overview of NVIDIA NeMo's neural machine translation systems for the constrained data track of the WMT21 News and Biomedical Shared Translation Tasks. Our news task submissions for English-German (En-De) and English-Russian (En-Ru) are built on top of a baseline transformer-ba"
url: "https://research.nvidia.com/publication/2021-11_nvidia-nemo-neural-machine-translation-systems-english-german-and-english"
status: "new"
---

# NVIDIA NeMo Neural Machine Translation Systems for English-German and English-Russian News and Biomedical Tasks at WMT21

## 摘要

This paper provides an overview of NVIDIA NeMo's neural machine translation systems for the constrained data track of the WMT21 News and Biomedical Shared Translation Tasks. Our news task submissions for English-German (En-De) and English-Russian (En-Ru) are built on top of a baseline transformer-based sequence-to-sequence model. Specifically, we use a combination of 1) checkpoint averaging 2) model scaling 3) data augmentation with backtranslation and knowledge distillation from right-to-left factorized models 4) finetuning on test sets from previous years 5) model ensembling 6) shallow fusion decoding with transformer language models and 7) noisy channel re-ranking. Additionally, our biomedical task submission for English-Russian uses a biomedically biased vocabulary and is trained from scratch on news task data, medically relevant text curated from the news task dataset, and biomedical data provided by the shared task. Our news system achieves a sacreBLEU score of 39.5 on the WMT'20 En-De test set outperforming the best submission from last year's task of 38.8. Our biomedical task Ru-En and En-Ru systems reach BLEU scores of 43.8 and 40.3 respectively on the WMT'20 Biomedical Task Test set, outperforming the previous year's best submissions.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
