---
title: "Rethinking KV Cache Eviction for Agentic LLM Serving"
collection: publications
category: techreports
permalink: /publication/2026-10-30-fan-penelope-kv-cache-eviction-agentic-llm-serving-arxiv
excerpt: "Agent workloads reuse long histories across turns, and recomputing KV near the end of a sequence costs the most. Penelope keeps shared prefixes and evicts KV from the start of the remaining history, so the cached suffix survives. It co-designs eviction, KV recomputation, and GPU-CPU cache management in SGLang. On real agent traces with three Qwen3 models, Penelope cuts mean time to first token by up to 76% and job completion time by up to 60% over SGLang."
date: 2026-10-30
venue: "arXiv preprint arXiv:2611.00391"
paperurl: "https://arxiv.org/abs/2611.00391"
citation: "Fan, J., Meng, H., Xia, Y., Chen, H. M., Li, D., & Nikolopoulos, D. S. (2026). *Rethinking KV Cache Eviction for Agentic LLM Serving*. arXiv:2611.00391 [cs.DC]."
---
