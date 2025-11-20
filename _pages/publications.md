---
permalink: /publications/
title: "Publications"
layout: single
author_profile: true
classes: wide
search: true
---

<style>
  .venue-ticker{
    display:inline-block; margin-left:.45rem; padding:.08rem .45rem;
    font-size:.76rem; font-weight:700; text-transform: lowercase;
    border:1px solid #cbd5e1; border-radius:999px; color:#0f172a; background:#f1f5f9;
  }
  html.theme-dark .venue-ticker{ background:#0f172a; border-color:#1f2937; color:#e6edf3; }

  .pub-list{ margin:.25rem 0 1.25rem; }
  .pub-item{ padding:.6rem .25rem; border-radius:.5rem; }
  .pub-item:hover{ background:rgba(14,165,233,.06); }
  html.theme-dark .pub-item:hover{ background:#0b1220; }

  .year-head{ margin-top:1.75rem; border-top:1px solid rgba(0,0,0,.06); padding-top:1rem; }
  html.theme-dark .year-head{ border-color:#1f2937; }

  .link-pills{ display:flex; flex-wrap:wrap; gap:.35rem; margin:.25rem 0 0; }
  .link-pill{
    display:inline-flex; align-items:center; gap:.35rem; padding:.2rem .6rem;
    border-radius:999px; font-weight:600; border:1px solid var(--brand-accent,#0ea5e9);
    text-decoration:none; transition:.15s ease; font-size:.85rem
  }
  .link-pill:hover{ background:var(--brand-accent,#0ea5e9); color:#fff }
  .pill--pdf{ border-color:#ef4444 } .pill--pdf:hover{ background:#ef4444; color:#fff }
  .pill--code{ border-color:#16a34a } .pill--code:hover{ background:#16a34a; color:#fff }
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

      {%- assign l = p.paper_url | downcase -%}
      {%- assign vt = '' -%}
      {% if l contains 'arxiv' %}{% assign vt = 'arxiv' %}
      {% elsif l contains 'emnlp' %}{% assign vt = 'emnlp' %}
      {% elsif l contains 'coling' %}{% assign vt = 'coling' %}
      {% elsif l contains 'naacl' %}{% assign vt = 'naacl' %}
      {% elsif l contains 'aclanthology' or l contains '/acl' %}{% assign vt = 'acl' %}
      {% elsif l contains 'neurips' or l contains '/nips' %}{% assign vt = 'neurips' %}
      {% elsif l contains 'iclr' %}{% assign vt = 'iclr' %}
      {% elsif l contains 'icml' %}{% assign vt = 'icml' %}
      {% elsif l contains 'cvpr' %}{% assign vt = 'cvpr' %}
      {% elsif l contains 'eccv' %}{% assign vt = 'eccv' %}
      {% elsif l contains 'ijcai' %}{% assign vt = 'ijcai' %}
      {% elsif l contains 'kdd' %}{% assign vt = 'kdd' %}
      {% elsif l contains 'sigir' %}{% assign vt = 'sigir' %}
      {% elsif l contains 'thewebconf' or l contains '/www.' %}{% assign vt = 'www' %}
      {% endif %}

      <li class="pub-item" data-tags="{{ p.tags | join: ' ' }}">
        <strong>
          <a class="pub-title" href="{{ p.paper_url | default: p.pdf_url | default: p.url | relative_url }}" target="_blank" rel="noopener">
            {{ p.title }}
          </a>
          {% if vt != '' %}<span class="venue-ticker">{{ vt }}</span>{% endif %}
        </strong><br/>

        <em>{{ p.authors | markdownify | replace: '<p>','' | replace: '</p>','' }}</em>.
        {% if p.venue %} {{ p.venue }}{% endif %}{% if p.year %} ({{ p.year }}){% endif %}.

        <div class="link-pills">
          {% if p.paper_url %}<a class="link-pill" href="{{ p.paper_url }}" target="_blank" rel="noopener">📄 Paper</a>{% endif %}
          {% if p.pdf_url %}<a class="link-pill pill--pdf" href="{{ p.pdf_url }}" target="_blank" rel="noopener">PDF</a>{% endif %}
          {% if p.code_url %}<a class="link-pill pill--code" href="{{ p.code_url }}" target="_blank" rel="noopener">Code</a>{% endif %}
          {% if p.url %}<a class="link-pill" href="{{ p.url | relative_url }}">Details</a>{% endif %}
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
        const lis = Array.from(b.querySelectorAll('.pub-item'));
        const visible = lis.some(li => li.style.display !== 'none');
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
      const curr = document.querySelector(`#pub-filters .btn[data-tag="${tag}"]`);
      if (curr) curr.classList.add('btn--primary');
      updateYears();
    }

    btns.forEach(b => b.addEventListener('click', () => setActive(b.dataset.tag)));
    updateYears(); // hide empty years on initial load
  })();
</script>
