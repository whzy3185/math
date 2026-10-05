# S7：一个已经成立的不等式，仍可能留下真正的结构问题

Bai, Gao, Xi, Yue, *On independent domination and packing numbers of subcubic graphs*.

- 精读版本：[arXiv:2401.04617v3](https://arxiv.org/pdf/2401.04617v3)，2024-04-23，19页
- arXiv DOI：[10.48550/arXiv.2401.04617](https://doi.org/10.48550/arXiv.2401.04617)
- Applied Mathematics and Computation524(2026),130048；[期刊 DOI](https://doi.org/10.1016/j.amc.2026.130048)
- 本次重点：pp.1,3–6,10–11,14,17–18；Question1、Theorem3、Lemma3、Propositions1–3、§4

## 源文叙事地图（限量概述）

Title: two graph invariants. Abstract: a predecessor inequality, its equality question, complete classification. Prior work: i(G)≤3ρ(G) for subcubic graphs. Gap: which connected graphs attain equality (Question1,p.3). Obstruction: equality leaves no slack in the predecessor's injection. Theorem3 gives four connected equality graphs. Architecture: reconstruct the inherited injection, turn equality into bijectivity, derive structural propositions, prove an auxiliary packing bound, complete the case analysis (§§2–4). Sharpness is an if-and-only-if classification, not a new universal inequality. The proof ends with the girth-five case; there is no separate closing-question section. The connectedness hypothesis is indispensable to the “four graphs” formulation.

## 对 domination v6 的原创分析

这给出一种正当的新问题来源：一个旧数值结果留下未解释的等号结构。我们的domination稿件必须更进一步区分三层：任意γ的边数极值；全部等号图；绝对边亏损t如何控制到等号族的编辑距离。三层分别需要证明，后两层不是第一层的修辞性附赠。

现有v6已经有真正值得开篇的张力：即使等号族完全明确，相对边亏损趋零仍可能不带来归一化编辑距离趋零；与此同时存在O(γt)的普遍上界，并在规定范围内有匹配阶下界。因此“rigidity”与“stability”需要在不同尺度上解释。不要先用很多页讲小阶反例，再把这个现象埋在后面。

对C029的借鉴则是负面的边界：没有等号分类就不要写rigidity of extremizers；规定词的边界模型与全部最优符号的结构分类是不同问题。C029可以大方承认后者尚未解决，仍然完整讲好统一谱上界。

## 为何是数学文章范例

重新阅读旧证明是为了提取只有等号时才成立的强约束，最终分类；这与仅仅重排旧证明不同。引言中偏多的预备记号可以进一步压缩，因此本研究借鉴其问题来源和证明转折，不主张逐段照搬。
