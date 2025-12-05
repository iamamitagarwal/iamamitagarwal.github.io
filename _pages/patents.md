---
permalink: /patents/
title: "Patents"
layout: single
author_profile: true
classes: wide
search: true
---

<style>
/* Make dense lists a bit lighter */
.pat-list li{ font-size:.93rem; line-height:1.33; }
.year-head{ font-size:1.55rem; }
.pat-title{
  text-decoration:none;
  font-weight:600;
}
.pat-title:hover{ text-decoration:underline; }
.pat-badge{
  display:inline-flex; align-items:center;
  padding:.18rem .55rem;
  border-radius:999px;
  font-weight:700; font-size:.85rem;
  border:1px solid rgba(14,165,233,0.45);
  background:rgba(14,165,233,0.08); color:#0b1320;
  margin-left:.5rem;
}
html.theme-dark .pat-badge{
  border:1px solid rgba(34,211,238,0.55);
  background:rgba(34,211,238,0.12);
  color:#0b1220;
}
</style>

{%- comment -%}
Collect unique tags across all patents.
Works whether `tags` is an array or a string (comma/space separated).
{%- endcomment -%}
{% assign pats = site.patents | sort: "year" | reverse %}
{% assign pat_tags = "" | split: "" %}
{% for p in pats %}
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
        {% unless pat_tags contains tclean %}
          {% assign pat_tags = pat_tags | push: tclean %}
        {% endunless %}
      {% endif %}
    {% endfor %}
  {% endif %}
{% endfor %}
{% assign pat_tags = pat_tags | sort %}

{%- comment -%} Build distinct year list {%- endcomment -%}
{% assign years = "" | split: "" %}
{% for p in pats %}
  {% unless years contains p.year %}
    {% assign years = years | push: p.year %}
  {% endunless %}
{% endfor %}

<div id="pat-filters" style="margin:.5rem 0 1rem 0;">
  <button class="btn btn--primary" data-tag="all">All</button>
  {% for t in pat_tags %}
    <button class="btn" data-tag="{{ t }}">{{ t }}</button>
  {% endfor %}
</div>

<div id="pat-year-filters" style="margin:-.2rem 0 1rem 0;">
  {% assign sorted_years = years | sort | reverse %}
  <button class="btn btn--primary" data-year="all">All years</button>
  {% for y in sorted_years %}
    <button class="btn" data-year="{{ y }}">{{ y }}</button>
  {% endfor %}
</div>

