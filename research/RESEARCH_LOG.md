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

---

## 2026-08-15 — Target A 接手复现与 n=20 首轮搜索

- **研究对象：** C029 signed circulant 全局谱半径猜想。
- **做了什么：** 克隆并审计当前仓库；搭建本地 `.venv`，使用 Codex bundled NumPy 与 SymPy 1.14.0；修复 `target_a_reproduce.py` 中 optimizer equality 的 SymPy 等零判定问题，改用阈值最小多项式整除 `A^2` 特征多项式；完整运行 `n=8,10,12,14,16,18` 复现，并在 Prompt 6 通过后运行 `n=20` 全 switching-class 搜索。
- **得到什么：** `n≤18` 全部 PASS；`n=20` 的 `2,097,152` 个 switching classes 全枚举 PASS。对 `n=20`，两个 optimizer class 达到阈值，其余 `2,097,150` 个 class 均由有理 Rayleigh 下界证书排除；exact fallback 为 0；未发现反例。
- **哪些失败：** 原脚本在 `n=14` 起会因 `sp.simplify(polynomial(threshold)) != 0` 误判 optimizer equality；诊断显示该值数值为 0，但 SymPy 未化简。该失败已通过最小多项式余式判零修复。
- **新发现：** 现有 Rayleigh-certificate 路线对 `n=20` 仍非常有效，约 98.46 秒完成，无需 exact fallback。当前证据等级为有限范围 **Verified**，不是全体偶数 `n` 的证明。
- **产物：** `research/logs/target_a_reproduction_n8_18.json`，SHA-256 `141d0253159acde39473cf4f825f65d438cd56e8433e407c3302fe048ad3715e`；`research/logs/target_a_search_n20.json`，SHA-256 `20a0d812a268d51c4c52188c63827732216815f20901ef83ad680816d82fbcc4`。
- **下一步：** 对 `n=20` 的最小非 optimizer orbit 做 dihedral/global-sign 归约与 flux 结构分析；随后设计 `n=22` 搜索的进度日志、checkpoint 与对称规约，避免一次性无进度枚举。

---

## 2026-08-15 — Target A flux atlas、n=22 穷举与无限反例族

- **研究对象：** C029 signed circulant global optimizer conjecture。
- **做了什么：** 实现 `(Q,alpha)/D_n` 的 binary-bracelet 枚举、defect-shell checkpoint、单次 dense eigendecomposition 与有理 Rayleigh 排除；用 `n=20` raw 全枚举交叉验证 canonicalizer；完成 `n=22` 全 quotient 搜索；扫描 two-defect、局域四缺陷与 period≤12 的 Floquet 结构族。
- **得到什么：** `n=20` 的 27,296 spectral states 与 raw 2,097,152 classes 完全一致；`n=22` 的 97,468 states 覆盖全部 8,388,608 classes，97,467 个非 optimizer 均精确排除，0 fallback、0 反例。near-minimizer atlas 显示 `n=20,22` 的第二名均为 `d=4`，从而引出周期搜索。
- **反例：** 找到 `Q=(+,-,-,-)`、`tau=(+,+,-,+,-,-,+,-)` 的 period-8 family。8 阶 Floquet 多项式精确化为 `P(y,c)=y^4-16y^3+(80-2c)y^2+(-128+16c)y+c^2-13c+38`。有理正性证明对所有 Bloch 相位有 `rho(A)^2<1561/200`；Taylor 有理下界证明 `rho_-(n)^2>1561/200` 对所有 `8|n,n≥32` 成立。故原猜想存在无限反例族。
- **独立审计：** 对显式 `n=32,alpha=+1` signing，Bareiss leading minors 与独立 rational `LDL^T` 均证明 `1561 I-200A^2` 正定；代数阈值隔离区间的下端点严格大于 `1561/200`。另保留 period-10、`n=50` 的独立反例族和整数证书。
- **证据等级：** 无限族论证为 **Proved（待独立人工审计）**；具体 `n=32` witness 为 **Verified**。未证明 `n=32` 是最小反例。
- **下一步：** 独立重推 Floquet determinant；检查 `n=24,26,28,30` 以确定最小反例范围；整理 claim-source map 与论文草稿。

---

## 2026-08-15 — Target A Tasks 30–32：发现冻结与 quotient 完整性审计

- **研究对象：** Target A 否证后的研究冻结和最小性搜索前置审计。
- **Task 30：** 从 `main@fb4375f` 建立 `agent/target-a-discovery-snapshot`；创建 `research/checkpoints/TARGET_A_DISCOVERY_SNAPSHOT.md`，冻结 period-8 无限族、`n=32` 双正定证书、`n=20,22` 搜索、period≤12 探索、环境、命令和 SHA-256。明确 `n=32 is the smallest counterexample` 为 `UNRESOLVED`。本地快照提交为 `21d5b84`，未 push。
- **Task 31：** 创建 `research/experiments/TARGET_A_MINIMALITY_SEARCH_PLAN.md`。Burnside 精确计数给出 `n=24,26,28,30` 分别有 353,812、1,299,064、4,810,472、17,929,600 个含 alpha quotient states；设计 direct-bracelet 流生成、defect-shell checkpoint、输入/证书哈希链、rational Rayleigh 与 exact fallback。未开始 `n≥24` 谱搜索。
- **Task 32：** 重跑 `n=20` 全部 2,097,152 raw switching classes，并与 27,296 quotient states 比较；global minimum、2 个 optimizer、smallest nonoptimizer `(Q-code=17425,alpha=-1)`、0 counterexample 和 orbit-size 空间恢复均一致。固定种子 `20260815` 抽取 32 个 `n=22` quotient states，展开 1,386 个 dihedral 成员和 2,772 个 global-sign switching classes；每个成员均找到精确 automorphism/switching/global-negation 关系。审计状态 `PASS`。
- **哪些失败：** 无数学或枚举失败。识别出当前 visited-array generator 在 `n=30` 会预分配约 1 GiB，因此计划要求生产搜索前实现并再次审计 constant-memory bracelet stream。
- **证据等级：** quotient 完整性数学论证和显式等价检查为 **Verified/PASS**；`n=24,26,28,30` 最小性结论仍为 **UNRESOLVED**。
- **下一步：** 按 stop point 停在 Task 33 前；下一轮先实现并验证 direct bracelet stream，然后执行完整 `n=24` 搜索。

---

## 2026-08-15 — Target A Task 33A：constant-memory bracelet stream

- **研究对象：** `n=24,26,28,30` 最小性搜索所需的生产级 Q-bracelet 枚举基础设施。
- **做了什么：** 新增独立 fixed-weight FKM necklace 递归生成器，按反射最小方向合并为 binary bracelets，并由最小周期精确给出二面体轨道大小；保留旧 visited-array 生成器作为参考实现。完整逐项比较每个偶数 `n=8,...,22` 的 defect count、canonical Q-code 和 orbit size；对 `n=24,26,28,30` 流式核对 fixed-weight Burnside 分层、总数、轨道覆盖、稳定顺序、SHA-256 与峰值 traced memory。
- **得到什么：** 审计总状态 `PASS`。`n=24,26,28,30` 的 Q-bracelet 数分别为 176,906、649,532、2,405,236、8,964,800，对应 353,812、1,299,064、4,810,472、17,929,600 个 `(Q,alpha)` 谱状态。峰值 traced memory 分别为 16,840、18,992、20,464、21,968 bytes；生成器不保留输出集或 `2^n` visited 表。
- **哪些失败：** 无数学、计数或实现失败。启用 `tracemalloc` 的完整审计耗时 1,354.73 秒，其中 `n=30` 为 1,020.00 秒；这是一次性内存审计开销，不是谱搜索耗时。
- **证据等级：** `n<=22` 新旧完整有序流等同性和 `n=24,26,28,30` Burnside/覆盖核对为 **Verified/PASS**。本任务没有执行 `n>=24` 谱搜索，因此最小反例结论仍为 **UNRESOLVED**。
- **产物：** `research/scripts/target_a_bracelets.py`、`research/scripts/target_a_direct_generator_audit.py`、`research/audit/DIRECT_BRACELET_GENERATOR_AUDIT.md`、`research/audit/direct_bracelet_generator_audit.json`。
- **下一步：** Task 33B 仅执行完整 `n=24` 谱搜索，并使用已审计的 direct bracelet stream、defect-shell checkpoint 与精确证书链。

---

## 2026-08-15 — Target A Task 33B：n=24 生产级完整搜索

