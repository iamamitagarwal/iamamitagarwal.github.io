---
permalink: /publications/
title: "Publications"
layout: single
author_profile: true
classes: wide
search: true
description: "Research publications across evaluation, retrieval, multimodal, multilingual, and document AI."
tags: ["Publications", "Research", "AI", "Alignment", "Reasoning", "Multilingual", "Multimodal", "RAG", "Retrieval", "Evaluation", "Document AI"]
keywords: ["Publications", "Papers", "Alignment", "Reasoning", "Multilingual", "Multimodal", "RAG", "Retrieval", "Evaluation", "Document AI", "LLM", "NLP", "Agentic AI", "AI safety", "CVPR", "ICLR", "ACL", "EMNLP", "WACV", "CIKM", "DASFAA"]
---

<p class="page-intro">Research across agents, multimodal models, retrieval, and evaluation. Browse by year, topic, or title, or visit the <a href="{{ '/research-topics/' | relative_url }}">research topics hub</a>.</p>

{% assign publications = site.publications | sort: "year" | reverse %}
{% assign publication_years = "" | split: "" %}
{% assign publication_topics = "" | split: "" %}

{% for publication in publications %}
  {% unless publication_years contains publication.year %}
    {% assign publication_years = publication_years | push: publication.year %}
  {% endunless %}

  {% capture joined_tags %}{{ publication.tags | join: '|' }}{% endcapture %}
  {% assign tag_source = joined_tags | strip %}
  {% if tag_source == "" %}
    {% assign tag_source = publication.tags | default: "" %}
  {% endif %}
  {% assign tag_values = tag_source | replace: ',', '|' | split: '|' %}
  {% for tag in tag_values %}
    {% assign clean_tag = tag | strip %}
    {% assign tag_key = clean_tag | downcase %}
    {% case tag_key %}
      {% when 'document-ai' %}{% assign clean_tag = 'Document AI' %}
      {% when 'information-retrieval' %}{% assign clean_tag = 'Retrieval' %}
      {% when 'responsible-ai' %}{% assign clean_tag = 'Responsible AI & Safety' %}
      {% when 'responsibleai' %}{% assign clean_tag = 'Responsible AI & Safety' %}
      {% when 'responsible ai' %}{% assign clean_tag = 'Responsible AI & Safety' %}
      {% when 'safety' %}{% assign clean_tag = 'Responsible AI & Safety' %}
    {% endcase %}
    {% if clean_tag != "" %}
      {% unless publication_topics contains clean_tag %}
        {% assign publication_topics = publication_topics | push: clean_tag %}
      {% endunless %}
    {% endif %}
  {% endfor %}
{% endfor %}
{% assign publication_years = publication_years | sort | reverse %}
{% assign publication_topics = publication_topics | sort %}

<form class="filter-bar" id="publication-filters" role="search" hidden>
  <label for="publication-search">
    Search papers
    <input class="filter-input" id="publication-search" name="q" type="search" autocomplete="off">
  </label>
  <label for="publication-year">
    Year
    <select class="filter-input" id="publication-year" name="year">
      <option value="">All years</option>
      {% for year in publication_years %}
        <option value="{{ year | escape }}">{{ year }}</option>
      {% endfor %}
    </select>
  </label>
  <label for="publication-topic">
    Topic
    <select class="filter-input" id="publication-topic" name="topic">
      <option value="">All topics</option>
      {% for topic in publication_topics %}
        <option value="{{ topic | downcase | replace: ' ', '-' | escape }}">{{ topic | escape }}</option>
      {% endfor %}
    </select>
  </label>
  <button class="filter-button" id="clear-publication-filters" type="button">Clear filters</button>
  <p class="filter-status" id="publication-filter-status" aria-live="polite"></p>
</form>

<noscript><p class="filter-note">Filtering is optional; the complete archive is listed below.</p></noscript>

