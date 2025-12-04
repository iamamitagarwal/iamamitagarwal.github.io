---
layout: paper
title: "Evaluate Generalisation & Robustness of Visual Features from Images to Video"
authors: 'Amit Agarwal'
year: 2021
venue: nan
tags:
- Retrieval
paper_url: https://www.researchgate.net/profile/Amit-Agarwal-62/publication/363539287_Evaluate_Generalisation_Robustness_of_Visual_Features_from_Images_to_Video/links/6321e7f8071ea12e3632736c/Evaluate-Generalisation-Robustness-of-Visual-Features-from-Images-to-Video.pdf
search: true
---

**Abstract.** Unlabeled data has always been more readily available for researchers and industrial applications but supervised learning techniques consistently outperformed unsupervised learning techniques, limiting our capability to capitalise on the massive volume of unlabeled data. Recently, self-supervised learning techniques have attempted to generate supervised signals from unlabeled data to learn a pretask and thus generate general visual representations. However, they are still in their early stage for computer vision tasks due to the different modalities and high-dimensional input signals like images, videos (with audio), 3D objects and geometry. This research studies the generalisation, robustness, and reusability of visual features learned from self-supervised image-based models for video-based tasks like action recognition and action retrieval for UCF101 and HMDB51 datasets. This research proposes a deep learning model that can be trained to adapt visual features learned from image-based models for action recognition and action retrieval task. Finally, clustering and silhouette score analysis is conducted to objectively evaluate the quality of these visual features for video tasks. The trained model head outperforms other video-based models trained on a similar dataset for the action recognition task by a margin greater than 20%. For action retrieval, the performance is highly competitive to the stateof-the-art models trained on much larger datasets than the self-supervised models used in this research. Silhouette score analysis results highlight that the image-based visual features cluster the videos correctly though the cluster boundaries are not very distinctive. The results from the experimental procedures univocally conclude that visual features from self-supervised image-based models can be adapted and reused for video-based tasks. It also highlights that different image-based self-supervised models can adapt to video-based tasks; thus, further studies should explore jointly training selfsupervised models for image and video modalities.
