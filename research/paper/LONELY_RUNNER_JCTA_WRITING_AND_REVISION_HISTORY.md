# 《The four-speed Lonely Runner spectrum below 1/4》写作、审稿与修订全过程

> 项目：四速度 Lonely Runner 低谱精确分类 / JCTA 投稿准备  
> 目标期刊：*Journal of Combinatorial Theory, Series A* (JCTA)  
> 当前记录截止版本：**v1.17**  
> 当前记录日期：**2026-09-08**  
> 主要作者：Yaoyang Chen, Yicheng Zhao, Xiangjiang Zhou, Jiachen Li  
> 本文档用途：完整保存本项目从初稿、文献学习、结构重写、模拟审稿、数学补强、计算机辅助证明规范化到当前投稿稿件的全过程，便于后续作者复盘、返修、答审稿人以及继续开展相关研究。

---

## 1. 项目的最终目标与当前核心结果

本项目最终要解决的是四个不同正整数速度的 Lonely Runner spectrum 在 `1/4` 以下的完整结构。

论文当前核心结果可以分成三个层次。

### 1.1 精确谱

论文确定

\[
\mathcal L_4\cap(0,1/4)
=
\left\{\frac{s}{4s+1}:s\in\mathbb Z_{\ge1}\right\}
\cup
\left\{\frac{s}{4s+2}:s\ge5,\ s\text{ odd}\right\}.
\]

这不仅证明 denominator defect 只能为 `1` 或 `2`，还进一步确定哪些候选分数真正出现。

最典型的缺失值是

\[
\frac3{14},
\]

它虽然满足 denominator defect `2`，但并不属于实际四速度 spectrum。

### 1.2 全局逆结构定理

真正支撑论文档次的核心不是最终有理数列表，而是结构性逆定理：

\[
\operatorname{ML}(V)<\frac14
\quad\Longrightarrow\quad
V\text{ 中存在三个不同元素 }a,b,c\text{ 满足 }a+b=c.
\]

换言之，四速度配置一旦进入 `1/4` 以下的 near-tight regime，就必然产生加法结构。

这一步把一个连续动力系统 / torus orbit 的低谱条件，转化为一个离散整数加法关系，是整篇论文最重要的 conceptual contribution。

### 1.3 配置分类

在得到 additive inverse theorem 后，所有低谱 primitive configurations 被归约到结构化族，再由二维安全区域几何、边同余以及精确有限验证完成分类。

最终出现两个无限族以及一个孤立配置

\[
\{1,3,4,14\},
\]

但该孤立配置的 loneliness value `4/17` 已经落在主要谱序列中，因此它产生新的 configuration，而不产生新的 spectral value。

---

# 2. 初始阶段：目标从“证明结果”转向“写成 JCTA 论文”

项目最早的重点是数学证明本身。但在准备投稿时，很快暴露出另一个问题：即使数学结果成立，稿件的写法仍然容易被审稿人看成“技术报告”而不是成熟的组合数学研究论文。

最初关注的几个问题包括：

- 是否符合 JCTA 的论文形式与学术表达；
- 是否太像技术报告；
- 第一人称 `we / our` 是否过多；
- 章节过碎，证明像工作日志；
- 缺乏清晰的“问题—方法—结论”叙事；
- 文献引用是否准确、完整且必要；
- author information、贡献顺序及投稿声明如何处理；
- 计算机辅助证明应如何表述，才不会变成软件工程报告。

在作者贡献顺序上，项目早期已经明确：第一作者贡献最高，之后依次降低。之后的修改主要集中在数学和论文组织上，不再反复调整作者顺序。

---

# 3. 第一份重要参考：Fan–Sun 论文

我们重点学习了 Fan 与 Sun 的论文：

> *Amending the Lonely Runner Spectrum Conjecture*，*The Electronic Journal of Combinatorics*，2026。

这篇文章与本课题直接相关，因此不仅用来学习数学背景，也用来学习“如何讲故事”。

最重要的启发并不是排版，而是其章节逻辑：

1. 先介绍 Lonely Runner Conjecture；
2. 再收缩到 near-tight spectrum；
3. 说明已有 spectrum conjecture；
4. 给出反例 / 缺口；
5. 提出新的数学问题；
6. 单独集中呈现 Main Results；
7. 最后进入技术工具和主证明。

由此确定一个贯穿后续所有修改的原则：

> **论文不能按“作者做了什么”推进，而应按“数学问题还缺什么”推进。**

也就是说，不应该写：

> We next prove...  
> We then compute...  
> We now check...

而应该写成：

> The first relation alone does not determine the orbit. This leaves the following obstruction...  
> To rule out this possibility, a second independent relation is required.  
> The resulting two-dimensional constraint still contains infinitely many primitive directions, so a quantitative bound is needed.

这样下一条 Lemma / Proposition 是由上一段未解决的数学问题自然引出的。

