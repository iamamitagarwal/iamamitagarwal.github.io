---
permalink: /patents/
title: "Patents"
layout: single
author_profile: true
classes: wide
search: true
---

<div id="pat-filters" style="margin:.5rem 0 1rem 0;">
  <button class="btn btn--primary" data-tag="all">All</button>
  {% assign all_tags = site.patents | map:'tags' | join:',' | split:',' | uniq | sort %}
  {% for t in all_tags %}{% unless t == '' %}
    <button class="btn" data-tag="{{ t | strip }}">{{ t | strip }}</button>
  {% endunless %}{% endfor %}
</div>

{% assign pats = site.patents | where_exp:'p','p.title' | where_exp:'p','p.year' | sort:'year' | reverse %}
{% assign years = pats | map:'year' | uniq %}

{% for y in years %}
<h3 class="year-heading" data-year="{{ y }}">{{ y }}</h3>
<ul class="pub-list">
{% for p in pats %}{% if p.year == y %}
  <li class="pub-item" data-tags="{{ p.tags | join:' ' }}">
    <strong><a href="{{ p.url | relative_url }}">{{ p.title }}</a></strong><br>
    {% if p.inventors %}<em>{{ p.inventors }}</em>.{% endif %}
    {% if p.office %} {{ p.office }}{% endif %}{% if p.number %} — {{ p.number }}{% endif %}{% if p.year %} ({{ p.year }}){% endif %}.
    {% if p.patent_url %} <a href="{{ p.patent_url }}">Patent</a>{% endif %}
  </li>
{% endif %}{% endfor %}
</ul>
{% endfor %}

<script>
  const btns = document.querySelectorAll('#pat-filters .btn');
  const applyFilter = (tag) => {
    const items = [...document.querySelectorAll('.pub-item')];
    const years = [...document.querySelectorAll('.year-heading')];
    items.forEach(li => {
      const tags = (li.dataset.tags || '').split(' ').filter(Boolean);
      li.style.display = (tag === 'all' || tags.includes(tag)) ? '' : 'none';
    });
    years.forEach(h => {
      const list = h.nextElementSibling;
      const visible = [...list.children].some(ch => ch.style.display !== 'none');
      h.style.display = visible ? '' : 'none';
      list.style.display = visible ? '' : 'none';
    });
  };
  btns.forEach(b => b.addEventListener('click', () => {
    btns.forEach(x => x.classList.remove('btn--primary'));
    b.classList.add('btn--primary');
    applyFilter(b.dataset.tag);
  }));
  applyFilter('all');
</script>
