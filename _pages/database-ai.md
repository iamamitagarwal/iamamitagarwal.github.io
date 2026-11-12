---
permalink: /projects/database-ai/
title: "Oracle AI Database 26ai & Agentic Retrieval"
layout: single
classes: wide project-story
project_story: true
last_modified_at: 2026-11-11
description: "Amit Agarwal's research on shared knowledge, semantic context and agentic retrieval in the Oracle AI Database 26ai ecosystem, connecting business data with application intelligence."
---

Enterprise agents need both business facts and the context that explains them. My work in the Oracle AI Database 26ai ecosystem connects shared knowledge architecture, semantic context and retrieval research with the needs of applications using enterprise data.

I lead application-facing science and architecture work, collaborating across research, platform and product teams. The database organization provides the underlying search and execution capabilities; my contribution focuses on how applications find, interpret and evaluate the evidence they use.

## A data foundation for agentic applications

Oracle AI Database 26ai brings AI retrieval and agent execution close to business data. Its complementary capabilities include:

- [AI Vector Search](https://docs.oracle.com/en/database/oracle/oracle-database/26/vecse/overview-ai-vector-search.html): embedding-based retrieval alongside relational business data, with [hybrid search](https://docs.oracle.com/en/database/oracle/oracle-database/26/vecse/understand-hybrid-search.html) for questions that depend on exact identifiers and semantic similarity.
- [Graph-based retrieval (GraphRAG)](https://docs.oracle.com/en/database/oracle/oracle-database/26/vecse/query-knowledge-graph.html): combines semantic search with relationships between entities to find supporting evidence.
- [AI Database Agent Engine](https://blogs.oracle.com/database/introducing-oracle-ai-database-agent-engine): governed, stateful agent workflows within the database, including routing, loops and human approval gates.

These capabilities broaden what an application can ask of its data foundation. A workflow can combine a business record, a document that explains a policy and a tool that performs an authorized operation. The research challenge is to make their meanings and evidence agree.

## Shared meaning across business data

My current research on a unified semantic layer examines how business concepts, source mappings, relationships and constraints can guide an agent toward the right evidence. A field name is not enough: its meaning can depend on a stored value, a time period or a rule defined in a document.

I work on the architectural choices behind a common ontology: a shared vocabulary of concepts and relationships across systems. Knowledge graphs give those concepts concrete links to records, documents and supporting evidence. The research includes how to grow that representation across sources while retaining source identity, conflicting interpretations and the context in which a relationship applies.

I work on how to represent that context, connect structured and unstructured sources and evaluate whether the added meaning improves the application's decisions. This research complements the [Shared Knowledge Store](/projects/shared-knowledge-store/), which makes enterprise knowledge reusable across agents and applications.

The database provides complementary building blocks. Its [knowledge-graph creation and maintenance tools](https://docs.oracle.com/en/database/oracle/oracle-database/26/vecse/dbms_graphRAG.html) extract entities and relationships from source text, add sources and update graph data when configured. Those product capabilities support application research; an accurate business ontology still requires decisions about meaning, evidence and ownership.

## Research that informs platform use

My [hard-negative mining research](/projects/enterprise-retrieval/) studies how models distinguish relevant evidence from convincing distractions. My [evaluation work](/projects/multimodal-evaluation/) asks whether an improvement survives changes in context, task and measurement. Both matter when application teams decide which representation, retrieval path or model to adopt.

I bring these findings into architecture and integration discussions with science and engineering teams. The aim is a reusable data-to-context foundation that supports business applications while keeping the evidence behind their answers inspectable.

The broader portfolio includes [Select AI's agent framework](https://docs.oracle.com/en/database/oracle/oracle-database/26/selai/select-ai-agent1.html). Oracle's October 2026 [AI Data Platform announcement](https://www.oracle.com/ca-en/news/announcement/ai-world-oracle-ai-data-platform-brings-ai-assisted-business-context-to-enterprise-ai-2026-10-27/) extends the product direction toward reusable business context and human-governed ontologies, with new capabilities planned over the following 12 months.

[Shared knowledge and agent applications](/projects/agentic-knowledge-systems/) · [Fusion business applications](/projects/multimodal-business-applications/) · [All projects](/projects/)
