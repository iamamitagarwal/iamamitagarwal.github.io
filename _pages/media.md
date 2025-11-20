---
permalink: /media/
title: "Media"
layout: single
author_profile: true
classes: wide
---

<style>
  /* Masonry layout – auto-fills as you add more */
  .masonry{ column-count:3; column-gap:1.2rem; }
  @media(max-width:1200px){ .masonry{ column-count:2; } }
  @media(max-width:720px){ .masonry{ column-count:1; } }

  .masonry-item{ break-inside:avoid; width:100%; margin:0 0 1.2rem; }

  /* ===== Newspaper clipping card ===== */
  .media-card{
    position:relative;
    border-radius:16px;
    background:#fffdfa;                           /* warm paper */
    border:1px solid #e5e7eb;                     /* paper edge */
    box-shadow:
      0 12px 22px rgba(0,0,0,.08),
      0 2px 5px rgba(0,0,0,.06);
    overflow:hidden;
    transform: rotate(-.25deg);
  }
  /* tiny random feel */
  .media-card:nth-child(2n){ transform: rotate(.2deg); }
  .media-card:nth-child(3n){ transform: rotate(-.1deg); }

  /* subtle deckled edge by masking a gradient fringe */
  .media-card::after{
    content:"";
    position:absolute; inset:0;
    pointer-events:none;
    background:
      radial-gradient(1200px 600px at 10% -200px, rgba(0,0,0,.06), transparent 60%),
      radial-gradient(900px 500px at 110% 120%, rgba(0,0,0,.05), transparent 55%);
    mix-blend-mode:multiply;
    opacity:.5;
  }

  /* header “tape” */
  .tape{
    position:absolute; top:10px; left:50%;
    transform:translateX(-50%) rotate(-2deg);
    padding:.3rem .8rem;
    background:#fef3c7;                           /* sticky note */
    color:#312e2b; font-weight:800; font-size:.85rem;
    border:1px solid #e5d5aa; border-radius:6px;
    box-shadow:0 4px 10px rgba(0,0,0,.08);
    max-width:85%;
    text-align:center;
    white-space:nowrap; overflow:hidden; text-overflow:ellipsis;
  }

  /* image — never crop */
  .media-img{
    width:100%;
    background:#f4f6f8;
  }
  .media-img img{
    display:block;
    width:100%; height:auto; object-fit:contain;
  }

  /* footer bar with actions */
  .media-foot{
    display:flex; align-items:center; justify-content:flex-end;
    gap:.5rem;
    padding:.55rem .65rem .7rem;
    background:linear-gradient(180deg, rgba(0,0,0,0) 0%, rgba(0,0,0,.05) 100%);
  }

  .pill{
    display:inline-flex; align-items:center; gap:.35rem;
    padding:.28rem .7rem; border-radius:999px;
    font-weight:800; font-size:.85rem; letter-spacing:.01em;
    border:1px solid #0ea5e9; color:#0b1320; text-decoration:none;
    background:#ecfeff;
    box-shadow:0 1px 0 rgba(255,255,255,.8) inset;
  }
  .pill:hover{ background:#0ea5e9; color:#fff; }
  .pill--pdf{ border-color:#ef4444; background:#fff1f1; }
  .pill--pdf:hover{ background:#ef4444; color:#fff; }

  html.theme-dark .media-card{
    background:#0b1220; border-color:#1f2937;
    box-shadow: none;
  }
  html.theme-dark .tape{
    background:#7c6f49; color:#fff; border-color:#6b623f;
  }
  html.theme-dark .pill{ background:#062a30; color:#d7eef6; border-color:#22d3ee; }
  html.theme-dark .pill--pdf{ background:#2a1212; border-color:#f87171; color:#ffe2e2; }
</style>

{%- comment -%}
Folders (case sensitive):
  /assets/media/pictures/   -> png/jpg/jpeg/webp/gif
  /assets/media/pdfs/       -> PDFs with the same base name (slug match is OK)
Optional site/title overrides:
  _data/media.yml
Keys can be the exact base file name OR its slugified form.
{%- endcomment -%}

{% assign pictures_dir = "/assets/media/pictures/" %}
{% assign pdfs_dir     = "/assets/media/pdfs/" %}

{% if site.data.media_links %}
  {% assign linkmap = site.data.media_links %}
{% elsif site.data.media %}
  {% assign linkmap = site.data.media %}
{% else %}
  {% assign linkmap = nil %}
{% endif %}

{% assign found_any = false %}

<div class="masonry">
{% for f in site.static_files %}
  {% assign p = f.path | downcase %}
  {% if p contains pictures_dir %}
    {% assign ext = f.extname | downcase %}
    {% if ext == ".png" or ext == ".jpg" or ext == ".jpeg" or ext == ".webp" or ext == ".gif" %}
      {% assign base = f.name | remove: f.extname %}
      {% assign slug_key = base | slugify: 'pretty' %}
      {% assign tight_key = slug_key | replace: '-', '' | replace: '_','' %}

      {#— locate matching PDF by slug —#}
      {% assign pdf_hit = nil %}
      {% for sf in site.static_files %}
        {% assign sp = sf.path | downcase %}
        {% if sp contains pdfs_dir and sf.extname %}
          {% assign pbase = sf.name | remove: sf.extname %}
          {% assign pkey  = pbase | slugify: 'pretty' | replace: '-', '' | replace: '_','' %}
          {% if pkey == tight_key %}
            {% assign pdf_hit = sf %}
            {% break %}
          {% endif %}
        {% endif %}
      {% endfor %}

      {#— resolve site link + title from _data/media.yml —#}
      {% assign entry = nil %}
      {% if linkmap %}
        {% assign entry = linkmap[base] | default: linkmap[slug_key] | default: linkmap[tight_key] %}
      {% endif %}

      {% assign site_link = nil %}
      {% assign title_override = nil %}
      {% assign pdf_manual = nil %}

      {% if entry %}
        {% if entry.site or entry.title or entry.pdf %}
          {% assign site_link = entry.site %}
          {% assign title_override = entry.title %}
          {% assign pdf_manual = entry.pdf %}
        {% else %}
          {% assign site_link = entry %}
        {% endif %}
      {% endif %}

      {% if pdf_manual %}
        {% assign pdf_hit = nil %}
        {% for sf in site.static_files %}
          {% if sf.path contains pdfs_dir and sf.name == pdf_manual %}
            {% assign pdf_hit = sf %}{% break %}
          {% endif %}
        {% endfor %}
      {% endif %}

      {% assign display_title = title_override | default: base %}

      {% assign found_any = true %}

      <figure class="masonry-item media-card">
        <div class="tape" title="{{ display_title }}">{{ display_title }}</div>

        <div class="media-img">
          <img src="{{ f.path | relative_url }}" alt="{{ display_title | escape }}" loading="lazy">
        </div>

        <div class="media-foot">
          {% if pdf_hit %}
            <a class="pill pill--pdf" href="{{ pdf_hit.path | relative_url }}" target="_blank" rel="noopener">PDF</a>
          {% endif %}
          <a class="pill" href="{{ site_link | default:'#' }}" target="_blank" rel="noopener">Site</a>
        </div>
      </figure>

    {% endif %}
  {% endif %}
{% endfor %}
</div>

{% unless found_any %}
<p><em>No media found under <code>/assets/media/pictures/</code>. PDFs go in <code>/assets/media/pdfs/</code>. Add optional titles/links in <code>_data/media.yml</code>.</em></p>
{% endunless %}
