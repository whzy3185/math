# Open Status Audit — Round 1

审计日期：2026-08-14

输入：[`RAW_CONJECTURE_SURVEY.md`](RAW_CONJECTURE_SURVEY.md)
原则：本文件中的“高可信开放”只表示在本轮公开检索范围内未发现解决，并且最新原始来源仍明确把它列为猜想/问题；它不是对不可见或未索引文献的绝对断言。

## 检索协议

对每一项执行或组合执行以下检索：猜想名称/编号、原论文标题、作者名加 `conjecture`、核心术语加 `proof` / `counterexample` / `disproof` / `false`、arXiv 版本和最新同题工作。优先检查 arXiv 原始页和 PDF；2025 年来源另做 exact-title 搜索以降低一年内后续工作遗漏风险。

本轮可复核的关键原始证据包括：

- [signed circulants 原始页](https://arxiv.org/abs/2607.18334)：仍称全偶数阶结论为 conjecture，并明确只穷举 `n=8,10,…,18`。
- [Promislow group 原始页](https://arxiv.org/abs/2607.18346)：明确写明“14 是否为全群最小值仍开放”，同时该论文已经专门研究最小见证。
- [AP-intersection 原始页](https://arxiv.org/abs/2607.23004)：只无条件确定 `N≤12`，一般公式仍为 conjecture。
- [Latin squares 原始页](https://arxiv.org/abs/2607.17547)：构造范围留下 `n=30` 与大阶证明缺口。
- [zero forcing 原始页](https://arxiv.org/abs/2511.16335)：明确称 fast-join 刻画为 conjectures，仅证明 joins 等情形。
- [unique domination 原始页](https://arxiv.org/abs/2511.01719)：只证明 `γ=2` 与 `n=3γ`。
- [Kneser xor-power 原始页](https://arxiv.org/abs/2510.01509)：一般指数仍为 conjecture。
- [rational-base normality 原始页](https://arxiv.org/abs/2510.11723)：仍以 conjecture 提出，并说明与多个长期问题的蕴含关系。
- [Hamiltonian bicirculants 原始页](https://arxiv.org/abs/2510.23420)：只给 partial verification 与显式覆盖范围。
- [Schur log-concavity 原始页](https://arxiv.org/abs/2509.22648)：只证明若干增长方向，主命题仍为 conjecture。
- [asymmetric induced saturation 原始页](https://arxiv.org/abs/2606.24763)：明确称 deletion-normal 一般命题为 conjecture，并验证至 6 顶点。

## 分类汇总

| 类别 | 数量 | 含义 |
|---|---:|---|
| A | 39 | 截至审计日，高度可信仍开放；有最新原始来源和未解决范围证据 |
| B | 4 | 状态或命题边界仍不够清楚，禁止直接写“open” |
| C | 0 | 本轮未发现已经解决的主表命题 |
| D | 0 | 本轮未发现主表原命题已有反例；若只对放宽版有反例，保留在 A 并注明 |
| E | 1 | 已有论文专门研究最小反例/最小见证 |
| F | 6 | 问题过宽、分类型或文献价值相对低，不优先进入攻击阶段 |

## 逐项审计

| ID | 类别 | 证据与判定 | 后续动作 |
|---|---|---|---|
| C001 | F | S01 新提出的参数分类问题，但不像单一可证伪命题。 | 仅作为 C004–C006 的辅助。 |
| C002 | A | S01 在完成 total-regularity 后仍明确列为 Problem 5.2；2026-08-12 新稿。 | 保留。 |
| C003 | F | “随直径增长的下界”未量化，存在多种不等价形式。 | 先形式化才可审计。 |
| C004 | A | S01 明确列为 defect-two 的下一开放问题，无解决稿命中。 | 保留。 |
| C005 | F | 存在性全分类过宽，不是单一反例目标。 | 拆为固定参数子问题。 |
| C006 | F | 依赖 C004–C005，且“影响答案”语义宽。 | 不进入 Top 20。 |
| C007 | F | 任意模式集的“必要充分条件”是研究纲领，不是边界清晰猜想。 | 仅作背景。 |
| C008 | F | 同 C007；可计算但目标过宽。 | 仅作背景。 |
| C009 | A | S03 在 2026-08-01 明确为 Question 6.4，并给上下界而非解答。 | 保留，但反例路径弱。 |
| C010 | B | “分类全部 Cayley 图”范围过大；S04 解决 normal 子类的一批情形，其他后续脉络尚未完全追踪。 | 标记 `UNVERIFIED OPEN STATUS`。 |
| C011 | A | S05 明确称 Dress Conjecture，证明 cofactor 类比及等价性而未证明本身。 | 保留。 |
| C012 | A | S05 明确称 long-standing Whiteley conjecture，并与 C011 等价。 | 保留。 |
| C013 | A | S05 只证明 cofactor 版本，原 R³ body-pin 命题仍为 Conj. 7.6。 | 保留。 |
| C014 | A | S05 证明 edge-transitive 特例；5-connected 版有反例但 6-connected 版仍列为 Conj. 9.1。 | 保留，边界攻击优先。 |
| C015 | A | S05 说明 4-connected 加强版为假，但 6-connected 版仍为 Conj. 9.2。 | 保留。 |
| C016 | B | 原问题是求最优常数，S06 推进下界；需单独核对所有并行改进稿的当前纪录。 | `UNVERIFIED OPEN STATUS`。 |
| C017 | A | S07 明确说一般 oriented graph 情形仍开放，同时列出 tournaments 等已证特例。 | 保留但经典难度高。 |
| C018 | A | S07 新提出加强版且未声称证明。 | 保留。 |
| C019 | A | S07 单列 tournament 加强版并说明旧证明方法不适用。 | 高优先可计算候选。 |
| C020 | E | S08 本身就是最小 non-UP 集研究；精确球内搜索已到半径 6。 | 不把“研究最小反例”包装成无人涉足。 |
| C021 | A | S08 明确以 Conj. 6.4 提出，随机/结构证据不能替代证明。 | 保留，可先寻找半径界反例。 |
| C022 | B | S09 证明 edgeless case和 point-determining case，但一般“所有图”仅以 suspect 表述；后续引用未完全审计。 | `UNVERIFIED OPEN STATUS`。 |
| C023 | A | S10 证明弱 stress-flex conjecture，随后明确提出 Strong Conj. 6.1。 | 保留。 |
| C024 | A | S11 v3 明确剩余 `6≤Δ≤32`；最新版本仍未关闭该窗口。 | 高优先。 |
| C025 | A | S12 无条件只验 `N≤12`，一般公式仍明确为 Conj. 1.3。 | 高优先。 |
| C026 | A | S12 明确把 kernel question 作为唯一剩余核心。 | 与 C025 合并研究。 |
| C027 | A | S13 明确构造/证明范围并留下 `n=30`、大阶 transversal 证明缺口。 | 高优先。 |
| C028 | A | S13 明确列 Question 1，未知参数集中在 `n≡3 mod 4`。 | 保留。 |
| C029 | A | 原始页仍为 conjecture；exact-title + counterexample/proof 检索只返回原稿，无后续解决。 | 最高优先；从 `n=20` 开始。 |
| C030 | A | S15 明确为 Conj. 4.4；原始页只声称 fence 情形结果。 | 最高优先。 |
| C031 | A | S15 明确为 Conj. 4.8；同上。 | 最高优先。 |
| C032 | A | S16 给出 `p=1/n` 等特例及 `p>1/3` 反例边界，`p≤1/3` 原命题仍为 Conj. 1。 | 保留。 |
| C033 | A | S16 仍以 MMS Conj. 2 引用，未声称一般证明。 | 经典高难，降低计算攻击优先。 |
| C034 | A | S16 新提出受限 MMS Conj. 3，并只证明其蕴含关系。 | 保留。 |
| C035 | A | S17 只验证 `k=1`，一般 `k≥1` 仍为 Conj. 1。 | 高优先，从 `k=2`。 |
| C036 | A | S18 明确只知有限多个偶圈 normal；一般 even-cycle 问题仍 wide open。 | 保留。 |
| C037 | A | S18 明确验证至 6 顶点并列为 Conj. 1.7；未发现后续反例。 | 最高优先，从 7 顶点。 |
| C038 | A | S19 仍称 conjecture，只证明 joins。 | 高优先。 |
| C039 | A | 同 S19；standard fast-join 刻画仍未闭合。 | 高优先。 |
| C040 | A | S20 只证明 `γ=2`、`n=3γ`；exact-title 检索未发现后续证明/反例。 | 最高优先。 |
| C041 | A | S21 明确 partial verification，给出 `m` 覆盖边界；检索未见一般解决。 | 高优先但首个未知规模较大。 |
| C042 | A | S22 v2 仍明确称 normality conjecture；数值实验不是证明。 | 保留，反例搜索只能发现有限统计异常。 |
| C043 | A | S22 明确把 `Z_{p/q}` 区间问题列为长期未决，并区分 `p>q²` 已知构造。 | 保留但高难。 |
| C044 | A | S22 证明与 C042 等价而未证明两者。 | 与 C042 合并，不单独占目标名额。 |
| C045 | A | S22 明确指出只在 `p≥2q−1` 已知，困难区仍为 Akiyama conjecture。 | 保留。 |
| C046 | A | S22 仍列 Dubickas `4/3` problem，并仅证明由 C042 推出。 | 保留。 |
| C047 | A | S23 原始页只给上下界，显式公式仍为 Conj. 1.2。 | 高优先。 |
| C048 | B | PDF 抽取文本为“固定 `ℓ,k` if `k` is large enough”，量词疑似 typo；摘要只明确猜“下界指数正确”。 | 先对照 TeX/作者版本，禁止直接编码。 |
| C049 | A | S24 明确列主 conjecture；放宽长度条件有反例，但主命题边界内未见反例。 | 最高优先，边界附近搜索。 |
| C050 | A | S25 明确为 Conj. 1；论文只证明复杂度和若干网络性质，exact-title 检索未见解决。 | 高优先。 |

## 结论

本轮没有发现可直接移入 C（已解决）或 D（原命题已有反例）的候选。该“零发现”不能解释为全局不存在相关结果；它只说明在 arXiv/公开网页的本轮检索中没有出现足以覆盖原命题的证明或反例。A 类可进入 Prompt 3；B 类必须先消除状态/量词歧义；E 类必须尊重已有最小反例研究；F 类不进入优先排序。
