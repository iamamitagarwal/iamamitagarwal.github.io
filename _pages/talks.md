---
permalink: /talks/
title: "Talks"
layout: single
classes: wide
description: "Invited talks, presentations, and workshops across AI, evaluation, and document understanding."
tags: ["Talks", "Workshops", "Presentations", "AI"]
keywords: ["Talks", "Workshops", "Presentations", "AI", "LLM", "Evaluation", "RAG", "Agentic AI", "Multimodal", "Multilingual"]
---

<p class="lead">Recorded talks, panel participation, and workshop appearances, with linked material where it is available.</p>

{% assign talks = site.talks | sort: "year" | reverse %}
<ol class="archive-list">
  {% for talk in talks %}
    {% assign event_url = talk.link_url | default: talk.event_url | default: talk.website | default: talk.site_url | default: "" %}
    {% assign pdf_url = talk.pdf_url | default: "" %}
    {% assign paper_link = talk.pub_url | default: "" %}
    {% if paper_link == "" and talk.pub_slug %}
      {% assign paper_match = site.publications | where_exp: "paper", "paper.url contains talk.pub_slug" | first %}
      {% if paper_match %}{% assign paper_link = paper_match.url | relative_url %}{% endif %}
    {% elsif paper_link == "" and talk.pub_title %}
      {% assign paper_match = site.publications | where: "title", talk.pub_title | first %}
      {% if paper_match %}{% assign paper_link = paper_match.url | relative_url %}{% endif %}
    {% endif %}
  <li class="archive-entry">
    <article>
      <div class="section-head">
        <h2><a href="{{ talk.url | relative_url }}">{{ talk.title | escape }}</a></h2>
        <p class="meta">{% if talk.date %}<time datetime="{{ talk.date | date: '%Y-%m-%d' }}">{{ talk.date | date: "%Y-%m-%d" }}</time>{% else %}{{ talk.year }}{% endif %} · {{ talk.venue }}</p>
      </div>
      <div class="link-row">
        {% if event_url != "" %}
        <a class="text-link" href="{{ event_url }}" target="_blank" rel="noopener">Event link</a>
        {% endif %}
        {% if pdf_url != "" %}
        <a class="text-link" href="{{ pdf_url | relative_url }}" target="_blank" rel="noopener">PDF</a>
        {% endif %}
        {% if paper_link != "" %}
        <a class="text-link" href="{{ paper_link }}">Related paper</a>
        {% endif %}
      </div>
      {% if talk.images %}
      <div class="media-grid">
        {% for image in talk.images %}
        <figure class="media-card">
          <a href="{{ image | relative_url }}" target="_blank" rel="noopener" aria-label="Open full image for {{ talk.title | escape }}">
            <img class="media-image" src="{{ image | relative_url }}" alt="" loading="lazy">
          </a>
          <figcaption class="media-caption">{{ talk.venue }} · {{ talk.year }}</figcaption>
        </figure>
        {% endfor %}
      </div>
      {% endif %}
    </article>
  </li>
  {% endfor %}
</ol>
