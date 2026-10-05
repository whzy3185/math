# math 仓库按时间顺序的变动说明

审阅日期：2026 年 10 月 5 日。仓库：`whzy3185/math`。本报告以本次固定的 23 个远端分支快照为依据，覆盖其共同根提交至 2026 年 9 月 15 日最新提交的可达历史。

## 结论

仓库最早形成文章规模的图论主线是 **C029／Target A：固定支撑 signed circulant 的最小谱半径问题**。它从候选猜想与反例搜索，发展成八周期谱机制、一般跳长推广，最终在 9 月 9 日分成“周期谱与渐近”和“有限全局极值”两篇独立论文方向。9 月 14 至 15 日又出现重要纠错，以及超越双缺陷构造的多缺陷方向。

与此同时，仓库保存了 F017 禁配置、四速度 Lonely Runner、Remark 3 乘积型 PDE、AML 生产消费稳定化等独立课题。它们不能拼成同一个图论项目。`main` 主要是入口和写作历史，只有 3 个可达提交、25 个文件，并未汇集其他分支的最新研究。

当前最需要注意的三件事：

1. **周期谱研究笔记已推进到 9 月 15 日，论文正文仍停在 9 月 9 日的版本。** 新的全类、多缺陷与正密度结果尚不能称为“已经整合成最终论文”。
2. **AML 最新分支不能标为 Lean 全绿。** 旧成功构建属于 `8af07749`；新增模块后的 `d46fa392` 构建失败，现有 HEAD `534c247d` 没有消除这条失败。
3. **历史上多次发生撤回、纠错与适用范围收缩。** 不能从 `FINAL`、`CLOSED`、`COMPLETE` 文件名或提交说明直接推断证明状态；关键修正见下文时间线和替代关系。

本轮是仓库历史和状态核查，没有启动新的数学研究，也没有重跑数学实验、Lean 或论文构建。以下“稿件证明”“记录通过”等表述均注明其证据来源，不等同于本轮重新认证。

## 阅读范围与日期规则

已完成的结构性覆盖：

- 23／23 个现存远端分支的固定提交及完整文件树，所有树均未截断；3 个现有标签均已解引用，目标都在本次可达提交集合内
- 39,001 条“分支—文件”记录，去重后 3,524 个路径、3,574 个 Git blob 版本
- 1,173 个去重可达提交，全部 parent 均在所取历史内；共同且唯一的根为 `fb4375f9588b558f162d7e3f6542c35b0056eea3`
- 对各主要研究线的入口、结论账本、真实证明稿、审计与撤回记录、代表性脚本、形式化工程和 CI 记录进行了交叉阅读

**这不等于逐字精读了全部 3,574 个文件版本，也不等于复核了每个提交的完整 diff。** 全量覆盖的是分支、文件树与提交历史；内容阅读聚焦于决定项目身份、数学范围、替代关系、当前缺口与实际验证状态的来源。二进制论文没有在本轮重新渲染；原日志和构建记录没有被当成本轮实际运行。

时间线按 Git `committerDate` 的 UTC 日期排序。作者日期另存于 `COMMITS.csv`；文档内日期与 Git 入库日期分列。最早文档记事可追到 **8 月 14 日**，但最早可见 Git 提交是 **8 月 15 日 05:45:17 UTC**。不能据此把 8 月初的聊天回忆定位成已经找到了对应 Git 项目。工作流文档署 9 月 14 日，但在 9 月 15 日提交。

本次范围不包括已经删除且不可达的远端分支、用户电脑上的工作树与未提交修改，或尚未定位到仓库的聊天附件。旧地图中提到的独立 poset／旧猜想分支以及 triangle-free／chromatic／Mycielski 包，须另行确认真实归档，不能擅自并入 Target A。

## 按时间顺序的主要变化

### 8 月 14 日文档记事与 8 月 15 日建库