---

# 4. 第一轮语言和叙事重写：v1.6 → v1.7

v1.6 是较早的投稿工程版本。第一轮系统修改形成 v1.7。

这一轮主要不是改数学，而是改“论文声音”。

## 4.1 降低第一人称

大量

- `We prove...`
- `We show...`
- `We now consider...`
- `Our construction...`

被改为由数学对象作主语：

- `Theorem ... establishes...`
- `The construction yields...`
- `The preceding identity implies...`
- `This reduction leaves...`
- `The following argument excludes...`

目标不是机械变成被动语态，而是让 theorem、lemma、relation、certificate、geometry 本身推动叙述。

## 4.2 Abstract / Introduction / Main Results 重写

Abstract 从流水账调整为：

> 问题 → 精确结论 → 结构定理 → 方法 → 有限验证。

Introduction 则重新安排为：

> Lonely Runner 背景 → spectrum refinement → 四速度缺口 → 本文主结果 → 方法概览。

## 4.3 初步确立论文主线

此时已经形成后来一直保留的证明核心：

\[
\text{low spectrum}
\Rightarrow
\text{short relation}
\Rightarrow
\text{second independent relation}
\Rightarrow
\text{rational two-plane}
\Rightarrow
\text{finite reduction}
\Rightarrow
\text{additive structure}.
\]

---

# 5. 章节压缩与背景扩充：v1.7 → v1.8

用户明确提出：

- 缩短章节数；
- 增加背景工作；
- Theorem 后不要再有括号式解释标题；
- 按 Fan–Sun 的章节逻辑进行组织。

因此 v1.8 开始将很多“步骤标题”合并。

原先类似：

- Forcing the first short relation
- Forcing a second independent relation
- From two short relations to an effective bound
- Excluding the non-additive branch

这种标题虽然描述准确，但仍带有“项目施工流程”的感觉。

修改方向变成较大的数学章节，并把真正的技术步骤留在连续正文里自然过渡。

同时 Introduction 增加 Lonely Runner 的经典背景、Diophantine approximation、distance graphs、flows、covering radius 等关联，但明确要求：

> 背景不是为了堆文献，而是为了说明本问题处在什么研究链条中。

Theorem / Lemma 后的括号式副标题，例如

> Theorem 2.1 (Exact four-speed low spectrum)

也被统一删除，改为简单的

> Theorem 2.1.

---

# 6. 对“技术报告味”的第一次彻底清理：v1.8 → v1.9

v1.8 虽然章节少了，但仍保留了大量类似：

- `Proof strategy.`
- `Role of computation.`
- `Relation-plane certification`
- `Computational verification`
- `Reproducibility`

以及文末：

- CRediT authorship contribution statement；
- Funding；
- Declaration of competing interest；
- Data and code availability；
- Generative AI declaration。

这些内容并非全部“不该存在”，但把它们直接放进 clean 数学正文，会让论文像提交材料 / 项目验收文档，而不是数学论文。

因此 v1.9 做了关键区分：

## 6.1 clean 数学版本

仅保留数学论文：

- 标题；
- Abstract；
- 正文；
- Acknowledgements（如需要）；
- References。

## 6.2 submission 版本

出版社明确要求的声明才保留在 submission version 中，而不污染 clean manuscript。

这一阶段开始形成一个长期原则：

> **数学正文和投稿元数据必须分开。**

---

# 7. 继续清除工程式 roadmap：v1.9 → v1.10

v1.9 仍有一些残留问题，例如 Main Results 后仍有：

> Section 3 develops...  
> Section 4 uses...  
> Section 5 then studies...

这种内容本质上还是“施工路线图”。

v1.10 进一步将其删除或压缩，让 theorem 后直接进入下一段数学逻辑。

同时：

- 合并过短的独立章节；
- 将 non-additive 分支并入 Fourier 结构部分；
- 引用最新四速度 / 多 runner 工作；
- 清理 verifier / certificate data / enumeration produces 等工程语气；
- 重新运行关键有限检查，确认数字没有因改写发生漂移。

到 v1.10 时，主体结构已大致稳定为：

1. Introduction
2. Main results
3. Fourier certificates and the non-additive case
4. Additive configurations
5. Concluding remarks

---

# 8. 第一次系统模拟审稿：v1.10 → v1.11

随后不再从作者角度修改，而是模拟 JCTA referee。

这一轮找到几个真正影响数学严谨性的点。

## 8.1 Abstract 中错误的 “Equivalently”

稿件曾把完整谱公式与

\[
q-4p\in\{1,2\}
\]

写成等价。

这是错误的，因为

\[
\frac3{14}<\frac14,
\qquad
14-4\cdot3=2,
\]

所以 defect condition 本身并不能排除 `3/14`。

因此改成：

> `In particular` / `Consequently`

