---
home_highlight_summary: "Evaluates research-level math solutions through their usefulness on related, verifiable problems."
layout: paper
title: "Judging What We Cannot Solve: A Consequence-Based Approach for Oracle-Free Evaluation of Research-Level Math"
authors: "Guijin Son, Donghun Yang, Hitesh Laxmichand Patel, Hyunwoo Ko, Amit Agarwal, Sunghee Ahn, Kyong-Ha Lee, Youngjae Yu"
year: 2026
venue: ICML 2026
venue_token: icml
priority: 0
highlight: true
highlight_rank: 2
recognition: "ICML 2026 Spotlight Paper"
recognition_type: spotlight
home_highlight_title: "Judging What We Cannot Solve"
tags:
  - Evaluation
keywords:
  - "Evaluation"
  - "Reasoning"
  - "Mathematical Reasoning"
  - "ICML"
paper_url: "https://proceedings.mlr.press/v306/son26a.html"
arxiv_id: "2602.06291"
search: true
last_modified_at: 2026-11-11
---

**Abstract.** Recent progress in reasoning models suggests that generating plausible attempts for
research-level mathematics may be within reach, but verification remains a bottleneck, consuming
scarce expert time. We hypothesize that a meaningful solution should contain enough method-level
information that, when applied to a neighborhood of related questions, it should yield better
downstream performance than incorrect solutions. Building on this idea, we propose Consequence-Based
Utility, an oracle-free evaluator that scores each candidate by testing its value as an in-context
exemplar in solving related yet verifiable questions. Our approach is evaluated on an original set
of research-level math problems each paired with one expert-written solution and nine LLM-generated
solutions. Notably, Consequence-Based Utility consistently outperforms reward models, generative
reward models, and LLM judges on ranking quality. Specifically, for GPT-OSS-120B it improves Acc@1
from 67.2 to 76.3 and AUC from 71.4 to 79.6, with similarly large AUC gains on GPT-OSS-20B (69.0 to
79.2). Furthermore, compared to LLM-Judges, it also exhibits a larger solver–evaluator gap,
maintaining stronger correct–wrong separation even on instances the underlying solver often fails to
solve.

**Source.** [Published ICML paper, PMLR 306](https://proceedings.mlr.press/v306/son26a.html). Copyright © 2026 by the authors.

**Summary.** This study evaluates research-level mathematics when checking each proposed solution directly is impractical. It scores a candidate solution by testing how useful it is as an example for solving related problems whose answers can be checked.
