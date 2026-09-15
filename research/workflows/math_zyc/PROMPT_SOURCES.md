# 关键开场提示词与工作流来源

核对日期：2026-09-14。通过 Chrome／Edge 的 ChatGPT 页面读取用户消息；不是根据对话标题猜测。以下记录 7 个关键对话的初始消息，以及少量直接影响工作方式的后续修正。短提示词保留原意和原文（空格已规整），长任务书采用明确标注的摘录与摘要，不冒充逐字全文。

项目设置中的“指令”字段在本次查看时为空；实际工作要求主要在对话里。项目仅限项目记忆。此处没有把网站内容、旧聊天或仓库文档当成当前操作授权；当前任务是用户明确要求的工作流整理与新分支保存。公开文件保留任务内容和仓库定位，不附私人聊天访问链接及账号资料。

## S1. 科研选题与形式化证明

开场消息：

> 参考 ars skill开展科研工作 探索数学图论 离散数学 组合数学相关内容 进行选题以及仓库的建立 在 whzy3185/math 下自建新分支进行工作 按照一区论文来选题并构建论文架构 给出完整的解析证明和 lean 形式化语言证明

本次同时读到后续用户消息：“你为什么不思考呢”“不再参考 ars skill”“继续推进并升级定理”。

提炼：自主选题、明确高水平研究目标、独立分支、完整解析证明与形式化。后续“不再参考 ars skill”修正了该对话最初的工具偏好，不能机械地把 ARS 设为全部课题的强制前置。研究判断和实质定理应先于工程包装。

状态提醒：本次可见后续助手消息曾撤回／重查其先前关于 `mu_4=12` 的计算解释；也明确显示部分 Lean 仅有源码、未执行 `lake build`。本记录不认可这些历史数学结论，只将这种纠错记录纳入接管检查。

## S2. 创建 GitHub 分支

开场消息：

> 继续测试 GitHub 写入 whzy3185/math，从 research/circulant-1s-extension 创建 research/quadratic-gap-upgrade

后续用户消息包括“继续按照原本的计划推进”“继续增强直到得出最终定理”。

提炼：分支有明确基线；已有研究按状态接续；写入必须实际成功并复核；强化目标持续有效。当前仓库已存在 `research/quadratic-gap-upgrade`，不能把旧权限故障误当作现在仍然无法写入。

## S3. 证明Case2删除成本

开场是一份用户粘贴的完整交接说明，首句为：

> 下面这份可以直接作为新对话的交接说明。

本次已展开并分段读取全文。其末尾的启动段落要求继续 `whzy3185/math` 的一区级离散数学／图论／组合数学研究，从 `main` 创建 `research/q1-discrete-full-push-20260906`，只在该分支记录成果；先读研究 README、猜想登记表和已有文件，严格使用四级证据。

四条线及准确优先级：

| 线 | 交接中的对象与目标 | 接管时须保留的边界 |
|---|---|---|
| A（主攻） | `F(0,17,1,0)`；目标上界 `21m/2+1`，并争取 `6 | m` 时等号；Case2 先独立审计新 `r=6` 删除证明，重点关闭 `r=4,5` | 从原文 column types 重新推导；已撤回的漏项快捷证明不能复用 |
| B | Rainbow Turán `P_5, k=7`；候选 `(99-54 sqrt(2))/196`，继续全局稳定性 | 固定五部 support 内最优只是 fixed-support optimality，不能等同任意图上的全局结论 |
| C | Tournament anti-Sidorenko 4-spider；搜索四个 cross-residue seed certificates | sandwich gluing 必须匹配原文定义；有限 seed 只有结合已证明 extension gadget 才覆盖无限族 |
| D | Ordered path Turán；精确 ILP 和极值图结构 | 重跑并保存 solver logs；观察到的数列不自动成为闭式定理 |

