---
layout: paper
title: "Bias Before Disclosure: A Behavioral Audit of LLM Assistants Under User-Identity Uncertainty"
authors: "Hitesh Laxmichand Patel, Srikant Panda, Amit Agarwal, Tejaswini Kumar, Bhargava Kumar, Karan Dua, Jyotika Singh, Taki Hasan Rafi, Mithil Bangera, Yeshil Bangera, Gouthami Vadithya"
year: 2026
venue: "EMNLP 2026"
venue_token: emnlp
venue_url: "https://aclanthology.org/2026.emnlp-main.1758/"
tags: ["Responsible-AI", "Evaluation"]
keywords: ["Responsible-AI", "Evaluation", "LLM", "EMNLP"]
paper_url: "https://aclanthology.org/2026.emnlp-main.1758/"
pdf_url: "https://aclanthology.org/2026.emnlp-main.1758.pdf"
search: true
last_modified_at: 2026-11-02
---

## Research overview

**Problem.** Assistants may assume demographic characteristics even when a user's query provides no identity information.

**Contribution.** The paper audits unsupported demographic commitment in 18 LLMs using 212 information-seeking queries, including forced-choice and abstention-first settings, and tests an identity-abstention prompt intervention.

**Findings and scope.** In forced-choice testing, 11 of 18 models assigned demographic labels on over 80% of queries. The intervention reduced classifier-detected presupposition from 41% to 16%, while increasing clarification requests. These diagnostic and classifier-based measures should not be treated as direct estimates of real-world harm.

*Overview source: [EMNLP 2026 proceedings abstract](https://aclanthology.org/2026.emnlp-main.1758/).*

**Abstract.** LLM assistants frequently answer everyday queries that reveal nothing about the user’s demographic identity. We audit whether models nevertheless attribute demographic characteristics to the user, a behavior we call unsupported demographic commitment. Across 18 proprietary and open-weight LLMs evaluated on 212 filtered information-seeking queries, 11 of 18 models commit to a demographic label on more than 80% of queries under a forced-choice diagnostic. In the matched abstention-first setting, the eight tested models average 44% commitment, compared with 5% for human annotators. Conditional on commitment, race, SES, location, and education show the same directional skew across all six domains, while gender varies by domain. Demographic-coded patterns also appear in free-form answers when no identity inference is requested. We evaluate identity-abstention, a prompt-level intervention that reduces classifier-detected presupposition from 41% to 16%, with a measurable clarification cost on queries that can be answered without additional context.

*Abstract reproduced from [the authors’ proceedings record](https://aclanthology.org/2026.emnlp-main.1758/) under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); wording unchanged, whitespace normalized.*
