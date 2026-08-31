# 文献综述：固定图上的 Signed Spectral-Radius Minimization

## 摘要

本文综述服务于论文 When Is the Twisted Signing of an Even Cycle Square
Spectrally Optimal? 的投稿定位与重构，而非一般 signed graph theory 的完整
回顾。核心问题是在固定底图
\[
C_n^2=C_n(1,2)
\]
上，对所有边签名 \(\sigma\) 最小化 signed adjacency spectral radius
\[
m_n=\min_\sigma \rho(A_\sigma).
\]

筛选后的文献库包含 13 条记录：3 条已发表 S 级文献、1 条必须单列的直接
preprint、7 条 A 级文献与 2 条历史源头。它们共同说明，当前工作并非普通的
signed graph extremal problem，也不是单纯的 periodic-operator analysis；
它同时具有固定底图优化、两侧谱半径、全阶分类、局部缺陷与有限证明闭合的
特征。

## 1. 问题位置

### 1.1 signing 与 two-lift 背景

Bilu--Linial (2006) 将签名与 two-lift 的新特征值联系起来，提出在一般正则图
上寻找小 signed spectrum 的广义计划。Marcus--Spielman--Srivastava (2015)
在 bipartite setting 中通过 interlacing families 得到 Ramanujan signing；
其中 bipartite spectral symmetry 将一侧控制转换为两侧控制。

当前问题的关键区别是 \(C_n^2\) 非二分图。对非二分固定图，控制
\(\lambda_{\max}\) 不自动控制
\(\rho(A)=\max\{|\lambda|:\lambda\in\operatorname{Spec}(A)\}\)。因此当前
论文研究的不是是否存在一个好的 signing，而是一个指定 signing 是否达到真正的
两侧最优值。

Belardo--Cioabă--Koolen--Wang (2018) 为这一转向提供了直接的已发表问题来源：
它明确提出，对一个固定 connected graph，哪些 signature 最小化 adjacency
spectral radius。该文应成为当前稿第一个现代问题定位引用；Bilu--Linial 与
MSS 应在同段作为广义来源与 bipartite 对照，而不应使 Introduction 变成
Ramanujan-lift 综述。

### 1.2 published signed spectral extremal line

Brunetti--Stanić (2022) 是最接近的已发表 spectral-radius extremal
classification：它在固定 order 的 connected unbalanced signed graphs 中确定
extremal spectral radius 和 index，并给出 switching-isomorphism 意义下的
extremizer。其意义在于证明，signed adjacency spectral radius 的完整 extremal
classification 已是成熟发表问题。

两者的优化域不同。Brunetti--Stanić 同时允许 underlying graph 与 signature
变化；当前工作固定 \(C_n(1,2)\)，只让 signature 变化。前者是全图类极值，
后者是高度结构化的 fixed-underlying-graph minimization。因此当前工作可被
表述为已发表 signed spectral extremal line 的固定底图完整实例，但不能被
表述为第一篇 signed spectral extremal classification。

Ghorbani--Majidi (2024) 在 complete signed graphs 中优化最大 index 或最小
minimum eigenvalue，并给出受负边子图约束的结构性 extremizer。它并非
\(\rho(A)\) 的 fixed-circulant minimization，但支持一个重要事实：固定的、
代数上显著的底图族可以承载非平凡 signed adjacency extremal theory。该文
适合放在 Related Work，不宜放在 Introduction 首段。

### 1.3 signed spectral-radius program

Belardo--Brunetti (2024) 完成 signed graph adjacency spectral radius 的
limit-point/Hoffman-program 一侧；Brunetti--Trevisan (2026) 表明 unbalanced
signed graph 序列已足以恢复所有此类 limit points。两篇工作与当前稿的
minimizer truth set 没有直接重叠，但说明 signed spectral radius 已形成持续
发展的分类程序。

它们适合放在 Related Work 后半段或 Discussion，作用是把 eventual failure
from 48 onward 放入更大的 signed spectral-radius classification
landscape。不能把它们误写成当前 fixed-cycle-square 问题已经被处理。

## 2. 具体 cycle-square 问题

