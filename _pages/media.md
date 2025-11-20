---
permalink: /media/
title: "Media"
layout: single
author_profile: true
classes: wide
---

<style>
/* Grid */
.media-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1rem}
@media(max-width:1200px){.media-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:720px){.media-grid{grid-template-columns:1fr}}

/* Card */
.media-card{position:relative;border:1px solid rgba(0,0,0,.08);border-radius:16px;overflow:hidden;background:#fff}
.media-thumb{display:block;aspect-ratio:16/9;object-fit:cover;width:100%;height:auto}
.media-meta{padding:.75rem 1rem .9rem}
.media-title{margin:0 0 .5rem;font-weight:800;font-size:1rem}
.media-actions{display:flex;gap:.5rem;flex-wrap:wrap}

/* Pills */
.pill{display:inline-flex;align-items:center;gap:.35rem;padding:.32rem .7rem;border-radius:999px;
      border:1px solid var(--brand-accent,#0ea5e9);text-decoration:none;font-weight:700;font-size:.85rem}
.pill:hover{background:var(--brand-accent,#0ea5e9);color:#fff}
.pill--pdf{border-color:#ef4444}.pill--pdf:hover{background:#ef4444;color:#fff}
.pill--site{border-color:#0ea5e9}
html.theme-dark .media-card{background:#0b1220;border-color:#1f2937}

/* Lightbox */
.lb{position:fixed;inset:0;background:rgba(0,0,0,.85);display:none;align-items:center;justify-content:center;z-index:9998}
.lb.open{display:flex}
.lb-inner{position:relative;max-width:92vw;max-height:88vh}
.lb-img{max-width:92vw;max-height:88vh;display:block;object-fit:contain;border-radius:12px}
.lb-nav{position:absolute;top:50%;left:0;right:0;display:flex;justify-content:space-between;transform:translateY(-50%)}
.lb-btn{background:rgba(0,0,0,.45);color:#fff;border:0;border-radius:999px;padding:.5rem .75rem;cursor:pointer}
.lb-close{position:absolute;top:-44px;right:-4px;background:rgba(0,0,0,.55);color:#fff;border:0;border-radius:999px;
         padding:.45rem .7rem;cursor:pointer}
.lb-caption{color:#e5e7eb;margin-top:.6rem;text-align:center;font-size:.95rem}
</style>

{% comment %}
Collect static files from the two folders.
This requires *no plugins* and works on GitHub Pages.
{% endcomment %}
{% assign all_imgs = site.static_files | where_exp:'f','f.path contains "/assets/media/pictures/"' | sort: 'name' %}
{% assign all_pdfs = site.static_files | where_exp:'f','f.path contains "/assets/media/pdfs/" and f.extname == ".pdf"' %}

<div class="media-grid">
{% for img in all_imgs %}
  {% assign base = img.name | replace: img.extname, '' %}
  {% assign pdf  = all_pdfs | where_exp:'p','p.name contains base' | first %}
  {% assign meta = site.data.media[base] %}
  {% assign pretty = meta.title | default: base | replace: '-', ' ' | replace: '_', ' ' %}
  {% assign site_link = meta.site | default: '#' %}

  <article class="media-card" data-index="{{ forloop.index0 }}">
    <a href="#" class="lb-open" data-index="{{ forloop.index0 }}">
      <img class="media-thumb" src="{{ img.path | relative_url }}" alt="{{ pretty | escape }}">
    </a>
    <div class="media-meta">
      <h3 class="media-title">{{ pretty }}</h3>
      <div class="media-actions">
        {% if pdf %}
          <a class="pill pill--pdf" href="{{ pdf.path | relative_url }}" target="_blank" rel="noopener">PDF</a>
        {% endif %}
        <a class="pill pill--site" href="{{ site_link }}" target="_blank" rel="noopener">Story</a>
      </div>
    </div>
  </article>
{% endfor %}
</div>

<!-- Lightbox / Carousel -->
<div class="lb" id="lb">
  <div class="lb-inner">
    <button class="lb-close" aria-label="Close">&times;</button>
    <img class="lb-img" id="lbImg" src="" alt="">
    <div class="lb-nav">
      <button class="lb-btn" id="lbPrev" aria-label="Previous">&#9664;</button>
      <button class="lb-btn" id="lbNext" aria-label="Next">&#9654;</button>
    </div>
    <div class="lb-caption" id="lbCap"></div>
  </div>
</div>

<script>
(function(){
  const cards = Array.from(document.querySelectorAll('.media-card'));
  const lb    = document.getElementById('lb');
  const lbImg = document.getElementById('lbImg');
  const lbCap = document.getElementById('lbCap');
  const prev  = document.getElementById('lbPrev');
  const next  = document.getElementById('lbNext');
  const close = document.querySelector('.lb-close');

  const images = cards.map(c => c.querySelector('.media-thumb').src);
  const captions = cards.map(c => c.querySelector('.media-title').textContent.trim());
  let i = 0;

  function show(k){
    i = (k + images.length) % images.length;
    lbImg.src = images[i];
    lbCap.textContent = captions[i];
  }

  document.addEventListener('click', (e)=>{
    const a = e.target.closest('.lb-open');
    if(a){
      e.preventDefault();
      const idx = +a.dataset.index || 0;
      show(idx);
      lb.classList.add('open');
    }
  });

  prev.addEventListener('click', ()=> show(i-1));
  next.addEventListener('click', ()=> show(i+1));
  close.addEventListener('click', ()=> lb.classList.remove('open'));
  lb.addEventListener('click', (e)=>{ if(e.target === lb) lb.classList.remove('open'); });
  document.addEventListener('keydown', (e)=>{
    if(!lb.classList.contains('open')) return;
    if(e.key === 'Escape') lb.classList.remove('open');
    if(e.key === 'ArrowLeft') show(i-1);
    if(e.key === 'ArrowRight') show(i+1);
  });
})();
</script>
