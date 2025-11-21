---
permalink: /projects/
title: "Projects"
layout: single
author_profile: true
classes: wide
search: true
---

<style>
  :root{
    --tile:#fff; --ink:#0b1320; --muted:#64748b; --rim:#e5e7eb; --rim-strong:#cbd5e1; --accent:#2d8fa2;
  }
  html.theme-dark{
    --tile:#0b1220; --ink:#e5e7eb; --muted:#9aa7b5; --rim:#1f2937; --rim-strong:#334155; --accent:#22d3ee;
  }

  #proj-filters{ display:flex; flex-wrap:wrap; gap:.5rem; margin:.5rem 0 1rem 0; }
  #proj-filters .btn{ font-weight:800; }

  .proj-grid{ display:grid; grid-template-columns:repeat(auto-fit, minmax(340px, 1fr)); gap:1rem; }

  .proj-card{
    background:var(--tile); color:var(--ink);
    border:1.5px solid var(--rim); border-radius:18px;
    box-shadow:0 10px 18px rgba(0,0,0,.06);
    padding:1rem 1.1rem; display:flex; flex-direction:column; gap:.65rem;
    transition:transform .12s ease, border-color .12s ease;
  }
  .proj-card:hover{ transform:translateY(-1px); border-color:var(--rim-strong); }

  .proj-head{ display:flex; align-items:baseline; gap:.6rem; flex-wrap:wrap; }
  .proj-title{ font-size:1.1rem; font-weight:900; line-height:1.2; }

  .proj-badges{ display:flex; gap:.4rem; flex-wrap:wrap; }
  .badge{
    display:inline-flex; align-items:center; gap:.35rem;
    padding:.2rem .6rem; border-radius:999px;
    font-weight:800; font-size:.78rem; letter-spacing:.01em;
    border:1px solid var(--rim-strong); background:rgba(2,132,199,.08);
  }
  .badge--year{ background:rgba(99,102,241,.12); }
  .badge--company{ background:rgba(34,197,94,.12); }
  .badge--role{ background:rgba(234,179,8,.12); }

  .tags{ display:flex; flex-wrap:wrap; gap:.35rem; }
  .tag{
    display:inline-flex; align-items:center; padding:.16rem .5rem;
    border-radius:999px; border:1px solid var(--rim);
    font-weight:700; font-size:.72rem; color:var(--muted);
  }

  .bullets{ margin:.2rem 0 0 0; padding-left:1.1rem; }
  .bullets li{ margin:.2rem 0; }

  .links{ display:flex; flex-wrap:wrap; gap:.45rem; margin-top:.2rem; }
  .link-pill{
    display:inline-flex; align-items:center; gap:.4rem;
    padding:.34rem .7rem; border-radius:999px; text-decoration:none;
    font-weight:800; border:1px solid var(--accent); color:var(--accent); background:#effafd;
  }
  .link-pill:hover{ background:var(--accent); color:#fff; }

  .proj-card, .proj-card li { font-size:.98rem; }
</style>

{%- assign items = site.data.projects -%}
{%- if items == nil or items == empty -%}
<div class="notice--info">
  Add projects to <code>_data/projects.yml</code> to populate this page.
</div>
{%- endif -%}

{%- assign all_tags = "" | split: "" -%}
{%- for p in items -%}
  {%- for t in p.tags -%}
    {%- assign tclean = t | strip -%}
    {%- unless all_tags contains tclean -%}{%- assign all_tags = all_tags | push: tclean -%}{%- endunless -%}
  {%- endfor -%}
{%- endfor -%}
{%- assign all_tags = all_tags | sort_natural -%}

<div id="proj-filters">
  <button class="btn btn--primary" data-tag="all">All</button>
  {%- for t in all_tags -%}<button class="btn" data-tag="{{ t | escape }}">{{ t }}</button>{%- endfor -%}
</div>

{%- assign sorted = site.data.projects | sort: "year" | reverse -%}
<div class="proj-grid">
{%- for p in sorted -%}
  <article class="proj-card" data-tags="{{ p.tags | join: ' ' }}">
    <div class="proj-head">
      <div class="proj-title">{{ p.title }}</div>
      <div class="proj-badges">
        {%- if p.company -%}<span class="badge badge--company">{{ p.company }}</span>{%- endif -%}
        {%- if p.role -%}<span class="badge badge--role">{{ p.role }}</span>{%- endif -%}
        {%- if p.year -%}<span class="badge badge--year">{{ p.year }}</span>{%- endif -%}
      </div>
    </div>

    {%- if p.tags and p.tags.size > 0 -%}
      <div class="tags">{%- for tg in p.tags -%}<span class="tag">{{ tg }}</span>{%- endfor -%}</div>
    {%- endif -%}

    {%- if p.bullets and p.bullets.size > 0 -%}
      <ul class="bullets">{%- for b in p.bullets -%}<li>{{ b }}</li>{%- endfor -%}</ul>
    {%- endif -%}

    {%- if p.links and p.links.size > 0 -%}
      <div class="links">
        {%- for l in p.links -%}<a class="link-pill" href="{{ l.url }}" target="_blank" rel="noopener">{{ l.label }}</a>{%- endfor -%}
      </div>
    {%- endif -%}
  </article>
{%- endfor -%}
</div>

<script>
(function(){
  const btns  = document.querySelectorAll('#proj-filters .btn');
  const cards = Array.from(document.querySelectorAll('.proj-card'));
  function setActive(tag){
    cards.forEach(c=>{
      const tags=(c.dataset.tags||'').split(/\s+/).filter(Boolean);
      c.style.display = (tag==='all'||tags.includes(tag)) ? '' : 'none';
    });
    btns.forEach(b=>b.classList.remove('btn--primary'));
    document.querySelector(`#proj-filters .btn[data-tag="${tag}"]`)?.classList.add('btn--primary');
  }
  btns.forEach(b=>b.addEventListener('click',()=>setActive(b.dataset.tag)));
})();
</script>
