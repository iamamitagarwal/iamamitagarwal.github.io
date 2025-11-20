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
    width:100%; height:auto; display:block; object-fit:cover; aspect-ratio:16/9;
    transition:transform .35s ease;
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

{% assign picture_root = "/assets/media/Picture/" %}
{% assign pdf_root     = "/assets/media/Media/" %}

{%- comment -%}
Collect all images under picture_root. We do filtering of extensions OUTSIDE where_exp
to stay compatible with GitHub Pages.
{%- endcomment -%}
{% assign pictures = site.static_files | where_exp: "f", "f.path contains picture_root" | sort: "name" %}

<div class="media-grid">
{% for pic in pictures %}
  {% assign ext = pic.extname | downcase %}
  {% if ext == ".png" or ext == ".jpg" or ext == ".jpeg" or ext == ".webp" or ext == ".gif" %}
    {% assign base = pic.name | remove: pic.extname %}

    {%- comment -%} Precompute potential PDF paths (both .pdf and .PDF) {%- endcomment -%}
    {% assign pdf_path1 = pdf_root | append: base | append: ".pdf" %}
    {% assign pdf_path2 = pdf_root | append: base | append: ".PDF" %}

    {%- comment -%} This where_exp uses only variables and == / or (no filters) {%- endcomment -%}
    {% assign pdf_match = site.static_files | where_exp:"f","f.path == pdf_path1 or f.path == pdf_path2" %}

    {%- comment -%} Optional external site link from _data/media_links.yml (basename -> url) {%- endcomment -%}
    {% if site.data.media_links %}
      {% assign site_link = site.data.media_links[base] | default: "#" %}
    {% else %}
      {% assign site_link = "#" %}
    {% endif %}

    <figure class="media-card">
      <img src="{{ pic.path | relative_url }}" alt="{{ base | escape }}">
      <figcaption class="media-actions">
        {% if pdf_match and pdf_match.size > 0 %}
          <a class="pill pill--pdf" href="{{ pdf_match[0].path | relative_url }}" target="_blank" rel="noopener">PDF</a>
        {% endif %}
        <a class="pill" href="{{ site_link }}" target="_blank" rel="noopener">Site</a>
      </figcaption>
    </figure>
  {% endif %}
{% endfor %}
</div>
