---
permalink: /
title: "Applied AI Research & Technical Leadership"
layout: single
author_profile: true
classes: wide profile-overview
description: "Amit Agarwal, Principal Applied Scientist at Oracle Cloud Infrastructure, connects action-oriented AI agents, retrieval, multimodal research, and evaluation with enterprise delivery."
tags: ["About", "Profile", "GenAI", "Oracle AI", "Amit Agarwal"]
keywords: ["Amit Agarwal", "Oracle AI", "OCI", "GenAI", "LLM", "RAG", "Evaluation", "Retrieval", "Multilingual", "Multimodal", "Agentic AI", "AI agents", "AI safety"]
header:
  overlay_image: /images/llm-hero.gif
  overlay_video: /files/videos/hero-16x9-720.mp4
  overlay_video_small: /files/videos/hero-16x9-360.mp4
  overlay_video_wide: /files/videos/hero-21x9-1280x544.mp4
  overlay_video_superwide: /files/videos/hero-3x1-1200x400.mp4
  overlay_video_ultrawide: /files/videos/hero-4x1-1280x320.mp4
  overlay_filter: 0.40
---

I’m **Amit Agarwal**, a **Principal Applied Scientist at Oracle Cloud Infrastructure**, with **10+ years in applied AI**. I lead technical work from research questions and model development through architecture, evaluation, and product integration. I joined OCI in 2021, following roles as Data Science Lead at Jio Platforms and Data Scientist at Abzooba.

My current work connects **action-oriented AI agents, shared knowledge infrastructure, multimodal and multilingual AI, and evaluation**. I shape research priorities and architecture, stay hands-on with models and evaluation harnesses, and bring science and engineering teams together to build reusable capabilities and guide product decisions.

[Research](/publications/) · [Projects](/projects/) · [CV](/cv/) · [Contact](mailto:amit.pinaki@gmail.com)

## Research Highlights
{% assign highlighted_pubs = site.publications | where: "highlight", true | sort: "highlight_rank" %}
<div class="research-highlights">
  {% for p in highlighted_pubs %}
  <article class="research-highlight research-highlight--{{ p.recognition_type | default: 'highlight' }}">
    <p class="research-highlight__recognition">{{ p.recognition }}</p>
    <h3><a href="{{ p.url | relative_url }}" title="{{ p.title }}">{{ p.home_highlight_title | default: p.title }}</a></h3>
  </article>
  {% endfor %}
</div>

## Research and Technical Leadership

I connect research with the systems that put it to work: framing problems, shaping architecture, building models, and defining evidence for product decisions. My work spans four connected areas.

### AI Agents & Knowledge Systems

I work on support agents and ticket automation, including incident triage and resolution workflows. My current research directions include **long-horizon tasks, multimodal agents, and agent memory**. Shared knowledge infrastructure provides the grounding for this work through retrieval, reranking, knowledge graphs, and access-aware context. My research spans [hard-negative mining](/publications/2025-hard-negative-mining-for-domain-specific-retrieval-in-enterprise-systems/), [conversational retrieval (RECOR)](/publications/2026-recor-reasoning-focused-multi-turn-conversational-retrieval-benchmark/), and [lifecycle-aware conversation clustering](/publications/2025-llm-guided-lifecycle-aware-clustering-of-multi-turn-customer-support-conversations/).

[Read the systems perspective](/projects/agentic-knowledge-systems/).

### Multimodal AI

I work on models that connect language, images, and context. This includes science co-ownership of multimodal RAG for Oracle Fusion, contributing to an image-to-text capability deployed in August 2025, and research on [context robustness (PCRI)](/publications/2025-pcri-measuring-context-robustness-in-multimodal-models-for-enterprise-applicatio/) and [culture mixing in vision-language models](/publications/2026-world-in-a-frame-understanding-culture-mixing-as-a-new-challenge-for-vision-language-models/).

### Evaluation & Reliability

I develop evaluation methods and harnesses that help teams understand model behavior and failure modes. Research includes [multimodal reasoning (RCI)](/publications/2025-rci-a-score-for-evaluating-global-and-local-reasoning-in-multimodal-benchmarks/), [semantic invariance of image-text metrics](/publications/2026-do-image-text-metrics-respect-semantic-invariances/), and the work on LLM judging and disability bias highlighted above.

[Read the evaluation perspective](/projects/multimodal-evaluation/).

### Document Intelligence

My work spans OCR, layout understanding, visual question answering, and information extraction. I connect model development with reusable document capabilities, supported by research on [domain-adapting graph networks](/publications/2025-fs-dag-few-shot-domain-adapting-graph-networks-for-visually-rich-document-unders/) and [multilingual synthetic documents (FlexDoc)](/publications/2025-flexdoc-parameterized-sampling-for-diverse-multilingual-synthetic-documents-for-/).

[Explore the project portfolio](/projects/) · [Browse all publications](/publications/) · [Patents](/patents/)

## Research Community and Background

I contribute to workshop organizing for [GRAIL-V at CVPR 2026](https://grailworkshops.github.io/speakers/#workshop-organizers), [SURGeLLM at ACL 2026](https://surgellm.github.io/acl2026/organizers/), and [DocInsights at EMNLP 2026](https://docinsights-workshop.github.io/docinsights-2026/organizers/). I also mentor emerging researchers and practitioners and share work through [talks](/talks/) and open-source collaboration.

I hold a **Master’s in Machine Learning & AI from Liverpool John Moores University**. Outside work, I enjoy paragliding and scuba diving.

For research collaborations, technical leadership opportunities, or a conversation about applied AI, [get in touch](mailto:amit.pinaki@gmail.com). My [CV](/cv/) provides the broader career and publication context.
