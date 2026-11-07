---
permalink: /workshops/
title: "Workshop Organizing"
seo_title: "Amit Agarwal — Workshop Organizing"
layout: single
author_profile: true
classes: wide
description: "Amit Agarwal's workshop organizing across vision-language AI, structured-data LLMs, and document intelligence at CVPR, ACL, and EMNLP 2026."
tags: ["Workshops", "Organizing", "Amit Agarwal", "AI Research"]
keywords: ["Amit Agarwal", "Workshop Organizer", "GRAIL-V", "SURGeLLM", "DocInsights", "CVPR 2026", "ACL 2026", "EMNLP 2026"]
---

I serve as a lead organizer for GRAIL-V at CVPR, SURGeLLM at ACL, and DocInsights at EMNLP. These workshops connect my research interests in grounded agents, structured-data reasoning, and document intelligence with the broader research community.

{% for workshop in site.data.workshops %}
## [{{ workshop.title }}]({{ workshop.local_url | relative_url }})

{{ workshop.venue }} · {{ workshop.year }} · {{ workshop.role }}

[Official organizer listing]({{ workshop.organizers_url }}) · [Local overview]({{ workshop.local_url | relative_url }})

{% endfor %}

See also my [research stories](/projects/) and [publications](/publications/).
