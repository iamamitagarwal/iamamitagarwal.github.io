---
permalink: /publications/
title: "Publications"
layout: single
author_profile: true
classes: wide
search: true
---

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
      {% for p in in_year %}
      <li class="pub-item" data-tags="{{ p.tags | join: ' ' }}">
        <strong><a class="pub-title" href="{{ p.paper_url | default: p.pdf_url | default: p.url | relative_url }}">{{ p.title }}</a></strong><br/>
        <em>{{ p.authors }}</em>. {{ p.venue }}{% if p.year %} ({{ p.year }}){% endif %}.
        <div class="link-pills">
          {% if p.paper_url %}<a class="link-pill" href="{{ p.paper_url }}">📄 Paper</a>{% endif %}
          {% if p.pdf_url %}<a class="link-pill pill--pdf" href="{{ p.pdf_url }}">PDF</a>{% endif %}
          {% if p.code_url %}<a class="link-pill pill--code" href="{{ p.code_url }}">Code</a>{% endif %}
          {% if p.bibtex %}<button class="link-pill pill--copy" data-bib="{{ p.bibtex | escape }}">BibTeX</button>{% endif %}
        </div>
      </li>
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
        const visible = b.querySelectorAll('.pub-item').length &&
                        Array.from(b.querySelectorAll('.pub-item')).some(li => li.style.display !== 'none');
        b.style.display = visible ? '' : 'none';
      });
    }
    function setActive(tag){
      items.forEach(li=>{
        const tags = (li.dataset.tags || '').split(/\s+/).filter(Boolean);
        const show = (tag === 'all' || tags.includes(tag));
        li.style.display = show ? '' : 'none';
      });
      btns.forEach(x => x.classList.remove('btn--primary'));
      document.querySelector(`#pub-filters .btn[data-tag="${tag}"]`)?.classList.add('btn--primary');
      updateYears();
    }
    btns.forEach(b => b.addEventListener('click', () => setActive(b.dataset.tag)));
    updateYears(); // initial cleanup for any empty years
  })();
</script>
