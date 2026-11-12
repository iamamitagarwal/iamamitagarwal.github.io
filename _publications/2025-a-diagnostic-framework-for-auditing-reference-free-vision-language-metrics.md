---
layout: paper
title: "A Diagnostic Framework for Auditing Reference-Free Vision-Language Metrics"
authors: "Angeline Charles, Srikant Panda, Amit Agarwal, Hitesh Laxmichand Patel, Priyaranjan Pattnayak, Bhargava Kumar, Tejaswini Kumar"
year: 2025
venue: AACL 2025
venue_token: aacl
venue_url: "https://aclanthology.org/2025.ijcnlp-long.142/"
tags:
  - Evaluation
  - Multimodal
keywords:
  - "Evaluation"
  - "Multimodal"
  - "Vision-Language"
  - "AACL"
  - "ACL"
paper_url: "https://aclanthology.org/2025.ijcnlp-long.142/"
pdf_url: "https://aclanthology.org/2025.ijcnlp-long.142.pdf"
search: true
last_modified_at: 2026-11-11
---

**Abstract.** Reference-free metrics such as CLIPScore and PAC-S are increasingly used in vision-language tasks due to their scalability and independence from human-written references. However, their reliability under linguistic, visual, and cultural variation remains underexplored. In this work, we present a systematic audit of CLIPScore and PAC-S using an eight-factor diagnostic framework applied to MS-COCO validation images. Our analysis reveals consistent failure modes across dimensions including object size, content category, syntax, named entities, spatial relations and cultural context. Both metrics penalize captions referencing African (−5.5%, −4.8%) and Arabian (−4.9%, −5.3%) cultures, favor large-object and animal-centric scenes (by 20-30%) and show limited sensitivity to spatial negation and word order. CLIPScore correlates more strongly with syntactic complexity, while PAC-S demonstrates greater robustness to verbosity and named–entity variation highlighting complementary strengths rather than superiority. These findings expose cultural and content bias, weak semantic robustness, and limited compositional understanding. We conclude with design recommendations to improve fairness, scale invariance, and semantic grounding in future reference-free evaluation metrics.

**Source.** [ACL Anthology proceedings PDF](https://aclanthology.org/2025.ijcnlp-long.142.pdf); [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

**Summary.** This paper introduces a diagnostic framework for auditing reference-free metrics used in vision-language evaluation. It focuses on understanding when these metrics are reliable and where they fail across different multimodal evaluation settings.
