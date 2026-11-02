---
permalink: /
title: "Amit Agarwal — Applied AI Research & Leadership"
seo_title: "Amit Agarwal — Enterprise AI, Multimodal Models & Evaluation"
layout: single
author_profile: true
classes: wide profile-overview
description: "Amit Agarwal, Senior Principal Applied Scientist at Oracle: enterprise AI agents, multimodal models, retrieval and evaluation."
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

I’m **Amit Agarwal**, a **Senior Principal Applied Scientist at Oracle Cloud Infrastructure**, with **10+ years across enterprise AI, research, and product development**. I build applied-science teams and lead work from research and architecture through evaluation and product integration, staying hands-on alongside science, engineering, and product teams.

[Research](/publications/) · [Projects](/projects/) · [CV](/cv/) · [Contact](mailto:amit.pinaki@gmail.com)

## Research Highlights
{% assign highlighted_pubs = site.publications | where: "highlight", true | sort: "highlight_rank" %}
<div class="research-highlights">
  {% for p in highlighted_pubs %}
  <article class="research-highlight research-highlight--{{ p.recognition_type | default: 'highlight' }}">
    <p class="research-highlight__recognition">{{ p.recognition }}</p>
    <h3><a href="{{ p.url | relative_url }}" title="{{ p.title }}">{{ p.home_highlight_title | default: p.title }}</a></h3>
    {% if p.home_highlight_summary %}<p class="research-highlight__summary">{{ p.home_highlight_summary }}</p>{% endif %}
  </article>
  {% endfor %}
</div>

## Enterprise AI Systems

### Agents & Automation

Tool-using agents for enterprise workflows, with current research on long-horizon tasks, feedback loops, multimodal agents, and shared memory.

[Read the agent systems perspective](/projects/agentic-knowledge-systems/).

### Search & Knowledge Systems

Enterprise search, multilingual retrieval, ranking, and RAG with access-aware grounding. Research includes [hard-negative mining](/publications/2025-hard-negative-mining-for-domain-specific-retrieval-in-enterprise-systems/) and [multilingual model alignment](/publications/2025-aligning-llms-for-multilingual-consistency-in-enterprise-applications/).

[Read the retrieval perspective](/projects/enterprise-retrieval/).

### Multimodal & Document Intelligence

Reasoning across text, images, video, and structured data, including document understanding, information extraction, and multimodal grounding.

### Evaluation & Responsible AI

Benchmarks, metrics, and evaluation harnesses that turn failure analysis into technical decisions, examining robustness, context sensitivity, multilingual consistency, and disability and cultural biases.

[Read the evaluation perspective](/projects/multimodal-evaluation/).

## Research to Product

- **Oracle Fusion ERP and Oracle AI Database 26ai:** Owned applied-science contributions to multimodal and agentic enablement, spanning multimodal RAG, embedding fusion, image understanding, and text-to-image capabilities with product engineering.
- **Oracle Support:** Current work on agents and knowledge systems for cloud-console assistance, ticket triage, and DevOps incident resolution, with Agent Hub routing, skill/tool retrieval, and shared context and memory.
- **Personalized leadership coaching:** Developed an agent pilot combining assessment-driven plans, persistent memory, retrieval-grounded recommendations, role-play practice, and proactive nudges.
- **Earlier work:** Led computer vision and document understanding at Jio Platforms, and built search, NLP, and recommendation systems at Abzooba.

[Explore the project portfolio](/projects/) · [Related patents](/patents/)

## Research Community and Background

I serve as a lead workshop organizer for [GRAIL-V at CVPR 2026](https://grailworkshops.github.io/speakers/#workshop-organizers), [SURGeLLM at ACL 2026](https://surgellm.github.io/acl2026/organizers/), and [DocInsights at EMNLP 2026](https://docinsights-workshop.github.io/docinsights-2026/organizers/). I also mentor emerging researchers and practitioners and share work through [talks](/talks/) and open-source collaboration.

I hold a **Master’s in Machine Learning & AI from Liverpool John Moores University**. Outside work, I enjoy paragliding and scuba diving.

For research collaborations, technical leadership opportunities, or a conversation about applied AI, [get in touch](mailto:amit.pinaki@gmail.com).
