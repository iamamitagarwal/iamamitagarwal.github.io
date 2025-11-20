---
permalink: /media/
title: "Media"
layout: single
author_profile: true
classes: wide
---

<style>
  /* Masonry grid */
  .masonry{ column-count:3; column-gap:1rem; }
  @media(max-width:1200px){ .masonry{ column-count:2; } }
  @media(max-width:720px){ .masonry{ column-count:1; } }

  .masonry-item{ break-inside:avoid; margin:0 0 1rem; width:100%; }

  /* Card + image (no cropping) */
  .media-card{
    position:relative; overflow:hidden; border-radius:14px;
    border:1px solid rgba(0,0,0,.08); background:#fff;
  }
  .media-card img{
    width:100%; height:auto; display:block;
    object-fit:contain; /* keep the whole image visible */
    background:#f3f4f6; /* neutral pad for transparent images */
  }

  /* Overlay actions */
  .media-actions{
    position:absolute; left:0; right:0; bottom:0;
    display:flex; gap:.5rem; padding:.5rem .6rem;
    background:linear-gradient(180deg, rgba(0,0,0,0) 0%, rgba(0,0,0,.45) 80%);
  }
  .pill{
    display:inline-flex; align-items:center; gap:.35rem;
    padding:.28rem .65rem; border-radius:999px; font-weight:700; font-size:.85rem;
    border:1px solid #0ea5e9; color:#fff; text-decoration:none;
    backdrop-filter:saturate(140%) blur(2px);
  }
  .pill:hover{ background:#0ea5e9; }
  .pill--pdf{ border-color:#ef4444; }
  .pill--pdf:hover{ background:#ef4444; }

  html.theme-dark .media-card{ border-color:#1f2937; background:#0b1220; }
</style>

{%- comment -%}
Expected folders (case-sensitive):
  /assets/media/Picture/  -> images (png, jpg, jpeg, webp, gif)
  /assets/media/Media/    -> PDFs with same *logical* name (slugified match ok)
Optionally add site links in either:
  _data/media_links.yml  OR  _data/media.yml
with keys = base name or slugified base name.
{%- endcomment -%}

{% assign picture_root_lc = "/assets/media/picture/" %}
{% assign pdf_root_lc     = "/assets/media/media/" %}

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
  {% if p contains picture_root_lc %}
    {% assign ext = f.extname | downcase %}
    {% if ext == ".png" or ext == ".jpg" or ext == ".jpeg" or ext == ".webp" or ext == ".gif" %}
      {% assign base = f.name | remove: f.extname %}
      {% assign key  = base | slugify: 'pretty' | replace: '-', '' | replace: '_','' %}

      {%- comment -%} Fuzzy PDF match by slug {%- endcomment -%}
      {% assign pdf_hit = nil %}
      {% for sf in site.static_files %}
        {% assign sp = sf.path | downcase %}
        {% if sp contains pdf_root_lc and sf.extname %}
          {% assign pbase = sf.name | remove: sf.extname %}
          {% assign pkey  = pbase | slugify: 'pretty' | replace: '-', '' | replace: '_','' %}
          {% if pkey == key %}
            {% assign pdf_hit = sf %}
            {% break %}
          {% endif %}
        {% endif %}
      {% endfor %}

      {% if linkmap %}
        {% assign site_link = linkmap[base] | default: linkmap[key] | default: "#" %}
      {% else %}
        {% assign site_link = "#" %}
      {% endif %}

      {% assign found_any = true %}

      <figure class="masonry-item media-card">
        <img src="{{ f.path | relative_url }}" alt="{{ base | escape }}" loading="lazy">
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
<p><em>No media found under <code>/assets/media/Picture/</code>. Double-check folder names and file types (.png, .jpg, .jpeg, .webp, .gif). PDFs go in <code>/assets/media/Media/</code>.</em></p>
{% endunless %}
