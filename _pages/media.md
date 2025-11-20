---
permalink: /media/
title: "Media"
layout: single
author_profile: true
classes: wide
---

<style>
  /* Masonry columns – it will auto-flow as you add media */
  .masonry{ column-count:3; column-gap:1rem; }
  @media (max-width:1200px){ .masonry{ column-count:2; } }
  @media (max-width:720px){  .masonry{ column-count:1; } }

  .masonry-item{ break-inside:avoid; width:100%; margin:0 0 1rem; }

  /* ===== Parchment newspaper clipping ===== */
  .media-card{
    position:relative;
    border-radius:14px;
    background:#fffaf1;               /* parchment */
    border:1px solid #e7dbc7;         /* paper edge */
    box-shadow:
      0 10px 18px rgba(0,0,0,.07),
      0 1px 3px rgba(0,0,0,.06);
    overflow:hidden;
    transform:rotate(-.18deg);        /* tiny hand-made feel */
  }
  .media-card:nth-child(2n){ transform:rotate(.15deg) }
  .media-card:nth-child(3n){ transform:rotate(-.08deg) }

  /* soft vignette + curled corners */
  .media-card::after{
    content:"";
    position:absolute; inset:0; pointer-events:none;
    background:
      radial-gradient(1200px 600px at 8% -200px, rgba(0,0,0,.06), transparent 60%),
      radial-gradient(900px 500px at 112% 120%, rgba(0,0,0,.05), transparent 55%);
    mix-blend-mode:multiply; opacity:.5;
  }
  .media-card::before{
    content:"";
    position:absolute; inset:-1px;
    background:
      radial-gradient(35px 35px at left top, rgba(0,0,0,.10), transparent 60%) top left no-repeat,
      radial-gradient(35px 35px at right top, rgba(0,0,0,.10), transparent 60%) top right no-repeat,
      radial-gradient(35px 35px at left bottom, rgba(0,0,0,.08), transparent 60%) bottom left no-repeat,
      radial-gradient(35px 35px at right bottom, rgba(0,0,0,.08), transparent 60%) bottom right no-repeat;
    background-size:36px 36px,36px 36px,36px 36px,36px 36px;
    opacity:.25; pointer-events:none;
  }

  /* “taped” label – warm sticky-note tone (smaller) */
  .tape{
    position:absolute; top:8px; left:50%;
    transform:translateX(-50%) rotate(-2deg);
    padding:.28rem .7rem;
    background:#f7ecd5;             /* warm */
    color:#1f2937;
    font-weight:800; font-size:.8rem;
    border:1px solid #eadfca;
    border-radius:6px;
    box-shadow:0 3px 8px rgba(0,0,0,.08);
    max-width:85%;
    text-align:center;
    white-space:nowrap; overflow:hidden; text-overflow:ellipsis;
  }

  .media-img{ width:100%; background:#f4f2ee; }
  .media-img img{ display:block; width:100%; height:auto; object-fit:contain; }

  .media-foot{
    display:flex; align-items:center; justify-content:flex-end;
    gap:.45rem; padding:.5rem .6rem .65rem;
    background:linear-gradient(180deg, rgba(0,0,0,0) 0%, rgba(0,0,0,.05) 100%);
  }

  .pill{
    display:inline-flex; align-items:center; gap:.4rem;
    padding:.28rem .62rem; border-radius:999px;
    font-weight:800; font-size:.8rem; letter-spacing:.01em;
    border:1px solid #7aa6b1; color:#10343d; text-decoration:none;
    background:#eef7f9; box-shadow:0 1px 0 rgba(255,255,255,.85) inset;
  }
  .pill svg{ width:15px; height:15px; }
  .pill:hover{ background:#2d8fa2; color:#fff; border-color:#2d8fa2; }

  .pill--pdf{ border-color:#d44; background:#fff1f1; color:#6b1010; }
  .pill--pdf:hover{ background:#d44; color:#fff; }

  /* Dark mode */
  html.theme-dark .media-card{ background:#0b1220; border-color:#1f2937; box-shadow:none; }
  html.theme-dark .tape{ background:#2a2b26; color:#f4f1e8; border-color:#3a3b33; }
  html.theme-dark .pill{ background:#0e2a31; color:#d7eef6; border-color:#2aaec4; }
  html.theme-dark .pill--pdf{ background:#2a1212; border-color:#f87171; color:#ffe2e2; }
</style>

{% assign pictures_dir = "/assets/media/pictures/" %}
{% assign pdfs_dir     = "/assets/media/pdfs/" %}

{%- comment -%} Prefer media_links.yml; fallback to media.yml {%- endcomment -%}
{% if site.data.media_links %}{% assign linkmap = site.data.media_links %}
{% elsif site.data.media %}{% assign linkmap = site.data.media %}
{% else %}{% assign linkmap = nil %}{% endif %}

{% assign found_any = false %}

<div class="masonry">
{% for f in site.static_files %}
  {% assign p = f.path | downcase %}
  {% if p contains pictures_dir %}
    {% assign ext = f.extname | downcase %}
    {% if ext == ".png" or ext == ".jpg" or ext == ".jpeg" or ext == ".webp" or ext == ".gif" %}

      {% assign base       = f.name | remove: f.extname %}
      {% assign slug_base  = base  | slugify: 'pretty' %}
      {% assign tight_base = slug_base | replace: '-', '' | replace: '_','' %}

      {%- comment -%} Match a PDF by normalized slug (== or contains both ways) {%- endcomment -%}
      {% assign pdf_hit = nil %}
      {% for sf in site.static_files %}
        {% assign sp = sf.path | downcase %}
        {% if sp contains pdfs_dir and sf.extname %}
          {% assign pbase   = sf.name | remove: sf.extname %}
          {% assign pslug   = pbase | slugify: 'pretty' %}
          {% assign ptight  = pslug | replace: '-', '' | replace: '_','' %}
          {% if ptight == tight_base or ptight contains tight_base or tight_base contains ptight %}
            {% assign pdf_hit = sf %}{% break %}
          {% endif %}
        {% endif %}
      {% endfor %}

      {%- comment -%} Robust data lookup: try direct keys, then scan all keys normalized {%- endcomment -%}
      {% assign entry = nil %}
      {% if linkmap %}
        {% assign entry = linkmap[base] | default: linkmap[slug_base] | default: linkmap[tight_base] %}
        {% if entry == nil %}
          {% for pair in linkmap %}
            {% assign k = pair[0] %}
            {% assign v = pair[1] %}
            {% assign kslug  = k | slugify: 'pretty' %}
            {% assign ktight = kslug | replace: '-', '' | replace: '_','' %}
            {% if ktight == tight_base or tight_base contains ktight or ktight contains tight_base %}
              {% assign entry = v %}{% break %}
            {% endif %}
          {% endfor %}
        {% endif %}
      {% endif %}

      {% assign site_link = "" %}
      {% assign title_override = nil %}
      {% assign pdf_manual = nil %}

      {% if entry %}
        {% if entry.site or entry.title or entry.pdf %}
          {% assign site_link     = entry.site  | default: "" | strip %}
          {% assign title_override = entry.title %}
          {% assign pdf_manual     = entry.pdf %}
        {% else %}
          {% assign site_link = entry | default: "" | strip %}
        {% endif %}
      {% endif %}

      {% if pdf_manual %}
        {% assign pdf_hit = nil %}
        {% for sf in site.static_files %}
          {% assign sp2 = sf.path | downcase %}
          {% if sp2 contains pdfs_dir and sf.name == pdf_manual %}
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
            <a class="pill pill--pdf" href="{{ pdf_hit.path | relative_url }}" target="_blank" rel="noopener">
              <svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M14 2H6a2 2 0 0 0-2 2v16c0 1.1.9 2 2 2h12a2 2 0 0 0 2-2V8l-6-6Zm1 7V3.5L19.5 9H15Z"/><path fill="currentColor" d="M7 14h10v2H7zm0-4h7v2H7z"/></svg>
              PDF
            </a>
          {% endif %}
          {% unless site_link == nil or site_link == "" or site_link == blank %}
            <a class="pill" href="{{ site_link }}" target="_blank" rel="noopener">
              <svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 4a8 8 0 1 0 0 16A8 8 0 0 0 12 4Zm6.9 7h-3.1a13 13 0 0 0-1-4.3A6 6 0 0 1 18.9 11ZM12 6c.8 0 2 1.7 2.6 5H9.4C10 7.7 11.2 6 12 6Zm-3.8.7A13 13 0 0 0 7.2 11H4.1a6 6 0 0 1 4.1-4.3ZM4.1 13h3.1a13 13 0 0 0 1 4.3A6 6 0 0 1 4.1 13ZM12 18c-.8 0-2-1.7-2.6-5h5.2C14 16.3 12.8 18 12 18Zm3.8-.7A13 13 0 0 0 16.8 13h3.1a6 6 0 0 1-4.1 4.3Z"/></svg>
              Site
            </a>
          {% endunless %}
        </div>
      </figure>

    {% endif %}
  {% endif %}
{% endfor %}
</div>

{% unless found_any %}
<p><em>No media found under <code>/assets/media/pictures/</code>. PDFs go in <code>/assets/media/pdfs/</code>. Add optional titles/links in <code>_data/media.yml</code>.</em></p>
{% endunless %}
