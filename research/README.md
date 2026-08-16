# 数学猜想反例研究项目

本目录用于长期、可复核地研究公开数学猜想的潜在反例。项目按以下研究链推进：

> 文献挖掘 → 猜想筛选 → 形式化 → 已知结果复核 → 基线复现 → 搜索器设计 → 反例搜索 → 精确验证 → 最小化 → 结构分析 → 无穷族 → 修正定理 → 文献查重 → 论文撰写 → 独立审计

## 当前阶段

- 阶段：Target A——**PAPER_PACKAGE_READY**；进入 Reviewer Zero 与定理依赖整理，尚未开始 manuscript
- 状态：**DISPROVED**；已证明 period-8 无限反例族，覆盖所有 `8|n, n≥32`
- 首个且最小的反例阶数：`n=32`
- 最小性状态：**SMALLEST_COUNTEREXAMPLE_VERIFIED**；有限穷举精确排除所有偶数 `8≤n≤30`，`n=32` 有显式精确证书
- witness 审计：**N32_WITNESS_INDEPENDENTLY_RECONSTRUCTED**；第二套实现从 flux 定义在非平凡 gauge 中重构并证明 switching equivalence
- Floquet 审计：**PERIOD8_FLOQUET_DETERMINANT_INDEPENDENTLY_AUDITED**；从有限矩阵、twisted Bloch 分解和双 determinant 路线独立重得 `P(y,c)`
- 无限族审计：**PERIOD8_INFINITE_FAMILY_INDEPENDENTLY_AUDITED**；正系数 uniform certificate、代数 threshold isolation 与双 holonomy 全部独立 PASS
- sharp 常数：**PERIOD8_SHARP_SPECTRAL_CONSTANT_PROVED**；`rho_*^2=4+sqrt(10+2sqrt(5))`，唯一 band edge 为 `z=1`
- period-8 分类：**PERIOD8_UNIQUE_OPTIMUM_AND_SECOND_BEST_PROVED**；128 个合法 flux vectors 的 18 个 `D_8` orbits 已完整分类，target 是唯一最优相
- 唯一第二名：全 unbalanced phase `Q=(-)^8`，`rho^2=8`；其余 16 类均以 exact Rayleigh certificate 证明严格大于 8
- 结构机制：**PERIOD8_STRUCTURAL_MECHANISM_PROVED**；`R(Q)<8` 当且仅当两个 positive-flux defects 对置，`R(Q)=8` 当且仅当 `Q=(-)^8`
- closed-walk/chiral：`M_2=160+16d`、`M_3=944+168d+96a+48b`；target 具有规范化 anti-period-4 chiral involution 和 `4+4` block reduction
- 一般周期 closed-walk：**GENERAL_PERIOD_CLOSED_WALK_OBSTRUCTIONS_PROVED**；对任意 `p>=1`，`M_1=4p`、`M_2=20p+16d`、`M_3=118p+168d+96a+48b`
- 一般周期 8-barrier 必要条件：`R(Q)<=8` 推出 `d<=3p/4` 且 `40d+96a+48b<=42p`；不声称充分性或全周期最优性
- 低周期前沿：**PERIOD_LE16_UNIQUE_PRIMITIVE_OPTIMUM_PROVED**；`p<=16` 的 2626 个 legal-Q/dihedral orbits 已由显式枚举与 Burnside 双路线核对，所有 2624 个非 target 表示均有 exact strict certificate
- 有界唯一性：primitive `tau` period 不超过 16 时，period-8 target 在 translation/reflection/global-negation/cell-repetition 等价下唯一最优；`p=16` 的 tie 是同一相位的重复胞元
- 低周期结构压缩：**LOW_PERIOD_STRUCTURAL_FRONTIER_PROVED**；2611 类由统一 `F_1,...,F_64` closed-walk hierarchy 排除，8 个全负表示由一个 cancellation lemma 处理，仅保留 5 个 residual endpoint certificates
- novelty/priority：**TARGET_A_NOVELTY_PRIORITY_AUDIT_PASS**；截至 2026-08-16，记录的 135 条 public-source queries 未发现 direct prior；N6 为 `CLOSE_PRIOR_FOUND`，N8/N9/N10 为 `RELATED_METHOD_ONLY`，其余 N1–N5/N7/N11 为 `NO_DIRECT_PUBLIC_PRIOR_FOUND`
- priority 边界：该结论受 indexing delay、Google Scholar 不可访问、Semantic Scholar/GitHub API 限流及非公开工作限制；项目自身 public GitHub disclosure 单列为 provenance，不计 independent prior
- 慢复现：**TARGET_A_FULL_SLOW_REPRODUCTION_PASS**；`n=24,26,28,30` 已从搜索层 fresh regeneration，四条最终 checkpoint chain 与历史结果逐项一致，committed replay 和三个默认跳过的 generator audits 均 PASS，mismatch 0
- 有限尺寸：`alpha=+1` 对每个 `n=8L` 精确达到 `rho_*`；`alpha=-1` 严格低于并收敛到 `rho_*`
- 下一关卡：Reviewer Zero、theorem dependency graph、proof compression 与 notation normalization；完成这些预审整理后才评估 manuscript drafting
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
| `reproducibility/` | 长实验复现摘要、运行环境、命令与外部证据哈希 |

## 核心记录

- [`CONJECTURE_REGISTRY.md`](CONJECTURE_REGISTRY.md)：所有候选猜想的统一登记表。
- [`RESEARCH_LOG.md`](RESEARCH_LOG.md)：按时间追加的研究活动日志。

每次研究开始前先读取登记表与日志；研究结束后必须追加日志，并同步更新相关候选状态。