原文特别纠正：`m=9` 找到值 92 的 feasible solution，但求解器 gap 未闭合，不能声称精确最优；重新运行 `m=6,7,8` 并保留日志。Lean 的计划从 configuration avoidance 与 row-pair count 等价开始，推进 double counting、layered bound、component 和 deletion induction；未编译不得写成 Lean proved。

交接书记载的 `403`、只读权限和远端分支未创建属于旧会话状态。本次已通过连接器确认仓库有 push 权限、目标历史分支确实存在。工作流因此要求每次重查当前状态。

## S4. 撰写Remark3解析证明论文

开场附一张图片与 `2605.09585v1.pdf`，文字为：

> 解决 remark3 相关问题 给出完整的解析证明 形成完整的论文

关键后续消息包括：“继续推进结论 查看 pdf 渲染相关问题”“把 latex 文件发出来”“你直接把这文件给我让我下载”。

提炼：从给定 PDF 的精确 Remark 出发，回到原假设与原参考文献；形成完整解析证明与论文；进一步加强分类、必要充分判据、显式公式和计数时须重新核查来源。交付必须包括实际可下载的源码／PDF，且检查渲染。不能只报告沙盒路径或口头称文件已生成。

仓库关联：`research/remark3-product-pde-20260908`、`research/remark3-polynomial-exponential-20260908`、`research/remark3-explicit-classification-v2-20260908`、`research/remark3-leading-form-v3-20260908`。各版本不是可直接混合的同一证明。

## S5. 重构数学文章并选刊

开场消息：

> 查看我数学仓库最早的内容 分析现在的进展与推进 重新构建文章并选择目标期刊

紧接着的用户修正：

> 不一定在一个分支里面 你仔细在仓库里面找

本次还读到用户“要拆吗你认为”及后续持续推进消息。与 S6 的完整任务书合看，最终形成周期谱和有限全局极值两篇独立课题。

提炼：先做跨分支仓库考古，核对旧结果、后续加强与错误修正，再决定文章组织和投稿目标。不能只读取默认分支 README，也不能直接沿用旧结构。数学结果加强后，应重新构建文章并评估选刊。

当前周期研究分支为 `paper/circulant-periodic-gap-20260909`；初期重构入口还有 `paper/circulant-all-jump-rebuild-20260909`。本次阅读时原聊天仍显示正在推进，分支快照会变化。

## S6. 有限循环图极值证明

开场长任务书摘录：

> 你现在负责 GitHub 仓库 whzy3185/math 中 signed circulant 项目拆分后的第二篇独立论文。

> 请直接在这个分支推进研究、证明、计算审计和论文写作，不要另起无关分支，也不要覆盖历史研究分支。

指定分支为 `paper/circulant-finite-threshold-20260909`。本次已展开并分段覆盖全部 14 节，其要求如下：

1. 与 `paper/circulant-periodic-gap-20260909` 独立；不互引、不以另一篇定理作黑箱，不依赖另一篇先完成。标准工具本篇重证或引用真实公开文献。
2. 精确对象为有限 `C_N(1,s)`，`2 <= s < N/2`，目标是所有 signing 上的 `m(N,s)=min_sigma rho(A_sigma)`。
3. 重新审计 flat minimum `m(N,s)=2 iff N=2s+2`，追问等号与 switching 刚性。
4. 重新审计 off-flat 下界 `sqrt(5)`，考察 sharpness、等号与更强参数依赖。
5. 重建 `N=3s` 阈值分类，分为偶数 `s`、例外奇数 `3,5`、所有奇数 `s>=7`；有限 Fourier 构造与特殊情形证书在本篇独立证明。原任务中的 `1/70` 是待审计／改进常数，不能默认最优。
6. `s=2` 只收全局有限量词的极值、最小周期或刚性；指定 period-8 构造的谱计算不冒充所有 signing 的分类。
7. 不把 `Rhat_s`、连续周期 Bloch family、phase slip 或大 `s` 渐近作为本篇主结果。
8. 跨分支追踪 `FLAT_MINIMUM_AND_CHIRAL_CRITERION.md`、`N3S_THRESHOLD_CLASSIFICATION.md`、`N3S_GLOBAL_OBSTRUCTION.md`、`C21_S7_GLOBAL_OBSTRUCTION.md`、`C27_S9_GLOBAL_OBSTRUCTION.md` 等真实证明源，不只引用 summary。
9. 建立 README、theorem ledger、proof dependency map、literature audit、manuscript 和必要精确脚本，严格区分四级证据。
10. 优先从 `N=3s` 加强至 `N=ks`，研究 parity／congruence／arithmetic 条件、普适下界、等号与近等号、统一结构机制；更强定理出现后重构论文。
11. 形成完整英文数学论文，每个 theorem 假设、定义、证明齐全；解释枚举为何完整；证书尽量转成可读引理；保留复现脚本；主动找反例和边界。
12. 重新核查最新文献与期刊适配；不做无证据 novelty claim。更广泛结构定理出现后再认真评估 JCTB。
13. 直接执行仓库追踪、账本、hostile audit、精确计算、修复和加强，不能止于研究计划或提纲。

