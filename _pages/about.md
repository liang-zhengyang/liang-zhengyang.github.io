---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

Zhengyang Liang is currently first-year PhD at Singapore Management University, supervised by Prof.[Lizi Liao](https://liziliao.github.io/).I used to work as a research intern at Beijing Academic of Artificial Intelligence, supervised by PI.[Zheng Liu](https://scholar.google.com/citations?hl=zh-CN&user=k2SF4M0AAAAJ) and PI.[Bo Zhao](https://www.bozhao.me/). Dedicated to exploring Video MLLM. Before that, I got my bachelor's degree at Beijing University of Posts and Telecommunications.

My research interest includes MLLM, Video LLM and Video Agent. <a href='https://scholar.google.com/citations?user=9IC8FBQAAAAJ'></a> 

✉️ Feel free to contact me with email: chr1ce@foxmail.com
<!-- (You can also use google scholar badge <a href='https://scholar.google.com/citations?user=9IC8FBQAAAAJ'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>). -->


# 🔥 News
- *2025.11*: &nbsp;🎉🎉 We released UniVA, an open-source universal video agent. Try it on [UniVA](https://univa.online).
- *2025.07*: &nbsp;🎉🎉 One paper accepted by ACMMM 2025.
- *2025.06*: &nbsp;🎉🎉 Video-XL-2 is released, try it on [Video-XL-2](https://unabletousegit.github.io/video-xl2.github.io/).
- *2025.05*: &nbsp; I will start my PhD journey in SMU at August. Supervised by Prof.[Lizi Liao](https://liziliao.github.io/).
- *2025.03*: &nbsp; Three papers have accepted by CVPR 2025. Congratulations to all collaborators.
- *2024.05*: &nbsp; I joined Beijing Academic of Artificial Intelligence as a research intern.
- *2024.07*: &nbsp; I got my bachelor degree from Beijing University of Posts and Telecommunications.
- *2023.12*: &nbsp; I joined Lenovo Research as a research intern.


# 📝 Publications 
<div class='paper-box'><div class='paper-box-image'><div class="paper-image-container"><div class="badge">Arxiv</div><img src='images/univa.png' alt="sym" width="200px" height="150px"></div></div>
<div class='paper-box-text' markdown="1">

[UniVA: Universal Video Agent towards Open-Source Next-Generation Video Generalist
](https://arxiv.org/abs/2511.08521)

<strong>Zhengyang Liang<sup>*</sup></strong>, Daoan Zhang<sup>*</sup>, Huichi Zhou, Rui Huang, Bobo Li, Yuechen Zhang, Shengqiong Wu, Xiaohan Wang, Jiebo Luo, Lizi Liao, Hao Fei<sup>✉</sup>

[**Paper**](https://arxiv.org/abs/2511.08521)|[**HomePage**](https://univa.online)|[**Code**](https://github.com/univa-agent/univa)|[**Benchmark**](https://huggingface.co/datasets/chr1ce/UniVA-Bench) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div class="paper-image-container"><div class="badge">Arxiv</div><img src='images/timescope.png' alt="sym" width="200px" height="150px"></div></div>
<div class='paper-box-text' markdown="1">

[TimeScope: Towards Task-Oriented Temporal Grounding In Long Videos](https://arxiv.org/abs/2509.26360)

Xiangrui Liu<sup>*</sup>, Minghao Qin<sup>*</sup>, Yan Shu, <strong>Zhengyang Liang</strong>, Yang Tian, Chen Jason Zhang, Bo Zhao, Zheng Liu<sup>✉</sup>

[**Paper**](https://arxiv.org/abs/2509.26360) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div class="paper-image-container"><div class="badge">Arxiv</div><img src='images/videoxl2.png' alt="sym" width="200px" height="150px"></div></div>
<div class='paper-box-text' markdown="1">

[Video-XL-2: Towards Very Long-Video Understanding Through Task-Aware KV Sparsification](https://arxiv.org/abs/2506.19225)

Minghao Qin<sup>*</sup>, Xiangrui Liu<sup>*</sup>, <strong>Zhengyang Liang<sup>*</sup></strong>, Yan Shu, Huaying Yuan, Juenjie Zhou, Shitao Xiao, Bo Zhao, Zheng Liu<sup>✉</sup>

[**Paper**](https://arxiv.org/abs/2506.19225)|[**HomePage**](https://unabletousegit.github.io/video-xl2.github.io/)|[**Code**](https://github.com/VectorSpaceLab/Video-XL)|[**Model**](https://huggingface.co/BAAI/Video-XL-2) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div class="paper-image-container"><div class="badge">ACL 2025</div><img src='images/visir.png' alt="sym" width="200px" height="150px"></div></div>
<div class='paper-box-text' markdown="1">

[Any Information Is Just Worth One Single Screenshot: Unifying Search With Visualized Information Retrieval](https://arxiv.org/abs/2502.11431)

Ze Liu, <strong>Zhengyang Liang</strong>, Junjie Zhou, Zheng Liu<sup>✉</sup>, Defu Lian

[**Paper**](https://arxiv.org/abs/2502.11431)|[**Code**](https://github.com/VectorSpaceLab/Vis-IR)|[**Model**](https://huggingface.co/BAAI/BGE-VL-Screenshot)|[**Dataset**](https://huggingface.co/datasets/marsh123/VIRA) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div class="paper-image-container"><div class="badge">CVPR 2025(Oral)</div><img src='images/videoxl.jpg' alt="sym" width="200px" height="150px"></div></div>
<div class='paper-box-text' markdown="1">

[Video-XL: Extra-Long Vision Language Model for Hour-Scale Video Understanding](https://arxiv.org/abs/2409.14485)

Yan Shu, Zheng Liu<sup>✉</sup>, Peitian Zhang, Minghao Qin, Junjie Zhou, <strong>Zhengyang Liang</strong>, Tiejun Huang, Bo Zhao<sup>✉</sup>

[**Paper**](https://arxiv.org/abs/2409.14485)|[**Code**](https://github.com/VectorSpaceLab/Video-XL) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div class="paper-image-container"><div class="badge">CVPR 2025</div><img src='images/mlvu.jpg' alt="sym" width="200px" height="150px"></div></div>
<div class='paper-box-text' markdown="1">

[MLVU: A Comprehensive Benchmark for Multi-Task Long Video Understanding](https://arxiv.org/abs/2406.04264)

Junjie Zhou<sup>*</sup>, Yan Shu<sup>*</sup>, Bo Zhao<sup>*</sup>, Boya Wu, <strong>Zhengyang Liang</strong>, Shitao Xiao, Xi Yang, Yongping Xiong, Bo Zhang, Tiejun Huang, Zheng Liu<sup>✉</sup>

[**Paper**](https://arxiv.org/abs/2406.04264)|[**Code**](https://github.com/JUNJIE99/MLVU/) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div class="paper-image-container"><div class="badge">CVPR 2025</div><img src='images/unveil2024.jpg' alt="sym" width="200px" height="150px"></div></div>
<div class='paper-box-text' markdown="1">

[Unveiling the Ignorance of MLLMs: Seeing Clearly, Answering Incorrectly](https://arxiv.org/abs/2406.10638)

Yexin Liu<sup>*</sup>, <strong>Zhengyang Liang<sup>*</sup></strong>, Yueze Wang, Xianfeng Wu, Feilong Tang, Muyang He, Jian Li, Zheng Liu, Harry Yang, Sernam Lim, Bo Zhao<sup>✉</sup>

[**Paper**](https://arxiv.org/abs/2406.10638)|[**Code**](https://github.com/BAAI-DCAI/Multimodal-Robustness-Benchmark)|[**Dataset**](https://huggingface.co/datasets/BAAI/Multimodal-Robustness-Benchmark) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div class="paper-image-container"><div class="badge">ACMMM 2025</div><img src='images/dsmd.jpg' alt="sym" width="200px" height="150px"></div></div>
<div class='paper-box-text' markdown="1">

[Dynamic Self-adaptive Multiscale Distillation from Pre-trained Multimodal Large Model for Efficient Cross-modal Representation Learning](https://arxiv.org/abs/2404.10838)

**Zhengyang Liang**, Meiyu Liang<sup>✉</sup>, Wei Huang, Yawen Li, Zhe Xue

[**Paper**](https://arxiv.org/abs/2404.10838)|[**Code**](https://github.com/chrisx599/DSMD) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div class="paper-image-container"><div class="badge">AAAI 2023</div><img src='images/cmgch.jpg' alt="sym" width="200px" height="150px"></div></div>
<div class='paper-box-text' markdown="1">

[Self-Supervised Multi-Modal Knowledge Graph Contrastive Hashing for Cross-Modal Search](https://ojs.aaai.org/index.php/AAAI/article/view/29280)

Meiyu Liang, Junping Du<sup>✉</sup>, **Zhengyang Liang**, Yongwang Xing, Wei Huang, Zhe Xue (Finished as first student author)

[**Paper**](https://ojs.aaai.org/index.php/AAAI/article/view/29280) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
</div>
</div>

<!-- - [Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet](https://github.com), A, B, C, **CVPR 2020** -->

# 🥇 Honors and Awards
- *2023*, Honorable Mention of Mathematical Contest in Modeling of America
- *2022*, The second prize of China(First prize of Beijing) of Mathematical Contest in Modeling of China 

# 📖 Educations
- *2025.08 - Now*, Ph.D, Singapore Management University.
- *2020.09 - 2024.07*, Bachelor, Beijing University of Posts and Telecommunications.

<!-- # 💬 Invited Talks
- *2021.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.03*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  \| [\[video\]](https://github.com/) -->

# 💻 Internships
- *2024.05 - 2025.05*, [Beijing Academic of Artificial Intelligence](https://www.baai.ac.cn/), Beijing.
- *2023.12 - 2024.04*, [Lenovo Research](https://research.lenovo.com/webapp/view/index.html), Beijing.