并明确 `3/14` 的缺失来自完整分类。

## 8.2 relation-plane 论证太黑箱

原文从“两条关系”直接跳到“有限 plane + 290”，中间数学责任不够明确。

v1.11 补出：

- 候选 relation plane 如何定义；
- saturation 如何保证整数参数完整；
- strict rational safe point 如何产生参数界；
- 290 是有限证书产生的统一上界，不是最优性结论。

## 8.3 零长度 safe interval 例外

当 `(a,b)=(1,2)` 时，安全区间长度

\[
\ell(1,2)=0.
\]

因此不能直接使用

\[
c<\frac1{2\ell(a,b)}.
\]

v1.11 将该例外提前分离，并解释：

> `(1,2,3)` 的临界安全时间是孤立点，这正是它必须单独形成族的数学原因。

## 8.4 Proposition 3.3 的全局上界补足

此前只在局部阈值范围内求最大值，却没有先显式闭合

\[
\operatorname{ML}(u,v,u+v,u+2v)\le\frac14.
\]

v1.11 补上 safe triangles 在 `δ=1/4` 时退化的论证。

## 8.5 cleveref 类型错误

共享计数器导致 Lemma / Proposition 在正文中被错误显示为 Theorem。

这说明一个重要经验：

> **LaTeX 无 warning 不代表交叉引用语义正确。必须看最终 PDF。**

---

# 9. 标题体系、连续叙述和参考文献审计：v1.11 → v1.12

用户随后提出一个非常重要的写作原则：

> 除了 theorem / lemma 等正式数学环境，不要再大量创造 GPT 式小标题；上下文应该自然引出下一条定理。

因此 v1.12 做了两个大的方向调整。

## 9.1 标题尽量使用期刊真实先例

我们对照近期 JCTA 以及相关组合数学论文，确认常见且自然的形式包括：

- Introduction and main results
- Proof of Theorem ...
- Concluding remarks
- 以真正数学对象命名的 section

而不是：

- Proof strategy
- Role of computation
- Main observation
- Technical reduction
- Verification pipeline

这些更像网页回答或技术文档。

## 9.2 连续数学叙述

Section 中大量 subsection 被取消。

证明链改成：

> 第一条 relation 仍不足以约束 orbit，因此需要第二条独立 relation。  
> 两条 relation 虽然将配置压入二维平面，但平面中仍含无限多个 primitive directions，因此需要 quantitative safe-point argument。  
> 得到 bounded directions 后，再进入精确有限排除。

这个模式被作为后续写作的固定模板。

---

# 10. 参考文献体系重新审查

这一阶段不再追求“引用越多越完整”，而是追求“不重不漏”。

基本原则形成如下。

## 10.1 早期成果优先引用原始出处

例如 Wills、Cusick 的经典结果，如果正文说的是他们最初提出 / 证明的事实，应直接引用原始论文，而不是仅引用后来综述。

后续论文只有在承担不同信息时才同时保留。

## 10.2 与本文直接相关的工作必须充分说明

重点核对：

- Kravitz 的 spectrum formulation；
- Fan–Sun 的 four-speed sharpened conjecture；
- Jain–Kravitz 的 relative spectrum / finite symmetric difference；
- Liu–Zhu 对结构化四速度族的已有求值；
- Cordella 的近期 bounded computations；
- Fourier / Riesz-product 相关方法；
- Lonely Runner 的经典低 runner 结果。

## 10.3 Liu–Zhu 的定位变化

在追溯文献时发现 Liu–Zhu 早期已经研究与本文 family (B) 等价的参数族。

这迫使论文进一步精确区分：

> 参数族本身并不是本文新发现；本文新意是证明所有低谱四速度配置都必须全局落入这些结构族或指定例外。

这实际上强化了 Theorem 1.2 的重要性。

## 10.4 关于 “Taiwanese” 的核查

曾专门核查：大陆作者近期论文是否直接在参考文献中使用正式期刊名 `Taiwanese Journal of Mathematics / Taiwanese J. Math.`。

找到近期大陆机构作者论文中的直接实例，因此结论是：

> 正式刊名中出现 `Taiwanese` 不应成为删除或改写文献的理由；是否保留文献只应依据学术相关性。

---

# 11. 三项小修：v1.12 → v1.13

在第二轮 simulated referee 接近 “minor revision / accept” 后，v1.13 完成三个小修：

1. Liu–Zhu 作者版本差异的来源准确标注；
2. supplement 中 manuscript mapping 与当前 theorem numbering 同步；
3. 两处数学措辞变得可独立引用：
   - 连续实参数轨道明确写出；
   - Proposition 中 `u,v` 的 coprime hypothesis 放回命题本身。

随后又进一步决定：对 Liu–Zhu 的旧作者 revision 不应在正式正文中承担过多篇幅，后续版本最终只保留正式发表论文和 erratum。

