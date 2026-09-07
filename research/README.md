# 当前研究入口

本分支 `research/quadratic-gap-upgrade` 已形成一个可作为当前研究终点的 theorem package：

1. **all-`s` periodic/Bloch sharp theory**：对一组 parity-dependent 显式周期符号族，
   所有整数 `s>=2` 都有 `Rhat_s<8`，且
   `s^2(8-Rhat_s)->pi^2`；
2. **finite exact flat theorem**：`m(N,s)=2` 当且仅当 `N=2s+2`，其余情况
   `m(N,s)>=sqrt(5)`；
3. **finite resonance threshold classification**：在整条 `N=3s` 上，
   \[
   m(3s,s)<\sqrt8
   \iff s\text{ 为偶数，或 }s\in\{3,5\},
   \]
   且所有奇 `s>=7` 满足统一 all-signing 下界
   `m(3s,s)^2>=8+1/70`。

当前总入口是
[`FINAL_THEOREM_PACKAGE_20260907.md`](generalization/circulant_1s/quadratic_gap_20260906/FINAL_THEOREM_PACKAGE_20260907.md)。

## Bloch 主结果

奇偶机制不同：

- 奇 `s`：period-two alternating-flux family，唯一 interior optimizer；
- 偶 `s`：primitive period-`4s` antipodal defect family，存在真实 phase slip。

对统一显式族，

`1/(6s(s+2)) <= 8-Rhat_s <= 4 sin^2(pi/(s+2))`

并且

` s^2(8-Rhat_s) -> pi^2. `

偶 `s=2r` 的经 hostile-audit 后 headline phase-slip 结果为

`r^2 phi_r -> pi/(4 sqrt(2))`

以及

`r^4(e_r-g_(2r)) -> pi^2/32`。

`EVEN_THIRD_ORDER_PHASE_SLIP_REFINEMENT.md` 中更高的 `r^-3/r^-5` 修正暂时不放入
最终 headline theorem，等待独立 uniform-remainder audit。

## finite-order 主结果

令 `m(N,s)` 为固定底图 `C_N(1,s)` 上对所有 edge signings 取最小 spectral radius。

### Flat line

`m(N,s)=2` iff `N=2s+2`; otherwise `m(N,s)>=sqrt(5)`.

### Resonance line `N=3s`

完整 `sqrt(8)` threshold classification 为

`m(3s,s)<sqrt(8)` iff `s` even or `s in {3,5}`.

更细地：

- `s=2`: `m(6,2)=2`；
- `s=3,5`: exact Sylvester certificates 给出 `sqrt(5)<=m<sqrt(8)`；
- even `s>=4`: antiperiodic alternating signing 给出 `sqrt(5)<=m<sqrt(8)`；
- odd `s>=7`: 每个 signing 都满足 `m(3s,s)^2>=8+1/70`。

最后一项证明结构：

- `(21,7)`：49,940 个 cyclic `Q` necklaces、199,760 个 Hamilton-gauge
  representatives 的 exact integer certificate；最弱生成 witness 余量 `18/131`；
- `(27,9)`：exact prefix pruning 覆盖全部 `2*8^9=268,435,456` 个 gauge
  representatives，只需 17,024 个最终 cyclic checks；
- `s>=11`：9-column signed-triangle finite-state lemma 强迫低谱状态在 bulk 中
  `B_(j+1)=-B_j`，而 helical seam 会要求 `B` 与 `-B` 正交相似；
  `tr(B^3)=+/-6` 排除这一可能。

## 2026-09-07 独立复跑

当前分析环境已重新复现：

- 9-column survivor counts `8,56,152,440,488,1016,656,1064,128`，且最终
  128 个 survivor 全部满足 forced middle alternation；
- `C_27(1,9)` 的 17,024 个最终 exact cyclic checks；
- `C_21(1,7)` 的全部 199,760 个 Hamilton-gauge representatives；
- `C_9(1,3)` 与 `C_15(1,5)` 两个短正例的所有正 leading principal minors。

## 当前入口

