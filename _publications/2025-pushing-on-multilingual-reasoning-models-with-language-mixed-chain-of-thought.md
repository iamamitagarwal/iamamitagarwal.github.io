---
layout: paper
title: "Pushing on Multilingual Reasoning Models With Language-Mixed Chain-of-Thought"
authors: 'Guijin Son, Donghun Yang, Hitesh Laxmichand Patel, Amit Agarwal, Hyunwoo Ko, Chanuk Lim, Srikant Panda, Minhyuk Kim, Nikunj Drolia, Dasol Choi, Kyong-Ha Lee, Youngjae Yu'
year: 2026
venue: ICLR 2026
venue_token: iclr
venue_url: "https://iclr.cc/virtual/2026/poster/10011063"
priority: 1
tags:
- Multilingual
keywords:
  - "Multilingual"
  - "ICLR 2026"
  - "ICLR"
paper_url: "https://iclr.cc/virtual/2026/poster/10011063"
arxiv_id: "2510.04230"
pdf_url: "https://openreview.net/pdf?id=ABc5y3741T"
search: true
last_modified_at: 2026-11-11
---

**Abstract.** Recent frontier models employ long-chain-of-thought reasoning to explore solution spaces in context and achieve stronger performance. While many works study distillation to build smaller yet capable models, most focus on English and little is known about language-specific reasoning. To bridge this gap, we first introduce Language-Mixed CoT, a reasoning schema that switches between English and a target language, using English as an anchor to excel in reasoning while minimizing translation artifacts. As a Korean case study, we curate YI-SANG: 5.79M native-Korean prompts from web Q&A, exams, STEM, and code; 3.7M long reasoning traces generated from Qwen3-32B; and a targeted 260k high-yield subset. We train nine models (4B–35B) across six families (Qwen2.5, Llama-3.1, Gemma-3, etc). Our best model, KO-REAson-35B, achieves state-of-the-art performance, with the highest overall average score (64.0±2.5), ranking first on 5/9 benchmarks and second on the remainder. Smaller and mid-sized models also benefit substantially, with an average improvement of +18.6 points across the evaluated nine benchmarks. Ablations show Language-Mixed CoT is more effective than monolingual CoT, also resulting in cross-lingual and multi-modal performance gains. We release our data-curation pipeline, evaluation system, datasets, and models to advance research on language-specific reasoning.

**Source.** [Final ICLR paper PDF](https://openreview.net/pdf?id=ABc5y3741T).
