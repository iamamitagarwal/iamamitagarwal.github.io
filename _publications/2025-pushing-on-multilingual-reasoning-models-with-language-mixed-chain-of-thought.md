---
layout: "single"
title: "Pushing on Multilingual Reasoning Models with Language-Mixed Chain-of-Thought"
authors: "Son, Guijin; Yang, Donghun; Patel, Hitesh Laxmichand; Agarwal, Amit; Ko, Hyunwoo; Lim, Chanuk; Panda, Srikant; Kim, Minhyuk; Drolia, Nikunj; Choi, Dasol;"
year: 2025
tags: [LLM, Retrieval, Document-AI, Systems]
paper_url: "https://arxiv.org/abs/2510.04230"
pdf_url: "https://arxiv.org/pdf/2510.04230.pdf"
search: true
---

**Abstract.** Recent frontier models employ long chain-of-thought reasoning to explore solution spaces in context and achieve stonger performance. While many works study distillation to build smaller yet capable models, most focus on English and little is known about language-specific reasoning. To bridge this gap, we first introduct **Language-Mixed CoT**, a reasoning schema that switches between English and a target language, using English as an anchor to excel in reasoning while minimizing translation artificats. As a Korean case study, we curate **Yi-Sang**: 5.79M native-Korean prompts from web Q&A, exams, STEM, and code; 3.7M long reasoning traces generated from Qwen3-32B; and a targeted 260k high-yield subset. We train ninve models (4B-35B) across six families (Qwen2.5, Llama-3.1, Gemma-3, etc). Our best model, **KO-REAson-35B**, achieves state-of-the-art performance, with the highest overall average score (64.0 \pm 25), ranking first on 5/9 benchmarks and second on the remainder. Samller and mid-sized models also benefit substantially, with an average improvement of +18.6 points across teh evaluated nine benchmarks. Ablations show **Language-Mixed CoT** is more effective than monolingual CoT, also resulting in cross-lingual and mult-modal performance gains. We release our data-curation pipeline, evaluation system, datasets, and models to advance research on language-specific reasoning. Data and model collection: https://huggingface.co/KOREAson.
