# Candidate Attackability Ranking

日期：2026-08-14
输入：Prompt 2 的 A 类 39 项与 E 类 1 项；B/F 类不排名。

## 20 分评分模型

| 维度 | 分值 | 判定标准 |
|---|---:|---|
| 文献价值 `L` | 0–4 | 0=几乎无背景；4=领域内重要或能连接多个问题 |
| 对象可生成 `G` | 0–3 | 0=难生成；3=有限、自然且可规范枚举 |
| 性质可判定 `D` | 0–3 | 0=近乎不可计算；3=可快速精确判定 |
| 已知验证边界 `K` | 0–2 | 2=明确首个未知规模/有限缺口 |
| 参数攻击面 `P` | 0–2 | 2=多参数、退化边界或已知加强版反例可迁移 |
| 自动化适配 `A` | 0–2 | 2=非常适合枚举/SAT/SMT/ILP/符号计算 |
| 反例可证明性 `V` | 0–2 | 2=候选可转为短 exact certificate |
| 扩展潜力 `E` | 0–2 | 2=自然通向最小性、无穷族、分类或修正定理 |

总分 `T=L+G+D+K+P+A+V+E`。同分时依次按 `V`、`K`、`L` 排序。该分数衡量“适合本项目攻击”，不衡量命题的绝对数学重要性。

## Top 20

| Rank | ID | 简称 | L | G | D | K | P | A | V | E | T | 决策 |
|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | C049 | Schur log-concavity 分拆序列 | 4 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | **20** | Top 10 |
| 2 | C037 | deletion-normal 图猜想 | 4 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | **20** | Top 10 |
| 3 | C025 | AP-intersection 精确极值 | 4 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | **20** | Top 10 |
| 4 | C040 | 唯一最小支配集二分图边界 | 3 | 3 | 3 | 2 | 2 | 2 | 2 | 2 | **19** | Top 10 |
| 5 | C047 | Kneser 二次 xor 最大团公式 | 4 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | **19** | Top 10 |
| 6 | C029 | signed circulant 全局谱半径最小类 | 3 | 3 | 3 | 2 | 1 | 2 | 2 | 2 | **18** | Top 10 |
| 7 | C030 | skew-shape order-polynomial 统计 | 3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | **18** | Top 10 |
| 8 | C031 | circular-fence order-polynomial 统计 | 3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | **18** | Top 10 |
| 9 | C019 | tournament strong Seymour vertex | 4 | 3 | 3 | 1 | 1 | 2 | 2 | 2 | **18** | Top 10 |
| 10 | C027 | Latin square 特殊 transversal | 3 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | **18** | Top 10 |
| 11 | C004 | defect-two total regularity | 3 | 3 | 3 | 1 | 2 | 2 | 2 | 2 | **18** | Top 20 |
| 12 | C032 | weighted Bernoulli 下界 | 4 | 2 | 3 | 1 | 2 | 2 | 2 | 2 | **18** | Top 20 |
| 13 | C034 | 受限 near-3k MMS | 4 | 2 | 3 | 1 | 2 | 2 | 2 | 2 | **18** | Top 20 |
| 14 | C038 | PSD fast-join 刻画 | 3 | 3 | 3 | 1 | 1 | 2 | 2 | 2 | **17** | Top 20 |
| 15 | C039 | standard fast-join 刻画 | 3 | 3 | 3 | 1 | 1 | 2 | 2 | 2 | **17** | Top 20 |
| 16 | C050 | perpane/cancellation 等价 | 3 | 3 | 3 | 1 | 2 | 2 | 2 | 1 | **17** | Top 20 |
| 17 | C036 | 偶圈 induced-saturation | 3 | 3 | 3 | 1 | 1 | 2 | 2 | 2 | **17** | Top 20 |
| 18 | C035 | `τ_k`-maximal 图边数 | 3 | 3 | 3 | 1 | 1 | 2 | 2 | 2 | **17** | Top 20 |
| 19 | C024 | 平面图 D-index 有限 Δ 窗口 | 4 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | **16** | Top 20；生成/判定成本高 |
| 20 | C041 | Hamiltonian bicirculants | 4 | 3 | 3 | 0 | 1 | 2 | 2 | 1 | **16** | Top 20；首未知规模大 |

说明：表格按总分降序，同分按反例证书、已知边界、文献价值及资源成本细排。C049、C037、C025 的满分表示项目适配度极高，不代表容易解决。

## 其余可保留候选

| ID | T | 主要降分原因 |
|---|---:|---|
| C002 | 14 | 参数文献脉络窄，未知范围不够明确 |
| C009 | 12 | 极值问题难以通过单一反例结案 |
| C011 | 13 | 三维刚性秩计算和证明转换成本高 |
| C012 | 12 | 经典高难，搜索空间增长快 |
| C013 | 15 | 划分数量大，但约束编码良好 |
| C014 | 16 | 有边界反例可迁移，刚性判定仍昂贵 |
| C015 | 16 | 同上，全局刚性比刚性更难 |
| C017 | 15 | 经典问题，已有大量特例研究 |
| C018 | 16 | 新问题但对象空间大 |
| C020 | 14 | 已有专门最小见证研究，新颖性风险 |
| C021 | 13 | 需要一般重实现界，不像直接反例搜索 |
| C023 | 13 | PL 曲面生成与 exact geometry 复杂 |
| C026 | 18 | 与 C025 高度耦合，合并为一个研究目标 |
| C028 | 17 | 与 C027 同源，合并可节约基础设施 |
| C033 | 13 | 经典 MMS 难度过高 |
| C042 | 11 | normality 无有限证书，统计异常不是反例 |
| C043 | 9 | 实数候选生成与全轨道验证困难 |
| C044 | 10 | 与 C042 等价且缺有限否证证书 |
| C045 | 12 | 表示系统复杂，搜索可行但证明难 |
| C046 | 14 | 找循环可否证，但无循环不能证明终止 |

