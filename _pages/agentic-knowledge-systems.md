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

## Research and delivery across cloud agents

At Oracle AI Foundations, I lead applied-science work across research, architecture, evaluation and product integration. Shared knowledge infrastructure connects retrieval, ranking and semantic context with the evidence an agent needs to use.

### Support and service-request workflows

I collaborate with support and engineering teams on retrieval quality, multi-turn behavior and evaluation for enterprise support agents. My work includes model integration, testing with support tasks and investigating failures that appear in application use. Re-evaluating a change against the actual conversation helps connect a science recommendation with engineering follow-through.

Service-request resolution, ticket triage and incident investigation require an agent to retain context and choose useful next steps. I work on the retrieval and evaluation questions behind those workflows: whether the evidence addresses the request, whether follow-up turns remain grounded and whether the next action advances the task.

### Console AI and reusable agent capabilities

[Console AI](https://blogs.oracle.com/cloud-infrastructure/introducing-console-ai-oci) brings conversational assistance and reviewable resource actions into the OCI Console. My work connects applied science with cloud-console agent evaluation and integration, including the relationship between task intent, cloud context and useful evidence.

In the separate Agent Hub effort, my architecture work includes agent routing, skill and tool retrieval, shared context and memory. These capabilities raise a common research question: how can several agents use relevant evidence and tools without losing the context of a longer task?

My [Fusion and business-application work](/projects/multimodal-business-applications/) applies related retrieval and evaluation questions in another product setting.

## Personalized Leadership Coaching Pilot

I developed a personalized leadership-coaching agent pilot combining assessment-driven plans, persistent memory, retrieval-grounded recommendations, role-play practice, and proactive nudges. This pilot brings personalization, context retention, and practice into a shared agent workflow.

## Evaluating longer tasks

For a support workflow, I ask three practical questions:

- **Context:** What evidence and prior steps should the agent retain, and when should that context be refreshed?
- **Action:** What can the agent do, what needs human review, and how does it recognize an unsuccessful step?
- **Evaluation:** Did the workflow make useful progress toward resolution, and can we trace errors to evidence, reasoning, or tool use?

These questions help connect research priorities with engineering decisions and product needs. They also separate a plausible answer from progress on a real task.

## From Search Results to Evidence

Consider an illustrative support question whose answer depends on a paragraph, a diagram, and the product version. Retrieving a relevant paragraph may still leave the agent without the relationship shown in the diagram or the qualification attached to the version. I think about knowledge infrastructure as a way to preserve those relationships while making evidence retrievable.

Retrieval finds candidates; reranking prioritizes them; a knowledge graph can preserve explicit relationships. Access-aware grounding determines which evidence is eligible for use. I evaluate these choices against representative tasks, including cases where extra context distracts a model or visual-to-text conversion loses important information.

## Evaluation as a Shared Language

My co-first-author [enterprise retrieval paper](https://aclanthology.org/2025.acl-industry.72/) examines difficult negative examples for ranking. My first-author [image–text evaluation paper](https://aclanthology.org/2026.findings-acl.1948/) examines whether evaluators respond to changes that preserve meaning. Together, they motivate my preference for inspecting both the evidence selected and the instrument used to judge the answer.

For technical leadership, I find it useful to make failures actionable across disciplines. Was necessary evidence absent? Was it retrieved but ranked poorly? Did the answer overlook a qualification? Did the evaluation reward the wrong behavior? These are distinct questions that help science and engineering teams choose the next intervention.

My architectural aim is a system whose decisions can be inspected and whose improvements can be explained with evidence.

Read [Enterprise Retrieval](/projects/enterprise-retrieval/) and [Multimodal Evaluation](/projects/multimodal-evaluation/) for the supporting research, or return to [projects](/projects/).

[Discuss this work](mailto:amit.pinaki@gmail.com).
