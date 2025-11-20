---
layout: paper
title: 'Tokenization matters: Improving zero-shot ner for indic languages'
authors: 'Pattnayak, Priyaranjan; Patel, Hitesh; **Agarwal, Amit**; '
year: 2025
venue: IEEE
tags:
- Multilingual
paper_url: https://ieeexplore.ieee.org/abstract/document/11103625
search: true
---

**Abstract.** Tokenization is a critical component of Natural Language Processing (NLP), especially for low-resource languages, where subword segmentation influences vocabulary structure and downstream task accuracy. Although Byte-Pair Encoding (BPE) is a standard tokenization method in multilingual language models, its suitability for Named Entity Recognition (NER) in low-resource Indic languages remains underexplored due to its limitations in handling morphological complexity. In this work, we systematically compare BPE, SentencePiece, and Character-Level tokenization strategies using IndicBERT for NER tasks in low-resource Indic languages like Assamese, Bengali, Marathi, and Odia, as well as extremely low-resource Indic languages like Santali, Manipuri, and Sindhi. We assess both intrinsic linguistic properties-tokenization efficiency, out-of-vocabulary (OOV) rates, and morphological preservation-as well as extrinsic downstream performance, including fine-tuning and zero-shot cross-lingual transfer. Our experiments show that SentencePiece is a consistently better performing approach than BPE for NER in low-resource Indic Languages, particularly in zero-shot cross-lingual settings, as it better preserves entity consistency. While BPE provides the most compact tokenization form, it is not capable of generalization because it misclassifies or even fails to recognize entity labels when tested on unseen languages. In contrast, SentencePiece constitutes a better linguistic structural preservation model, benefiting extremely low-resource and morpholically rich Indic languages, such as Santali and Manipuri, for superior entity recognition, as well as high generalization across scripts, such as Sindhi, written in Arabic. The results point to SentencePiece as the more effective tokenization strategy for NER within multilingual and low-resource Indic NLP applications.
