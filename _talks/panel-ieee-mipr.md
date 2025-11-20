---
title: "Panel  Ieee Mipr"
event: "IEEE MIPR"
role: "Panel"
layout: "single"
author_profile: true
tags: [Panel]
slides:
  - "/assets/talks/Panel- IEEE MIPR - Innovation Forums Bio.pdf"
---
{% if page.slides or page.gallery %}
<div class="link-pills">
  {% if page.slides %}{% for s in page.slides %}<a class="link-pill" href="{{ s }}" target="_blank">📑 Slides</a>{% endfor %}{% endif %}
</div>
{% if page.gallery %}
<div class="grid__wrapper" style="margin-top:.75rem">
  {% for img in page.gallery %}
  <a href="{{ img }}" class="grid__item"><img src="{{ img }}" alt=""></a>
  {% endfor %}
</div>
{% endif %}
{% endif %}
