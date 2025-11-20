---
layout: paper
title: Aligning llms for multilingual consistency in enterprise applications
authors: '**Agarwal, Amit**; Meghwani, Hansa; Patel, Hitesh Laxmichand; Sheng, Tao;
  Ravi, Sujith; Roth, Dan; '
year: 2025
venue: EMNLP
tags:
- Safety
- Multilingual
- LLM
- Retrieval
paper_url: https://aclanthology.org/2025.emnlp-industry.9/
search: true
---

**Abstract.** Large language models (LLMs) remain unreliable for global enterprise applications due to substantial performance gaps between high-resource and mid/low-resource languages, driven by English-centric pretraining and internal reasoning biases. This inconsistency undermines customer experience and operational reliability in multilingual settings such as customer support, content moderation, and information retrieval. Even with advanced Retrieval-Augmented Generation (RAG) systems, we observe up to an 29% accuracy drop in non-English languages compared to English. We propose a practical, batch-wise alignment strategy for fine-tuning LLMs, leveraging semantically equivalent multilingual data in each training batch to directly align model outputs across languages. This approach improves non-English accuracy by up to 23.9% without compromising English performance, model reasoning, or retrieval quality. Our method is simple to implement, scalable, and integrates seamlessly with existing LLM training & deployment pipelines, enabling more robust and equitable multilingual AI solutions in industry.
