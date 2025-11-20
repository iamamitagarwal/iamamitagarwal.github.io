---
permalink: /talks/
title: "Talks"
layout: single
author_profile: true
classes: wide
search: true
---

<div id="talk-filters" style="margin:.5rem 0 1rem 0;">
  <button class="btn btn--primary" data-tag="all">All</button>
  <button class="btn" data-tag="Invited">Invited</button>
  <button class="btn" data-tag="Panel">Panel</button>
  <button class="btn" data-tag="Tutorial">Tutorial</button>
</div>

{% assign groups = site.talks | sort: "year" | reverse | group_by: "year" %}
{% for y in groups %}
### {{ y.name }}
<ul class="talk-list">
{% for t in y.items %}
  <li class="talk-item" data-tags="{{ t.tags | join: ' ' }}">
    <strong><a href="{{ t.url | relative_url }}">{{ t.title }}</a></strong><br/>
    <em>{{ t.event }}</em>{% if t.role %} · {{ t.role }}{% endif %}{% if t.year %} ({{ t.year }}){% endif %}<br/>
    <div class="link-pills">
      {% if t.slides %}{% for s in t.slides %}<a class="link-pill" href="{{ s }}" target="_blank">📑 Slides</a>{% endfor %}{% endif %}
    </div>
  </li>
{% endfor %}
</ul>
{% endfor %}

<script>
  const tbtns = document.querySelectorAll('#talk-filters .btn');
  const titems = document.querySelectorAll('.talk-item');
  tbtns.forEach(b => b.addEventListener('click', () => {
    tbtns.forEach(x => x.classList.remove('btn--primary'));
    b.classList.add('btn--primary');
    const tag = b.dataset.tag;
    titems.forEach(li => {
      const tags = (li.dataset.tags || '').split(' ');
      li.style.display = (tag === 'all' || tags.includes(tag)) ? '' : 'none';
    });
  }));
</script>
