---
layout: single
title: "Video-BrowseComp: Benchmarking Agentic Video Research on Open Web"
permalink: /video-browsecomp/
author_profile: false
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"
---

<div align="center">
    <img src="../images/videobrowsecomp_teaser.png" alt="Video-BrowseComp Teaser" width="100%" style="display:none;"/> <!-- Placeholder for teaser if available -->
</div>

<div align="center">
    <strong>Zhengyang Liang<sup>1,♣</sup>, Yan Shu<sup>2,♣</sup>, Xiangrui Liu<sup>3</sup>, Minghao Qin<sup>3</sup>, Kaixin Liang<sup>4</sup>, Paolo Rota<sup>2</sup>, Nicu Sebe<sup>2</sup>, Zheng Liu<sup>3</sup>, Lizi Liao<sup>1</sup></strong>
    <br>
    <sup>1</sup>Singapore Management University, <sup>2</sup>University of Trento, <br>
    <sup>3</sup>Beijing Academy of Artificial Intelligence, <sup>4</sup>Beijing University of Posts and Telecommunications
    <br>
    <br>
    <a href="https://arxiv.org/abs/2504.12516" class="btn btn--primary">Paper</a>
    <a href="https://github.com/liang-zhengyang/Video-BrowseComp" class="btn btn--success">Code</a>
    <a href="https://huggingface.co/datasets/liang-zhengyang/Video-BrowseComp" class="btn btn--info">Dataset</a>
</div>

## Abstract

The evolution of autonomous agents is redefining information seeking, transitioning from passive retrieval to proactive, open-ended web research. However, while textual and static multimodal agents have seen rapid progress, a significant modality gap remains in the web's most dynamic modality: video. Existing video benchmarks predominantly focus on passive perception, feeding curated clips to models without requiring external retrieval. They fail to evaluate agentic video research, which necessitates actively interrogating video timelines, cross-referencing dispersed evidence, and verifying claims against the open web. 

To bridge this gap, we present **Video-BrowseComp**, a challenging benchmark comprising 210 questions tailored for open-web agentic video reasoning. Unlike prior benchmarks, Video-BrowseComp enforces a mandatory dependency on temporal visual evidence, ensuring that answers cannot be derived solely through text search but require navigating video timelines to verify external claims. Our evaluation of state-of-the-art models reveals a critical bottleneck: even advanced search-augmented models like GPT-5.1 (w/ Search) achieve only 23.81% accuracy. Our analysis reveals that these models largely rely on textual proxies, excelling in metadata-rich domains (e.g., TV shows with plot summaries) but collapsing in metadata-sparse, dynamic environments (e.g., sports, gameplay) where visual grounding is essential. As the first open-web video research benchmark, Video-BrowseComp advances the field beyond passive perception toward proactive video reasoning.

## Leaderboard

We evaluate state-of-the-art models on Video-BrowseComp. The accuracy (%) is reported for Overall (OA) and three difficulty levels (Level 1, Level 2, Level 3).

| Model | Overall Acc (%) | Level 1 (%) | Level 2 (%) | Level 3 (%) | Calibration Error (%) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Tool-Free Models** | | | | | |
| Qwen3-VL-8B-Thinking | 7.14 | 12.00 | 0.00 | 0.00 | 52.49 |
| Qwen3-VL-235B-A22B-Instruct | 13.33 | 22.40 | 0.00 | 0.00 | 77.64 |
| GLM-4.6V | 10.95 | 16.80 | 3.23 | 0.00 | 44.40 |
| gpt-4o-2024-11-20 | 17.62 | 28.00 | 3.23 | 0.00 | 58.81 |
| gpt-4o-mini-2024-07-18 | 9.52 | 16.00 | 0.00 | 0.00 | 63.55 |
| gpt-5-mini-2025-08-07 | 15.71 | 26.40 | 0.00 | 0.00 | 37.47 |
| gemini-2.5-flash-2025-06 | 16.67 | 27.20 | 1.61 | 0.00 | 77.79 |
| gemini-2.5-pro-2025-06 | 19.52 | 31.20 | 3.23 | 0.00 | 79.18 |
| **Search Models** | | | | | |
| gemini-2.5-flash-2025-06 (w/ Search) | 20.95 | 32.80 | 4.84 | 0.00 | 35.98 |
| gemini-2.5-pro-2025-06 (w/ Search) | **23.81** | **37.60** | 4.84 | 0.00 | 31.45 |
| gpt-5.1-2025-11-13 (w/ Search) | 15.24 | 21.60 | 6.45 | 4.35 | **30.20** |
| o4-mini-deep-research-2025-06-26 | 22.86 | 30.40 | **12.90** | **8.70** | 42.55 |

<br>
*Note: Bold indicates the best performance.*

## Citation

```bibtex
@article{liang2025video,
  title={Video-BrowseComp: Benchmarking Agentic Video Research on Open Web},
  author={Liang, Zhengyang and Shu, Yan and Liu, Xiangrui and Qin, Minghao and Liang, Kaixin and Rota, Paolo and Sebe, Nicu and Liu, Zheng and Liao, Lizi},
  journal={arXiv preprint},
  year={2025}
}
```
