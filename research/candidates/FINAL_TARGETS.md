# Final Targets

日期：2026-08-14

输入：`CANDIDATE_RANKING.md` Top 10
目标：选择 3–5 个互补项目；任何时刻仅一个 `ACTIVE`。

## Top 10 形式化攻击评估

### C049 — Schur log-concavity of partition sequences

1. **原命题：** 在 S24 Conj. 1 的长度/间隔假设下，`f_i=s_{λ∪iβ+iα}` 构成 strongly Schur log-concave 序列。
2. **变量：** partitions `λ,β`，整数向量 `α`，索引 `i`。
3. **定义域：** 每个下标确为 partition；采用论文的零函数约定处理越界项。
4. **结论：** 对所有有效 `i≥1`，`f_i²-f_{i-1}f_{i+1}` Schur-positive。
5. **反例条件：** 满足全部假设，且某个 Schur 展开系数为负。
6. **已知规模：** 论文报告 `|λ|≤6,ℓ(λ)≤3` 的测试参数支持；放宽 `ℓ(λ)>ℓ(α)` 后存在反例。
7. **起点：** 贴边界枚举 `ℓ(λ)=ℓ(α)+1`、`λ_last=β_1`，从 `|λ|=7` 起。
8. **空间：** 分拆数乘有限 `α,β` 盒；原始为指数增长，但 `|λ|≤15` 可按边界切片。
9. **对称：** 去除尾零、共同平移/共轭分拆仅在证明等价后使用；参数规范排序。
10. **判定复杂度：** Littlewood–Richardson 展开为 exact 整数计算；中等。
11. **策略：** exhaustive boundary sweep；LR-rule structured enumeration；随机 hill-climb 最小 Schur 系数；发现后 exact verifier。
12. **失败机制猜测：** 长度边界、最后一行与 `β_1` 碰撞、partition 失稳、LR cancellation。

### C037 — deletion-normal graphs

1. **原命题：** 每个非完全图 `H` 都存在有限 `H`-deletion-saturated 图。
2. **变量：** 模式图 `H`、witness 图 `G`。
3. **定义域：** `H` 非完全；`G` 至少一条边且 induced-`H`-free。
4. **结论：** 存在 `G`，删去任一边都会产生 induced `H`。
5. **反例条件：** 一个 `H` 对所有有限 `G` 都不存在 witness；这不是有限搜索可直接认证的条件。
6. **已知规模：** 所有 `|H|≤6` 已证/验证。
7. **起点：** 7 顶点非完全图，优先排除已知闭包类。
8. **空间：** 7 顶点 `H` 约 10^6 个 unlabeled graphs；每个 `G` 的阶无先验界。
9. **对称：** graph6 canonical labeling；按补图对偶 deletion/addition。
10. **判定复杂度：** 给定 `(H,G)` 可精确判定；反例的全称条件不可有限判定。
11. **策略：** structured construction/SAT witness；学习难例；尝试推导 witness-size bound；不把 bounded failure 当反例。
12. **失败机制猜测：** twin structure、极端 degree、self-complementary obstruction、witness 阶数爆炸。

### C025 — AP-intersection exact extremum

1. **原命题：** `t(N)=C(N,2)+1+⌊(N−1)/4⌋`。
2. **变量：** `N` 与 distinct subset family `F⊆2^[N]`。
3. **定义域：** 任意两成员交集是非空 arithmetic progression。
4. **结论：** `|F|` 不超过显式界，且构造达到。
5. **反例条件：** 合法 `F` 且大小严格超过该界。
6. **已知规模：** 无条件 `N≤12`；starred 情形全 `N`。
7. **起点：** `N=13`。
8. **空间：** compatibility graph 有 `2^N` 顶点；求超过阈值的 clique。
9. **对称：** `[N]` 的反射；不能假设任意置换保持 AP。
10. **判定复杂度：** 给定 family 为多项式时间 exact；搜索 NP-hard maximum clique。
11. **策略：** 复现公开代码；SAT cardinality；branch-and-bound；从 near-starred 局部突变。
12. **失败机制猜测：** 非-starred kernel、多个中心竞争、边界 AP 窗口、异常 4/5-term AP。

### C040 — bipartite unique-domination edge bound

