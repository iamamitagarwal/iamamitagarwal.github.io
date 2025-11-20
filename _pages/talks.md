
---
permalink: /talks/
title: "Talks"
layout: single
author_profile: true
classes: wide
search: true
---

<div id="talk-tabs" style="margin:.5rem 0 1rem 0;">
  <button class="btn btn--primary" data-tab="all">All</button>
</div>



{% assign grouped = site.talks | sort: "year" | reverse | group_by: "venue" %}
{% for g in grouped %}
## {{ g.name }}
  {% assign by_year = g.items | sort: "year" | reverse | group_by: "year" %}
  {% for y in by_year %}
### {{ y.name }}
<ul class="talk-list">
  {% for t in y.items %}
  <li class="talk-item">
    <strong><a href="{{ t.url | relative_url }}">{{ t.title }}</a></strong>
    {% if t.pdf_url %}
      <div class="link-pills">
        {% if t.pdf_url contains '.pdf' %}
          <a class="link-pill pill--pdf" href="{{ t.pdf_url }}">PDF</a>
        {% else %}
          {% for p in t.pdf_url %}<a class="link-pill pill--pdf" href="{{ p }}">PDF</a>{% endfor %}
        {% endif %}
      </div>
    {% endif %}
    {% if t.images %}
      <div class="talk-thumbs">
        {% for img in t.images %}
          <a href="{{ t.url | relative_url }}"><img src="{{ img }}" alt="{{ t.title }}" /></a>
        {% endfor %}
      </div>
    {% endif %}
  </li>
  {% endfor %}
</ul>
  {% endfor %}
{% endfor %}

<style>
.talk-list{ list-style:none; margin:0; padding:0; }
.talk-item{ padding: .8rem 0; border-bottom: 1px solid rgba(0,0,0,.08); }
.talk-item:last-child{ border-bottom:0; }
.talk-thumbs{ display:flex; gap:.6rem; margin-top:.35rem; flex-wrap:wrap; }
.talk-thumbs img{ width:260px; height:auto; border-radius:.5rem; border:1px solid rgba(0,0,0,.08); }
html.theme-dark .talk-item{ border-color:#1f2937; }
html.theme-dark .talk-thumbs img{ border-color:#1f2937; }
</style>
