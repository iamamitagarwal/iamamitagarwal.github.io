---
permalink: /awards/
title: "Awards"
layout: single
author_profile: true
classes: wide
search: true
---

{% assign items = site.awards | sort: "year" | reverse | group_by: "year" %}
{% for y in items %}
{% if y.name %}
### {{ y.name }}
<ul class="awards-list">
{% for a in y.items %}
  <li class="awards-item">
    <strong>{{ a.title }}</strong>{% if a.organization %} — <em>{{ a.organization }}</em>{% endif %}{% if a.year %} ({{ a.year }}){% endif %}<br/>
    <div class="link-pills">
      {% if a.pdf_url %}<a class="link-pill" href="{{ a.pdf_url }}" target="_blank">📜 Certificate</a>{% endif %}
    </div>
  </li>
{% endfor %}
</ul>
{% endif %}
{% endfor %}
