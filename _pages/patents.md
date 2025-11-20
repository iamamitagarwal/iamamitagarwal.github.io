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
  <button class="btn" data-tag="LLM">LLM</button>
  <button class="btn" data-tag="Retrieval">Retrieval</button>
  <button class="btn" data-tag="Document-AI">Document-AI</button>
  <button class="btn" data-tag="Safety">Safety</button>
  <button class="btn" data-tag="Systems">Systems</button>
</div>

{% assign pats = site.patents | sort: "year" | reverse %}
{% assign years = "" | split: "" %}
{% for p in pats %}{% unless years contains p.year %}{% assign years = years | push: p.year %}{% endunless %}{% endfor %}

{% for yr in years %}
  {% assign in_year = pats | where: "year", yr %}
  {% if in_year.size > 0 %}
  <section class="year-block" data-year="{{ yr }}">
    <h3 class="year-head">{{ yr }}</h3>
    <ul class="pat-list">
      {% for p in in_year %}
      <li class="pat-item" data-tags="{{ p.tags | join: ' ' }}">
        <strong>{{ p.title }}</strong><br/>
        <em>{{ p.inventors }}</em>{% if p.assignee %}. {{ p.assignee }}{% endif %}{% if p.status %} — {{ p.status }}{% endif %}{% if p.year %} ({{ p.year }}){% endif %}.
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
      document.querySelector(`#pat-filters .btn[data-tag="${tag}"]`)?.classList.add('btn--primary');
      updateYears();
    }
    btns.forEach(b => b.addEventListener('click', () => setActive(b.dataset.tag)));
    updateYears(); // initial cleanup
  })();
</script>
