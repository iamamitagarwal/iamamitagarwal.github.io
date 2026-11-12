---
permalink: /workshops/
title: "Workshop Organizing"
seo_title: "Amit Agarwal — Workshop Organizing"
layout: single
classes: wide
description: "Amit Agarwal's workshop organizing across vision-language AI, structured-data LLMs, and document intelligence at CVPR, ACL, and EMNLP 2026."
tags: ["Workshops", "Organizing", "Amit Agarwal", "AI Research"]
keywords: ["Amit Agarwal", "Workshop Organizer", "GRAIL-V", "SURGeLLM", "DocInsights", "CVPR 2026", "ACL 2026", "EMNLP 2026"]
---

<p class="lead">I serve as a lead organizer for GRAIL-V at CVPR, SURGeLLM at ACL, and DocInsights at EMNLP.</p>

{% assign workshops = site.data.workshops %}
<ol class="archive-list">
  {% for workshop in workshops %}
    {% assign workshop_url = workshop.url | default: "" %}
    {% assign organizer_url = workshop.organizers_url | default: "" %}
  <li class="archive-entry">
    <article>
      <div class="section-head">
        <h2><a href="{{ workshop.local_url | relative_url }}">{{ workshop.title | escape }}</a></h2>
        <p class="meta">
          {% if workshop.date %}<time datetime="{{ workshop.date }}">{{ workshop.date | date: "%Y-%m-%d" }}</time>{% else %}{{ workshop.year }}{% endif %}
          · {{ workshop.venue }} · {{ workshop.role }}
        </p>
      </div>
      <div class="link-row">
        <a class="text-link" href="{{ workshop.local_url | relative_url }}">Workshop overview</a>
        {% if workshop_url != "" and workshop_url != organizer_url %}
        <a class="text-link" href="{{ workshop_url }}" target="_blank" rel="noopener">Official workshop site</a>
        {% endif %}
        {% if organizer_url != "" %}
        <a class="text-link" href="{{ organizer_url }}" target="_blank" rel="noopener">Organizer listing</a>
        {% endif %}
      </div>
    </article>
  </li>
  {% endfor %}
</ol>

<p class="link-row"><a class="text-link" href="{{ '/projects/' | relative_url }}">Research stories</a><a class="text-link" href="{{ '/publications/' | relative_url }}">Publications</a></p>
