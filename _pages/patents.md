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
.pat-list li{ font-size:.95rem; line-height:1.35; }
.year-head{ font-size:1.55rem; }
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

<div id="pat-filters" style="margin:.5rem 0 1rem 0;">
  <button class="btn btn--primary" data-tag="all">All</button>
  {% for t in pat_tags %}
    <button class="btn" data-tag="{{ t }}">{{ t }}</button>
  {% endfor %}
</div>

{%- comment -%} Build distinct year list {%- endcomment -%}
{% assign years = "" | split: "" %}
{% for p in pats %}
  {% unless years contains p.year %}
    {% assign years = years | push: p.year %}
  {% endunless %}
{% endfor %}

{% for yr in years %}
  {% assign in_year = pats | where: "year", yr %}
  {% if in_year.size > 0 %}
  <section class="year-block" data-year="{{ yr }}">
    <h3 class="year-head">{{ yr }}</h3>
    <ul class="pat-list">
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

        <li class="pat-item" data-tags="{{ tags_attr }}">
          <strong>{{ p.title }}</strong><br/>
          {% assign inv_str = p.inventors | default: "" %}
          {% assign inv_html = inv_str | markdownify | remove: '<p>' | remove: '</p>' %}
          {% assign inv_hl = inv_html
            | replace: "<strong>Agarwal, Amit</strong>", "<span class='author-me'>Agarwal, Amit</span>"
            | replace: "Agarwal, Amit", "<span class='author-me'>Agarwal, Amit</span>"
            | replace: "Amit Agarwal", "<span class='author-me'>Amit Agarwal</span>" %}
          <em>{{ inv_hl }}</em>{% if p.assignee %}. {{ p.assignee }}{% endif %}{% if p.status %} — {{ p.status }}{% endif %}{% if p.year %} ({{ p.year }}){% endif %}.
          {% assign main_link = p.uspto_url | default: p.google_patents_url | default: p.google_patent_url | default: p.patent_url | default: p.url %}
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
      {% endfor %}
    </ul>
  </section>
  {% endif %}
{% endfor %}

<script>
  (function(){
    const btns  = document.querySelectorAll('#pat-filters .btn');
    const items = Array.from(document.querySelectorAll('.pat-item'));
    const blocks= Array.from(document.querySelectorAll('.year-block'));

    function updateYears(){
      blocks.forEach(b=>{
        const visible = Array.from(b.querySelectorAll('.pat-item'))
          .some(li => li.style.display !== 'none');
        b.style.display = visible ? '' : 'none';
      });
    }
    function setActive(tag){
      items.forEach(li=>{
        const tags = (li.dataset.tags || '').split(/\s+/).filter(Boolean);
        li.style.display = (tag === 'all' || tags.includes(tag)) ? '' : 'none';
      });
      btns.forEach(x => x.classList.remove('btn--primary'));
      const active = document.querySelector(`#pat-filters .btn[data-tag="${tag}"]`);
      if (active) active.classList.add('btn--primary');
      updateYears();
    }
    btns.forEach(b => b.addEventListener('click', () => setActive(b.dataset.tag)));
    updateYears(); // initial cleanup
  })();
</script>
