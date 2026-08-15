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
