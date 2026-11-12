---
permalink: /patents/
title: "Patents"
layout: single
classes: wide
search: true
description: "Patent portfolio covering document AI, information extraction, retrieval, and LLM systems."
tags: ["Patents", "IP", "AI", "Document AI", "Information Extraction", "LLM"]
keywords: ["Patents", "IP", "Document AI", "Information Extraction", "LLM", "Retrieval", "Enterprise AI"]
---

<p class="lead">These inventions cover document understanding, retrieval and language models. Entries distinguish granted patents from published applications and link to the patent documents.</p>

<p>Browse the <a class="text-link" href="{{ '/research-topics/' | relative_url }}">research topics</a> hub for subject groupings that connect patents with related research papers.</p>

{% assign patents = site.patents | sort: "year" | reverse %}
<ol class="archive-list">
  {% for patent in patents %}
    {% assign patent_id = patent.patent_url | split: "/patent/" | last | split: "/" | first %}
    {% assign patent_status = "Patent record" %}
    {% if patent_id contains "B2" %}
      {% assign patent_status = "Granted patent" %}
    {% elsif patent_id contains "A1" %}
      {% assign patent_status = "Published application" %}
    {% endif %}
  <li class="archive-entry">
    <article>
      <div class="section-head">
        <h2><a href="{{ patent.url | relative_url }}">{{ patent.title | escape }}</a></h2>
        <p class="meta">Priority year {{ patent.year }}</p>
      </div>
      <p class="meta">Inventors: {{ patent.inventors | escape }}</p>
      <div class="link-row">
        <span class="meta">{{ patent_status }}</span>
        <a class="text-link" href="{{ patent.patent_url }}" target="_blank" rel="noopener">{{ patent_id | escape }}</a>
      </div>
    </article>
  </li>
  {% endfor %}
</ol>
