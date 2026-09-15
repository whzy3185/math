# Skill／MCP 深层架构设计

这份设计把 `math_zyc` 当作一个可恢复的研究系统，而不是把整段 ChatGPT 对话塞进一个更长的 prompt。核心原则是：Skill 负责行为规则和路由，MCP 负责有边界的能力，仓库状态负责事实，研究批次负责推进，账本负责证据与交接。

## 1. 先确定边界：Skill、MCP、普通代码各做什么

| 层 | 适合承载 | 不适合承载 |
|---|---|---|
| Skill | 触发条件、证据词汇、优先级、研究循环、何时调用哪类工具、输出契约、错误与停止规则 | GitHub token、当前分支事实、长篇论文全文、具体仓库的易变状态 |
| MCP server/tool | 读取仓库、创建分支、读取提交、写入文件、检索文献、运行验证器、编译 Lean、渲染 PDF；每个工具有明确输入输出和副作用 | 把所有研究判断硬编码成工具；代替模型判断新颖性或证明是否闭合 |
| 普通脚本／CI | 精确枚举、证书生成、独立 verifier、Lean build、LaTeX/PDF render、hash 和日志 | 解释“为什么这个实验足以证明无限命题”；不能单独提升证据等级 |
| 仓库文件 | `CLAIM_LEDGER`、`PROOF_GRAPH`、`LITERATURE_AUDIT`、实验日志、交接和论文 | 隐藏在聊天上下文中的临时状态 |
| 模型／编排器 | 选择下一批数学工作、解释结果、发现冲突、决定是否加强和重新审查 | 自行假设工具成功、把草稿当定理或跳过副作用确认 |

最小可行实现只需要一个 Skill 加 GitHub、shell／验证和文献三个工具域；MCP server 不应因为“研究”这个标签而把所有功能都暴露成一个万能 `do_research`。

## 2. 推荐的深层分层

```text
用户短指令
   ↓
Skill Router（识别课题、当前分支、优先级、禁止跨线）
   ↓
Research Orchestrator（生成一批可验证的下一步）
   ├─ State Adapter：读取仓库与当前 commit，生成 StateSnapshot
   ├─ Evidence Adapter：更新 claim、proof、literature、verification 账本
   ├─ GitHub Adapter：分支、提交、文件、PR；写操作返回 commit/ref
   ├─ Literature Adapter：来源、版本、定理逐项比较、日期
   ├─ Compute Adapter：精确脚本、枚举、证书、独立 verifier
   ├─ Lean Adapter：版本探测、构建、日志、源码与命题对齐
   └─ Manuscript Adapter：LaTeX 编译、PDF 渲染、交叉引用视觉检查
   ↓
BatchResult + EvidenceDelta + HandoffDelta
   ↓
仓库 commit／审计记录／下一轮状态
```

编排器是唯一允许改变研究状态的“事务协调者”。各 Adapter 尽量无状态：给定仓库、commit、参数，返回可复核结果。这样可避免模型把一次失败的工具调用叙述成已经完成。

## 3. 状态对象必须先于工具调用

编排器每轮开始构造 `StateSnapshot`，最少包括：

```json
{
  "repository": "whzy3185/math",
  "branch": "paper/circulant-finite-threshold-20260909",
  "base_commit": "085ea69",
  "topic": "finite-global-signed-circulant-extrema",
  "objective": "close the highest-priority proof obligation",
  "evidence_policy": ["Observed", "Verified finite", "Proved", "Published/Established"],
  "lean_build": "unknown",
  "literature_audit_at": null,
  "working_tree": "unknown",
  "open_obligations": [],
  "forbidden_scopes": [],
  "last_handoff": null
}
```

`StateSnapshot` 不是模型自己填写的摘要：分支、commit、文件哈希、构建日志和工作树状态必须由 Adapter 读取。模型可以提出 `objective` 和 `open_obligations`，但要在写入账本前指向实际文件或工具结果。

## 4. 工具调用关系：按依赖执行，不按关键词堆叠

