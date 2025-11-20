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
</div>

{% assign pubs_by_year = site.publications | sort: "year" | reverse | group_by: "year" %}

{% for y in pubs_by_year %}
### {{ y.name }}{:.year-head}
<ul class="pub-list">
{% for p in y.items %}
  <li class="pub-item" data-tags="{{ p.tags | join: ' ' }}">
    <strong><a href="{{ p.paper_url | default:p.pdf_url | default:'#' }}">{{ p.title }}</a></strong><br/>
    <em>{{ p.authors }}</em>. {{ p.venue }}{% if p.year %} ({{ p.year }}){% endif %}.

    {% if p.abstract %}
    <details class="pub-abs"><summary>Abstract</summary>
      <p>{{ p.abstract }}</p>
    </details>
    {% endif %}

    <div class="link-pills">
      {% if p.paper_url %}<a class="link-pill" href="{{ p.paper_url }}" target="_blank" rel="noopener"><i class="fa fa-file-alt"></i>Paper</a>{% endif %}
      {% if p.pdf_url %}<a class="link-pill pill--pdf" href="{{ p.pdf_url }}" target="_blank" rel="noopener"><i class="fa fa-file-pdf"></i>PDF</a>{% endif %}
      {% if p.code_url %}<a class="link-pill pill--code" href="{{ p.code_url }}" target="_blank" rel="noopener"><i class="fab fa-github"></i>Code</a>{% endif %}
      {% if p.bibtex %}<button class="link-pill pill--copy" type="button" data-bib="{{ p.bibtex | escape }}"><i class="fa fa-clipboard"></i>BibTeX</button>{% endif %}
    </div>
  </li>
{% endfor %}
</ul>
{% endfor %}

<script>
  // Build tag buttons from data-tags across items
  (function(){
    const wrap = document.getElementById('pub-filters');
    const items = [...document.querySelectorAll('.pub-item')];
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
      // hide year headers with no visible items in the following list
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
