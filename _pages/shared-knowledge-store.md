---
permalink: /projects/shared-knowledge-store/
title: "Shared Knowledge Store: A Common Knowledge Fabric for Agents"
layout: single
classes: wide project-story
project_story: true
last_modified_at: 2026-11-12
description: "Amit Agarwal's research and architecture leadership on Shared Knowledge Store, connecting enterprise knowledge, semantic context and multimodal evidence for agentic applications."
---

I lead research and architecture for Shared Knowledge Store (SKS), a common knowledge and context foundation for Oracle AI applications. I work across science, engineering and application teams to turn fragmented organizational knowledge into evidence that agents can find, interpret and use.

The ambition is a connected institutional memory: an agent should understand how a service, its documentation, an incident and the team responsible for it relate to one another. That requires more than a collection of searchable documents. It requires a shared representation of meaning, relationships and the conditions under which information is useful.

## Building a foundation that teams can reuse

An application team building a support assistant and another building an operational agent often face the same knowledge problems. They need relevant sources, current context, citations and a way to understand relationships across systems. Solving those independently repeats work and leaves each application with a different view of the organization.

An important architecture question is how teams can share a knowledge service without blurring the boundaries of the evidence they are using. A request needs an explicit knowledge scope, and bringing in new sources should not leave applications uncertain about what was processed or where it belongs.

My contributions have made those boundaries concrete: requests with an unrecognized scope are rejected rather than quietly searching more broadly, and interrupted ingestion can resume against the intended sources and destination. That gives application teams an explicit contract for the knowledge they build on, while keeping source updates recoverable as the shared service evolves.

The architecture connects Confluence and documentation, Jira and incident history with code, service dependencies and ownership. My semantic-layer research extends that view to business records held in structured systems. The common goal is to preserve the relationships and evidence that each application needs.

## Context for agent decisions

Consider an on-call engineer investigating an incident. A relevant runbook is useful, but the decision may also depend on a related ticket, a service dependency, the applicable product version and who can authorize a change. An agent needs to bring those pieces together without treating similarity as proof that a recommendation is correct.

My research addresses relationship-aware retrieval, evidence coverage and context selection across a developing task. Knowledge graphs connect related artifacts; knowing where evidence came from and when it applied helps distinguish a useful precedent from an outdated one. The evaluation question is whether the assembled evidence supports a sound next step for the agent or engineer.

This foundation supports work on site reliability engineering (SRE), on-call assistance, incident investigation, service-request resolution and internal knowledge assistants. Logs, metrics and deployment context create further demands on how operational evidence is linked and interpreted. Finding a related incident can guide investigation; establishing a cause requires additional validation.

## Business meaning across records and documents

My current research on a unified semantic layer asks how an agent can connect the meaning in a business question with the right records and supporting documents. The design links concepts, source mappings, relationships and constraints with their evidence, while keeping the underlying systems authoritative.

An ontology is an explicit map of concepts and their relationships; a knowledge graph connects specific entities using those relationships. I work on how these representations can connect systems while preserving the evidence behind their meaning. A service, an incident and its owner should retain their identities as an agent moves between sources.

The research examines how shared meaning can guide source selection, structured database queries, document retrieval and clarification when a question is ambiguous. The [Oracle AI Database 26ai work](/projects/database-ai/) connects this application-facing research with the database's graph and retrieval capabilities.

## Multimodal knowledge

The same platform problem appears in media. Useful knowledge may be inside an image, a diagram or a moment in a long video. My work with media and application teams connects visual and language representations with retrieval and evaluation, so an agent can return the relevant evidence rather than only a file with a matching title.

Current research extends toward creative-media workflows, where retrieved assets and retained context can support generation and editing. Evaluating those workflows adds questions about intent, content fidelity and consistency across modalities.

## Connecting the research agenda with delivery

The shared foundation does not remove the need for application-specific judgment. An incident investigation, a business question and a media search can use the same knowledge layer while needing different evidence, models and checks. I work with the teams building those applications to make that distinction explicit in the research and evaluation.

My [hard-negative mining research](/projects/enterprise-retrieval/) addresses evidence selection; my [multilingual model-adaptation work](/publications/2025-aligning-llms-for-multilingual-consistency-in-enterprise-applications/) addresses consistent responses across languages. [Agent and multimodal evaluation](/projects/multimodal-evaluation/) examines how these capabilities behave in complete workflows.

[Cloud agents and support workflows](/projects/agentic-knowledge-systems/) · [Oracle AI Database 26ai](/projects/database-ai/) · [All projects](/projects/)
