# C029 定理 1.1：从等长单元的对称性，到不等长单元的共同边界

研究日期：2026-10-05。对象：20 页第三版《Uniform Schur bounds for unequal cells in signed cycle squares》的 Theorem 1.1。本文给出研究后的叙事建议和原创英文草稿，**没有修改原定理，也没有把证明尚未覆盖的对象写进结论**。

## 直接参考的数学论文

以下是写法与问题组织的参考，不是声称它们已经证明C029定理1.1。全部精读版本与页码见逐篇案例。

1. Ai–Lei–Ning–Shi：*Graph operations and a unified method for kinds of Turán-type problems on paths, cycles and matchings*。读v2的§§1–3、§5选段、§6；[预印本全文](https://arxiv.org/pdf/2312.08226v2)；[CJM期刊DOI10.4153/S0008414X25101788](https://doi.org/10.4153/S0008414X25101788)。用于研究“共同机制怎样成为主角”。
2. Kim–Liu–Shangguan–Wang–Wu–Xue：*Stability with minuscule structure for chromatic thresholds*。读v2的§1.1、Theorem1.1、§§3–4及Lemma4.7；[预印本全文](https://arxiv.org/pdf/2506.14748v2)；[Peking Mathematical Journal DOI10.1007/s42543-026-00127-4](https://doi.org/10.1007/s42543-026-00127-4)。用于研究“怎样从数值转向结构”。
3. Chen–Rong–Xu：*Optimal stability results on color-biased Hamilton cycles*。读v2的§1、§2.1–2.2、§3；[全文](https://arxiv.org/pdf/2507.17739v2)；[arXiv DOI10.48550/arXiv.2507.17739](https://doi.org/10.48550/arXiv.2507.17739)。本次未核实期刊DOI；用于研究“怎样让证明路线具有因果”。
4. Naserasr–Pham–Pujol–Zhou：*Fractional balanced chromatic number and arboricity of planar (signed) graphs*。读v1的§1、§§3–5、Theorems13–16、Remark17；[预印本全文](https://arxiv.org/pdf/2505.16808v1)；[JGT期刊DOI10.1002/jgt.70047](https://doi.org/10.1002/jgt.70047)。用于研究“先显现局部障碍，再解释定量结果”。

完整七篇目录包含另外三个精确极值/等号案例：[目录及DOI](SOURCE_CATALOG.md)。这里的判断不以作者姓名推断族裔；机构按所读版本核实。

当前数学依据：[冻结v3主稿](https://github.com/whzy3185/math/blob/8ce218113ed07e3879ddc8bc157c7d32e77ad206/research/c029_holonomy_schur_20261005/manuscript_v3/manuscript.pdf)；[第六节精确拼接与二关联估计](https://github.com/whzy3185/math/blob/8ce218113ed07e3879ddc8bc157c7d32e77ad206/research/c029_holonomy_schur_20261005/manuscript_v3/sections/06_cells.tex#L104-L154)。

## 一、推荐的故事究竟是什么

推荐主线：**单元长度可以不同，谱控制却来自同一个边界结构。**

等长单元提供平移对称性，因而可以逐个 Fourier/Bloch 纤维研究谱。不等长之后，原来的单元平移不再适用。但定理 1.1 发现，对这些规定好的单元，完整对称性并不是统一上界所必需的：把内部消去后，每个保留接点汇合相邻两条链的响应，其对角块接近同一个正定的六维模型；剩余相互作用的大小由最短单元和每个边界的两次链端关联控制。单元再多，也不需要把误差按单元总数相加。

这段故事的美感来自两个真正的数学分离：

1. **全谱精确求解与统一谱上界可以分开。** 不再能使用相同单元的纤维分解，并不意味着统一控制也随之消失。
2. **局部长度与整体规模可以分开。** 长度决定边界响应的衰减；关联数决定这些响应怎样拼接。总单元数只增加矩阵维数，不进入已证明的误差上界。

这里不使用“无序系统”“任意扰动稳定性”“最优谱界”等说法。所有图仍然是有限环上的规定符号词；允许不同长度，不等于允许任意符号、任意局部缺陷或无限非周期算子。

## 二、先把不能被叙事改动的定理钉住

设

\[
 t=(1,1,-1,1,-1,-1,1,-1),\quad w_j=t^j\Vert(1,-1),\quad h_j=8j+2\quad(j\ge1).
\]

对任意正整数 \(r\)、任意 \(j_0,\ldots,j_{r-1}\ge1\)，取 \(\tau=w_{j_0}\Vert\cdots\Vert w_{j_{r-1}}\)，总长度为 \(N\)。在 \(C_N(1,2)\) 上，\(A_N(\tau,\alpha)\) 表示三角形符号为 \(\tau\)、Hamilton 环符号积为 \(\alpha\in\{\pm1\}\) 的规范化邻接矩阵。具体地，\(a_i=1\)（\(i<N-1\)）、\(a_{N-1}=\alpha\)，长度一的边符号为 \(a_i\)，长度二的边符号为 \(\tau_i a_i a_{i+1}\)，下标循环取值。

原定理给出两个严格不等式：

\[
\min_i h_{j_i}\ge106\ \Longrightarrow\ \rho(A_N(\tau,\alpha))^2<198/25=7.92,
\]
\[
\min_i h_{j_i}\ge202\ \Longrightarrow\ \rho(A_N(\tau,\alpha))^2<790537/100000=7.90537.
\]

两式均适用于两种 holonomy，常数与 \(r\) 无关，也不要求各长度相等。\(\rho\) 是最大特征值绝对值，控制两个谱端点。106 和 202 是当前证明给出的充分长度，未证明必要；两个谱帽是已认证的上界，未证明最优。

## 三、证明怎样产生故事，而不是让故事代替证明

### 1. 第一个障碍：等长纤维分解回答不了任意不等长拼接

第五节的 unit-phase 结论足以处理相同单元的任意重复，因为满足 \(z^r=\alpha\) 的纤维能组成直和。不等长拼接没有这个共同的单元平移。引言应明确这一失效位置，而不是含糊地说“现有方法存在局限”。这只是当前证明中的障碍，不是对整个文献作不可能性断言。

### 2. 换一个保留信息的方式

考察 \(cI-A^2\)；其正定性与 \(\rho(A)^2<c\) 等价。每个边界保留六个坐标，内部划为四点块链。不同内部之间没有耦合，所以它们的 Schur 修正可以相加。这里的消元不是丢弃顶点后的普通诱导子图，它保留了内部对边界的全部二次型影响。

### 3. 为什么不同长度仍然有共同对象

这些单元端部的符号完全相同，差别只在内部重复的次数。第四、五节证明同一开放 Riccati 轨道的收缩、两端响应衰减和累积边界项收敛。在**固定一个谱帽 \(c\)** 时，所有合法长链使用同一套极限响应；保留接点合并左、右相邻链的响应后，得到同一个 \(S_\infty(c)\)。它的正定性已经由种子与尾项估计证明，不是读者需要另行接受的假设。两个不同的 \(c\) 使用各自的有限前提；“共同”不能被误写成两个谱帽共用同一数值矩阵。

### 4. 真正值得放在引言中的一行计算

消元后得到 \(6r\) 维矩阵 \(\mathcal S\)。其跨边界项满足

\[
\left|2\sum_i\omega_i\langle v_i,F_i v_{i+1}\rangle\right|
\le \sum_i\|F_i\|(\|v_i\|^2+\|v_{i+1}\|^2)
\le2\max_i\|F_i\|\sum_i\|v_i\|^2.
\]

这不是不同误差符号恰好相消，而是**相对于总二次型质量的局部关联估计**。每一块恰被两条链端计入；\(r=1\) 的环计两次，\(r=2\) 的两条平行贡献都保留。因此短小计算确实覆盖每一个 \(r\ge1\)，没有把最小规模例外藏起来。

### 5. 为什么可以由局部正性得到全局结论

原稿证明

\[
\|\mathcal S-I_r\otimes S_\infty\|\le E_s,
\quad E_s=\frac{12b^2q^{2s}}{1-q^2}+576\delta\theta^s+32aq^s,
\quad s=\min_i s_i.
\]

于是最短链控制整个扰动。将这个量与已建立的局部正定余量比较，即得全体边界的正定性；再连同被消去的所有正定主元，经 Schur 合同恢复 \(cI-A^2\succ0\)。不能省掉“主元正定”，也不能把六维余量直接称为原始大矩阵的相同欧氏特征值间隙。

### 6. 精确计算应处于怎样的位置

有限有理数检验提供收缩与正性的有限前提，分析证明把这些前提推进到任意长度和任意单元数。这是有限认证辅助的数学证明。叙事上先解释为什么有限信息足够，再交代怎样严格验证它；不能写成“进行了很多测试，所以相信一般情形”，也不必让软件文件、运行次数和散列值占据摘要的中心。

## 四、三种可行叙事及取舍

### A. 对称性退场，共同边界留下（推荐）

组织参照：[S1，§2与§6](cases/S1_unification.md)的共同机制及边界；[S2，§1.1](cases/S2_structural_scale.md)的结构层次。

核心问题：当各单元不再等长时，哪些谱控制仍然成立？

标题候选：**Uniform spectral bounds for signed cycle squares with unequal cells**

优点：对象、困难、结论都具体；读者先理解两种统一性，再理解技术。证明中的共同极限与二关联估计恰好解开开篇问题。这里所谓“对称性退场”仅指等长单元的平移，不宣称这些有限环完全没有周期。

### B. 一个局部正定模型控制任意长的环

组织参照：[S3，§2.1](cases/S3_quantitative_stability.md)的因果路线；[S6，§§2–4](cases/S6_construction_and_limits.md)的局部约束先行。

核心问题：如何把单个边界的正定性传给任意数量的边界？

标题候选：**Boundary reduction and uniform spectral bounds for signed cycle squares**

优点：更适合希望先看矩阵机制的读者。风险：容易把六维矩阵写成抽象工程部件；必须先展示原来的图与符号词，并说明为什么这个模型是由图强制产生的。它可作为证明总览的副主线。

### C. 从精确周期解走向显式竞争构造

组织参照：[S6，§§3–5](cases/S6_construction_and_limits.md)的构造后果与方法边界。

核心问题：精确周期结构如何为更广的显式构造提供出发点？

标题候选：**Spectral bounds from periodic words in signed cycle squares**

优点：能连接后面的 one-cell 界和反例范围。风险：读者可能误以为旧见证范围是新贡献，或者把定理 1.1 降成一个用于补齐表格的技术工具。当前任务明确聚焦定理 1.1，因此不推荐将 C 作为主叙事。

**推荐组合：A 负责问题与结论，B 负责解答，C 只作为后续应用。** 不额外声称新的任意图拼接原理，除非将来真的单独证明它。

## 五、原创英文稿：可直接用于进一步修订

以下是候选文案，不是已经写回主稿的修订。英文有意保持节制，让反差来自数学事实。

### 标题

**Uniform spectral bounds for signed cycle squares with unequal cells**

相较现标题，删去标题里的 Schur，使题目先回答“什么对象上得到了什么现象”。Schur 仍应在摘要与证明总览明确出现；这是调整阅读顺序，不是掩盖方法。

### 聚焦主定理的摘要草稿

Periodic signings admit a spectral description in terms of a single cell. We study prescribed signings of cycle squares assembled from cells of unequal lengths, for which the equal-cell Fourier decomposition no longer applies. The cells consist of repetitions of a fixed period-eight triangle-sign word followed by a fixed two-sign ending. We prove that their squared adjacency spectral radius is less than 7.92 when every cell has length at least 106, and less than 7.90537 when every cell has length at least 202. Both bounds hold for either Hamilton-cycle holonomy and for every positive number of cells. The proof reduces each interior to its boundary response. At each of the two spectral caps, the diagonal block at each retained junction approaches a common positive six-dimensional matrix as its two adjacent cells become long, while the interaction estimate depends only on the two chain ends incident with each boundary. This separates the role of the shortest cell from that of the total number of cells. Exact rational inequalities supply the finite premises of the argument.

用途：以定理 1.1 为中心的摘要候选。它没有概括原稿其余全部定理，不能不经编辑判断就当作整篇稿件的最终完整摘要。

### 整篇论文摘要的兼容版本

We study prescribed signings of cycle squares assembled from cells of unequal lengths. Although the equal-cell Fourier decomposition no longer applies, eliminating the cell interiors yields a common boundary model. We prove squared spectral-radius bounds of 7.92 and 7.90537 when the shortest cell has length at least 106 and 202, respectively. The bounds hold for either Hamilton-cycle holonomy and for every positive number of cells: local response decay controls the length dependence, and two chain-end incidences at each boundary prevent the error from growing with the number of cells. The argument uses a contractive four-dimensional Riccati recurrence and exact rational finite premises. For the positive-holonomy one-cell family, the sharper bound holds at every admissible size, and the supremum is enclosed in an interval of width \(10^{-6}\). Together with the inherited period-eight family, the unequal-cell bounds and exact finite cases complete explicit competitors to the twisted signing at orders 32, 40, and every even order at least 48, recovering the previously known witness range. We include the inherited exact period-eight holonomy calculation and apply it to the revised global-optimality conjecture. The unrestricted minimum and its minimizing signings remain undetermined.

### 引言开头：六段及每段的责任

**P1：先给对象与可理解的问题。**

A periodic signing of a cycle square can be studied through a single cell and its boundary phase. This description makes the symmetry explicit, but it also ties the calculation to repetitions of the same cell. We ask what spectral control remains when the cells are allowed to have different lengths.

**P2：马上限定变化范围，不靠形容词扩张。**

Our cells have a fixed internal pattern and fixed ends. Write \(t=(1,1,-1,1,-1,-1,1,-1)\), and form \(w_j=t^j\Vert(1,-1)\), of length \(8j+2\). We concatenate any positive number of these triangle-sign words, with the integers \(j\ge1\) chosen independently. Thus the lengths may vary, while the local form of each junction is preserved. The Hamilton-cycle holonomy may have either sign.

**P3：把两个困难同时提出。**

Two uniformities are required. Cell lengths must be allowed to vary independently within a single concatenation, and the resulting errors must remain controlled when arbitrarily many cells are joined around the cycle. An estimate obtained by adding one error for each cell would lose precisely the second uniformity. The equal-cell Fourier decomposition does not handle independently chosen unequal lengths within the same concatenation.

**P4：给解决困难的数学句子，再引出定理。**

Both difficulties can be resolved at the boundary. After the interiors are eliminated, the diagonal block at each retained junction combines the responses of its two adjacent cells and approaches the same positive six-dimensional matrix at a fixed spectral cap. The remaining interactions join neighboring boundaries, so their quadratic-form estimate depends on two chain-end incidences at each boundary, independently of the number of cells. The shortest cell controls the local error; the cyclic incidence controls its assembly. Our main theorem makes this separation quantitative.

**此处接原定理 1.1，保持规范矩阵定义、全部量词、严格符号和两组阈值。**

**P5：定理后解释它实际增加了什么。**

The bounds are uniform in both the number and the lengths of the prescribed cells. They do not require the lengths to coincide, and they hold for both holonomies. The numerical caps are sufficient upper thresholds for these explicit signings. The assertion concerns the entire spectrum through \(\rho(A)^2\), rather than only its largest eigenvalue.

**P6：交代来源与后续地位。**

The period-eight calculation and earlier explicit competitors provide the starting point of the construction. The present result supplies a common analytic bound for the unequal-cell family. Together with the inherited period-eight family, the unequal-cell estimate and exact finite checks recover the previously established witness range. The positive-holonomy one-cell family admits a sharper completion. These consequences are presented after the uniform theorem, with the inherited constructions and formulas identified separately.

P6 对应原稿已有引用 EarlierPeriodEight、EarlierTargetA、C029Supplement。应沿用原稿冻结来源，不把它们换成下面用于学习写法的论文。叙事参考文献与数学依赖文献承担不同责任。

### 从相关工作转回主问题的过渡

Related signed-spectral problems place different demands on a proof. Kannan and Pragada bound the largest adjacency eigenvalue in terms of edge count, frustration index, and balanced clique number. Belardo and Brunetti study limit points of signed adjacency spectral radii. Here the signing words are prescribed, and the question is uniform control of both spectral edges under unequal cyclic concatenation. This leads us to compare boundary responses rather than to classify global optimizers or identify a limiting spectral radius.

这段应接原稿已有 Belardo–Brunetti 与 Kannan–Pragada 引用；它不把文献当作相同定理的先例。

### 证明总览：让每一步具有因果关系

We prove the theorem by testing the positivity of \(cI-A^2\). The prescribed ends of each cell allow us to retain six coordinates at every junction and eliminate the intervening four-site blocks. Their Schur complements follow one length-independent Riccati recurrence. A contraction estimate controls the pivots, and separate response estimates control what the eliminated interior contributes to its two ends. These estimates produce a positive limiting boundary matrix at each of the two values of \(c\).

For unequal cells, the finite responses are assembled before any limit is taken. Relative to a block diagonal sum of the limiting matrices, the diagonal errors are controlled by the shortest cell. The off-diagonal terms satisfy a quadratic-form bound in which each boundary is counted twice. Its constant is therefore independent of the number of cells, including the one-cell and two-cell cases. Positivity of the assembled boundary matrix, together with positivity of the eliminated pivots, then gives the spectral bound. Exact rational checks establish the finite inequalities needed to enter the contractive regime.

### 结尾的问题应从证明边界自然长出来

The argument suggests two distinct directions for refinement. One is quantitative: determine whether the sufficient length thresholds or the certified spectral caps can be improved for the same words. The other is structural: identify which changes to the cell endings still admit a common positive boundary model. The latter would require new local analysis; it is not a consequence of allowing the present cells to have unequal lengths. Determining the unrestricted minimum over all signings remains a separate problem.

这些是本研究提出的未来方向，不是声称文献已有的开放猜想；也不暗示数值常数一定能够改进。

## 六、同一内容怎样由说明书式排列改成数学文章

### 例一：不要以计算维数作为动机

当前摘要句：A four-dimensional Riccati recurrence with exact rational premises gives a common six-dimensional limiting boundary matrix, whose degree-two assembly error is independent of the number of cells.

建议展开：The lengths may vary, and the number of cells is unrestricted. Their endpoint responses have common limits: at a fixed spectral cap, the diagonal block at each junction combines the two adjacent responses into the same positive local model. Since every boundary meets two chain ends, the error is controlled locally rather than accumulated over all cells.

变化：先让读者知道要统一什么，再解释为什么统一成立。四维、六维仍保留在随后方法句；不存在通过省略技术条件来提高结论的行为。

### 例二：路线图不应只是目录

说明书式示例（本研究构造，不是原稿引文）：Section 4 introduces the recurrence, Section 5 proves estimates, and Section 6 handles unequal cells.

建议：Eliminating a cell interior replaces its length by a boundary response. The contraction estimates show that these responses share a common limit. A local incidence estimate then allows the finite responses to be joined without introducing dependence on the number of cells.

变化：每句的结论成为下一句的输入；读者可以在看到大矩阵之前理解证明为什么会结束。

### 例三：把数值写成问题的答案

薄弱写法示例：We obtain the bounds 7.92 and 7.90537 by exact computations.

建议：The common boundary model yields a spectral cap for every unequal concatenation once its shortest cell is sufficiently long. Two exact choices of the local inequalities give the explicit pairs \((106,7.92)\) and \((202,7.90537)\).

变化：数字解释“多长足够、能压到多低”；认证保留为严格性的来源，而不是全文的情节。

## 七、为何这能有数学美感

这里的“故事”有可检验的张力：一个原来依赖对称性的描述，遇到了破坏共同单元尺度的变化；新的观察不是恢复对称性，而是找到在变化中保持一致的边界量。读者先看到大矩阵的维数随 \(r\) 增长，随后看到控制常数不随之增长，最后理解是因为二次型只沿局部关联累计。这是证明内部已有的惊讶，不需要另造物理隐喻。

克制同样重要。Schur 补、Riccati 收缩、二次型估计本身都是标准工具；真正应当被突出的是这些规定单元具有共同正定边界，并且组合方式使估计同时摆脱长度差异和单元总数。不能把标准工具重新命名，就宣称发明一般理论。

详见 [参考案例](cases/README.md)、[跨案例比较](CROSS_CASE_COMPARISON_ZH.md)、[版本与阅读证据](evidence/READING_AND_SCOPE.md)。