1. **原命题：** S20 Conj. 1 的显式 `m(n,γ)` 上界成立。
2. **变量：** bipartite graph `G`、`n=|V|`、domination number `γ`。
3. **定义域：** 无孤点、唯一 minimum dominating set、`γ≥2,n≥3γ`。
4. **结论：** `|E(G)|≤m(n,γ)`。
5. **反例条件：** 满足定义域且边数超过界。
6. **已知规模：** `γ=2` 和 `n=3γ` 已证。
7. **起点：** `γ=3,n=10`，随后增大 `n`。
8. **空间：** 固定 bipartition `(a,b)` 有 `2^{ab}` 图；SAT 可直接施加高密度约束。
9. **对称：** 同一侧顶点置换、交换两侧、canonical bipartite labeling。
10. **判定复杂度：** domination number/唯一性 NP-hard，但小规模 SAT exact。
11. **策略：** SAT/CP-SAT；从极值构造加边；随机高密度图；delta-debug 反例。
12. **失败机制猜测：** 不平衡 bipartition、private-neighborhood 共享、`n=3γ+1` 边界、多个近最小支配集。

### C047 — 2-xor Kneser clique number

1. **原命题：** 固定 `k`、充分大 `n` 时 `f_2(n,k)` 等于 S23 Conj. 1.2 的显式式。
2. **变量：** `n,k` 与 xor-product 中 clique。
3. **定义域：** 两份 `KG(n,k)`；顶点等价为两块基集上的成对 `k`-子集。
4. **结论：** maximum clique 等于公式。
5. **反例条件：** 任意 `n` 位于宣称稳定区却有更大 clique；“充分大”使单个小 `n` 不能直接否证渐近命题。
6. **已知规模：** 论文给上下界和构造，稳定阈值未给。
7. **起点：** 小 `k=2,3`，逐 `n` 求 exact 值并猜阈值。
8. **空间：** 顶点数 `C(n,k)^2`；最大团指数增长。
9. **对称：** `S_n×S_n` 与交换两坐标。
10. **判定复杂度：** maximum clique NP-hard；给定 clique 易验。
11. **策略：** SAT/ILP；orbital branching；代数构造；局部搜索超越公式。
12. **失败机制猜测：** 小 `n` 非稳定、有限几何构造、奇偶 `n/k`、高对称 block design。

### C029 — signed circulant optimizer

1. **原命题：** 每个偶数 `n≥8` 上，`C_n(1,2)` 的 `α=−1` twisted signing 全局最小化谱半径。
2. **变量：** 偶数 `n`、edge signing `σ`（模 switching）。
3. **定义域：** `C_n(1,2)` 的所有 `±1` signings。
4. **结论：** `ρ(A_σ)≥ρ_-(n)`。
5. **反例条件：** 某 signing 的谱半径严格小于 `ρ_-(n)`。
6. **已知规模：** 浮点穷举 `n=8,10,…,18`。
7. **起点：** exact 复现后搜索 `n=20`。
8. **空间：** 论文约化为 `2^{n+1}` switching classes；`n=20` 约 2.1M。
9. **对称：** switching、dihedral automorphisms、global sign（谱半径不变）。
10. **判定复杂度：** integer characteristic polynomial + algebraic root isolation；可精确。
11. **策略：** exhaustive canonical classes；flux-structured enumeration；branch-and-bound；随机 signing 只作候选生成。
12. **失败机制猜测：** 非交替 flux、holonomy/parity、短周期缺陷、偶数阶模 4/6 转变。

### C030 — skew-shape order-polynomial identity

1. **原命题：** 对 skew-shape cell poset `P`，`n!Ω(P;t)=Σ t^{ebl_P(σ)}`。
2. **变量：** skew shape `λ/μ`、其 labelings/permutations `σ`。
3. **定义域：** 有限 skew Young diagrams；精确定义沿用 S15。
4. **结论：** 两个整数多项式相等。
5. **反例条件：** 任一系数不同。
6. **已知规模：** 论文证明 fence 情形；未量化 skew-shape 穷举边界。
7. **起点：** 先复现 ribbons，再从最小含 `2×2` block 的 shape。
8. **空间：** 按 cell 数为 skew partition pairs；labelings 最坏 `n!`。
9. **对称：** 平移、180°/转置仅在统计不变性验证后 quotient。
10. **判定复杂度：** 小 `n` 可 exact；动态规划可代替全 `n!`。
11. **策略：** structured enumeration；DP histogram；symbolic order polynomial；随机大 shape。
12. **失败机制猜测：** `2×2` block、disconnected shape、block-root 非唯一、边界 cancellation。

