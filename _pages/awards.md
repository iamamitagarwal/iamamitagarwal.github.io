---
permalink: /awards/
title: "Awards"
layout: single
classes: wide
description: "Awards and recognitions across research, product, and innovation."
tags: ["Awards", "Recognition", "AI"]
keywords: ["Awards", "Recognition", "AI", "Innovation"]
---

<p class="lead">Research recognition and company awards.</p>

{% assign recognized_papers = site.publications | where_exp: "paper", "paper.recognition != nil" | sort: "year" | reverse %}
{% if recognized_papers.size > 0 %}
<section aria-labelledby="research-recognition-heading">
  <div class="section-head">
    <h2 id="research-recognition-heading">Research recognition</h2>
  </div>
  <ul class="award-list">
    {% for paper in recognized_papers %}
    <li class="award-entry">
      <div>
        <h3><a class="text-link" href="{{ paper.url | relative_url }}">{{ paper.title | escape }}</a></h3>
      </div>
      <p class="meta">{{ paper.recognition | escape }}</p>
    </li>
    {% endfor %}
  </ul>
</section>
{% endif %}

{% assign awards = site.awards | sort: "year" | reverse %}
{% assign organizations = "Oracle,Abzooba" | split: "," %}
{% for organization in organizations %}
  {% assign organization_awards = awards | where: "org", organization %}
  {% if organization_awards.size > 0 %}
<section aria-labelledby="{{ organization | slugify }}">
  <div class="section-head">
    <h2 id="{{ organization | slugify }}">{{ organization }}</h2>
  </div>
  <ul class="award-list">
    {% for award in organization_awards %}
      {% assign certificate = award.certificate | default: award.pdf | default: award.certificate_url | default: "" %}
      {% assign recognition_link = award.link | default: "" %}
    <li class="award-entry">
      <div>
        <h3><a href="{{ award.url | relative_url }}">{{ award.title | escape }}</a></h3>
        <p class="meta">{{ award.year }}</p>
      </div>
      <div class="link-row">
        {% if certificate != "" %}
        <a class="text-link" href="{{ certificate | relative_url }}" target="_blank" rel="noopener">Certificate (PDF)</a>
        {% endif %}
        {% if recognition_link != "" %}
        <a class="text-link" href="{{ recognition_link }}" target="_blank" rel="noopener">Recognition details</a>
        {% endif %}
      </div>
    </li>
    {% endfor %}
  </ul>
</section>
  {% endif %}
{% endfor %}
