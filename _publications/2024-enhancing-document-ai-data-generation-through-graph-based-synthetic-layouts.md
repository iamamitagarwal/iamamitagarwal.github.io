---
layout: paper
title: Enhancing Document AI Data Generation Through Graph-Based Synthetic Layouts
authors: 'Agarwal, Amit; Patel, Hitesh; Pattnayak, Priyaranjan; Panda, Srikant;
  Kumar, Bhargava; Kumar, Tejaswini; '
year: 2024
venue: arXiv
tags:
- Document-AI
- Graph
paper_url: https://arxiv.org/abs/2412.03590
search: true
---

**Abstract.** The development of robust Document AI models has been constrained by limited access to high-quality, labeled datasets, primarily due to data privacy concerns, scarcity, and the high cost of manual annotation. Traditional methods of synthetic data generation, such as text and image augmentation, have proven effective for increasing data diversity but often fail to capture the complex layout structures present in real world documents. This paper proposes a novel approach to synthetic document layout generation using Graph Neural Networks (GNNs). By representing document elements (e.g., text blocks, images, tables) as nodes in a graph and their spatial relationships as edges, GNNs are trained to generate realistic and diverse document layouts. This method leverages graph-based learning to ensure structural coherence and semantic consistency, addressing the limitations of traditional augmentation techniques. The proposed framework is evaluated on tasks such as document classification, named entity recognition (NER), and information extraction, demonstrating significant performance improvements. Furthermore, we address the computational challenges of GNN based synthetic data generation and propose solutions to mitigate domain adaptation issues between synthetic and real-world datasets. Our experimental results show that graph-augmented document layouts outperform existing augmentation techniques, offering a scalable and flexible solution for training Document AI models.
