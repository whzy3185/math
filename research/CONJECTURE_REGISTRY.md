# Conjecture Registry

本登记表是项目中所有候选猜想的唯一状态索引。尚未完成最新文献复核的候选必须标记为 `UNVERIFIED OPEN STATUS`，不得直接写成“open”。

## 状态词汇

- `UNSCREENED`：已收集但尚未初筛。
- `UNVERIFIED OPEN STATUS`：疑似开放，但尚无充分证据。
- `OPEN—EVIDENCE AUDITED`：截至登记日期，已有充分公开证据支持其仍开放。
- `SOLVED`：已有证明。
- `DISPROVED`：已有反例或反证。
- `STATUS UNCLEAR`：资料冲突或无法充分确认。
- `PAUSED`：因成本、价值或其他明确原因暂停。
- `ACTIVE` / `SECONDARY` / `BACKLOG`：目标选定后的研究优先级。
- `MINIMAL-COUNTEREXAMPLE STUDIED`：已有公开工作专门研究最小反例或最小见证。
- `LOW-VALUE/BROAD`：问题过宽、非单一命题或当前文献价值不足以优先攻击。

## Registry

| ID | Field | Conjecture | Source | Year | Current status | Object type | Parameters | Verification complexity | Searchability | Known verified range | Potential attack surface | Score | Decision | Notes |
|---|---|---|---|---:|---|---|---|---|---|---|---|---:|---|---|
| C001 | Graph theory | Mixed Moore parameter existence | S01 | 2026 | LOW-VALUE/BROAD | mixed graph | r,z,k,δ | medium | high | not reported | SAT, enumeration | — | BACKLOG | Prompt 2: F |
| C002 | Graph theory | Diameter-2 almost mixed Moore uniqueness | S01 | 2026 | OPEN—EVIDENCE AUDITED | mixed graph | r,z | medium | high | one known graph | canonical enumeration | — | ELIGIBLE | A |
| C003 | Graph theory | Defect lower bound growing with diameter | S01 | 2026 | LOW-VALUE/BROAD | mixed graph | k,δ | high | medium | special family only | construction | — | BACKLOG | F |
| C004 | Graph theory | Defect-two total regularity | S01 | 2026 | OPEN—EVIDENCE AUDITED | mixed graph | r,z,k | medium | high | not reported | SAT, degree defects | — | ELIGIBLE | A |
| C005 | Graph theory | Existence classification of defect-two graphs | S01 | 2026 | LOW-VALUE/BROAD | mixed graph | r,z,k | high | medium | not reported | fixed-parameter splits | — | BACKLOG | F |
| C006 | Graph theory | Effect of digons on defect-two solutions | S01 | 2026 | LOW-VALUE/BROAD | mixed graph | r,z,k | medium | high | partial constructions | digon mutation | — | BACKLOG | F |
| C007 | Combinatorics | Pattern-avoiding derangement/desarrangement classification | S02 | 2026 | LOW-VALUE/BROAD | permutation | Π,n | medium | high | 3-pattern cases | exact enumeration | — | BACKLOG | F |
| C008 | Combinatorics | fix/pix equidistribution classification | S02 | 2026 | LOW-VALUE/BROAD | permutation | Π,n | medium | high | 3-pattern cases | exact enumeration | — | BACKLOG | F |
| C009 | Graph theory | Odd-cycle span defect exponent | S03 | 2026 | OPEN—EVIDENCE AUDITED | graph | N | high | medium | upper/lower bounds | extremal construction | — | ELIGIBLE | A |
| C010 | Algebraic combinatorics | Aldous-property Cayley graph classification | S04 | 2026 | UNVERIFIED OPEN STATUS | Cayley graph | n,generators | high | medium | normal cases | conjugacy reduction | — | HOLD | B |
| C011 | Rigidity | Dress clique-value conjecture | S05 | 2026 | OPEN—EVIDENCE AUDITED | rigidity matroid | graph | high | medium | cofactor analogue | exact rank | — | ELIGIBLE | A |
| C012 | Rigidity | Whiteley R3/cofactor equality | S05 | 2026 | OPEN—EVIDENCE AUDITED | matroid | n | very high | medium | equivalent to C011 | rational rank | — | ELIGIBLE | A |
| C013 | Rigidity | Body-pin partition characterization | S05 | 2026 | OPEN—EVIDENCE AUDITED | multigraph/framework | H,partitions | high | high | cofactor version | ILP, partitions | — | ELIGIBLE | A |
| C014 | Rigidity | 6-connected K4-covered rigidity | S05 | 2026 | OPEN—EVIDENCE AUDITED | graph | n | high | high | edge-transitive | boundary transfer | — | ELIGIBLE | A |
| C015 | Rigidity | 6-connected zeolite global rigidity | S05 | 2026 | OPEN—EVIDENCE AUDITED | line graph | n | high | high | 4-connected false | mutate counterexamples | — | ELIGIBLE | A |
| C016 | Spectral graph theory | Nikiforov optimal consecutive-cycle constant | S06 | 2026 | UNVERIFIED OPEN STATUS | graph | n,C | very high | medium | successive lower bounds | spectral optimization | — | HOLD | B |
| C017 | Digraphs | Seymour second-neighborhood conjecture | S07 | 2026 | OPEN—EVIDENCE AUDITED | oriented graph | n | very high | high | tournaments, δ+≤6 | canonical digraphs | — | ELIGIBLE | A |
| C018 | Digraphs | Strong Seymour vertex | S07 | 2026 | OPEN—EVIDENCE AUDITED | oriented graph | n | medium | high | partial | canonical digraphs | — | ELIGIBLE | A |
| C019 | Digraphs | Strong Seymour vertex in tournaments | S07 | 2026 | OPEN—EVIDENCE AUDITED | tournament | n | medium | very high | not reported | unlabeled tournaments | 18 | BACKLOG Target E | A |
| C020 | Group theory | Promislow minimum non-UP size 14 | S08 | 2026 | MINIMAL-COUNTEREXAMPLE STUDIED | finite group subset | n,radius | high | high | ball radius 6 | exact constraints | — | SECONDARY | E |
| C021 | Group theory | Polynomial/small re-realization radius | S08 | 2026 | OPEN—EVIDENCE AUDITED | integer systems | n | high | medium | 7000 random systems | lattice bounds | — | ELIGIBLE | A |
| C022 | Graph coloring | Eventual unlabeled list-color equality | S09 | 2026 | UNVERIFIED OPEN STATUS | graph | G,k | medium | high | point-determining graphs | small exceptions | — | HOLD | B |
| C023 | Rigidity | Strong stress-flex conjecture | S10 | 2026 | OPEN—EVIDENCE AUDITED | PL framework | surface,stress | very high | medium | convex weak version | nonconvex exact models | — | ELIGIBLE | A |
| C024 | Graph coloring | Planar D-index bound for Δ=6..32 | S11 | 2026 | OPEN—EVIDENCE AUDITED | planar graph | Δ | high | high | Δ≤5,Δ≥33 | SAT coloring | — | ELIGIBLE | A |
| C025 | Extremal combinatorics | Exact AP-intersection family size | S12 | 2026 | OPEN—EVIDENCE AUDITED | set family | N | medium | very high | N≤12 | SAT/ILP | 20 | FIRST ALTERNATE | A |
| C026 | Extremal combinatorics | Szabó kernel/starred extremal family | S12 | 2026 | OPEN—EVIDENCE AUDITED | set family | N | medium | very high | N≤12 | non-starred search | — | ELIGIBLE | A |
| C027 | Latin squares | No disjoint transversals and no pinned entry | S13 | 2026 | OPEN—EVIDENCE AUDITED | Latin square | even n | medium | high | 28,32..10000 | transversal ILP | — | ELIGIBLE | A |
| C028 | Latin squares | Dominant transversal existence | S13 | 2026 | OPEN—EVIDENCE AUDITED | Latin square | n | medium | high | most residue classes | n=3 mod 4 | — | ELIGIBLE | A |
| C029 | Spectral graph theory | Signed circulant global optimizer | S14 | 2026 | DISPROVED — SMALLEST FAILURE n=32 VERIFIED | signed graph | even n | low-medium | very high | all even n=8..30 verified true; n=32 exact counterexample; false for every 8\|n, n≥32 | exhaustive exact finite computation + explicit n=32 certificate + period-8 Floquet family | 18 | Target A—independent reconstruction audit | smallest counterexample order computationally certified 2026-08-15 |
| C030 | Algebraic combinatorics | Skew-shape order-polynomial statistic | S15 | 2026 | OPEN—EVIDENCE AUDITED | poset/permutation | shape,n | low-medium | very high | fence case | symbolic enumeration | 18 | BACKLOG Target C | A |
| C031 | Algebraic combinatorics | Circular-fence order-polynomial statistic | S15 | 2026 | OPEN—EVIDENCE AUDITED | poset/permutation | fence,n | low-medium | very high | fence case | symbolic enumeration | — | ELIGIBLE | A |
| C032 | Probability | Weighted Bernoulli mean exceedance | S16 | 2026 | OPEN—EVIDENCE AUDITED | rational weights | p,m,w | medium | high | p=1/n | boundary weights | — | ELIGIBLE | A |
| C033 | Extremal combinatorics | MMS conjecture | S16 | 2026 | OPEN—EVIDENCE AUDITED | real vector | n,k | very high | medium | many special cases | sign-pattern LP | — | ELIGIBLE | A |
| C034 | Extremal combinatorics | Restricted near-3k MMS | S16 | 2026 | OPEN—EVIDENCE AUDITED | real vector | n,k,ε,C | high | high | not reported | integer reduction | — | ELIGIBLE | A |
| C035 | Graph theory | Edge count of τk-maximal graphs | S17 | 2026 | OPEN—EVIDENCE AUDITED | graph | n,k | medium | high | k=1 | flow/matroid | — | ELIGIBLE | A |
| C036 | Graph theory | Even cycles are normal | S18 | 2026 | OPEN—EVIDENCE AUDITED | induced-saturated graph | t | medium | high | t=2..5 | witness search | — | ELIGIBLE | A |
| C037 | Graph theory | Every non-complete graph deletion-normal | S18 | 2026 | OPEN—EVIDENCE AUDITED | graph pair H,G | |H| | medium | very high | |H|≤6 | SAT witness/counterexample | — | ELIGIBLE | A |
| C038 | Zero forcing | PSD fast-join characterization | S19 | 2025 | OPEN—EVIDENCE AUDITED | graph | n | low-medium | very high | joins | graph enumeration | — | ELIGIBLE | A |
| C039 | Zero forcing | Standard fast-join characterization | S19 | 2025 | OPEN—EVIDENCE AUDITED | graph | n | low-medium | very high | joins | graph enumeration | — | ELIGIBLE | A |
| C040 | Domination | Bipartite uniquely-dominatable edge bound | S20 | 2025 | OPEN—EVIDENCE AUDITED | bipartite graph | n,γ | low-medium | very high | γ=2,n=3γ | SAT/ILP | 19 | BACKLOG Target D | A |
| C041 | Hamiltonicity | Hamiltonian bicirculants | S21 | 2025 | OPEN—EVIDENCE AUDITED | bicirculant | m,d,s | medium-high | high | broad m range | structured generation | — | ELIGIBLE | A |
| C042 | Number theory | Rational-base word normality | S22 | 2025 | OPEN—EVIDENCE AUDITED | infinite word | p,q,seed | very high | medium | q=1, experiments | discrepancy search | — | ELIGIBLE | A |
| C043 | Number theory | Nonexistence of Zp/q numbers | S22 | 2025 | OPEN—EVIDENCE AUDITED | real orbit | p,q | very high | low | finite exclusions | orbit pruning | — | ELIGIBLE | A |
| C044 | Number theory | Equidistribution of Tp/q iterates | S22 | 2025 | OPEN—EVIDENCE AUDITED | integer orbit | p,q,n,k | very high | medium | equivalent C042 | residue search | — | MERGE C042 | A |
| C045 | Number theory | At most two rational-base expansions | S22 | 2025 | OPEN—EVIDENCE AUDITED | representation | p,q,x | high | medium | p≥2q−1 | overlap automata | — | ELIGIBLE | A |
| C046 | Number theory | Dubickas termination problem | S22 | 2025 | OPEN—EVIDENCE AUDITED | integer dynamics | p,q,S,x0 | high | high | not reported | cycle search | — | ELIGIBLE | A |
| C047 | Extremal combinatorics | Exact 2-xor Kneser clique number | S23 | 2025 | OPEN—EVIDENCE AUDITED | Kneser graph | n,k | medium | very high | bounds | maximum clique | — | ELIGIBLE | A |
| C048 | Extremal combinatorics | Higher xor-power exponent | S23 | 2025 | UNVERIFIED OPEN STATUS | Kneser xor-power | ℓ,k,n | high | high | bounds | exponent constructions | — | HOLD | B/quantifier typo |
| C049 | Algebraic combinatorics | Schur log-concavity of partition sequences | S24 | 2025 | OPEN—EVIDENCE AUDITED | symmetric function | λ,α,β | low-medium | very high | small λ tests | boundary exact expansion | 20 | SECONDARY Target B | A |
| C050 | Quantum/combinatorics | Perpane iff perfect cancellation graph | S25 | 2025 | OPEN—EVIDENCE AUDITED | graph/network | G | medium | high | structural cases | SAT/network synthesis | — | ELIGIBLE | A |

## 单项候选的最低证据要求

候选进入排序前，Notes 或关联文档至少应记录：

- 原始出处与稳定链接；
- 精确定义及原猜想原文位置；
- 正式发表信息（如有）；
- 已证明的特殊情况；
- 作者或既有程序验证的范围；
- 已知失败或反例范围；
- 最新状态检索的日期、查询方式和证据；
- 对“仍开放”判断的置信度及未消除的不确定性。

完整命题、作者、arXiv 链接及初筛数据见 [`literature/RAW_CONJECTURE_SURVEY.md`](literature/RAW_CONJECTURE_SURVEY.md)；开放状态证据见 [`literature/OPEN_STATUS_AUDIT.md`](literature/OPEN_STATUS_AUDIT.md)。Score 在 Prompt 3 统一计算，当前以 `—` 占位。
