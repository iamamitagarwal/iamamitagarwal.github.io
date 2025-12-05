---
layout: paper
title: "Hard Negative Mining for Domain-Specific Retrieval in Enterprise Systems"
authors: 'Hansa Meghwani, Amit Agarwal, Priyaranjan Pattnayak, Hitesh Laxmichand Patel, Srikant Panda'
year: 2025
venue: ACL
tags:
- Document-AI
- Eval
- Retrieval
paper_url: https://aclanthology.org/2025.acl-industry.72/
search: true
---

**Abstract.** Enterprise search systems often struggle to retrieve accurate, domain-specific information due to semantic mismatches and overlapping terminologies. These issues can degrade the performance of downstream applications such as knowledge management, customer support, and retrieval-augmented generation agents. To address this challenge, we propose a scalable hard-negative mining framework tailored specifically for domain-specific enterprise data. Our approach dynamically selects semantically challenging but contextually irrelevant documents to enhance deployed re-ranking models. Our method integrates diverse embedding models, performs dimensionality reduction, and uniquely selects hard negatives, ensuring computational efficiency and semantic precision. Evaluation on our proprietary enterprise corpus (cloud services domain) demonstrates substantial improvements of 15\% in MRR@3 and 19\% in MRR@10 compared to state-of-the-art baselines and other negative sampling techniques. Further validation on public domain-specific datasets (FiQA, Climate Fever, TechQA) confirms our method's generalizability and readiness for real-world applications.
