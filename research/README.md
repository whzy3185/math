# 当前研究入口

本分支 `research/quadratic-gap-upgrade` 继续推进 `C_N(1,s)` 的一般跳长谱构造。
2026-09-06 当前主结果已经从“偶跳长 quadratic gap”扩展并闭合为：

> 对一组 parity-dependent 显式周期符号族，所有整数 `s>=2` 都有
> `Rhat_s<8`，并且
> `s^2(8-Rhat_s) -> pi^2`。

奇偶机制不同：

- 奇 `s`：period-two alternating-flux family，唯一 interior optimizer；
- 偶 `s`：primitive period-`4s` antipodal defect family，存在真实 phase slip，
  但 global localization 证明 phase drift 不改变 leading `pi^2/s^2` 常数。

因此 **jump parameter `s` 的 sharp asymptotic 已全覆盖**。当前主要开放问题已经下移到：
second-order even phase slip、finite-order compatibility、global minimization over all signings、
Lean 完整形式化和文献优先权审计。

## 入口

| 阅读目的 | 文件 |
|---|---|
| all-`s` sharp 主定理 | [ALL_S_UNIFIED_THEOREM](generalization/circulant_1s/quadratic_gap_20260906/ALL_S_UNIFIED_THEOREM.md) |
| odd `s` sharp `pi^2` gap 与唯一相位 | [ODD_JUMP_SHARP_GAP](generalization/circulant_1s/quadratic_gap_20260906/ODD_JUMP_SHARP_GAP.md) |
| even global sharp `pi^2` theorem | [EVEN_GLOBAL_PI2_THEOREM](generalization/circulant_1s/quadratic_gap_20260906/EVEN_GLOBAL_PI2_THEOREM.md) |
| even global phase localization 的显式 lemma | [GLOBAL_PI2_LOCALIZATION_LEMMA](generalization/circulant_1s/quadratic_gap_20260906/GLOBAL_PI2_LOCALIZATION_LEMMA.md) |
| exact `s=10` phase-slip 反例 | [PHASE_SLIP_COUNTEREXAMPLE](generalization/circulant_1s/quadratic_gap_20260906/PHASE_SLIP_COUNTEREXAMPLE.md) |
| odd-order naive one-defect 障碍 | [ODD_ORDER_ONE_DEFECT_OBSTRUCTION](generalization/circulant_1s/quadratic_gap_20260906/ODD_ORDER_ONE_DEFECT_OBSTRUCTION.md) |
| 当前 workstream 总览 | [quadratic-gap workstream](generalization/circulant_1s/quadratic_gap_20260906/README.md) |
| 新论文架构 | [PAPER_ARCHITECTURE](generalization/circulant_1s/quadratic_gap_20260906/PAPER_ARCHITECTURE.md) |
| 数学结论、证明、验证与可复用性 | [成果索引](repository_guide/RESULTS_INDEX.md) |
| 冻结稿、纠错稿与历史分支 | [分支和稿件地图](repository_guide/BRANCH_AND_PAPER_MAP.md) |

## 当前 theorem picture

令 `Rhat_s` 表示当前 parity-dependent 显式周期符号族的 continuous squared Bloch radius，
`ghat_s=8-Rhat_s`。则对所有整数 `s>=2`：

`1/(6s(s+2)) <= ghat_s <= 4 sin^2(pi/(s+2))`，

并且更强地

` s^2 ghat_s -> pi^2. `

奇 `s` 的最优 continuous phase 满足 Chebyshev 方程

` s U_(s-1)(cos(2 theta_s)) = 1 `

并有 `theta_s=pi/(2s)+O(s^-3)`。

偶 `s=2r` 的 global optimizer 不一定在 zero phase；但若
`h_r` 是 global maximizing square-root phase parameter，则

` r^2(2-h_r) -> 0 `，

因此 phase slip 只影响 leading order 以下的项。

## 下一层 conjecture

数值结果指向 even phase-slip 的二阶精确常数：

` r^2 phi_r -> pi/(4 sqrt(2)) `

和

` r^4(e_r-g_(2r)) -> pi^2/32 `。

这两个目前仍是 conjecture，不应写成 theorem。

## 有限环覆盖

- 奇 `s`：period-two word 对所有满足 `2<=s<N/2` 的偶数 `N` 都给出 `rho^2<8`。
- 偶 `s`：当前 antipodal theorem 对 `N=4sL` 给出 `rho^2<8`。
- odd `N`：单一 concentrated parity defect 并不够；`(N,s)=(21,7)` 已有 exact integer Rayleigh obstruction。

所以当前没有闭合的是 **order compatibility**，不是 jump parameter。

## 版本/阶段

- 冻结文章：`paper/jgt-authorial-rewrite`，`6766ecb`。
- 修正结尾：`paper/period8-conclusion-correction`，`2dc5b90`。
- 一般跳长研究基线：`research/circulant-1s-extension`。
- 当前 all-`s` sharp quadratic-gap 主线：`research/quadratic-gap-upgrade`。

冻结正文和旧 `formal/TargetA` kernel 均未改动。

## 证据规则

1. 当前 all-`s` theorem 是显式 parity-dependent family 的 Bloch 谱结论，不是 `m(N,s)` 的全局最小值分类。
2. continuous Bloch edge、finite Fourier grid、Hamilton holonomy 和全部 switching classes 必须区分。
3. `PHASE_SLIP_COUNTEREXAMPLE.md` 是 exact Sturm 证书；二阶 phase-slip 常数目前只是 numerical conjecture。
4. `GLOBAL_PI2_LOCALIZATION_LEMMA.md` 是 even global sharp theorem 的关键解析补强。
5. 新 Lean 文件尚未在本环境中真实编译；未编译形式化不能标成 kernel-checked theorem。
6. “未找到直接先例”只代表有限检索范围，不构成世界首次证明。

历史导航仍见 `repository_guide/`；旧候选状态见 `CONJECTURE_REGISTRY.md`。
