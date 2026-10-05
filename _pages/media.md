---
permalink: /media/
title: "Media"
layout: single
author_profile: true
classes: wide
description: "Workshop organizing, press coverage, interviews, and media features related to my research and work."
tags: ["Media", "Press", "AI"]
keywords: ["Media", "Press", "Interviews", "AI", "GenAI", "LLM"]
---

<style>
  /* Explicit grid avoids browser-dependent multi-column figure fragmentation. */
  .page__content .media-grid{ display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:1.4rem; margin:0 0 1.4rem; }
  .page__content .media-card{ display:flex; flex-direction:column; float:none; width:auto; min-width:0; margin:0; padding:0; overflow:hidden; background:#fff; border:1px solid #d4e0e8; border-radius:8px; }
  .page__content .media-card .media-img{ width:100%; max-width:none; flex:none; aspect-ratio:16 / 10; overflow:hidden; background:#edf3f7; border-bottom:1px solid #d4e0e8; }
  .page__content .media-card .media-img a{ display:block; float:none; width:100%; height:100%; max-width:none; margin:0; }
  .page__content .media-card .media-img a img{ display:block; width:100%; max-width:none; height:100%; margin:0; object-fit:cover; object-position:top; border:0; border-radius:0; }
  .page__content .workshop-card .media-img{ aspect-ratio:1265 / 712; }
  .page__content .workshop-card .media-img a img{ object-fit:contain; }
  .page__content .media-title{ margin:0; padding:1rem 1rem .5rem; font-size:1rem; line-height:1.4; font-weight:700; border:0; color:#142e42; text-align:left; }
  .media-foot{ display:flex; flex-wrap:wrap; gap:.6rem; margin-top:auto; padding:.4rem 1rem 1rem; }
  .media-foot .pill{ display:inline-flex; align-items:center; gap:.35rem; padding:.35rem .65rem; border:1px solid #a8c6d7; border-radius:4px; background:transparent; color:#07567d; font-size:.75rem; font-weight:600; text-decoration:none; }
  .media-foot .pill svg{ width:15px; height:15px; }
  .media-foot .pill:hover{ background:#e9f5fb; }
  .media-card a:focus-visible{ outline:3px solid #078cc9; outline-offset:-3px; }
  #wnxTab, #contactFab{ display:none; }
  html.theme-dark .media-card{ background:#152533; border-color:#3b5264; }
  html.theme-dark .media-img{ background:#203441; border-color:#3b5264; }
  html.theme-dark .media-title{ color:#f0f6fa; }
  html.theme-dark .media-foot .pill{ color:#a9dfff; border-color:#537d96; }
  html.theme-dark .media-foot .pill:hover{ background:#254256; }
  @media(max-width:700px){
    .page__content .media-grid{ grid-template-columns:minmax(0,1fr); gap:1rem; }

  }
</style>

{% assign pictures_dir = "/assets/media/pictures/" %}
{% assign pdfs_dir     = "/assets/media/pdfs/" %}

{% if site.data.media_links %}{% assign linkmap = site.data.media_links %}
{% elsif site.data.media %}{% assign linkmap = site.data.media %}
{% else %}{% assign linkmap = nil %}{% endif %}

{% assign found_any = false %}

{% assign media_groups = "featured,remaining" | split: "," %}
{% for media_group in media_groups %}
<div class="media-grid">
{% if linkmap %}
  {% for pair in linkmap %}
    {% assign entry_key = pair[0] %}
    {% assign entry = pair[1] %}
    {% if media_group == "featured" and entry.featured != true %}{% continue %}{% endif %}
    {% if media_group == "remaining" and entry.featured == true %}{% continue %}{% endif %}
    {% if entry.image %}
      {% assign display_title = entry.title | default: entry_key %}
      {% assign site_link = entry.site | default: "" | strip %}
      {% assign entry_links = entry.links %}
      {% assign found_any = true %}
      <figure class="media-card{% if entry.image contains '/workshops/' %} workshop-card{% endif %}">
        <div class="media-img">
          <a href="{{ entry.image }}" target="_blank" rel="noopener" aria-label="View full image: {{ display_title | escape }}"><img src="{{ entry.image }}" alt="{{ display_title | escape }}" loading="lazy"></a>
        </div>

        <h2 class="media-title">{{ display_title }}</h2>

        <div class="media-foot">
          {% if entry_links %}
            {% for media_link in entry_links %}
              {% assign media_link_url = media_link.url | default: "" | strip %}
              {% unless media_link_url == nil or media_link_url == "" or media_link_url == blank %}
                <a class="pill" href="{{ media_link_url }}" target="_blank" rel="noopener">
                  <svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 4a8 8 0 1 0 0 16A8 8 0 0 0 12 4Zm6.9 7h-3.1a13 13 0 0 0-1-4.3A6 6 0 0 1 18.9 11ZM12 6c.8 0 2 1.7 2.6 5H9.4C10 7.7 11.2 6 12 6Zm-3.8.7A13 13 0 0 0 7.2 11H4.1a6 6 0 0 1 4.1-4.3ZM4.1 13h3.1a13 13 0 0 0 1 4.3A6 6 0 0 1 4.1 13ZM12 18c-.8 0-2-1.7-2.6-5h5.2C14 16.3 12.8 18 12 18Zm3.8-.7A13 13 0 0 0 16.8 13h3.1a6 6 0 0 1-4.1 4.3Z"/></svg>
                  {{ media_link.label | default: "Site" }}
                </a>
              {% endunless %}
            {% endfor %}
          {% else %}
            {% unless site_link == nil or site_link == "" or site_link == blank %}
              <a class="pill" href="{{ site_link }}" target="_blank" rel="noopener">
                <svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 4a8 8 0 1 0 0 16A8 8 0 0 0 12 4Zm6.9 7h-3.1a13 13 0 0 0-1-4.3A6 6 0 0 1 18.9 11ZM12 6c.8 0 2 1.7 2.6 5H9.4C10 7.7 11.2 6 12 6Zm-3.8.7A13 13 0 0 0 7.2 11H4.1a6 6 0 0 1 4.1-4.3ZM4.1 13h3.1a13 13 0 0 0 1 4.3A6 6 0 0 1 4.1 13ZM12 18c-.8 0-2-1.7-2.6-5h5.2C14 16.3 12.8 18 12 18Zm3.8-.7A13 13 0 0 0 16.8 13h3.1a6 6 0 0 1-4.1 4.3Z"/></svg>
                Site
              </a>
            {% endunless %}
          {% endif %}
        </div>
      </figure>
    {% endif %}
  {% endfor %}
{% endif %}

{% if media_group == "remaining" %}
{% for f in site.static_files %}
  {% assign p = f.path | downcase %}
  {% if p contains pictures_dir %}
    {% assign ext = f.extname | downcase %}
    {% if ext == ".png" or ext == ".jpg" or ext == ".jpeg" or ext == ".webp" or ext == ".gif" %}

      {% assign base       = f.name | remove: f.extname %}
      {% assign slug_base  = base  | slugify: 'pretty' %}
      {% assign tight_base = slug_base | replace: '-', '' | replace: '_','' %}

      {%- comment -%} find matching PDF by normalized slug {%- endcomment -%}
      {% assign pdf_hit = nil %}
      {% for sf in site.static_files %}
        {% assign sp = sf.path | downcase %}
        {% if sp contains pdfs_dir and sf.extname %}
          {% assign pbase  = sf.name | remove: sf.extname %}
          {% assign pslug  = pbase | slugify: 'pretty' %}
          {% assign ptight = pslug | replace: '-', '' | replace: '_','' %}
          {% if ptight == tight_base or ptight contains tight_base or tight_base contains ptight %}
            {% assign pdf_hit = sf %}{% break %}
          {% endif %}
        {% endif %}
      {% endfor %}

      {%- comment -%} look up site/title overrides in _data/media*.yml {%- endcomment -%}
      {% assign entry = nil %}
      {% if linkmap %}
        {% assign entry = linkmap[base] | default: linkmap[slug_base] | default: linkmap[tight_base] %}
        {% if entry == nil %}
          {% for pair in linkmap %}
            {% assign k = pair[0] %}{% assign v = pair[1] %}
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
        {% if entry.image %}
          {% continue %}
        {% endif %}
        {% if entry.site or entry.title or entry.pdf %}
          {% assign site_link = entry.site | default: "" | strip %}
          {% assign title_override = entry.title %}
          {% assign pdf_manual = entry.pdf %}
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

      <figure class="media-card">
        <div class="media-img">
          <a href="{{ f.path | relative_url }}" target="_blank" rel="noopener" aria-label="View full image: {{ display_title | escape }}"><img src="{{ f.path | relative_url }}" alt="{{ display_title | escape }}" loading="lazy"></a>
        </div>

        <h2 class="media-title">{{ display_title }}</h2>

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
{% endif %}
</div>
{% endfor %}

{% unless found_any %}
<p><em>No media found under <code>/assets/media/pictures/</code>. PDFs go in <code>/assets/media/pdfs/</code>. Add optional titles/links in <code>_data/media.yml</code>.</em></p>
{% endunless %}
