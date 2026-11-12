---
layout: paper
title: "From Portraits to Pathology: Probing Diagnostic Overreach in Vision-Language Models"
authors: "Karan Dua, Amit Agarwal, Hitesh Laxmichand Patel, Hansa Meghwani, Jyotika Singh, Ranjeet Gupta, Graham Horwood, Tao Sheng, Avi Sil, Sujith Ravi, Dan Roth"
year: 2026
venue: arXiv
venue_token: arxiv
tags:
  - Multimodal
  - Evaluation
  - Safety
keywords:
  - "Multimodal"
  - "Evaluation"
  - "Safety"
  - "Abstention"
  - "PARITY"
paper_url: "https://arxiv.org/abs/2609.05540"
arxiv_id: "2609.05540"
pdf_url: "https://arxiv.org/pdf/2609.05540"
search: true
last_modified_at: 2026-11-11
---

**Abstract.** Many medical conditions require clinical assessment of symptoms, history, and functioning rather than judgments from appearance. We study whether vision–language models (VLMs) abstain from facial attribution of autism spectrum disorder (ASD), attention-deficit/hyperactivity disorder (ADHD), major depressive disorder (MDD), and generalized anxiety disorder (GAD). To support this study, we construct PARITY (Paired Assessment with Reused Identity), a demographically balanced dataset for testing whether changing facial expressions alters diagnostic judgments, while holding identity and other visual factors as constant as possible. Our comprehensive evaluation of 27 open- and closed-weight models reveals inconsistent abstention across expressions, conditions, and task formats. Models turn facial expressions into unsupported medical judgments: this behavior is widespread among open-weight VLMs and extends to safety-trained frontier models that abstain on individual portraits yet make diagnostic judgments when comparing portraits of the same identity. Safeguard checks reveal further gaps: clinical instructions do not consistently prevent these judgments, and a guardrail model rarely flags paired requests as unsafe. Semantic analysis further shows that most baseline open-model refusals fail to explain both the insufficiency of facial evidence and the need for clinical assessment. Unsupported judgments and seemingly authoritative explanations can cause distress, reinforce stigma, and offer false reassurance, underscoring the need for stronger safety measures in model training and deployment.

**Source.** [arXiv v2 paper PDF](https://arxiv.org/pdf/2609.05540v2); [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

**Summary.** This study examines whether vision–language models decline unsupported diagnostic judgments from facial photographs. The PARITY dataset varies expressions while controlling identity, enabling evaluation across 27 models and four clinical conditions. The authors report inconsistent abstention, including models that refuse individual portraits but make judgments when comparing images. Prompted clinical guidance and guardrail checks do not reliably prevent these failures.

**Version note.** The [first version](https://arxiv.org/abs/2609.05540v1), submitted September 2, 2026, was titled “Knowing When Not to Answer: Abstention and Refusal Reasoning in Vision--Language Models.” The current title and summary follow the October 12, 2026 revision. Both titles refer to the same arXiv record.