---

# 12. 从“解释计算”升级为“加强数学结论”：v1.13 → v1.14

这是项目的一个重要转折点。

用户明确要求：

> 不要任何防御；缺数学结论就升级结论。

因此不再写：

> 为什么计算可信；  
> 为什么使用程序；  
> verifier 做了什么。

而是把有限计算背后的对象直接提升为正文数学结论。

## 12.1 第一关系完整分类

将第一 Fourier certificate 产生的所有 primitive absolute relation types 完整列为 23 类。

其中 `(0,1,1,1)` 是唯一直接强制 additive triple 的类型，non-additive 剩余 22 类。

## 12.2 第二 certificate 最小阶数

把原本“选择 `k=3,4,9`”升级为最小性事实：

- 20 类最小 `k=3`；
- `(1,1,1,2)` 最小 `k=4`；
- `(0,0,1,2)` 最小 `k=9`。

这样 `4,9` 不再像调参数得到的偶然常数，而是结构性 finite data。

## 12.3 rational plane 精确计数

有限关系对被升级为精确数学统计：

\[
83\,842
\to
37\,612
\to
37\,074
\to
6\,866.
\]

具体解释为：

- 83,842 个归一化独立关系对；
- 37,612 个不同 rank-two rational relation spaces；
- 538 个包含 forbidden relation 的核被排除；
- 37,074 个 admissible planes；
- 6,866 个 signed-coordinate-permutation classes。

## 12.4 290 的来源显式化

不再把 `290` 当作程序输出，而是展示 strict safe point certificate 如何给出参数界，并给出达到当前 certificate bound 的具体 plane / basis。

同时明确：

> `290` 是一个 sufficient uniform certificate bound，不主张最优。

## 12.5 有限分类精确计数

正文加入：

\[
\binom{290}{4}=288\,641\,640,
\]

其中 additive quadruples：

\[
5\,971\,776,
\]

non-additive quadruples：

\[
282\,669\,864,
\]

并全部有 `1/4`-safe time。

additive bounded region 则有：

\[
815\,970
\]

个参数 triples，恰好

\[
7\,149
\]

个无共同安全时间，其中

\[
7\,148
\]

个属于主二参数族，唯一剩余为

\[
\{1,3,4,14\}.
\]

---

# 13. 第二次重要数学纠错：v1.14 → v1.15

新的 simulated referee 指出一个明确概念错误：

稿件曾说两张 Fourier certificates “raise the rank of the relation lattice from zero to at least two”。

但完整关系格

\[
\Lambda(v)=\{r\in\mathbb Z^4:r\cdot v=0\}
\]

对于 primitive nonzero `v∈Z^4` 本身始终是 rank 3。

因此真正正确的 statement 是：

> 两张 certificate 强制得到两个线性无关、且 coefficients uniformly bounded 的整数关系。

然后定义它们的饱和张成：

\[
L(r,s)
=
\operatorname{span}_{\mathbb Q}\{r,s\}\cap\mathbb Z^4,
\]

这是 primitive rank-two sublattice，而 speed vector 落在

\[
L(r,s)^\perp.
\]

这一修正非常重要，因为它重新准确表达了论文真正的 inverse mechanism：

\[
\boxed{\text{shortness + independence}}
\]

而不是错误的 “rank raising”。

---

# 14. 把 finite search 变成 exact finite mathematics：v1.15

这一轮还加入了 finite endpoint principle。

对于速度 `v`，定义其 `1/4`-safe closed intervals 集合 `S_v`。

证明：若多个 `S_v` 的交非空，则某个连通分支的端点必来自有限 endpoint universe。

于是定义 `E_N`。

对

\[
t=p/q,
\]

令

\[
r\equiv vp\pmod q,
\qquad0\le r<q,
\]

则

\[
\|vt\|\ge1/4
\iff
q\le4r\le3q.
\]

这把 continuous safe-time verification 化成纯整数判定。

最终得到：

\[
|E_{290}|=34\,205,
\qquad
|E_{445}|=80\,381.
\]

这一步使 Proposition 2.10 / 3.2 从“跑程序”转成同一个数学有限判定原则的两次应用。

---

# 15. Supplement 从“程序包”升级为 proof package：v1.15 → v1.16

模拟审稿人指出一个关键 computer-assisted proof 风险：

> 验证 6,866 行 certificate 都正确，并不能自动证明它们覆盖理论生成的全部 6,866 classes。

因为理论上可能“重复一个类、漏掉另一个类”，数量仍然相同。

因此 v1.16 加入真正的 coverage equality：

\[
\{\text{generated canonical Plücker classes}\}
=
\{\text{certificate-table classes}\}.
\]

并实际验证：

- missing = 0；
- extra = 0。

## 15.1 generator / verifier 分离

Supplement 开始明确区分：

