---
layout: paper
title: 'RCI: A Score for Evaluating Global and Local Reasoning in Multimodal Benchmarks'
authors: 'Agarwal, Amit; Patel, Hitesh Laxmichand; Panda, Srikant; Meghwani, Hansa;
  Singh, Jyotika; Dua, Karan; Li, Paul; Sheng, Tao; Ravi, Sujith; Roth, Dan; '
year: 2025
venue: EMNLP
tags:
- LLM
- Retrieval
- Eval
- Vision-Language
- Safety
paper_url: https://aclanthology.org/2025.emnlp-industry.10/
search: true
---

**Abstract.** Multimodal Large Language Models (MLLMs) have achieved impressive results on vision-language benchmarks, yet it remains unclear whether these benchmarks assess genuine global reasoning or allow success via localized visual cues. Existing evaluation methods do not explicitly measure this distinction, hindering effective dataset curation and real-world focused model development. We introduce Region Comprehension Index (RCI), the first model-based score to directly quantify a dataset’s reliance on global versus local visual information. RCI systematically compares reference-model performance on image patches versus full images, revealing if tasks require holistic image understanding or can be solved with partial or localized visual cues. When applying RCI to 13 widely used multimodal benchmarks, we observed that most of them favor localized reasoning and exhibit significant spatial biases, indicating potential risks in real-world applications. RCI equips researchers & practitioners with an actionable tool for diagnosing & mitigating these biases, enabling the construction of datasets and benchmarks to foster the development of robust, enterprise-ready multimodal systems.
