---
permalink: /awards/
title: "Awards"
layout: single
author_profile: true
classes: wide
---

<style>
  :root{
    --paper:#fffaf1;
    --ink:#0b1320;
    --muted:#64748b;
    --ring:#e7dbc7;
    --ring-strong:#d9c6a6;
    --tile:#fff;
    --shadow:0 10px 18px rgba(0,0,0,.07),0 1px 3px rgba(0,0,0,.06);
    --accentA:#2d8fa2;  --accentB:#7c62ff; --accentC:#f97316; --accentD:#14b8a6;
  }

  /* two-column responsive layout with a visible vertical divider */
  .awards-wrap{
    display:grid; grid-template-columns: 1.1fr minmax(420px, 1.1fr);
    gap:1.25rem; align-items:start; position:relative;
  }
  @media(max-width:1100px){ .awards-wrap{ grid-template-columns:1fr; } }

  .awards-wrap::before{
    content:""; position:absolute; top:.25rem; bottom:.25rem; left:50%; width:2px;
    transform:translateX(-50%);
    background:linear-gradient(180deg, rgba(45,143,162,.25), rgba(124,98,255,.25));
    border-radius:2px;
    opacity:.8;
  }
  @media(max-width:1100px){ .awards-wrap::before{ display:none; } }

  /* Left: metrics */
  .metrics{
    display:grid; grid-template-columns:repeat(2,minmax(180px,1fr)); gap:1rem;
  }
  @media(max-width:720px){ .metrics{ grid-template-columns:1fr 1fr; } }

  .metric{
    background:var(--tile); border:1.5px solid var(--ring); border-radius:16px;
    box-shadow:var(--shadow); padding:1rem 1rem .9rem;
  }
  .metric strong{
    display:block; font-size:2.2rem; line-height:1; letter-spacing:.02em; color:var(--ink);
    margin-bottom:.35rem;
  }
  .metric small{
    display:block; color:var(--muted); font-weight:600; font-size:.96rem;
  }
  .metric small .muter{ font-weight:500; opacity:.95; }

  /* Best paper badge list (kept once, with link) */
  .best-paper{
    margin-top:1rem;
    background:var(--tile); border:1.5px solid var(--ring); border-radius:16px;
    box-shadow:var(--shadow); padding:1rem 1.1rem;
  }
  .best-paper h4{ margin:.1rem 0 .6rem; }
  .bp-item{ display:flex; gap:.6rem; align-items:flex-start; margin:.35rem 0; }
  .bp-emoji{ font-size:1.15rem; line-height:1.15; margin-top:.05rem }
  .bp-title a{ font-weight:700; }
  .bp-title span{ color:var(--muted); font-weight:600; margin-left:.35rem; }

  /* Right: awards bubbles */
  .awards-grid{
    display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:1rem;
  }
  .award-card{
    background:var(--tile);
    border:1.5px solid var(--ring);
    border-radius:20px; box-shadow:var(--shadow);
    padding:1rem 1.1rem; display:flex; align-items:center; gap:.9rem;
    transition:transform .12s ease, box-shadow .12s ease, border-color .12s ease;
    position:relative; isolation:isolate;
  }
  .award-card:hover{ transform:translateY(-2px) scale(1.01); border-color:var(--ring-strong); }
  .award-icon{
    flex:0 0 42px; height:42px; border-radius:999px; display:grid; place-items:center;
    color:#fff; font-size:1.05rem; font-weight:900;
    background:linear-gradient(135deg, var(--accentA), var(--accentB));
    box-shadow:0 4px 10px rgba(0,0,0,.08);
  }
  .award-body{ min-width:0; }
  .award-title{ font-weight:800; color:var(--ink); overflow:hidden; text-overflow:ellipsis; white-space:nowrap; }
  .award-meta{ color:var(--muted); font-weight:600; font-size:.95rem; }
  .award-actions{ margin-left:auto; display:flex; gap:.5rem; }
  .pill{
    display:inline-flex; align-items:center; gap:.4rem; padding:.35rem .7rem; border-radius:999px;
    border:1px solid var(--accentA); color:var(--accentA); background:#f0fbfe; text-decoration:none; font-weight:800;
  }
  .pill:hover{ background:var(--accentA); color:#fff; }
  .pill--pdf{ border-color:#d44; color:#d44; background:#fff1f1; }
  .pill--pdf:hover{ background:#d44; color:#fff; }

  /* give each bubble a slightly different rim hue */
  .awards-grid .award-card:nth-child(4n+1){ --accentA:#2d8fa2; --accentB:#7c62ff; }
  .awards-grid .award-card:nth-child(4n+2){ --accentA:#f97316; --accentB:#f59e0b; }
  .awards-grid .award-card:nth-child(4n+3){ --accentA:#14b8a6; --accentB:#0ea5e9; }
  .awards-grid .award-card:nth-child(4n+4){ --accentA:#22c55e; --accentB:#10b981; }
</style>

{%- comment -%}
Counts are computed from your collections:
- Papers = site.publications.size
- Patents = site.patents.size
- Talks (top-tier) = count of site.talks where `tier` contains "top", or tags include "top"/"tier1"/"top-tier", or `venue_tier == 'top'`.
Best-paper items come from _data/best_papers.yml (list), each with { title, venue, year, link }.
Awards are read from your _awards collection. Optional front-matter on each item:
  title: "Victor Award"
  year: 2024
  org: "Acme Corp"
  icon: "trophy" | "medal" | "star"
  certificate: /assets/awards/victor-award.pdf  # or leave blank to auto-match a PDF in /assets/awards/
{%- endcomment -%}

{%- assign papers_count = site.publications | size -%}
{%- assign patents_count = site.patents | size -%}
{%- assign talks_top = 0 -%}
{%- for t in site.talks -%}
  {%- assign tier = t.tier | default:t.venue_tier | downcase -%}
  {%- assign tags_join = t.tags | join: " " | downcase -%}
  {%- if tier contains "top" or tags_join contains "tier1" or tags_join contains "top-tier" or tags_join contains "top" -%}
    {%- assign talks_top = talks_top | plus: 1 -%}
  {%- endif -%}
{%- endfor -%}

<div class="awards-wrap">
  <!-- LEFT: metrics + best paper list -->
  <div>
    <div class="metrics">
      <div class="metric">
        <strong>{{ papers_count }}</strong>
        <small>papers in<br><span class="muter">top venues</span></small>
      </div>
      <div class="metric">
        <strong>{{ patents_count }}</strong>
        <small>patents</small>
      </div>
      <div class="metric">
        <strong>&gt;{{ talks_top }}</strong>
        <small>talks at tier-1<br><span class="muter">conferences</span></small>
      </div>
    </div>

    <div class="best-paper">
      <h4>Best paper awards</h4>
      {%- if site.data.best_papers and site.data.best_papers.size > 0 -%}
        {%- for bp in site.data.best_papers -%}
          <div class="bp-item">
            <div class="bp-emoji">🏅</div>
            <div class="bp-title">
              <a href="{{ bp.link | relative_url }}" target="_blank" rel="noopener">{{ bp.title }}</a>
              <span>— {{ bp.venue }} {{ bp.year }}</span>
            </div>
          </div>
        {%- endfor -%}
      {%- else -%}
        {%- comment -%} Fallback: try to find the Accesseval paper automatically {%- endcomment -%}
        {%- assign acc = nil -%}
        {%- for p in site.publications -%}
          {%- assign tl = p.title | downcase -%}
          {%- if tl contains "accesseval" or tl contains "disability bias" -%}
            {%- assign acc = p -%}{%- break -%}
          {%- endif -%}
        {%- endfor -%}
        {%- if acc -%}
          <div class="bp-item">
            <div class="bp-emoji">🏅</div>
            <div class="bp-title">
              <a href="{{ acc.url | relative_url }}">{{ acc.title }}</a>
              <span>— {{ acc.venue | default:"EMNLP" }} {{ acc.year | default:"2025" }}</span>
            </div>
          </div>
        {%- else -%}
          <p style="color:var(--muted)">Add items to <code>_data/best_papers.yml</code> to list them here.</p>
        {%- endif -%}
      {%- endif -%}
    </div>
  </div>

  <!-- RIGHT: award bubbles -->
  <div class="awards-grid">
    {%- assign awards = site.awards | sort: "year" | reverse -%}
    {%- for a in awards -%}
      {%- assign icon = a.icon | default:"trophy" -%}
      {%- assign cert = a.certificate | default:a.pdf | default:a.certificate_url -%}

      {%- if cert == nil or cert == "" -%}
        {%- assign akey = a.slug | default:a.title | slugify: "pretty" -%}
        {%- for sf in site.static_files -%}
          {%- assign sp = sf.path | downcase -%}
          {%- if sp contains "/assets/awards/" and sf.extname == ".pdf" -%}
            {%- assign base = sf.name | remove: sf.extname | slugify: "pretty" -%}
            {%- if base == akey -%}
              {%- assign cert = sf.path | relative_url -%}
              {%- break -%}
            {%- endif -%}
          {%- endif -%}
        {%- endfor -%}
      {%- endif -%}

      <div class="award-card">
        <div class="award-icon">
          {%- if icon == "medal" -%}🥇
          {%- elsif icon == "star" -%}⭐
          {%- else -%}🏆
          {%- endif -%}
        </div>
        <div class="award-body">
          <div class="award-title">{{ a.title }}</div>
          <div class="award-meta">
            {%- if a.org %}{{ a.org }}{% endif -%}
            {%- if a.year %}{% if a.org %} • {% endif %}{{ a.year }}{% endif -%}
          </div>
        </div>
        <div class="award-actions">
          {%- if cert and cert != "" -%}
            <a class="pill pill--pdf" href="{{ cert }}" target="_blank" rel="noopener">PDF</a>
          {%- endif -%}
          {%- if a.link and a.link != "" -%}
            <a class="pill" href="{{ a.link }}" target="_blank" rel="noopener">Site</a>
          {%- endif -%}
        </div>
      </div>
    {%- endfor -%}
  </div>
</div>