- **研究对象：** C029 Conjecture 3 在 `n=24` 的完整有限验证。
- **做了什么：** 新增 production minimality driver，仅流式调用已审计的 direct bracelet generator；启动谱计算前重新核对 Burnside 总数和每个 defect shell；对每个 `(Q,alpha)` 精确反向重构；用单次 dense eigendecomposition 提议整数向量，再以有理 Rayleigh 下界对认证阈值上界作严格比较；optimizer 单独使用最小多项式整除与根隔离；以 28 个不可变 chunk 保存输入/证书摘要、内容哈希和连续 hash chain，并完成无谱 resume 重放审计。
- **得到什么：** `VERIFIED_NO_COUNTEREXAMPLE_AT_N24`。176,906/176,906 个 Q-bracelets、353,812/353,812 个谱状态全部完成，恢复 33,554,432 个 switching classes。optimizer 精确等于阈值；其余 353,811 个状态全部 `RAYLEIGH_CERTIFIED`，exact fallback 0、反例 0。因此 Conjecture 3 对 `n=24` 成立。
- **新发现：** OBSERVED numeric top-100 中最低非 optimizer 为 `Q-code=1118481, d=6, alpha=-1`，缺陷位置 `0,4,8,12,16,20`，数值 gap 约 `0.00908278`。未做 exact second-minimum 排序。
- **哪些失败：** 首轮成功完成后发现结果 JSON 未顶层保存实际使用的 `rho_-(24)^2` 有理隔离区间；补齐字段后从空 checkpoint 重新完整运行，输入摘要、证书摘要和最终链均与首轮一致。没有数学或搜索失败。
- **证据等级：** `n=24` 全 quotient 搜索、optimizer 等号和全部非 optimizer 排除为 **Verified/PASS**。`n=32` 是否为最小反例仍为 **UNRESOLVED**，因为 `n=26,28,30` 尚未检查。
- **产物：** `research/scripts/target_a_minimality_search.py`、`research/logs/target_a_search_n24.json`、`research/logs/checkpoints/n24/`、`research/experiments/TARGET_A_N24_RESULT.md`。结果 JSON SHA-256 为 `3fea700914b3c2d8a08a26bbaf490432123ed1a877c231f0d53ddbdf8f394a51`；checkpoint manifest SHA-256 为 `978b38db75ccf8d05bd7bae76b28373d5a0b56655299ea2a65cc25722514a98b`。
- **下一步：** Task 34 仅执行 `n=26` 完整搜索；本任务没有启动 `n=26,28,30`。

---

## 2026-08-15 — Target A Task 34：n=26 生产级完整搜索

- **研究对象：** C029 Conjecture 3 在 `n=26` 的完整有限验证。
- **做了什么：** 复用 Task 33B 的 direct-stream、roundtrip、exact optimizer、rational Rayleigh 与 immutable checkpoint pipeline；只增加 `n=26` 硬编码 Burnside 门、结果 provenance 字段和不参与判定的 period-4 Q-pattern 二面体 Hamming distance。修改后完整回归 `n=8,10,12`，并只读重放 `n=24` 的 28 个 chunks、输入摘要、证书摘要和最终链，全部一致后才启动正式搜索。
- **得到什么：** `VERIFIED_NO_COUNTEREXAMPLE_AT_N26`。649,532/649,532 个 Q-bracelets、1,299,064/1,299,064 个谱状态全部完成，恢复 134,217,728 个 switching classes。optimizer 精确等于阈值；其余 1,299,063 个状态全部 `RAYLEIGH_CERTIFIED`，exact fallback 0、反例 0。因此 Conjecture 3 对 `n=26` 成立，严格有限验证范围扩展到所有偶数 `n=8,10,...,26`。
- **新发现：** OBSERVED numeric top-100 中最低非 optimizer 为 `Q-code=1118481, d=6, alpha=+1`，缺陷间隔 `4,4,4,4,4,6`，到 period-4 Q-pattern 的二面体最小 Hamming distance 为 1，数值 gap 约 `0.03250783`。这与不能被 4 整除的有限尺寸 period-4 近似一致，但未作 exact ordering 或理论结论。
- **哪些失败：** 无数学、搜索或 checkpoint 失败。正式运行后只读重放 76 个 chunks，再次验证完整 generator cursor、计数、输入/证书摘要、最终链、optimizer 和零反例。
- **证据等级：** `n=26` 全 quotient 搜索、optimizer 等号和全部非 optimizer 排除为 **Verified/PASS**。`n=32` 是否为最小反例仍为 **UNRESOLVED**，因为 `n=28,30` 尚未检查。
- **产物：** `research/logs/target_a_search_n26.json`、`research/logs/checkpoints/n26/`、`research/experiments/TARGET_A_N26_RESULT.md`。结果 JSON SHA-256 为 `9cb022a9bc7ba5e2ad7d8d1d0427ec3073a64aae60a09ef032f0a2286875f815`；checkpoint manifest SHA-256 为 `59d106f91ff5bd457e25c1676233970ee46382e4ace7c8e41b7769b85d5b140d`。
- **下一步：** Task 35 仅执行 `n=28` 完整搜索；本任务没有启动 `n=28,30`。

---

## 2026-08-15 — Target A Task 35：n=28 生产级完整搜索

- **研究对象：** C029 Conjecture 3 在 `n=28` 的完整有限验证。
- **做了什么：** 冻结既有 quotient 与 exact-decision pipeline；新增 `n=28` Burnside 硬门、period-4 distance-0 parity guard 和全流 `best_numeric_by_period4_distance` 诊断。正式搜索前默认/minimality/generator tests 通过，并只读重放 `n=24,26` 的计数、游标、输入/证书摘要、optimizer、零反例和最终链。正式搜索后再次只读重放全部 250 个 `n=28` chunks。
- **得到什么：** `VERIFIED_NO_COUNTEREXAMPLE_AT_N28`。2,405,236/2,405,236 个 Q-bracelets、4,810,472/4,810,472 个谱状态全部完成，恢复 536,870,912 个 switching classes。optimizer 精确等于阈值；其余 4,810,471 个状态全部 `RAYLEIGH_CERTIFIED`，exact fallback 0、反例 0。因此 Conjecture 3 对 `n=28` 成立，严格有限验证范围扩展到所有偶数 `n=8,10,...,28`。
- **新发现：** n=28 没有非法 distance-0 记录。OBSERVED numeric 最低非 optimizer 为 `Q-code=4460817, d=6, alpha=-1`，缺陷间隔 `4,4,4,6,4,6`，period-4 distance 为 5，数值 gap 约 `0.02631274`。distance-1 类最佳为 `Q-code=1118481, alpha=-1`，gap 约 `0.03165537`，并非整体最低。自动日志表给出 n=24/26/28 的最佳 observed distance 为 0/1/5。
- **哪些失败：** 首次组合 n=24/n=26 双重放命令因过度压缩的一行 Python 和 shell 引号各发生一次解析失败；均未读取完成或改写 checkpoint。改用仓库外临时只读脚本后，两组重放全部 PASS，临时脚本随即删除。没有数学、搜索或 checkpoint 失败。
- **证据等级：** `n=28` 全 quotient 搜索、optimizer 等号和全部非 optimizer 排除为 **Verified/PASS**。period-4 表仅为 **Observed**。`n=32` 是否为最小反例仍为 **UNRESOLVED**，因为 `n=30` 尚未检查。
- **产物：** `research/logs/target_a_search_n28.json`、`research/logs/checkpoints/n28/`、`research/experiments/TARGET_A_N28_RESULT.md`、`research/logs/target_a_period4_diagnostic_n24_28.json`。结果 JSON SHA-256 为 `07644fbae5bbb93da64bc9d532a1a4a41bc38d013dd96ab2b19524f0fe524269`；checkpoint manifest SHA-256 为 `e1d1411f0563915c282651d12858c77671b5a8153ac2b47357373d7963b2fc91`。
- **下一步：** Task 36 仅执行 `n=30` 完整搜索；本任务没有启动 `n=30`。

---

## 2026-08-15 — Target A Task 36：n=30 生产级完整搜索

