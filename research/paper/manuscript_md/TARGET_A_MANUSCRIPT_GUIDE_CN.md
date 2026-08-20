# Target A 论文中文阅读指南

这份指南帮助作者理解 Markdown 稿件的数学主线，不进入投稿正文。正文中的
`R(Q)` 始终表示无限体积极限下的**谱半径平方**。

## 摘要

- **为什么存在：** 用一段话告诉审稿人论文否证了什么、最强结果是什么、哪些
  部分依赖计算。
- **核心结论：** 最小反例是 `n=32`；所有 `8|n, n>=32` 有显式反例；period-8
  sharp constant 为 `eta=4+sqrt(10+2sqrt(5))`；并有 period-8 完整结构分类、
  任意周期必要障碍和 primitive period `<=16` 唯一性。
- **主要证明思路：** Floquet + 精确多项式 + `A^2` 缺陷消去 + closed-walk moments。
- **计算依赖：** `n<=30` 最小性排除和 `p<=16` 完整分类。
- **审稿人可能质疑：** 是否误写成 all-period 结果；摘要已明确限定。

## 第 1 节：引言

- **为什么存在：** 建立 signed adjacency、switching 和 flux-phase 背景，解释原猜想
  的来源与论文贡献。
- **核心结论：** 正式陈述 Theorem A-F，并把三个不同优化域分开。
- **主要证明思路：** 先反例和无穷族，再从 squared operator 中提取结构机制。
- **计算依赖：** 引言只声明边界，不承担计算证明。
- **审稿人可能质疑：** 新颖性和 scope。正文只使用 2026-08-20 的有限公开状态复核，
  不写绝对优先权。

## 第 2 节：预备知识

- **为什么存在：** 一次性固定 `G_n,sigma,A_sigma,tau,Q,alpha,H_Q(z),R(Q),M_k,F_k`。
- **核心结论：** switching 不变性、有限 Floquet 条件 `z^L=alpha`、无限条件
  `|z|=1`、translation/reflection/edge-sign negation 和 zone folding。
- **主要证明思路：** 都是显式酉共轭或 fiber 分解；重复胞元按内部平移特征空间直和。
- **计算依赖：** 无，属于解析核心。
- **审稿人可能质疑：** finite 与 infinite Bloch 参数是否混用、odd cell 下 edge-sign negation
  是否漏掉 `z->-z`；正文均已显式说明。

## 第 3 节：最小反例

- **为什么存在：** 证明 `n=32` 不只是一个反例，而是最小反例。
- **核心结论：** `rho(A_32)^2<1561/200<rho_-(32)^2`，且 `8<=n<=30` 全部排除。
- **主要证明思路：** 对 witness 使用正文展示的 Floquet 多项式正系数展开；对阈值使用
  nested radical minimal polynomial 与 Sturm isolation；对较小阶使用完整 switching quotient。
- **计算依赖：** 完整有限排除是 computer-assisted；order-32 witness 是短 exact certificate。
- **审稿人可能质疑：** 17,929,600 states 如何覆盖 `2^31` classes。Appendix A 用
  `(Q,alpha)`、dihedral orbit size 和两个 `tau` lifts 证明覆盖。

## 第 4 节：周期构造与 Floquet

- **为什么存在：** 把孤立的 `n=32` witness 提升成无穷族。
- **核心结论：** 显式 `8x8` fiber、`z^L=alpha` 直和、quartic `P(y,c)`，以及统一
  `rho^2<1561/200`。
- **主要证明思路：** 从四条 lattice transitions 直接生成 `H(z)`；fraction-free determinant
  得到 `P`；在 `B=1561/200` 处做正系数展开。
- **计算依赖：** determinant 可由符号计算复核，但正文给出了完整矩阵和恒等式。
- **审稿人可能质疑：** 是否只对一种 holonomy 成立；uniform unit-circle 证明同时覆盖
  `alpha=+1,-1`。

## 第 5 节：精确 period-8 band edge

- **为什么存在：** 将方便的有理上界替换为 sharp constant。
- **核心结论：** `R=eta`，且唯一 band edge 是 `z=1`；正 holonomy 有限尺寸精确达到，
  负 holonomy 只趋近。
- **主要证明思路：** `c=2` 时 quartic 平移成 biquadratic；在 `(eta,2)` 处做 sharp
  positive expansion；再证明 top root 随 `c` 严格递增。
