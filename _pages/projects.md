---
permalink: /projects/
title: "Projects"
layout: single
author_profile: true
classes: wide
---

<style>
  :root{
    --card-bg: #fff;
    --card-ring:#e5e7eb;
    --shadow: 0 10px 18px rgba(0,0,0,.07), 0 1px 3px rgba(0,0,0,.06);
  }
  html.theme-dark{
    --card-bg:#0b1220;
    --card-ring:#1f2937;
    --shadow:none;
  }

  /* filters */
  #proj-filters{ margin:.25rem 0 1rem; display:flex; flex-wrap:wrap; gap:.5rem; }
  #proj-filters .btn{ padding:.4rem .7rem; font-weight:800; border-radius:999px; }
  #proj-filters .btn--primary{ background:#0ea5e9; color:#fff; }

  /* Masonry-ish grid */
  .projects-grid{ display:grid; grid-template-columns: repeat(2, minmax(300px,1fr)); gap:1.1rem; }
  @media (max-width: 1100px){ .projects-grid{ grid-template-columns:1fr; } }

  /* Card */
  .project-card{
    position:relative;
    background:var(--card-bg);
    border:1.5px solid var(--card-ring);
    border-radius:18px;
    box-shadow:var(--shadow);
    padding:1rem 1rem 1rem 1.1rem;
    overflow:hidden;
    /* default accents (overridden per-card via JS) */
    --accentA:#22c55e; --accentB:#86efac;
  }

  /* Vertical accent bar */
  .project-card::before{
    content:"";
    position:absolute; left:0; top:0; bottom:0; width:7px;
    background:linear-gradient(180deg, var(--accentA), var(--accentB));
    border-radius:18px 0 0 18px;
  }

  .proj-title{ font-size:1.25rem; line-height:1.25; font-weight:900; margin: .1rem 0 .5rem; }
  .badges{ display:flex; flex-wrap:wrap; gap:.4rem; margin:.2rem 0 .6rem; }
  .pill{ display:inline-flex; align-items:center; padding:.28rem .6rem; border-radius:999px; font-weight:800; font-size:.85rem; border:1px solid #e5e7eb; }
  html.theme-dark .pill{ border-color:#334155; }
  .tag{ background:#eef2ff; border-color:#c7d2fe; }
  html.theme-dark .tag{ background:#1f2937; border-color:#334155; }
  .cta-row{ margin-top:.6rem; display:flex; gap:.5rem; flex-wrap:wrap; }
  .cta{ display:inline-flex; align-items:center; gap:.4rem; padding:.35rem .8rem; border-radius:999px; font-weight:800; border:1px solid #0ea5e9; color:#0ea5e9; background:#f0fbfe; text-decoration:none; }
  .cta:hover{ background:#0ea5e9; color:#fff; }

  /* a touch more space away from the divider on Awards-style layouts */
  .projects-wrap{ margin-right:.25rem; }
</style>

<div id="proj-filters">
  <button class="btn btn--primary" data-tag="all">All</button>
  <button class="btn" data-tag="Document-AI">Document-AI</button>
  <button class="btn" data-tag="LLM">LLM</button>
  <button class="btn" data-tag="Evaluation">Evaluation</button>
  <button class="btn" data-tag="Ranking">Ranking</button>
  <button class="btn" data-tag="Retrieval">Retrieval</button>
  <button class="btn" data-tag="Safety">Safety</button>
  <button class="btn" data-tag="Systems">Systems</button>
</div>

<div class="projects-grid">
  {%- comment -%}
    Source: we build cards from your curated projects list below.
    Add/edit items right here – each needs: title, org, year, bullets[], tags[], and optional ctas[].
  {%- endcomment -%}
  {%- assign projects =  site.data.projects | default: "" -%}
  {%- if projects == "" -%}
    {%- assign projects =  array -%}
    {%- assign projects = projects | push:
      {
        "title":"Accesseval — Benchmarking disability bias in LLMs",
        "org":"Oracle Cloud Infrastructure",
        "year":"2025",
        "tags":["LLM","Safety","Evaluation","Document-AI"],
        "bullets":[
          "Built bias measurement slices and procedures; drove Best Paper — Social Impact at EMNLP 2025.",
          "Open, extensible task templates for continuous fairness monitoring."
        ],
        "ctas":[{"label":"Publication","href":"/publications/accesseval-benchmarking-disability-bias"}]
      }
    -%}
    {%- assign projects = projects | push:
      {
        "title":"GenAI Evaluation Platform (LLM/RAG)",
        "org":"Oracle Cloud Infrastructure",
        "year":"2025",
        "tags":["LLM","Retrieval","Evaluation","Safety","Systems"],
        "bullets":[
          "Shipped an evaluation harness and dashboards used across orgs.",
          "Regression-proofed ranking/retrieval with measurable quality bars and alerts.",
          "Reduced serving cost ~20–30% via ranking/latency trade-offs without quality loss."
        ],
        "ctas":[{"label":"Notes","href":"#"}]
      }
    -%}
    {%- assign projects = projects | push:
      {
        "title":"Safety & Guardrails for GenAI Features",
        "org":"Oracle Cloud Infrastructure",
        "year":"2025",
        "tags":["Safety","LLM","Systems"],
        "bullets":[
          "Guardrails and policy checks integrated into product surfaces.",
          "Red-teaming playbooks and auto-tests wired into CI."
        ]
      }
    -%}
    {%- assign projects = projects | push:
      {
        "title":"LLM Retrieval + Ranking Optimization",
        "org":"Oracle Cloud Infrastructure",
        "year":"2025",
        "tags":["Retrieval","Ranking","LLM","Systems"],
        "bullets":[
          "Hybrid retrieval stack with learned re-rankers and quality gates.",
          "Latency-aware ranking with SLAs for enterprise scenarios."
        ]
      }
    -%}
  {%- endif -%}

  {%- for p in projects -%}
  <article class="project-card" data-tags="{{ p.tags | join: ' ' }}">
    <div class="proj-title">{{ p.title }}</div>

    <div class="badges">
      <span class="pill">{{ p.org }}</span>
      <span class="pill">{{ p.year }}</span>
      {%- for t in p.tags -%}
        <span class="pill tag">{{ t }}</span>
      {%- endfor -%}
    </div>

    <ul style="margin:.2rem 0 .6rem 1.1rem;">
      {%- for b in p.bullets -%}
        <li style="margin:.25rem 0">{{ b }}</li>
      {%- endfor -%}
    </ul>

    {%- if p.ctas and p.ctas.size > 0 -%}
    <div class="cta-row">
      {%- for c in p.ctas -%}
        <a class="cta" href="{{ c.href | relative_url }}" target="{{ c.target | default: '_self' }}">{{ c.label }}</a>
      {%- endfor -%}
    </div>
    {%- endif -%}
  </article>
  {%- endfor -%}
</div>

<script>
  // Tag -> gradient palette
  const palette = {
    "LLM":            ["#7c3aed","#a78bfa"],
    "Retrieval":      ["#10b981","#34d399"],
    "Ranking":        ["#22c55e","#86efac"],
    "Document-AI":    ["#0ea5e9","#22d3ee"],
    "Evaluation":     ["#06b6d4","#67e8f9"],
    "Safety":         ["#f97316","#f59e0b"],
    "Systems":        ["#64748b","#94a3b8"]
  };
  // Fallback cycle if no known tag is present
  const cycle = [
    ["#22c55e","#86efac"],
    ["#0ea5e9","#22d3ee"],
    ["#7c3aed","#a78bfa"],
    ["#f97316","#f59e0b"],
    ["#10b981","#34d399"],
    ["#06b6d4","#67e8f9"]
  ];

  // Apply per-card accent based on the first matching tag
  document.querySelectorAll('.project-card').forEach((card, i) => {
    const tags = (card.dataset.tags || "").split(/\s+/).filter(Boolean);
    let picked = null;
    for (const t of tags){ if (palette[t]) { picked = palette[t]; break; } }
    if (!picked) picked = cycle[i % cycle.length];
    card.style.setProperty('--accentA', picked[0]);
    card.style.setProperty('--accentB', picked[1]);
  });

  // Simple tag filter (optional; remove if you already wired one)
  const btns  = document.querySelectorAll('#proj-filters .btn');
  const cards = Array.from(document.querySelectorAll('.project-card'));
  function setActive(tag){
    cards.forEach(el=>{
      const tags = (el.dataset.tags||"").split(/\s+/);
      el.style.display = (tag==="all" || tags.includes(tag)) ? "" : "none";
    });
    btns.forEach(b=>b.classList.remove('btn--primary'));
    document.querySelector(`#proj-filters .btn[data-tag="${tag}"]`)?.classList.add('btn--primary');
  }
  btns.forEach(b => b.addEventListener('click', ()=> setActive(b.dataset.tag)));
</script>