- 生成 relation planes；
- canonicalize Plücker representatives；
- certificate table；
- 独立 row verifier；
- non-additive box verifier；
- additive bounded verifier。

## 15.2 exact arithmetic

所有 proof-critical 判定使用：

- integer arithmetic；
- rational arithmetic；
- exact modular comparisons；

不依赖 floating point threshold。

## 15.3 运行信息

README 中加入：

- Python / C++ 版本；
- no randomness；
- 命令；
- expected outputs；
- runtime；
- peak memory；
- SHA-256。

但这些不放进正文，只留在 supplement。

这形成后来一直坚持的分工：

> **正文负责数学命题，supplement 负责执行与永久复核。**

---

# 16. 参考同方向 computer-assisted 论文，重新确定写法

我们进一步研究了 Rosenfeld、Trakulthongchai、Cordella 及 Fan–Sun 的相关写法。

得到一个非常明确的结论：

> Lonely Runner 方向大量使用 computer-assisted proof；计算机辅助本身不是问题，关键是先把它要验证的东西写成干净的数学命题。

## 16.1 Rosenfeld 型写法

先证明数学归约：

> 若某个有限模条件成立，则任何反例必须满足某个强制条件。

程序只验证有限条件。

## 16.2 Trakulthongchai 型写法

算法先表述为数学集合运算；真正的 C++ / runtime / hardware 放在后面。

## 16.3 Cordella 型写法

与本项目最接近：

> 理论结构 → 参数空间分解 → 少量 finite exact computation。

并明确区分：

- proof-critical computations；
- merely experimental / sanity-check computations。

## 16.4 我们采用的最终标准

> **正文风格学习传统组合数学论文；计算透明度学习现代 exact computer-assisted proof。**

因此不再新增：

- `Computer Verification` 大章节；
- `Implementation details` 工程式正文；
- `Reproducibility pipeline` 小标题。

而是：

> Proposition 明确有限数学结论；证明说明 finite exact verification；实现细节归档到 supplement。

---

# 17. v1.17：当前写作与数学结构进一步闭合

v1.17 主要根据最新审稿意见完成几项最后的数学与写作闭合。

## 17.1 Abstract 再压缩

不再同时列 saturated span、safe point margin、290 等全部技术词。

摘要只保留：

> exact spectrum → inverse theorem → two Fourier certificates → exact finite closure → additive classification。

## 17.2 Theorem 1.3 变成真正闭合的 classification theorem

family (B) 的严格低谱条件直接进入主定理：

\[
u-v\not\equiv0\pmod4,
\qquad
2u-v\not\equiv0\pmod4.
\]

不再在 theorem 中只说 family，然后等到后面 Proposition 才告诉读者哪些参数成立。

## 17.3 `H=7` 升级成正式引理

最终二参数谱可以写成

\[
\operatorname{ML}=\frac{H-1}{4H}.
\]

所有 odd `H≥5` 出现，唯一缺少 `H=7`。

因此

\[
H=7
\Longleftrightarrow
s=3
\Longleftrightarrow
\frac3{14}.
\]

这使 `3/14` 的排除成为结构性的 arithmetic obstruction，而不是计算“没搜到”。

## 17.4 Fourier certificate 的设计动机进一步突出

第一 certificate 被解释为同时服务于：

- negative orbit average；
- zero constant term；
- bounded Fourier support；
- parity-controlled coefficient signs。

第二 certificate 则服务于：

- 已知 relation line 总贡献变正；
- 整体 orbit average 仍负；
- 因此必须存在一条真正独立的 negative-coefficient relation。

这是论文中最有原创性的技术思想之一。

---

# 18. 当前数学证明链的最终形态

截至 v1.17，Theorem 1.2 的证明可以概括为：

\[
\operatorname{ML}(V)<\frac14
\]

\[
\Downarrow
\]

第一 Laurent-polynomial Fourier certificate

\[
\Downarrow
\]

一个 coefficients uniformly bounded 的 primitive integer relation

\[
\Downarrow
\]

第二 Fourier certificate

\[
\Downarrow
\]

第二条线性无关的 bounded relation

\[
\Downarrow
\]

primitive saturated rank-two short-relation lattice

\[
\Downarrow
\]

有限多个 rational speed planes

\[
\Downarrow
\]

strict rational safe-point geometry

\[
\Downarrow
\]

primitive speed bound

\[
v_{\max}\le290
\]

\[
\Downarrow
\]

exact finite endpoint verification

\[
\Downarrow
\]

所有 non-additive configurations 被排除

\[
\Downarrow
\]

\[
\boxed{a+b=c}.
\]

这一链条决定了论文不是“2.8 亿 brute-force 搜索”，而是：

> **结构性 inverse theorem + exact finite closure。**

---

# 19. 当前 additive 分支的最终证明链

得到

\[
V=\{a,b,a+b,c\}
\]

后：