### 4.1 恢复状态

```text
resolve_repo → get_default_branch → get_current_ref
            → list_recent_commits → read_state_files
            → classify_claims → select_priority
```

如果仓库、分支或权限不明确，停止在状态恢复层；不要先写论文。若分支已被其他研究线占用，创建本任务分支或只读快照，禁止覆盖历史分支。

### 4.2 文献与新颖性

```text
read_seed_or_current_claim
  → identify S0/S1/S2/S4 sources
  → search exact wording + synonyms + forward/backward citations
  → compare theorem tuples
  → write LITERATURE_AUDIT
  → decide: continue / revise claim / stop for collision
```

文献工具只提供来源和文本；“新颖”“open”“优先权安全”是编排器基于日期化证据做出的审计结论，不能由搜索命中数直接推出。

### 4.3 证明、反驳与强化

```text
claim → cheap_falsification
      → proof_dependency_map
      → structural_lemma / exact_reduction
      → finite_certificate + independent_verifier (if needed)
      → adversarial_checks
      → strengthen_axes
      → update_claim_ledger
```

有限计算只有在 `finite_reduction_proved=true` 且覆盖、边界、判定和复现记录齐全时，才可以成为 `Proved` 证据链的一部分。否则最多是 `Verified finite`。

### 4.4 形式化与论文

```text
stable_statement
  → align_lean_statement
  → build_with_declared_toolchain
  → inspect_log_and_no_placeholders
  → compare Lean ↔ human theorem
  → compile_latex
  → render_pdf
  → visual_cross_reference_check
  → freeze_or_reopen
```

Lean 编译失败不阻塞人类证明继续前进，但必须降级 Lean 状态；PDF 编译成功也不等于数学正确或交叉引用语义正确。

## 5. 工具域的最小 MCP 接口

每个工具都返回 `observations`、`artifacts`、`status`、`side_effects`、`provenance`，并在失败时返回结构化错误。建议接口如下：

| 工具域 | 只读工具 | 写入／副作用工具 |
|---|---|---|
| `repo` | `resolve_repo`, `read_file`, `read_tree`, `read_commit`, `diff_refs` | `create_branch`, `create_commit`, `update_file`, `open_draft_pr` |
| `literature` | `search_source`, `fetch_source`, `compare_claims`, `check_versions` | `write_audit_record`（最好由 orchestrator 统一写） |
| `verification` | `run_exact_check`, `read_certificate`, `compare_outputs` | `generate_certificate`（写入指定临时目录） |
| `formal` | `detect_toolchain`, `read_build_log` | `run_lean_build` |
| `manuscript` | `extract_pdf_text`, `inspect_render` | `compile_tex`, `render_pdf` |
| `state` | `load_snapshot`, `load_obligations` | `append_batch`, `write_handoff` |

工具命名要暴露动作和范围；例如 `read_commit`、`run_exact_check` 比 `analyze_project` 可审计。写工具应接收 `expected_base_commit`，若远端已变化则拒绝写入并要求重新恢复状态。

## 6. 一轮研究批次的事务协议

```text
BEGIN
  snapshot = load_state()
  plan = choose_one_obligation(snapshot)
  preflight = verify_scope_and_permissions(plan)
  result = execute_read_or_compute_tools(plan)
  audit = adversarial_review(result)
  delta = classify_evidence(result, audit)
  if delta is coherent:
      write ledger + proof graph + handoff
      commit with parent = snapshot.base_commit
  else:
      preserve failure artifact and downgrade claim
END
```

编排器提交前必须检查：

- 修改仅属于当前课题和分支；
- `expected_base_commit` 未变化；
- 新结论都带证据等级、依赖和来源；
- 失败计算、反例、撤回和旧结论替代关系没有被删除；
- 生成的脚本、日志、证书可从干净 checkout 重跑，或明确写出不可重跑原因；
- 写 GitHub、发 PR、合并主分支和对外发布是分开的动作。

## 7. Skill 的触发和渐进披露

