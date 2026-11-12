---
layout: paper
title: "Think Twice Before You Write -- an Entropy-based Decoding Strategy to Enhance LLM Reasoning"
authors: "Jiashu He, Meizhu Liu, Olaitan P Olaleye, Amit Agarwal, M. Avendi, Yassi Abbasi, Matthew Rowe, Hitesh Laxmichand Patel, Paul Li, Tao Sheng, Sujith Ravi, Dan Roth"
year: 2026
venue: Under Review
venue_token: arxiv
tags:
  - Reasoning
  - Evaluation
keywords:
  - "Reasoning"
  - "Decoding"
  - "Entropy"
  - "LLM"
  - "arXiv"
paper_url: "https://arxiv.org/abs/2604.00018"
arxiv_id: "2604.00018"
search: true
last_modified_at: 2026-11-11
---

**Abstract.** Decoding strategies play a central role in shaping the reasoning ability of large
language models (LLMs). Traditional methods such as greedy decoding and beam search often suffer
from error propagation, while sampling-based approaches introduce randomness without adequate
robustness. Self-consistency improves reliability by aggregating multiple rollouts, but incurs
significant computational overhead. We propose an entropy-guided decoding framework that introduces
token-level adaptivity into generation. At each step, the model computes the entropy of the token
distribution, identifies high-uncertainty positions, and selectively branches on these vulnerable
points. A dynamic pool of partial rollouts is maintained and expanded until solutions are completed,
concentrating computation where uncertainty is greatest and avoiding unnecessary exploration in
confident regions. To enable efficient termination, we apply a rollout-level Entropy After
&lt;/Think&gt; (EAT) stopping criterion by performing entropy evaluation after the full reasoning
trace, rather than incrementally at every step. Experiments on GSM8K, AMC2023, and their perturbed
variants demonstrate that our method achieves consistently strong accuracy. Notably, on smaller
LLMs, performance is comparable to GPT-5 while operating at a fraction of the cost.

**Source.** [“Think Twice Before You Write -- an Entropy-based Decoding Strategy to Enhance LLM Reasoning,” arXiv:2604.00018v1](https://arxiv.org/abs/2604.00018v1); [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

**Summary.** This paper proposes an entropy-guided decoding framework for improving LLM reasoning.
The method identifies high-uncertainty token positions, selectively branches generation around those
points, and uses an Entropy After Think stopping criterion to reduce unnecessary rollout
computation.