<div class="publication-archive">
  {% for year in publication_years %}
    {% assign year_publications = publications | where: "year", year %}
    {% assign priority_publications = "" | split: "" %}
    {% assign other_publications = "" | split: "" %}

    {% for publication in year_publications %}
      {% if publication.priority != nil %}
        {% assign priority_publications = priority_publications | push: publication %}
      {% else %}
        {% assign other_publications = other_publications | push: publication %}
      {% endif %}
    {% endfor %}
    {% assign priority_publications = priority_publications | sort: "priority" %}
    {% assign ordered_publications = priority_publications | concat: other_publications %}

    <section class="publication-year" data-year="{{ year | escape }}">
      <h2 class="meta">{{ year }}</h2>
      <ul class="paper-list">
        {% for publication in ordered_publications %}
          {% assign joined_tags = "" %}
          {% capture joined_tags %}{{ publication.tags | join: '|' }}{% endcapture %}
          {% assign tag_source = joined_tags | strip %}
          {% if tag_source == "" %}
            {% assign tag_source = publication.tags | default: "" %}
          {% endif %}
          {% assign tag_values = tag_source | replace: ',', '|' | split: '|' %}
          {% assign paper_topics = "" | split: "" %}
          {% for tag in tag_values %}
            {% assign clean_tag = tag | strip %}
            {% assign tag_key = clean_tag | downcase %}
            {% case tag_key %}
              {% when 'document-ai' %}{% assign clean_tag = 'Document AI' %}
              {% when 'information-retrieval' %}{% assign clean_tag = 'Retrieval' %}
              {% when 'responsible-ai' %}{% assign clean_tag = 'Responsible AI & Safety' %}
              {% when 'responsibleai' %}{% assign clean_tag = 'Responsible AI & Safety' %}
              {% when 'responsible ai' %}{% assign clean_tag = 'Responsible AI & Safety' %}
              {% when 'safety' %}{% assign clean_tag = 'Responsible AI & Safety' %}
            {% endcase %}
            {% if clean_tag != "" %}
              {% unless paper_topics contains clean_tag %}
                {% assign paper_topics = paper_topics | push: clean_tag %}
              {% endunless %}
            {% endif %}
          {% endfor %}

          {% assign research_context = site.data.paper_context[publication.slug] %}
          {% capture search_text %}{{ publication.title }} {{ publication.authors }} {{ publication.venue }} {{ publication.description }} {{ publication.abstract }} {{ publication.content | markdownify | strip_html }} {{ publication.tags | join: ' ' }} {{ publication.keywords | join: ' ' }} {{ research_context.summary }} {{ research_context.terms | join: ' ' }} {% for topic in paper_topics %}{{ topic }} {% endfor %}{% endcapture %}
          <li class="paper-entry" data-year="{{ publication.year | escape }}" data-topics="{{ paper_topics | jsonify | escape }}" data-search="{{ search_text | strip_html | replace: '&lt;', '<' | replace: '&gt;', '>' | strip_newlines | escape }}">
            {% if publication.recognition %}
              <p class="recognition recognition--{{ publication.recognition_type | default: 'highlight' | slugify }}">{{ publication.recognition | escape }}</p>
            {% endif %}
            <h3><a class="paper-title" href="{{ publication.url | relative_url }}">{{ publication.title | escape }}</a></h3>

            {% assign full_authors = publication.authors | default: "" %}
            {% assign author_list = full_authors | split: "," %}
            {% assign author_count = author_list | size %}
            {% assign authors_display = full_authors %}
            {% if author_count > 12 %}
              {% assign lead_authors = author_list | slice: 0, 3 %}
              {% capture authors_display %}{% for author in lead_authors %}{% unless forloop.first %}, {% endunless %}{{ author | strip }}{% endfor %}{% endcapture %}
              {% assign authors_display = authors_display | strip %}
              {% assign author_preview_has_amit = false %}
              {% assign amit_author = "" %}
              {% for author in author_list %}
                {% assign author_name = author | strip %}
                {% assign author_key = author_name | downcase %}
                {% if author_key == "amit agarwal" %}
                  {% assign amit_author = author_name %}
                  {% if forloop.index0 < 3 %}
                    {% assign author_preview_has_amit = true %}
                  {% endif %}
                {% endif %}
              {% endfor %}
              {% if amit_author != "" and author_preview_has_amit == false %}
                {% assign authors_display = authors_display | append: ", … " | append: amit_author %}
              {% endif %}
              {% assign authors_display = authors_display | append: ", et al." %}
            {% endif %}
            <p class="paper-authors" title="{{ full_authors | escape }}">{% include publication_authors.html authors=authors_display %}</p>
            {% if author_count > 12 %}
            <details class="full-author-list">
              <summary>All {{ author_count }} authors</summary>
              <p class="paper-authors">{% include publication_authors.html authors=full_authors %}</p>
            </details>
            {% endif %}

            {% assign venue_text = publication.venue | default: "" %}
            <p class="meta">
              {% if publication.venue %}
                {% if publication.venue_url %}
                  <a href="{{ publication.venue_url | escape }}" target="_blank" rel="noopener noreferrer">{{ publication.venue | escape }}</a>
                {% else %}
                  {{ publication.venue | escape }}
                {% endif %}
              {% endif %}
              {% assign venue_year = publication.year | append: "" %}
              {% if publication.year %}
                {% unless venue_text contains venue_year %}<span>{{ publication.year }}</span>{% endunless %}
              {% endif %}
              {% if publication.status %}<span>{{ publication.status | escape }}</span>{% endif %}
            </p>

            {% if paper_topics.size > 0 %}
              <p class="paper-topics"><span class="meta">Topics:</span>
                {% for topic in paper_topics %}
                  {% unless forloop.first %}<span aria-hidden="true"> · </span>{% endunless %}{{ topic | escape }}
                {% endfor %}
              </p>
            {% endif %}

            {% assign paper_href = publication.paper_url | default: "" %}
            {% assign doi_value = publication.doi | default: publication.DOI | default: "" %}
            {% assign arxiv_href = "" %}
            {% if publication.arxiv_id %}
              {% assign arxiv_href = "https://arxiv.org/abs/" | append: publication.arxiv_id %}
            {% endif %}
            {% if paper_href == "" and doi_value != "" %}
              {% assign paper_href = "https://doi.org/" | append: doi_value %}
            {% endif %}
            {% if paper_href == "" and arxiv_href != "" %}
              {% assign paper_href = arxiv_href %}
            {% endif %}
            {% assign paper_label = "Paper" %}
            {% if paper_href contains "arxiv.org/" %}{% assign paper_label = "arXiv" %}{% endif %}
            {% assign pdf_href = publication.pdf_url | default: publication.pdf | default: "" %}
            {% if pdf_href contains "arxiv.org/" and paper_label != "arXiv" %}
              {% assign pdf_href = "" %}
            {% endif %}
            {% assign code_href = publication.code_url | default: "" %}
            {% assign dataset_href = publication.dataset_url | default: publication.data_url | default: "" %}
            {% assign source_urls = "" | split: "" %}

            <nav class="paper-actions" aria-label="Publication resources">
              {% if paper_href != "" %}
                {% assign paper_action_label = paper_label %}
                {% if pdf_href != "" and paper_href == pdf_href %}
                  {% assign paper_action_label = paper_label | append: " + PDF" %}
                {% endif %}
                <a href="{{ paper_href | escape }}" target="_blank" rel="noopener noreferrer">{{ paper_action_label }}</a>
                {% assign source_urls = source_urls | push: paper_href %}
              {% endif %}
              {% if pdf_href != "" %}
                {% unless source_urls contains pdf_href %}
                  <a href="{{ pdf_href | escape }}" target="_blank" rel="noopener noreferrer">PDF</a>
                  {% assign source_urls = source_urls | push: pdf_href %}
                {% endunless %}
              {% endif %}
              {% if code_href != "" %}
                {% unless source_urls contains code_href %}
                  <a href="{{ code_href | escape }}" target="_blank" rel="noopener noreferrer">Code</a>
                  {% assign source_urls = source_urls | push: code_href %}
                {% endunless %}
              {% endif %}
              {% if dataset_href != "" %}
                {% unless source_urls contains dataset_href %}
                  <a href="{{ dataset_href | escape }}" target="_blank" rel="noopener noreferrer">Dataset</a>
                {% endunless %}
              {% endif %}
            </nav>
          </li>
        {% endfor %}
      </ul>
    </section>
  {% endfor %}