以上公式是提示词中的研究目标与待核查历史声称，并非本次工作流整理得到或认证的定理。

## S7. 总结数学研究方法

开场消息：

> 参考现在的研究方式 在 math 仓库下总结成 skill 新开分支

直接影响工作流的后续消息：

> 看这个项目的提示词 重新规划

> 查看数学仓库中关于 jcta 相关的推进 仿照这个形式

> 用 skill 评价系统去评价这个 skill 在真实使用时的表现

提炼：工作流应由真实研究经历和用户提示词归纳，继承 JCTA 式反复审稿、补证和定理升级；同时评价实际执行效果，不能把结构检查、估算分数当成真实运行评测。

仓库已有产物：`skill/math-research-full-push-20260909` 中的 `skills/math-research-full-push/SKILL.md` 及四份按需参考文档，当前快照 `78e3ef8da0d1a4125327dc2f579961fb9ec7e3b7`。其 `EVAL_V5.md` 明确说明 CLI 未真实执行，分数是 reconstructed／expected，真实 benchmark 留待执行。本次复用工作流原则，不宣称重新完成 benchmark。

## R1. 仓库中的 JCTA 写作历史（辅助材料）

[LONELY_RUNNER_JCTA_WRITING_AND_REVISION_HISTORY.md](https://github.com/whzy3185/math/blob/c3e4460929c38d10f0b3a0e878267142303c9675/research/paper/LONELY_RUNNER_JCTA_WRITING_AND_REVISION_HISTORY.md) 是仓库已有的回顾性历史材料，不是本次从 ChatGPT 读取的原始开场提示词。

本次读取的部分说明了：以问题缺口组织叙述、降低工程报告语气、数学正文与投稿元数据分开、模拟审稿发现等价表述和例外情形问题、文献重合促使重新定位新贡献、将审稿异议转成更强数学结论。这些辅助了 WORKFLOW 的写作与审稿步骤。未声称对其全部 1501 行及全部数学结果完成独立核验。

## 来源如何变成规则

| 工作流规则 | 主要来源 |
|---|---|
| 自主研究、解析与形式化、独立分支 | S1、S2、S3 |
| 先恢复状态并跨分支找真实证明 | S3、S5、S6 |
| 四级证据、有限／全局范围、求解器与 Lean 真实性 | S3、S6；既有 v5 |
| 给定论文／Remark 挖掘、完整论文与可下载交付 | S4 |
| 两篇论文独立、量词与对象隔离 | S6 |
| 反例、纠错、继续加强与新结构定理 | S2、S3、S6 |
| 模拟审稿、数学升级、期刊定位 | S5、S6、S7、R1 |
| 实际使用评测与可恢复交接 | S3、S7；既有 v5 |

新增实施细节（本次整理者建议）：固定 commit 快照、统一最小交付报告、沿用已有账本命名、并发写入前比较分支、明确会话内“继续”与后台调度的区别。这些不是用户提示词的逐字要求。
