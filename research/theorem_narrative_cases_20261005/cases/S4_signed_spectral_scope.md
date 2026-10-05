# S4：精确极值与等号分类；题材接近不等于定理接近

Qin, Li, *Spectral Turán problem for $\mathcal{K}_{3,3}^{-}$-free signed graphs*.

- 精读版本：[arXiv:2508.05500v1](https://arxiv.org/pdf/2508.05500v1)，2025-08-07，19 页
- arXiv DOI：[10.48550/arXiv.2508.05500](https://doi.org/10.48550/arXiv.2508.05500)
- 本次重点：pp.1–4,6,17–18；Theorem1、Lemma3、§3
- 期刊状态以目录的核验字段为准；不能由致谢中出现referees推断已发表

## 源文叙事地图（限量概述）

Title: one forbidden signed family. Abstract: unsigned ancestry, signed bipartite exclusions, smaller solved case, present case. Gap: the K_{3,3} exclusion (§1). Theorem1: for unbalanced signed graphs of order n≥7 avoiding every unbalanced signed K_{3,3}, the index is at most n−2, with a switching-isomorphism equality characterization. Architecture: exhibit the candidate, compare quotient spectra, switch an extremal eigenvector to nonnegative coordinates, and exclude alternatives (§§2–3). Sharpness is attainment plus classification, not merely a close numerical bound. The selected version ends with the proof, acknowledgements and references; it has no separate closing-question section. The forbidden family refers to unbalanced signings of K_{3,3}, not K_{3,3} with an edge deleted.

## 对 C029 的原创分析

这篇的意义首先是划清“相近论文”的边界。它比较一个禁子图类里不同底图与符号的最大index；C029固定cycle-square底图和规定单元，控制两端的谱半径上界。研究对象同属符号图，量词、优化方向和输出层次却不同。C029不应借用“谱Turán问题”来增加表面分量。

对C029可借鉴的是让候选图先于矩阵计算出现。读者看到符号词的端部与接缝，就能知道后面的六维边界不是凭空挑选的矩阵尺寸。现有边界图可承担这一责任，图注应解释所保留坐标及相邻链，而不只标“示意图”。

不能直接照搬的是多页辅助多项式比较之后才交代主证明的组织。C029的读者需要先知道每个量在最后正定比较中的角色，然后再看到精确有理数前提。

## 为何是数学文章；为何不是首选美文模板

它有明确极值问题、候选结构、必要性证明和充分性验证，并非工程测试报告。但对当前“解释主定理为何动人”的任务，它更适合作为范围校准和同领域图示范例，优先级低于S1–S3。
