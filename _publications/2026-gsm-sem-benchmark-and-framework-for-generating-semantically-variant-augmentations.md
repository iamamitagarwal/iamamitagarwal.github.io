---
layout: paper
title: "GSM-SEM: Benchmark and Framework for Generating Semantically Variant Augmentations"
authors: "Jyotika Singh, Fang Tu, Aziza Mirsaidova, Amit Agarwal, Hitesh Laxmichand Patel, Sandip Ghoshal, Miguel Ballesteros, Karan Dua, Yassine Benajiba, Weiyi Sun, Tao Sheng, Graham Horwood, Sujith Ravi, Dan Roth"
year: 2026
venue: arXiv
venue_token: arxiv
tags:
  - Evaluation
  - Reasoning
keywords:
  - "Evaluation"
  - "Reasoning"
  - "Math Reasoning"
  - "Benchmark Augmentation"
  - "arXiv"
paper_url: "https://arxiv.org/abs/2605.07053"
arxiv_id: "2605.07053"
search: true
last_modified_at: 2026-11-11
---

**Abstract.** Benchmarks like GSM8K are popular measures of mathematical reasoning, but leaderboard
gains can overstate true capability due to memorization of fixed test sets. Most robustness variants
apply surface-level perturbations (paraphrases, renamings, number swaps, distractors) that largely
preserve the underlying facts, and static releases can themselves become memorization targets over
time. We introduce GSM-SEM, a reusable and stochastic framework for generating semantically diverse
benchmark variants with substantially higher semantic variance than prior approaches. GSM-SEM
perturbs problem statements by modifying entities, attributes, and/or relationships, frequently
altering underlying facts and requiring models to recompute solutions under new conditions, while
constraining generation to preserve the original calculations/answer and approximate problem
difficulty. GSM-SEM generates fresh variants on each run without requiring re-annotation, reducing
reliance on static public benchmarks for evaluation and thereby lowering the bias of memorization.
We apply GSM-SEM on GSM8K and two existing variation suites (GSM-Symbolic and GSM-Plus), producing
GSM8K-SEM, GSM-Symbolic-SEM, and GSM-Plus-SEM. Evaluating 14 SOTA LLMs, we observe consistent
performance drops with larger decline when semantic perturbations are coupled with symbolic/plus
variations (average drop rate ~28% in maximum strictness configuration of GSM-SEM). We publicly
release the three SEM variants as fully human-validated datasets. Finally, to demonstrate
applicability beyond GSM-style math problems, we apply GSM-SEM to additional benchmarks including
BigBenchHard, LogicBench, and NLR-BIRD.

**Source.** [“GSM-SEM: Benchmark and Framework for Generating Semantically Variant Augmentations,” arXiv:2605.07053v2](https://arxiv.org/abs/2605.07053v2); [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

**Summary.** GSM-SEM introduces a reusable framework for generating semantically diverse variants of
math reasoning benchmarks. Instead of relying on surface paraphrases alone, it changes entities,
attributes, and relationships while preserving answer structure and approximate difficulty, reducing
memorization pressure in static benchmark use. The paper evaluates state-of-the-art LLMs on
GSM-style and broader reasoning tasks using these semantic augmentations.
