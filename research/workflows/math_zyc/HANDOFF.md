# 接管入口与执行提示词

日期：2026-09-14。工作流分支：`codex/math-zyc-workflow-20260914`。基于既有方法分支 `skill/math-research-full-push-20260909` 的提交 `78e3ef8da0d1a4125327dc2f579961fb9ec7e3b7` 建立。

## 阅读顺序

1. [PROMPT_SOURCES.md](PROMPT_SOURCES.md)：7 个关键开场提示词的依据和范围修正。
2. [WORKFLOW.md](WORKFLOW.md)：日常研究、证明、审稿、交付循环。
3. [既有 math-research-full-push v5](../../../skills/math-research-full-push/SKILL.md)：保留原有可复用 skill，本次未改动其内容。
4. 根据下面的课题地图，读取对应研究分支的最新提交和真实证明源。

## 课题地图

以下是本次本地仓库读取时的快照，后续接手要重新获取远端状态。文件名或提交说明只用于定位，不代表本次认证了证明。

| 课题 | 分支 | 本次快照 | 首先核查 |
|---|---|---|---|
| 现有方法 skill | `skill/math-research-full-push-20260909` | `78e3ef8` | v5、四份 references、EVAL_V5 与真实 benchmark 缺口 |
| 周期谱主线 | `paper/circulant-periodic-gap-20260909` | `6de1441` | `research/paper_rebuild/circulant_all_jump_20260909/` 中最新 ledger、full-class 文档及其证明依赖 |
| 有限全局极值 | `paper/circulant-finite-threshold-20260909` | `085ea69` | `research/paper_rebuild/circulant_finite_threshold_20260909/` 的账本与依赖图；N=7s 等最新结果的精确范围 |
| 一般跳长历史入口 | `research/circulant-1s-extension` | `65ec344` | repository_guide、状态覆盖表和源证明 |
| 谱隙加强历史 | `research/quadratic-gap-upgrade` | `47f64e5` | finite-global 与 continuous 构造结果的分界；旧常数和后续替代 |
| Remark3 最新命名版本 | `research/remark3-leading-form-v3-20260908` | `a981f61` | v3 与 v2、product-pde 等各版本的新增假设、分类陈述、审计和编译记录 |
| Forbidden configuration／Case2 | `research/q1-discrete-full-push-20260906` | `9e9f93b` | `F017_CASE2_R6_INDEPENDENT_AUDIT.md`、`F017_TRANSITIVITY_CLIQUE_CASE1.md`；确认 r=4,5 的当前缺口 |
| JCTA 写作历史 | `main` | `c3e4460` | 1501 行写作修订历史是经验材料；研究当前状态需另查对应分支 |

“科研选题与形式化证明”对话中还有 triangle-free／chromatic／Mycielski 相关研究包；本次未核实其完整远端归档对应关系。应先定位真实包和源码，不能把这些内容并入 signed-circulant 或 F017 主线，也不能沿用已被后续消息质疑的 `mu_4=12`。

## 可以直接用于下一轮的接管提示词

> 按 `research/workflows/math_zyc/WORKFLOW.md` 接续 whzy3185/math 的数学研究。先确认本轮课题、指定分支和最新提交，恢复最强可靠定理、真实证明源、依赖图、失败路线、被替代结果和最新文献定位。不要仅凭 README、聊天总结或 FINAL 文件判断完成状态。
>
> 已指定课题时直接执行最高优先级未闭合任务；“继续”意味着恢复并推进，不重复问我要做什么。每轮产生一个可以检查的数学增量：证明、反例、结构加强、有限化、文献冲突核清、精确复核或编译通过且陈述对齐的形式化结果。
>
> 严格区分 Observed、Verified finite、Proved、Published/Established，并单独记录 Lean 构建状态。每条结果写清对象、参数和量词；指定构造、固定 support、固定周期或有限样本不能自动升为全局定理。求解器 gap 未关闭不得声称最优；没有实际编译不得声称 Lean proved。
>
> 先对抗性核查，再继续加强范围、常数、等号、分类、刚性和统一机制；发现错误立即修正所有依赖，不维护旧结论。实质加强后重新核查文献。按数学障碍组织完整证明与文章，把模拟审稿的问题转成数学义务；检查实际渲染的 PDF，交付真实可下载文件。
>
> 保持两篇 circulant 论文的对象范围和证明独立，不用另一篇未发表结果作黑箱。已有研究者仍在写入时使用独立分支和固定快照，合入前检查新增变更。完成后更新账本、证明依赖、验证记录和交接文件，给出实际提交与明确下一问题。

## 接管的第一轮验收

- 正确定位一个课题的当前分支、commit、定理和真实证明依赖。
- 找出最关键未闭合义务，实际复核一个可完成的证明环节或精确证书。
- 若发现历史错误，记录撤回范围并更新依赖；若未发现，仍说明检查覆盖范围。
- 产生文件与提交，明确未运行的计算／Lean／文献全文核验。
- 记录任务完成度、无必要澄清次数、证据等级错误、定理增量、构建状态和用时／工具开销，作为真实效果评测，不虚构分数。

本次交付只完成工作流与接管方法的整理，没有重跑各数学课题的实验、Lean 或论文构建，也没有启动后台研究任务。
