---
permalink: /publications/
title: "Publications"
layout: single
author_profile: true
classes: wide
search: true
---

<style>
/* ====== venue badge palette ====== */
.venue-badge{display:inline-flex;align-items:center;gap:.35rem;
  padding:.18rem .55rem;border-radius:999px;font-weight:800;font-size:.75rem;
  text-transform:uppercase;letter-spacing:.02em;border:1px solid transparent}

/* ACL family */
.vb-acl{background:#fde68a;color:#713f12;border-color:#f59e0b}
.vb-emnlp{background:#d9f99d;color:#365314;border-color:#84cc16}
.vb-naacl{background:#bae6fd;color:#0c4a6e;border-color:#38bdf8}
.vb-eacl{background:#f5d0fe;color:#6b21a8;border-color:#e879f9}
.vb-coling{background:#cffafe;color:#164e63;border-color:#67e8f9}
.vb-tacl{background:#fef3c7;color:#7c2d12;border-color:#fbbf24}
.vb-cl{background:#ede9fe;color:#4c1d95;border-color:#c4b5fd}

/* Other publishers */
.vb-ieee{background:#dbeafe;color:#1e3a8a;border-color:#60a5fa}
.vb-acm{background:#bbf7d0;color:#065f46;border-color:#34d399}
.vb-openreview{background:#f5f5f4;color:#292524;border-color:#d6d3d1}
.vb-springer{background:#e0e7ff;color:#3730a3;border-color:#a5b4fc}
.vb-arxiv{background:#fecaca;color:#7f1d1d;border-color:#f87171}

/* fallback */
.vb-generic{background:#e5e7eb;color:#111827;border-color:#d1d5db}

/* pills you already use */
.link-pills{display:flex;flex-wrap:wrap;gap:.5rem;margin:.35rem 0 0}
.link-pill{display:inline-flex;align-items:center;gap:.4rem;padding:.25rem .7rem;border-radius:999px;font-weight:700;border:1px solid var(--brand-accent,#0ea5e9);text-decoration:none}
.link-pill:hover{background:var(--brand-accent,#0ea5e9);color:#fff}
.pill--pdf{border-color:#ef4444}.pill--pdf:hover{background:#ef4444;color:#fff}
.pill--code{border-color:#16a34a}.pill--code:hover{background:#16a34a;color:#fff}

/* authors highlight */
.me-emph{font-weight:800}
.year-head{margin:.75rem 0 .25rem}
.pub-item{padding:.4rem .55rem;border-radius:.5rem}
.pub-item:hover{background:rgba(14,165,233,.06)}
html.theme-dark .pub-item:hover{background:#0b1220}
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

/* collect distinct years that actually have items */
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
        {% comment %}
          Compute a colored venue badge from paper_url (with override).
        {% endcomment %}
        {% assign url = p.paper_url | default: p.pdf_url | default: "" %}
        {% assign host = url | replace: 'https://','' | replace:'http://','' | split:'/' | first | downcase %}
        {% assign path = url | split:'/' | last | downcase %}

        {% assign badge = '' %}
        {% assign vb = 'vb-generic' %}

        {% if p.venue_slug %}
          {% assign slug = p.venue_slug | downcase %}
          {% assign badge = slug %}
          {% case slug %}
            {% when 'emnlp' %}{% assign vb='vb-emnlp' %}
            {% when 'acl' %}{% assign vb='vb-acl' %}
            {% when 'naacl' %}{% assign vb='vb-naacl' %}
            {% when 'eacl' %}{% assign vb='vb-eacl' %}
            {% when 'coling' %}{% assign vb='vb-coling' %}
            {% when 'tacl' %}{% assign vb='vb-tacl' %}
            {% when 'cl' %}{% assign vb='vb-cl' %}
            {% when 'ieee' %}{% assign vb='vb-ieee' %}
            {% when 'acm' %}{% assign vb='vb-acm' %}
            {% when 'openreview' %}{% assign vb='vb-openreview' %}
            {% when 'springer' %}{% assign vb='vb-springer' %}
            {% when 'arxiv' %}{% assign vb='vb-arxiv' %}
            {% else %}{% assign vb='vb-generic' %}
          {% endcase %}
        {% else %}
          {% if host contains 'aclanthology.org' %}
            {% if path contains 'emnlp' %}{% assign badge='emnlp' %}{% assign vb='vb-emnlp' %}
            {% elsif path contains 'naacl' %}{% assign badge='naacl' %}{% assign vb='vb-naacl' %}
            {% elsif path contains 'acl' %}{% assign badge='acl' %}{% assign vb='vb-acl' %}
            {% elsif path contains 'eacl' %}{% assign badge='eacl' %}{% assign vb='vb-eacl' %}
            {% elsif path contains 'coling' %}{% assign badge='coling' %}{% assign vb='vb-coling' %}
            {% elsif path contains 'tacl' %}{% assign badge='tacl' %}{% assign vb='vb-tacl' %}
            {% elsif path contains 'cl' %}{% assign badge='cl' %}{% assign vb='vb-cl' %}
            {% else %}{% assign badge='acl' %}{% assign vb='vb-acl' %}
            {% endif %}
          {% elsif host contains 'ieeexplore.ieee.org' %}
            {% assign badge='ieee' %}{% assign vb='vb-ieee' %}
          {% elsif host contains 'dl.acm.org' %}
            {% assign badge='acm' %}{% assign vb='vb-acm' %}
          {% elsif host contains 'arxiv.org' or host == 'arxiv' %}
            {% assign badge='arxiv' %}{% assign vb='vb-arxiv' %}
          {% elsif host contains 'openreview' %}
            {% assign badge='openreview' %}{% assign vb='vb-openreview' %}
          {% elsif host contains 'springer' %}
            {% assign badge='springer' %}{% assign vb='vb-springer' %}
          {% else %}
            {% comment %}last-ditch: look for tokens in full URL{% endcomment %}
            {% if url contains 'emnlp' %}{% assign badge='emnlp' %}{% assign vb='vb-emnlp' %}
            {% elsif url contains 'naacl' %}{% assign badge='naacl' %}{% assign vb='vb-naacl' %}
            {% elsif url contains 'acl' %}{% assign badge='acl' %}{% assign vb='vb-acl' %}
            {% elsif url contains 'coling' %}{% assign badge='coling' %}{% assign vb='vb-coling' %}
            {% endif %}
          {% endif %}
        {% endif %}

        {% assign authors_html = p.authors | replace: 'Agarwal, Amit', '<strong class="me-emph">Agarwal, Amit</strong>' %}

        <li class="pub-item" data-tags="{{ p.tags | join: ' ' }}">
          <strong>
            {% if url %}
              <a class="pub-title" href="{{ url }}">{{ p.title }}</a>
            {% else %}
              <a class="pub-title" href="{{ p.url | relative_url }}">{{ p.title }}</a>
            {% endif %}
          </strong>
          {% if badge != '' %}
            <span class="venue-badge {{ vb }}">{{ badge }}</span>
          {% endif %}
          <br/>
          <em>{{ authors_html }}</em>. {{ p.venue }}{% if p.year %} ({{ p.year }}){% endif %}.

          <div class="link-pills">
            {% if p.paper_url %}<a class="link-pill" href="{{ p.paper_url }}">📄 Paper</a>{% endif %}
            {% if p.pdf_url %}<a class="link-pill pill--pdf" href="{{ p.pdf_url }}">PDF</a>{% endif %}
            {% if p.code_url %}<a class="link-pill pill--code" href="{{ p.code_url }}">Code</a>{% endif %}
            {% if p.url %}<a class="link-pill" href="{{ p.url | relative_url }}">Details</a>{% endif %}
            {% if p.bibtex %}<button class="link-pill" onclick="navigator.clipboard.writeText(this.dataset.bib);this.textContent='Copied!';setTimeout(()=>this.textContent='BibTeX',900)" data-bib="{{ p.bibtex | escape }}">BibTeX</button>{% endif %}
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
        const vis = Array.from(b.querySelectorAll('.pub-item')).some(li => li.style.display !== 'none');
        b.style.display = vis ? '' : 'none';
      });
    }
    function setActive(tag){
      items.forEach(li=>{
        const tags = (li.dataset.tags || '').split(/\s+/).filter(Boolean);
        li.style.display = (tag === 'all' || tags.includes(tag)) ? '' : 'none';
      });
      btns.forEach(x=>x.classList.remove('btn--primary'));
      document.querySelector(`#pub-filters .btn[data-tag="${tag}"]`)?.classList.add('btn--primary');
      updateYears();
    }
    btns.forEach(b => b.addEventListener('click', () => setActive(b.dataset.tag)));
    updateYears();
  })();
</script>
