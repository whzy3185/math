# Domination v6：等号刚性与近等号形状之间的距离

对象：v6，源PDF SHA256：`b2752241c9c2dedf14a0ffd76e536698588757bb2c37f8d1df91e9ba95e31a8c`。以下为叙事草稿，不修改数学声明。

## 推荐主线

唯一最小支配集给出最低阶数3γ；再增加一个或两个顶点，边数极值和全部等号结构可以完全确定。但这个刚性结论并不自动给出通常直觉中的dense edit stability。真正的定量尺度是绝对边亏损t对应γt量级的编辑代价。

范围：有限简单二部图、无孤立点、唯一minimum-cardinality dominating set的大小γ≥2；阶数3γ+r,r∈{1,2}。主类不要求连通。minimum不能改成inclusion-minimal。编辑距离对所有顶点双射最小化，不固定原二部分划分或支配集。

## 确切结论与来源责任

第一边界最大边数为γ(γ+7)/2，唯一等号图为H(⌈γ/2⌉,⌊γ/2⌋)。第二边界为⌈γ²/2⌉+5γ：γ=2有H2(1,1),F0,F1三类；γ=2k+1≥3只有H2(k+1,k)；γ=2k≥4有H2(k,k),H2(k+1,k−1)两类。所有等号图连通。

第一边界对每个非负t有d_edit≤min{γ(γ+7)−t,12γt}。下界族只在γ=2k,k≥2,1≤s≤k−1,t=s时声明：s(k+1)≤d_edit≤s(2k+1)。

第二边界对全部图、全部非负t有d_edit(G,E2(γ))≤min{2M2(γ)−t,20γt}。下界族在k≥3,ε∈{0,1},1≤s≤k−2,γ=2k+ε,t=2s时声明：s(k+2)≤d_edit(G,E2(γ))≤2s(k+1)。下界对完整等号族和任意双射成立。12与20未证明最优，未给一般精确距离或最近极值图。

Koch–Narayan已经给出γ=2极值，以及(n,γ)=(10,3)的唯一等号图；Erlbacher已经给出13顶点22边、14顶点28边及某不平衡构造子族。正式稿保留这些原始引用，不能用叙事改写擦去继承关系。

## 原创英文摘要候选

For bipartite graphs without isolated vertices and with a unique minimum dominating set of size γ≥2, we determine the maximum number of edges at orders 3γ+1 and 3γ+2 and classify every equality graph. The maxima are γ(γ+7)/2 and ⌈γ²/2⌉+5γ. We then ask how the equality structure changes under an absolute edge deficit t. Edit distance, minimized over all vertex relabellings, is at most 12γt at the first boundary and 20γt from the full equality family at the second. Connected constructions match the γt order in specified ranges: even γ with 1≤t≤γ/2−1 at the first boundary, and both parities with t=2s,1≤s≤⌊γ/2⌋−2,⌊γ/2⌋≥3 at the second. Thus exact equality classification coexists with failure of dense edit stability: relative edge deficit may vanish while normalized edit distance stays bounded away from zero. The proofs use private-neighbour replacements, local deficit identities, and explicit constructions. Previously known finite examples and construction subfamilies are recovered with attribution.

## 原创引言开头与转折

If a graph has no isolated vertices and its minimum dominating set is unique, each member of that set has at least two exterior private neighbours. A graph with domination number γ therefore has at least 3γ vertices. We study the first two orders above this boundary, where only one or two vertices remain after two private neighbours have been assigned to every center.

This small remainder makes exact extremal analysis possible. It also raises a second question. Once every graph attaining the edge bound is known, how much of its shape is forced by a small deficit? We determine a linear-deficit edit scale and show why a vanishing relative deficit alone does not imply proximity in normalized edit distance.

这里的转折不是抽象宣称“结构复杂而有趣”。它提出一个可精确回答的问题，并让反例和上界讨论同一个量。

## 原创证明总览

Choose two exterior private neighbours for each dominating vertex. With one or two residual vertices, the possible incidences determine which local edge patterns would permit a competing dominating set. Their edge caps give the extremal inequalities; simultaneous saturation forces the equality structures. For near-equality, retain the losses in this count instead of discarding them. Split imbalance, deficient local cells, and missing residual incidences then control the cost of a repair. Modified rows yield the lower constructions, and relabelling-invariant estimates keep them far from every relevant extremizer.

## 参考与迁移边界

[S7](../cases/S7_equality_rigidity.md)的“旧不等式→等号结构”启发把新增数学层次说清；[S3](../cases/S3_quantitative_stability.md)启发把最优性的量、范围与度量分开；[S2](../cases/S2_structural_scale.md)启发解释结构尺度。这里的唯一支配集问题、编辑距离和构造机制均不同于那些论文，不能宣称套用其定理。

## Before/after例子

当前v6已经说出edge-edit stability，不能把它误写成完全没有主线的早期稿。可改进的只是信息顺序。

说明书式示例（本研究构造）：We prove edge bounds, classify equality graphs, and give upper and lower edit estimates.

改为：The equality graphs are completely determined at both boundary orders, yet their near-extremal geometry depends on absolute rather than relative edge loss. Local deficit identities give the upper scale, while explicit connected examples show why that scale cannot be replaced by dense edit stability.

“cannot be replaced”指稿中已有归一化反例，不是声称所有其他稳定性定义都失败。主定理后的范围段落仍须保留。