1. 证明 `gcd(a,b)=1`；
2. 把前三个 runners 的 safe region 识别为二维 triangle；
3. 计算 orbit chord 与最长 safe-time interval；
4. 得到第四速度的粗界；
5. 从三条 triangle edge 上的 modular progressions 得到
   \[
   c\equiv ma\pmod b,
   \quad
   c\equiv nb\pmod a,
   \quad
   c\equiv ha\pmod{a+b},
   \]
   且 `|m|,|n|,|h|≤2`；
6. 大参数下由 CRT + size bound 得
   \[
   c=ma+nb,
   \]
   并只剩六种可能；
7. 排除 doubled cases；
8. 剩余大参数全部重参数化为
   \[
   \{u,v,u+v,u+2v\};
   \]
9. 有界剩余 exact classification；
10. 处理唯一 sporadic configuration
    \[
    \{1,3,4,14\},
    \qquad ML=4/17;
    \]
11. 对 family (A)、family (B) 求精确公式；
12. 用 modulo 4 residue classification 得到完整 spectrum。

---

# 20. 计算机辅助内容是如何被重写的

本项目对 computer-assisted proof 的写法经历了明显变化。

## 20.1 最早不理想的状态

容易写成：

> The verifier checks...  
> The program enumerates...  
> The certificate data show...  
> Computational verification...  
> Reproducibility...

这使数学论文像软件工程报告。

## 20.2 中间阶段：减少工程语气

首先删除独立的：

- Proof strategy；
- Role of computation；
- Computational verification；
- Relation-plane certification；
- Reproducibility。

但仅删除标题还不够，因为数学责任仍可能黑箱化。

## 20.3 最终阶段：把计算转成数学有限命题

### Plane 部分

计算对象是：

- finite set of short relation pairs；
- rational relation planes；
- Plücker canonical classes；
- strict safe-point certificates。

### Box elimination 部分

通过 endpoint lemma 先证明有限化，再定义：

\[
B_v\subseteq E_N,
\]

其中

\[
t=p/q\in B_v
\iff
q\le4(vp\bmod q)\le3q.
\]

于是配置安全性就是 finite set intersection。

### Supplement

只有 supplement 才记录：

- CSV；
- C++ / Python；
- bitset；
- runtime；
- memory；
- SHA；
- exact commands。

这最终形成一个重要方法论：

> **数学正文不能证明“程序跑了”，而应该证明“为什么只需要检查这个有限对象”；程序只完成最后一个完全定义的有限命题。**

---

# 21. 多轮模拟审稿的结论变化

整个项目并不是一次修改完成，而是不断以 referee 标准重新检查。

大致演变如下：

### v1.10 左右

判断：**Major Revision**。

主要问题：

- 贡献边界还不够精确；
- finite plane proof 太黑箱；
- Abstract 有逻辑用语错误；
- 若干边界条件和交叉引用问题。

### v1.11–v1.13

判断逐渐提升到：**Minor Revision / acceptance after minor revision**。

原因：

- 关键数学缺口补齐；
- 文献定位更准确；
- references 与 previous work 分界清楚。

### v1.14

数学内容进一步升级，但随后被发现 relation lattice rank 的概念错误。

这说明：

> “写得更强”必须同时经过数学语义审查，不能只追求 statement 更漂亮。

### v1.15

rank 错误修正；finite endpoint lemma 加入；计算证明更加数学化。

判断重新明显上升。

### v1.16–v1.17

重点从数学正确性转移到 publication-grade reproducibility：

- exact coverage equality；
- generator / verifier separation；
- explicit certificate data；
- deterministic exact finite checks。

当前模拟审稿总体判断：

> **数学上接近可接受，若 supplement 正式归档并可复现，则进入 Minor Revision / Accept after revision 区间。**

---

# 22. 写作上的长期经验：哪些东西以后不能再退回去

以下原则应当视为本项目的“禁止回退规则”。

## 22.1 不要重新加入 GPT 式小标题

避免：

- Proof strategy
- Role of computation
- Main idea
- Technical reduction
- Why this works
- Verification details

除非该标题在同等级期刊中有明确且合理的数学内容先例。

## 22.2 不要把 theorem 变成带营销副标题的形式

保持：

> Theorem 1.2.

而不是：

> Theorem 1.2 (The key additive inverse theorem).

重要性应由正文体现，而不是括号宣传。

## 22.3 不要用 `we` 驱动论文

优先：

> The first relation leaves...  
> The second certificate forces...  
> The safe triangle yields...  
> The congruence implies...

而不是：

> We now...  
> We next...  
> We then...

## 22.4 不要为了“纯数学”强行删除 exact computer-assisted proof

如果替代方案只是几十页人工 casework，论文可能反而变差。

真正值得升级的是统一结构定理，而不是把代码分支人工抄进正文。

