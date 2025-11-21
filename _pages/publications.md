---
permalink: /publications/
title: "Publications"
layout: single
author_profile: true
classes: wide
search: true
---

<style>
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

/* Slightly smaller publication rows (keep badges/tags as-is) */
.pub-list li{ font-size:.95rem; line-height:1.35; }
.year-head{ font-size:1.55rem; }
</style>

{%- comment -%}
Build the filter buttons from the real tags across all publications.
Handles tags as arrays OR strings (single or space/comma-separated).
{%- endcomment -%}
{% assign pubs = site.publications | sort: "year" | reverse %}
{% assign tags = "" | split: "" %}
{% for p in pubs %}
  {% if p.tags %}
    {%- comment -%} Normalize to a space-separated string {%- endcomment -%}
    {% capture joined %}{{ p.tags | join: ' ' }}{% endcapture %}
    {% assign tag_source = joined %}
    {% if tag_source == "" %}
      {% assign tag_source = p.tags %}
    {% endif %}
    {% assign tlist = tag_source | replace: ',', ' ' | split: ' ' %}
    {% for t in tlist %}
      {% assign tclean = t | strip %}
      {% if tclean != "" and not tags contains tclean %}
        {% assign tags = tags | push: tclean %}
      {% endif %}
    {% endfor %}
  {% endif %}
{% endfor %}
{% assign tags = tags | sort %}

<div id="pub-filters" style="margin:.5rem 0 1rem 0;">
  <button class="btn btn--primary" data-tag="all">All</button>
  {% for t in tags %}
    <button class="btn" data-tag="{{ t }}">{{ t }}</button>
  {% endfor %}
</div>

{% comment %} Build distinct year list {% endcomment %}
{% assign years = "" | split: "" %}
{% for p in pubs %}
  {% unless years contains p.year %}
    {% assign years = years | push: p.year %}
  {% endunless %}
{% endfor %}

{% for yr in years %}
  {% assign in_year = pubs | where: "year", yr %}

  {% comment %} Order each year: first-author = "Agarwal, Amit" first, then others {% endcomment %}
  {% assign agarwal_first = "" | split: "" %}
  {% assign others = "" | split: "" %}
  {% for p in in_year %}
    {% assign first_author = p.authors | split: ";" | first | strip %}
    {% if first_author contains "Agarwal, Amit" %}
      {% assign agarwal_first = agarwal_first | push: p %}
    {% else %}
      {% assign others = others | push: p %}
    {% endif %}
  {% endfor %}
  {% assign ordered = agarwal_first | concat: others %}

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

<script>
  (function(){
    const btns  = document.querySelectorAll('#pub-filters .btn');
    const items = Array.from(document.querySelectorAll('.pub-item'));
    const blocks= Array.from(document.querySelectorAll('.year-block'));

    function updateYears(){
      blocks.forEach(b=>{
        const vis = Array.from(b.querySelectorAll('.pub-item'))
          .some(li => li.style.display !== 'none');
        b.style.display = vis ? '' : 'none';
      });
    }
    function setActive(tag){
      items.forEach(li=>{
        const tags = (li.dataset.tags || '').split(/\s+/).filter(Boolean);
        li.style.display = (tag === 'all' || tags.includes(tag)) ? '' : 'none';
      });
      btns.forEach(x => x.classList.remove('btn--primary'));
      const active = document.querySelector(`#pub-filters .btn[data-tag="${tag}"]`);
      if (active) active.classList.add('btn--primary');
      updateYears();
    }
    btns.forEach(b => b.addEventListener('click', () => setActive(b.dataset.tag)));
    updateYears(); // initial cleanup
  })();
</script>