- **研究对象：** C029 Conjecture 3 在 `n=30` 的完整有限验证，以及偶数 `n=8,...,30` 的有限范围闭合。
- **做了什么：** 增加 `n=30` Burnside 分层硬门；将 period-4 参照统一为从索引 0 开始的长度 `n` 截断，并按参照 defect 奇偶验证全流距离奇偶；新增可复用的只读 checkpoint replay 工具。正式搜索前默认与聚焦测试通过，并用该工具重放 `n=24,26,28`；正式搜索后独立重放全部 908 个 `n=30` chunks。扩展自动诊断表到 `n=24,26,28,30`。
- **得到什么：** `VERIFIED_NO_COUNTEREXAMPLE_AT_N30`。8,964,800/8,964,800 个 Q-bracelets、17,929,600/17,929,600 个谱状态全部完成，恢复 536,870,912 个 Q-vectors 和 2,147,483,648 个 switching classes。optimizer 精确等于阈值；其余 17,929,599 个状态全部 `RAYLEIGH_CERTIFIED`，exact fallback 0、反例 0。因此 Conjecture 3 对 `n=30` 成立，严格有限验证范围闭合到所有偶数 `n=8,10,...,30`。
- **新发现：** `n=30` period-4 参照 defect 数为 8，合法距离均为偶数，完整诊断观察到距离 `0,2,...,22`。OBSERVED numeric 最低非 optimizer 为 `Q-code=17843217, d=6, alpha=+1`，缺陷间隔 `4,6,4,6,4,6`，period-4 distance 为 6，数值 gap 约 `0.01882988`；distance 0 类并非整体最低。自动表中 `n=24/26/28/30` 最佳 observed distance 为 `0/1/5/6`。
- **哪些失败：** 无数学、搜索、checkpoint 或重放失败。正式运行耗时 1,498.36 秒，峰值 RSS 122,224,640 bytes。
- **证据等级：** `n=30` 全 quotient 搜索、optimizer 等号和全部非 optimizer 排除为 **Verified/PASS**。项目状态为 **FINITE_RANGE_COMPLETE_THROUGH_N30**；本任务没有组装或宣称 `SMALLEST_COUNTEREXAMPLE_VERIFIED`。
- **产物：** `research/logs/target_a_search_n30.json`、`research/logs/checkpoints/n30/`、`research/experiments/TARGET_A_N30_RESULT.md`、`research/logs/target_a_period4_diagnostic_n24_30.json`、`research/scripts/target_a_checkpoint_replay.py`。结果 JSON SHA-256 为 `34bbeba4b07723eff94eb8cc7b19f640ea2c07674e72cb5b91b3c74ba1a0b449`；checkpoint manifest SHA-256 为 `56b0cc2c8d12da9d99ca49d66d136d7b40a517cb4211f8fed5eb7b69c83ec7d4`。
- **下一步：** Task 36A 仅汇编并独立审计偶数 `n=8,...,30` 的完整无反例证据与既有 `n=32` 精确 witness，形成最小反例证书；不新增谱搜索。

---

## 2026-08-15 — Target A Task 36A：最小反例阶数认证

- **研究对象：** 独立审计 Target A 的完整有限排除链与冻结的 `n=32` 显式反例，并认证最小 admissible failure order。
- **做了什么：** 从 `TARGET_A_SPEC.md` 的 Domain 规则程序生成 `8,10,...,30`，逐项读取而非信任 Markdown 摘要：`n=8,...,20` raw switching-class JSON、`n=22` full quotient JSON、`n=24,26,28,30` production result 与 manifests。重新计算全部依赖 SHA-256；两次只读重放四组 production checkpoints。新增不导入 witness constructor 的 `n=32` checker，直接重建 32 阶矩阵、flux 与 holonomy，独立重算 Bareiss 和有理 LDL 正定性及阈值代数比较。新增总证书、最小依赖 manifest、独立总 checker 与六类篡改负测。
- **得到什么：** `SMALLEST_COUNTEREXAMPLE_VERIFIED`。Conjecture 3 的 admissible domain 恰为所有偶数 `n>=8`；完整精确计算排除全部 `n=8,10,...,30`；冻结 signing 在 `n=32` 满足 `rho(A)^2 < 1561/200 < rho_-(32)^2`。因此 `n=32` 是最小反例阶数。
- **证据性质：** 最小性结论是 **有限范围 exhaustive exact computation + 显式 exact witness**，不是 computation-free proof。没有宣称 `n=32` 反例唯一、switching class 唯一、period-8 family 全局最优，或所有偶数 `n>=32` 均失败；无限族边界仍为 `8|n, n>=32`。
- **哪些失败：** 无证据、checker、重放或数学失败。删除 `n=28`、篡改 `n=30` SHA、把首阶改为 34、修改 witness 边符号、把有限反例数改为 1、把 completion fraction 降到 1 以下的临时负测均按要求失败，未修改 committed evidence。
- **验证：** `N32_CERTIFICATE_PASS`；`TARGET_A_MINIMALITY_CERTIFICATE_PASS`（状态升级前后各完整运行一次）；默认 36 项测试中 33 PASS、3 个既有慢测跳过；JSON parse、compileall 与 diff 检查 PASS。
- **产物：** `research/counterexamples/target_a_minimality_certificate.json`（SHA-256 `1f20469033876569292de247344ba88eb0831c163e01c1441f1b75aa8bca95c7`）；`research/audit/TARGET_A_MINIMALITY_DEPENDENCIES.json`（SHA-256 `5bb4a6c39039bb76e41945c0c1f0dffd545b778c0230ce85d3f905bc197b284f`）；`research/audit/target_a_minimality_checkpoint_replay.json`（SHA-256 `bcfcb67f6b1e67f7d7ec36552c99aeebfcd8811a46ef697de7314b4ad2311d57`）；`research/proofs/TARGET_A_SMALLEST_COUNTEREXAMPLE.md`；两个独立 checker 及测试。
- **下一步：** Task 37 从定义使用第二套实现独立重构 `n=32` witness；随后 Task 38 从零独立推导并审计 period-8 Floquet 行列式与证明。本任务不开始论文正文。

---

## 2026-08-15 — Target A Task 37：n=32 witness 第二套独立重构

- **研究对象：** 从 `n=32`、period-8 triangle flux `(+,+,-,+,-,-,+,-)` 与 `alpha=+1` 出发，以不依赖现有 constructor/helper 的第二套实现重构显式反例，并审计其与冻结 witness 的 switching class 一致性。
- **做了什么：** 选择非平凡确定性 gauge `a=(+,-,+,-,-,+,-,+)^4`，直接按定义 `b_i=tau_i a_i a_(i+1)` 得到 step-2 signs `(-,-,+,+,+,+,-,-)^4`；独立重建 32 阶整数邻接矩阵。脚本先原子写入 construction snapshot 并固定 SHA，之后才读取冻结 witness。由 step-1 方程从 `d_0=+1` 递归求得 `d=(+,+,-,-,+,-,-,+)^4`，逐边核对 32 条 step-1 与 32 条 step-2 方程，并直接验证完整 `A_ind=D A_frozen D`。
- **得到什么：** `N32_WITNESS_INDEPENDENTLY_RECONSTRUCTED`。反向重建 `tau=(+,+,-,+,-,-,+,-)^4`、`Q=(+,-,-,-)^8`、`alpha=+1` 全部一致；`charpoly(A)` 与 `charpoly(A^2)` 均和冻结 witness 精确相同。新实现的 fraction-free Bareiss 与 rational LDL 各得 32 个正 pivot，exact algebraic comparison 再次证明 `rho(A_ind)^2 < 1561/200 < rho_-(32)^2`。
- **独立性边界：** 新脚本只导入 Python 标准库与 SymPy；未导入 period-8 family、flux search、minimality search、reproduction、现有 witness constructor、Q/triangle reconstruction helper 或 `verify_target_a_n32_certificate.py`；未使用浮点本征值。它只审计具体 witness，不把 period-8 infinite-family proof 标为 independently audited。
- **哪些失败：** 无构造、switching、矩阵、谱一致性或证书失败。临时负测修改一条冻结 step-2 边时 switching audit 按要求失败；修改 tau 输入时 reconstruction 按要求失败；未改写冻结 witness。
- **验证：** Task 37 tests 11/11 PASS；默认 47 项中 44 PASS、3 个既有慢测跳过；Target A 聚焦 tests 34/34 PASS；`N32_CERTIFICATE_PASS`；`TARGET_A_MINIMALITY_CERTIFICATE_PASS`（含 `n=24,26,28,30` 只读重放）；JSON parse、compileall 与 diff 检查 PASS。
- **产物：** `research/audit/target_a_n32_independent_reconstruction.json`（SHA-256 `53b9b117b074427134e7e8f71838d5b2af85930492e988a8c1d17d9542fd7b7a`）；`research/audit/n32_witness_reconstruction_audit.json`（SHA-256 `35a28ffb95cb1ab1e15838997b7fc9a696d7f69caa70a4aeafd50f653bc5c543`）；`research/audit/N32_WITNESS_RECONSTRUCTION.md`（SHA-256 `5836edf9b59c4fa926c53b69e8cfa9af18bf640f5e88d42590ded5afd32b7d1c`）；`research/scripts/target_a_n32_independent_reconstruction.py` 及测试。
- **下一步：** Task 38 从零独立推导 period-8 Floquet reduction 与 determinant，并审计无限反例族证明。本任务没有开始论文正文、novelty audit 或任何新搜索。

