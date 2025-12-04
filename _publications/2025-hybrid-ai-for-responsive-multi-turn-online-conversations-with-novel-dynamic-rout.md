---
layout: paper
title: "Hybrid AI for Responsive Multi-Turn Online Conversations With Novel Dynamic Routing and Feedback Adaptation"
authors: 'Priyaranjan Pattnayak; Amit Agarwal; Hansa Meghwani; Hitesh Laxmichand Patel; Srikant Panda'
year: 2025
venue: NAACL
tags:
- LLM
- Retrieval
paper_url: https://aclanthology.org/2025.knowledgenlp-1.20/
search: true
---

**Abstract.** Retrieval-Augmented Generation (RAG) systems and large language model (LLM)-powered chatbots have significantly advanced conversational AI by combining generative capabilities with external knowledge retrieval. Despite their success, enterprise-scale deployments face critical challenges, including diverse user queries, high latency, hallucinations, and difficulty integrating frequently updated domain-specific knowledge. This paper introduces a novel hybrid framework that integrates RAG with intent-based canned responses, leveraging predefined high-confidence responses for efficiency while dynamically routing complex or ambiguous queries to the RAG pipeline. Our framework employs a dialogue context manager to ensure coherence in multi-turn interactions and incorporates a feedback loop to refine intents, dynamically adjust confidence thresholds, and expand response coverage over time. Experimental results demonstrate that the proposed framework achieves a balance of high accuracy (95%) and low latency (180ms), outperforming RAG and intent-based systems across diverse query types, positioning it as a scalable and adaptive solution for enterprise conversational AI applications.
