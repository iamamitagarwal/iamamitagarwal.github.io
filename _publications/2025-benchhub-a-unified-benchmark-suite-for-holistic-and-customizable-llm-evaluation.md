---
layout: paper
title: "Benchmarks Are Not Atomic: Composition-Aware LLM Evaluation using BenchHub"
authors: 'Eunsu Kim, Haneul Yoo, Guijin Son, Hitesh Patel, Amit Agarwal, Alice Oh'
year: 2026
venue: "NeurIPS 2026 Evaluations & Datasets Track (accepted)"
venue_token: neurips
venue_url: "https://neurips.cc/virtual/2026/poster/139267"
tags:
- Evaluation
keywords:
  - "Evaluation"
  - "NeurIPS"
  - "LLM"

paper_url: https://arxiv.org/abs/2506.00482
arxiv_id: "2506.00482"
pdf_url: "https://arxiv.org/pdf/2506.00482v2"
search: true
last_modified_at: 2026-11-02
---

## Research overview

**Problem.** A single benchmark score can hide which skills and contexts its questions cover, making model comparisons depend on the mix of examples.

**Contribution.** BenchHub describes benchmarks through attributes of individual examples, enabling inspection, comparison and controlled evaluation-set construction across 54 benchmarks, 839,000 samples and 10 languages.

**Findings and scope.** Aggregate scores concealed category-level performance differences, and model rankings changed under reweighting and resampling. The findings support making benchmark composition explicit; they do not identify a universally best model or benchmark mixture.

*Overview source: [arXiv v2 abstract, October 12, 2026](https://arxiv.org/abs/2506.00482v2).*

**Abstract.** LLM benchmarks are often treated as coherent measurement units, yet they are heterogeneous collections of instances spanning diverse domains, skills, formats, and contexts. As a result, aggregate benchmark scores can conflate model capability with benchmark composition, obscuring what existing benchmarks actually cover. We introduce BenchHub, a composition-aware evaluation framework that represents benchmarks as distributions over instance-level attributes. BenchHub integrates 54 benchmarks comprising 839K samples across 10 languages. It enables researchers to inspect benchmark contents, uncover reusable coverage hidden behind benchmark names, transparently compare benchmarks, and construct controllable evaluation sets for application-aligned model selection. Using BenchHub, we show that similarly motivated benchmarks can differ substantially in internal composition, existing benchmarks often contain reusable coverage beyond their stated purposes, models exhibit fine-grained category-level performance variation hidden by aggregate scores, and model rankings can shift under different reweighting and resampling configurations. Our results motivate evaluation practices that make benchmark composition explicit, inspectable, and controllable.

*Abstract reproduced from [the authors’ published record](https://arxiv.org/abs/2506.00482v2) under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); wording unchanged, whitespace normalized.*

**Version note.** This record describes [arXiv v2, revised October 12, 2026](https://arxiv.org/abs/2506.00482v2). The original May 2025 version was titled *BenchHub: A Unified Benchmark Suite for Holistic and Customizable LLM Evaluation*. The current arXiv record reports acceptance to the NeurIPS 2026 Evaluations & Datasets Track, and the paper appears in the [NeurIPS 2026 program](https://neurips.cc/virtual/2026/poster/139267).
