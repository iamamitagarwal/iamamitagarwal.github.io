---
permalink: /projects/database-ai/
title: "Oracle AI Database 26ai & Agentic Retrieval"
layout: single
classes: wide project-story
project_story: true
last_modified_at: 2026-11-11
description: "Amit Agarwal's retrieval, semantic-context and evaluation work in the Oracle AI Database 26ai ecosystem, with vector, hybrid, graph and agent platform context."
---

Enterprise agents need to interpret business data and retrieve supporting evidence from documents. My applied-science work in the Oracle AI Database 26ai ecosystem focuses on retrieval, ranking, semantic context and the evaluation needed to connect those capabilities with applications.

## The data and retrieval foundation

Oracle AI Database 26ai provides several complementary capabilities:

- [AI Vector Search](https://docs.oracle.com/en/database/oracle/oracle-database/26/vecse/overview-ai-vector-search.html) uses embeddings for semantic retrieval alongside business data.
- [Hybrid search](https://docs.oracle.com/en/database/oracle/oracle-database/26/vecse/understand-hybrid-search.html) combines keyword and vector signals, useful when a query depends on both exact identifiers and meaning.
- [Graph-aware retrieval](https://docs.oracle.com/en/database/oracle/oracle-database/26/vecse/query-knowledge-graph.html) brings relationships into evidence selection for GraphRAG applications.

These platform capabilities establish the environment in which application-facing science must work. My focus is the quality of the evidence selected, how business meaning is represented and whether the resulting context helps an agent answer the actual question.

## Agents at the data boundary

Oracle also provides database-side agent offerings. [Oracle AI Database Agent Engine](https://blogs.oracle.com/database/introducing-oracle-ai-database-agent-engine) addresses agent execution around enterprise data. The [Select AI Agent Framework](https://docs.oracle.com/en/database/oracle/oracle-database/26/selai/select-ai-agent1.html) documents agent construction for Autonomous AI Database. These are distinct product interfaces that shape integration and evaluation requirements.

An application must connect the user's intent with eligible data, useful tools and evidence. That creates research questions about source selection, semantic interpretation, grounding and the handling of ambiguity.

## My research and architecture work

I lead work on shared knowledge infrastructure and current research connecting structured data with document evidence. Retrieval and ranking are part of that foundation; semantic context helps determine what a source means and how an agent should use it. The architecture must also preserve the evidence behind an answer as the task develops.

My [hard-negative mining research](/projects/enterprise-retrieval/) studies how ranking models distinguish relevant material from convincing distractions. My [agent and multimodal evaluation work](/projects/multimodal-evaluation/) examines the outcomes and failure modes that matter after evidence is retrieved. Together, these connect model research with the needs of application and platform teams.

[Shared knowledge and agent applications](/projects/agentic-knowledge-systems/) · [Fusion business applications](/projects/multimodal-business-applications/) · [All projects](/projects/)
