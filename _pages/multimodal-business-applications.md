---
permalink: /projects/multimodal-business-applications/
title: "Fusion Applications & Enterprise Agents"
layout: single
classes: wide project-story
project_story: true
last_modified_at: 2026-11-12
description: "Amit Agarwal's multimodal applied-science leadership for Oracle Fusion applications: image understanding, cross-modal retrieval, evaluation and collaboration with application engineering."
---

I led multimodal applied-science contributions for Oracle Fusion applications, working with application engineering to make image understanding and enterprise knowledge useful inside business workflows. My work connects model research with the quality, latency and integration decisions that determine whether an AI capability is useful in a product.

## Bringing multimodal understanding into Fusion

My contributions include science behind an image-to-text capability deployed in production, as well as multimodal retrieval demonstrations spanning images, audio and video. The broader research problem is to make information inside visual and document-rich content available to applications that need to answer questions and assist with business tasks.

A recurring challenge was understanding what happened between a model comparison and the answer an application produced. Parsing could lose visual information; the order of retrieved evidence and its citations could change what the model could use. Our science and application-engineering reviews examined those differences alongside model and prompt choices, rather than treating an offline score as the final product decision.

I brought image, audio and video retrieval demonstrations into that collaboration, making the behavior visible to the teams integrating it. In later multimodal evaluation work, I developed tooling that retains query-level evidence and explicitly marks incomplete runs. The goal is to give science and application teams a comparison they can inspect, including cases where an additional retrieval signal introduces noise instead of useful context.

## From business evidence to agentic workflows

Oracle Fusion Cloud Applications connects enterprise resource planning (ERP) and other business suites with a growing set of agentic capabilities. [AI Agent Studio](https://www.oracle.com/news/announcement/oracle-expands-ai-agent-studio-for-fusion-applications-with-agentic-applications-builder-2026-03-24/) supports composing agents and workflows, integrating business content, retaining context and observing execution. [Fusion Claw](https://www.oracle.com/news/announcement/ai-world-oracle-advances-outcome-driven-ai-across-fusion-applications-2026-10-26/) adds a runtime for longer-running, governed business processes.

This evolution makes the quality of business evidence more consequential. In a multi-tool workflow, a misunderstanding can affect the next action as well as the answer. An agent needs the applicable document or image, the relevant business context and a way to recognize uncertainty before proceeding.

For my work with Fusion teams, that means evaluating multimodal understanding in the context of the task an agent is trying to complete. An answer may look plausible while missing the evidence needed for the next tool call or business decision.

## Reusing research across product boundaries

The same questions arise across [shared knowledge infrastructure](/projects/shared-knowledge-store/), [database AI](/projects/database-ai/) and [support agents](/projects/agentic-knowledge-systems/): what does the evidence mean, is it sufficient for the task and how do we know the model used it correctly?

I help teams carry research and evaluation methods across those boundaries while accounting for each product's requirements. My work on [ranking enterprise evidence](/projects/enterprise-retrieval/) and [multimodal evaluation](/projects/multimodal-evaluation/) supplies the scientific foundation for those decisions.

[Oracle Fusion application context](https://www.oracle.com/news/announcement/ai-world-oracle-advances-outcome-driven-ai-across-fusion-applications-2026-10-26/) · [All projects](/projects/) · [Discuss this work](mailto:amit.pinaki@gmail.com)