<div markdown="0">
{% for yr in years %}
  {% assign in_year = pats | where: "year", yr %}
  {% if in_year.size > 0 %}
  {% assign pos0 = "" | split: "" %}
  {% assign pos1 = "" | split: "" %}
  {% assign pos2 = "" | split: "" %}
  {% assign pos3 = "" | split: "" %}
  {% assign posNone = "" | split: "" %}
  <section class="year-block" data-year="{{ yr }}">
    <h3 class="year-head">{{ yr }}</h3>
    {% for p in in_year %}
        {%- comment -%}
        Normalize data-tags for filtering (array or string).
        {%- endcomment -%}
        {% capture joined_item %}{{ p.tags | join: ' ' }}{% endcapture %}
        {% if joined_item == "" %}
          {% assign tags_attr = p.tags | replace: ',', ' ' %}
        {% else %}
          {% assign tags_attr = joined_item %}
        {% endif %}

        {% assign inv_list = p.inventors | split: "," %}
        {% assign amit_idx = 999 %}
        {% for a in inv_list %}
          {% assign a_trim = a | strip | downcase %}
          {% if a_trim contains "amit" and a_trim contains "agarwal" %}
            {% assign amit_idx = forloop.index0 %}
          {% endif %}
        {% endfor %}

        {% capture item_html %}
        <li class="pat-item" data-tags="{{ tags_attr }}" data-year="{{ p.year }}" data-bucket="{{ bucket }}">
          {% assign main_link = p.uspto_url | default: p.google_patents_url | default: p.google_patent_url | default: p.patent_url | default: p.url %}
          {% assign venue = p.venue | default: p.office | default: "" | strip %}
          <a class="pat-title" {% if main_link %}href="{{ main_link }}" target="_blank" rel="noopener"{% else %}href="#" aria-disabled="true"{% endif %}>{{ p.title }}</a>
          {% if venue and venue != "" %}
            <span class="pat-badge">{{ venue | upcase }}</span>
          {% endif %}
          <br/>
          {% assign inv_str = p.inventors | default: "" %}
          {% assign inv_html = inv_str | markdownify | remove: '<p>' | remove: '</p>' %}
          {% assign inv_hl = inv_html
            | replace: "<strong>Agarwal, Amit</strong>", "<span class='author-me'>Agarwal, Amit</span>"
            | replace: "Agarwal, Amit", "<span class='author-me'>Agarwal, Amit</span>"
            | replace: "Amit Agarwal", "<span class='author-me'>Amit Agarwal</span>" %}
          <span class="pat-authors">{{ inv_hl }}</span>{% if p.assignee %}. {{ p.assignee }}{% endif %}{% if p.status %} — {{ p.status }}{% endif %}.
          <div class="link-pills">
            {% if main_link %}
              <a class="link-pill pill--uspto" href="{{ main_link }}" target="_blank" rel="noopener">Patent</a>
            {% elsif p.title %}
              <a class="link-pill" href="https://patents.google.com/?q={{ p.title | uri_escape }}" target="_blank" rel="noopener">Search</a>
            {% endif %}
            {% if p.pdf_url %}
              <a class="link-pill pill--pdf" href="{{ p.pdf_url }}" target="_blank" rel="noopener">PDF</a>
            {% endif %}
            {% if p.bibtex %}
              <button class="link-pill pill--copy" data-bib="{{ p.bibtex | escape }}">BibTeX</button>
            {% endif %}
          </div>
        </li>
        {% endcapture %}

        {% if amit_idx == 0 %}
          {% assign pos0 = pos0 | push: item_html %}
        {% elsif amit_idx == 1 %}
          {% assign pos1 = pos1 | push: item_html %}
        {% elsif amit_idx == 2 %}
          {% assign pos2 = pos2 | push: item_html %}
        {% elsif amit_idx < 999 %}
          {% assign pos3 = pos3 | push: item_html %}
        {% else %}
          {% assign posNone = posNone | push: item_html %}
        {% endif %}
    {% endfor %}

    {% assign ordered_items = pos0 | concat: pos1 | concat: pos2 | concat: pos3 | concat: posNone %}
    <ul class="pat-list">
      {% for html in ordered_items %}
        {{ html }}
      {% endfor %}
    </ul>
  </section>
  {% endif %}
{% endfor %}
</div>

<script>
  (function(){
    const tagBtns  = document.querySelectorAll('#pat-filters .btn');
    const yearBtns = document.querySelectorAll('#pat-year-filters .btn');
    const items    = Array.from(document.querySelectorAll('.pat-item'));
    const blocks   = Array.from(document.querySelectorAll('.year-block'));

    let activeTag = 'all';
    let activeYear = 'all';

    function applyFilters(){
      items.forEach(li=>{
        const tags = (li.dataset.tags || '').split(/\s+/).filter(Boolean);
        const yr   = li.dataset.year || '';
        const tagOk  = (activeTag === 'all' || tags.includes(activeTag));
        const yearOk = (activeYear === 'all' || yr === activeYear);
        li.style.display = (tagOk && yearOk) ? '' : 'none';
      });
      blocks.forEach(b=>{
        const visible = Array.from(b.querySelectorAll('.pat-item'))
          .some(li => li.style.display !== 'none');
        b.style.display = visible ? '' : 'none';
      });
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

    applyFilters();
  })();
</script>
