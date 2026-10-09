---
title: "Serving Masked Diffusion LLMs: Characterization and Design Principles from Real Hardware"
collection: publications
category: techreports
permalink: /publication/2026-08-24-amin-masked-diffusion-llm-serving-arxiv
excerpt: "A hardware characterization of masked diffusion language models under concurrent serving on an H200 GPU, showing that request complexity clusters into discrete step-count levels and that only 24% of single-request wall-clock time is GPU computation, with the remainder lost to CPU-side dispatch overhead. Batching recovers much of this gap (16.0x throughput at batch size 16), indicating that diffusion LLM serving needs parallelism structured differently from autoregressive pipelines."
date: 2026-08-24
venue: "arXiv preprint arXiv:2608.23807"
paperurl: "https://arxiv.org/abs/2608.23807"
citation: "Amin, F., Afroz, S., Moghadampanah, M., & Nikolopoulos, D. S. (2026). *Serving Masked Diffusion LLMs: Characterization and Design Principles from Real Hardware*. arXiv:2608.23807 [cs.AI]."
---