Suvagiya (2026, preprint) 是当前论文唯一的具体 direct predecessor。它给出
\(C_n(1,2)\) 的 flux coordinates、distinguished twisted classes、candidate
spectral formula、通过小阶的验证，以及被当前稿解决的 all-even conjecture。

其文章结构可以概括为：

specific circulant family -> switching and flux parametrization ->
distinguished signing families -> Fourier spectral formula -> small-order
computational evidence -> all-even conjecture.

当前论文应被表述为对该序列的严格升级：

published fixed-graph signing problem -> signed cycle-square family ->
Suvagiya candidate and conjecture -> complete nonmonotone truth set ->
period-eight bulk and G6 local mechanism -> analytic tail plus finite
exact completion.

因此 Suvagiya 应在已发表问题背景之后、主定理之前出现。将 preprint 放在
Introduction 第一段会使整篇文章看起来像近期手稿的局部修补；将它放在独立
问题背景之后，才能强调当前稿解决的是 fixed-graph signed spectral extremal
classification 的一个具体而完整实例。

## 3. 周期、flux 与局部 interface

Korotyaev--Saburova (2023) 是当前稿最应保留的 periodic/Floquet 方法引用。
它将 periodic magnetic discrete graph 的 spectrum 组织为有限 Floquet fibers，
并把 fiber trace 表示为由 flux、potential 与 quotient-graph cycles 控制的
quasimomentum Fourier series。其结构为：

periodic operator definition -> Floquet fiber reduction -> trace formulas ->
bandwidth estimates and sharpness examples.

这与当前稿的 period-eight reference phase、finite fiber determinant 和
flux-sensitive spectral edge 之间存在语言与方法对应。但引用时必须保持边界：
该文不研究 signing minimization，也不提供 G6 phase-slip theorem。

Kuchment--Vainberg (2006) 研究 locally perturbed periodic graph operators 的
embedded eigenfunctions 与局域化结构。它可用于说明 periodic bulk、local
perturbation 与 localized spectral state 是有成熟背景的 operator-theoretic
构型。当前稿对 bilateral G6、stable/unstable matching、finite-ring patch
identification 的证明仍是自足的，不能写成该文的直接应用。

Hu--Liu (2025) 的相关性偏结构背景而非技术移植。该文通过 signed graph
isoperimetry 获得 non-bipartite Cayley、vertex-transitive 与 Cayley-sum graphs
的非平凡谱区间。它支持把 \(C_n(1,2)\) 介绍为结构化 non-bipartite
circulant，而不支持任何 minimizer 结论。

## 4. 全阶分类与计算机辅助闭合

Lin--Ning (2021) 是最适合当前稿借鉴的 JGT 文章架构。其核心不是主题相同，
而是完整分类的组织方式：

classification theorem stated early -> large-order regime -> finite
exceptions -> all-order synthesis.

当前稿已经具备相同骨架：period-eight/G6/IMS 给出 eventual regime，
\(48\le n<240\) 的证书构成 finite bridge，更小阶的 switching quotient 与
finite-state closure 处理 nonmonotone exceptions。后续重构应让读者在进入
certificate details 前先看见这一骨架。

Goedgebeur--Schaudt (2018) 的启发在于 computation 的合法性叙事。它先建立
extension/reduction 与 canonicalization 的 completeness contract，再报告有限
enumeration。对当前稿而言，Section 7 不应反复强调 exact，而应把有限状态空间
为何覆盖全部 signings 讲清一次，然后把 arithmetic certificates 作为该完备
约化的闭合步骤。

## 5. 逐篇论证结构：主定理（问题）→ 证明 → 可引用描述

本节是供正文写作直接调用的压缩卡片。`全文核对`表示已按本地合法 PDF
检查过 theorem/proposition 与章节；`摘要层`表示只核对了出版社/作者公开的
摘要、元数据或页面，故只陈述该来源明确给出的结论，绝不虚构证明细节。

### S1. Belardo--Cioabă--Koolen--Wang (2018): 问题源头

**主问题。** Problem 3.18 直接提出：给定 simple connected graph (G)，刻画
使 adjacency spectral radius 最小的 signature。这不是一条声称已经解决问题的
主定理，而是当前稿最准确的已发表问题节点。