</div>

<script>
  (function () {
    var form = document.getElementById("publication-filters");
    var searchInput = document.getElementById("publication-search");
    var yearSelect = document.getElementById("publication-year");
    var topicSelect = document.getElementById("publication-topic");
    var clearButton = document.getElementById("clear-publication-filters");
    var status = document.getElementById("publication-filter-status");
    var entries = Array.prototype.slice.call(document.querySelectorAll(".paper-entry"));
    var yearSections = Array.prototype.slice.call(document.querySelectorAll(".publication-year"));

    if (!form || !searchInput || !yearSelect || !topicSelect || !clearButton || entries.length === 0) {
      return;
    }

    function applyFilters() {
      var query = searchInput.value.trim().toLowerCase();
      var selectedYear = yearSelect.value;
      var selectedTopic = topicSelect.value;
      var visibleCount = 0;

      entries.forEach(function (entry) {
        var searchText = (entry.getAttribute("data-search") || "").toLowerCase();
        var topics = JSON.parse(entry.getAttribute("data-topics") || "[]");
        var matchesQuery = query === "" || searchText.indexOf(query) !== -1;
        var matchesYear = selectedYear === "" || entry.getAttribute("data-year") === selectedYear;
        var matchesTopic = selectedTopic === "" || topics.some(function (topic) {
          return topic.toLowerCase().replace(/ /g, "-") === selectedTopic;
        });
        var visible = matchesQuery && matchesYear && matchesTopic;

        entry.hidden = !visible;
        if (visible) {
          visibleCount += 1;
        }
      });

      yearSections.forEach(function (section) {
        section.hidden = section.querySelector(".paper-entry:not([hidden])") === null;
      });

      status.textContent = visibleCount + " of " + entries.length + " papers shown.";
    }

    form.hidden = false;
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      applyFilters();
    });
    searchInput.addEventListener("input", applyFilters);
    yearSelect.addEventListener("change", applyFilters);
    topicSelect.addEventListener("change", applyFilters);
    clearButton.addEventListener("click", function () {
      searchInput.value = "";
      yearSelect.value = "";
      topicSelect.value = "";
      applyFilters();
      searchInput.focus();
    });
    applyFilters();
  })();
</script>

<script type="application/ld+json">
{"@context":"https://schema.org","@type":"ItemList","name":"Research publications by Amit Agarwal","itemListElement":[
{% for paper in publications %}
{"@type":"ListItem","position":{{ forloop.index }},"name":{{ paper.title | jsonify }},"url":{{ paper.url | absolute_url | jsonify }}}{% unless forloop.last %},{% endunless %}
{% endfor %}]}
</script>
