---
layout: paper
title: "Learning from Unknown for Open-Set Test-Time Adaptation"
authors: "Taki Hasan Rafi, Amit Agarwal, Hitesh Laxmichand Patel, Dong-Kyu Chae"
year: 2026
venue: WACV 2026
venue_url: "https://openaccess.thecvf.com/content/WACV2026/html/Rafi_Learning_from_Unknown_for_Open-Set_Test-Time_Adaptation_WACV_2026_paper.html"
tags: ["Multimodal"]
keywords:
  - "Multimodal"
  - "WACV"
paper_url: "https://openaccess.thecvf.com/content/WACV2026/html/Rafi_Learning_from_Unknown_for_Open-Set_Test-Time_Adaptation_WACV_2026_paper.html"
pdf_url: "https://openaccess.thecvf.com/content/WACV2026/papers/Rafi_Learning_from_Unknown_for_Open-Set_Test-Time_Adaptation_WACV_2026_paper.pdf"
search: true
last_modified_at: 2026-11-11
---

**Abstract.** Deep learning models often struggle to maintain performance when the training and testing data come from different distributions. Test-time adaptation (TTA) addresses this by adapting a pre-trained model to an unlabeled target domain under distribution shifts. A more challenging setting is open-set TTA (OSTTA), where the target domain may contain unknown samples outside the source classes. Existing OSTTA methods primarily detect and discard such unknowns, relying only on known samples for adaptation. In this work, we argue that unknown samples can also provide valuable cues for improving adaptation. We propose LU-OSTTA (learning from unknown for OSTTA), a simple yet effective framework that leverages both in-distribution and semantically useful out-of-distribution samples. Our approach introduces: (i) a class-conditioned dynamic energy threshold to separate OOD samples more reliably, (ii) an optimal transport-based pseudo-label refinement to mitigate noise under distribution shifts, and (iii) an adaptive prototype weighting strategy that emphasizes semantically aligned target samples while down-weighting harmful ones. Experimental results demonstrate that our LU-OSTTA consistently outperforms state-of-the-art TTA and OSTTA methods, highlighting the benefits of utilizing rather than discarding unknown samples. Our code is available at: https://github.com/takihasan/LU-OSTTA.

Source: [CVF Open Access publication page](https://openaccess.thecvf.com/content/WACV2026/html/Rafi_Learning_from_Unknown_for_Open-Set_Test-Time_Adaptation_WACV_2026_paper.html).
