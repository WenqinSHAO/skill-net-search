---
id: "cvpr-0042"
title: "The Best Defense is a Good Offense: Adversarial Augmentation against Adversarial Attacks"
conference: "CVPR 2023"
date: "2023-05"
authors:
  - name: "Iuri Frosio"
    affiliation: "NVIDIA"
    is_industry: true
  - name: "Jan Kautz"
    affiliation: "NVIDIA"
    is_industry: true
topics:
  - AI & Machine Learning
  - Computer Vision
tags:
  - nvidia-research
arxiv: ""
research_areas:
  - "Artificial Intelligence and Machine Learning"
  - "Computer Vision"
external_links:
  - name: "CVPR official paper"
    url: "https://openaccess.thecvf.com/content/CVPR2023/html/Frosio_The_Best_Defense_Is_a_Good_Offense_Adversarial_Augmentation_Against_CVPR_2023_paper.html"
  - name: "Code repo"
    url: "https://github.com/NVlabs/A5"
  - name: "Arxiv paper"
    url: "https://arxiv.org/abs/2305.14188"
abstract: "Many defenses against adversarial attacks (\\eg robust classifiers, randomization, or image purification) use countermeasures put to work only after the attack has been crafted. We adopt a different perspective to introduce A5 (Adversarial Augmentation Against Adversarial Attacks), a novel framework "
url: "https://research.nvidia.com/publication/2023-05_best-defense-good-offense-adversarial-augmentation-against-adversarial-attacks"
status: "new"
---

# The Best Defense is a Good Offense: Adversarial Augmentation against Adversarial Attacks

## 摘要

Many defenses against adversarial attacks (\eg robust classifiers, randomization, or image purification) use countermeasures put to work only after the attack has been crafted. We adopt a different perspective to introduce A5 (Adversarial Augmentation Against Adversarial Attacks), a novel framework including the first certified preemptive defense against adversarial attacks. The main idea is to craft a defensive perturbation to guarantee that any attack (up to a given magnitude) towards the input in hand will fail. To this aim, we leverage existing automatic perturbation analysis tools for neural networks.&nbsp;We study the conditions to apply A5 effectively, analyze the importance of the robustness of the to-be-defended classifier, and inspect the appearance of the robustified images. We show effective on-the-fly defensive augmentation with a robustifier network that ignores the ground truth label, and demonstrate the benefits of robustifier and classifier co-training. In our tests, A5 consistently beats state of the art certified defenses on MNIST, CIFAR10, FashionMNIST and Tinyimagenet. We also show how to apply A5 to create certifiably robust physical objects. Our code at https://github.com/NVlabs/A5 allows experimenting on a wide range of scenarios beyond the man-in-the-middle attack tested here, including the case of physical attacks.

## Problem

*(待补充)*

## Method

*(待补充)*

## Evaluation

*(待补充)*

## Limitations

*(待补充)*
