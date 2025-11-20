---
permalink: /media/
title: "Media"
layout: single
author_profile: true
classes: wide
search: true
---

{% assign items = site.media | sort: "year" | reverse | group_by: "year" %}
{% for y in items %}
### {{ y.name }}
<ul class="media-list">
{% for m in y.items %}
  <li class="media-item">
    <strong>{{ m.title }}</strong>{% if m.outlet %} — <em>{{ m.outlet }}</em>{% endif %}{% if m.year %} ({{ m.year }}){% endif %}<br/>
    <div class="link-pills">
      {% if m.url %}<a class="link-pill" href="{{ m.url }}" target="_blank">🔗 Link</a>{% endif %}
      {% if m.pdf_url %}<a class="link-pill" href="{{ m.pdf_url }}" target="_blank">📄 PDF</a>{% endif %}
    </div>
  </li>
{% endfor %}
</ul>
{% endfor %}