---

## 2026-08-15 — Target A Task 38：period-8 Floquet reduction 与 determinant 独立审计

- **研究对象：** 从 period-8 triangle flux `(+,+,-,+,-,-,+,-)`、`n=8L` 与 twisted condition `x_(i+n)=alpha*x_i` 出发，建立不依赖旧 family helper 的有限矩阵到 `8 x 8` Floquet block 与特征行列式的第二条推导链。
- **做了什么：** 从 Hamilton-cycle gauge 的 edge signs 重新推出 local operator，并对 `alpha=+-1` 直接比较 finite gauge 与 twisted-boundary 的 32 阶整数矩阵；按 `i=8m+r` 生成 32 条 residue/cell-shift transition；由 `u_m=z^m v` 推出 `z^L=alpha` 和 `|z|=1`，再直接从 transition table 生成 `H(z)`。以 cell shift 的正交特征基、8 维不变子空间和 `L*8=8L` 维数计数证明 direct sum；对 `L=4, alpha=+-1` 用 full charpoly 与 resultant block product 作 exact regression。
- **得到什么：** `PERIOD8_FLOQUET_DETERMINANT_INDEPENDENTLY_AUDITED`。符号检查 `H(z)` 在单位圆上 Hermitian；SymPy determinant 与手写 fraction-free Bareiss 完全一致，自动出现 `x` 偶性和 `z -> z^-1` 对称。由 Laurent coefficients 和 Chebyshev recurrence 自动得到 `P_ind(y,c)=y^4-16y^3+(80-2c)y^2+(-128+16c)y+c^2-13c+38`；独立 snapshot 冻结后才读取旧 certificate，9 个非零 monomial coefficients 逐项一致。
- **逻辑连接：** `z^L=alpha` 给出 `|z|=1` 和 `c=z+z^-1=2cos(theta) in [-2,2]`；Hermitian 性保证 eigenvalue `lambda` 为实数，因此 `det(lambda I-H)=0` 严格推出 `P(lambda^2,c)=0` 且 `lambda^2>=0`。同一 `H(z)` 与 `alpha` 无关，`alpha` 只选择 admissible roots。
- **独立性与边界：** 新脚本只导入标准库与 SymPy，未导入 period-8 family/search/reproduce、旧 Floquet symbol、polynomial 或 determinant helper；冻结旧证据仅在独立 transition 与 polynomial snapshot 写入并固定 SHA 后读取。本任务不证明 `P(y,c)>0` for `y>=1561/200`，也不重审全 `n` threshold，因此没有写 `PERIOD8_INFINITE_FAMILY_INDEPENDENTLY_AUDITED`。
- **负向测试：** flip 一个 tau sign 会改变 determinant；篡改 cell shift、复用错误 alpha root set、把一个 `z^-1` wrap entry 改成 `z`、篡改 frozen coefficient、删除一个 Bloch block 均按要求 FAIL，未修改 committed evidence。
- **验证：** Task 38 tests 20/20 PASS；`alpha=+1` 与 `alpha=-1` exact finite consistency PASS；已有 Task 37、n32 certificate、minimality certificate 及 Target A/default regression 保持 PASS；JSON parse、compileall 与 diff 检查 PASS。
- **产物：** `research/audit/target_a_period8_cell_transitions.json`（SHA-256 `e40f49a274904c73765c5703c099bbb3307d67b3905cb8cecd9d9016f26e6f17`）；`research/audit/target_a_period8_independent_polynomial.json`（SHA-256 `cc26dedfee3fe3e6c0674f1b217fde592a043a5d8b4913752dc37ad2a62193b2`）；`research/audit/period8_floquet_independent_audit.json`（SHA-256 `2a5657d0791b1e1a3c742ae8e0a738f083115b4e4516e5e8d8fd4d1999d6c3ee`）；`research/audit/PERIOD8_FLOQUET_INDEPENDENT_AUDIT.md`（SHA-256 `e2b6d588dcef4b49813b939bbb902a74aab290bb1403578999af0bf50fb56309`）；独立脚本及测试。
- **下一步：** Task 39 独立证明 `P(y,c)>0` for `y>=1561/200, c in [-2,2]` 与 `1561/200<rho_-(n)^2` for every `8|n, n>=32`，再升级完整无限反例族的独立审计状态。

---

## 2026-08-16 — Target A Task 39：period-8 无限反例族完整独立审计

- **研究对象：** 以 Task 38 独立审计并固定 SHA 的 `P(y,c)`、Hermitian/root-link 与 Floquet direct sum 为唯一理论依赖，独立证明所有 `L>=4`、`alpha=+-1` 的 period-8 signing 满足 `rho(A)^2<1561/200<rho_-(8L)^2`。
- **主 positivity 证书：** 从 Task 38 coefficient map 重建而非手写 `P`。置 `B=1561/200`、`u=y-B`、`t=2-c` 后自动展开为 9 项；所有系数非负且常数 `84332641/1600000000` 严格为正，因此直接证明更强区域 `P(y,c)>0` for `y>=B, c<=2`。主 snapshot 在 secondary threshold route 前冻结。另以自动导出的 `c`-vertex 与 `P(B+u,2)` 全正系数作独立 cross-check。
- **谱逻辑：** Task 38 保证 admissible `H(z)` Hermitian、`lambda` 为实数且 `P(lambda^2,c)=0`。若 `lambda^2>=B` 将与严格 positivity 矛盾，故所有 block 及其 direct sum 都满足严格 `rho^2<B`；同一论证覆盖 `alpha=-1,+1`。
- **主 threshold 证书：** 从 `TARGET_A_SPEC.md` 的定义与 `cos^2(theta)=(1+cos(2theta))/2` 自动推出 `rho_-^2(n)=4+2cos(2pi/n)+2cos(4pi/n)`。在 `n=32` 用两次正半角构造 exact radical，自动得到八次 minimal polynomial；Sturm 证明 `(7809/1000,781/100)` 恰含一个实根，并以 exact algebraic comparison 识别该根，从而 `1561/200<rho_-^2(32)`。初等 cosine monotonicity 将严格下界推广到所有 `n>=32`，最终仅限制到真实 family domain `n=8L, L>=4`。
- **第二 threshold 路线：** 独立重算 alternating Taylor lower polynomial 与 `9<pi^2<10`，精确恢复 `1178731111/150994944`，其超过 `B` 的差为 `5389327/3774873600`。该路线只作 secondary cross-check。
- **负向测试：** 篡改一个 `P` coefficient、令 positivity 常数为负、从 `L=3/n=24` 开始、误纳 `n=30`、破坏 Task 38 audit SHA、删除 `alpha=-1`、使用空 isolating interval、宣称 all even `n>=32` 均按要求 FAIL；临时 fixtures 未修改 committed evidence。
- **状态与证据边界：** 新增 `PERIOD8_INFINITE_FAMILY_INDEPENDENTLY_AUDITED`，但不声明所有偶数 `n>=32` 失败、period-8 optimal、`n=32` witness 唯一或全局最小谱半径已知。README、registry 与原 period-8 proof 已同步。`TARGET_A_SPEC.md` 因 Task 36A minimality certificate 和 dependency manifest 固定整文件 SHA 而保持字节不变；当前审计状态由上述非冻结状态文档记录，避免改写 finite-range evidence。
- **验证：** Task 39 tests 23/23 PASS；Target A focused tests 77/77 PASS；default 90 项中 87 PASS、3 个既有慢测跳过；`TARGET_A_PERIOD8_INFINITE_FAMILY_PASS`；`N32_CERTIFICATE_PASS`；`TARGET_A_MINIMALITY_CERTIFICATE_PASS`（含 `n=24,26,28,30` 完整只读重放）；JSON parse、compileall、禁止导入与 diff 检查 PASS。
- **产物：** `research/audit/target_a_period8_uniform_positivity_snapshot.json`（SHA-256 `86d2e7d09534162187699a693d1432a976f2183d9ce06a96cbb40148bb939124`）；`research/audit/period8_infinite_family_independent_audit.json`（SHA-256 `b36bce66ec367e418e1499a1400773147d29537da92a49695b8d7dc9c1c08fa8`）；`research/audit/PERIOD8_INFINITE_FAMILY_INDEPENDENT_AUDIT.md`（SHA-256 `8e9e497375d1df759727d517e2ec26e3b08cf3d023a0cfe9215baa4ec0377bc3`）；主审计脚本、独立总 checker 与测试。
- **下一步：** Task 40A 从 audited `P(y,c)` 求 period-8 phase 的 sharp infinite-volume spectral radius；本任务不开始论文正文、optimality search 或 novelty audit。

