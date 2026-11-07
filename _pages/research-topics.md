---
permalink: /research-topics/
title: "Research Topics"
seo_title: "Amit Agarwal — Research Topics, Papers and Patents"
last_modified_at: 2026-11-06
layout: single
author_profile: true
classes: wide research-topics
search: true
description: "Browse research papers and patent records by topic, from document intelligence and retrieval to multilingual, multimodal, and responsible AI."
---

{% assign paper_total = 0 %}
{% assign patent_total = 0 %}
{% for topic in site.data.research_topics %}
  {% assign paper_total = paper_total | plus: topic.publications.size %}
  {% assign patent_total = patent_total | plus: topic.patents.size %}
{% endfor %}

Explore my **{{ paper_total }} research papers** and **{{ patent_total }} patent records**, organized around the problems they address. Follow a title for its authors, abstract or summary, and original source.

<nav aria-label="Research topics"><ul>{% for topic in site.data.research_topics %}<li><a href="#{{ topic.slug }}">{{ topic.title }}</a></li>{% endfor %}</ul></nav>

{% for topic in site.data.research_topics %}
<section class="research-topic" id="{{ topic.slug | escape }}">
  <h2>{{ topic.title | escape }}</h2>
  <p>{{ topic.description | escape }}</p>

  {% if topic.publications.size > 0 %}
  <h3>Papers ({{ topic.publications.size }})</h3>
  <ul>
    {% for paper_slug in topic.publications %}
      {% assign paper_matches = site.publications | where: "slug", paper_slug %}
      {% assign paper = paper_matches | first %}
      {% if paper %}
      <li>
        <a href="{{ paper.url | relative_url }}">{{ paper.title | escape }}</a>
        {% if paper.year %}<span class="research-topic__meta">({{ paper.year }}{% if paper.venue %}; {{ paper.venue | escape }}{% endif %})</span>{% endif %}
      </li>
      {% else %}
      <li class="research-topic__missing">Unresolved paper record: {{ paper_slug | escape }}</li>
      {% endif %}
    {% endfor %}
  </ul>
  {% endif %}

  {% if topic.patents.size > 0 %}
  <h3>Patent records ({{ topic.patents.size }})</h3>
  <ul>
    {% for patent_slug in topic.patents %}
      {% assign patent_matches = site.patents | where: "slug", patent_slug %}
      {% assign patent = patent_matches | first %}
      {% if patent %}
      <li>
        <a href="{{ patent.url | relative_url }}">{{ patent.title | escape }}</a>
        <span class="research-topic__meta">({{ patent.patent_url | split: "/patent/" | last | split: "/" | first }})</span>
      </li>
      {% else %}
      <li class="research-topic__missing">Unresolved patent record: {{ patent_slug | escape }}</li>
      {% endif %}
    {% endfor %}
  </ul>
  {% endif %}
</section>
{% endfor %}
