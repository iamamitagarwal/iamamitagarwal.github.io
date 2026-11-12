---
permalink: /projects/enterprise-retrieval/
title: "Enterprise Retrieval: Learning From Plausible Wrong Answers"
layout: single
author_profile: true
classes: wide project-story
project_story: true
description: "Amit Agarwal on co-first-author hard-negative mining research, domain-specific reranking, and the decisions behind useful retrieval evaluation."
---

A document can share the right vocabulary and still answer the wrong question. For an enterprise agent, that mistake can propagate into a recommendation or action. My retrieval research studies how to teach ranking models to distinguish useful evidence from convincing distractions.

## The Research Question

I am a **co-first author** of [Hard Negative Mining for Domain-Specific Retrieval in Enterprise Systems](https://aclanthology.org/2025.acl-industry.72/), published at ACL 2025 Industry. Our team studied how to select challenging, irrelevant documents for reranker training. These “hard negatives” resemble relevant material closely enough to expose mistakes that random examples can miss.

The published method combines multiple embedding representations, reduces their dimensionality, and selects difficult negatives for fine-tuning. On the proprietary cloud-services test set, the in-house cross-encoder reranker achieved **MRR@10 of 0.64**, compared with **0.57 for ADORE+STAR** and **0.45 without fine-tuning**. MRR rewards placing the first relevant result near the top; here the cutoff is ten results. The paper reports 1,000 training and 4,250 test query–positive-document pairs, with metrics averaged across three runs. These are study results from the shared research effort. [Paper, Tables 2–3](https://aclanthology.org/2025.acl-industry.72.pdf).

## Training data as a research decision

Selecting negatives is a decision about what the model should learn. Randomly irrelevant documents can make training look successful without exposing the distinctions that matter in a specialized domain. Challenging examples make those distinctions measurable, but an incorrectly labeled negative can teach the model to reject a valid answer.

I connect this research with my [shared knowledge architecture work](/projects/shared-knowledge-store/), where an agent may need to select evidence across products, versions and source types. The modeling question and the system question meet at the same point: what evidence is sufficient for this particular task?

The research also informs how I work with science and engineering teams. Failure analysis needs to distinguish a gap in the source material from a representation, ranking or labeling problem. Each points to a different intervention and a different experiment.

## From ranking quality to agent behavior

The paper establishes a ranking improvement on its evaluated cloud-services dataset. Application-level evaluation then asks whether the selected evidence helps an agent answer correctly or make a useful next move. Those are related questions, with different success criteria.

That distinction matters as retrieval becomes part of an agent loop. A new observation can change what information is needed, which source should be queried and whether earlier context is still applicable. My current work connects those agentic retrieval questions with reusable knowledge infrastructure and task-level evaluation.

Continue with [Agentic Systems: From Evidence to Action](/projects/agentic-knowledge-systems/) and [Multimodal Evaluation](/projects/multimodal-evaluation/), or explore my [publications](/publications/).

[Discuss this work](mailto:amit.pinaki@gmail.com).
