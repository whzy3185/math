# S5：术语改变会改变问题；第二极值必须说明排除了谁

Li, Qin, *The index of $t\mathcal{C}_3^{-}$-free signed graphs*.

- 精读版本：[arXiv:2512.07579v1](https://arxiv.org/pdf/2512.07579v1)，2025-12-08，17 页
- arXiv DOI：[10.48550/arXiv.2512.07579](https://doi.org/10.48550/arXiv.2512.07579)
- 强匹配期刊对应版：*Maximum and second maximum indices of $t\mathcal{C}_3^{-}$-free unbalanced signed graphs*，Discrete Applied Mathematics394，168–179；[DOI10.1016/j.dam.2026.07.026](https://doi.org/10.1016/j.dam.2026.07.026)。已分配2026-12-15未来issue，当前有出版方预览；精确在线日期未核实。作者顺序、问题与独特定理分段匹配，未作全版本等同性证明。
- 本次重点：pp.1–3,6,11–13,16；Theorems1–2、Lemma8及应用
- 与S4为同一研究团队，不能当作两个独立群体的风格证据

## 源文叙事地图（限量概述）

Title: maximum index under a triangle restriction. Abstract: predecessor, maximum, second maximum. Prior work: unsigned disjoint-copy problems and signed predecessors (§1). Critical gap/model choice: the forbidden unbalanced triangles need not be vertex-disjoint (p.3). Theorem1 treats the maximum for t≥2,n≥6; Theorem2 excludes its switching class and splits second-maximum cases for t≥3,n≥9. Architecture: compare candidates, prove the structural Lemma8, reuse it for the main result and refinements (§§2–3). Limits: parameter intervals and the exclusion in the runner-up question are essential. The paper ends after the proof and references, without a dedicated new-question section. Switching equivalence must be retained when interpreting displayed graph representatives.

## 对 C029 的原创分析

“任意长度的单元”很容易被读成任意符号的单元；“holonomy任意”容易被读成各个接缝都有独立可选相位。C029必须在读者形成错误直觉之前给出合法词w_j和全局α∈{±1}。这不是把摘要写得局促，而是让读者准确知道自由度在哪里。

C029目前没有完整最优族，当然更没有第二最优族。不能把一个精确周期竞争者与另一构造的大小关系写成全局排序。主定理是一整族显式对象的统一控制，已经可以形成独立问题，无需借“极值完整分类”的叙事包装。

## 为何保留这个案例

它是数学论文，且展示了最大值与排除最大者后的第二问题如何分开。不过，背景中先讨论vertex-disjoint、随后改变模型会增加阅读成本。对当前稿件更好的做法，是一开始就把将研究的模型说明白。本研究保留它作为反向校准，不将其所有组织方式都推荐给C029。
