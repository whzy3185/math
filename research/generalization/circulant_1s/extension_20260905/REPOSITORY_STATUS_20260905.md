# 仓库现状与交接基线（2026-09-05）

**后续整理补记：**用户已授权独立修复中英文结尾。纠错现已完成于
[`paper/period8-conclusion-correction` / `2dc5b90`](https://github.com/whzy3185/math/tree/paper/period8-conclusion-correction)，
两份PDF已重新编译。原冻结稿不变；下文“尚未修改”描述的是当时冻结
分支。全仓库新的入口、成果索引和过时覆盖见
[研究总览](../../../README.md)。本轮暂停新增数学探索，先完成整理和已知纠错。

供能够直接访问 GitHub 的网页端 GPT 阅读。仓库：
[`whzy3185/math`](https://github.com/whzy3185/math)。
**请切换到 [`research/circulant-1s-extension`](https://github.com/whzy3185/math/tree/research/circulant-1s-extension)
分支，不要以默认 `main` 分支或旧论文目录作为最新研究基线。**

本记录依据本地文件、Git 状态及已经执行的校验整理。它不代表本轮重新
逐行审计了所有历史分支。旧目录中的“PASS”“CLOSED”“100%”是工作
记录，数学正确性必须回到定义、证明和证据判断。

## 1. 两条当前主线

| 内容 | 分支／提交 | 当前处理 |
|---|---|---|
| 中英文 period-eight 文章 | `paper/jgt-authorial-rewrite`，`6766ecb` | 冻结；不由新探索修改 |
| 冻结标签 | `freeze/period8-jgt-2026-09-05`，指向 `6766ecb` | 已推送远端 |
| 一般 `C_N(1,s)` 推广 | `research/circulant-1s-extension` | 独立 worktree；继续研究的主线 |
| 首轮推广猜想 | `b8e971e` | C1–C4 原始记录，保留不改 |
| 首轮解析证明 | `29b63db` | 全偶跳长构造、平坦谱分类、chiral 判据 |
| 定量改进与文献边界 | `29773c3` | 多项式谱隙、有限比较阈值、Q6/Q7 开放问题 |

论文与推广在本地使用两个独立 worktree；网页端按上述 Git 分支区分即可。

冻结检查对象为 `research/paper_strengthening`、`research/paper` 和
`formal/TargetA` 的已提交树。推广 worktree 中这三个目录与冻结提交一致。
原论文 worktree 另有旧稿控制文档等未提交修改，未被覆盖或纳入推广提交。
其他 WorkBuddy、旧猜想审计等 worktree 本轮未重新审查，其独立状态不
应合并为本报告的完成状态。

## 2. 冻结文章的数学内容

令 `eta=4+sqrt(10+2sqrt(5))`。

| 结果 | 范围 | 证据状态 |
|---|---|---|
| period-eight 正 holonomy 精确半径 | 每个 `L>=1`，`rho(A*_(8L,+))^2=eta` | 稿件含解析证明与精确符号复核 |
| period-eight 负 holonomy 精确半径 | 每个 `L>=1`，平方半径为 `4+sqrt(8+2cos(pi/L)+sqrt(26-6cos(pi/L)))<eta` | 解析证明；不是新 Lean 声明 |
| 完整四条平方色散支 | `4±sqrt(8+c±sqrt(26-3c))`，`c∈[-2,2]` | 解析求解 |
| 八是首个 sub-eight 本原周期 | 仅步长 `(1,2)` 的合法周期符号 | 低阶矩、精确有限证书、周期重复不变性 |
| 八周期内 sub-eight 轨道唯一 | 合法八周期 `Q` 字、自然对称与 lift 约定 | 解析结构加小型精确整数递推 |
| 半胞 chiral 机制 | 步长 `(1,2)`、指定 `DT_m` 类 | 系数计算和通量等价 |
| twisted 严格比较 | `N=8L,L>=4`，正 holonomy witness | 原 Lean L1–L7 比较 kernel 覆盖 `alpha=+1` |

Lean 并没有验证新的一般跳长定理、负 holonomy 公式、完整新谱公式、
最小周期分类或本轮多项式谱隙。旧 kernel 的完整覆盖也不能扩大成
“本文全部数学均已 Lean 验证”。

## 3. 本轮发现：冻结稿结尾存在已可判定的错误问题

英文 `sections_en/07_conclusion.tex` 问：是否存在无限多个 `L` 使

\[
 m(C_{8L}(1,2))=\sqrt\eta.
\]

但 Section 4 已经证明，负 holonomy 的同一局部八周期相满足

\[
 m(C_{8L}(1,2))\le\rho(A^*_{8L,-})<\sqrt\eta
 \quad\text{对每个有限 }L\ge1.
\]

所以在引言“全部边符号极小化”的定义下，这个结尾问题的答案已经
是否定的，不能继续当作开放猜想。中文结尾有同一问题。

**影响：**这处矛盾直接涉及结论部分提出的后续问题；它本身不推翻
正 holonomy 精确半径定理或 twisted 反例族。它同时说明，之前“只剩
作者元数据”的完成报告过于乐观。

**处理：**按用户冻结要求，本轮没有编辑旧文。下一次解冻修订时应
改为询问负 holonomy 精确值能否达到全局最小，或研究全局最小值的
极限；这两种替代问法也仍需证据，不能直接宣布为正确猜想。

## 4. 推广主线的当前结果

统一记号：`N` 为有限图阶数，`s` 为第二跳长，`p` 为符号周期。
只考虑简单四正则图 `C_N(1,s)`，`2<=s<N/2`。

### A. 每个偶跳长都有显式 sub-eight 相

对每个偶数 `s>=2`，取本原周期 `4s`，定义

\[
 \tau_i^{(s)}=\begin{cases}(-1)^i,&0\le i<2s,\\
 -(-1)^i,&2s\le i<4s.\end{cases}
\]

其 Bloch 平方谱边 `R_s=max_(|z|=1)rho(H_s(z))^2` 严格小于 `8`。
证明路线是半胞 chiral 降维、四段链消元、固定八端点行列式、
Chebyshev 正生成函数和惯性连续性。

这是本仓库目前最值得继续审查、发展为升级主定理的部分。

### B. 谱隙与有限环的定量改进

最新解析推导给出

\[
 \frac1{2s^3}\le8-R_s\le4\sin^2\frac\pi{s+2}.
\]

因而 `R_s→8`。在 `N=4sL` 上，两种 holonomy 的新符号都严格
优于两种 alternating/twisted 符号，只需满足充分条件

\[
 L>\pi\sqrt{\frac{s(1+s^2)}2}.
\]

此处“两种”是对同一底图、同一 alternating 局部字的两种 Hamilton
holonomy 而言。该条件是保守充分界，不是精确首次失效阶数。

### C. 绝对下界及等号类

\[
 m(N,s)=2\iff N=2s+2;
 \qquad N\ne2s+2\Longrightarrow m(N,s)\ge\sqrt5.
\]

共邻点奇偶性证明必要性，Task 60 既有构造证明充分性。等号类由
alternating Hamilton 坐标刻画；`(8,3)=K_(4,4)` 单列为四阶 Hadamard
情形。谱半径二的一般符号图分类已有成熟文献，不能以此直接宣称
全新的普遍分类。

### D. 一般跳长的半胞判据

在 `2m` 周期、指定 `DT_m` 算子类内，所有 Bloch 相位上反对易等价于

\[
 \tau_{i+m}=(-1)^{s+1}\tau_i.
\]

等价地，`Q` 半周期，半胞通量积等于 `(-1)^(s+1)`。
奇跳长下普通二部图对称与指定半胞对称是不同陈述。

## 5. 证据与尚未证明的部分

上述推广有同一研究代理写出的解析证明和单独构造的精确计算校验；
没有外部独立数学审阅。不能把“不同实现的计算”写成“独立审稿人
验证”，也不能用有限检查代替无限参数的解析论证。

| 检查 | 已执行范围 |
|---|---|
| 八端点行列式 | 五变量符号恒等式 |
| 原 fiber 与 Chebyshev 公式 | 偶跳长 2–16；40 个精确相位案例，每例4个平方谱参数 |
| 原平方算子与链约化 | 同一40个精确案例 |
| 短字 chiral 条件 | 1,700个精确案例 |
| 小阶平坦谱分类 | 60,096个 Hamilton 坐标；阶数5–12 |
| 定量不等式链 | `r=2..24`，7个精确 `h`，共161例 |
| 行列式导数／逆迹 | 15个精确相位案例 |

尚未证明：

1. 是否总在 `z=1` 取得一般偶跳长族的最大谱边；
2. 是否 `s^2(8-R_s)→pi^2`；
3. 是否存在统一的 `c/s^2` 谱隙下界；
4. 一般跳长的最小 sub-eight 本原周期与该周期内刚性；
5. 奇跳长上是否能改善其自身 alternating 参考值；
6. 除平坦共振族之外的全部全局极小值和全部 minimizers；
7. 全偶跳长构造与既有周期算子文献的精确优先权关系。

数值上，`s^2 lambda_min(C_s(1))` 在 `s=16,64,256` 时约为
`8.3098,9.4457,9.7613`，接近 `pi^2`。这些是 `z=1` 的数值，
不是已经确定的全局 Bloch 谱隙，不能据此证明第1或第2项。

## 6. 网页端 GPT 的文件阅读顺序

下面链接相对于本文件所在目录，均指向本分支中的实际文件。

| 顺序 | 文件 | 阅读目的 |
|---|---|---|
| 1 | [首轮猜想记录](CONJECTURES_BEFORE_TESTS.md) | 确认原始 C1–C4 的量词与目标，不能把后来的结论倒填成原始猜想 |
| 2 | [全偶跳长主定理与完整证明](EVEN_JUMP_THEOREM_AND_PROOF.md) | 从原算子到所有相位的严格 sub-eight；这是最重要的数学文件 |
| 3 | [最新多项式谱隙证明](POLYNOMIAL_GAP_BOUND.md) | 最新定量结果；比上一文件的指数小下界更强 |
| 4 | [平坦谱分类与一般 chiral 条件](FLAT_MINIMUM_AND_CHIRAL_CRITERION.md) | 补充的一般结构结果及其文献边界 |
| 5 | [证明审查与范围](PROOF_AUDIT_AND_SCOPE.md) | 第一轮已检查的易错接口和未验证范围 |
| 6 | [定量猜想记录](QUANTITATIVE_QUESTIONS.md) | Q5 已有新证明；Q6/Q7 仍开放，注意记录先后顺序 |
| 7 | [首轮精确验证器](verify_extension.py)、[结果](EXACT_AUDIT.json) | 检查计算如何重建原矩阵、实际覆盖多少参数 |
| 8 | [定量验证器](verify_quantitative_gap.py)、[结果及数值线索](QUANTITATIVE_AUDIT.json) | 固定参数求导、逆迹、不等式链；区分精确测试与浮点证据 |
| 9 | [文献核查记录](LITERATURE_BOUNDARY_20260905.md) | 已检索内容与尚未确立的新颖性，不能把无搜索命中当作优先权证明 |

旧论文按需读：

- [冻结论文主入口](../../../paper_strengthening/manuscript_period8_jgt/main_en.tex)
  与[中文主入口](../../../paper_strengthening/manuscript_period8_jgt/main_zh.tex)；
- [冻结 theorem package](../../../paper_strengthening/final_theorem_package.md)；
- [两种 holonomy 的精确证明](../../../paper_strengthening/manuscript_period8_jgt/sections_en/04_period8_exact.tex)；
- [本次发现有错误问题的英文结尾](../../../paper_strengthening/manuscript_period8_jgt/sections_en/07_conclusion.tex)
  与[中文结尾](../../../paper_strengthening/manuscript_period8_jgt/sections_zh/07_conclusion.tex)。

一般跳长旧基础：
[Task 60 交接](../task60/TASK60_HANDOFF.md)、
[平方算子公式](../task60/TASK60_GENERAL_H2_FORMULA.md)、
[奇偶跳长的 alternating 色散](../task60/TASK60_TWISTED_DISPERSION.md)。
这些是已存在的基础工作，不应被重新包装成本轮新发现。

## 7. 建议网页端如何思考、接着做什么

请独立判断，不要因仓库写了“证明完成”就默认正确。每一步输出明确
命题、可核验推导和剩余缺口；如无法读取某个文件，要报告缺失范围。

1. **先查一致性和基本模型。** 核实第3节的冻结稿结尾矛盾；区分
   有限全局最小值、周期 Bloch 极值和不同 holonomy。确认 `tau` 与
   `-tau` 的谱关系不能从 `s=2` 无条件移植到奇跳长。
2. **独立审查一般主定理。** 从原算子重建 `4s→2s` 约化、边界相位和
   八端点矩阵；检查 Chebyshev 生成函数、系数正性及惯性连续性。
   尤其不能把正行列式直接当作正定，也不能以有限 `s` 的采样证明
   所有偶 `s`。先确认该定理，发现缺口则定位并修复。
3. **审查最新定量证明。** 检查 `q>=S^2/3`、`F_(r-1)<=rS/2`、
   固定 `h` 对 `y` 求导的合法性，以及 `tr(C^-1)=q_y/q<=14r^3`。
   明确损失一个 `s` 的位置；核对有限比较阈值的量词和常数。
4. **优先研究最有价值的锐化。** 先攻 `z=1` 是否总为最大相位，或
   建立足够强的统一相位估计；再研究 `s^2(8-R_s)→pi^2`。端点
   数值接近 `pi^2` 不能证明全局极限。可从高对角段消元得到低对角段
   的有效边界条件，目标是解释常数，而非只做拟合。
5. **进一步拓展只择一条。** 要么一般偶跳长的最小周期和首次刚性，
   要么奇跳长对其自身参考值 `M_s<8` 的真正改善。先提出精确猜想并
   尝试证伪；不要把“构造周期为4s”写成“最小可能周期为4s”。
   奇跳长仅证明 `<8` 不足以击败其 alternating 候选。
6. **最后做文献与文章判断。** 核查新构造是否是已知图族的同构重述
   或成熟算子定理的直接特例，再判断适合升级为一篇文章的主定理，
   还是与冻结八周期稿分成两篇。用户偏好 JGT 首投、LAA 备用，不能
   因这一偏好省略新颖性与证明难度判断。

初次接手不必读取庞大的旧 enumeration 目录或未重新审核的
R2/R4/R6/G6 项目。上述主线通过独立审查后，再按具体数学需要调用
历史成果。全局最小值、全周期分类和奇跳长全面推广都没有完成。

**回传本地研究时，请列出：**实际读过的文件；独立确认的命题；第一个
错误或缺口；新定理的完整证明或明确反例；未证引理；引用来源与读取
范围；建议下一步。不要只回传“总体成立”或没有推导的新猜想列表。
