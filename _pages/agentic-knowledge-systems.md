---
permalink: /projects/agentic-knowledge-systems/
title: "Agentic Systems: From Evidence to Action"
layout: single
author_profile: true
classes: wide project-story
project_story: true
description: "Amit Agarwal's work on support agents, incident triage, shared knowledge infrastructure, and research directions in long-horizon tasks and multimodal memory."
---

An enterprise agent needs to connect evidence with useful action: understand a support request, gather context, choose a next step, and assess whether the task is progressing. My work spans support agents, ticket automation, incident triage and resolution workflows, and the shared knowledge infrastructure that grounds them.

## My Role and Scope

As a Principal Applied Scientist at Oracle Cloud Infrastructure, I work across research, architecture, evaluation, and product integration. My work includes architecting shared knowledge infrastructure combining knowledge graphs, multimodal and multilingual retrieval, reranking, and access-aware grounding. My [profile](/) and [CV](/cv/) describe this contribution and its career context.

The following design principles illustrate how I reason about these systems. Their application depends on the task, available evidence, and deployment requirements.

## Support Workflows and Longer Tasks

My current research directions include **long-horizon tasks, multimodal agents, and multimodal memory**. I am interested in how agents preserve relevant context across steps, combine text and visual evidence, and use tools while keeping their decisions inspectable. These are ongoing directions, with task-specific evaluation guiding development.

For a support workflow, I ask three practical questions:

- **Context:** What evidence and prior steps should the agent retain, and when should that context be refreshed?
- **Action:** What can the agent do, what needs human review, and how does it recognize an unsuccessful step?
- **Evaluation:** Did the workflow make useful progress toward resolution, and can we trace errors to evidence, reasoning, or tool use?

These questions help connect research priorities with engineering decisions and product needs. They also separate a plausible answer from progress on a real task.

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
