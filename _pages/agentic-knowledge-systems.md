---
permalink: /projects/agentic-knowledge-systems/
title: "Cloud Agents: Support, Operations & Reusable Intelligence"
layout: single
author_profile: true
classes: wide project-story
project_story: true
last_modified_at: 2026-11-12
description: "Amit Agarwal's applied-science leadership across Oracle Support, Agent Hub and Console AI: long-horizon workflows, agent routing, context, tool use and evaluation."
---

I lead applied-science work on agents that help people investigate problems and get work done across cloud and support workflows. The challenge is to connect a user's goal with the right knowledge, tools and operational context, then sustain useful progress across a task that may take many steps.

## From support answers to resolution workflows

Support requests rarely arrive as complete specifications. An agent may need to clarify symptoms, find relevant product guidance, interpret prior tickets and decide whether to investigate further or hand over to an engineer. A fluent answer is only useful if it moves that process forward.

My Oracle Support work connects model integration, retrieval quality and multi-turn reasoning with service-request workflows. One example was preparing the work for an independent evaluation. The comparison needed to be usable outside the science team, with the model, knowledge configuration and environment clear to the people assessing it.

I coordinated with engineering on the service setup and access, checked that the evaluation team could use it, and brought the comparison material to Support. That completed a cross-team handoff from an internal research result to a setup others could examine. It is a practical part of my role: keeping the scientific assumptions visible as the work moves into an application.

The broader scope spans ticket triage, incident investigation, product and licensing questions, and resolution assistance. Different tasks need different evidence and authority. I focus on the shared capabilities behind them: retaining relevant context, selecting useful knowledge and tools, handling uncertainty and evaluating progress toward resolution.

## Agent Hub: reusable capabilities across applications

Within [Oracle AI Data Platform](https://www.oracle.com/ai-data-platform/), I lead applied-science and architecture work on agent discovery, routing and tool selection for Agent Hub. The platform gives organizations a way to connect people with capabilities across business functions. [AI Registry](https://www.oracle.com/ai-data-platform/ai-registry/) provides the inventory, capability descriptions and access controls that support discovery and reuse.

My work addresses semantic routing: interpreting the meaning of a request and the task's current state to select an appropriate agent, skill or tool. This brings research and platform architecture together. Choosing a plausible capability is not enough; the choice needs to fit what the user is trying to do and what that capability can actually perform.

Across a longer task, context and memory need the same care: retain what remains useful, while recognizing when an earlier assumption no longer holds. Those questions guide how I connect routing research with task-level evaluation.

I work across science and engineering on those decisions, connecting reusable architecture with application-level evaluation. Task-specific tools need clear inputs, permitted actions and interpretable results. Feedback traces—records of the agent's decisions, evidence and tool results—help teams diagnose errors and decide what to change.

Model selection raises a related question: which model offers the right quality, response time and cost for a request? I connect these application requirements with model evaluation, while keeping selection among models distinct from choosing an agent's next tool or action.

## Console AI

[Console AI](https://blogs.oracle.com/cloud-infrastructure/introducing-console-ai-oci) brings conversational guidance and reviewable resource actions into the Oracle Cloud Infrastructure (OCI) Console. It gives cloud operators a different interaction model: describe a goal, inspect the proposed action and work with an assistant that understands the surrounding cloud context.

My applied-science work connects task intent, tool selection, evidence and multi-turn evaluation with engineering integration. A successful agent needs to use the right resource and arguments, preserve permissions and approval boundaries, and recognize when the expected state change did not occur.

That creates a research agenda extending beyond response quality: long-horizon task completion, failure recovery, meaningful human oversight and the reliability of the evaluation environment itself. I use these questions to help align scientific investigation with the behavior the application needs.

<span id="personalized-leadership-coaching-pilot"></span>

## Leadership coaching assistant

I developed a leadership-coaching assistant that carries assessment and personal context into a learning plan, recommendations and role-play practice. The current prototype uses persistent memory and proactive nudges to explore a different form of long-running assistance: helping someone act on feedback over time.

## A common research agenda

Across these applications, I focus on three connected questions:

- **Context and memory:** Which evidence and prior decisions remain useful as the task changes?
- **Reasoning and action:** Which agent, skill or tool can advance the task, and what should require human review?
- **Evaluation:** Can we verify progress and distinguish failures in the agent from failures in its tools or environment?

These are shared research questions, but the product decisions differ. I work with science, product and engineering teams to decide which capabilities belong in the common platform and which need to remain specific to a support, cloud or coaching workflow.

The [Shared Knowledge Store](/projects/shared-knowledge-store/) supplies the broader knowledge foundation. My [Fusion application work](/projects/multimodal-business-applications/) explores multimodal AI in business workflows, while [agent and multimodal evaluation](/projects/multimodal-evaluation/) examines how to judge these capabilities.

[Discuss this work](mailto:amit.pinaki@gmail.com).
