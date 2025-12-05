---
layout: paper
title: "Who's Asking? Investigating Bias Through the Lens of Disability-Framed Queries in LLMs"
authors: 'Vishnu Hari, Kalpana Panda, Srikant Panda, Amit Agarwal, Hitesh Laxmichand Patel'
year: 2025
venue: IEEE
tags:
- Responsible-AI
- Evaluation
paper_url: https://openaccess.thecvf.com/content/ICCV2025W/CV4A11y/html/Hari_Whos_Asking_Investigating_Bias_Through_the_Lens_of_Disability-Framed_Queries_ICCVW_2025_paper.html
search: true
---

**Abstract.** Large Language Models (LLMs) routinely infer users' demographic traits from phrasing alone, which can result in biased responses, even when no explicit demographic information is provided. The role of disability cues in shaping these inferences remains largely uncharted. Thus, we present the first systematic audit of disability-conditioned demographic bias across eight state-of-the-art instruction-tuned LLMs ranging from 3B to 72B parameters. Using a balanced template corpus that pairs nine disability categories with six real-world business domains, we prompt each model to predict five demographic attributes - gender, socioeconomic status, education, cultural background, and locality - under both neutral and disability-aware conditions. Across a varied set of prompts, models deliver a definitive demographic guess in up to 97% of cases, exposing a strong tendency to make arbitrary inferences with no clear justification. Disability context heavily shifts predicted attribute distributions, and domain context can further amplify these deviations. We observe that larger models are simultaneously more sensitive to disability cues and more prone to biased reasoning, indicating that scale alone does not mitigate stereotype amplification. Our findings reveal persistent intersections between ableism and other demographic stereotypes, pinpointing critical blind spots in current alignment strategies. We release our evaluation framework and results to encourage disability-inclusive benchmarking and recommend integrating abstention calibration and counterfactual fine-tuning to curb unwarranted demographic inference. Code and data will be released on acceptance.
