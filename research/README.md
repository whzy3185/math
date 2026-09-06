# 当前研究入口

本分支 `research/quadratic-gap-upgrade` 当前已经形成两条互补主线：

1. **all-`s` periodic/Bloch sharp theory**：对一组 parity-dependent 显式周期符号族，
   所有整数 `s>=2` 都有 `Rhat_s<8`，且
   `s^2(8-Rhat_s)->pi^2`；
2. **finite arithmetic obstruction**：对所有奇 `s>=7`，任意 signing 的
   `C_(3s)(1,s)` 都满足
   `rho^2>=8+1/70`。

这说明“每个 jump 都存在 sub-`sqrt(8)` 周期 Bloch 构造”与“每个有限阶都能
实现 sub-`sqrt(8)`”是两件不同的事；`N=3s` 是已证明的无限算术障碍族。

## Bloch 主结果

奇偶机制不同：

- 奇 `s`：period-two alternating-flux family，唯一 interior optimizer；
- 偶 `s`：primitive period-`4s` antipodal defect family，存在真实 phase slip。

对统一显式族，

`1/(6s(s+2)) <= 8-Rhat_s <= 4 sin^2(pi/(s+2))`

并且

` s^2(8-Rhat_s) -> pi^2. `

偶 `s=2r` 的 phase slip 已推进到：

`phi_r = pi/(4 sqrt(2) r^2) - 3pi/(16 r^3) + o(r^-3)`

以及

`e_r-g_(2r) = pi^2/(32 r^4) - 3pi^2/(32 sqrt(2) r^5) + o(r^-5)`。

## finite-order 主结果

令 `m(N,s)` 为固定底图 `C_N(1,s)` 上对所有 edge signings 取最小 spectral radius。
当前已经证明

`m(3s,s)^2 >= 8 + 1/70`  对所有奇 `s>=7`。

证明结构：

- `(21,7)`：49,940 个 cyclic `Q` necklaces、199,760 个 Hamilton-gauge
  representatives 的 exact integer certificate；实际得到更强 `18/131` 余量；
- `(27,9)`：exact prefix pruning 覆盖全部 `2*8^9=268,435,456` 个 gauge
  representatives，只需 17,024 个最终 cyclic checks；
- `s>=11`：9-column signed-triangle finite-state lemma 强迫低谱状态在 bulk 中
  `B_(j+1)=-B_j`，而 helical seam 会要求 `B` 与 `-B` 正交相似；
  `tr(B^3)=+/-6` 排除这一可能。

因此 `N=3s` 的 obstruction 是 **all-signing theorem**，不是某个 defect Ansatz
失败。

## 当前入口

| 阅读目的 | 文件 |
|---|---|
| 当前总览 | [workstream README](generalization/circulant_1s/quadratic_gap_20260906/README.md) |
| 当前 theorem / evidence 索引 | [RESULTS_INDEX](generalization/circulant_1s/quadratic_gap_20260906/RESULTS_INDEX.md) |
| all-`s` sharp Bloch theorem | [ALL_S_UNIFIED_THEOREM](generalization/circulant_1s/quadratic_gap_20260906/ALL_S_UNIFIED_THEOREM.md) |
| odd `s` exact/sharp theory | [ODD_JUMP_SHARP_GAP](generalization/circulant_1s/quadratic_gap_20260906/ODD_JUMP_SHARP_GAP.md) |
| even global `pi^2` theorem | [EVEN_GLOBAL_PI2_THEOREM](generalization/circulant_1s/quadratic_gap_20260906/EVEN_GLOBAL_PI2_THEOREM.md) |
| even second-order phase slip | [EVEN_SECOND_ORDER_PHASE_SLIP_THEOREM](generalization/circulant_1s/quadratic_gap_20260906/EVEN_SECOND_ORDER_PHASE_SLIP_THEOREM.md) |
| even next correction | [EVEN_THIRD_ORDER_PHASE_SLIP_REFINEMENT](generalization/circulant_1s/quadratic_gap_20260906/EVEN_THIRD_ORDER_PHASE_SLIP_REFINEMENT.md) |
| exact `s=10` phase-zero failure | [PHASE_SLIP_COUNTEREXAMPLE](generalization/circulant_1s/quadratic_gap_20260906/PHASE_SLIP_COUNTEREXAMPLE.md) |
| infinite `N=3s` all-signing obstruction | [N3S_GLOBAL_OBSTRUCTION](generalization/circulant_1s/quadratic_gap_20260906/N3S_GLOBAL_OBSTRUCTION.md) |
| exact `(21,7)` theorem | [C21_S7_GLOBAL_OBSTRUCTION](generalization/circulant_1s/quadratic_gap_20260906/C21_S7_GLOBAL_OBSTRUCTION.md) |
| exact `(27,9)` theorem | [C27_S9_GLOBAL_OBSTRUCTION](generalization/circulant_1s/quadratic_gap_20260906/C27_S9_GLOBAL_OBSTRUCTION.md) |
| 9-column local rule verifier | [verify_triangle_strip_local_rule.py](generalization/circulant_1s/quadratic_gap_20260906/verify_triangle_strip_local_rule.py) |
| 新论文架构 | [PAPER_ARCHITECTURE](generalization/circulant_1s/quadratic_gap_20260906/PAPER_ARCHITECTURE.md) |
| 最新文献边界 | [LITERATURE_UPDATE_20260906](generalization/circulant_1s/quadratic_gap_20260906/LITERATURE_UPDATE_20260906.md) |
| 2026-09-05 历史仓库索引 | [旧成果索引](repository_guide/RESULTS_INDEX.md) |

## 当前开放问题

1. 求 `m(3s,s)` 的真正值或大 `s` 渐近，而不只是统一下界；
2. 分类其他 chord-cycle length `L=N/gcd(N,s)`，特别是 `L=5,7,9`；
3. 尝试用手工矩阵不等式替代 9-column exact finite-state lemma；
4. 继续去掉 even `s` 下 `4s | N` 的有限阶限制；
5. 完成 Lean 形式化并真实 `lake build`；
6. 扩展 magnetic/flux-phase / block-Jacobi 文献审计后再决定 novelty 措辞。

## 证据边界

- Bloch 主定理与 phase-slip 渐近：解析证明正文；
- `(21,7)`、`(27,9)` 与 9-column 状态规则：exact finite computer-assisted
  certificate，浮点只负责提出整数 witness，不决定真假；
- `N=3s` 无限族：解析结构证明 + exact finite local lemma/base cases；
- `formal/QuadraticGap/`：已有 Lean source，但当前环境没有真实 Lean/Lake 编译记录，
  不能标为 kernel-checked；
- 文献“未找到直接先例”不是 priority certificate。

冻结 period-eight 正文和旧 `formal/TargetA` kernel 均未修改。
