---
id: arxiv-2597
title: "GenTranslate: Large Language Models are Generative Multilingual Speech and Machine Translators"
conference: arXiv 2024
date: 2024-08
authors:
  - name: "Huck Yang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Yuchen Hu"
    affiliation: ""
    is_industry: false
  - name: "Chen Chen"
    affiliation: ""
    is_industry: false
  - name: "Ruizhe Li"
    affiliation: ""
    is_industry: false
  - name: "Zhehuai Chen"
    affiliation: ""
    is_industry: false
  - name: "Eng Siong Chng"
    affiliation: ""
    is_industry: false
topics:
  - AI & Machine Learning
  - Applied_perception
  - Foundation_models
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Applied Perception"
  - "Artificial Intelligence and Machine Learning"
  - "Generative AI"
  - "Machine Translation"
  - "Natural Language Processing"
  - "Speech Processing"
abstract: "Recent advances in large language models (LLMs) have stepped forward the development of multilingual speech and machine translation by its reduced representation errors and incorporated external knowledge. However, both translation tasks typically utilize beam search decoding and top-1 hypothesis se"
url: "https://research.nvidia.com/publication/2024-08_gentranslate-large-language-models-are-generative-multilingual-speech-and"
status: new
---

# GenTranslate: Large Language Models are Generative Multilingual Speech and Machine Translators

## 摘要

Recent advances in large language models (LLMs) have stepped forward the development of multilingual speech and machine translation by its reduced representation errors and incorporated external knowledge. However, both translation tasks typically utilize beam search decoding and top-1 hypothesis selection for inference. These techniques struggle to fully exploit the rich information in the diverse N-best hypotheses, making them less optimal for translation tasks that require a single, high-quality output sequence. In this paper, we propose a new generative paradigm for translation tasks, namely "GenTranslate", which builds upon LLMs to generate better results from the diverse translation versions in N-best list. Leveraging the rich linguistic knowledge and strong reasoning abilities of LLMs, our new paradigm can integrate the rich information in N-best candidates to generate a higher-quality translation result. Furthermore, to support LLM finetuning, we build and release a HypoTranslate dataset that contains over 592K hypotheses-translation pairs in 11 languages. Experiments on various speech and machine translation benchmarks (e.g., FLEURS, CoVoST-2, WMT) demonstrate that our GenTranslate significantly outperforms the state-of-the-art model.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
