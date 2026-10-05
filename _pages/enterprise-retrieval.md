---
permalink: /projects/enterprise-retrieval/
title: "Enterprise Retrieval: Learning From Plausible Wrong Answers"
layout: single
author_profile: true
classes: wide project-story
project_story: true
description: "Amit Agarwal on co-first-author hard-negative mining research, domain-specific reranking, and the decisions behind useful retrieval evaluation."
---

A document can share the right vocabulary and still answer the wrong question. My enterprise retrieval research asks how to teach a ranking model to recognize that distinction. It connects a practical search problem with a broader technical leadership responsibility: choosing training examples and evaluation criteria that reflect the decisions a system must make.

## The Research Question

I am a **co-first author** of [Hard Negative Mining for Domain-Specific Retrieval in Enterprise Systems](https://aclanthology.org/2025.acl-industry.72/), published at ACL 2025 Industry. Our team studied how to select challenging, irrelevant documents for reranker training. These “hard negatives” resemble relevant material closely enough to expose mistakes that random examples can miss.

The published method combines multiple embedding representations, reduces their dimensionality, and selects difficult negatives for fine-tuning. On the proprietary cloud-services test set, the in-house cross-encoder reranker achieved **MRR@10 of 0.64**, compared with **0.57 for ADORE+STAR** and **0.45 without fine-tuning**. MRR rewards placing the first relevant result near the top; here the cutoff is ten results. The paper reports 1,000 training and 4,250 test query–positive-document pairs, with metrics averaged across three runs. These are study results from the shared research effort. [Paper, Tables 2–3](https://aclanthology.org/2025.acl-industry.72.pdf).

## The Design Decision

The decision I find most useful is to treat training-data selection as a model-design choice. When two documents discuss neighboring concepts, a strong system needs to distinguish their relevance to the actual question. More data helps only when it teaches the distinction we care about.

In my approach to technical leadership, that means making the error understandable before choosing the intervention. I want a team to be able to explain why a candidate is wrong, what information would make it right, and whether the labeling process captures that difference. A difficult negative that is actually a valid answer can teach the wrong behavior.

There is also a tradeoff between richer representations and operational complexity. My preference is to judge additional components by the failures they resolve and the evidence they add. An architecture should remain understandable enough that another researcher can inspect its assumptions and an engineer can reason about its maintenance.

## What the Result Establishes

The comparison supports the reported ranking improvement under the paper’s dataset and training conditions. It does not quantify downstream answer correctness, customer adoption, production latency, or business impact. A retrieval result is one part of an agent’s evidence chain.

My practical takeaway is to connect model development to an explicit evaluation question: did the system learn to separate the relevant answer from a convincing distraction? That question remains useful when the surrounding application, model, or document collection changes.

Continue with [Agentic Systems: From Evidence to Action](/projects/agentic-knowledge-systems/) and [Multimodal Evaluation](/projects/multimodal-evaluation/), or explore my [publications](/publications/).

[Discuss this work](mailto:amit.pinaki@gmail.com).
