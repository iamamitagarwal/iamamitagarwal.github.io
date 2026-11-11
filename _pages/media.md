---
permalink: /media/
title: "Media"
layout: single
classes: wide
description: "Workshop organizing, press coverage, interviews, and media features related to my research and work."
tags: ["Media", "Press", "AI"]
keywords: ["Media", "Press", "Interviews", "AI", "GenAI", "LLM"]
---

<p class="lead">Workshop organizing and media coverage related to my research and work.</p>

{% assign media_items = site.data.media %}
{% assign media_groups = "featured,archive" | split: "," %}
{% for media_group in media_groups %}
<section aria-label="{% if media_group == 'featured' %}Featured media{% else %}More media{% endif %}">
  <div class="section-head">
    <h2>{% if media_group == "featured" %}Featured{% else %}More coverage and organizing{% endif %}</h2>
  </div>
  <div class="media-grid">
    {% for pair in media_items %}
      {% assign entry_key = pair[0] %}
      {% assign entry = pair[1] %}
      {% if media_group == "featured" and entry.featured != true %}{% continue %}{% endif %}
      {% if media_group == "archive" and entry.featured == true %}{% continue %}{% endif %}

      {% assign image_url = entry.image | default: "" %}
      {% assign pdf_url = "" %}
      {% if image_url == "" %}
        {% for media_file in site.static_files %}
          {% assign media_path = media_file.path | downcase %}
          {% assign media_base = media_file.name | remove: media_file.extname %}
          {% if media_path contains "/assets/media/pictures/" and media_base == entry_key %}
            {% assign image_url = media_file.path %}
            {% break %}
          {% endif %}
        {% endfor %}
        {% for media_file in site.static_files %}
          {% assign media_path = media_file.path | downcase %}
          {% assign media_base = media_file.name | remove: media_file.extname %}
          {% assign media_ext = media_file.extname | downcase %}
          {% if media_path contains "/assets/media/pdfs/" and media_ext == ".pdf" and media_base == entry_key %}
            {% assign pdf_url = media_file.path %}
            {% break %}
          {% endif %}
        {% endfor %}
      {% endif %}

      {% if image_url != "" %}
        {% assign display_title = entry.title | default: entry_key %}
        {% assign site_url = entry.site | default: "" %}
    <figure class="media-card">
      <a href="{{ image_url | relative_url }}" target="_blank" rel="noopener" aria-label="Open full image: {{ display_title | escape }}">
        <img class="media-image" src="{{ image_url | relative_url }}" alt="" loading="lazy">
      </a>
      <figcaption class="media-caption">
        <h3>{{ display_title | escape }}</h3>
        <div class="link-row">
          {% if entry.links %}
            {% for media_link in entry.links %}
              {% assign media_link_url = media_link.url | default: "" %}
              {% if media_link_url != "" %}
                {% if media_link_url contains "://" %}
                  <a class="text-link" href="{{ media_link_url }}" target="_blank" rel="noopener">{{ media_link.label | default: "Source" }}</a>
                {% else %}
                  <a class="text-link" href="{{ media_link_url | relative_url }}">{{ media_link.label | default: "Source" }}</a>
                {% endif %}
              {% endif %}
            {% endfor %}
          {% else %}
            {% if site_url != "" %}
            <a class="text-link" href="{{ site_url }}" target="_blank" rel="noopener">Source</a>
            {% endif %}
            {% if pdf_url != "" %}
            <a class="text-link" href="{{ pdf_url | relative_url }}" target="_blank" rel="noopener">PDF</a>
            {% endif %}
          {% endif %}
        </div>
      </figcaption>
    </figure>
      {% endif %}
    {% endfor %}
  </div>
</section>
{% endfor %}
