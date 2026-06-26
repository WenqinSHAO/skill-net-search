---
id: "arxiv-2775"
title: "NVIDIA NeMo Offline Speech Translation Systems for IWSLT 2022"
conference: "arXiv 2022"
date: "2022-05"
authors:
  - name: "Oleksii Hrinchuk"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Vahid Noroozi"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Abhinav Khattar"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Anton Peganov"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Sandeep Subramanian"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Somshubra Majumdar"
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
    url: "https://aclanthology.org/2022.iwslt-1.18.pdf"
abstract: "This paper provides an overview of NVIDIA NeMo’s speech translation systems for the IWSLT 2022 Offline Speech Translation Task. Our cascade system consists of 1) Conformer RNN-T automatic speech recognition model, 2) punctuation-capitalization model based on pre-trained T5 encoder, 3) ensemble of Tr"
url: "https://research.nvidia.com/publication/2022-05_nvidia-nemo-offline-speech-translation-systems-iwslt-2022"
status: "new"
---

# NVIDIA NeMo Offline Speech Translation Systems for IWSLT 2022

## 摘要

This paper provides an overview of NVIDIA NeMo’s speech translation systems for the IWSLT 2022 Offline Speech Translation Task. Our cascade system consists of 1) Conformer RNN-T automatic speech recognition model, 2) punctuation-capitalization model based on pre-trained T5 encoder, 3) ensemble of Transformer neural machine translation models fine-tuned on TED talks. Our end-to-end model has less parameters and consists of Conformer encoder and Transformer decoder. It relies on the cascade system by re-using its pre-trained ASR encoder and training on synthetic translations generated with the ensemble of NMT models. Our En-&gt;De cascade and end-to-end systems achieve 29.7 and 26.2 BLEU on the 2020 test set correspondingly, both outperforming the previous year’s best of 26 BLEU.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