- **计算依赖：** 无有限枚举依赖。
- **审稿人可能质疑：** equality 是否还有其他 `z`；unit circle 上 `z+z^-1=2` 只可能
  `z=1`。

## 第 6 节：Eight-barrier

- **为什么存在：** 这是论文的结构核心，解释 target 为什么特殊。
- **核心结论：** 无 defect 时 `R=8`；两个 antipodal defects 时 `R=eta<8`；其余
  period-8 phase 全部 `R>8`。
- **主要证明思路：** `A^2` 的 odd displacement 全含 `1+Q_i`；低阶 moments 处理
  `d>=4`，exact longer moments 处理 separation 1,2,3，sharp Floquet theorem 处理
  separation 4。
- **计算依赖：** 三个 separation 的 exact closed-walk integers 是有限符号枚举；主要
  组合逻辑已完整写在正文。
- **审稿人可能质疑：** 是否错误使用 `F_k<=0 => R<=8`；正文只使用合法方向
  `F_k>0 => R>8`。

## 第 7 节：一般周期

- **为什么存在：** 将 period-8 现象提升为任意周期的必要条件。
- **核心结论：** `M1=4p`、`M2=20p+16d`、`M3=118p+168d+96a+48b`，并得到两个
  eight-barrier 必要不等式。
- **主要证明思路：** 用正文给出的整数动态规划递推枚举长度 2/4/6 的闭步词，将剩余
  `tau` 因子望远镜化成 `Q` 区间积。
- **计算依赖：** 430 个长度六闭步词的符号收集由递推和 checker 双重给定，公式推导和
  推论逻辑均在正文。
- **审稿人可能质疑：** `p=1,2,3,4` residue collision；Laurent 条目保留 multiplicity，
  cyclic identities 对短周期仍成立。

## 第 8 节：低周期前沿

- **为什么存在：** 说明 target 不只是 period-8 内最优，在一个更大且完整的有界域中仍唯一。
- **核心结论：** primitive `tau` period `<=16` 的唯一 minimizer 是 target。
- **主要证明思路：** 2626 orbit 完整计数；2611 个由 moment hierarchy 排除，8 个由 baseline
  lemma，5 个由 exact endpoint Rayleigh，2 个是同一 target 的重复胞元。
- **计算依赖：** orbit enumeration、moment hierarchy 和 5 个 residual certificate 是
  computer-assisted exact proof。
- **审稿人可能质疑：** radical squaring 是否选错分支；正文和 Appendix B 都先验证 `r>4`。

## 第 9 节：计算辅助验证

- **为什么存在：** 让审稿人知道机器到底证明了什么，而不是只看到“程序通过”。
- **核心结论：** 所有严格比较来自 rational、integer、Sturm 或 positive-definite certificates；
  regeneration 与 integrity replay 明确区分，并绑定到公开不可变 commit 和逐文件哈希。
- **主要证明思路：** 说明 quotient coverage、certificate coverage、fresh regeneration 和
  independent checker 的逻辑关系。
- **计算依赖：** 本节本身就是计算证据边界说明。
- **审稿人可能质疑：** 环境能否重建、较大阶 generator 是否完全独立。环境版本已锁定；最大
  三阶的 recordwise 独立性仍诚实列为 execution-trust boundary；Appendix C 已给出完整
  重生成命令、终端 chain hash 和实测时间/内存/磁盘。

## 第 10 节：讨论

- **为什么存在：** 将反例、结构机制和未解决问题放回同一数学图景。
- **核心结论：** 结果是 period-8 完整结构、任意周期必要条件和 bounded frontier，不是
  all-period theorem。
- **主要证明思路：** 本节不引入新证明，只解释已有结论的关系。
- **计算依赖：** 无新增计算。
- **审稿人可能质疑：** 是否把 open problems 写成暗示性结论；五个问题均明确标为开放。

## 附录 A-C

- **附录 A：** 给出 switching/flux quotient、Burnside 公式、canonical set equality 和最小性
  搜索覆盖证明。
- **附录 B：** 给出 18 个 period-8 orbit 表、5 个 residual vectors 与完整 rational comparison。
- **附录 C：** 给出 Python/package lock、仓库相对命令、slow audits、regeneration/replay 区别和
  negative tests。
- **最可能的质疑：** 计算证书是否可独立审计。附录的目标就是让审稿人无需相信数值 preview，
  只需检查有限整数/有理运算和覆盖恒等式。
