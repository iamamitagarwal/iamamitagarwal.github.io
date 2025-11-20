---
layout: paper
title: 'PCRI: Measuring Context Robustness in Multimodal Models for Enterprise Applications'
authors: 'Laxmichand Patel, Hitesh; **Agarwal, Amit**; Panda, Srikant; Meghwani, Hansa;
  Dua, Karan; Li, Paul; Sheng, Tao; Ravi, Sujith; Roth, Dan; '
year: 2025
venue: EMNLP
tags:
- Eval
- Vision-Language
- LLM
- Retrieval
paper_url: https://aclanthology.org/2025.emnlp-industry.14/
search: true
---

**Abstract.** The reliability of Multimodal Large Language Models (MLLMs) in real-world settings is often undermined by sensitivity to irrelevant or distracting visual context, an aspect not captured by existing evaluation metrics. We introduce the Patch Context Robustness Index (PCRI), the first systematic and interpretable score for quantifying MLLM robustness to variations in visual context granularity, measuring performance changes between localized image patches and full-image input. Applying PCRI to 19 state-of-the-art MLLMs across 15 vision-language benchmarks, we find that most leading models remain brittle to background noise, with only a few, such as InternVL2-26B and Qwen2VL-72B, demonstrating consistent robustness across tasks. PCRI analysis also highlights how different model architectures handle and integrate visual context, offering actionable diagnostic insight for both researchers and practitioners. PCRI enables rigorous comparison of context robustness, supporting principled model selection and guiding the development of future architectures and training strategies for robust, real-world deployment.