| 阅读目的 | 文件 |
|---|---|
| 最终 theorem package | [FINAL_THEOREM_PACKAGE_20260907](generalization/circulant_1s/quadratic_gap_20260906/FINAL_THEOREM_PACKAGE_20260907.md) |
| `N=3s` iff 分类 | [N3S_THRESHOLD_CLASSIFICATION](generalization/circulant_1s/quadratic_gap_20260906/N3S_THRESHOLD_CLASSIFICATION.md) |
| 当前总览 | [workstream README](generalization/circulant_1s/quadratic_gap_20260906/README.md) |
| theorem / evidence 索引 | [RESULTS_INDEX](generalization/circulant_1s/quadratic_gap_20260906/RESULTS_INDEX.md) |
| all-`s` sharp Bloch theorem | [ALL_S_UNIFIED_THEOREM](generalization/circulant_1s/quadratic_gap_20260906/ALL_S_UNIFIED_THEOREM.md) |
| odd `s` exact/sharp theory | [ODD_JUMP_SHARP_GAP](generalization/circulant_1s/quadratic_gap_20260906/ODD_JUMP_SHARP_GAP.md) |
| even global `pi^2` theorem | [EVEN_GLOBAL_PI2_THEOREM](generalization/circulant_1s/quadratic_gap_20260906/EVEN_GLOBAL_PI2_THEOREM.md) |
| even second-order phase slip | [EVEN_SECOND_ORDER_PHASE_SLIP_THEOREM](generalization/circulant_1s/quadratic_gap_20260906/EVEN_SECOND_ORDER_PHASE_SLIP_THEOREM.md) |
| exact `s=10` phase-zero failure | [PHASE_SLIP_COUNTEREXAMPLE](generalization/circulant_1s/quadratic_gap_20260906/PHASE_SLIP_COUNTEREXAMPLE.md) |
| infinite odd `N=3s` obstruction | [N3S_GLOBAL_OBSTRUCTION](generalization/circulant_1s/quadratic_gap_20260906/N3S_GLOBAL_OBSTRUCTION.md) |
| short `N=3s` exact positive verifier | [verify_n3s_short_threshold.py](generalization/circulant_1s/quadratic_gap_20260906/verify_n3s_short_threshold.py) |
| 9-column local rule verifier | [verify_triangle_strip_local_rule.py](generalization/circulant_1s/quadratic_gap_20260906/verify_triangle_strip_local_rule.py) |
| 最新文献边界 | [LITERATURE_UPDATE_20260907](generalization/circulant_1s/quadratic_gap_20260906/LITERATURE_UPDATE_20260907.md) |

## 仍未声称解决的更大问题

当前 theorem package **不是** 任意 `(N,s)` 的 `m(N,s)` 闭式分类。仍开放：

1. 求 `m(3s,s)` 在各 regime 内的真正值或大 `s` 渐近；
2. 分类其他 chord-cycle length `L=N/gcd(N,s)`，特别是 `L=5,7,9`；
3. 用手工矩阵不等式替代 9-column exact finite-state lemma；
4. 去掉 even `s` 下 `4s | N` 的有限阶限制；
5. 完成 Lean 形式化并真实 `lake build`；
6. 扩展 magnetic/flux-phase / block-Jacobi 文献审计后再决定 novelty 措辞。

## 证据边界

- Bloch 主定理与 second-order phase slip：解析证明正文；
- `s=3,5` 正例：exact Sylvester positive-definiteness certificates；
- `(21,7)`、`(27,9)` 与 9-column 状态规则：exact finite computer-assisted
  certificates，浮点只负责提出整数 witness，不决定真假；
- `N=3s` odd `s>=7`：解析结构证明 + exact finite local lemma/base cases；
- `formal/QuadraticGap/`：已有 Lean source，但当前环境没有真实 Lean/Lake 编译记录，
  不能标为 kernel-checked；
- 文献“未找到直接先例”不是 priority certificate。

冻结 period-eight 正文和旧 `formal/TargetA` kernel 均未修改。
