---
permalink: /awards/
title: "Awards"
layout: single
author_profile: true
classes: wide
---

<style>
  :root{
    --ink:#0b1320; --muted:#6b7280; --line:#e5e7eb; --paper:#fffdfa;
    --accent:#0ea5e9; --accent-2:#f59e0b;
  }
  .awards-grid{ display:grid; grid-template-columns:360px 1px minmax(0,1fr); gap:2rem; align-items:start; }
  @media (max-width:1100px){ .awards-grid{ grid-template-columns:1fr; } .awards-divider{ display:none; } }
  .awards-divider{ width:1px; background:linear-gradient(180deg,transparent,var(--line),transparent); }

  .awards-metrics{ display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:1rem; }
  .metric{ background:var(--paper); border:1px solid var(--line); border-radius:20px; padding:1.1rem 1rem;
           box-shadow:0 10px 18px rgba(0,0,0,.06), 0 2px 5px rgba(0,0,0,.04); }
  .metric__num{ font-size:2.2rem; font-weight:800; line-height:1.1; color:var(--ink); }
  .metric__label{ margin-top:.2rem; color:var(--muted); font-weight:600; letter-spacing:.01em; }
  .metric--accent{ border-color: rgba(14,165,233,.35); }
  .metric--gold{ border-color: rgba(245,158,11,.35); }

  .best-card{ margin-top:1rem; background:#fff; border:1px solid var(--line); border-radius:16px; padding:1rem;
              box-shadow:0 8px 16px rgba(0,0,0,.05); }
  .best-card h4{ margin:.1rem 0 .6rem; font-weight:900; }
  .best-item{ display:flex; gap:.5rem; align-items:flex-start; margin:.35rem 0; }
  .best-medal{ font-size:1rem; line-height:1.25rem; }
  .best-item a{ font-weight:700; text-decoration:none; }
  .best-item a:hover{ text-decoration:underline; }

  .awards-list{ display:flex; flex-direction:column; gap:1rem; }
  .award{ background:#fff; border:1px solid var(--line); border-radius:16px; padding:1.0rem 1.1rem; box-shadow:0 8px 16px rgba(0,0,0,.05); }
  .award__head{ display:flex; align-items:center; gap:.6rem; flex-wrap:wrap; margin-bottom:.25rem; }
  .award__title{ margin:0; font-size:1.05rem; font-weight:800; color:var(--ink); }
  .award__badge{ font:700 .75rem/1 system-ui, -apple-system, Segoe UI, Roboto, Inter, Arial;
                 padding:.18rem .5rem; border-radius:999px; border:1px solid var(--line); color:#334155; background:#f8fafc; }
  .award__meta{ color:var(--muted); margin:.15rem 0 .5rem; }
  .award__desc{ margin:.2rem 0 .6rem; }

  .pill{ display:inline-flex; align-items:center; gap:.4rem; padding:.32rem .7rem; border-radius:999px;
         font-weight:800; font-size:.85rem; border:1px solid var(--accent); color:var(--ink);
         text-decoration:none; background:#ecfeff; }
  .pill:hover{ background:var(--accent); color:#fff; }
  .pill--pdf{ border-color:#ef4444; background:#fff1f1; color:#6b1010; }
  .pill--pdf:hover{ background:#ef4444; color:#fff; }
  .pill svg{ width:16px; height:16px }

  html.theme-dark .metric,html.theme-dark .award,html.theme-dark .best-card{ background:#0b1220; border-color:#1f2937; box-shadow:none; }
  html.theme-dark .award__badge{ background:#0f172a; color:#e2e8f0; border-color:#1e293b; }
  html.theme-dark .pill{ background:#062a30; color:#d7eef6; border-color:#22d3ee; }
  html.theme-dark .pill--pdf{ background:#2a1212; color:#ffe2e2; border-color:#f87171; }
</style>

{% comment %}
Compute live counts; keep best_papers configurable via _data/awards_stats.yml (or page.stats).
{% endcomment %}
{% assign papers_total  = site.publications | size %}
{% assign patents_total = site.patents | size %}
{% assign talks_total   = site.talks | size | default: 0 %}
{% assign stats = site.data.awards_stats | default: page.stats %}
{% assign best_list = stats.best_papers %}

<div class="awards-grid">
  <!-- Left: metrics + best-paper list -->
  <section aria-label="Highlights">
    <div class="awards-metrics">
      <div class="metric metric--accent">
        <div class="metric__num">{{ papers_total }}</div>
        <div class="metric__label">papers in top venues</div>
      </div>
      <div class="metric">
        <div class="metric__num">{{ patents_total }}</div>
        <div class="metric__label">patents</div>
      </div>
      <div class="metric">
        <div class="metric__num">&gt;{{ talks_total }}</div>
        <div class="metric__label">talks at tier-1 confs</div>
      </div>
      <div class="metric metric--gold">
        <div class="metric__num">🏅</div>
        <div class="metric__label">best paper awards</div>
      </div>
    </div>

    {% if best_list and best_list.size > 0 %}
    <div class="best-card">
      <h4>Best paper awards</h4>
      {% for bp in best_list %}
        {%- assign link = bp.url -%}
        {%- if link == nil and bp.pub_id -%}
          {%- assign hit = site.publications | where_exp: "p", "p.path contains bp.pub_id" | first -%}
          {%- if hit -%}{%- assign link = hit.url | relative_url -%}{%- endif -%}
        {%- endif -%}
        <div class="best-item">
          <div class="best-medal">🥇</div>
          <div>
            {% if link %}<a href="{{ link }}" target="_blank" rel="noopener">{{ bp.note }}</a>
            {% else %}{{ bp.note }}{% endif %}
          </div>
        </div>
      {% endfor %}
    </div>
    {% endif %}
  </section>

  <div class="awards-divider" aria-hidden="true"></div>

  <!-- Right: award cards from the awards collection -->
  <section aria-label="Awards" class="awards-list">
    {% assign items = site.awards | sort: "year" | reverse %}
    {% for a in items %}
      <article class="award">
        <div class="award__head">
          <h3 class="award__title">{{ a.title }}</h3>
          {% if a.year %}<span class="award__badge">{{ a.year }}</span>{% endif %}
        </div>
        <p class="award__meta">
          {% if a.org %}<strong>{{ a.org }}</strong>{% endif %}
          {% if a.location %} — {{ a.location }}{% endif %}
        </p>
        {% if a.summary %}<p class="award__desc">{{ a.summary }}</p>{% endif %}
        <div class="award__actions">
          {% if a.certificate_url %}
            <a class="pill pill--pdf" href="{{ a.certificate_url }}" target="_blank" rel="noopener">
              <svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M14 2H6a2 2 0 0 0-2 2v16c0 1.1.9 2 2 2h12a2 2 0 0 0 2-2V8l-6-6Zm1 7V3.5L19.5 9H15Z"/><path fill="currentColor" d="M7 14h10v2H7zm0-4h7v2H7z"/></svg>
              Certificate
            </a>
          {% endif %}
          {% if a.link %}
            <a class="pill" href="{{ a.link }}" target="_blank" rel="noopener">
              <svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="m10.59 13.41 6.3-6.3v4.59h2V4h-7.7v2h4.59l-6.3 6.3 1.12 1.11Z"/><path fill="currentColor" d="M19 19H5V5h6V3H5a2 2 0 0 0-2 2v14c0 1.1.9 2 2 2h14a2 2 0 0 0 2-2v-6h-2v6Z"/></svg>
              Details
            </a>
          {% endif %}
        </div>
      </article>
    {% endfor %}
  </section>
</div>
