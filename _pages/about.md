---
permalink: /
title: "Applied AI Research & Technical Leadership"
layout: single
author_profile: true
classes: wide profile-overview
description: "Amit Agarwal, Senior Principal Applied Scientist at Oracle Cloud Infrastructure, connects AI agents, search and knowledge systems, multimodal and document intelligence, and evaluation with enterprise delivery."
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

I’m **Amit Agarwal**, a **Senior Principal Applied Scientist at Oracle Cloud Infrastructure**, with **10+ years across enterprise AI, research, and product development**. I lead applied research and system development from problem definition and architecture through evaluation and product integration. I stay hands-on and bring science, engineering, and product teams together around shared technical direction, reusable capabilities, and delivery. I have built and grown applied-science teams from inception through architecture and delivery of enterprise semantic layers, personalized search and agents, and support automation.

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

## Enterprise AI Systems

### Agents & Automation

I work on tool-using agents for enterprise support and operational workflows. Current research directions include long-horizon tasks, feedback loops, multimodal agents, and shared memory—connecting evidence with useful action and evaluating progress across steps.

[Read the agent systems perspective](/projects/agentic-knowledge-systems/).

### Search & Knowledge Systems

My work spans enterprise search, multilingual retrieval, ranking, and RAG with access-aware grounding. Research includes [hard-negative mining](/publications/2025-hard-negative-mining-for-domain-specific-retrieval-in-enterprise-systems/) and [multilingual model alignment](/publications/2025-aligning-llms-for-multilingual-consistency-in-enterprise-applications/).

[Read the retrieval perspective](/projects/enterprise-retrieval/).

### Multimodal & Document Intelligence

I work on reasoning across text, images, video, and structured data, including document understanding, information extraction, and multimodal grounding. The research connects models with context and the evidence needed to interpret their outputs.

### Evaluation & Responsible AI

I develop benchmarks, metrics, and harnesses for retrieval, reasoning, agents, and multimodal systems. The work examines robustness, context sensitivity, multilingual consistency, and disability and cultural biases, helping teams turn failure analysis into technical decisions.

[Read the evaluation perspective](/projects/multimodal-evaluation/).

## Research to Product

- **Oracle Fusion ERP and Oracle AI Database 26ai:** Owned applied-science contributions to multimodal and agentic enablement, spanning multimodal RAG, embedding fusion, image understanding, and text-to-image capabilities with product engineering.
- **Enterprise knowledge infrastructure:** Architected a shared foundation for RAG and agents, combining multimodal and multilingual retrieval, ranking, and access-aware grounding.
- **Oracle Support:** Current work on agents and knowledge systems for cloud-console assistance, ticket triage, and DevOps incident resolution, with Agent Hub routing, skill/tool retrieval, and shared context and memory.
- **Personalized leadership coaching:** Developed an agent pilot combining assessment-driven plans, persistent memory, retrieval-grounded recommendations, role-play practice, and proactive nudges.
- **Document intelligence:** Research and [inventions](/patents/) in key-value extraction, synthetic training data, and adaptation across document types.
- **Jio Platforms:** Led computer-vision work spanning video analytics, detection and tracking, and OCR-based document understanding.
- **Abzooba:** Built search, NLP, and recommendation systems, with technical leadership and product ownership for financial-news recommendation and disclosure classification.

[Explore the project portfolio](/projects/) · [Browse all publications](/publications/) · [CV](/cv/)

## Research Community and Background

I serve as a lead workshop organizer for [GRAIL-V at CVPR 2026](https://grailworkshops.github.io/speakers/#workshop-organizers), [SURGeLLM at ACL 2026](https://surgellm.github.io/acl2026/organizers/), and [DocInsights at EMNLP 2026](https://docinsights-workshop.github.io/docinsights-2026/organizers/). I also mentor emerging researchers and practitioners and share work through [talks](/talks/) and open-source collaboration.

I hold a **Master’s in Machine Learning & AI from Liverpool John Moores University**. Outside work, I enjoy paragliding and scuba diving.

For research collaborations, technical leadership opportunities, or a conversation about applied AI, [get in touch](mailto:amit.pinaki@gmail.com). My [CV](/cv/) provides the broader career and publication context.
