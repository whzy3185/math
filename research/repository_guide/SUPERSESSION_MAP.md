# 历史状态与替代关系

本文件是覆盖层：保留原证明、证书、日志和冻结文件，不通过批量改标题
抹掉历史。只有本轮明确确认错误的结尾问题标为“否定”；其他退出主线
的内容不因此被判为错误。

| 旧文件/表述 | 现状 | 应读取的替代入口 |
|---|---|---|
| `research/README.md` 原“当前交付”为Markdown V2与旧TeX | **入口过时**；原文已留快照 | [现入口](../README.md)、[原文快照](HISTORICAL_RESEARCH_README.md) |
| `CONJECTURE_REGISTRY.md` 自称唯一状态索引，C029含“manuscript not started” | **候选历史登记**；开放性判断受原日期限制 | [当前成果](RESULTS_INDEX.md)，不据此决定投稿状态 |
| `analytic_inventory/README.md` 把period8解析多项式列为未来目标 | **阶段计划过时**；该目标已有后续证明 | P2–P6及[最新period8包](../paper_strengthening/final_theorem_package.md) |
| `analytic_inventory/analytic_claim_registry.md` 把`1561/200`作为主定理表达 | **有效但较弱的旧表达** | 正负有限精确谱边与完整色散 |
| `proof_closure/FINAL_MATHEMATICAL_PROOF_STATUS.md` 全偶阶“CLOSED” | **历史计算辅助范围**；不是全解析或全部极小值 | [旧解析缺口记录](../proof_closure/ANALYTIC_GAP_AUDIT_CURRENT.md)与当前成果D表 |
| `r2_boundary_tail_closure.md` 与 `r2_tail_majorant_lemma.md` 的核心维数、tail常数与推广状态 | **版本/坐标接口待核对**；有草稿不等于关闭 | [tail审计](../analytic_inventory/r2_tail_line_audit.md)；先核对6/8维对象是否同一坐标，不在本轮修复 |
| `paper_strengthening/current_verified_kernel.md` 最后列“精确负sector、最小周期仍open” | **有意保留的Phase0快照**，并非当前开放清单 | [最终包](../paper_strengthening/final_theorem_package.md)；原文件不改 |
| `paper_strengthening/CURRENT_RESEARCH_STATE.md` 下一步“开始创建稿件” | **八周期写作前状态** | [稿件地图](BRANCH_AND_PAPER_MAP.md) |
| `JGT_RECENT_STRUCTURE_AUDIT.md` 最后建议七节 | **原结构建议**；文献观察与最后决策分开 | 当前实际六节；[结构V2](../paper_strengthening/FINAL_ARTICLE_ARCHITECTURE_V2.md) |
| `FINAL_ARTICLE_ARCHITECTURE.md` | **已显式被V2替代** | 同上V2 |
| `INTEGRITY_REPORT_STAGE_2_5.md` / `INTEGRITY_REPORT_AUTHORIAL_REWRITE.md` 全面PASS语气 | **历史检查记录**；不能保证整篇正确 | 已知结尾缺陷与独立纠错`2dc5b90` |
| 冻结稿结尾问`m(8L,2)=sqrt(eta)`是否无限成立 | **被同文负holonomy公式否定** | [纠错记录](https://github.com/whzy3185/math/blob/2dc5b90/research/paper_strengthening/manuscript_period8_jgt/CONCLUSION_CORRECTION_20260905.md) |
| Task60 handoff称仅完成60.0–60.1、等用户继续 | **一般跳长早期快照** | [当前推广说明](../generalization/circulant_1s/extension_20260905/REPOSITORY_STATUS_20260905.md) |
| 新推广主证明的指数小谱隙下界 | **仍正确但已加强** | [多项式谱隙](../generalization/circulant_1s/extension_20260905/POLYNOMIAL_GAP_BOUND.md) |
| `QUANTITATIVE_QUESTIONS.md` Q5称candidate | **保留提出时状态**；其后已有证明正文 | 同上定量证明；Q6/Q7仍开放 |
| 历史novelty报告“未找到直接先例” | **限日期和检索范围的观察** | 不作全球优先权证明；下一阶段重新核查 |

## 过时不等于错误

同一数学事实可能从CAS核验升级为完整手算推导；旧证明因此不再是
首选入口，但其正确性不会自动被否定。相反，开放问题与同文定理
矛盾是真实错误，不能仅叫“写作风格”。此处两类处理严格分开。

## 冻结与纠错

原论文分支和freeze tag未修改。纠错分支仅修改两个结尾、两个PDF和
纠错记录。当前研究分支也保留冻结正文，因此从本分支打开旧结尾仍
会看见原文；这不是漏修，而是版本隔离。实际阅读修正稿请使用纠错
分支链接。后续是否将其合入新的正式稿，待用户授权的论文修订阶段处理。