## 22.5 不要把 supplement 的 QA 语言放进主文

例如：

- mutation testing；
- adversarial checks；
- runtime benchmark；
- memory usage。

这些可以作为软件质量保证，但不构成数学证明本身。

## 22.6 不要把“当前证书界”写成“最优常数”

尤其 `290`。

当前表述应始终明确：

> sufficient uniform certificate bound; no optimality is claimed.

---

# 23. 引用与 priority 的长期经验

## 23.1 直接相关工作必须明确区分

- Fan–Sun：提出 four-speed sharpened spectrum conjecture、发现 family；
- Jain–Kravitz：relative spectrum、finite symmetric difference；
- Liu–Zhu：早期研究结构化 family；
- Cordella：近期 bounded exact search，出现 `{1,3,4,14}`；
- 本文：global inverse theorem + exact classification。

## 23.2 不要把 bounded observation 写成 global prior result

特别是 Cordella 的结果应明确：

> bounded computational observation versus global theorem。

## 23.3 不要为了“完整”强行引用不相关论文

References 的标准不是数量，而是每一条都能回答：

> 它支持正文哪一句？  
> 它是否是直接前作？  
> 它是否提供 proof-used theorem？  
> 它是否承担历史来源？

如果都不是，应删除。

---

# 24. clean PDF 与 submission PDF 为什么分开

后期项目一直维护两个版本：

## clean PDF

用于：

- 作者审读；
- 导师 / 合作者看数学；
- 模拟 referee；
- 日常修改。

只保留数学论文内容。

## submission PDF

用于 Elsevier/JCTA 正式投稿。

仅在出版社明确要求时保留相关声明，例如 AI-assisted language / organization disclosure 等。

数学正文在两个版本中保持一致。

经验：

> 平时只改 clean source；投稿前再同步生成 submission version。

---

# 25. 当前 proof-critical finite data

截至 v1.17，关键数据如下，后续修改不能无意改变这些值。

## Fourier / relations

- first absolute relation types: **23**；
- non-additive first types: **22**；
- second-certificate least `k`:
  - 20 types: `3`；
  - `(1,1,1,2)`: `4`；
  - `(0,0,1,2)`: `9`。

## Plane reduction

- normalized independent relation pairs: **83,842**；
- distinct rational rank-two relation spaces: **37,612**；
- forbidden spaces: **538**；
- admissible spaces: **37,074**；
- signed-coordinate-permutation classes: **6,866**；
- coverage: **0 missing / 0 extra**；
- minimum certified margin: `1/28`；
- maximum safe-point denominator required: `17`；
- current uniform speed bound: **290**。

## Non-additive bounded elimination

- `|E_290| = 34,205`；
- total increasing quadruples `≤290`: **288,641,640**；
- additive quadruples: **5,971,776**；
- non-additive quadruples: **282,669,864**；
- uncovered non-additive quadruples: **0**。

## Additive bounded region

- `|E_445| = 80,381`；
- parameter triples: **815,970**；
- no common `1/4`-safe time: **7,149**；
- family (B): **7,148**；
- unique sporadic set: `\{1,3,4,14\}`；
- unclassified: **0**。

---

# 26. 当前论文最有价值的三层贡献

如果未来写 cover letter、response、报告或答辩，建议按以下层次强调。

## 第一层：结构性 inverse theorem

\[
\operatorname{ML}(V)<1/4
\Rightarrow
\exists a,b,c\in V,\ a+b=c.
\]

这是最重要的。

## 第二层：完整 primitive configuration classification

解释所有低谱 configuration 为什么只来自有限结构族及唯一 sporadic case。

## 第三层：exact spectrum

\[
\mathcal L_4\cap(0,1/4)
\]

被完整确定，并结构性排除 `3/14`。

Cover letter 不应只写：

> We prove `3/14` does not occur.

因为那会严重低估论文。

---

# 27. 当前仍需作者本人完成的事项

截至 v1.17，建议只剩少量外部 / 投稿事项，不再大改证明。

## 27.1 永久归档 supplement

将冻结后的 proof-critical supplement 上传到：

- Zenodo；或
- 学校机构 repository；或
- 其他具有永久 DOI / version 的归档平台。

应记录：

- DOI；
- release/tag；
- archive SHA-256；
- license。

不能由写作助手虚构 DOI。

## 27.2 作者最终核验

所有署名作者应最终确认：

- theorem statements；
- proof logic；
- computational outputs；
- references；
- author contribution；
- declarations。

## 27.3 投稿前只做“小修”

当前不建议继续大规模：

- 换章节结构；
- 改核心符号；
- 重写主证明；
- 为去计算而强行加入大量 casework。

后续修改应以：

- typo；
- reference metadata；
- permanent archive information；
- editor/referee 明确意见

为主。

---

# 28. 版本演化简表