### C031 — circular-fence identity

1. **原命题：** circular fence poset 满足 `n!Ω(P;t)=Σ t^{bbl_P(σ)}`。
2. **变量：** cyclic up/down composition 与 permutations。
3. **定义域：** S15 定义的 circular fences。
4. **结论：** 两个整数多项式相等。
5. **反例条件：** 某系数不相等。
6. **已知规模：** 未报告完整范围。
7. **起点：** 最短非平凡 cyclic compositions，逐 `n`。
8. **空间：** cyclic compositions 约指数增长，dihedral quotient 后显著减小。
9. **对称：** rotation、reflection、global order duality。
10. **判定复杂度：** 同 C030。
11. **策略：** canonical cyclic composition；DP；exact polynomial comparison；局部 mutation。
12. **失败机制猜测：** 奇偶周期、首尾 block 合并、旋转根选择、对偶不对称。

### C019 — strong Seymour vertex in tournaments

1. **原命题：** 每个 tournament 都含 strong Seymour vertex。
2. **变量：** tournament `T`、候选顶点 `v`。
3. **定义域：** 有限 complete oriented graphs。
4. **结论：** `∃v StrongSeymour_T(v)`，定义严格取 S07。
5. **反例条件：** 对每个顶点 strong 条件均失败。
6. **已知规模：** S07 未报告 exhaustive bound。
7. **起点：** 先复现论文例与普通 Seymour 定理，再枚举 unlabeled tournaments。
8. **空间：** labeled 为 `2^{C(n,2)}`；unlabeled 至 `n≈11–12` 尚可专用生成。
9. **对称：** tournament isomorphism、dual orientation（需核强条件是否保持）。
10. **判定复杂度：** 给定 tournament 为多项式时间 exact counts。
11. **策略：** exhaustive；按 score sequence 枚举；regular/near-regular 随机；SAT 直接编码 `∀v ¬Strong`。
12. **失败机制猜测：** regularity、邻域 cancellation、cyclic blow-up、奇数阶 parity。

### C027 — Latin square transversal construction

1. **原命题：** 每个偶数 `n≥28` 存在无两条不交 transversals 且无 pinned entry 的 Latin square。
2. **变量：** `n`、Latin square `L`、其 transversal 集。
3. **定义域：** 偶数阶 Latin squares。
4. **结论：** 存在满足两性质的 `L`。
5. **反例条件：** 某偶数 `n` 的所有 Latin squares 都不满足；同 C037，纯有限失败需完整分类才可否证。
6. **已知规模：** `n=28`、`32≤n≤10000` 已构造；`n=30` 未覆盖。
7. **起点：** 论文构造在 `n=30` 的适配/扰动。
8. **空间：** 全 Latin squares 巨大；只搜索参数化 construction family。
9. **对称：** row/column/symbol isotopy、parastrophy。
10. **判定复杂度：** transversal existence NP-hard；给定有限 square 可 ILP 完整枚举/覆盖。
11. **策略：** structured construction；ILP transversal oracle；local trades；SAT 处理 pinned/disjoint 条件。
12. **失败机制猜测：** `n=30` 模结构、必要 transversal 缺失、pinned entry、构造的 parity obstruction。

## 最终选择

| 角色 | ID | 状态 | 选择理由 |
|---|---|---|---|
| **Target A** | **C029** | **ACTIVE** | 最小未知规模明确，搜索空间约 2.1M，可做完整 exact enumeration，反例与无反例结果均可严格认证。 |
| **Target B** | **C049** | SECONDARY | 符号计算可直接产生负整数系数证书，已知放宽版反例提示边界附近有攻击面。 |
| **Target C** | **C030** | BACKLOG | 多项式恒等式反例证书短，适合独立 verifier；与 Target B 共用对称函数/组合基础设施。 |
| **Target D** | **C040** | BACKLOG | 图/SAT 路线，首个参数窗口小，反例是有限邻接表。 |
| **Target E** | **C019** | BACKLOG | tournament 可按同构完整生成，反例可逐顶点 exact 验证，且与其他目标方法互补。 |

C025 保留为第一替补：价值很高且反例证书明确，但已有公开 exact computation，需先审计其代码和 `N=13` 资源成本。C037、C027 暂不设为主目标，因为“有限范围没有 witness”不能直接否证存在性命题。

下一阶段只研究 Target A；其他目标不得同时启动大规模计算。