---

## 2026-08-16 — Target A Task 40A：period-8 sharp spectral constant

- **研究对象：** 从 Task 38 审计的 `P(y,c)` 精确求 period-8 phase 的 infinite-volume sharp squared spectral constant，并分别刻画有限 `alpha=+1` 与 `alpha=-1` holonomy sectors。
- **端点与常数：** 自动重建 `P(y,2)=y^4-16y^3+76y^2-96y+16`；置 `x=y-4` 得 `x^4-20x^2+80`。最大非负根为 `eta=4+sqrt(10+2sqrt(5))`，故 `rho_*=sqrt(eta)`。`eta` 的最小多项式为 `Y^4-16Y^3+76Y^2-96Y+16`，隔离区间为 `(1951/250,1561/200)`；`rho_*` 的最小多项式为 `R^4-2R^3-6R^2+12R-4`，隔离区间为 `(2793/1000,1397/500)`。
- **sharp positivity 证书：** 置 `s=sqrt(10+2sqrt(5))`、`u=y-eta`、`t=2-c` 后，自动展开
  `P(eta+u,2-t)=u^4+4su^3+2u^2t+(40+12sqrt(5))u^2+4sut+8sqrt(5)su+t^2+(4sqrt(5)-3)t`。
  八个非常数系数均严格为正，纯 `u` 与纯 `t` 项给出 `P>=0` 且等号当且仅当 `(u,t)=(0,0)`。因此 `sup_(|z|=1) rho(H(z))^2=eta`，并且唯一 band edge 为 `c=2`，即唯一 `z=1`。
- **top-root 单调性：** 令 `r(c)` 为 `P(y,c)` 的最大非负根。由 `P(y,-2)` 的最大根 `y_0=6+sqrt(2)`、`P(y_0,c)=(c+2)(c+5-8sqrt(2))` 及 `c_0(y)=y^2-8y+13/2` 在相关根支上严格大于 2，证明 `r(c)` 在 `[-2,2]` 严格递增。
- **有限 holonomy 结论：** 对每个 `L>=1`，`alpha=+1` 的 admissible phases 含 `z=1`，故最大 squared radius 精确等于 `eta`；`alpha=-1` 的最大 `c` 为 `2cos(pi/L)<2`，故最大 squared radius为 `r(2cos(pi/L))<eta`，且随 `L -> infinity` 收敛到 `eta`。
- **旧界比较：** 精确证明 `eta<1561/200`，差为 `761/200-sqrt(10+2sqrt(5))>0`；因此 Task 39 的 `B=1561/200` 是严格统一上界，但不是 sharp constant。
- **边界：** 本任务只解决固定 period-8 phase 的 sharp spectral constant；没有搜索或声明该 phase 在所有 signing 中最优，也没有开始论文正文、classification 或 novelty audit。
- **负向测试：** 较小端点根冒充最大根、篡改 radical、负 positivity 系数、在 `c<2` 宣称达到 sharp 值、`alpha=-1` 有限达到 `eta`、把其最大 `c` 写成 2、破坏 Task 39 SHA、把旧 `B` 宣称为 sharp，八类 fixtures 均按要求失败。
- **验证：** Task 40A tests 23/23 PASS；Target A focused tests 100/100 PASS；default 113 项中 110 PASS、3 个既有慢测跳过；`TARGET_A_PERIOD8_SHARP_CONSTANT_PASS`、`TARGET_A_PERIOD8_INFINITE_FAMILY_PASS`、`N32_CERTIFICATE_PASS`、`TARGET_A_MINIMALITY_CERTIFICATE_PASS`；JSON parse、compileall、禁止导入与 diff 检查 PASS。
- **产物：** `research/scripts/target_a_period8_sharp_constant.py`（SHA-256 `b83879735be6641b82b4ab032b825e06ea999ba23d83eaa141f0557c3b1e0c3e`）；`research/scripts/verify_target_a_period8_sharp_constant.py`（SHA-256 `04aadb96462b3cd7febe75887cacdffffbbcd1c8d7b641dec80489994cbe049b`）；`research/proofs/target_a_period8_sharp_constant.json`（SHA-256 `f742f79d804f3c44da18dcb4b6562d4d7d1eb75e9f631133bc7314c475dbaa63`）；`research/proofs/TARGET_A_PERIOD8_SHARP_CONSTANT.md`（SHA-256 `e912a020ae2dc0931903b07172ec44f8823902c49a09f08356795c4ffa3e1c72`）；独立 checker 与测试。
- **下一步：** Task 40B 研究 period-8 sharp constant 附近的结构分类与候选最优性边界；在建立新证据前不升级为所有 signing 的全局最优结论。

---

## 2026-08-16 — Target A Task 40B：period-8 flux phases 完整分类与唯一最优相

- **研究对象：** 完整分类所有 8-periodic infinite-volume flux phases，判断 Task 40A phase 是否为 period-8 唯一 minimizer，并确定 runner-up 与 exact gap；不比较 arbitrary periods、所有 signings 或 finite-L global optima。
- **phase space 完整性：** 从定义枚举 256 个 `tau in {+-1}^8`，按 `Q_i=tau_i tau_(i+1)` 得 128 个合法 parity-even `Q`，每个 fiber 恰为 `tau,-tau`。Route A 显式生成 rotation/reflection orbits；Route B 独立计算 16 个 `D_8` 元素的 fixed points 并用 Burnside lemma 复核。两路均得 18 个 orbits，shell counts 为 `d=0/2/4/6/8: 1/4/8/4/1`，orbit sizes 之和为 128。
- **独立 Bloch 构造：** 新分类器不导入既有 period-8/family/search/reproduce helper，直接从 `(A_tau x)_i=x_(i-1)+x_(i+1)+tau_(i-2)x_(i-2)+tau_i x_(i+2)` 生成 crossing-number Bloch entries。18 类逐一符号验证 `H(z)^T=H(z^-1)`、`z=+-1` integral symmetric，以及 `H_(-tau)(z)=-D H_tau(z)D`。
- **完整排名：** target word `10001000` 的 canonical orbit 为 `P8-06: 00010001`，orbit size 4、primitive Q period 4、primitive tau period 8。Task 40A 给出 `R(P8-06)=eta=4+sqrt(10+2sqrt(5))<8`。对其余 17 类，程序在 `z=+-1` 与 `v in {-1,0,1}^8` 中自动找到 exact Rayleigh certificates；全部证明 `R>=8`，其中除 runner-up 外的 16 类全部严格 `R>8`。
- **唯一第二名：** all-unbalanced `P8-01: Q=(-)^8` 的 lift 为 `tau_i=(-1)^i`。fresh operator derivation 给出 `A=C+DE` 与 `A^2=4I+S^2+S^-2+S^4+S^-4<=8I`；`z=1, v=(-1)^8` 达到 quotient 8。因此它唯一满足 `R=8`，是唯一 runner-up。exact squared gap 为 `4-sqrt(10+2sqrt(5))`，radius gap 为 `2sqrt(2)-sqrt(4+sqrt(10+2sqrt(5)))`。
- **d=2 shell：** 四个 orbit 自动对应 cyclic separation `1,2,3,4`；前三者分别由 exact endpoint Rayleigh quotient 证明 `>8`，均匀 separation 4 即 target 满足 `eta<8`。结论是 finite exact shell classification，不宣称一般 separation monotonicity。
- **谱重合审计：** 18 类的 full Bloch characteristic signatures、squared characteristic signatures 和 `z=+-1` endpoint spectra 分别形成 18 个 exact classes。`P8-11/P8-12` 的相同 numeric band preview 只标为 **OBSERVED**，未冒充 exact sharp-constant coincidence。
- **状态与边界：** 新状态为 `PERIOD8_FLUX_CLASSIFICATION_COMPLETE`、`PERIOD8_UNIQUE_OPTIMUM_PROVED`、`PERIOD8_SECOND_BEST_GAP_PROVED`，总状态 `PERIOD8_UNIQUE_OPTIMUM_AND_SECOND_BEST_PROVED`。明确记录 `finite_size_global_optimality: NOT_CLAIMED`、`all_period_global_optimality: NOT_CLAIMED`、`all_signings_global_optimality: NOT_CLAIMED`。
- **负向测试：** 删除/重复 orbit、错误 orbit/shell/size、错误 reflection canonicalization、target rotation 识别失败、tau closure/reconstruction 损坏、Rayleigh vector/numerator/denominator/comparison 篡改、runner 仅下界冒充 exact、存在更优类或 tie 仍宣称 unique、Task 40A SHA 损坏，以及 finite/all-period/all-signings overclaim 均按要求 FAIL。
- **验证：** Task 40B tests 25/25 PASS；Target A focused tests 125/125 PASS；default 138 项中 135 PASS、3 个既有慢测跳过；Task 38 Floquet、Task 39 infinite family、Task 40A sharp、Task 40B classification、独立 n32 reconstruction、n32 certificate 与完整 minimality certificate 全部 PASS；JSON parse、compileall、forbidden-import、source-hash link、frozen SHA 与 diff 检查 PASS。
- **产物：** `research/proofs/target_a_period8_pattern_classification.json`（SHA-256 `a7a7b7259a99f099c7d2ab756a1a2f4c1ee233214f352d12df9e61cf1b47464c`）；`research/proofs/TARGET_A_PERIOD8_PATTERN_CLASSIFICATION.md`（SHA-256 `653f4b67401f8bb83aa043070260c3b5949a1fb833a72db0fc8b7a1b807ac05a`）；`research/audit/period8_pattern_classification_audit.json`（SHA-256 `274e80a6b43183d4a6137ac3d9a676e6942f1d84a46691cb2b63018b66c69e80`）；主分类器（SHA-256 `bacfd061e7ca7bbd33c07b6e9aea7186ef697aaa4c13468362dde338db98ca52`）、独立 checker（SHA-256 `17191409d23260853febc1551c2df3293b38c25f93daa70648b6f3c64f5b064a`）与测试。
- **下一步：** Task 40C 提炼 equal-spacing target 与 `8`-barrier 的结构机制，形成可复用 theorem package；随后 Task 41 才开始 current novelty audit。

