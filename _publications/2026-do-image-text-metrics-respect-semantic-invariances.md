---
layout: paper
title: "Do Image-Text Metrics Respect Semantic Invariances?"
authors: "Amit Agarwal, Hitesh Laxmichand Patel, Meizhu Liu, Jyotika Singh, Karan Dua, Hansa Meghwani, Matthew Rowe, Michael Avendi, Yassi Abbasi, Tao Sheng, Sujith Ravi, Dan Roth"
year: 2026
priority: 1
venue: ACL Findings 2026
venue_token: acl
venue_url: "https://aclanthology.org/2026.findings-acl.1948/"
tags:
  - Multimodal
  - Evaluation
  - Responsible-AI
keywords:
  - "Multimodal"
  - "Evaluation"
  - "Image-Text Metrics"
  - "Semantic Invariance"
  - "ACL Findings"
  - "ACL 2026"
paper_url: "https://aclanthology.org/2026.findings-acl.1948/"
arxiv_id: "2605.24702"
pdf_url: "https://aclanthology.org/2026.findings-acl.1948.pdf"
search: true
last_modified_at: 2026-11-11
---

**Abstract.** Reference-free image-to-text evaluators are now standard for scoring image-caption
alignment, yet it is unclear whether they respect semantic invariances. We present an invariance
probe on five popular evaluators (CLIPScore, PAC-S, UMIC, FLEUR, and a deterministic LLM judge)
under semantics-preserving perturbations along three axes- spatial (flips, context-preserving
repositioning, light rotations), object (scale, category), and socio-linguistic framing
(cultural/economic adjectives with neutral and length-matched controls). Across curated slices of
three detection datasets and three caption evaluation suites, we find consistent non-semantic
sensitivities, where benign spatial edits and simple phrasing changes shift scores by ≈6-9% on
average, and for systems separated by just 0.7%, these shifts can cause ranking flips in upto ∼37%
of cases, particularly under spatial changes. A small human study also supports this finding and
confirms that annotators generally judge perturbed pairs as equally correct, so these shifts reflect
metric behavior rather than semantic change. We further propose invariance-calibrated scoring, a
post-hoc adjustment that roughly halves median absolute sensitivity while retaining correlation with
learned caption evaluators.

**Source.** [“Do Image–Text Metrics Respect Semantic Invariances?,” ACL Anthology PDF](https://aclanthology.org/2026.findings-acl.1948.pdf); [CC BY 4.0 license](https://creativecommons.org/licenses/by/4.0/).

**Summary.** This paper studies whether reference-free image-to-text evaluators respect
meaning-preserving changes in images and captions. It probes popular caption-alignment metrics
across spatial, object-level, and socio-linguistic perturbations, showing that non-semantic changes
can shift scores and alter system rankings. The work also proposes invariance-calibrated scoring to
reduce these sensitivities while preserving alignment with learned caption evaluators.