**文章的论证结构。** 基础谱工具（coefficient formula、spectral moments、
interlacing、Schwenk recursion）→ 若干 signed-spectrum 专题（少特征值、
Hoffman program、最小特征值）→ 明确列出 open problems，其中包括 Problem
3.18。其功能是把“固定 (G)，只变 (sigma)”确认为独立研究方向。

**对本文的一句话描述。** 本文给出 Problem 3.18 在一个非二分、无限
circulant family (G=C_n(1,2)) 上的全阶完整实例，而非声称解决一般问题。

**证据层级。** 全文核对；应在 Introduction 的问题定位段引用。

### S2. Brunetti--Stanić (2022): signed extremal classification 的已发表范式

**主定理。** Theorems 3.1、3.5、4.7、4.8 分别围绕 order (n) 的 connected
unbalanced signed graphs，确定 maximum/minimum spectral-radius 或 index
极值以及相应 switching-isomorphism extremizer。

**证明链。** 先以 interlacing 与基本谱不等式给极值候选的必要条件 → 对
unbalanced connected graphs 做结构约化（特别是 cyclotomic/complete signed
graph 的极端情形）→ 用 switching 归并候选 → 通过显式特征多项式、eigenspace
与比较不等式排除其余情形。文章不是计算枚举，而是“结构引理先锁定候选、谱计算
完成 equality case”的标准极值证明。

**对本文的一句话描述。** 它证明 signed spectral-radius extremal
classification 已可形成完整定理；本稿的差别在于底图固定为 (C_n(1,2))，而非
允许底图随 order 改变。

**证据层级。** 全文核对；适合放在 Problem 3.18 之后，作为最近的已发表
extremal analogue。

### S3. Korotyaev--Saburova (2023): 周期磁算子的 Floquet--trace 链

**主定理。** Theorem 2.6 给出磁 Schrödinger operator 的 Floquet direct-integral
分解；Theorems 2.9 与 2.11 将 fiber trace 表为 fundamental graph 上 closed
walk/cycle 的 quasimomentum Fourier sum，并导出 band-width 估计；Theorem 3.2
给出对应 magnetic adjacency fiber 的 trace formula。

**证明链。** Γ-periodic graph 与 fundamental quotient → 磁 phase/flux 的
gauge-invariant 编码 → 有限维 fiber matrices → 展开 trace powers 为 closed
walks → 按 cycle flux 收集项 → 由 trace bounds 推出 spectral-band 结论和
sharpness examples。它把周期谱的全局问题降为一个有限 quotient 的代数计算。

**对本文的一句话描述。** 可引用为 period-eight bulk、有限 fiber determinant
与 flux-sensitive band edge 的方法背景；不能引用为 G6 defect 或 minimizer
定理的来源。

**证据层级。** 全文核对；适合 Section 3 的 method-background 段。

### S4. Suvagiya (2026 preprint): 本文直接的 conjectural predecessor

**主命题与猜想。** Proposition 1：对 even (n\geq10)，其 quadrilateral
constraints 一致且解恰有四个 switching classes；Proposition 2 用 triangle
signs 给出 twisted classes 的约束/坐标化；Conjecture 3 断言对每个 even
(n\geq8)，指定 α=−1 twisted signing 达到
(min_sigma\rho(A_\sigma))。

**证明链。** (C_n(1,2)) 的 local cycle signs → switching/flux
parametrization → distinguished twisted classes → Fourier computation得到
candidate spectral radius → small-order calculation → all-even conjecture。
这里的终点是 conjecture；没有 analytic tail、finite certificate closure 或对
counterexamples 的结构解释。

**对本文的一句话描述。** 当前稿的主定理应精确表述为该 all-even conjecture
的 complete truth-set determination，而非把 preprint 的数值证据说成先前证明。

**证据层级。** 全文核对，但为 preprint；必须同时给出版本号/日期并避免称为
published result。

### A1. Ghorbani--Majidi (2024): complete signed graphs 上的单侧极值

**主定理。** 文章在 complete signed graphs 上，按最大 largest eigenvalue 或
最小 least eigenvalue 组织 extremal characterization，并以 negative-edge
subgraph 的结构描述 equality cases。

**证明链。** 从 complete underlying graph 的 signed adjacency 结构出发 → 将
目标 eigenvalue 与负边子图的组合性质联系 → 对极端结构构造与比较 → 识别
equality cases。这里的目标是单侧 index，不能替代本稿的 two-sided
(ho(A)) 问题。