## Top 10 深入攻击分析

### 1. C049 — Schur log-concavity

- **入口：** 枚举满足论文边界的最小分拆 `λ,β,α`，exact 展开 `s_μ²-s_{μ-1}s_{μ+1}` 的 Schur 系数。
- **首攻边界：** `ℓ(λ)=ℓ(α)+1`、`λ_last=β_1` 附近；放宽版反例提示 failure 可能贴着边界出现。
- **工具：** Sage/对称函数、整数 Littlewood–Richardson 系数、delta debugging。
- **候选证书：** 一组分拆参数和一个负 Schur 系数即可精确否证。
- **升级潜力：** 最小反例、失败参数分类、修正长度/间隔条件、无穷反例族。

### 2. C037 — deletion-normal

- **入口：** 从 7 顶点非完全图 `H` 开始，按同构分类；对每个 `H` 搜索 deletion-saturated witness `G`，找不到见证不能直接当反例。
- **双层策略：** 先复现 `|H|≤6`；再用 SAT 逐步扩大 witness 顶点上界，并分析难例共同结构。
- **风险：** 否证需要证明某个 `H` 对所有有限 `G` 都无 witness，单纯有限搜索不足。
- **升级潜力：** 即使无反例，也可得到 7 顶点全分类或新的构造闭包定理。

### 3. C025 — AP-intersection extremal families

- **入口：** 复现公开的 `N≤12` exact computation，从 `N=13` 搜索超过公式界的集合族。
- **编码：** 每个 `[N]` 子集为候选顶点；两子集交为非空 AP 时连边，问题化为最大团。
- **证书：** 超界 family 是短、完全离散的反例；最大性可由 SAT/maximum-clique certificate 支撑。
- **升级潜力：** 最小 `N`、非-starred 结构、kernel conjecture、修正公式。

### 4. C040 — unique domination bipartite bound

- **入口：** 从首个未证明组合 `γ≥3,n>3γ` 开始生成二分图。
- **编码：** 支配数、唯一最小支配集与边数阈值均可 SAT/ILP；先固定 bipartition sizes。
- **证书：** 邻接表 + 唯一支配集的完整枚举/独立 verifier。
- **升级潜力：** 最小反例、极值结构分类、修正边界。

### 5. C029 — signed circulants

- **入口：** 先 exact 复现 `n≤18`，再完整枚举 `n=20` 的 switching classes。
- **关键改进：** 不使用 `10^-9` 浮点比较；用整数 characteristic polynomial、Sturm sequence 或代数数隔离比较谱半径。
- **证书：** signing、switching invariant、特征多项式及严格代数数次序。
- **升级潜力：** 最小反例或 flux-minimization 定理、周期性无穷族。

### 6. C030 — skew-shape order polynomial

- **入口：** 按 cell 数和 skew-shape 同构枚举，分别 exact 计算 `Ω(P;t)` 与 `ebl` 分布。
- **边界：** disconnected/ribbon/thin shapes 与含 `2×2` block 的首次转变。
- **证书：** 两个整数多项式及首个不同系数。
- **升级潜力：** 最小形状反例、成立形状分类、修正统计量。

### 7. C031 — circular fence order polynomial

- **入口：** 用 cyclic composition 规范化 circular fences，逐规模比较两侧多项式。
- **风险：** 定义中的旋转/反射等价必须与论文一致。
- **证书：** fence composition、order polynomial、`bbl` histogram。
- **升级潜力：** parity/周期 failure mechanism 和参数化族。

### 8. C047 — Kneser xor-power

- **入口：** 固定小 `k`，寻找公式进入稳定区前后的最大团；先复现论文上下界构造。
- **编码：** 顶点为 `k`-集对，邻接由 xor-disjointness 精确判定；maximum clique 可调用 SAT/ILP。
- **证书：** 超公式 clique 可直接反例；若支持命题，则记录稳定阈值猜测。
- **升级潜力：** 精确阈值 `n_0(k)`、无穷构造、改进常数 `c(k)`。

### 9. C019 — strong Seymour tournament

- **入口：** 生成 unlabeled tournaments，计算每个顶点的一、二阶出邻域与 strong 条件。
- **边界：** regular/near-regular、极端 score sequence、高对称 tournament。
- **证书：** tournament adjacency matrix；逐顶点列出违反 strong 条件的 exact counts。
- **升级潜力：** 最小反例、blow-up 家族、增加度数条件后的修正定理。

### 10. C027 — Latin square transversal gap

- **入口：** 首先核验论文构造 `n=28,32`，然后集中处理 `n=30`；大于 10000 的部分更适合证明而非搜索。
- **编码：** transversal 是 3D matching；pinned entry、两两不交、dominant 等条件可用 ILP/SAT。
- **证书：** Latin square 与全部关键 transversal 的覆盖/不相交证书。
- **升级潜力：** 补齐 `n=30`、统一构造、参数化证明。

## Prompt 4 建议

最终目标选择不应简单取排名前三。建议从互补的计算范式中选 3–5 项：

- exact spectral：C029；
- symbolic algebraic combinatorics：C049 或 C030；
- finite graph/SAT：C040 或 C019；
- extremal maximum-clique：C025；
- structured design/ILP：C027。
