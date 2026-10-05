# S3：证明路线要解释因果，最优性必须拆成具体命题

Chen, Rong, Xu, *Optimal stability results on color-biased Hamilton cycles*.

- 精读版本：[arXiv:2507.17739v2](https://arxiv.org/pdf/2507.17739v2)，2025-07-29，14 页
- arXiv DOI：[10.48550/arXiv.2507.17739](https://doi.org/10.48550/arXiv.2507.17739)
- 截至研究日：本次未核实期刊DOI；不是断言没有发表
- 本次重点：pp.1–7,12–13；Theorems1.2–1.3、§2.1、Proposition2.3、§3

## 源文叙事地图（限量概述）

Title: optimal stability. Abstract: benchmark, lower stability threshold, qualified sharpness, mechanism. Prior work: color-bias existence thresholds and extremal constructions (§1). Gap: structural stability below that threshold. Obstruction: local bad bowties can change cycle color counts. Theorems1.2–1.3 separate the three-color configuration. Architecture: many disjoint obstructions force discrepancy; remove a small set; classify remaining local types; assemble the global partition (§2.1). Sharpness: the leading minimum-degree threshold and the additive order are different assertions; the additive example addresses two colors (pp.4–5). Limits and closing: necessity for more colors and a resilience formulation remain questions (§3). Closeness uses the paper's matching-based definitions, not an interchangeable edit metric.

## 对 C029 的原创分析

“第四节建立递推、第五节给估计、第六节作拼接”只是目录。读者真正需要的是每一步为什么不可缺：内部长度被替换成边界响应；收缩让响应靠近共同模型；共同模型正定但仍不能直接推出拼接正定；二关联估计最终控制相互作用。这四个箭头就是数学情节。

这里的结构与源文不同：C029不靠删除少量坏顶点，而是对完整矩阵做合同消元；也没有把图修复成极值图。因此不能将这条谱上界叫作通常意义下的“稳定性定理”。可以说已证明的界不要求等长，或者界在规定不等长拼接下统一成立；这两句话已经足够。

对domination v6，“匹配阶的稳定性尺度”必须连同参数范围出现：第一边界下界为偶数γ及指定t；第二边界为两种γ奇偶、指定偶数t，并且距离要对整个等号族最小化。上界中的12与20不是最优常数。对C029同样不能因存在一个小数上界，就在标题中加入“sharp”。

## 为何是数学文章范例

它在证明之前说明局部障碍如何迫使全局后果，使读者知道后续引理为什么有用。数学美感来自可验证的因果和明确的反例边界；“optimal”这个词本身不是美感的来源。
