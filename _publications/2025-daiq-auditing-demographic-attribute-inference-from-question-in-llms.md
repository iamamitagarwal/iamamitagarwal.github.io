---
layout: paper
title: 'DAIQ: Auditing Demographic Attribute Inference from Question in LLMs'
authors: 'Panda, Srikant; Patel, Hitesh Laxmichand; Al-Khalifa, Shahad; **Agarwal,
  Amit**; Al-Khalifa, Hend; Al-Ghamdi, Sharefah; '
year: 2025
venue: arXiv
tags:
- Graph
- LLM
- Safety
paper_url: https://arxiv.org/abs/2508.15830
search: true
---

**Abstract.** Large Language Models (LLMs) are known to reflect social biases when demographic attributes, such as gender or race, are explicitly present in the input. But even in their absence, these models still infer user identities based solely on question phrasing. This subtle behavior has received far less attention, yet poses serious risks: it violates expectations of neutrality, infers unintended demographic information, and encodes stereotypes that undermine fairness in various domains including healthcare, finance and education. We introduce Demographic Attribute Inference from Questions (DAIQ), a task and framework for auditing an overlooked failure mode in language models: inferring user demographic attributes from questions that lack explicit demographic cues. Our approach leverages curated neutral queries, systematic prompting, and both quantitative and qualitative analysis to uncover how models infer demographic information. We show that both open and closed source LLMs do assign demographic labels based solely on question phrasing. Prevalence and consistency of demographic inferences across diverse models reveal a systemic and underacknowledged risk: LLMs can fabricate demographic identities, reinforce societal stereotypes, and propagate harms that erode privacy, fairness, and trust posing a broader threat to social equity and responsible AI deployment. To mitigate this, we develop a prompt-based guardrail that substantially reduces identity inference and helps align model behavior with fairness and privacy objectives.
