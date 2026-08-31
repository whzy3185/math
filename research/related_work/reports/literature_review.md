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

## 5. 核心文章的写作结构比较

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

## 6. 当前稿的引用方案

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

## 7. 推荐的 Introduction 引用次序

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

## 8. Novelty 与引用风险

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

## 9. 结论

文献综述的主结论不是已有很多 signed graph papers，而是已有三种互补的成熟
文献传统：

1. fixed-graph signing problem 与 signed spectral extremal classification；
2. periodic magnetic/Floquet graph operator 与 local perturbation；
3. all-order graph classification 与 proof-producing finite completion。

当前稿的贡献恰好位于三者交点：它把 fixed cycle square 上的 signing
minimization 升级为完整全阶分类，并用 period-eight bulk、elementary G6
interface 与 IMS localization 解释严格失败为何从 \(48\) 开始持续出现。
