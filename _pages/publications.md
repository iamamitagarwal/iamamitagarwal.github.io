---
permalink: /publications/
title: "Publications"
layout: single
author_profile: true
classes: wide
search: true
---

<div id="pub-filters" style="margin:.5rem 0 1rem 0;">
  <button class="btn btn--primary" data-tag="all">All</button>
  <button class="btn" data-tag="LLM">LLM</button>
  <button class="btn" data-tag="Retrieval">Retrieval</button>
  <button class="btn" data-tag="Safety">Safety</button>
  <button class="btn" data-tag="Document-AI">Document AI</button>
</div>

{% assign pubs_by_year = site.publications | sort: "year" | reverse | group_by: "year" %}

{% for y in pubs_by_year %}
### {{ y.name }}
<ul class="pub-list">
{% for p in y.items %}
  <li class="pub-item" data-tags="{{ p.tags | join: ' ' }}">
    <strong>{{ p.title }}</strong><br/>
    <em>{{ p.authors }}</em>. {{ p.venue }} ({{ p.year }}).<br/>
    {% if p.paper_url %}<a href="{{ p.paper_url }}">Paper</a>{% endif %}
    {% if p.pdf_url %} · <a href="{{ p.pdf_url }}">PDF</a>{% endif %}
    {% if p.code_url %} · <a href="{{ p.code_url }}">Code</a>{% endif %}
  </li>
{% endfor %}
</ul>
{% endfor %}

<script>
  const btns = document.querySelectorAll('#pub-filters .btn');
  const items = document.querySelectorAll('.pub-item');
  btns.forEach(b => b.addEventListener('click', () => {
    btns.forEach(x => x.classList.remove('btn--primary'));
    b.classList.add('btn--primary');
    const tag = b.dataset.tag;
    items.forEach(li => {
      const tags = (li.dataset.tags || '').split(' ');
      li.style.display = (tag === 'all' || tags.includes(tag)) ? '' : 'none';
    });
  }));
</script>
