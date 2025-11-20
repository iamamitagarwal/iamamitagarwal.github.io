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
</div>

{% assign pats_by_year = site.patents | sort: "year" | reverse | group_by: "year" %}

{% for y in pats_by_year %}
### {{ y.name }}{:.year-head}
<ul class="pat-list">
{% for p in y.items %}
  <li class="pat-item" data-tags="{{ p.tags | join: ' ' }}">
    <strong><a href="{{ p.patent_url | default:p.uspto_url | default:'#' }}">{{ p.title }}</a></strong><br/>
    <em>{{ p.inventors }}</em>.
    {% if p.assignee %} {{ p.assignee }}.{% endif %}
    {% if p.number %} {{ p.number }}.{% endif %}
    {% if p.status %} <span class="label">{{ p.status }}</span>{% endif %}
    {% if p.year %} ({{ p.year }}){% endif %}

    {% if p.abstract %}
    <details class="pub-abs"><summary>Abstract</summary>
      <p>{{ p.abstract }}</p>
    </details>
    {% endif %}

    <div class="link-pills">
      {% if p.patent_url %}<a class="link-pill" href="{{ p.patent_url }}" target="_blank" rel="noopener"><i class="fa fa-file-alt"></i>Patent</a>{% endif %}
      {% if p.uspto_url %}<a class="link-pill pill--uspto" href="{{ p.uspto_url }}" target="_blank" rel="noopener"><i class="fa fa-university"></i>USPTO</a>{% endif %}
      {% if p.pdf_url %}<a class="link-pill pill--pdf" href="{{ p.pdf_url }}" target="_blank" rel="noopener"><i class="fa fa-file-pdf"></i>PDF</a>{% endif %}
      {% if p.bibtex %}<button class="link-pill pill--copy" type="button" data-bib="{{ p.bibtex | escape }}"><i class="fa fa-clipboard"></i>BibTeX</button>{% endif %}
    </div>
  </li>
{% endfor %}
</ul>
{% endfor %}

<script>
  // Build tag buttons and filter (same pattern as publications)
  (function(){
    const wrap = document.getElementById('pat-filters');
    const items = [...document.querySelectorAll('.pat-item')];
    const set = new Set();
    items.forEach(li => (li.dataset.tags||'').split(' ').filter(Boolean).forEach(t => set.add(t)));
    [...set].sort().forEach(tag=>{
      const b = document.createElement('button');
      b.className = 'btn'; b.textContent = tag; b.dataset.tag = tag; wrap.appendChild(b);
    });

    const buttons = wrap.querySelectorAll('button');
    const years   = [...document.querySelectorAll('.year-head')];

    function apply(tag){
      buttons.forEach(x=>x.classList.toggle('btn--primary', x.dataset.tag===tag));
      items.forEach(li=>{
        const tags = (li.dataset.tags||'').split(' ');
        li.style.display = (tag==='all' || tags.includes(tag)) ? '' : 'none';
      });
      years.forEach(h=>{
        const ul = h.nextElementSibling;
        const visible = ul && [...ul.children].some(li => li.style.display !== 'none');
        h.style.display = ul.style.display = visible ? '' : 'none';
      });
    }
    wrap.addEventListener('click', e=>{
      const b = e.target.closest('button[data-tag]'); if(!b) return;
      apply(b.dataset.tag);
    });
    apply('all');
  })();
</script>
