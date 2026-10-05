# Mycielski v8：同一个投影，三种信息，三对锐界

对象：19页v8。这里是原创叙事方案，不是替换或加强原定理。源PDF SHA256：`928585c2f04a2676c180b91e704a4dadf288f3b85e00038295de21e04a6ad081`。本研究不为尚未公开的稿件猜测链接。

## 推荐主线

一步、两步ordinary Mycielski构造如何改变Hall obstruction？同一投影论证利用的基图信息越强，得到的上界越精确。三层条件应一开始并排出现，读者因此知道常数之间的差别有结构来源。

- 非空有限简单二部基图：一步5/2、两步11/4
- 非空有限简单基图且χ_c(G)<3：一步3、两步23/7
- 非空有限简单基图且χ_f(G)<3：一步3、两步10/3

这些是分别在整类上取到的锐界，不是整类里每个基图都达到。ordinary μ²指连续两次ordinary Mycielski构造；不能换成height-two generalized cone。非空指至少一个顶点，允许无边图。严格小于3不能改成小于等于3；K_{2,2,2}给出端点失败。

对应的达到基图依次为K2与K_{2,2}；K_{11/4}与K_{20/7}；M4与M4。M2=K2、M_{r+1}=μ(Mr)，因此μ²(M4)=M6。

## 与参考写法的连接

[S1](../cases/S1_unification.md)启发共同机制先于应用列表；[S6](../cases/S6_construction_and_limits.md)启发上界与显式达到见证配对；[S7](../cases/S7_equality_rigidity.md)提醒一般等号限制不等于完整分类。这个主线是当前证明的编辑解释，不以参考论文为本文数学结果的来源。

## 原创英文标题与摘要

**Sharp Hall bounds for one and two Mycielski steps**

We determine sharp uniform Hall-ratio bounds for one and two ordinary Mycielski steps over three nested classes of nonempty finite simple base graphs. The bound pairs are 5/2 and 11/4 for bipartite bases, 3 and 23/7 when the circular chromatic number is below three, and 3 and 10/3 when the fractional chromatic number is below three. A common projection argument explains the hierarchy: bipartiteness supplies an exact factor two, strict fractional coloring supplies integral slack, and circular coloring excludes the remaining extremal configuration. Explicit bases attain all six bounds; the one-step bipartite result is classical. In the fractional two-step case, equality forces a twenty-vertex induced set of independence number six and a projection onto at most seventeen base vertices with circular chromatic number at least three. A structural witness and an explicit fractional coloring yield ρ(M6)=10/3. Separately, a computer-assisted census finds 1,990 maximizing embedded subsets in M6, forming 199 orbits under its ambient automorphism group D5. The strict fractional hypothesis cannot be extended to equality at three.

## 原创开头和转折

The Mycielski construction raises chromatic number while preserving triangle-freeness. For the Hall ratio, the relevant question is more local: which induced subsets provide the strongest independence obstruction after the construction? We study one and two ordinary steps, asking how the answer depends on the coloring information available for the base graph.

The same projection is useful in all three base classes. Once the distinguished vertices are removed, the remaining layers map to the base, and a coloring of the base bounds their total contribution. What changes between the classes is the information that can be recovered from this bound. The three pairs of sharp constants record that change.

既有v8已经准确列出三类，不应为了制造“before/after”把它说成只有孤立M6数值的论文。建议改进是把表格与投影因果关系更靠近，并在正式正文中继续保留CGL、LPU、CHZ、Vince等原稿来源。

## 证明总览候选

After deleting the distinguished vertices, the four base layers admit a projection to G. Pulling back a fractional coloring bounds the order of every projected induced subset by its independence number times the coloring weight. For bipartite bases, the exact factor two combines with the distinguished-vertex adjacencies. Under χ_f(G)<3, integrality leaves a small exceptional equality pattern; circular windows rule out that pattern when χ_c(G)<3. We then give explicit supports that attain the bounds. Only after the analytic equality restrictions are in place do we enumerate all maximizing subsets of M6.

## 等号与计算必须保留的区分

一般χ_f(G)<3情形，10/3等号迫使order20、α6，含z,z′,w；四层p+r=11,q+t=6；最终original/clone数为(13,6),(14,5),(15,4)，且χ_f(G)≥17/6。这些是必要条件，不是对所有基图的完整等号分类。

M6的1,990个subset分为D5作用下199个embedded orbits，每轨大小10；三个层型对应109、83、7个轨道。这不是199个抽象图同构类型，也不是解析证明枚举了所有基图。可将census作为“分析限制如何使完整有限问题成为可能”的后果；不能让计算输出取代一般上界与达到证明。

## Before/after例子

说明书式示例（本研究构造）：We prove three bounds and enumerate the maximizing subsets of M6.

改为：One projection argument yields different sharp bounds according to the coloring information retained by the base. Its equality restrictions then reduce the maximizing-subset problem in M6 to a complete finite census.

前一句只列任务；后一句解释它们为何属于同一篇数学文章。没有改变定理，也没有将经典one-step结论包装成新结果。
