---
permalink: /publications/
title: "Publications"
layout: single
author_profile: true
classes: wide
search: true
---

<style>
/* Slightly smaller list typography so dense years feel lighter */
  .pub-list li{ font-size:.93rem; line-height:1.33; }
.year-head{ font-size:1.55rem; }

/* Venue badge */
.venue-badge{
  display:inline-flex; align-items:center;
  padding:.14rem .6rem; margin-left:.5rem;
  border-radius:999px; font-weight:700; font-size:.8rem;
  border:1px solid transparent;
}
/* Color map */
.badge-emnlp{ background:#0d9488; color:#fff; }
.badge-acl{ background:#10b981; color:#0b1320; }
.badge-naacl{ background:#f59e0b; color:#111827; }
.badge-neurips{ background:#06b6d4; color:#0b1320; }
.badge-iclr{ background:#a78bfa; color:#111827; }
.badge-icml{ background:#22c55e; color:#0b1320; }
.badge-cvpr{ background:#60a5fa; color:#0b1320; }
.badge-iccv{ background:#3b82f6; color:#fff; }
.badge-eccv{ background:#2563eb; color:#fff; }
.badge-ieee{ background:#93c5fd; color:#0b1320; }
.badge-acm{ background:#f97316; color:#0b1320; }
.badge-arxiv{ background:#e5e7eb; color:#111827; border-color:#cbd5e1; }
html.theme-dark .badge-arxiv{ background:#374151; color:#e5e7eb; border-color:#4b5563; }
</style>

{%- comment -%}
Collect unique tags from all publications.
Handles tags stored as arrays or strings (single or comma/space separated).
{%- endcomment -%}
{% assign pubs = site.publications | sort: "year" | reverse %}
{% assign pub_tags = "" | split: "" %}
{% for p in pubs %}
  {% if p.tags %}
    {% capture joined %}{{ p.tags | join: ' ' }}{% endcapture %}
    {% assign tag_source = joined %}
    {% if tag_source == "" %}
      {% assign tag_source = p.tags %}
    {% endif %}
    {% assign tlist = tag_source | replace: ',', ' ' | split: ' ' %}
    {% for t in tlist %}
      {% assign tclean = t | strip %}
      {% if tclean != "" %}
        {% unless pub_tags contains tclean %}
          {% assign pub_tags = pub_tags | push: tclean %}
        {% endunless %}
      {% endif %}
    {% endfor %}
  {% endif %}
{% endfor %}
{% assign pub_tags = pub_tags | sort %}

{%- comment -%} Build distinct year list {%- endcomment -%}
{% assign years = "" | split: "" %}
{% for p in pubs %}
  {% unless years contains p.year %}
    {% assign years = years | push: p.year %}
  {% endunless %}
{% endfor %}

<div id="pub-filters" style="margin:.5rem 0 1rem 0;">
  <button class="btn btn--primary" data-tag="all">All</button>
  {% for t in pub_tags %}
    <button class="btn" data-tag="{{ t }}">{{ t }}</button>
  {% endfor %}
</div>

<div id="pub-year-filters" style="margin:-.2rem 0 1rem 0;">
  {% assign years_sorted = years | sort | reverse %}
  <button class="btn btn--primary" data-year="all">All years</button>
  {% for y in years_sorted %}
    <button class="btn" data-year="{{ y }}">{{ y }}</button>
  {% endfor %}
</div>

<div markdown="0">
{% for yr in years %}
  {% assign in_year = pubs | where: "year", yr %}

  {%- comment -%} Order within year by Amit Agarwal position: first, second, third+, none {%- endcomment -%}
  {% assign pos0 = "" | split: "" %}
  {% assign pos1 = "" | split: "" %}
  {% assign pos2 = "" | split: "" %}
  {% assign pos3 = "" | split: "" %}
  {% assign posNone = "" | split: "" %}

  {% for p in in_year %}
    {% assign alist = p.authors | split: "," %}
    {% assign amit_idx = 999 %}
    {% for a in alist %}
      {% assign a_trim = a | strip | downcase %}
      {% if a_trim contains "amit" and a_trim contains "agarwal" %}
        {% assign amit_idx = forloop.index0 %}
      {% endif %}
    {% endfor %}
    {% if amit_idx == 0 %}
      {% assign pos0 = pos0 | push: p %}
    {% elsif amit_idx == 1 %}
      {% assign pos1 = pos1 | push: p %}
    {% elsif amit_idx == 2 %}
      {% assign pos2 = pos2 | push: p %}
    {% elsif amit_idx < 999 %}
      {% assign pos3 = pos3 | push: p %}
    {% else %}
      {% assign posNone = posNone | push: p %}
    {% endif %}
  {% endfor %}
  {% assign ordered = pos0 | concat: pos1 | concat: pos2 | concat: pos3 | concat: posNone %}

  {% if ordered.size > 0 %}
    <section class="year-block" data-year="{{ yr }}">
      <h3 class="year-head">{{ yr }}</h3>
      <ul class="pub-list">
        {% for p in ordered %}
          {% include publication_row.html pub=p %}
        {% endfor %}
      </ul>
    </section>
  {% endif %}
{% endfor %}
</div>

<script>
  (function(){
    const tagBtns  = document.querySelectorAll('#pub-filters .btn');
    const yearBtns = document.querySelectorAll('#pub-year-filters .btn');
    const items = Array.from(document.querySelectorAll('.pub-item'));
    const blocks= Array.from(document.querySelectorAll('.year-block'));

    let activeTag  = 'all';
    let activeYear = 'all';

    function updateYears(){
      blocks.forEach(b=>{
        const vis = Array.from(b.querySelectorAll('.pub-item'))
          .some(li => li.style.display !== 'none');
        b.style.display = vis ? '' : 'none';
      });
    }

    function applyFilters(){
      items.forEach(li=>{
        const tags = (li.dataset.tags || '').split(/\s+/).filter(Boolean);
        const yr   = li.closest('.year-block')?.dataset.year || '';
        const tagOk  = (activeTag === 'all' || tags.includes(activeTag));
        const yearOk = (activeYear === 'all' || yr === activeYear);
        li.style.display = (tagOk && yearOk) ? '' : 'none';
      });
      updateYears();
    }

    function setTag(tag){
      activeTag = tag;
      tagBtns.forEach(x => x.classList.toggle('btn--primary', x.dataset.tag === tag));
      applyFilters();
    }

    function setYear(y){
      activeYear = y;
      yearBtns.forEach(x => x.classList.toggle('btn--primary', x.dataset.year === y));
      applyFilters();
    }

    tagBtns.forEach(b => b.addEventListener('click', () => setTag(b.dataset.tag)));
    yearBtns.forEach(b => b.addEventListener('click', () => setYear(b.dataset.year)));

    updateYears();
  })();
</script>