初始材料先整理开放猜想、候选排序、研究目标和可复现搜索入口。8 月 15 日的 [根提交](https://github.com/whzy3185/math/commit/fb4375f9588b558f162d7e3f6542c35b0056eea3) 将这些材料写入仓库。早期目标中 C029 被选为 Target A，随后进入实质搜索；C040 和 C019 是候选／后备方向，不能从“出现在登记表”推断已经完成研究。

8 月 15 日 [冻结反例发现](https://github.com/whzy3185/math/commit/21d5b848ec6222e9cca8b263dcc9cd397b86b236) 后，仓库继续审计 switching／商空间枚举、bracelet 流式生成与独立验证。当天多条提交记录了 `n=24,26,28,30` 的穷尽检查，并在 [cd14e6ab](https://github.com/whzy3185/math/commit/cd14e6ab001a5321e95e2e4412e55c33cbbea5c6) 将 `n=32` 记录为 Target A 的最小反例，再独立重构 witness 和八周期 Floquet 行列式。这里的最小性属于当时明确限定的 Target A 模型和枚举覆盖，不是任意 signed graph 的全局断言。

### 8 月 16 日从单个反例转向八周期机制

[239ff8d2](https://github.com/whzy3185/math/commit/239ff8d206e88bbc7463863ad635bbf73e350791) 起的提交将 `n=32` 现象推广到八周期无限族，继续推导尖锐谱常数、flux 相位、闭游走障碍和低周期谱边界。其后增加新颖性与优先权检查、慢速复现记录及审稿前材料。

本阶段的变化是：研究对象由有限反例见证，转向能解释反例来源的周期结构和可复核证书。历史“复现通过”是仓库保留的记录；本轮没有重新执行这套计算。

### 8 月 20 至 21 日第一轮文章形成

8 月 20 日依次建立文章架构、Markdown 稿、经内部审阅修订的稿件、期刊格式 LaTeX 和中文稿；8 月 21 日补充计算核验、相关文献、数学定位与中英文同步。[1723787b](https://github.com/whzy3185/math/commit/1723787b334f893aee086141962994dc4fe96635)、[1f768806](https://github.com/whzy3185/math/commit/1f7688061071f736b801a2c007559d9525929fed)、[9d75ce04](https://github.com/whzy3185/math/commit/9d75ce04fd4509034ef65db50177d236f13479ab) 标记了这段过程。

这些是文章组织和审查材料的真实历史，不代表已经向期刊投稿、通过外部同行评审或获得接收。

### 8 月 22 至 23 日界面机制加强并发生秩修正

8 月 22 日研究扩展到双缺陷、phase slip、gap-six／gap-ten 界面态、有限环递推和较高周期精确前沿。8 月 23 日进一步讨论 G6 谱边、全偶阶族、fixed-r 激发计数和单间隙层级。

**8 月 23 日 [c26c18f9](https://github.com/whzy3185/math/commit/c26c18f9077f184b8a62684baf2feb1e099edccc) 是关键纠错节点。** 旧的 G6 exact-r／rank-one 叙述忽略了双重本征空间，需改用 `2r` 模式、余维 `2r` 及 `2r × 2r` Feshbach 体系。该修正撤回受影响的秩与计数论证；仓库仍保留独立支撑的全偶阶 `n≥48` 反例结果。不能把受修正的局部结论与保留的整体构造混为一谈。

### 8 月 24 至 25 日 JGT 稿与一般跳长分叉

8 月 24 日完成 Task 57、Task 58 的证明连接、稿件范围冻结、正文重写与内部审查，之后形成 `agent/target-a-discovery-snapshot` 的 [0ebfc7ba](https://github.com/whzy3185/math/commit/0ebfc7ba36c67fec5cb79bb9e515dcd3cb2c69c8) 快照。同日晚 [e9a17543](https://github.com/whzy3185/math/commit/e9a175438f3aac353f90f65a241e4829f555c0ed) 和 [bf1d75c8](https://github.com/whzy3185/math/commit/bf1d75c8545e8bec79ec39086a27aa9b61d412a2) 将 switching 代数与 twisted 构造推广到一般 `C_N(1,s)`。

这份 8 月 24 日稿件题为 *When Is the Twisted Signing of an Even Cycle Square Spectrally Optimal?*，记录的完整真假集合为：对偶数 `n≥8`，twisted 候选严格失去最优性当且仅当 `n=32`、`n=40` 或 `n≥48`。证明包结合精确有限分类、局部证书与 `n≥240` 的 IMS 尾部，有限 witness 衔接 `48≤n<240`。它回答“指定 twisted 候选何时最优”，没有求出失败阶数上的全部极小值，也没有分类所有极小 signing。

8 月 25 日在 `exp/circulant-1s-generalization` 上完善作者信息、图形与措辞，停在 [833face6](https://github.com/whzy3185/math/commit/833face614d2e9bda09d7d7112dc89f9a78b3555)。这些分支是后续主线的祖先，停在旧日期不表示研究丢失，也不表示其旧稿就是当前最强版本。

### 8 月 31 日至 9 月 2 日文献更新与解析闭合检查

8 月 31 日 `research/spectral-related-work-refresh` 重建谱图论相关文献和证明架构。9 月 1 日 `proof/complete-mathematical-closure` 对有限分类进行审计，启动以解析证明替换计算步骤的计划，并加入固定工具链的 Lean 基础工程。

9 月 2 日 `analytic-proof-first` 继续 Riccati、Schur 与 residue-two 尾部控制。**[11e1d23f](https://github.com/whzy3185/math/commit/11e1d23fead9e8b48a112dfa516c4d2cc983d9a6) 明确撤回了不完整的 residue-two tail 闭合声明。** 现有审计仍保留 `ANALYTIC_TAIL_MAJORANT_OPEN`；不能把早期计算辅助闭合标记改读成“无限尾部已经纯解析闭合”。

### 9 月 3 至 5 日八周期解析稿与结尾纠错

9 月 3 至 4 日形式化工程增加 Hermitian 性、Bloch fiber 与有限图本征值比较；[c1c4600c](https://github.com/whzy3185/math/commit/c1c4600c0f882edaf675742cbc6f620ce5e2d321) 冻结正 holonomy 的 period-8 形式化核心。它覆盖特定构造与比较，不包含负 holonomy 全部理论、任意 signing 的全局分类或后来的一般跳长主定理。

9 月 4 日文章进一步加强精确谱边、最小周期和半胞 chiral 机制，形成 `period8-paper-strengthening` 与 `paper/jgt-authorial-rewrite` 的双语稿。

9 月 5 日一般偶跳长结果与多项式谱隙得到更新。同时发现冻结稿结尾提出的 `m(8L,2)=sqrt(eta)` 无限成立问题，与同文负 holonomy 公式冲突；[2dc5b90d](https://github.com/whzy3185/math/commit/2dc5b90d3ef86dc81a304379154d1063273a3c93) 在独立 `paper/period8-conclusion-correction` 分支修正中英文结尾。**修正版并未自动进入所有后继研究分支。** 冻结原稿、纠错稿、当前研究导航必须分开读取。

同日 [d7f7ebea](https://github.com/whzy3185/math/commit/d7f7ebea5ddae11c8280cb311305edf1b712b247) 只为 `main` 新增导航，没有把整套研究合入默认分支。

### 9 月 6 日图论扩展与两个独立研究线并行

signed-circulant 主线继续谱隙、平坦极小值与共振阈值研究，走向 `research/quadratic-gap-upgrade`。其中 [3881fb8f](https://github.com/whzy3185/math/commit/3881fb8f31ea38da904efa1abca50fae96be79d6) 给出 `s=10` 的精确反例，以 `h=19997/10000`、`y=317/40` 的分离证书否定“Bloch 最大值必在 phase 0”。这使后续尖锐渐近必须处理全相位边界层，不能只检查端点。随后 [6d48b849](https://github.com/whzy3185/math/commit/6d48b849a1eff9e1385b3dfa4cf13cd26cc184e4) 统一所有 `s≥2` 的指定构造并记录 `s²(8−Rhat_s)→π²`；它仍不是所有 signing 的全局极值。

另一方面，`research/q1-discrete-full-push-20260906` 处理 **F017／`F(0,17,1,0)` 禁配置**。当天 [c8ec8e66](https://github.com/whzy3185/math/commit/c8ec8e66ad0af4a80783f90899901a141b72bdd8) 给出 Case 2、`r=6` 的删除成本论证，随后 [9e9f93b4](https://github.com/whzy3185/math/commit/9e9f93b4d17575004f352a1178174aaf06125c68) 推进 transitivity clique 与 Case 1。当前 `r=4,5` 仍未关闭，因而不能写成 `21m/2+1` 整体目标已完成。文档提及的 `case2_p17_r6_certificate.py` 不在该分支当前完整文件树中；解析计数论证与脚本可复跑性应分列。

同日，**四速度 Lonely Runner** 的独立 `lean-lonely-runner-ci` 分支进行了多轮编译修复，HEAD 为 [29fa62f1](https://github.com/whzy3185/math/commit/29fa62f117eca8fce2f503581533de22dac7a95e)。本轮查到该版本的 [`lake build` 成功日志](https://github.com/whzy3185/math/actions/runs/34035796801)，但其范围是部分系数／Laurent 证书与展开式模块，不能扩写成整篇数学主定理已经 Lean 认证。

### 9 月 7 日一般跳长与有限极值范围扩大

`research/quadratic-gap-upgrade` 在 [c986c038](https://github.com/whzy3185/math/commit/c986c03888129c30921e174993fbc3ee52bb86b6) 至 [9240e6f0](https://github.com/whzy3185/math/commit/9240e6f0fbc9c78f8ca82258b4bf30c669881719) 附近汇总 `N=3s` 阈值分类、一般跳长构造和谱隙加强。随后扩展到 Clifford Cartesian product、单位生成 circulant 与 lattice quotient 等方向。

本阶段须始终区分：指定周期构造的连续 Bloch 谱、有限 Fourier 采样，以及所有 signing 上的有限全局极小值。`Rhat_s` 的渐近不能替代 `m(N,s)` 的全局最优性。

当天 [bc6653a6](https://github.com/whzy3185/math/commit/bc6653a6699d09720eac56d85797bd68d00121c1) 与 [b8dda5ad](https://github.com/whzy3185/math/commit/b8dda5ad37197e0ec92062384a276839ac9cf670) 纠正 `s=2L` 的旧外推。研究转向有精确端点判据支持的 one-defect staircase，推进至 `L=19`；最后的临界比值探索仍含 Observed 层面的数值信息，不应由文件名升级为一般定理。

### 9 月 8 日 Remark 3 四分支与 JCTA 历史入库

**Remark 3 乘积型 PDE 是独立的分析课题。** 当天先有 [82c7863a](https://github.com/whzy3185/math/commit/82c7863a8b385a10da630aa7b57d4f7a043160a5) 的 polynomial-exponential 论文，再由 [d579b4f2](https://github.com/whzy3185/math/commit/d579b4f290881968c5b6011ae213b594645417f1) 保存 14 组符号检查及 13 页构建记录；v2 的 [f0ecf1cf](https://github.com/whzy3185/math/commit/f0ecf1cfee9b10b4cfb78a2002112dbc2a51d692) 增加不可约全方向分类、精确解数及 93 项检查；v3 的 [a981f618](https://github.com/whzy3185/math/commit/a981f618c368d957f076f8346ec79aefb8f1c6f0) 增加原坐标方向判据、最高齐次项障碍与泛型无解，另有 18 项检查。

并行的 `research/remark3-product-pde-20260908` 在 [57300701](https://github.com/whzy3185/math/commit/57300701ce0259485e3e5e28e3fe991a70170bd5) 保存双语稿、加权规范形和 31 项测试日志，但该分支声明测试程序通过外部 ZIP 交付，仓库没有对应完整测试源码。它不是 v3 的后继，不能仅按提交时刻把两个证明版本混合。

上述检查和页面数是原构建记录所载，本轮未重跑。各稿均未宣称 Lean 形式化或外部同行审定；与 Chen–Han 相关二维结果的关系以及 Xu–Ding 2026 近题论文的逐定理全文比对仍是新颖性边界。

同日 [c3e44609](https://github.com/whzy3185/math/commit/c3e4460929c38d10f0b3a0e878267142303c9675) 向 `main` 添加 Lonely Runner 的 JCTA 写作与修订回顾。它是回顾材料的入库时间，不是文中每个历史版本、证明和编辑事件的发生时间；记录中的“审稿”须区分内部模拟与真实期刊审稿。

### 9 月 9 日 circulant 拆成两篇独立论文

从综合重构分支 [cca0ea95](https://github.com/whzy3185/math/commit/cca0ea95730ee0130d403d90d8a8aa2781fdf138) 出发，研究明确拆成：

- `paper/circulant-periodic-gap-20260909`：周期 signing、连续 Bloch 谱、压缩、相位与渐近
- `paper/circulant-finite-threshold-20260909`：有限 `C_N(1,s)` 所有 signing 上的 `m(N,s)`、阈值与刚性

二者共享历史，但不是可以互相引用未发表黑箱的同一篇文章。固定周期全类分类也不能自动升级为任意有限图的全局分类。

周期谱正文最后一次修改是 [eadf1b17](https://github.com/whzy3185/math/commit/eadf1b17ef266be0fd84b65e217eb711970bf9fe)，时间为 **9 月 9 日 09:37:45 UTC**。之后大量研究笔记变化没有同步为该正文的新版本。

当天还形成 `skill/math-research-full-push-20260909` 的 v1 至 v5 方法整理，最终 [78e3ef8d](https://github.com/whzy3185/math/commit/78e3ef8da0d1a4125327dc2f579961fb9ec7e3b7)。这是一条工作方法与交付规范线，不是新增数学定理；其评估记录明确区分预期／重构评估与尚未实际执行的 benchmark。

### 9 月 9 至 10 日有限全局极值的分类加强

有限极值论文从原 twisted 候选是否最优的问题，转向真正的所有 signing 极小值。在仓库证明稿中：

- [23dcb234](https://github.com/whzy3185/math/commit/23dcb2344c942e672706036eff7a459e8c4598e4) 记录 parity-defect 三分法及 `m(4s,s)²=4+2cos(π/(2s))`
- [8d0da21c](https://github.com/whzy3185/math/commit/8d0da21ce057505e53da17162ac4f8ba6c8430fd) 修补严格低于 `sqrt(6)` 的分类论证；其对外部 signed 最小特征值分类定理的使用仍需单独审计
- [96bba9bc](https://github.com/whzy3185/math/commit/96bba9bc2a8feeccabcea93cd0e8bbc2ed8bb18b)、[bbe4d372](https://github.com/whzy3185/math/commit/bbe4d37269b4b08f734ee3c72aff2b6f0cf774c9)、[388da21e](https://github.com/whzy3185/math/commit/388da21e832db02039e8a7c35d78f69b37815d44) 汇总 `sqrt(6)` 等号参数 `(12,4),(16,3),(16,5),(20,8)`，switching 类数分别为 `2,32,32,2`，对称轨道数为 `1,2,2,1`；其中 16 阶部分使用精确有限穷尽证书
- [cc7a9677](https://github.com/whzy3185/math/commit/cc7a9677a39f5f780b96e2c3f33809632320e228) 用投影到奇环的 1-Lipschitz 行指标替代旧 seam-distance 论证
- [02494f4e](https://github.com/whzy3185/math/commit/02494f4ef5592bf1a809a1bbe703cd089f2f56de) 将奇数 `s≥7` 的 `N=3s` 平方谱半径障碍加强为 `8+24/1667`
- [bfad5b29](https://github.com/whzy3185/math/commit/bfad5b29130a997417f73173b4a8cc691fb863df) 记录 `m(5s,s)<sqrt(8)` 当且仅当 `s` 偶数或为不大于 13 的奇数；后续文档撤下此前 `k=5` 的旧开放项

这些是现有解析源与有限证书所支持的仓库状态；本轮没有重新运行枚举。它们说明有限论文已有超出 9 月 7 日汇总的实质进展，也说明 `N=7s` 仍应与已经记录完整阈值的 `N=5s` 分开。

### 9 月 9 至 11 日 AML 稳定化研究及 Lean 状态分离

[2216af9f](https://github.com/whzy3185/math/commit/2216af9f6e5b90b4a17024b22d2cf7fe8281071a) 建立 **AML 生产消费系统的质量加权稳定化** 课题。其后论文从具体系统推进到非线性质量加权 coercivity、二次／退化阻尼的速率分岔，以及有限 `L^p` 输入到强范数的迁移；9 月 11 日继续处理一维情形、边界条件和投稿格式。

这一阶段也有明确修正：[5e443d70](https://github.com/whzy3185/math/commit/5e443d7029f2c77c32b3d44a9d02219c58d8676c) 把 `F(v*)=0` 作为显式假设，撤回“区间端点的一侧耗散性自动推出平衡根”的推断；[bf761c72](https://github.com/whzy3185/math/commit/bf761c72d33b7f3f615f1742439e7d0d33a79554) 将主结果扩为非线性 q 阻尼，并把完整稳定化的输入由一致 `L∞` 界弱化为最终有限 `Lp` 界。尖锐性只针对信号衰减指数，不能扩写为全系统强范数阈值尖锐。

原论文状态文档将解析证明链标为已逐行检查，投稿清单记录 4 页 AML 格式构建；本轮只核查这些源文件及记录，未重新编译、重新证明或确认投稿已经发生。

**Lean 的实际状态与投稿清单不同：**

- 9 月 11 日 09:49:25 的 [8af07749](https://github.com/whzy3185/math/commit/8af07749fe733276054660a732bceaed8a86da4c) 对应 [run 290 成功](https://github.com/whzy3185/math/actions/runs/34586143612)
- 10:00:15 的 [d46fa392](https://github.com/whzy3185/math/commit/d46fa39226f282dc86187afc507d846556d7ff23) 加入 `BoxSignalGradientSupCore` 后，[run 292 失败](https://github.com/whzy3185/math/actions/runs/34587030868)
- 当前 [534c247d](https://github.com/whzy3185/math/commit/534c247d397ae4d522473f733c546e1b3ed28fe8) 为 15:22:17 的投稿清单提交，没有修复上述新增模块
- 当前根导入为 94 个模块；旧成功版本为 93 个，文档中的 92 个又是更早统计

失败具体涉及新模块第 47 行 `hs`／`aesop` 与第 80 行不存在的 `Real.sqrt_le_sqrt.mpr`。对旧成功提交到 HEAD 的差异核查表明，后续正式源码没有相应修复。

因此，旧成功证据不能覆盖当前 HEAD。成功版本本身也是实质性的部分形式化：一般光滑区域几何、完整 Neumann 半群平滑、Choi 局部有界性和若干强范数接口仍未在内核中全部导出，不能将 box 情形的条件性终点写成整篇一般区域论文已形式化。

### 9 月 14 日有限阈值推进与周期谱连续纠错

有限全局极值分支推进宽度七的 half-line 归约与 even-gap 障碍，并把 `N=7s` 的精确正例基底扩到每个奇数 `s≤29`，HEAD 为 [085ea698](https://github.com/whzy3185/math/commit/085ea698475b7b32e0ae57457ec903a922248f69)。这些结果要按各自参数范围阅读；有限已验证基底与任意参数分类不是同一个结论。

周期谱分支在同一天经历多轮实质修正：

1. [f7473d39](https://github.com/whzy3185/math/commit/f7473d3992d058714aba86c96260fa5e69d9db2e) 提出 antiperiodic-well 的普遍 phase-slip；[dfe1212f](https://github.com/whzy3185/math/commit/dfe1212f051c81c73b6a3f73b7e9393359b3386b) 撤回错误说法
2. 随后将适用范围收缩到 periodic／balanced wells，修正 cusp 机制
3. 又发现“精确 antiperiodic locking”仍过强；[1d9ba89b](https://github.com/whzy3185/math/commit/1d9ba89bdfac44bd4d5c9f6edaae7a427834ff7a) 改为物理 seam 引起的指数小相位移动
4. [7073fd8d](https://github.com/whzy3185/math/commit/7073fd8d7d18afff87d5f5390b67f8d3b149c82d) 及后续提交继续修正 tunneling 的主尺度和全阶相图
5. [184e2663](https://github.com/whzy3185/math/commit/184e2663697c21c6b0f5dd00accf6968522ce6c1) 汇总固定周期双缺陷几何分类与修正后的 tunneling 理论；其中 `r≥9` 的方向选择尾部已关闭，应读 `COMPLETE` 账本，不能沿用稍早 `FINAL` 账本中的旧“下一目标”

同日下午研究从双缺陷转向固定周期全类：先处理 period 8／12／16，随后发现 period 20、24、28、32、36、40 的多缺陷构造可以优于完整双缺陷家族。这里 period-8／jump-4 的问题不能与早期 `s=2` 的八周期结果混用。

### 9 月 15 日工作流入库与多缺陷新阶段

署名日期为 9 月 14 日的“数学 zyc”工作流在 [a1e0d3bf](https://github.com/whzy3185/math/commit/a1e0d3bfcb68b98aacb1ce3c750201076393a4f9) 入库，归纳已有七组任务的研究目标、纠错要求、证据层级与交接方式。它明确 triangle-free／chromatic／Mycielski 包的远端归档尚未核实，也提醒不能延用曾被质疑的 `mu_4=12`。

同日下午周期谱线继续：

- [2fcb76a7](https://github.com/whzy3185/math/commit/2fcb76a76bac4609f6f5d6a1450632d103f76ba9)：`8r+4` 周期的无限 DDGG 多缺陷改进
- [2b286fc9](https://github.com/whzy3185/math/commit/2b286fc96bb7d5f134a57aa4859bf5a575774e2e)：代数 DDGG dislocation edge 与指数收敛
- [258fb503](https://github.com/whzy3185/math/commit/258fb5031cc277eb6efff103d38f40eec0f4be16)：`p=8r` 的双 dislocation 构造
- [2ead87cf](https://github.com/whzy3185/math/commit/2ead87cf3ff0784edd945f551cbb18fbe99cc94d)：周期 48、56、64 的精确证书
- [739bb6a4](https://github.com/whzy3185/math/commit/739bb6a4913a68edef6f53e0078747da364059a7)：正密度多缺陷 staircase 与一致谱隙
- [c33959cd](https://github.com/whzy3185/math/commit/c33959cda2a899714b6d243e8dadf29139860c54)：period-20 全类优化器分类记录
- 最新 [ef65a3da](https://github.com/whzy3185/math/commit/ef65a3da6077c13927db5552a3196906d5ac2a6a)：常数量级 Bloch gap 需要正缺陷密度的论证

具体范围还需要保留三条限制：`p=8r+4` 的 DDGG `<31/4` 结论覆盖 `r≥2`，而 `p=8r` 互补族目前只有 eventual 结论与若干有限认证，不能写成已经统一关闭全 `r≥3`；period-20 全类唯一性在原稿标为精确有限验证，不外推任意周期；最新稀疏缺陷论证显示 `d=o(p) ⇒ liminf R≥8`，原文末尾直接写 `R→8` 的口号需要另有上界才能夹逼。这是现存表述范围的审计问题，本轮没有擅自修改其证明。

这标志着研究主题已超出原双缺陷正文。但这些是当前源稿和证明笔记中记录的进展，本轮没有重跑证书或为新定理作独立正确性背书，也没有看到已将全部结果整合进最新英文论文的证据。

## 必须保留的纠错和替代关系

| 历史说法或入口 | 当前应如何读取 |
|---|---|
| G6 exact-r、rank-one 计数 | 8 月 23 日已修正为涉及双重本征空间的 2r 框架，不可沿用旧证明 |
| residue-two tail 已解析闭合 | 9 月 2 日已撤回；仍有解析 majorant 缺口 |
| `CLOSED` 的全偶阶分类 | 按当时计算机辅助证明范围读取，不自动表示纯解析、全极值或 Lean 覆盖 |
| 八周期 `m(8L,2)=sqrt(eta)` 的原稿结尾 | 与同文负 holonomy 公式冲突；应读独立纠错分支 |
| 一般推广中的 `s=2L` 外推 | 9 月 7 日已被反例／端点检查修正 |
| AML 端点耗散自动推出平衡根 | 9 月 9 日撤回，需显式假设 `F(v*)=0` |
| 稀疏缺陷必有 `R→8` | 已显示结论是 `liminf R≥8`，极限等号需要上界；该表述问题尚需核清 |
| antiperiodic 普遍 phase-slip | 9 月 14 日撤回；后续还把“精确锁定”修正为指数小移动 |
| 双缺陷的固定周期最优性 | 是该受限家族内的最优性；9 月 14 至 15 日多缺陷材料表明不能自动扩为全类 |
| period-8 结果 | 必须写明 jump、holonomy、连续／有限谱及 signing 类别，不能只按周期名串接 |
| `main` 或 9 月 5 日 README | 只是入口／旧状态，不代表其他分支的最新研究 |
| AML 状态文档的旧成功构建 | 只覆盖旧 SHA；当前新增模块有明确失败记录 |
| Lonely Runner 构建成功 | 覆盖指定 Lean 库与证书片段，不等于全文主定理形式化完成 |
| Remark 3 测试日志与 PDF 构建记录 | 是旧执行记录；不同分支源码交付完整性不同，且没有完成全部近题文献比对 |

## 早期研究项目候选及当前入口

以下名称用于辨认“八月那条图论研究”，不是替用户重新选题。初始登记见 [候选目标](https://github.com/whzy3185/math/blob/c3e4460929c38d10f0b3a0e878267142303c9675/research/candidates/FINAL_TARGETS.md) 与 [猜想登记表](https://github.com/whzy3185/math/blob/c3e4460929c38d10f0b3a0e878267142303c9675/research/CONJECTURE_REGISTRY.md)。

| 项目名称 | 与早期记忆的对应 | 目前能确认的状态 |
|---|---|---|
| C029／Target A：偶数循环图平方的 signed 谱极值 | 最早的主攻项目；从 `C_n(1,2)` 的所有 signing 优化猜想开始 | 已形成反例、谱机制和多代稿件，后推广到一般跳长并拆成两篇 |
| G6 界面态与全偶阶反例 | C029 内部的结构方向，并非另一个无关课题 | 保留全偶阶构造，exact-r 秩叙述已经修正，部分纯解析替换仍有缺口 |
| 八周期精确谱与 Lean 比较 | C029 后期收窄的文章／形式化方向 | 正 holonomy 核心有形式化材料；负 holonomy、全局分类范围不能混写 |
| C040：二部图唯一最小支配集的边数上界 | 8 月 14 日候选表中的后备项 | 条件含无孤点、唯一 minimum dominating set、γ≥2、n≥3γ；未覆盖首例 γ=3,n=10；本次未发现成熟稿 |
| C019：锦标赛中的强 Seymour 顶点存在性 | 8 月 14 日候选表中的后备项 | 登记为 backlog，不能误写成 spectral Turán 或已完成成果 |
| triangle-free／chromatic／Mycielski 相关图论包 | “数学 zyc”工作流确实提及 | 23 个当前分支中没有定位到对应专门归档，`mu_4=12` 曾被质疑，暂不认可或接续其旧结论 |
| F017：`F(0,17,1,0)` 禁配置 | 9 月新开的独立离散线 | Case 1、clique 与 Case 2 的 r=6 有源稿；r=4,5 未闭合 |

其他独立文章级项目为“四速度 Lonely Runner 的低谱分类”“Remark 3 乘积型 PDE 的整函数解分类”“生产消费型趋化系统的质量加权稳定化”。前两者不能算作新的 C029 分支成果，后两者属于分析／PDE。


## 当前分支状态总览

下表是本次快照，不按“分支名听起来新”判断成熟度。完整 SHA、文件数、可达提交数及相对 `main` 的 ahead／behind 数见 [BRANCH_SNAPSHOT.csv](BRANCH_SNAPSHOT.csv)。

| 分支 | HEAD 与 UTC 日期 | 当前用途与边界 |
|---|---|---|
| `agent/target-a-discovery-snapshot` | [0ebfc7ba](https://github.com/whzy3185/math/commit/0ebfc7ba36c67fec5cb79bb9e515dcd3cb2c69c8) · 2026-08-24 | 早期反例与 Task59 JGT 稿基线 |
| `exp/circulant-1s-generalization` | [833face6](https://github.com/whzy3185/math/commit/833face614d2e9bda09d7d7112dc89f9a78b3555) · 2026-08-25 | Task60 一般跳长入口与旧稿润色 |
| `research/spectral-related-work-refresh` | [ebc6de4f](https://github.com/whzy3185/math/commit/ebc6de4fb67eeae7af961eb415a4dc1fdcc4c2c7) · 2026-08-31 | 相关文献与证明架构 |
| `proof/complete-mathematical-closure` | [44ff33a8](https://github.com/whzy3185/math/commit/44ff33a89294056907d0b909d68a8db27371c4f0) · 2026-09-01 | 计算辅助分类与解析缺口审计 |
| `analytic-proof-first` | [7b6a351c](https://github.com/whzy3185/math/commit/7b6a351cc5f8f83f5527b7fc547f0a865ea50cf2) · 2026-09-04 | 八周期解析化与部分 Lean 核心 |
| `period8-paper-strengthening` | [1201d4ec](https://github.com/whzy3185/math/commit/1201d4ecbc12da1152c110a18f57b9de49cbb191) · 2026-09-04 | 精确谱、最小周期与双语稿 |
| `paper/jgt-authorial-rewrite` | [6766ecbc](https://github.com/whzy3185/math/commit/6766ecbc20b084c648b29b0bf3813b8c1ecf86cb) · 2026-09-04 | 冻结原稿，结尾有后续修正 |
| `paper/period8-conclusion-correction` | [2dc5b90d](https://github.com/whzy3185/math/commit/2dc5b90d3ef86dc81a304379154d1063273a3c93) · 2026-09-05 | 独立中英文结尾纠错稿 |
| `research/circulant-1s-extension` | [65ec3440](https://github.com/whzy3185/math/commit/65ec34402f08bc1025077233a24c121b00f5703a) · 2026-09-05 | 一般跳长与仓库导航 |
| `research/q1-discrete-full-push-20260906` | [9e9f93b4](https://github.com/whzy3185/math/commit/9e9f93b4d17575004f352a1178174aaf06125c68) · 2026-09-06 | F017 局部证明；r=4,5 未闭合 |
| `lean-lonely-runner-ci` | [29fa62f1](https://github.com/whzy3185/math/commit/29fa62f117eca8fce2f503581533de22dac7a95e) · 2026-09-06 | HEAD 构建成功，覆盖部分证书 |
| `research/quadratic-gap-upgrade` | [47f64e51](https://github.com/whzy3185/math/commit/47f64e51fb78313fdd2bae1ae4542f7836c68ca1) · 2026-09-07 | 一般跳长谱隙、阈值和 staircase |
| `research/remark3-polynomial-exponential-20260908` | [d579b4f2](https://github.com/whzy3185/math/commit/d579b4f290881968c5b6011ae213b594645417f1) · 2026-09-08 | Remark 3 v1 与 14 组记录 |
| `research/remark3-explicit-classification-v2-20260908` | [f0ecf1cf](https://github.com/whzy3185/math/commit/f0ecf1cfee9b10b4cfb78a2002112dbc2a51d692) · 2026-09-08 | Remark 3 不可约分类与 93 项记录 |
| `research/remark3-product-pde-20260908` | [57300701](https://github.com/whzy3185/math/commit/57300701ce0259485e3e5e28e3fe991a70170bd5) · 2026-09-08 | 平行双语稿；测试源码不在该分支 |
| `research/remark3-leading-form-v3-20260908` | [a981f618](https://github.com/whzy3185/math/commit/a981f618c368d957f076f8346ec79aefb8f1c6f0) · 2026-09-08 | v2 加 v3 补充；18 项新增记录 |
| `main` | [c3e44609](https://github.com/whzy3185/math/commit/c3e4460929c38d10f0b3a0e878267142303c9675) · 2026-09-08 | 初始材料、导航和 JCTA 回顾 |
| `paper/circulant-all-jump-rebuild-20260909` | [cca0ea95](https://github.com/whzy3185/math/commit/cca0ea95730ee0130d403d90d8a8aa2781fdf138) · 2026-09-09 | 两篇拆分之前的重构基线 |
| `skill/math-research-full-push-20260909` | [78e3ef8d](https://github.com/whzy3185/math/commit/78e3ef8da0d1a4125327dc2f579961fb9ec7e3b7) · 2026-09-09 | 研究方法 v5；实际 benchmark 未跑 |
| `research/aml-production-consumption-stabilization` | [534c247d](https://github.com/whzy3185/math/commit/534c247d397ae4d522473f733c546e1b3ed28fe8) · 2026-09-11 | 论文投稿准备；最新 Lean 有失败 |
| `paper/circulant-finite-threshold-20260909` | [085ea698](https://github.com/whzy3185/math/commit/085ea698475b7b32e0ae57457ec903a922248f69) · 2026-09-14 | 有限全局极值；N=7s 仍非全分类 |
| `codex/math-zyc-workflow-20260914` | [a1e0d3bf](https://github.com/whzy3185/math/commit/a1e0d3bfcb68b98aacb1ce3c750201076393a4f9) · 2026-09-15 | 数学 zyc 工作流与来源梳理 |
| `paper/circulant-periodic-gap-20260909` | [ef65a3da](https://github.com/whzy3185/math/commit/ef65a3da6077c13927db5552a3196906d5ac2a6a) · 2026-09-15 | 最新多缺陷笔记；正文未同步 |

### 分叉关系怎样影响阅读

1. signed-circulant 主线从共同根发展，经早期反例、一般跳长、文献更新、解析证明、八周期稿与 quadratic-gap 阶段，再分为两篇论文；大量旧分支 HEAD 已是新分支的祖先
2. `paper/period8-conclusion-correction` 是独立修正文稿线；其补丁没有因为“时间更早”就自动进入所有后继分支
3. Remark 3 的 polynomial-exponential → v2 → v3 是真实祖先关系；product-pde 是平行版本
4. F017、Lonely Runner、Remark 3、AML 与 `main` 的共同历史入口主要停在导航提交；默认分支并未合并它们的成果
5. 方法分支及后来的工作流／AML 分支在 Git 上继承部分 F017 资料，但这种代码历史继承不表示课题在数学上属于同一主线

## 下一步只需先确定课题

本报告完成的是“先看清仓库，再列项目和变动”。若要恢复八月的图论研究，**C029／Target A 最符合仓库最早的文章级主线**；但若用户指的是 triangle-free／chromatic／Mycielski 对话，则还需定位真实包，不能用 signed circulant 代替。

确定课题后，各线最明确的续接点不同：周期谱要先核查最新多缺陷证明与论文同步；有限全局极值要按参数区间核查覆盖；F017 要关闭 `r=4,5`；Remark 3 要补最接近文献的全文对照；AML 要先修复／重验最新 Lean 模块并区分形式化边界。此处只列准确入口，不擅自开始新的证明或修正文稿。

## 配套文件与证据解释

- [EVENTS.csv](EVENTS.csv)：按 UTC 排列的 144 条分线事件记录，涉及 142 个不同提交；保留交叉主题注记以及中英文来源描述。事件提交日期和被读取的证据快照分列，避免把后来的总结冒充早期原文
- [COMMITS.csv](COMMITS.csv)：1,173 个去重可达提交的完整时间线，保留作者日期、提交日期、parent、所属可达分支与固定链接
- [BRANCH_SNAPSHOT.csv](BRANCH_SNAPSHOT.csv)：23 个分支的固定 HEAD、文件数及历史关系
- 本报告内的 commit 链接均固定到完整 SHA；证据清单中的文档链接也固定到核查快照，避免后续分支更新改变原说明

`EVENTS.csv` 中 `source_observed_at_sha` 是本轮实际读到证据的版本；部分来源固定到后来的分支 HEAD，因此不表示该文件当时已经存在。`COMMITS.csv` 是提交元数据全表，事件摘要是有选择的解释，不代替逐条 diff。

“提交发生”与“定理成立”是两种不同事实。完整提交列表证明版本轨迹；稿件与证明源说明作者当时如何论证；原始 CI 日志可证明特定 SHA 的构建结果；本轮没有新执行的数学计算、Lean 构建或 PDF 检查，因而没有把历史记录升级为本轮认证。

## 主要原始证据入口

- [初始 Target A 对象](https://github.com/whzy3185/math/blob/c3e4460929c38d10f0b3a0e878267142303c9675/research/conjectures/TARGET_A_SPEC.md)
- [旧结果替代地图](https://github.com/whzy3185/math/blob/65ec34402f08bc1025077233a24c121b00f5703a/research/repository_guide/SUPERSESSION_MAP.md)
- [F017 r=6 审计](https://github.com/whzy3185/math/blob/9e9f93b4d17575004f352a1178174aaf06125c68/research/proofs/F017_CASE2_R6_INDEPENDENT_AUDIT.md)
- [F017 clique 与 Case 1](https://github.com/whzy3185/math/blob/9e9f93b4d17575004f352a1178174aaf06125c68/research/proofs/F017_TRANSITIVITY_CLIQUE_CASE1.md)
- [有限极值最新账本](https://github.com/whzy3185/math/blob/085ea698475b7b32e0ae57457ec903a922248f69/research/paper_rebuild/circulant_finite_threshold_20260909/THEOREM_LEDGER.md)
- [周期谱双缺陷完整账本](https://github.com/whzy3185/math/blob/ef65a3da6077c13927db5552a3196906d5ac2a6a/research/paper_rebuild/circulant_all_jump_20260909/THEOREM_LEDGER_20260914_COMPLETE.md)
- [最新 period-20 有限全类证书](https://github.com/whzy3185/math/blob/ef65a3da6077c13927db5552a3196906d5ac2a6a/research/paper_rebuild/circulant_all_jump_20260909/PERIOD20_FULL_CLASS_EXACT_CLASSIFICATION.md)
- [稀疏缺陷与正密度必要性](https://github.com/whzy3185/math/blob/ef65a3da6077c13927db5552a3196906d5ac2a6a/research/paper_rebuild/circulant_all_jump_20260909/POSITIVE_DEFECT_DENSITY_NECESSITY.md)
- [Remark 3 v3 状态与文献边界](https://github.com/whzy3185/math/blob/a981f618c368d957f076f8346ec79aefb8f1c6f0/research/remark3_rigidity_v3/README.md)
- [Remark 3 平行双语稿复现限制](https://github.com/whzy3185/math/blob/57300701ce0259485e3e5e28e3fe991a70170bd5/research/remark3_product_pde/verification/REPORT.md)
- [AML 最新解析研究状态](https://github.com/whzy3185/math/blob/534c247d397ae4d522473f733c546e1b3ed28fe8/research/aml_prodcons_stabilization/RESEARCH_STATE.md)
- [AML 最新论文](https://github.com/whzy3185/math/blob/534c247d397ae4d522473f733c546e1b3ed28fe8/research/paper/aml_mass_weighted_stabilization/main.tex)
- [AML 旧形式化状态文档](https://github.com/whzy3185/math/blob/534c247d397ae4d522473f733c546e1b3ed28fe8/research/aml_prodcons_stabilization/LEAN_VERIFICATION_STATUS.md)
- [Lonely Runner CI 工作流](https://github.com/whzy3185/math/blob/29fa62f117eca8fce2f503581533de22dac7a95e/.github/workflows/lean-lonely-runner.yml)
- [JCTA 写作历史](https://github.com/whzy3185/math/blob/c3e4460929c38d10f0b3a0e878267142303c9675/research/paper/LONELY_RUNNER_JCTA_WRITING_AND_REVISION_HISTORY.md)
- [数学 zyc 接管与课题地图](https://github.com/whzy3185/math/blob/a1e0d3bfcb68b98aacb1ce3c750201076393a4f9/research/workflows/math_zyc/HANDOFF.md)
- [方法 v5 评估边界](https://github.com/whzy3185/math/blob/78e3ef8da0d1a4125327dc2f579961fb9ec7e3b7/research/skill-eval/math-research-full-push/EVAL_V5.md)

构建状态以文中直接链接的 GitHub Actions 原始记录为准；不能用一份旧状态文档替代不同 SHA 的真实结果。

