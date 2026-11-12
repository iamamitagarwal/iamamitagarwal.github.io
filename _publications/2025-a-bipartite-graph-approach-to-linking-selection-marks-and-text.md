---
layout: paper
title: "A Bipartite Graph Approach to Linking Selection Marks and Text"
authors: "Amit Agarwal, Srikant Panda, Kulbhushan Pachauri"
year: 2025
venue: ICDMAI 2025
venue_token: icdmai
venue_url: "https://link.springer.com/chapter/10.1007/978-981-96-5860-2_1"
tags:
  - Document AI
keywords:
  - "Document AI"
  - "Optical Character Recognition"
  - "Optical Mark Recognition"
  - "Graph Matching"
  - "ICDMAI"
paper_url: "https://link.springer.com/chapter/10.1007/978-981-96-5860-2_1"
search: true
last_modified_at: 2026-11-11
---

**Abstract.** In a document, Different Graphical elements can be recognized by technologies like Optical Character Recognition (OCR) and Optical Mark Recognition (OMR). While OCR is meant to detect and identify text regions, OMR is mainly used to detect and identify selection markings like ticks, bubbles, or checkmarks. Though OCR and OMR technologies have advanced significantly in recent years, further research is required to determine how selection marks relate to text in order to improve OCR’s capabilities. In this study, we present a novel method to associate the relevant text detected by OCR with the selection marks identified by OMR. To identify text components and selection marks from a document image, we employ an OCR pipeline (OCR with OMR capability). Next, using the structure of the graph network as a guide, we construct the selection mark to text association as an optimization problem and use bipartite network algorithms to match the selection marks with their associated text. Our proposed method correctly connects selection marks with their corresponding text in a variety of document types across different domains, according to experimental results. Our analysis of ten different document types from various industry domains yielded an average F1-score of 95.95%. Our suggested method can be combined with any OCR pipeline to improve its performance without adding to its complexity. This could lead to a rise in office automation and Robotic Process Automation (RPA) for tasks involving document processing.

**Source.** [Springer chapter record](https://link.springer.com/chapter/10.1007/978-981-96-5860-2_1).

**Summary.** The paper formulates the association of document selection marks with their text labels as a bipartite graph matching problem. It combines OCR and mark recognition with an optimization step to connect detected marks to the relevant text. Evaluation across ten document categories reports a mean F1 score of 95.95%, supporting integration into document-processing pipelines.

**Publication note.** Presented in the ICDMAI 2025 proceedings, pages 1–12. Springer lists the first online publication as November 23, 2025, and the formal book citation year as 2026 (Lecture Notes in Networks and Systems, volume 1369). This listing uses the conference and first-online year.
