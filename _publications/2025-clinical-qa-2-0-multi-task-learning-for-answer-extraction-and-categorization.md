---
layout: paper
title: "Clinical QA 2.0: Multi-Task Learning for Answer Extraction and Categorization"
authors: 'Priyaranjan Pattnayak, Hitesh Laxmichand Patel, Amit Agarwal, Bhargava Kumar, Srikant Panda, Tejaswini Kumar'
year: 2025
venue: arXiv
tags:
- Health
- Retrieval
paper_url: https://arxiv.org/abs/2502.13108
search: true
---

**Abstract.** Clinical Question Answering (CQA) plays a crucial role in medical decision-making, enabling physicians to extract relevant information from Electronic Medical Records (EMRs). While transformer-based models such as BERT, BioBERT, and ClinicalBERT have demonstrated state-of-the-art performance in CQA, existing models lack the ability to categorize extracted answers, which is critical for structured retrieval, content filtering, and medical decision support. To address this limitation, we introduce a Multi-Task Learning (MTL) framework that jointly trains CQA models for both answer extraction and medical categorization. In addition to predicting answer spans, our model classifies responses into five standardized medical categories: Diagnosis, Medication, Symptoms, Procedure, and Lab Reports. This categorization enables more structured and interpretable outputs, making clinical QA models more useful in real-world healthcare settings. We evaluate our approach on emrQA, a large-scale dataset for medical question answering. Results show that MTL improves F1-score by 2.2% compared to standard fine-tuning, while achieving 90.7% accuracy in answer categorization. These findings suggest that MTL not only enhances CQA performance but also introduces an effective mechanism for categorization and structured medical information retrieval.
