---
permalink: /community/
title: "Community"
layout: single
classes: wide
description: "Workshop organizing, invited talks and research community activity from Amit Agarwal at CVPR, ACL, EMNLP and other venues."
tags: ["Community", "Workshops", "Talks", "AI Research"]
keywords: ["Amit Agarwal", "Community", "Workshop Organizer", "AI Talks", "Research Service"]
---

<p class="lead">Bringing researchers together through workshops, invited talks and conversations about AI.</p>

<section class="community-section" aria-labelledby="workshops-heading">
  <details class="community-disclosure" open>
    <summary>
      <h2 id="workshops-heading" class="community-summary-copy">Workshop organizing<span>Lead organizer at CVPR, ACL and EMNLP</span></h2>
    </summary>
    <div class="community-content">
      <p class="community-index-link"><a class="text-link" href="{{ '/workshops/' | relative_url }}">All workshops</a></p>
      <div class="community-workshops">
        {% for workshop in site.data.workshops %}
          {% case workshop.name %}
            {% when 'GRAIL-V' %}
              {% assign preview_image = site.data.media['oracleai-beyond-perception-cvpr-2026'].image %}
              {% assign preview_description = 'Grounded retrieval and agentic intelligence for vision-language.' %}
            {% when 'SURGeLLM' %}
              {% assign preview_image = site.data.media['surgellm-2026-organizers'].image %}
              {% assign preview_description = 'Understanding, retrieval, generation and evaluation over structured data.' %}
            {% when 'DocInsights' %}
              {% assign preview_image = site.data.media['docinsights-2026-organizers'].image %}
              {% assign preview_description = 'Document intelligence beyond plain text: structure, evidence and multimodal understanding.' %}
          {% endcase %}
        <a class="community-workshop" href="{{ workshop.local_url | relative_url }}">
          <img src="{{ preview_image | relative_url }}" alt="" loading="lazy" width="480" height="300">
          <h3>{{ workshop.name | escape }}</h3>
          <p class="meta">{{ workshop.venue | escape }}</p>
          <p>{{ preview_description }}</p>
          <span class="text-link">Workshop overview</span>
        </a>
        {% endfor %}
      </div>
      <p class="community-planned">I am also a lead organizer of RBD, planned for NAACL 2027. Official event details will be linked when available.</p>
    </div>
  </details>
</section>

<section class="community-section" aria-labelledby="talks-heading">
  <details class="community-disclosure" open>
    <summary>
      <h2 id="talks-heading" class="community-summary-copy">Talks and panels<span>Invited talks, panel discussions and workshop appearances</span></h2>
    </summary>
    <div class="community-content">
      <p class="community-index-link"><a class="text-link" href="{{ '/talks/' | relative_url }}">All talks and event materials</a></p>
      <ol class="community-talks">
        {% assign talks = site.talks | sort: 'year' | reverse %}
        {% for talk in talks %}
        <li>
          <a class="community-talk" href="{{ talk.url | relative_url }}">
            {% if talk.images.first %}<img src="{{ talk.images.first | relative_url }}" alt="" loading="lazy" width="168" height="120">{% endif %}
            <span class="community-talk-copy"><strong>{{ talk.title | escape }}</strong><span>Event details{% if talk.pdf_url %}, PDF{% endif %}{% if talk.images %} and photos{% endif %}</span></span>
          </a>
        </li>
        {% endfor %}
      </ol>
    </div>
  </details>
</section>
