---
layout: paper
title: "RECOR: Reasoning-Focused Multi-Turn Conversational Retrieval Benchmark"
authors: "Mohammed Ali, Abdelrahman Abdallah, Amit Agarwal, Hitesh Laxmichand Patel, Adam Jatowt"
year: 2026
venue: ACL Findings 2026
venue_token: acl
venue_url: "https://aclanthology.org/2026.findings-acl.129/"
tags:
  - Information-Retrieval
  - Evaluation
keywords:
  - "Information Retrieval"
  - "Conversational Retrieval"
  - "Reasoning"
  - "Evaluation"
  - "ACL Findings"
paper_url: "https://aclanthology.org/2026.findings-acl.129/"
arxiv_id: "2601.05461"
pdf_url: "https://aclanthology.org/2026.findings-acl.129.pdf"
search: true
last_modified_at: 2026-11-11
---

**Abstract.** Existing benchmarks treat multi-turn conversation and reasoning-intensive retrieval
separately, yet real-world information seeking requires both. To bridge this gap, we present a
benchmark for reasoning-based conversational information retrieval comprising 707 conversations
(2,971 turns) across eleven domains. To ensure quality, our Decomposition-and-Verification framework
transforms complex queries into fact-grounded multi-turn dialogues through multi-level validation,
where atomic facts are verified against sources and explicit retrieval reasoning is generated for
each turn. Comprehensive evaluation reveals that combining conversation history with reasoning
doubles retrieval performance (Baseline .236 → History+Reasoning .479 nDCG@10), while
reasoning-specialized models substantially outperform dense encoders. Despite these gains, further
analysis highlights that implicit reasoning remains challenging, particularly when logical
connections are not explicitly stated in the text.

**Source.** [“RECOR: Reasoning-focused Multi-turn Conversational Retrieval Benchmark,” ACL Anthology PDF](https://aclanthology.org/2026.findings-acl.129.pdf); [CC BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).

**Summary.** RECOR is a benchmark for reasoning-intensive conversational retrieval. It combines
multi-turn search with explicit retrieval reasoning, enabling evaluation of systems that must use
both conversation history and reasoning to retrieve the right evidence.