主 Skill 只放路由和不可违反的规则，建议控制在约 600–900 tokens：

```yaml
name: math-research-full-push
description: Use when doing long-horizon theorem research in a repository...
```

触发后先读仓库状态，再按任务读取一个参考模块：`literature`、`proof`、`verification` 或 `publication`。不要每轮加载所有历史论文和全部聊天摘要。`math_zyc` 这份架构应作为仓库参考文档，而不是把个人 ChatGPT 对话原文打包进可安装 Skill。

Skill 的输出契约应固定为：`state_snapshot`、`selected_obligation`、`tool_trace`、`evidence_delta`、`files_changed`、`commit`、`remaining_risks`、`next_obligation`。没有这些字段，就不能把一轮称为“已完成”。

## 8. 哪些东西不应做成 MCP

- 不要提供 `prove_theorem`：证明是否闭合需要阅读依赖与反例，工具只能运行具体检查。
- 不要提供 `declare_novel` 或 `mark_open`：这些是有日期的文献审计结论。
- 不要把 GitHub 写入、论文投稿和消息发送绑成一个工具链；每个副作用都应单独呈现。
- 不要让浏览器抓取对话成为仓库事实源。对话负责提取初始要求，仓库账本负责当前事实。
- 不要用一个永久记忆文件代替版本化状态；每轮以 commit、日志和 handoff 恢复。

## 9. 推荐落地顺序

**阶段 1：仓库内 Skill（现在就能用）**

保留现有 `math-research-full-push`，新增本目录的架构、提示词来源和接管模板；先用现成 GitHub、shell、文献和 PDF 工具验证输出契约。

**阶段 2：只读 MCP**

先实现 `resolve_repo`、`read_tree`、`read_file`、`read_commit`、`load_snapshot`、`search_source`、`run_exact_check`、`detect_toolchain`。只读层稳定后，错误大多是路由或状态恢复错误，容易定位。

**阶段 3：受约束写入**

增加 `create_branch`、`update_file`、`create_commit`、`write_handoff`；所有写入绑定 `expected_base_commit` 和目标路径白名单。默认先写独立分支，默认草稿 PR。

**阶段 4：验证与论文适配器**

加入 Lean、精确 verifier、LaTeX 和 PDF render，保存命令、版本、日志、hash。此时才评价 `Proved` 或 `submission-ready` 的自动化质量。

**阶段 5：基准评测**

用六类真实场景评测：恢复“继续”、反例纠错、定理加强、文献冲突、模拟审稿、普通教材问题边界。指标是证据等级错误、无谓澄清、真实提交完成率、定理增量、构建状态、工具成本和恢复成功率；静态 prompt 分数不能替代这些指标。

## 10. 深层风险与解决方案

| 风险 | 解决方案 |
|---|---|
| 长对话和仓库状态漂移 | 每轮读取 commit 和账本；交接只引用可验证文件 |
| 模型把实验说成定理 | 强制 `evidence_delta` 与有限覆盖字段 |
| 两篇论文交叉污染 | `forbidden_scopes` 和分支白名单，在工具调用前检查 |
| 远端写入部分成功 | 工具返回 commit/ref；写后立即 read-back；失败保留 idempotency key |
| Lean 外围模块通过但主命题未对齐 | 保存 theorem fingerprint 和源码位置，构建后做陈述比对 |
| 文献搜索过时 | 审计日期、版本、forward citation 和材料哈希 |
| 多工具互相调用形成黑箱 | 只有 orchestrator 可提交状态；每个 adapter 返回 provenance |
| 研究目标无限扩张 | 每批只选一个 obligation；阶段性 freeze／reopen |

## 11. 当前建议

先把它做成仓库内 Skill 加只读 MCP，再做受约束写入。原因是当前最大风险是状态、证据和范围错误，工具数量不足不是主要瓶颈。只有当只读恢复和证据账本连续多轮稳定后，才值得把分支／提交／验证／PDF 组合成自动化写入链。
