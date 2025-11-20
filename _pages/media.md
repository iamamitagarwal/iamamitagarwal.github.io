---
permalink: /media/
title: "Media"
layout: single
author_profile: true
classes: wide
---

<style>
  .media-grid{
    display:grid;
    grid-template-columns:repeat(3,minmax(0,1fr));
    gap:1rem;
  }
  @media(max-width:1200px){ .media-grid{ grid-template-columns:repeat(2,minmax(0,1fr)); } }
  @media(max-width:720px){ .media-grid{ grid-template-columns:1fr; } }

  .media-card{
    position:relative; overflow:hidden; border-radius:14px;
    border:1px solid rgba(0,0,0,.08); background:#fff;
  }
  .media-card img{
    width:100%; height:auto; display:block; object-fit:cover;
    aspect-ratio:16/9; transition:transform .35s ease;
  }
  .media-card:hover img{ transform:scale(1.02); }

  .media-actions{
    position:absolute; left:0; right:0; bottom:0;
    display:flex; gap:.5rem; padding:.5rem .6rem;
    background:linear-gradient(180deg, rgba(0,0,0,0) 0%, rgba(0,0,0,.45) 80%);
  }
  .pill{
    display:inline-flex; align-items:center; gap:.35rem;
    padding:.28rem .65rem; border-radius:999px; font-weight:700; font-size:.85rem;
    border:1px solid #0ea5e9; color:#fff; text-decoration:none; backdrop-filter:saturate(140%) blur(2px);
  }
  .pill:hover{ background:#0ea5e9; }
  .pill--pdf{ border-color:#ef4444; }
  .pill--pdf:hover{ background:#ef4444; }
  html.theme-dark .media-card{ border-color:#1f2937; background:#0b1220; }
</style>

{%- comment -%}
We compare lowercased paths to be resilient to case differences.
Expected folders:
  - /assets/media/pictures/  (images)
  - /assets/media/pdfs/    (PDFs)
{%- endcomment -%}
{% assign picture_root_lc = "/assets/media/pictures/" %}
{% assign pdf_root_lc     = "/assets/media/pdfs/" %}

{%- comment -%} read optional link map from either file {%- endcomment -%}
{% if site.data.media_links %}
  {% assign linkmap = site.data.media_links %}
{% elsif site.data.media %}
  {% assign linkmap = site.data.media %}
{% else %}
  {% assign linkmap = nil %}
{% endif %}

{% assign found_any = false %}

<div class="media-grid">
{% for f in site.static_files %}
  {% assign p = f.path | downcase %}
  {% if p contains picture_root_lc %}
    {% assign ext = f.extname | downcase %}
    {% if ext == ".png" or ext == ".jpg" or ext == ".jpeg" or ext == ".webp" or ext == ".gif" %}
      {% assign base = f.name | remove: f.extname %}

      {%- comment -%} find matching PDF (case-insensitive) {%- endcomment -%}
      {% assign pdf1 = pdf_root_lc | append: base | append: ".pdf" %}
      {% assign pdf2 = pdf_root_lc | append: base | append: ".PDF" %}
      {% assign pdf_hit = nil %}
      {% for sf in site.static_files %}
        {% assign sp = sf.path | downcase %}
        {% if sp == pdf1 or sp == pdf2 %}
          {% assign pdf_hit = sf %}
          {% break %}
        {% endif %}
      {% endfor %}

      {% if linkmap %}
        {% assign site_link = linkmap[base] | default: "#" %}
      {% else %}
        {% assign site_link = "#" %}
      {% endif %}

      {% assign found_any = true %}

      <figure class="media-card">
        <img src="{{ f.path | relative_url }}" alt="{{ base | escape }}">
        <figcaption class="media-actions">
          {% if pdf_hit %}
            <a class="pill pill--pdf" href="{{ pdf_hit.path | relative_url }}" target="_blank" rel="noopener">PDF</a>
          {% endif %}
          <a class="pill" href="{{ site_link }}" target="_blank" rel="noopener">Site</a>
        </figcaption>
      </figure>
    {% endif %}
  {% endif %}
{% endfor %}
</div>

{% unless found_any %}
<p><em>No media found under <code>/assets/media/pictures/</code>. Double-check folder names and file types (.png, .jpg, .jpeg, .webp, .gif). PDFs should live in <code>/assets/media/pdfs/</code> with the same base filename.</em></p>
{% endunless %}
