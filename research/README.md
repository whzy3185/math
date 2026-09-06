# 当前研究入口

本分支从 `research/circulant-1s-extension` 继续推进 `C_N(1,s)` 的一般跳长谱构造。
2026-09-06 的 quadratic-gap 主线现已从“所有偶 `s`”继续扩展到**所有整数跳长 `s>=2`**：

- 偶 `s`：使用 primitive period-`4s` antipodal defect family；
- 奇 `s`：使用 period-two alternating-flux family。

对这组 parity-dependent 显式构造，已经证明统一的

`8-Rhat_s = Theta(s^-2)`，

并且奇数子序列具有 sharp 常数

`s^2(8-Rhat_s) -> pi^2`。

偶数子序列的 phase-zero endpoint 也具有 `pi^2` 常数，但精确 Sturm 证书表明从 `s=10`
开始不能把全局最坏相位简单固定在 zero phase；当前剩余的 sharp 问题是证明偶数 phase slip
只影响次阶项。

## 入口

| 阅读目的 | 文件 |
|---|---|
| all-`s` 统一主定理 | [ALL_S_UNIFIED_THEOREM](generalization/circulant_1s/quadratic_gap_20260906/ALL_S_UNIFIED_THEOREM.md) |
| odd `s` sharp `pi^2` gap、唯一最优相位 | [ODD_JUMP_SHARP_GAP](generalization/circulant_1s/quadratic_gap_20260906/ODD_JUMP_SHARP_GAP.md) |
| even quadratic gap、phase slip、endpoint `pi^2` 与当前路线 | [quadratic-gap workstream](generalization/circulant_1s/quadratic_gap_20260906/README.md) |
| 新论文架构 | [PAPER_ARCHITECTURE](generalization/circulant_1s/quadratic_gap_20260906/PAPER_ARCHITECTURE.md) |
| 数学结论、证明、验证与可复用性 | [成果索引](repository_guide/RESULTS_INDEX.md) |
| 冻结稿、纠错稿与历史分支 | [分支和稿件地图](repository_guide/BRANCH_AND_PAPER_MAP.md) |
| 判断旧文档是否仍为当前依据 | [过时状态覆盖表](repository_guide/SUPERSESSION_MAP.md) |
| 现稿主要问题、一篇还是两篇 | [初步评估](repository_guide/PAPER_ASSESSMENT.md) |
| 全仓库文件、JSON和文档盘点的真实覆盖 | [覆盖记录](repository_guide/COVERAGE_AND_COMPLETION.md) |
| 一般跳长详细交接 | [情况说明](generalization/circulant_1s/extension_20260905/REPOSITORY_STATUS_20260905.md) |

## 当前 theorem picture

令 `Rhat_s` 表示当前 parity-dependent 显式周期符号族的 continuous squared Bloch radius，
`ghat_s=8-Rhat_s`。

对所有整数 `s>=2`：

`1/(6s(s+2)) <= ghat_s <= 4 sin^2(pi/(s+2))`，

因此

`ghat_s = Theta(s^-2)`。

奇 `s` 进一步有

`4 sin^2(pi/(2s)-pi^2/(4s^3)) <= ghat_s <= 4 sin^2(pi/(2s))`

以及

`s^2 ghat_s -> pi^2`。

偶 `s` 当前有

`1/6 <= liminf s^2 ghat_s <= limsup s^2 ghat_s <= pi^2`，

且 endpoint 单独满足 sharp `pi^2` limit。剩余问题是 even small-phase two-mode coupling。

## 有限环覆盖

- 奇 `s`：period-two word 对每个满足 `2<=s<N/2` 的偶数 `N` 都可用，且两种 Hamilton holonomy
  的有限谱半径平方都严格小于 `8`。
- 偶 `s`：当前 antipodal theorem 对 `N=4sL` 给出两种 holonomy 都严格小于 `8`。

所以跳长参数 `s` 已经全覆盖；尚未全覆盖的是 finite-order compatibility：odd `N` 以及偶 `s`
时 `4s` 不整除 `N` 的情形仍是后续问题。

## 四个版本/阶段

- 冻结文章：`paper/jgt-authorial-rewrite`，`6766ecb`。
- 修正结尾的可读文章：
  [`paper/period8-conclusion-correction`](https://github.com/whzy3185/math/tree/paper/period8-conclusion-correction)，
  `2dc5b90`。
- 一般跳长研究基线：
  [`research/circulant-1s-extension`](https://github.com/whzy3185/math/tree/research/circulant-1s-extension)。
- 当前 all-`s` quadratic-gap 升级：`research/quadratic-gap-upgrade`。

原论文分支、freeze tag 与旧 Lean kernel 均未改动。

## 目录保留与用途

| 目录 | 当前用途 |
|---|---|
| `generalization/circulant_1s/quadratic_gap_20260906/` | 当前 all-`s` quadratic gap、odd sharp model、even phase slip 与后续边界层分析 |
| `generalization/circulant_1s/extension_20260905/` | 一般偶跳长解析结果、旧开放猜想、精确复核基线 |
| `generalization/circulant_1s/task60/` | 一般 `C_N(1,s)` algebra 与 alternating 谱基础，尤其 odd parity 基线 |
| `paper_strengthening/` | 八周期已完成成果、原稿与正文书目，按冻结处理 |
| `analytic_inventory/`、`proof_closure/` | 历史解析化与证明缺口；不是所有状态都仍为当前 |
| `proofs/`、`discovery/` | 历史接口、分类、低周期等结果；复用前核查量词和证据 |
| `paper/` | 旧稿与旧范围，保留可追溯历史 |
| `scripts/`、`audit/`、`reproducibility/` | 原始验证器与证据边界，不因精确计算就自动成为解析证明 |
| `logs/`、`experiments/` | 大型历史计算记录 |
| `related_work/`、`paper_strengthening/reference_library/` | 现有书目、PDF、笔记与访问状态 |
| `repository_guide/` | 导航、全文件清单、状态覆盖和初步评估 |
| `../formal/TargetA/` | 冻结的正 holonomy 八周期比较 Lean kernel |
| `../formal/QuadraticGap/` | 新 all-`s` / quadratic-gap 证明的独立 Lean 形式化轨道 |

## 证据规则

1. 结论按数学对象、量词与证明范围登记，不以文件名“complete”认定完成。
2. 解析证明、有限精确步骤、历史计算辅助、浮点线索、Lean证明分别说明。
3. 当前 all-`s` theorem 是显式 parity-dependent family 的谱结论，不是 `m(N,s)` 全局最小值闭式分类。
4. finite Bloch grid、continuous Bloch edge、Hamilton holonomy 与所有 switching classes 必须区分。
5. 旧文献的“未找到直接先例”仅在当时检索范围有效，不构成世界首次证明。
6. 新 Lean 文件尚需真实 toolchain 编译核验；未编译的形式化草案不能标记为 kernel-checked theorem。

先前 README 的完整原文保存在
[历史快照](repository_guide/HISTORICAL_RESEARCH_README.md)。原候选编号仍见
[猜想登记表](CONJECTURE_REGISTRY.md)，其历史状态不取代上述当前索引。
