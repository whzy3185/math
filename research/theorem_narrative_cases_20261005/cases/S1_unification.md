# S1：统一性应有一个可以检查的共同机制

Ai, Lei, Ning, Shi, *Graph operations and a unified method for kinds of Turán-type problems on paths, cycles and matchings*.

- 精读版本：[arXiv:2312.08226v2](https://arxiv.org/pdf/2312.08226v2)，2024-01-29，25 页
- arXiv DOI：[10.48550/arXiv.2312.08226](https://doi.org/10.48550/arXiv.2312.08226)
- 期刊版题名略变：*Graph operations and a unified method for Turán-type problems on paths, cycles, and matchings*；Canadian Journal of Mathematics，2025-11-03 在线，First View 1–27；[期刊 DOI](https://doi.org/10.4153/S0008414X25101788)
- 本次重点：pp.1,4–6,9–10,14,17,19,23；不是期刊全文逐行审计

## 源文叙事地图（限量概述）

Title: operations and unification. Abstract: feasible parameters, three structural theorems, applications. Prior work: separate extremal, degree-power and spectral problems (§1). Gap: uncovered parameter ranges and explicit Problems 1–2 (p.4). Obstruction: a familiar path-to-cycle join does not preserve spectral ordering (p.23). Theorems: feasible parameters force extremizers into specified families (§2); weak feasibility gives an attaining member, not all extremizers. Architecture: verify parameters (§3), derive applications (§4), prove structural reductions (§5). Sharpness/limits: distinguish extremal value from complete classification. Closing questions: ordering under joins, weaker connectivity, and weak-feasibility equality cases (§6).

## 对 C029 的原创分析

统一性不等于把几条结果放在同一个标题下。对定理1.1来说，可检验的共同对象是固定谱帽下的六维边界矩阵；共同的操作是消去内部；共同的控制是两次链端关联。这三个事实足以支撑“共同机制”，但不足以支撑“任意图参数的统一理论”。这一层级差异应写进摘要和相关工作。

引言段落的任务应按逻辑分配：第一段给出等长单元这个熟悉的可解场景；第二段使读者看到长度独立变化以后原分解不再适用；第三段提出为何误差不能随单元数累积；第四段才告诉读者共同边界量是什么。这是本研究为C029提出的结构，不是模仿源文句型。

C029还有一个适合保留的“看似可省、实际不可省”的小结：从相同单元的所有相位得到上界，不能直接当成不同单元混合的证明。两个问题看上去只差“长度不等”，却需要不同的组合论证。把这一点说明白，比宣布方法“强大”更能传达定理的价值。

反面边界也应具体。C029得到的是规定构造的统一上界，没有得到最小谱半径，也没有得到全部最优符号。一个有数学分量的叙事应让读者清楚知道量词停在哪里。

## 为何是数学文章范例

可借鉴的是抽象定义、结构定理与多种后果之间的证明关系。最有价值的是“少了一个条件，结论也必须降级”的自我限制。不能照搬其优先权措辞；也不必照搬以章节列表为主的路线图。
