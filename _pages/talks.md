---
permalink: /talks/
title: "Talks"
layout: single
author_profile: true
classes: wide
search: true
---

<style>
/* --- Talks grid cards --- */
.talks-group { margin: 1.5rem 0 2.25rem; }
.talks-group > h2 { margin: 0 0 .25rem 0; }
.talks-group > h3 {
  margin: .25rem 0 1rem 0;
  font-weight: 600; color: rgba(0,0,0,.66);
}
html.theme-dark .talks-group > h3 { color: #aab2bf; }

.talks-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1rem;
}
@media (max-width: 1100px) { .talks-grid { grid-template-columns: repeat(2, minmax(0,1fr)); } }
@media (max-width: 720px)  { .talks-grid { grid-template-columns: 1fr; } }

.talk-card{
  background: rgba(255,255,255,.8);
  border: 1px solid rgba(0,0,0,.08);
  border-radius: 14px;
  padding: .75rem;
  transition: box-shadow .15s ease, transform .15s ease;
}
.talk-card:hover{ box-shadow: 0 10px 25px rgba(0,0,0,.08); transform: translateY(-2px); }
html.theme-dark .talk-card{ background: #0b1220; border-color: #1f2937; }

.talk-thumb{
  display:block; overflow:hidden; border-radius: 10px;
  aspect-ratio: 16/9; background:#eee;
}
.talk-thumb img{
  width:100%; height:100%; object-fit: cover; display:block;
}
html.theme-dark .talk-thumb{ background:#0f172a; }

.talk-title{ margin:.6rem 0 .25rem 0; font-size: 1.05rem; line-height:1.25; }
.talk-meta{ margin:0 0 .5rem 0; font-size:.92rem; opacity:.8; }

.talk-pills{ display:flex; flex-wrap:wrap; gap:.5rem; margin-top:.25rem; }
/* reuse your link-pill classes; small size variant for cards */
.talk-pills .link-pill{ padding:.2rem .6rem; font-size:.9rem; }
</style>

{% comment %}
We expect each talk file in _talks/ to have at least:
---
title: "...",
venue: "EMNLP" | "COLING" | "IEEE MIPR" | "ICDMAI" | ...,
year: 2025,
role: "Invited talk" | "Panel" | "...",   # optional
pdf_url: /files/talks/whatever.pdf       # optional
link_url: https://event-program...       # optional
images:
  - /images/talks/cover.jpg               # first image is used as card cover
---
Body content (optional, for the detail page)
{% endcomment %}

{% assign all = site.talks | sort: "year" | reverse %}

{% assign by_venue = all | group_by: "venue" %}

{% for vg in by_venue %}
  {% assign venue_name = vg.name %}
  {% assign venue_items = vg.items | sort: "year" | reverse %}
  {% assign by_year = venue_items | group_by: "year" %}

  {% for yg in by_year %}
  <section class="talks-group">
    <h2 id="{{ venue_name | slugify }}">{{ venue_name }}</h2>
    <h3>{{ yg.name }}</h3>

    <div class="talks-grid">
      {% for t in yg.items %}
      <article class="talk-card">
        <a class="talk-thumb" href="{{ t.url | relative_url }}">
          {% assign cover = t.images | first %}
          {% if cover %}
            <img src="{{ cover | relative_url }}" alt="{{ t.title | escape }}">
          {% endif %}
        </a>

        <h4 class="talk-title"><a href="{{ t.url | relative_url }}">{{ t.title }}</a></h4>
        {% if t.role %}
          <p class="talk-meta">{{ t.role }}</p>
        {% endif %}

        <div class="talk-pills">
          {% if t.pdf_url %}
            <a class="link-pill" href="{{ t.pdf_url | relative_url }}" target="_blank" rel="noopener">PDF</a>
          {% endif %}
          {% if t.link_url %}
            <a class="link-pill" href="{{ t.link_url }}" target="_blank" rel="noopener">Event</a>
          {% endif %}
        </div>
      </article>
      {% endfor %}
    </div>
  </section>
  {% endfor %}
{% endfor %}
