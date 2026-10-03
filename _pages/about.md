---
permalink: /
title: "Applied AI Research & Technical Leadership"
layout: single
author_profile: true
classes: wide
description: "Amit Agarwal, Principal Applied Scientist at Oracle Cloud Infrastructure, connects retrieval, agentic AI, multimodal research, and evaluation with enterprise delivery."
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

My current work focuses on **shared knowledge infrastructure, retrieval and agentic systems, multimodal and multilingual AI, and evaluation harnesses**. I bring research and engineering teams together around clear problems, meaningful comparisons, and capabilities that can be reused across applications.

[Research](/publications/) · [Projects](/projects/) · [CV and resumes](/cv/) · [Contact](mailto:amit.pinaki@gmail.com)

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

- **Enterprise retrieval:** Co-first author of [hard-negative mining research](/publications/2025-hard-negative-mining-for-domain-specific-retrieval-in-enterprise-systems/) reporting **MRR@10 of 0.64 versus 0.57** for ADORE+STAR on a cloud-services test set (ACL 2025 Industry).
- **Multilingual model development:** First author of [multilingual consistency research](/publications/2025-aligning-llms-for-multilingual-consistency-in-enterprise-applications/). In the reported study, batch-aligned preference optimization using ORPO achieved **74.9% average MGSM exact match versus 57.2%** for the Llama-3.1-70B baseline (EMNLP 2025 Industry).
- **Evaluation quality:** First-author work on [image-text metric invariance](/publications/2026-do-image-text-metrics-respect-semantic-invariances/) examines how meaning-preserving changes can alter scores and system rankings, and proposes calibration to reduce that sensitivity (ACL 2026 Findings).

## From Research to Enterprise Systems

My technical leadership combines architectural direction with hands-on implementation. I work across science and engineering to define evaluation criteria, investigate failure cases, and connect model behavior to product requirements.

Explore the problems, decisions, and evidence behind this work:

- [Enterprise retrieval: learning from hard negatives](/projects/enterprise-retrieval/) — what a domain-specific ranking study shows, and how I approach retrieval decisions.
- [Knowledge infrastructure for grounded AI agents](/projects/agentic-knowledge-systems/) — connecting retrieval, permissions, and evaluation through technical leadership.
- [Multimodal evaluation: understanding what a score measures](/projects/multimodal-evaluation/) — visual reasoning, metric robustness, and the limits of benchmark results.

- **Knowledge and agents:** Architected shared knowledge infrastructure combining knowledge graphs, multimodal and multilingual retrieval, reranking, and access-aware grounding. My current work includes governed context delivery and streaming evaluation tooling.
- **Multimodal delivery:** Co-owned multimodal RAG science for Oracle Fusion, contributing to an **image-to-text capability deployed to production in August 2025**.
- **Document intelligence:** Delivered work across OCR, layout understanding, visual question answering, and key information extraction, alongside research on graph models and synthetic document data.

## Research Community and Background

I contribute to workshop organizing for [GRAIL-V at CVPR 2026](https://grailworkshops.github.io/speakers/#workshop-organizers), [SURGeLLM at ACL 2026](https://surgellm.github.io/acl2026/organizers/), and [DocInsights at EMNLP 2026](https://docinsights-workshop.github.io/docinsights-2026/organizers/). I also mentor emerging researchers and practitioners and share work through [talks](/talks/) and open-source collaboration.

I hold a **Master’s in Machine Learning & AI from Liverpool John Moores University**. Outside work, I enjoy paragliding and scuba diving.

For research collaborations, technical leadership opportunities, or a conversation about applied AI, [get in touch](mailto:amit.pinaki@gmail.com). My [CV](/cv/) provides the broader career and publication context.