**对本文的一句话描述。** 用于支持“固定、代数高度对称的底图族也有深刻
signed spectral extremal theory”，不用于支持我们的具体结论。

**证据层级。** 摘要层；正文只引用其明确发表的 extremal scope，不写具体
lemma 或 theorem number。

### A2. Hu--Liu (2025): signed Cheeger 常数到非二分 Cayley 谱

**主定理。** Theorem 1.1 为 non-bipartite finite Cayley graphs 给出由 outer
vertex-boundary isoperimetric constant 控制的 nontrivial normalized adjacency
eigenvalue interval；Theorem 1.2 是 d-regular signed graph 的对应 signed
Cheeger inequality；Theorem 1.3 将结论扩展到 vertex-transitive/Cayley-sum
场景。

**证明链。** signed graph connection 与 switching 基础 → signed isoperimetric
quantities → coarea/functional inequality（Theorem 4.1）→ Cayley 结构的
specialization（Section 5）→ 更一般 connection graph extension（Section 6）。

**对本文的一句话描述。** 它给出非二分 Cayley/circulant 的现代谱背景；其
isoperimetric bounds 不判定任何 (C_n(1,2)) signing minimizer。

**证据层级。** 全文核对；宜在对象背景一句带过。

### A3. Belardo--Brunetti (2024): Hoffman limit-point program

**主定理。** 文章的核心是 signed-graph adjacency spectral radii 的 limit
points/Hoffman program，而非固定图最小化；其结论将 signed spectral radii
的累积极限问题放入可分类框架。

**证明链。** 从 signed graph switching 与谱半径序列出发 → 构造/识别可实现的
accumulation patterns → 与经典 Hoffman-program 问题比较。这是一条序列与极限
点的分类线，不是单个有限 circulant 的优化。

**对本文的一句话描述。** 适合在 Related Work 末段说明 signed spectral radius
研究已形成持续分类程序；不应被当作同题已有结果。

**证据层级。** 官方 OA 页面与摘要层核对；本地下载受站点限制，避免引用其
未逐页复核的内部引理。

### A4. Brunetti--Trevisan (2026): unbalanced limit-point completion

**主定理。** 文章表明，限制到 unbalanced signed graphs 仍能得到 signed graph
spectral-radius limit-point line 的完整/相同极限点现象。

**证明链。** 以 unbalanced constraint 替换一般 signed graph 类 → 保留或重新
构造趋近序列 → 比较各类 limit points。论证重点是 family-level asymptotics，
不是给定底图上的 equality classification。

**对本文的一句话描述。** 它是当前 signed spectral-radius program 的最新
旁证，可用于 Discussion，不应挤占本文主要问题来源的位置。

**证据层级。** 官方 OA 页面与摘要层核对；本地下载受站点限制。

### A5. Kuchment--Vainberg (2006): local perturbation 的可局域化定理

**主定理。** Theorem 5 说明局部扰动的 periodic graph operator 在 band interior
出现 embedded eigenvalue 时，对应 eigenfunction 必为 compactly supported；
Theorem 6 给出更一般的紧支撑结论，并进一步讨论 quantum-graph 版本。

**证明链。** Floquet transform → fiber/Fermi-surface 的解析结构 → local source
项的 Fourier transform → 可除性与代数几何论证 → inverse Floquet transform
得到 compact support。文章的关键是把“局部扰动诱发的谱态”变成可控的有限支持对象。

**对本文的一句话描述。** 适合为 bulk-plus-local-defect 的直觉提供严肃背景；
当前稿的 finite-ring Evans matching 和 G6 gap state 仍须独立证明。

**证据层级。** 全文核对；宜放在 interface discussion，而非主定理引言。

### A6. Lin--Ning (2021): analytic tail + finite exceptions 的分类模板

**主定理。** Theorem 2 先处理 (n\geq17) 的 outerplanar maximizer；Theorem 3
随后给出全部 order 的完整结论，明确分离 small orders 与一个 exceptional
counterexample order。

