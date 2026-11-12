---
layout: paper
title: "Robust Audio-Text Retrieval via Cross-Modal Attention and Hybrid Loss"
authors: "Meizhu Liu, Matthew Rowe, Amit Agarwal, Michael Avendi, Yassi Abbasi, Hitesh Laxmichand Patel, Paul Li, Kyu J. Han, Tao Sheng, Sujith Ravi, Dan Roth"
year: 2026
venue: arXiv
venue_token: arxiv
tags:
  - Multimodal
  - Retrieval
keywords:
  - "Multimodal"
  - "Retrieval"
paper_url: "https://arxiv.org/abs/2604.23323"
arxiv_id: "2604.23323"
pdf_url: "https://arxiv.org/pdf/2604.23323"
search: true
last_modified_at: 2026-11-11
---

**Abstract.** Audio-text retrieval enables semantic alignment between audio content and natural
language queries, supporting applications in multimedia search, accessibility, and surveillance.
However, current state-of-the-art approaches struggle with long, noisy, and weakly labeled audio due
to their reliance on contrastive learning and large-batch training. We propose a novel multimodal
retrieval framework that refines audio and text embeddings using a cross-modal embedding refinement
module combining transformer-based projection, linear mapping, and bidirectional attention. To
further improve robustness, we introduce a hybrid loss function blending cosine similarity,
$\mathcal{L}_{1}$, and contrastive objectives, enabling stable training even under small-batch
constraints. Our approach efficiently handles long-form and noisy audio (SNR 5 to 15) via
silence-aware chunking and attention-based pooling. Experiments on benchmark datasets demonstrate
improvements over prior methods.

**Source.** [“Robust Audio-Text Retrieval via Cross-Modal Attention and Hybrid Loss,” arXiv:2604.23323v1](https://arxiv.org/abs/2604.23323v1); [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

**Summary.** The paper develops an audio–text retrieval framework that refines both modalities
through transformer projections, linear mappings and bidirectional attention. A combined cosine, L1
and contrastive training objective supports smaller batches, while silence-based segmentation and
attention pooling address lengthy, noisy recordings. Benchmark experiments evaluate retrieval
improvements over earlier approaches.
