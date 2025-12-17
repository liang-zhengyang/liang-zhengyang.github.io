---
layout: single
title: "Video-BrowseComp: Benchmarking Agentic Video Research on Open Web"
permalink: /video-browsecomp/
author_profile: false
toc: true
toc_label: "Table of Contents"
toc_icon: "cog"
classes: wide
---

<style>
    .author-block {
        text-align: center;
        margin-bottom: 20px;
    }
    .affiliation-block {
        text-align: center;
        font-size: 0.9em;
        color: #666;
        margin-bottom: 30px;
    }
    .button-block {
        text-align: center;
        margin-bottom: 40px;
    }
    .abstract-box {
        background-color: #f8f9fa;
        border-left: 5px solid #20c997;
        padding: 20px;
        margin-bottom: 30px;
        border-radius: 4px;
    }
    .leaderboard-table {
        width: 100%;
        border-collapse: collapse;
        margin: 20px 0;
        font-size: 0.9em;
        font-family: sans-serif;
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
    }
    .leaderboard-table thead tr {
        background-color: #009879;
        color: #ffffff;
        text-align: center;
    }
    .leaderboard-table th,
    .leaderboard-table td {
        padding: 12px 15px;
        text-align: center;
        border-bottom: 1px solid #dddddd;
    }
    .leaderboard-table tbody tr {
        border-bottom: 1px solid #dddddd;
    }
    .leaderboard-table tbody tr:nth-of-type(even) {
        background-color: #f3f3f3;
    }
    .leaderboard-table tbody tr:last-of-type {
        border-bottom: 2px solid #009879;
    }
    .leaderboard-table tbody tr:hover {
        color: #009879;
        font-weight: bold;
    }
    .best-score {
        font-weight: bold;
        color: #d63031;
    }
</style>

<div class="author-block">
    <strong>Zhengyang Liang<sup>1,♣</sup>, Yan Shu<sup>2,♣</sup>, Xiangrui Liu<sup>3</sup>, Minghao Qin<sup>3</sup>, Kaixin Liang<sup>4</sup>, Paolo Rota<sup>2</sup>, Nicu Sebe<sup>2</sup>, Zheng Liu<sup>3</sup>, Lizi Liao<sup>1</sup></strong>
</div>

<div class="affiliation-block">
    <sup>1</sup>Singapore Management University, <sup>2</sup>University of Trento, <br>
    <sup>3</sup>Beijing Academy of Artificial Intelligence, <sup>4</sup>Beijing University of Posts and Telecommunications
</div>

<div class="button-block">
    <a href="https://arxiv.org/abs/2504.12516" class="btn btn--primary btn--large"><i class="fas fa-file-pdf"></i> Paper</a>
    <a href="https://github.com/liang-zhengyang/Video-BrowseComp" class="btn btn--success btn--large"><i class="fab fa-github"></i> Code</a>
    <a href="https://huggingface.co/datasets/liang-zhengyang/Video-BrowseComp" class="btn btn--info btn--large"><i class="fas fa-database"></i> Dataset</a>
</div>

## Abstract

<div class="abstract-box">
The evolution of autonomous agents is redefining information seeking, transitioning from passive retrieval to proactive, open-ended web research. However, while textual and static multimodal agents have seen rapid progress, a significant modality gap remains in the web's most dynamic modality: video. Existing video benchmarks predominantly focus on passive perception, feeding curated clips to models without requiring external retrieval. They fail to evaluate agentic video research, which necessitates actively interrogating video timelines, cross-referencing dispersed evidence, and verifying claims against the open web. 
<br><br>
To bridge this gap, we present <strong>Video-BrowseComp</strong>, a challenging benchmark comprising 210 questions tailored for open-web agentic video reasoning. Unlike prior benchmarks, Video-BrowseComp enforces a mandatory dependency on temporal visual evidence, ensuring that answers cannot be derived solely through text search but require navigating video timelines to verify external claims. Our evaluation of state-of-the-art models reveals a critical bottleneck: even advanced search-augmented models like GPT-5.1 (w/ Search) achieve only 23.81% accuracy. Our analysis reveals that these models largely rely on textual proxies, excelling in metadata-rich domains (e.g., TV shows with plot summaries) but collapsing in metadata-sparse, dynamic environments (e.g., sports, gameplay) where visual grounding is essential. As the first open-web video research benchmark, Video-BrowseComp advances the field beyond passive perception toward proactive video reasoning.
</div>