**证明链。** 先将 extremal graph 约化为 edge-maximal outerplanar structure →
用 Rayleigh/Perron eigenvector estimates 把大阶候选锁定为 (K_1\vee P_{n-1})
→ 完成 (n\geq17) proof → 对 (n\leq16) 作有限分类与计算核对 → 汇总成
all-order theorem。小阶不是附录噪声，而是主分类的一部分。

**对本文的一句话描述。** 当前稿可借其节奏组织：先读懂 eventual theorem，
再看到 finite bridge 和 exceptions 如何闭合，而不是把 certificate 放在叙事中心。

**证据层级。** 全文核对；这是最重要的 JGT 写作结构参照。

### A7. Goedgebeur--Schaudt (2018): 先证明枚举完备，再报告计算结论

**主定理。** Theorem 7 证明 Algorithm 1 若终止，其输出恰好是目标
(k)-critical (H)-free graphs 的完整列表；其后 Theorems 8、10、13 将该
complete-generation contract 用于具体 finite classifications。

**证明链。** vertex-critical graph 的 deletion/coloring lemmas → 找到每个
target 必含的可逆 reduction → 从 smaller graphs extension 生成 → canonical
isomorphism rejection 消重 → Theorem 7 证明 soundness/completeness → 对
受限类运行枚举并把输出提升为定理。

**对本文的一句话描述。** 本稿的 finite-state quotient、canonicalization 与
exact certificate 应按同样顺序叙述：先说明所有 signings 为什么被覆盖，才让
机器计算承担最后的有限判断。

**证据层级。** 全文核对；适合作为 computer-assisted finite closure 的方法引用。

### H1. Bilu--Linial (2006): signing 的 two-lift 出发点

**主定理/猜想。** Conjecture 3.1 提出每个 (d)-regular graph 有小 signed
spectrum 的 signing；Theorem 3.1 给出一般最大度 (d) 图的较弱存在性界。

**证明链。** two-lift 的新特征值等同于 signed adjacency eigenvalues →
probabilistic signing 与 discrepancy/jumbledness estimate → 矩阵谱范数控制
→ existence result。其论证是“存在好的 signing”，不区分固定图上指定 candidate
的最优性。

**对本文的一句话描述。** 只用于一两句历史来源：本稿将 existence language
改为一个 non-bipartite fixed graph family 的 exact minimization language。

**证据层级。** 全文核对。

### H2. Marcus--Spielman--Srivastava (2015): interlacing family 的存在性闭合

**主定理。** 文章以 matching polynomial 的 real-rootedness/bound、
interlacing families 和 universal cover 比较为核心，证明 bipartite regular
graphs 存在 Ramanujan two-lifts，并由此构造无限 Ramanujan families。

**证明链。** matching polynomial roots → signed characteristic polynomials
的期望 → partial signings 形成 interlacing family → 至少一个 leaf signing
不超过平均多项式的最大根 → universal-cover bound → iterative two-lift
construction。谱对称性使 bipartite 情形的单侧/两侧控制兼容。

**对本文的一句话描述。** 作为反衬最有效：(C_n(1,2)) 非二分，故本稿不能
从一个 upper-edge certificate 自动得到 spectral-radius minimization。

**证据层级。** 全文核对。

## 6. 核心文章的写作结构比较

| 文献 | Introduction 起点 | Main theorem 位置 | 证明组织 | 对当前稿最可复用的部分 |
|---|---|---|---|---|
| Belardo et al. 2018 | general signed spectral questions | 多个问题条目 | survey synthesis | 先定义 fixed-graph signing problem |
| Brunetti--Stanić 2022 | signed spectral extremal quantities | 早期列出极值对象 | structural reduction plus switching extremizers | 量与优化域先说清 |
| Ghorbani--Majidi 2024 | complete signed graph family | 定理按 extremal quantity 组织 | negative-edge structure plus eigenvectors | 固定图族也可承载完整 extremal theorem |
| Hu--Liu 2025 | signed functional and Cayley context | 定义后集中陈述 | isoperimetry to spectral consequence | 从结构对象到谱结论的紧凑过渡 |
| Korotyaev--Saburova 2023 | periodic operator | Floquet setup 后 | fibers to trace to estimate | 把 flux/Floquet 放在 spectral mechanism 前 |
| Lin--Ning 2021 | conjectural classification | 很早 | tail to finite closure to synthesis | all-order classification 的节奏 |
| Goedgebeur--Schaudt 2018 | finite graph class | reduction 后 | completeness to enumeration | 先证明可枚举，再给计算结论 |
| Suvagiya 2026 | specific signed circulant | candidate formula 后 | coordinates to evidence to conjecture | 具体对象与 conjecture attribution |