| 版本 | 主要变化 |
|---|---|
| v1.6 | 较早投稿工程；数学内容已有，但叙事偏技术报告 |
| v1.7 | 第一轮客观化语言；重写 Abstract / Introduction；降低第一人称 |
| v1.8 | 压缩章节；增加背景；删除 theorem 括号副标题 |
| v1.9 | 清除 Proof strategy / Role of computation 等工程式标题；clean/submission 分离 |
| v1.10 | 继续删除 roadmap；合并章节；减少 verifier 工程语言 |
| v1.11 | 首轮 major referee 修复：逻辑等价、safe interval、plane proof、交叉引用等 |
| v1.12 | 标题体系按期刊实例重构；连续论述；参考文献深审 |
| v1.13 | 三项 minor fixes；Liu–Zhu 版本、编号映射、数学措辞 |
| v1.14 | 有限计算升级为数学结论：23 types、minimal k、plane counts、精确有限统计 |
| v1.15 | 修正 full relation lattice rank 错误；加入 endpoint lemma；Plücker formulation |
| v1.16 | 补 `t0=τ/g`；coverage set equality；完善 supplement verifier / archive metadata |
| v1.17 | 摘要压缩；Theorem 1.3 闭合；H=7 正式引理；计算正文进一步数学化 |

---

# 29. 对整个项目写作过程的总结

这篇论文的修改过程可以概括为四次“升级”。

## 第一次升级：从“证明材料”变成“论文”

主要解决：

- 第一人称；
- 流水账；
- 章节过碎；
- 缺少故事线。

## 第二次升级：从“技术报告”变成“数学叙事”

主要解决：

- Proof strategy / Role of computation 等小标题；
- 工程说明；
- 过量 roadmap；
- 主文与 submission metadata 混杂。

## 第三次升级：从“计算得到结果”变成“结构定理 + exact finite closure”

主要解决：

- relation types；
- short relation independence；
- rational plane finite classification；
- endpoint lemma；
- exact arithmetic。

## 第四次升级：从“结果可信”变成“proof 可永久复核”

主要解决：

- Plücker canonicalization；
- coverage set equality；
- certificate table；
- independent verifier；
- deterministic supplement；
- archive metadata。

最终形成的论文不再是：

> 做了一个很大的计算，所以 spectrum 是这些值。

而是：

> 两个 Fourier certificates 强制低复杂度算术结构；该结构把无限问题压到有限个二维格 / 子环面；几何进一步给出统一参数界；最后由 exact finite proof 完成闭合；随后 additive geometry 给出完整配置与谱分类。

这是整个项目从最初写作到当前 v1.17 最重要的变化。

---

# 30. 后续研究方向

如果未来继续做，而不是仅投稿，本项目已经自然产生几个研究方向。

### 30.1 统一 safe-subtorus theorem

能否对 primitive rank-two short-relation lattice 给出 intrinsic arithmetic criterion，保证其 speed plane 与 strict `1/4`-safe cube 相交？

如果能做到，可以部分甚至全部替代 6,866-plane certificate classification。

### 30.2 更高速度数的 inverse certificate method

第一 / 第二 Fourier certificate 的思想能否扩展为：

\[
\text{low spectrum}
\Rightarrow
\text{several independent short relations}
\Rightarrow
\text{low-dimensional rational subtorus}?
\]

这可能比直接计算更具有推广价值。

### 30.3 参数界最优性

当前 `290` 只是 certificate bound，不是最优值。

可以研究：

- 最小统一 bound；
- 是否存在纯几何 bound；
- 是否无需 finite box elimination。

### 30.4 additive branch 的纯解析有限消除

Proposition 3.2 是最可能进一步解析化的 finite part。

但是否值得取决于能否得到新的统一 lemma；不建议用大量人工 casework 仅仅为了删除计算机辅助。

---

# 31. 最后原则：停止无收益的大改

当前稿件已经经历多轮独立模拟审稿和数学复核。

接下来应坚持：

> **只有新的数学错误、新的真实 referee 意见、或者明确的 publication requirement，才值得改变证明结构。**

不要因为“还能写得更漂亮”而持续重构已经稳定的核心证明。

当前最重要的是：

1. 冻结 v1.17 数学正文；
2. 永久归档 supplement；
3. 作者人工逐页核验；
4. 准备 JCTA submission metadata / cover letter；
5. 正式投稿。

---

## 附：本项目最值得保留的一句话

如果未来需要一句话向编辑、审稿人或报告听众解释这篇论文的真正贡献，建议使用：

> **The proof converts a near-tight dynamical obstruction into bounded arithmetic rigidity: two Fourier certificates force two independent short relations, which reduce all low four-speed configurations to finitely many rational planes; this global reduction leads to the additive inverse theorem and hence to the exact four-speed spectrum below `1/4`.**

这比单独说“排除了 `3/14`”更准确地体现论文的数学价值。
