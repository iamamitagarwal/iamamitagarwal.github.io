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
.pub-list li{ font-size:.95rem; line-height:1.35; }
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

<div id="pub-filters" style="margin:.5rem 0 1rem 0;">
  <button class="btn btn--primary" data-tag="all">All</button>
  {% for t in pub_tags %}
    <button class="btn" data-tag="{{ t }}">{{ t }}</button>
  {% endfor %}
</div>

{%- comment -%} Build distinct year list {%- endcomment -%}
{% assign years = "" | split: "" %}
{% for p in pubs %}
  {% unless years contains p.year %}
    {% assign years = years | push: p.year %}
  {% endunless %}
{% endfor %}

{% for yr in years %}
  {% assign in_year = pubs | where: "year", yr %}

  {%- comment -%} Agarwal-first ordering within the year {%- endcomment -%}
  {% assign agarwal_first = "" | split: "" %}
  {% assign others = "" | split: "" %}
  {% for p in in_year %}
    {% assign first_author = p.authors | split: ";" | first | strip %}
    {% assign fa_lower = first_author | downcase %}
    {% if first_author contains "Agarwal, Amit" or first_author contains "Amit Agarwal" or (fa_lower contains "amit" and fa_lower contains "agarwal") %}
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
    updateYears();
  })();
</script>
