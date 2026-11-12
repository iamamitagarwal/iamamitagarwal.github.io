---
permalink: /projects/multimodal-media/
title: "Multimodal Media: Search, Storytelling & Evaluation"
layout: single
classes: wide project-story
project_story: true
last_modified_at: 2026-11-11
description: "Amit Agarwal's work on media understanding and search, text-to-storyboard evaluation, narrative consistency and research directions in creative editing and character-aware retrieval."
---

I work with science, media and application teams on how AI understands, finds and transforms visual content. My work connects video and image retrieval with evaluation of creative workflows, from locating a useful scene to checking whether generated frames preserve a written story.

## Finding moments, characters and narrative context

A useful media result can be a moment within a long video, a visual relationship that a caption leaves out, or a sequence of scenes that develops an idea. I lead work connecting visual and language representations with search and evaluation so applications can retrieve evidence at that level of detail.

Current research directions include character- and storyline-aware search: finding scenes involving a character, following their role across events, or locating a moment by what happens rather than its file name. These questions connect retrieval with temporal understanding and memory across a sequence.

I work on these capabilities as part of a broader [shared knowledge foundation](/projects/shared-knowledge-store/#multimodal-knowledge). The architectural goal is to make media evidence reusable across search, question answering and creative applications.

## From a written story to visual frames

I contribute to research on evaluating text-to-storyboard generation, where a model turns a short narrative into a multi-panel visual sequence. A visually attractive board may still omit a key event, reverse the order of actions or change a character between panels.

My contributions include proposing analysis of how many frames are needed to represent a story and how that choice affects evaluation and judge training. I also examined how panel boundaries and cropping affect the construction of controlled tests. These are research-design questions about what an evaluator can reliably inspect.

The evaluation approach considers the opening, development, turning point and ending, along with the causal progression between them. It also asks whether a vision-language model—a model that interprets images and text—can judge the board faithfully, rather than relying on the written story or overlooking errors in the image.

## Creative editing and consistency

I am exploring how these ideas extend to scene editing and creative workflows. A change to one scene raises questions about what should change and what should remain stable: character identity, setting, visual style and the narrative role of the scene.

The research connects generation, editing and evaluation. It asks how to test whether a requested change happened, whether unrelated content was preserved and whether the resulting sequence still makes sense. Character search and retained narrative context offer complementary ways to find and reuse relevant material.

## Connecting models with application decisions

I bring research questions, model comparisons and evaluation design into discussions with engineering and application teams. The choices include how content is represented, which evidence the model sees, how an evaluation is calibrated and what a workflow needs to retain between steps.

Earlier at Jio Platforms, I led computer-vision work on video analytics, detection and tracking through data design, model evaluation and product integration. That experience informs how I approach the gap between a promising model result and a useful application.

My [agent and multimodal evaluation work](/projects/multimodal-evaluation/) examines the measurement methods behind these decisions. Related published work includes [video-understanding robustness](/publications/2024-mvtamperbench-evaluating-robustness-of-vision-language-models/) and [image–text metric reliability](/publications/2026-do-image-text-metrics-respect-semantic-invariances/).

[All projects](/projects/) · [Research papers](/publications/) · [Discuss this work](mailto:amit.pinaki@gmail.com)
