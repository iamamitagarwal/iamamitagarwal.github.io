---
permalink: /projects/multimodal-evaluation/
title: "Evaluating Agents & Multimodal AI"
layout: single
author_profile: true
classes: wide project-story
project_story: true
last_modified_at: 2026-11-11
description: "Amit Agarwal on long-horizon agent evaluation, tool use, research harnesses, creative-media workflows and reliable multimodal measurement."
---

I lead evaluation work that helps science and product teams decide whether an AI capability is ready for the behavior they need. The scope spans long-horizon support workflows, cloud-console actions and multimodal content, where a single answer score cannot explain whether the system made useful progress.

My work combines task and benchmark design, controlled comparisons, research harnesses and failure analysis. I bring those results into architecture and model decisions across science and engineering, with published research examining the reliability of the measurement itself.

## Long-horizon tasks and useful progress

In support and service-request workflows, I examine grounded answers, useful next steps, clarification, handoff and failure recovery. A longer conversation needs to preserve relevant context and recognize when a tool or retrieval step has failed. Evaluation must track progress across those steps as well as the final answer.

For cloud-console agents, the evaluation problem includes correct tool selection and arguments, appropriate human approval and verifiable changes to system state. The evaluation plans I work with combine outcome checks, tool-call evidence and multi-turn testing, with separate failure categories for the agent, infrastructure, simulator and verifier. These distinctions help science and engineering teams choose the right intervention.

## Research harnesses and reproducibility

I build evaluation methods that teams can inspect and reuse. My hands-on contributions include a streaming multimodal evaluator that preserves case-level evidence and explicitly marks incomplete runs. This lets teams check whether a better score reflects better behavior or missing cases and execution differences.

The broader method retains the evidence behind a score: task and data versions, model and prompt configuration, tool behavior, outputs and failure status. Human review and judge calibration matter when success depends on judgment, safety or the quality of a handoff. The goal is to make a scientific comparison useful for a delivery decision and reproducible by another team.

## Creative-media workflows

Our multimodal work has included image-generation evaluation using prompt-constraint checks and image-based questions, including chart understanding. This connects generation quality with whether the requested content is actually present and supported.

My current research also considers evaluation for editing, video and consistent style. Those extensions remain areas of development. They complement retrieval and image-understanding evaluation, with safety and moderation requirements included in the design.

## Research on the measurement itself

When a model’s score improves, I want to understand what changed: useful behavior, a benchmark shortcut or sensitivity in the evaluator itself. My published research investigates that measurement question.

### Can meaning stay constant while scores change?

I am the first author of [Do Image–Text Metrics Respect Semantic Invariances?](https://aclanthology.org/2026.findings-acl.1948/), published in ACL 2026 Findings. Our team tested five evaluators—CLIPScore, PAC-S, UMIC, FLEUR, and a deterministic LLM judge—using spatial, object, and wording perturbations intended to preserve meaning.

Across curated slices of three detection datasets and three caption evaluation suites, the study reports average score changes of approximately **6–9%**. For systems separated by **0.7%**, ranking reversals occurred in up to approximately **37% of cases**. A small human study supported the interpretation that the evaluated pairs generally remained equally correct. The proposed calibration roughly halved median absolute sensitivity. These findings describe the paper’s tested conditions, not all images, evaluators, or applications. [Primary paper record](https://aclanthology.org/2026.findings-acl.1948/).

### Does the task require the whole image?

I also first-authored [RCI: A Score for Evaluating Global and Local Reasoning in Multimodal Benchmarks](https://aclanthology.org/2025.emnlp-industry.10/), published at EMNLP 2025 Industry. The Region Comprehension Index compares reference-model performance using image patches and full images. Applied to **13 multimodal benchmarks**, the study found that most favored localized reasoning and exhibited spatial biases. RCI is a diagnostic tied to the models and benchmarks examined; it does not directly establish human-like understanding.

### Safety, bias and benchmark design

My collaborative research also examines what evaluation misses. [AccessEval](/publications/2025-accesseval-benchmarking-disability-bias-in-large-language-models/) studies disability bias, while [Bias Before Disclosure](/publications/2026-bias-before-disclosure-a-behavioral-audit-of-llm-assistants-under-user-identity-uncertainty/) audits demographic assumptions when users provide no identity information. [BenchHub](/publications/2025-benchhub-a-unified-benchmark-suite-for-holistic-and-customizable-llm-evaluation/) examines how benchmark composition affects comparisons and model rankings.

Together, these studies motivate complementary checks for task quality, safety, bias, consistency, and evaluator reliability. In agent workflows, that means examining task completion and tool use alongside the quality of the final response, with clear failure categories and human review where judgments are sensitive.

## Turning evaluation into research decisions

I use task-level failures, controlled comparisons and human inspection to help teams decide what to change next. That includes checking whether a model comparison is stable, whether a benchmark tests the capability the application needs and whether the evaluator rewards the intended behavior.

This perspective connects to [Enterprise Retrieval](/projects/enterprise-retrieval/) and [Agentic Systems: From Evidence to Action](/projects/agentic-knowledge-systems/), where evidence selection and answer evaluation shape the same end-to-end decision. More work is listed under [publications](/publications/).

[Discuss this work](mailto:amit.pinaki@gmail.com).