---

## 2026-08-16 — Target A Task 40C：8-barrier、closed-walk moments 与 equal-spacing 机制

- **研究对象：** 将 Task 40B 的 18-orbit endpoint-Rayleigh 分类压缩为 period-8 structural reproof，解释 `Q=-1` cancellation、positive-flux defect geometry、closed-walk barrier 与 target chiral symmetry；不扩大到 arbitrary periods、finite-size global optimization 或所有 signings。
- **A² local formula：** 从 Hamilton-gauge 四条 transitions 逐项展开两步算子，对全部 256 个 `tau` 与 8 个 indices machine-check。对 odd displacements，系数统一含 `1+Q_i`：`Q_i=-1` 精确抵消，`Q_i=+1` 打开 amplitude `+-2`；共完成 4096 次 cancellation 与 4096 次 activation 检查。
- **moment framework：** 以 exact integer closed-walk dynamic programming 计算 `M_k=CT_z tr(H(z)^(2k))`，证明仅使用正确方向 `F_k=M_(k+1)-8M_k>0 => R>8`。自动从 exact expansion 推导并在 128 个合法 Q 上验证 `M_1=32`、`M_2=160+16d`、`M_3=944+168d+96a+48b`，故 `F_2=-336+40d+96a+48b`。
- **high-defect proof：** `d=4` 用四个 cyclic positive gaps 之和为 8 证明 `2a+b>=4`，故 `F_2>=16`；`d=6` 用两个 negative positions 最多破坏四条 adjacent positive edges 得 `a>=4`，故 `F_2>=288`；`d=8` 由 `F_1=32`。因此不引用 13 个 orbit witnesses 即得所有 `d>=4` phases 满足 `R>8`。
- **d=2 hierarchy：** separation `s=1,2,3` 的首次正 excess 精确为 `F_4=5504`、`F_6=64336`、`F_9=2872096`；检测尺度严格递增 `4<6<9`。`s=4` 的 `F_1,...,F_9` 全负，但明确不以此证明上界；它依赖 Task 40A 得 `R=eta<8`。因此 antipodal/equal-spacing pair 是 two-defect shell 唯一 sub-8 phase。
- **8-barrier trichotomy：** 对每个合法 period-8 Q，`R(Q)<8` 当且仅当 `D(Q)={j,j+4}`，此时 `R=eta`；`R(Q)=8` 当且仅当 `D(Q)=emptyset`，即 `Q=(-)^8`；其余全部 `R(Q)>8`。结构路线展开到 128 个 Q 后与 Task 40B 分类逐项一致：below/equal/above counts 为 `4/1/123`，mismatch 0。
- **chiral mechanism：** canonical target `Q=00010001` 自动重建 `tau=(+,-,+,-,-,+,-,+)` 与 `tau_(i+4)=-tau_i`。严格区分 raw `D*T4` 在 z-fiber 上平方为 `zI`；选择 `xi^2=z` 后以 `J_z=xi^-1 D T4(z)` 得 `J_z^2=I` 和 `J_z H(z) J_z^-1=-H(z)`，从而得到 `4+4` off-diagonal decomposition 与两个 squared 4-dimensional blocks。
- **anti-period-4 分类：** 精确证明 `tau_(i+4)=-tau_i` iff `Q_(i+4)=Q_i` 且前四项乘积为 -1。8 个 vectors 恰分成 canonical `00010001`（d=2 target）与 `01110111`（d=6, R>8）两个 D8 orbits，故 chiral symmetry 本身不足以保证 optimality。
- **逻辑与 scope：** negative `F_k` 不推出 `R<=8`，有限前十 moments 不证明 target bound。状态升级为 `PERIOD8_EIGHT_BARRIER_TRICHOTOMY_PROVED`、`PERIOD8_CLOSED_WALK_MECHANISM_PROVED`、`PERIOD8_TARGET_CHIRAL_MECHANISM_PROVED`，总状态 `PERIOD8_STRUCTURAL_MECHANISM_PROVED`；finite-size/all-period/all-signings optimality 均 `NOT_CLAIMED`。
- **负向测试：** A² index/coupling 方向、M2/M3 coefficient、exact CT 方法、moment 逻辑方向、d2 separation/first-positive、target anti-periodicity、J²/anticommutation、chiral overclaim、trichotomy coverage、all-unbalanced/non-target d2 classification、Task 40B mismatch、dependency SHA 与三类 scope overclaim 均按要求 FAIL。
- **验证：** Task 40C tests 28/28 PASS；Target A focused tests 153/153 PASS；default 166 项中 163 PASS、3 个既有 slow tests 跳过；Task 38 Floquet、Task 39 infinite family、Task 40A sharp、Task 40B classification、Task 40C mechanism、独立 n32 reconstruction、n32 certificate 与完整 minimality certificate 全部 PASS。
- **产物：** `research/proofs/target_a_period8_structural_mechanism.json`（SHA-256 `34212c53f16e2fe67e2ed2c7b00cd37f62e4fe97eae48d1e33e2350b40f3f728`）；`research/proofs/TARGET_A_PERIOD8_STRUCTURAL_MECHANISM.md`（SHA-256 `ca89c37eeabe100d3f2fe62695cf99b2cba6eaf116966862eb0e45352e7277d4`）；主脚本 SHA-256 `381f92aa983c701dee2319aa15470e17e1bc9fa2062ee7a74386c56dd7e367c5`；checker SHA-256 `428995679eff90b81b9fa6d628392019cb5a890a01283d8e7890cf262827750f`；测试与 theorem package。
- **下一步：** Task 41 对 arXiv、期刊发表、作者更新、引用与后续 signed-circulant 文献执行 current novelty/priority audit；在审计完成前不开始论文 manuscript。

---

## 2026-08-16 — Target A Task 42A：一般周期 closed-walk identities 与 8-barrier 必要障碍

