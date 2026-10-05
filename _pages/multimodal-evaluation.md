---
permalink: /projects/multimodal-evaluation/
title: "Multimodal Evaluation: Testing What a Score Means"
layout: single
author_profile: true
classes: wide project-story
project_story: true
description: "Amit Agarwal on first-author research into image-text metric invariance, global versus local reasoning, and reliable model comparisons."
---

When a model’s score improves, I want to understand what changed. Did the model become more useful, did the benchmark reward a shortcut, or did the evaluator react to an irrelevant detail? My multimodal evaluation research investigates the measurement itself so that comparisons can support better research and engineering decisions.

## Can Meaning Stay Constant While Scores Change?

I am the first author of [Do Image–Text Metrics Respect Semantic Invariances?](https://aclanthology.org/2026.findings-acl.1948/), published in ACL 2026 Findings. Our team tested five evaluators—CLIPScore, PAC-S, UMIC, FLEUR, and a deterministic LLM judge—using spatial, object, and wording perturbations intended to preserve meaning.

Across curated slices of three detection datasets and three caption evaluation suites, the study reports average score changes of approximately **6–9%**. For systems separated by **0.7%**, ranking reversals occurred in up to approximately **37% of cases**. A small human study supported the interpretation that the evaluated pairs generally remained equally correct. The proposed calibration roughly halved median absolute sensitivity. These findings describe the paper’s tested conditions, not all images, evaluators, or applications. [Primary paper record](https://aclanthology.org/2026.findings-acl.1948/).

## Does the Task Require the Whole Image?

I also first-authored [RCI: A Score for Evaluating Global and Local Reasoning in Multimodal Benchmarks](https://aclanthology.org/2025.emnlp-industry.10/), published at EMNLP 2025 Industry. The Region Comprehension Index compares reference-model performance using image patches and full images. Applied to **13 multimodal benchmarks**, the study found that most favored localized reasoning and exhibited spatial biases. RCI is a diagnostic tied to the models and benchmarks examined; it does not directly establish human-like understanding.

Both projects are collaborative research. First authorship identifies my role in the published work; the experimental findings belong to the author teams.

## How I Use These Questions

My perspective is that evaluation design is part of technical leadership. Before a team optimizes a number, it should be able to explain the behavior that number is intended to measure. Otherwise, an apparently successful iteration can send development in an unhelpful direction.

I favor complementary views of quality: representative examples, controlled changes, aggregate results, and human inspection where judgment matters. Each answers a different question. A controlled change can expose sensitivity, while a realistic task can reveal whether that sensitivity matters to the application. Neither replaces the other.

There is a practical tradeoff between richer evaluation and the time required to interpret it. I would prioritize checks capable of changing a decision: whether a model comparison is stable, whether a benchmark requires the capability we need, and whether the evaluator agrees with the intended notion of correctness. Calibration and diagnostic scores help investigate these questions; their value still depends on the use case.

This perspective connects to [Enterprise Retrieval](/projects/enterprise-retrieval/) and [Agentic Systems: From Evidence to Action](/projects/agentic-knowledge-systems/), where evidence selection and answer evaluation shape the same end-to-end decision. More work is listed under [publications](/publications/).

[Discuss this work](mailto:amit.pinaki@gmail.com).
