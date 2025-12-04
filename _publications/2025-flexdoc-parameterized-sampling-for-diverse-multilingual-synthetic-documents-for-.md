---
layout: paper
title: "FlexDoc: Parameterized Sampling for Diverse Multilingual Synthetic Documents for Training Document Understanding Models"
authors: 'Karan Dua; Hitesh Laxmichand Patel; Puneet Mittal; Ranjeet Gupta; Amit Agarwal; Praneet Pabolu; Srikant Panda; Hansa Meghwani; Graham Horwood; Fahad Shah'
year: 2025
venue: EMNLP
tags:
- Document-AI
- Multilingual
- Legal
paper_url: https://aclanthology.org/2025.emnlp-industry.105/
search: true
---

**Abstract.** Developing document understanding models at enterprise scale requires large, diverse, and well-annotated datasets spanning a wide range of document types. However, collecting such data is prohibitively expensive due to privacy constraints, legal restrictions, and the sheer volume of manual annotation needed-costs that can scale into millions of dollars. We introduce FlexDoc, a scalable synthetic data generation framework that combines Stochastic Schemas and Parameterized Sampling to produce realistic, multilingual semi-structured documents with rich annotations. By probabilistically modeling layout patterns, visual structure, and content variability, FlexDoc enables the controlled generation of diverse document variants at scale. Experiments on Key Information Extraction (KIE) tasks demonstrate that FlexDoc-generated data improves the absolute F1 Score by up to 11% when used to augment real datasets, while reducing annotation effort by over 90% compared to traditional hard-template methods. The solution is in active deployment, where it has accelerated the development of enterprise-grade document understanding models while significantly reducing data acquisition and annotation costs.
