---
permalink: /awards/
title: "Awards"
layout: single
author_profile: true
classes: wide
---

<style>
  /* ========= Scoped theme tokens (light + dark) ========= */
  .awards-scope{
    --paper:#fffaf1;
    --tile:#ffffff;
    --ink:#0b1320;
    --muted:#5a6b82;
    --ring:#e7dbc7;
    --ring-strong:#d9c6a6;
    --shadow:0 10px 18px rgba(0,0,0,.07),0 1px 3px rgba(0,0,0,.06);

    --accentA:#2d8fa2; --accentB:#7c62ff; --accentC:#f97316; --accentD:#14b8a6;
    --pdfRed:#d44;
  }
  html.theme-dark .awards-scope{
    --paper:#0e1624;
    --tile:#0f1b2d;
    --ink:#e6edf3;
    --muted:#9fb4cc;
    --ring:#1c2a42;
    --ring-strong:#2a3b5d;
    --shadow:0 12px 22px rgba(0,0,0,.32),0 1px 3px rgba(0,0,0,.2);

    --accentA:#27a3c0; --accentB:#8b7bff; --accentC:#fb923c; --accentD:#2dd4bf;
    --pdfRed:#ff7a7a;
  }

  /* ====== Layout (with a clearer divider + wider column gap) ====== */
  .awards-wrap{
    display:grid;
    grid-template-columns: 1.05fr minmax(420px,1.1fr);
    column-gap:2rem; row-gap:1.5rem;
    align-items:start; position:relative;
  }
  @media(max-width:1100px){ .awards-wrap{ grid-template-columns:1fr; } }

  .awards-wrap::before{
    content:""; position:absolute; top:.25rem; bottom:.25rem; left:50%;
    transform:translateX(-50%); width:3px; border-radius:3px;
    background:linear-gradient(180deg,var(--accentA),var(--accentB));
    opacity:.35;
  }
  @media(max-width:1100px){ .awards-wrap::before{ display:none; } }

  /* ====== Metric tiles (left) ====== */
  .metrics{ display:grid; grid-template-columns:repeat(2,minmax(220px,1fr)); gap:1rem; }
  @media(max-width:720px){ .metrics{ grid-template-columns:1fr 1fr; } }

  .metric{
    background:var(--tile); border:1.5px solid var(--ring); border-radius:16px;
    box-shadow:var(--shadow); padding:1rem 1rem .9rem;
  }
  .metric strong{ display:block; font-size:2.2rem; line-height:1; letter-spacing:.02em; color:var(--ink); margin-bottom:.35rem; }
  .metric small{ display:block; color:var(--muted); font-weight:600; font-size:.96rem; }
  .metric small .muter{ font-weight:500; opacity:.95; }

  /* ====== Best paper (left) ====== */
  .best-paper{
    margin-top:1rem;
    background:var(--tile); border:1.5px solid var(--ring); border-radius:16px;
    box-shadow:var(--shadow); padding:1rem 1.1rem;
  }
  .best-paper h4{ margin:.1rem 0 .75rem; color:var(--ink); display:flex; align-items:center; gap:.6rem; }
  .bp-chip{
    display:inline-block; padding:.2rem .55rem; border-radius:999px;
    background:rgba(20,184,166,.12); color:var(--ink); font-weight:800; font-size:.78rem;
    border:1px solid rgba(20,184,166,.35);
  }
  .bp-item{ display:flex; gap:.6rem; align-items:flex-start; margin:.45rem 0; }
  .bp-emoji{ font-size:1.15rem; line-height:1.15; margin-top:.05rem }
  .bp-title a{ font-weight:800; color:var(--ink); text-decoration:underline; }
  .bp-title a:visited{ color:var(--ink); }
  .bp-title span{ color:var(--muted); font-weight:600; margin-left:.35rem; }

  /* ====== Award bubbles (right) ====== */
  .awards-grid{
    display:grid;
    grid-template-columns:repeat(auto-fit, minmax(340px,1fr));
    gap:1rem;
  }
  .award-card{
    background:var(--tile); border:1.5px solid var(--ring); border-radius:20px;
    box-shadow:var(--shadow); padding:1rem 1.1rem; display:flex; align-items:center; gap:.9rem;
    transition:transform .12s ease, box-shadow .12s ease, border-color .12s ease;
  }
  .award-card:hover{ transform:translateY(-2px) scale(1.01); border-color:var(--ring-strong); }

  .award-icon{
    flex:0 0 44px; height:44px; border-radius:999px; display:grid; place-items:center;
    color:#fff; font-size:1.05rem; font-weight:900;
    background:linear-gradient(135deg, var(--accentA), var(--accentB));
    box-shadow:0 4px 10px rgba(0,0,0,.08);
  }

  .award-body{ min-width:0; }
  .award-title{
    font-weight:800; color:var(--ink);
    font-size:1.02rem; line-height:1.25;
    overflow:hidden; text-overflow:ellipsis; white-space:nowrap;
  }
  .award-meta{ color:var(--muted); font-weight:600; font-size:.95rem; }

  .award-actions{ margin-left:auto; display:flex; gap:.5rem; }
  .pill{
    display:inline-flex; align-items:center; gap:.4rem; padding:.35rem .7rem; border-radius:999px;
    border:1px solid var(--accentA); color:var(--accentA); background:#f0fbfe; text-decoration:none; font-weight:800;
  }
  .pill, .pill:visited{ color:var(--accentA); }
  .pill:hover{ background:var(--accentA); color:#fff; }

  .pill--pdf{
    border-color:var(--pdfRed); color:var(--pdfRed); background:rgba(255,0,0,.06);
  }
  .pill--pdf, .pill--pdf:visited{ color:var(--pdfRed); }
  .pill--pdf:hover{ background:var(--pdfRed); color:#fff; }

  /* Slight rim hue variety */
  .awards-grid .award-card:nth-child(4n+1){ --accentA:#2d8fa2; --accentB:#7c62ff; }
  .awards-grid .award-card:nth-child(4n+2){ --accentA:#f97316; --accentB:#f59e0b; }
  .awards-grid .award-card:nth-child(4n+3){ --accentA:#14b8a6; --accentB:#0ea5e9; }
  .awards-grid .award-card:nth-child(4n+4){ --accentA:#22c55e; --accentB:#10b981; }
</style>

{%- comment -%}
Counts:
- Papers  = site.publications.size
- Patents = site.patents.size
- Talks   = total talks (per your request)
Best-paper items come from _data/best_papers.yml entries: { title, venue, year, link, tags[] }.
Awards come from the _awards collection. Front matter supported:
  title, year, org, icon: trophy|medal|star, certificate: /assets/awards/xxx.pdf, link:
{%- endcomment -%}

{% assign papers_count = site.publications | size %}
{% assign patents_count = site.patents | size %}
{% assign talks_total   = site.talks | size %}

<div class="awards-scope">
  <div class="awards-wrap">
    <!-- LEFT -->
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
          <strong>&gt;{{ talks_total }}</strong>
          <small>talks at tier-1<br><span class="muter">conferences</span></small>
        </div>
      </div>

      <div class="best-paper">
        <h4>Best paper awards <span class="bp-chip">Social Impact</span></h4>
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
          {%- endif -%}
        {%- endif -%}
      </div>
    </div>

    <!-- RIGHT -->
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
            <div class="award-title" title="{{ a.title }}">{{ a.title }}</div>
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
</div>
