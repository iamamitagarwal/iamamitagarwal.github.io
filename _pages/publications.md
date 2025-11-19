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
  {% assign all_tags = site.publications | map:'tags' | join:',' | split:',' | uniq | sort %}
  {% for t in all_tags %}{% unless t == '' %}
    <button class="btn" data-tag="{{ t | strip }}">{{ t | strip }}</button>
  {% endunless %}{% endfor %}
</div>

{% comment %} robust grouping; drop items with blank year {% endcomment %}
{% assign pubs = site.publications | where_exp:'p','p.title' | where_exp:'p','p.year' | sort:'year' | reverse %}
{% assign years = pubs | map:'year' | uniq %}

{% for y in years %}
### {{ y }}
<ul class="pub-list">
{% for p in pubs %}{% if p.year == y %}
  <li class="pub-item" data-tags="{{ p.tags | join:' ' }}">
    <strong>{{ p.title }}</strong><br>
    {% if p.authors %}<em>{{ p.authors }}</em>.{% endif %}
    {% if p.venue %} {{ p.venue }}{% endif %}{% if p.year %} ({{ p.year }}){% endif %}.
    {% if p.paper_url %} <a href="{{ p.paper_url }}">Paper</a>{% endif %}
    {% if p.pdf_url %} · <a href="{{ p.pdf_url }}">PDF</a>{% endif %}
    {% if p.code_url %} · <a href="{{ p.code_url }}">Code</a>{% endif %}
  </li>
{% endif %}{% endfor %}
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
      const tags = (li.dataset.tags || '').split(' ').filter(Boolean);
      li.style.display = (tag === 'all' || tags.includes(tag)) ? '' : 'none';
    });
  }));
</script>
