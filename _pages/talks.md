---
permalink: /talks/
title: "Talks"
layout: single
author_profile: true
classes: wide
---

<style>
  /* Layout: 2-column venue grid */
  .venue-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:2rem;margin-top:.5rem;}
  @media(max-width:1100px){.venue-grid{grid-template-columns:1fr}}
  .venue-col{min-width:0;}

  /* Venue heading (links to official site if provided) */
  .venue-title{margin:.5rem 0 1rem;font-size:1.35rem;font-weight:800;}
  .venue-title a{text-decoration:none;border-bottom:2px solid transparent}
  .venue-title a:hover{border-color:var(--brand-accent,#0ea5e9)}

  /* Card list inside each venue */
  .talks-list{display:grid;grid-template-columns:1fr;gap:1rem;}

  .talk-card{background:var(--mm-surface,#fff);border:1px solid rgba(0,0,0,.08);
             border-radius:16px;overflow:hidden;box-shadow:0 1px 2px rgba(0,0,0,.04)}
  html.theme-dark .talk-card{background:#0b1220;border-color:#1f2937;box-shadow:none}

  .talk-cover img{display:block;width:100%;height:180px;object-fit:cover}
  .talk-placeholder{height:180px;display:flex;align-items:center;justify-content:center;opacity:.6}

  .talk-meta{padding:.75rem 1rem 1rem}
  .talk-title{display:flex;flex-wrap:wrap;gap:.5rem;align-items:center;margin:0;font-size:1.05rem;line-height:1.35}
  .talk-title a{text-decoration:none}
  .talk-title a:hover{text-decoration:underline}

  /* Badges next to the title */
  .badge-year{background:#f1f5f9;border:1px solid #cbd5e1;color:#0f172a;
              padding:.12rem .55rem;border-radius:999px;font-weight:700;font-size:.8rem}
  html.theme-dark .badge-year{background:#0f172a;border-color:#1f2937;color:#e6edf3}

  .badge{display:inline-block;padding:.12rem .6rem;border-radius:999px;
         font-weight:700;font-size:.8rem;text-decoration:none;transition:.15s ease}
  .badge-event{border:1px solid var(--brand-accent,#0ea5e9)}
  .badge-event:hover{background:var(--brand-accent,#0ea5e9);color:#fff}
  .badge-pdf{border:1px solid #ef4444}
  .badge-pdf:hover{background:#ef4444;color:#fff}
</style>

{% assign talks_all = site.talks | sort: "year" | reverse %}
{% assign by_venue = talks_all | group_by: "venue" %}

<div class="venue-grid">
  {% for v in by_venue %}
    {% assign venue_slug = v.name | slugify %}
    {% assign venue_meta = site.data.venues[venue_slug] %}

    <section class="venue-col">
      <h2 class="venue-title">
        {% if venue_meta and venue_meta.url %}
          <a href="{{ venue_meta.url }}" target="_blank" rel="noopener">{{ v.name }}</a>
        {% else %}
          {{ v.name }}
        {% endif %}
      </h2>

      <div class="talks-list">
        {% assign items = v.items | sort: "year" | reverse %}
        {% for t in items %}
          {% assign event_url = t.link_url | default: t.event_url | default: t.website | default: t.site_url %}
          <article class="talk-card">
            <a class="talk-cover" href="{{ t.url | relative_url }}">
              {% if t.images and t.images[0] %}
                <img src="{{ t.images[0] | relative_url }}" alt="{{ t.title | escape }}">
              {% else %}
                <div class="talk-placeholder">Talk</div>
              {% endif %}
            </a>

            <div class="talk-meta">
              <h3 class="talk-title">
                <a href="{{ t.url | relative_url }}">{{ t.title }}</a>
                {% if t.year %}<span class="badge-year">{{ t.year }}</span>{% endif %}
                {% if event_url %}<a class="badge badge-event" href="{{ event_url }}" target="_blank" rel="noopener">Event</a>{% endif %}
                {% if t.pdf_url %}<a class="badge badge-pdf" href="{{ t.pdf_url | relative_url }}" target="_blank" rel="noopener">PDF</a>{% endif %}
              </h3>
            </div>
          </article>
        {% endfor %}
      </div>
    </section>
  {% endfor %}
</div>
