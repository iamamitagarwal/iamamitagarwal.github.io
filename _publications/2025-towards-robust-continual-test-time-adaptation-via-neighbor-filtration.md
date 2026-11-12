---
layout: paper
title: "Towards Robust Continual Test-Time Adaptation via Neighbor Filtration"
authors: "Taki Hasan Rafi, Amit Agarwal, Hitesh Laxmichand Patel, Dong-Kyu Chae"
year: 2025
venue: CIKM 2025
venue_url: "https://doi.org/10.1145/3746252.3760858"
tags: ["Multimodal"]
keywords:
  - "Multimodal"
  - "CIKM"
paper_url: "https://doi.org/10.1145/3746252.3760858"
search: true
last_modified_at: 2026-11-11
---

**Abstract.** Test-Time Adaptation (TTA) aims to adapt an unseen target domain utilizing the unlabeled target data using a pre-trained source model. Continual TTA is a more challenging paradigm that deals with non-stationary environments during the test data adaptation. Most existing continual TTA methods are based on pseudo-labeling, but often (1) rely on overconfident pseudo-labels and (2) remain unstable under continual distribution shifts leading to error accumulation and catastrophic forgetting. To tackle these limitations, we propose *Neighbor-Filtration based Continual Test-Time Adaptation* (NF-CTTA), a reliable and memory-aware adaptation framework that addresses these challenges. NF-CTTA first calibrates pseudo-labels using class-conditional calibration error to correct over/under-confidence of the model. To further ensure reliability, we introduce an OOD Neighbor Filtration technique that selects a subset of high-confidence samples based on entropy and neighbor similarity, ensuring consistency within the semantic neighborhood. Finally, we propose a priority-guided memory buffer that retains the most informative low-entropy samples for replay, mitigating catastrophic forgetting across evolving test distributions. Extensive experiments across multiple domain shift benchmarks demonstrate that NF-CTTA achieves superior performance and stability compared to existing TTA and CTTA methods. The code is available at: https://github.com/takihasan/NF-CTTA.

Source: [ACM publication DOI](https://doi.org/10.1145/3746252.3760858) ([author accepted manuscript](https://openreview.net/pdf/87e6c1ef17739255ecdf8cace1424c75fc0dcbf5.pdf), [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)).