## 7. 当前稿的引用方案

### 主文必须出现

1. Belardo--Cioabă--Koolen--Wang (2018)：fixed-graph signing 最小化问题。
2. Brunetti--Stanić (2022)：已发表 signed spectral-radius extremal
   classification。
3. Suvagiya (2026 preprint)：具体 \(C_n(1,2)\) conjecture。
4. Korotyaev--Saburova (2023)：periodic flux/Floquet 术语背景。
5. Lin--Ning (2021)：all-order analytic-tail plus finite-closure 结构。

### 建议主文或技术节保留

- Bilu--Linial (2006) 与 MSS (2015)：2-lift 由来和 bipartite contrast。
- Ghorbani--Majidi (2024)：fixed-family signed adjacency extremal analogue。
- Hu--Liu (2025)：non-bipartite Cayley context。
- Kuchment--Vainberg (2006)：local defect/interface context。
- Goedgebeur--Schaudt (2018)：completeness-first enumeration。
- Belardo--Brunetti (2024)：signed spectral-radius program。

### 可降权、移动或删除

- Zaslavsky (1982)：保留一次，限于 switching 基本记号。
- Cycon et al.：只在 IMS technical point 使用。
- Sawada (2001)：只在 bracelet/canonicalization discussion 或 supplement 使用。
- Davis (1979)、Kuchment (1993)、Fredricksen--Maiorana (1978)、Lam (1991)：
  不宜出现在问题重要性叙事；应删除、移入 supplement，或由更直接现代文献替代。
- Goedgebeur et al. (2024) 与 Goedgebeur (2020)：有更直接的 Lin--Ning /
  Goedgebeur--Schaudt 架构样本时可以退出主 bibliography。

## 8. 推荐的 Introduction 引用次序

1. Belardo--Cioabă--Koolen--Wang：fixed-graph signing optimization。
2. Brunetti--Stanić；可选 Ghorbani--Majidi：已发表 extremal signed
   spectral work及 fixed-family distinction。
3. Bilu--Linial 与 MSS：压缩说明 signing/lift 背景及 non-bipartite obstacle。
4. Hu--Liu：将对象放入 non-bipartite Cayley/circulant context。
5. Suvagiya：具体 flux、twisted candidate、conjecture。
6. 主定理与 nonmonotone truth pattern。
7. Korotyaev--Saburova、Kuchment--Vainberg：periodic bulk 与 local interface。
8. Lin--Ning、Goedgebeur--Schaudt：analytic tail 与 finite completion 的
   proof architecture。

## 9. Novelty 与引用风险

本次审计没有发现已发表工作处理同一个问题
\[
\min_{\sigma:E(C_n(1,2))\to\{\pm1\}}\rho(A_\sigma)
\]
并给出当前稿的 all-even classification。亦未发现已发表工作给出相同 twisted
truth set、\(n=32,40\) exceptions、\(n\ge48\) onset、period-eight reference
edge 或 G6 phase-slip mechanism。

这一结论的边界是：它基于精选种子、受控 citation chaining、出版社/arXiv/机构
元数据和本地已得全文，不是对世界文献库的绝对否定。最安全的 novelty wording
仍应是：To the best of our knowledge, no previous work determines, for every
even \(n\), whether a prescribed signing minimizes the spectral radius among
all signings of \(C_n(1,2)\).

## 10. 结论

文献综述的主结论不是已有很多 signed graph papers，而是已有三种互补的成熟
文献传统：

1. fixed-graph signing problem 与 signed spectral extremal classification；
2. periodic magnetic/Floquet graph operator 与 local perturbation；
3. all-order graph classification 与 proof-producing finite completion。

当前稿的贡献恰好位于三者交点：它把 fixed cycle square 上的 signing
minimization 升级为完整全阶分类，并用 period-eight bulk、elementary G6
interface 与 IMS localization 解释严格失败为何从 \(48\) 开始持续出现。
