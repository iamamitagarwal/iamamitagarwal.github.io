---
permalink: /publications/
title: "Publications"
layout: single
author_profile: true
classes: wide
search: true
---

<style>
/* ===== venue badge palette ===== */
.venue-badge{display:inline-flex;align-items:center;gap:.35rem;
  padding:.18rem .55rem;border-radius:999px;font-weight:800;font-size:.75rem;
  text-transform:uppercase;letter-spacing:.02em;border:1px solid transparent}
.vb-acl{background:#fde68a;color:#713f12;border-color:#f59e0b}
.vb-emnlp{background:#d9f99d;color:#365314;border-color:#84cc16}
.vb-naacl{background:#bae6fd;color:#0c4a6e;border-color:#38bdf8}
.vb-eacl{background:#f5d0fe;color:#6b21a8;border-color:#e879f9}
.vb-coling{background:#cffafe;color:#164e63;border-color:#67e8f9}
.vb-tacl{background:#fef3c7;color:#7c2d12;border-color:#fbbf24}
.vb-cl{background:#ede9fe;color:#4c1d95;border-color:#c4b5fd}
.vb-ieee{background:#dbeafe;color:#1e3a8a;border-color:#60a5fa}
.vb-acm{background:#bbf7d0;color:#065f46;border-color:#34d399}
.vb-openreview{background:#f5f5f4;color:#292524;border-color:#d6d3d1}
.vb-springer{background:#e0e7ff;color:#3730a3;border-color:#a5b4fc}
.vb-arxiv{background:#fecaca;color:#7f1d1d;border-color:#f87171}
.vb-generic{background:#e5e7eb;color:#111827;border-color:#d1d5db}

/* link pills */
.link-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin:.35rem 0 0}
.link-pill{display:inline-flex;align-items:center;gap:.4rem;padding:.25rem .7rem;border-radius:999px;font-weight:700;border:1px solid var(--brand-accent,#0ea5e9);text-decoration:none}
.link-pill:hover{background:var(--brand-accent,#0ea5e9);color:#fff}
.pill--pdf{border-color:#ef4444}.pill--pdf:hover{background:#ef4444;color:#fff}
.pill--code{border-color:#16a34a}.pill--code:hover{background:#16a34a;color:#fff}

/* authors highlight + list styling */
.me-emph{font-weight:800}
.year-head{margin:.75rem 0 .25rem}
.pub-item{padding:.4rem .55rem;border-radius:.5rem}
.pub-item:hover{background:rgba(14,165,233,.06)}
html.theme-dark .pub-item:hover{background:#0b1220}
</style>

<div id="pub-filters" style="margin:.5rem 0 1rem 0;">
  <button class="btn btn--primary" data-tag="all">All</button>
  <button class="btn" data-tag="Document-AI">Document-AI</button>
  <button class="btn" data-tag="LLM">LLM</button>
  <button class="btn" data-tag="ML">ML</button>
  <button class="btn" data-tag="Retrieval">Retrieval</button>
  <button class="btn" data-tag="Safety">Safety</button>
  <button class="btn" data-tag="Systems">Systems</button>
  <button class="btn" data-tag="Vision-Language">Vision-Language</button>
</div>

{% assign pubs = site.publications | sort: "year" | reverse %}

/* build distinct year list */
{% assign years = "" | split: "" %}
{% for p in pubs %}
  {% unless years contains p.year %}{% assign years = years | push: p.year %}{% endunless %}
{% endfor %}

{% for yr in years %}
  {% assign in_year = pubs | where: "year", yr %}
  {% if in_year.size > 0 %}
  <section class="year-block" data-year="{{ yr }}">
    <h3 class="year-head">{{ yr }}</h3>
    <ul class="pub-list">

      {%- comment -%} PASS 1: first-author = starts with "Agarwal, Amit" {%- endcomment -%}
      {% for p in in_year %}
        {% assign auth_lc = p.authors | downcase | strip %}
        {% assign starts_me = auth_lc | slice: 0, 13 %}
        {% if starts_me == 'agarwal, amit' %}
          {% include publication_row.html pub=p %}
        {% endif %}
      {% endfor %}

      {%- comment -%} PASS 2: everyone else {%- endcomment -%}
      {% for p in in_year %}
        {% assign auth_lc = p.authors | downcase | strip %}
        {% assign starts_me = auth_lc | slice: 0, 13 %}
        {% unless starts_me == 'agarwal, amit' %}
          {% include publication_row.html pub=p %}
        {% endunless %}
      {% endfor %}

    </ul>
  </section>
  {% endif %}
{% endfor %}

<script>
(function(){
  const btns  = document.querySelectorAll('#pub-filters .btn');
  const items = Array.from(document.querySelectorAll('.pub-item'));
  const blocks= Array.from(document.querySelectorAll('.year-block'));
  function updateYears(){
    blocks.forEach(b=>{
      const vis = Array.from(b.querySelectorAll('.pub-item')).some(li => li.style.display !== 'none');
      b.style.display = vis ? '' : 'none';
    });
  }
  function setActive(tag){
    items.forEach(li=>{
      const tags = (li.dataset.tags || '').split(/\s+/).filter(Boolean);
      li.style.display = (tag === 'all' || tags.includes(tag)) ? '' : 'none';
    });
    btns.forEach(x=>x.classList.remove('btn--primary'));
    document.querySelector(`#pub-filters .btn[data-tag="${tag}"]`)?.classList.add('btn--primary');
    updateYears();
  }
  btns.forEach(b => b.addEventListener('click', () => setActive(b.dataset.tag)));
  updateYears();
})();
</script>
