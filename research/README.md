# 数学猜想反例研究项目

本目录用于长期、可复核地研究公开数学猜想的潜在反例。项目按以下研究链推进：

> 文献挖掘 → 猜想筛选 → 形式化 → 已知结果复核 → 基线复现 → 搜索器设计 → 反例搜索 → 精确验证 → 最小化 → 结构分析 → 无穷族 → 修正定理 → 文献查重 → 论文撰写 → 独立审计

## 当前阶段

- 阶段：Target A——signed circulant 反例审计与论文整理
- 状态：**DISPROVED**；已证明 period-8 无限反例族，覆盖所有 `8|n, n≥32`
- 首个显式见证：`n=32`；有限验证已完整覆盖所有偶数 `8≤n≤30`
- 最小性状态：**FINITE_RANGE_COMPLETE_THROUGH_N30**；尚未组装最小反例证书
- 下一关卡：Task 36A 汇编并独立审计最小反例证书；不新增谱搜索
- 研究对象：C029 signed circulant global optimizer conjecture

## 优先研究范围

优先考虑 graph theory、combinatorics、algebraic combinatorics、discrete mathematics、matrix theory、polynomial theory、computational algebra、elementary/computational number theory 与 finite structures。

优先关注 arXiv 分类：`math.CO`、`math.AC`、`math.GR`、`math.RA`、`math.NT`、`math.MG`、`math.LA`；必要时可扩展到其他数学方向。

## 证据等级

所有结果必须明确标记为以下四种状态之一，禁止跨级表述：

1. **Observed**：程序或人工探索观察到现象。
2. **Verified**：具体对象已通过精确计算验证。
3. **Proved**：一般数学命题已有严格证明。
4. **Published/Established**：可靠公开文献已经建立该结果。

## 强制研究规则

1. “猜想仍然开放”的判断必须通过最新公开资料检索，并追踪原始论文、正式期刊版本、后续引用及作者后续工作；不得只依赖摘要或二手网页。
2. 每个猜想必须保存原始出处、精确定义、原猜想原文、已证明特殊情形、已计算验证范围、已知失败范围与最新研究状态。
3. 数值实验只用于发现候选反例；浮点结果不能单独构成反例证明。
4. 最终验证优先采用整数或有理数运算、符号计算、精确组合枚举与可复核证明。
5. 随机算法必须保存算法、参数和随机种子。
6. 计算机穷举必须保存搜索空间、剪枝条件、程序版本与 Git commit、输入、输出、校验和及完整日志。
7. 已解决的猜想应立即记录并停止重复研究；成本过高的方向应记录原因并降低优先级。
8. “最小反例”必须由完整搜索或数学证明支撑；否则只能称为“在已说明搜索范围内找到的最小反例”。
9. “无穷反例族”必须有一般证明，有限计算不能替代该证明。
10. 所有 AI 生成的证明、代码结论与文献判断必须独立复核。
11. 禁止为了形成论文而夸大结果；不确定的状态必须明确标记。

## 目录职责

| 路径 | 用途 |
|---|---|
| `conjectures/` | 精确定义、形式化规格与目标说明 |
| `literature/` | 原始文献、状态复核与新颖性审计 |
| `candidates/` | 候选评分、排序与最终目标选择 |
| `experiments/` | 复现实验、搜索计划与实验报告 |
| `counterexamples/` | 候选反例、精确证书与最小化记录 |
| `proofs/` | 失败机制、无穷族、修正命题与证明草稿 |
| `scripts/` | 生成器、验证器与搜索程序 |
| `notebooks/` | 探索性分析；不可作为最终证明的唯一载体 |
| `logs/` | 完整运行日志、环境信息与校验和 |
| `paper/` | 论文提纲、正文、参考文献与 claim-source 映射 |
| `audit/` | 独立计算、证明审计、最小性证书与模拟审稿 |

## 核心记录

- [`CONJECTURE_REGISTRY.md`](CONJECTURE_REGISTRY.md)：所有候选猜想的统一登记表。
- [`RESEARCH_LOG.md`](RESEARCH_LOG.md)：按时间追加的研究活动日志。

每次研究开始前先读取登记表与日志；研究结束后必须追加日志，并同步更新相关候选状态。
