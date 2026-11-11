---
permalink: /community/
title: "Community"
layout: single
classes: wide
description: "Workshop organizing, talks, and research community activity from Amit Agarwal."
tags: ["Community", "Workshops", "Talks", "AI Research"]
keywords: ["Amit Agarwal", "Community", "Workshop Organizer", "AI Talks", "Research Service"]
---

<p class="lead">Research community work includes workshop organizing, invited talks, and panel participation.</p>

<section aria-labelledby="workshops-heading">
  <div class="section-head">
    <h2 id="workshops-heading">Workshop organizing</h2>
    <a class="text-link" href="{{ '/workshops/' | relative_url }}">All workshops</a>
  </div>
  <ol class="archive-list">
    {% for workshop in site.data.workshops %}
    {% assign organizer_url = workshop.organizers_url | default: "" %}
    <li class="archive-entry">
      <article>
        <h3><a href="{{ workshop.local_url | relative_url }}">{{ workshop.title | escape }}</a></h3>
        <p class="meta">{{ workshop.role }} · {{ workshop.venue }} · {{ workshop.year }}</p>
        <div class="link-row">
          <a class="text-link" href="{{ workshop.local_url | relative_url }}">Overview</a>
          {% if organizer_url != "" %}
          <a class="text-link" href="{{ organizer_url }}" target="_blank" rel="noopener">Official organizer listing</a>
          {% endif %}
        </div>
      </article>
    </li>
    {% endfor %}
  </ol>
</section>

<section aria-labelledby="talks-heading">
  <div class="section-head">
    <h2 id="talks-heading">Talks and panels</h2>
    <a class="text-link" href="{{ '/talks/' | relative_url }}">Talk and event records</a>
  </div>
  <p>Browse invited-talk, panel, and workshop records with available event images, PDFs, and related papers.</p>
</section>