- **研究对象：** 将 Task 40C 的 period-8 closed-walk 机制推广到任意整数周期 `p>=1` 的 Hamilton-gauge signing；只建立一般周期必要条件，不声称充分性、全周期最优性、有限尺寸全局最优性或所有 signing 的全局结论。
- **一般 `A^2` 局部公式：** 从无限 lattice 的四条 transitions 独立相乘，得到 displacement `-4,...,+4` 的完整系数；公式不含 `p`。对周期 `1,...,8` 的全部 510 个 `tau` words、3586 个 rows 逐项核验，覆盖短胞元 residue collision。
- **符号闭步推导：** 枚举 `{-2,-1,+1,+2}` 上全部长度 2、4、6 closed step words，共 `4/36/430` 条；将闭步 tau 单项式的成对端点严格改写为 Q 区间乘积，再按平移类收集，独立得到 `M_1=4p`、`M_2=28p+8 sum Q_i`、`M_3=238p+156 sum Q_i+24 sum Q_iQ_(i+1)+12 sum Q_iQ_(i+2)`。置 `I_i=(1+Q_i)/2` 后化为 `M_2=20p+16d` 与 `M_3=118p+168d+96a+48b`。
- **一般 8-barrier 障碍：** 若 `R(Q)<=8`，则逐 band 有 `y^(k+1)<=8y^k`，故 `M_(k+1)<=8M_k`。由 `F_1=16d-12p` 得 `d<=3p/4`；由 `F_2=-42p+40d+96a+48b` 得 `40d+96a+48b<=42p`。只使用严格反命题 `F_k>0 => R>8`，明确拒绝以非正 excess 证明上界。
- **机器验证：** 主路线全枚举 `p=1,...,12` 的 4095 个合法 Q，另以固定 seed 在 `p=13,17,24,31,48` 核验 320 个样本，并检查 translation、reflection、`tau -> -tau`。第二条 exact Laurent-polynomial 路线对 `p<=6` 的 63 个合法 Q 逐项重算常数项。独立 checker 不导入主脚本，以递归闭步枚举、`p<=10` 全枚举及另一随机 seed 重验；无数值积分。
- **状态：** `GENERAL_PERIOD_CLOSED_WALK_IDENTITIES_PROVED`、`GENERAL_PERIOD_DEFECT_DENSITY_OBSTRUCTION_PROVED`、`GENERAL_PERIOD_LOCAL_CLUSTER_OBSTRUCTION_PROVED`；总状态 `GENERAL_PERIOD_CLOSED_WALK_OBSTRUCTIONS_PROVED`。可读局部 motif basis 已在 `M_3` 达成，因此 optional `M_4` 不进入本 theorem package，下一步转 Task 42B。
- **负向测试：** M3 coefficient、raw closed-walk expansion、density implication direction、nonpositive excess overclaim、necessary-as-sufficient、all-period global overclaim、quadrature 与 source SHA 篡改均按要求 FAIL；Task 42A tests 15/15 PASS，Task 40A/40B/40C/42A 定向回归 91/91 PASS，全套 default tests 为 178 PASS、3 个既有 slow generator tests SKIP、17 subtests PASS；独立 checker `TARGET_A_GENERAL_PERIOD_MOMENTS_PASS`。
- **产物：** 主脚本 SHA-256 `04579c1d67c6af2da2a2629ba97352294864c19ae3a9b0ccc832111587731c6d`；checker `563ec3882130037de1136da8ea695be5b2d0d1ad4c46194d829614628ca4637d`；测试 `190506ba146b83ecd76459a71eb424d0bafa89a0aef4ede4d1f2907409fde527`；JSON `566928bc0fc06bc984a102d29f84a8694d9c9cb17b254e8940d3c53bdaac2401`；proof markdown `14bb089d2d3dbb375ca0e409557fc1fd8121ad5106f2e08cb5d7005aef8d7a33`。
- **下一步：** Task 42B 以 explicit dihedral orbit enumeration 与独立 Burnside count 完整核验 `p<=16` 的 2626 个 legal-Q orbit diagnostics，并分类 primitive tau phases 的低周期谱前沿；Task 41 novelty/priority audit 与 Lane R full reproduction 继续并行。

---

## 2026-08-16 — Target A Task 42B：primitive period 不超过 16 的完整谱前沿

- **研究对象：** 完整分类 `1<=p<=16` 的 periodic Hamilton-gauge phases，判断是否存在 `R<eta` 的更优相或与 target 真正不同的 tie；结论严格限制在 primitive `tau` period 不超过 16，不升级为 all-period、finite-size 或 arbitrary-signing global theorem。
- **phase space 双路线：** Route A 显式枚举 `product Q_i=1` 的 `2^(p-1)` 个 words 并按 rotations/reflections 分 orbit；Route B 不枚举 sign words，仅用每个 dihedral permutation 的 cycle decomposition、cycle parity 与 Burnside lemma 计数。逐周期共同得到 `1,2,2,4,4,8,9,18,23,44,63,122,190,362,612,1162`，总数 2626，mismatch 0。
- **一般 Bloch 构造：** 从无限 lattice transitions 与 cell-crossing Laurent exponent 构造任意 `p` 的 `H_(p,Q)(z)`，包括 `p=1,2,3` 的 residue collisions。全部 2626 类精确核验 `H_tau(z)^T=H_tau(z^-1)`；修正一般 negation 关系为 `H_(-tau)(z)=-D H_tau((-1)^p z)D`，明确 odd `p` 会发生 `z -> -z`。每类的 Q dihedral images 与 tau translation/reflection/global-negation images 逐集合一致。
- **primitive/repetition：** 每类直接重算 primitive Q 与 tau periods。Target 的 primitive Q key 为 `0001`、primitive tau period 为 8；表中 `P08-0006: 00010001` 与 `P16-0512: 0001000100010001` 使用同一 infinite-phase key `tau8:Q0001`，后者只是重复 unit cell，不计为第二 minimizer。
- **discovery scan：** 对 2626 类使用 256 点 Bloch grid，逐周期前五名再以 4096 点 refine；preview 只标 `OBSERVED`，不作 theorem 输入。没有非 target preview 低于 eta。最近竞争者为 `p=10, Q=0000010001`，observed `R^2=7.91638155174...`，gap 约 `0.11215548656`。
- **exact certificate partition：** 2624 个 competitors 中，1787 类由 Task 42A 的 positive `F1/F2` 证明 `R>8>eta`；824 类在 `z=+-1` 由 ternary integer Rayleigh vector 证明 `R>eta`；余下 13 类由 endpoint small-integer Rayleigh vector 证明；uncertified 0。所有比较将 rational quotient `r` 化为 `u=((r-4)^2-10)/2`，以 exact `u>0,u^2>5` 证明 `r>eta`。
- **危险类双证书：** 对 numeric gap 最小的 24 个 endpoint-certified classes，独立生成 `det(yI-H^2)` 并以 exact Sturm intervals 隔离最大 squared eigenvalue；每个 rational lower endpoint 都严格大于 eta。所有 13 个 observed gap `<0.25` 的类均包含在这批双检中。
- **frontier：** `p=8` 与 `p=16` 的 observed minimum 是同一 target phase，exact `R=eta`；其余每个周期的每个 orbit 均 exact `R>eta`。非 target 周期内的 minimizing orbit 只标 numeric ranking，不冒充 exact within-period minimizer。
- **状态与边界：** 新状态 `LOW_PERIOD_PHASE_SPACE_COMPLETE`、`LOW_PERIOD_SPECTRAL_FRONTIER_TABLE_PROVED`、`PERIOD_LE16_UNIQUE_PRIMITIVE_OPTIMUM_PROVED`。禁止表述为 period 17 以上、all-period、finite-size 或 all-signings optimum；numeric previews 未用作证明。
- **独立验证：** checker 不导入 classifier，重算两路 orbit counts、全部 Q/tau/orbit/primitive/geometric data、1787 个 moment 与 837 个 endpoint certificates、24 个 Sturm polynomials/intervals 及 target repetition；`TARGET_A_LOW_PERIOD_SPECTRAL_FRONTIER_PASS`。Task 42B tests 15/15 PASS，Task 40A/40B/40C/42A/42B 定向回归 106/106 PASS，全套 default tests 为 193 PASS、3 个既有 slow generator tests SKIP、17 subtests PASS。
- **产物：** classifier SHA-256 `0bea57a542dd5f1fc92745bb803185fca6fa432053efba6fe099d815cc2e7730`；checker `f6f2eae206e735d4caaa8560faabbb4e5edf5a01fda096c41653161ee97291c9`；tests `c13753b0cfb113bea7ffff40d7699b0bd4b2761015bab988f7cf0a5a5dccd72c`；JSON `82e69ab7df7d81d6c2c46364a6e07aba7578fbc3ad21a69dcc17ffd08333928d`；proof markdown `a3e155b00744cd33e40d525494a11cc54bbb7fe1a310148f5db4af7eea83159c`。
- **下一步：** Task 42C 用 Task 42A general moments、defect density、local clusters、gap statistics 与 primitive/chiral structure 压缩 2624 份 exact exclusions；Task 41 handoff 完成后追加 N10/N11 targeted novelty search，Lane R 继续冻结重算。

