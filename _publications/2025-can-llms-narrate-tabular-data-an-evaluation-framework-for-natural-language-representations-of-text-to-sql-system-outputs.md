---
layout: paper
title: "Can LLMs Narrate Tabular Data? An Evaluation Framework for Natural Language Representations of Text-to-SQL System Outputs"
authors: "Jyotika Singh, Weiyi Sun, Amit Agarwal, Viji Krishnamurthy, Yassine Benajiba, Sujith Ravi, Dan Roth"
year: 2025
venue: EMNLP 2025 Industry Track
venue_token: emnlp
venue_url: "https://aclanthology.org/2025.emnlp-industry.60/"
tags:
  - Evaluation
keywords:
  - "Evaluation"
  - "Text-to-SQL"
  - "Tabular Data"
  - "EMNLP"
paper_url: "https://aclanthology.org/2025.emnlp-industry.60/"
pdf_url: "https://aclanthology.org/2025.emnlp-industry.60.pdf"
search: true
last_modified_at: 2026-11-11
---

**Abstract.** In modern industry systems like multi-turn chat agents, Text-to-SQL technology bridges natural language (NL) questions and database (DB) querying. The conversion of tabular DB results into NL representations (NLRs) enables the chat-based interaction. Currently, NLR generation is typically handled by large language models (LLMs), but information loss or errors in presenting tabular results in NL remains largely unexplored. This paper introduces a novel evaluation method - Combo-Eval - for judgment of LLM-generated NLRs that combines the benefits of multiple existing methods, optimizing evaluation fidelity and achieving a significant reduction in LLM calls by 25-61%. Accompanying our method is NLR-BIRD, the first dedicated dataset for NLR benchmarking. Through human evaluations, we demonstrate the superior alignment of Combo-Eval with human judgments, applicable across scenarios with and without ground truth references.

**Source.** [ACL Anthology proceedings PDF](https://aclanthology.org/2025.emnlp-industry.60.pdf); [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

**Summary.** This paper evaluates whether large language models can faithfully turn Text-to-SQL outputs into natural-language descriptions. It proposes a framework for judging the quality of such narrations over tabular results.
