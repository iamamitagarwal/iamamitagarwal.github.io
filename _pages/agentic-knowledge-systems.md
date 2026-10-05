---
permalink: /projects/agentic-knowledge-systems/
title: "Agentic Knowledge Systems: Making Evidence Usable"
layout: single
author_profile: true
classes: wide project-story
project_story: true
description: "Amit Agarwal's approach to shared knowledge infrastructure, retrieval, reranking, access-aware grounding, and evaluation for enterprise agents."
---

An agent answering an enterprise question needs usable evidence: relevant information, enough surrounding context to interpret it, and appropriate access to the source. My work on shared knowledge infrastructure brings these concerns together. The question guiding my architectural perspective is simple: **what must an agent know about its evidence before it can use it well?**

## My Role and Scope

As a Principal Applied Scientist at Oracle Cloud Infrastructure, I work across research, architecture, evaluation, and product integration. My work includes architecting shared knowledge infrastructure combining knowledge graphs, multimodal and multilingual retrieval, reranking, and access-aware grounding. My [profile](/) and [CV](/cv/) describe this contribution and its career context.

The following design principles illustrate how I reason about these systems. Their application depends on the task, available evidence, and deployment requirements.

## From Search Results to Evidence

Consider an illustrative support question whose answer depends on a paragraph, a diagram, and the product version. Retrieving a relevant paragraph may still leave the agent without the relationship shown in the diagram or the qualification attached to the version. I think about knowledge infrastructure as a way to preserve those relationships while making evidence retrievable.

Different components serve different purposes. Retrieval finds candidates; reranking helps decide which candidates deserve attention. A knowledge graph can represent explicit relationships, while access-aware grounding makes authorization part of deciding what evidence is eligible for use. My design preference is to give each component a clear responsibility and evaluate whether it improves the task at hand.

These choices involve tradeoffs. More context can improve coverage while introducing distracting material. Graph structure can make relationships explicit while adding maintenance requirements. Converting visual content into text can make it easier to search while losing information that requires direct visual interpretation. I treat those as questions to investigate against representative tasks.

## Evaluation as a Shared Language

My co-first-author [enterprise retrieval paper](https://aclanthology.org/2025.acl-industry.72/) examines difficult negative examples for ranking. My first-author [image–text evaluation paper](https://aclanthology.org/2026.findings-acl.1948/) examines whether evaluators respond to changes that preserve meaning. Together, they motivate my preference for inspecting both the evidence selected and the instrument used to judge the answer.

For technical leadership, I find it useful to make failures actionable across disciplines. Was necessary evidence absent? Was it retrieved but ranked poorly? Did the answer overlook a qualification? Did the evaluation reward the wrong behavior? These are distinct questions that help science and engineering teams choose the next intervention.

The public research supports specific experimental findings, detailed in the related stories. It does not establish a universal quality, cost, or latency improvement for a complete agent platform. My architectural aim is a system whose decisions can be inspected and whose improvements can be explained with evidence.

Read [Enterprise Retrieval](/projects/enterprise-retrieval/) and [Multimodal Evaluation](/projects/multimodal-evaluation/) for the supporting research, or return to [projects](/projects/).

[Discuss this work](mailto:amit.pinaki@gmail.com).
