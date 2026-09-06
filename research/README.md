# 当前研究入口

本分支从 `research/circulant-1s-extension` 继续推进 `C_N(1,s)` 的一般偶跳长谱构造。
2026-09-06 新增 quadratic-gap 主线：在不修改冻结 period-eight 稿件和旧 Lean kernel 的前提下，
已把显式 antipodal family 的 Bloch gap 从旧的 `Omega(s^-3)` 提升到 `Theta(s^-2)`，
并证明 phase-zero endpoint 的缩放常数为 `pi^2`；同时用精确 Sturm 计数反驳了旧 Q7
“所有偶 `s` 的最坏相位都在 zero phase”猜想。全局 `s^2(8-R_s)->pi^2` 仍待完成
phase boundary-layer 控制。

## 入口

| 阅读目的 | 文件 |
|---|---|
| 2026-09-06 quadratic gap 新主线、Q7 反例、endpoint `pi^2` 渐近 | [quadratic-gap workstream](generalization/circulant_1s/quadratic_gap_20260906/README.md) |
| 数学结论、证明、验证与可复用性 | [成果索引](repository_guide/RESULTS_INDEX.md) |
| 冻结稿、纠错稿与历史分支 | [分支和稿件地图](repository_guide/BRANCH_AND_PAPER_MAP.md) |
| 判断旧文档是否仍为当前依据 | [过时状态覆盖表](repository_guide/SUPERSESSION_MAP.md) |
| 现稿主要问题、一篇还是两篇 | [初步评估](repository_guide/PAPER_ASSESSMENT.md) |
| 全仓库文件、JSON和文档盘点的真实覆盖 | [覆盖记录](repository_guide/COVERAGE_AND_COMPLETION.md) |
| 一般跳长详细交接 | [情况说明](generalization/circulant_1s/extension_20260905/REPOSITORY_STATUS_20260905.md) |

## 三个版本

- 冻结文章：`paper/jgt-authorial-rewrite`，`6766ecb`。
- 修正结尾的可读文章：
  [`paper/period8-conclusion-correction`](https://github.com/whzy3185/math/tree/paper/period8-conclusion-correction)，
  `2dc5b90`。
- 一般跳长研究基线：
  [`research/circulant-1s-extension`](https://github.com/whzy3185/math/tree/research/circulant-1s-extension)。
- 当前 quadratic-gap 升级：`research/quadratic-gap-upgrade`。

原论文分支、freeze tag与新推广分支中的冻结正文均未改动。请用纠错
分支读新结尾，不要从其他旧稿目录拿同名 `main.tex`。

## 目录保留与用途

| 目录 | 当前用途 |
|---|---|
| `generalization/circulant_1s/quadratic_gap_20260906/` | 当前 quadratic gap、phase slip、endpoint sharp asymptotic 与后续边界层分析 |
| `generalization/circulant_1s/extension_20260905/` | 一般跳长解析结果、旧开放猜想、精确复核基线 |
| `generalization/circulant_1s/task60/` | 已继承的一般模型与alternating谱基础 |
| `paper_strengthening/` | 八周期已完成成果、原稿与正文书目，按冻结处理 |
| `analytic_inventory/`、`proof_closure/` | 历史解析化与证明缺口；不是所有状态都仍为当前 |
| `proofs/`、`discovery/` | 历史接口、分类、低周期等结果；复用前核查量词和证据 |
| `paper/` | 旧稿与旧范围，保留可追溯历史 |
| `scripts/`、`audit/`、`reproducibility/` | 原始验证器与证据边界，不因精确计算就自动成为解析证明 |
| `logs/`、`experiments/` | 大型历史计算记录，本轮未重跑 |
| `related_work/`、`paper_strengthening/reference_library/` | 现有书目、PDF、笔记与访问状态 |
| `repository_guide/` | 导航、全文件清单、状态覆盖和初步评估 |
| `../formal/TargetA/` | 冻结的正 holonomy 八周期比较 Lean kernel |
| `../formal/QuadraticGap/` | 新 quadratic-gap 证明的独立 Lean 形式化轨道 |

## 证据规则

1. 结论按数学对象、量词与证明范围登记，不以文件名“complete”认定完成。
2. 解析证明、有限精确步骤、历史计算辅助、浮点线索、Lean证明分别说明。
3. 全局最小值与指定符号的半径不同；有限环和Bloch谱边不同；两个holonomy
   不能混为一个最优值。当前新结果证明的是显式 antipodal family 的 gap 阶与 endpoint 渐近，
   不是所有 `m(N,s)` 的闭式解。
4. 旧文献的“未找到直接先例”仅在当时检索范围有效，不构成世界首次证明。
5. 不要求用户先懂全部数学才能决策；后续研究应给出可核验的判断与有限
   修订范围，而不是靠持续堆积成果延后投稿。
6. 本轮未对全部历史证明作语义重审；文件清单和JSON解析成功不等于数学正确。

先前README的完整原文保存在
[历史快照](repository_guide/HISTORICAL_RESEARCH_README.md)。原候选编号仍见
[猜想登记表](CONJECTURE_REGISTRY.md)，其历史状态不取代上述当前索引。