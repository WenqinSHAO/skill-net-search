---
id: iclr-0006
title: "Fugatto 1 - Foundational Generative Audio Transformer Opus 1"
conference: ICLR 2025
date: 2025-04
authors:
  - name: "Siddharth Gururani"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Huck Yang"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Rafael Valle"
    affiliation: ""
    is_industry: false
  - name: "Rohan Badlani"
    affiliation: ""
    is_industry: false
  - name: "Zhifeng Kong"
    affiliation: ""
    is_industry: false
  - name: "Sang-gil Lee"
    affiliation: ""
    is_industry: false
  - name: "Arushi Goel"
    affiliation: ""
    is_industry: false
  - name: "Sungwon Kim"
    affiliation: ""
    is_industry: false
  - name: "Joao Felipe Santos"
    affiliation: ""
    is_industry: false
  - name: "Shuqi Dai"
    affiliation: ""
    is_industry: false
  - name: "Aya AIJa'fari"
    affiliation: ""
    is_industry: false
  - name: "Alex Liu"
    affiliation: ""
    is_industry: false
  - name: "Kevin Shih"
    affiliation: ""
    is_industry: false
  - name: "Wei Ping"
    affiliation: ""
    is_industry: false
  - name: "Bryan Catanzaro"
    affiliation: ""
    is_industry: false
topics:
  - Foundation_models
  - AI & Machine Learning
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Generative AI"
  - "Natural Language Processing"
external_links:
  - name: "Demo Website"
    url: "https://fugatto.github.io/"
abstract: "Fugatto is a versatile audio synthesis and transformation model capable of followingfree-form text instructions with optional audio inputs. While large languagemodels (LLMs) trained with text on a simple next-token prediction objective canlearn to infer instructions directly from the data, models tr"
url: "https://research.nvidia.com/publication/2025-04_fugatto-1-foundational-generative-audio-transformer-opus-1"
status: new
---

# Fugatto 1 - Foundational Generative Audio Transformer Opus 1

## 摘要

Fugatto is a versatile audio synthesis and transformation model capable of followingfree-form text instructions with optional audio inputs. While large languagemodels (LLMs) trained with text on a simple next-token prediction objective canlearn to infer instructions directly from the data, models trained solely on audiodata lack this capacity. This is because audio data does not inherently contain theinstructions that were used to generate it. To overcome this challenge, we introducea specialized dataset generation approach optimized for producing a wide range ofaudio generation and transformation tasks, ensuring the data reveals meaningfulrelationships between audio and language. Another challenge lies in achievingcompositional abilities – such as combining, interpolating between, or negatinginstructions – using data alone. To address it, we propose ComposableART, aninference-time technique that extends classifier-free guidance to compositionalguidance. It enables the seamless and flexible composition of instructions, leadingto highly customizable audio outputs outside the training distribution. Our evaluationsacross a diverse set of tasks demonstrate that Fugatto performs competitivelywith specialized models, while ComposableART enhances its sonic palette andcontrol over synthesis. Most notably, we highlight our framework’s ability tosynthesize emergent sounds – sonic phenomena that transcend conventional audiogeneration – unlocking new creative possibilities. Demo Website.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