## Leaderboard

We evaluate state-of-the-art models on Video-BrowseComp. The accuracy (%) is reported for Overall (OA) and three difficulty levels (Level 1, Level 2, Level 3).

<table class="leaderboard-table">
    <thead>
        <tr>
            <th>Model</th>
            <th>Overall Acc (%)</th>
            <th>Level 1 (%)</th>
            <th>Level 2 (%)</th>
            <th>Level 3 (%)</th>
            <th>Calibration Error (%)</th>
        </tr>
    </thead>
    <tbody>
        <tr><td colspan="6" style="text-align:left; background-color:#e0e0e0; font-weight:bold;">Tool-Free Models</td></tr>
        <tr><td>Qwen3-VL-8B-Thinking</td><td>7.14</td><td>12.00</td><td>0.00</td><td>0.00</td><td>52.49</td></tr>
        <tr><td>Qwen3-VL-235B-A22B-Instruct</td><td>13.33</td><td>22.40</td><td>0.00</td><td>0.00</td><td>77.64</td></tr>
        <tr><td>GLM-4.6V</td><td>10.95</td><td>16.80</td><td>3.23</td><td>0.00</td><td>44.40</td></tr>
        <tr><td>gpt-4o-2024-11-20</td><td>17.62</td><td>28.00</td><td>3.23</td><td>0.00</td><td>58.81</td></tr>
        <tr><td>gpt-4o-mini-2024-07-18</td><td>9.52</td><td>16.00</td><td>0.00</td><td>0.00</td><td>63.55</td></tr>
        <tr><td>gpt-5-mini-2025-08-07</td><td>15.71</td><td>26.40</td><td>0.00</td><td>0.00</td><td>37.47</td></tr>
        <tr><td>gemini-2.5-flash-2025-06</td><td>16.67</td><td>27.20</td><td>1.61</td><td>0.00</td><td>77.79</td></tr>
        <tr><td>gemini-2.5-pro-2025-06</td><td>19.52</td><td>31.20</td><td>3.23</td><td>0.00</td><td>79.18</td></tr>
        <tr><td colspan="6" style="text-align:left; background-color:#e0e0e0; font-weight:bold;">Search Models</td></tr>
        <tr><td>gemini-2.5-flash-2025-06 (w/ Search)</td><td>20.95</td><td>32.80</td><td>4.84</td><td>0.00</td><td>35.98</td></tr>
        <tr><td>gemini-2.5-pro-2025-06 (w/ Search)</td><td><span class="best-score">23.81</span></td><td><span class="best-score">37.60</span></td><td>4.84</td><td>0.00</td><td>31.45</td></tr>
        <tr><td>gpt-5.1-2025-11-13 (w/ Search)</td><td>15.24</td><td>21.60</td><td>6.45</td><td>4.35</td><td><span class="best-score">30.20</span></td></tr>
        <tr><td>o4-mini-deep-research-2025-06-26</td><td>22.86</td><td>30.40</td><td><span class="best-score">12.90</span></td><td><span class="best-score">8.70</span></td><td>42.55</td></tr>
    </tbody>
</table>

## Citation

```bibtex
@article{liang2025video,
  title={Video-BrowseComp: Benchmarking Agentic Video Research on Open Web},
  author={Liang, Zhengyang and Shu, Yan and Liu, Xiangrui and Qin, Minghao and Liang, Kaixin and Rota, Paolo and Sebe, Nicu and Liu, Zheng and Liao, Lizi},
  journal={arXiv preprint},
  year={2025}
}
```