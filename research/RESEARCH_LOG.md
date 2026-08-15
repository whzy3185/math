# Research Log

本文件只追加、不覆写既有记录。每次研究必须记录日期、研究对象、所做工作、所得结果、失败、新发现与下一步。

---

## 2026-08-14 — 项目初始化（Prompt 0）

- **研究对象：** 项目基础设施与总规则；尚未选择具体猜想。
- **做了什么：** 在 E 盘克隆空的 GitHub 仓库；建立 `research/` 目录结构、项目规则、猜想登记表和研究日志模板。
- **得到什么：** 形成可版本控制的研究骨架；明确证据等级、开放状态审计、精确验证、随机性记录、穷举记录、最小性、无穷族及独立复核规则。
- **哪些失败：** 无。远程仓库为空，因而没有旧内容可迁移或兼容。
- **新发现：** 当前仓库没有任何历史引用或默认分支；首次提交后才会建立分支和远程引用。
- **下一步：** 单独执行 Prompt 1，进行公开文献挖掘并生成 `literature/RAW_CONJECTURE_SURVEY.md`；本次初始化不开始猜想搜索。

---

## 2026-08-14 — 第一轮公开文献挖掘（Prompt 1）

- **研究对象：** 2022–2026 年优先数学分类中明确提出、可计算探索的 Conjecture / Question / Open Problem。
- **做了什么：** 使用 arXiv 官方 API 初筛，下载并回读 28 篇原始论文 PDF；从正文提取并整理 50 个候选及 4 个备用候选，逐项记录来源、精确命题、参数、作者验证范围、生成/判定能力、已知边界、初步难度和价值。
- **得到什么：** 生成 `literature/RAW_CONJECTURE_SURVEY.md`。较强的近期攻击面包括 signed circulant 谱半径、order-polynomial 组合解释、induced saturation、zero forcing、唯一支配集、Schur log-concavity 与 Latin-square 参数缺口。
- **哪些失败：** 仅靠摘要会混入“论文已经证明的旧猜想”，因此所有候选均回到 PDF 正文核对；若干 PDF 的标题断行导致自动提取失败，已人工改用上下文定位。尚未完成逐题全球状态审计。
- **新发现：** 多个候选具有明确首个未知规模或作者穷举边界，例如 C029 已验偶数 `n≤18`、C037 已验所有至多 6 顶点模式图、C025 已无条件验至 `N=12`、C027 仅留下非常具体的参数缺口。
- **下一步：** 执行 Prompt 2；逐题搜索 proof/disproof/counterexample、版本更新、正式期刊版、后续引用和作者后续工作，并将无法充分确认者继续标记为 `UNVERIFIED OPEN STATUS`。

---

## 2026-08-14 — 开放状态第一轮审计（Prompt 2）

- **研究对象：** `RAW_CONJECTURE_SURVEY.md` 中的 50 个候选。
- **做了什么：** 按猜想名称、论文标题、作者和 proof/disproof/counterexample 关键词检查公开索引、arXiv 原始页与版本；重点复核 2025 年候选和 14 个高可计算候选；生成 `literature/OPEN_STATUS_AUDIT.md` 并同步登记表。
- **得到什么：** A 类 39 项、B 类 4 项、E 类 1 项、F 类 6 项；本轮未发现 C 类（已解决）或 D 类（原命题已有反例）。
- **哪些失败：** C010、C016、C022 的后续研究脉络未达到足以断言开放的证据强度；C048 原文量词疑似 typo。它们均保留 `UNVERIFIED OPEN STATUS`，不进入直接攻击。
- **新发现：** C020 已有公开论文专门研究最小 non-UP 见证，必须避免重复包装；C029、C037、C040、C049 等仍具有清楚的首个未知规模或边界条件。
- **下一步：** 执行 Prompt 3，仅对 A 类和可合理保留的 E 类候选做 20 分可攻击性评分，筛出 Top 20 与 Top 10。

---

## 2026-08-14 — 可攻击性评分与最终目标选择（Prompts 3–4）

- **研究对象：** 状态审计后保留的 A/E 类候选。
- **做了什么：** 建立可复算 20 分模型，给出 Top 20 与 Top 10 深入分析；逐项形式化 Top 10 的变量、定义域、反例条件、已知边界、搜索空间、对称、判定成本和 failure mechanism。
- **得到什么：** 选择 C029 为 Target A（ACTIVE），C049 为 Target B（SECONDARY），C030/C040/C019 为后备目标；生成 `candidates/CANDIDATE_RANKING.md` 与 `candidates/FINAL_TARGETS.md`。
- **哪些失败：** C037/C027 虽评分高，但不存在有限 witness-size bound 时，有限搜索失败不能成为反例证书；因此不设为当前主目标。
- **新发现：** C029 的首轮完整空间约 `2^21≈2.1M` switching classes，且 exact spectral comparison 可形成严格证书，是最适合进入 formalization/reproduction 的目标。
- **下一步：** Prompt 5，仅形式化 Target A=C029；在规格完成前不执行大规模搜索。

---

## 2026-08-15 — Target A 精确验证器与首个复现点（Prompt 6，进行中）

- **研究对象：** C029 signed circulant 全局谱半径猜想。
- **做了什么：** 实现独立 exact verifier 与 switching-class reproduction driver；使用代数数、整数特征多项式、Sylvester 判据和有理 Rayleigh 下界，避免用浮点结果作最终结论。
- **得到什么：** `n=8` 的 512 个 switching classes 完整枚举 PASS；quadrilateral 系统秩为 7、解类数为 4；两个 optimizer 类达到精确阈值，其余 510 类均有有理证书排除反例。
- **哪些失败：** 尚未执行 `n=10,12,14,16,18` 的完整复现，因此 Prompt 6 总状态仍为 IN PROGRESS。
- **新发现：** 数值本征向量只用于提出整数 Rayleigh 向量；每个非 optimizer 的最终排除可完全由有理数与代数数区间验证。
- **下一步：** 保存 `n≤18` 完整日志与 checksum；只有全体 PASS 后才进入 Prompt 7/`n=20`。