---

## 2026-08-16 — Target A Task 42C：低周期 exact frontier 的 closed-walk 结构压缩

- **研究对象：** 将 Task 42B 对 `p<=16` 的 2624 个 competitor representations 从大规模逐类 endpoint certificates 压缩为统一 moment hierarchy、一个 cancellation baseline lemma 与极少数 residual certificates；不扩大 Task 42B 的 bounded theorem scope。
- **adaptive moment hierarchy：** 对每类精确计算 `F_k=M_(k+1)-8M_k`，先统一检查 `F_1,...,F_24`，仅对 residual 扩展到 `F_25,...,F_64`。严格只用 `F_k>0 => R>8`，不以 finite negative excess 证明上界。共 2611 类出现首次 positive excess：`F1/F2/F3/F4/F5` 分别检测 `64/1723/493/178/56` 类，最晚的两类分别到 `F48` 与 `F64` 才越过，说明低密度 near-barrier geometry 需要长 closed walks。
- **15 类稳定 residual：** 8 类是 `Q=(-)^p` 的重复 cells，统一由 period-independent identity `A^2=4I+S^2+S^-2+S^4+S^-4` 得 exact `R=8>eta`；2 类是同一 target phase 的 `p=8/16` 表示，依赖 Task 40A 得 `R=eta`；其余 5 类为 `P10-0006/P12-0006/P14-0006/P14-0154/P16-0006`。
- **exception geometry：** 四个 `P(2m)-0006` residuals 是 positive defects cyclic separation 4、另一 gap 逐渐增大的 primitive phases；`P14-0154` 是 cyclic gaps `3,4,3,4` 的四-defect phase。对五类仅保留 Task 42B exact endpoint integer Rayleigh certificate 证明 `R>eta`。numeric previews 不作为证明，也不声称前四类 exact `R<8` 或 `P14-0154` exact `R=8`。
- **compression accounting：** `2611 moment + 8 baseline + 5 endpoint = 2624 competitors`，再加 2 target representations 恰覆盖 2626 orbits，overlap/omission/uncertified 均为 0。Task 42B 的 837 个 endpoint certificates 中有 832 个被统一 moment route 替换。
- **状态与 scope：** 新状态 `LOW_PERIOD_STRUCTURAL_FRONTIER_PROVED`。它证明 primitive period≤16 frontier 的结构压缩，不声明 negative excess upper bound、period≥17、all-period optimum 或论文 package ready。
- **独立验证：** checker 不导入 structural classifier，从 Task 42B orbit table 重建每类 signed closed walks，逐项核验首次 positive index/value 到 `F64`，重建 15 类 residual partition，并重新乘五个 endpoint matrices/vectors 与 exact eta comparison；`TARGET_A_LOW_PERIOD_STRUCTURAL_FRONTIER_PASS`。Task 42C tests 11/11 PASS；全套 default tests 为 204 PASS、3 个既有 slow generator tests SKIP、17 subtests PASS。
- **产物：** classifier SHA-256 `c3681df7083c96b754507a40491ee0f58737546b6f0e9003dade2f228d41d18e`；checker `0f6238c45f72aae1ac5ab8daed758e9f5642e0138404de0caedb4cdd721ec0a2`；tests `f40db0b48d32fe8ec735896cb7df892eccddecae4d3a721a703b0348aef314a2`；JSON `7f9fe5b0f318f07b31d71c638049bc9458422fae9ad4c5ee40062c40b5891b71`；proof markdown `cd6de9cc2c5a201247b09814815ced50aa68bf6133a203569bc3a877ee6e2c01`。
- **下一步：** 同步接收 Task 41 经 N10/N11 targeted search 更新的 handoff；核验 safe wording 后由 main agent 导入。Lane R 完成 n30、certificate replay 与 slow generator tests 后再导入精简 reproduction summary。

---

## 2026-08-16 — Target A Task 41：novelty、priority 与 provenance audit

- **审计边界：** 独立 sub-agent 在 frozen `c5cadf3ec7e160fc994453907fe83c579dc89646` baseline 上只审计 public literature、priority、provenance 与 author updates，不进行数学搜索，不修改 active worktree。cutoff 为 2026-08-16；Task 42A/B 完成后追加 N10/N11 synchronization-gate targeted search。
- **覆盖：** query ledger 共 135 条，覆盖 arXiv、Crossref、DataCite、OpenAlex、Semantic Scholar、general web、GitHub repository/history/content、author pages、citations/follow-ups，并尝试 Google Scholar。Google Scholar 明确记为 inaccessible；Semantic Scholar 与 GitHub REST API 记为 partially rate-limited，均未冒充 negative finding。
- **primary sources：** arXiv:2607.18334 与 arXiv:2607.17343 截止审计仍为 v1；作者仓库 `Vaibhavs25/bilu-linial-parity` 最新 commit `312f0e2...`，八个 commits 均在 2026-07-19，无后续 branch/issue/PR 或 target-specific update。source archives 与作者 TeX blobs 的 SHA-256 一致。
- **claims N1–N11：** N1–N5、N7、N11 为 `NO_DIRECT_PUBLIC_PRIOR_FOUND`；N6 为 `CLOSE_PRIOR_FOUND`，因为原论文 Proposition 1 已给 all-unbalanced phase 的 `2sqrt(2)`/squared 8 value，但没有 period-8 unique runner-up classification；N8/N9/N10 为 `RELATED_METHOD_ONLY`，分别存在 parity-closed-walk、Bloch/chiral 与一般 moment/Floquet 方法先例，但未找到 target-specific theorem。`DIRECT_PRIOR_FOUND=0`、`UNRESOLVED=0`。
- **安全措辞：** 冻结结论为“As of 16 August 2026, no direct public prior was found in the sources and queries recorded in this audit.”；明确受 indexing delay、不可访问服务、private/unindexed work 限制，不使用 world-first/definitely-first 等绝对表述。项目自己的 public GitHub commits 单列 project-origin disclosure，不计 independent prior。
- **provenance：** timeline 区分 2013/2021/2023 method antecedents、2026-07-19 primary papers/author repo 与本项目各 claim-bearing commits。匿名 raw GitHub 最迟在记录的 `2026-08-16T05:33:13Z/05:45:32Z` 可读；Git commit timestamp 不冒充精确 public exposure time。
- **导入验证：** main agent 原样导入五个 handoff artifacts，逐项复核 SHA、JSON、11 个 labels、assessment counts、source references、Q001–Q135 连续性、service limitations、N10/N11 proof fingerprints、禁用措辞与 safe sentence。仓库内 checker `TARGET_A_NOVELTY_PRIORITY_AUDIT_PASS`，tests 11/11 PASS。
- **产物 SHA-256：** audit markdown `e4711c2e6251dda1422fa0348b7dfcc054a6f40ae0cac6d1569756096b504e63`；audit JSON `68cc3aa7c1a65877c3d7488518faf7defc0400306b59128dc9212d42dca573b4`；query ledger `72719ff69a5b1f0c0149d2734de253c3207d22dd854a69cf32e68ef1ca2c0235`；source snapshot `df3776cbeed1863bef256858d07b8100658c863fb4f79ba3af22387ac7993b79`；timeline `9f221c2a0deaf5ab9533fc24d5f104752cce4e25c471cbbc5c424d452cd6c39d`；checker `7ef8fafcef9f1bee4e68463892820865aeee18271f49cd82778264c3e8b92a6a`；tests `a77b3d9befa0ad5f8a3b6f91ca57d84a16812a9230b533a55201b72146e08272`。
- **下一步：** 导入 Lane R 四个 fresh spectral regenerations、committed checkpoint replay 与 slow generator audits 的精简 manifest/hash summary；满足 paper gate 后先执行 Reviewer Zero/theorem dependency graph，不直接写 manuscript。
