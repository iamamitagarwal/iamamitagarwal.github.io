---
layout: paper
title: "INCLUDE-2.0: Disentangling Knowledge Gaps in Multilingual LLM Evaluation"
authors: "Angelika Romanou, María Grandury, Clara Meister, Negar Foroutan, Jabez Magomere, Anna Sotnikova, Hitesh Laxmichand Patel, Akshay Kumar Dubey, Alfonso Amayuelas, Amit Agarwal, Arion Das, Carlos Arriaga, Cheng Yu, Dalia Ali, David Quispe-Castillo, Fenal Ashokbhai Ilasariya, Francisco-Javier Rodrigo-Ginés, Gonzalo Martínez, Gouthami Vadithya, Guido Ivetta, Javier Conde, Jorge Vallego, Juan J. Calderón G., Karan Gupta, Marcos J Gomez, Marvin M. Agüero-Torales, Mithil Bangera, Naira Paola Arnez Jordan, Oscar M. Cumbicus-Pineda, Priyaranjan Pattnayak, Reewos Erwin Talla Chumpitaz, Sahil Aggarwal, Sahil Raj, Shruti Jalan, Srikant Panda, Susana Zhou, Yeshil Bangera, Orestis Papakyriakopoulos, Scott A. Hale, Shamsuddeen Hassan Muhammad, Antoine Bosselut"
year: 2026
venue: "EMNLP 2026"
venue_token: emnlp
venue_url: "https://aclanthology.org/2026.emnlp-main.1344/"
tags: ["Multilingual", "Evaluation"]
keywords: ["Multilingual", "Evaluation", "LLM", "EMNLP"]
paper_url: "https://aclanthology.org/2026.emnlp-main.1344/"
pdf_url: "https://aclanthology.org/2026.emnlp-main.1344.pdf"
search: true
last_modified_at: 2026-11-11
---

**Abstract.** Current multilingual benchmarks cover often conflate language proficiency with the ability to answer questions grounded in specific regions and communities. We introduce INCLUDE-2.0, a large-scale benchmark for region-aware multilingual factual evaluation, which covers 91 languages from 86 countries (127 total language–country pairs), comprising over 220K curated samples drawn from native regional sources. Unlike existing benchmarks that often treat language as a proxy for region, INCLUDE-2.0 distinguishes between questions whose answers are independent of context, vary by country, concern widely documented facts about a place, or depend on knowledge primarily expressed through local linguistic and cultural sources. Each item is annotated with its regional knowledge type and domain, and paired with an English translation, enabling controlled analysis of the relationship between language proficiency and possession of regional knowledge. Evaluating frontier and open-weight models on INCLUDE-2.0, we find that aggregate measures of multilingual accuracy mask substantial performance differenes across regional knowledge types, languages, and regions, and that frontier models generally perform worse on locally embedded knowledge than other knowledge types. INCLUDE-2.0 is available at https://huggingface.co/datasets/epfl-nlp/include-2.0

**Source.** [ACL Anthology paper PDF](https://aclanthology.org/2026.emnlp-main.1344.pdf); [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

**Summary.** INCLUDE-2.0 evaluates factual knowledge across 91 languages and 86 countries using more than 220,000 examples. It separates language ability from several forms of regional knowledge and pairs questions with English translations. Results reveal weaknesses on locally grounded knowledge that aggregate multilingual scores can obscure.
