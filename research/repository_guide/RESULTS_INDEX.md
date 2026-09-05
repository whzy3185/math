# 成果—证据—复用索引

日期：2026-09-05。此表描述当前实际文件与证据形式，不把历史状态标签
视为证明。一般跳长为当前研究主线；八周期为已有完整稿；历史材料按
复用价值归档而不搬移。`N` 为阶数，`s` 为跳长，`p` 为符号周期。

## 状态约定

- **解析正文已存在：**有可读证明；本轮核对用途、范围和依赖，不代表
  外部数学家已经独立审阅。
- **有限精确成分：**符号/整数计算承担特定有限步骤，要说明完整性。
- **历史计算辅助：**旧文件声称有证书与 checker；本轮未重跑大规模生产链。
- **草稿/开放：**不能作为当前主定理前提。
- **已被否定：**有明确反证；区别于仅仅退出正文或被更强结果替代。

## A. 一般跳长主线

令 `E=research/generalization/circulant_1s/extension_20260905/`。
下表链接为实际证明入口。

| ID | 准确结论 | 证明/验证入口 | 当前状态与依赖 | 论文角色 |
|---|---|---|---|---|
| G1 | `C_N(1,s)` 的 Hamilton 坐标与碰撞安全平方公式 | [Task60公式](../generalization/circulant_1s/task60/TASK60_GENERAL_H2_FORMULA.md) | 既有解析基础；不能当作新发现 | 共用预备知识 |
| G2 | 偶/奇跳长 alternating 色散分别为 `4cos²θ+4cos²(sθ)`、`4cos²θ+4sin²(sθ)` | [Task60色散](../generalization/circulant_1s/task60/TASK60_TWISTED_DISPERSION.md) | 既有解析；奇跳长参考阈值不是8 | 比较基准 |
| G3 | `DT_m` 全相位反对易 iff `tau_(i+m)=(-1)^(s+1)tau_i` | [一般判据§3](../generalization/circulant_1s/extension_20260905/FLAT_MINIMUM_AND_CHIRAL_CRITERION.md) | 解析正文；指定单项式类，不分类所有 unitary | 共用结构引理 |
| G4 | 对每个偶 `s>=2`，显式本原周期 `4s` 对径双缺陷字满足 `R_s<8` | [主定理及证明](../generalization/circulant_1s/extension_20260905/EVEN_JUMP_THEOREM_AND_PROOF.md) | 解析正文；依赖 chiral、八端点行列式、正生成函数、惯性 | 最有价值的升级主结果候选 |
| G5 | 一般偶跳长的平方特征方程 `q_(s/2)(y,h)` | [同文§3](../generalization/circulant_1s/extension_20260905/EVEN_JUMP_THEOREM_AND_PROOF.md) | Chebyshev 精确代数公式；不是一般阶根式全解 | G4证明主体 |
| G6 | `1/(2s³)<=8-R_s<=4sin²(pi/(s+2))` | [定量证明](../generalization/circulant_1s/extension_20260905/POLYNOMIAL_GAP_BOUND.md) | 最新解析正文；强于G4原来的指数小下界；不是锐渐近 | 自然定量推论 |
| G7 | `N=4sL` 两种 holonomy 的 target 都 sub-eight；当 `L>pi sqrt(s(1+s²)/2)` 时严格优于两种 alternating 字 | [定量证明§6](../generalization/circulant_1s/extension_20260905/POLYNOMIAL_GAP_BOUND.md) | 有限Bloch直和与已有比较；仅充分阈值 | 有限图主要应用 |
| G8 | `m(N,s)=2 iff N=2s+2`，否则 `m(N,s)>=sqrt5` | [平坦分类§1](../generalization/circulant_1s/extension_20260905/FLAT_MINIMUM_AND_CHIRAL_CRITERION.md) | 共邻点奇偶性；充分构造Task60已有；外部经典分类有强重叠 | 可独立保留，未必放主线 |
| G9 | 平坦族等号符号；`(8,3)=K_(4,4)` 的Hadamard例外 | [平坦分类§2](../generalization/circulant_1s/extension_20260905/FLAT_MINIMUM_AND_CHIRAL_CRITERION.md) | switching 与图自同构区别明确；尚需外部新颖性核查 | G8的等号结构 |
| G10 | `R_s=rho(H_s(1))²` | [Q7记录](../generalization/circulant_1s/extension_20260905/QUANTITATIVE_QUESTIONS.md) | **开放**；只有有限相位数值线索 | 不写作定理 |
| G11 | `s²(8-R_s)->pi²` | [Q6记录](../generalization/circulant_1s/extension_20260905/QUANTITATIVE_QUESTIONS.md) | **开放**；现有数据为`z=1`值，非已证全局值 | 不写作定理 |
| G12 | 一般跳长最小sub-eight周期、唯一性、全部`m(N,s)` | [研究边界](../generalization/circulant_1s/extension_20260905/PROOF_AUDIT_AND_SCOPE.md) | **开放**；构造的primitive period不等于最小可行period | 不作为现有成果 |

复核入口：[首轮验证器](../generalization/circulant_1s/extension_20260905/verify_extension.py)、
[精确结果](../generalization/circulant_1s/extension_20260905/EXACT_AUDIT.json)、
[定量验证器](../generalization/circulant_1s/extension_20260905/verify_quantitative_gap.py)、
[定量结果](../generalization/circulant_1s/extension_20260905/QUANTITATIVE_AUDIT.json)。
G3–G9 都不在现有 Lean 正式范围内。

## B. 八周期完整稿

| ID | 结论 | 证明与验证入口 | 范围/复用 |
|---|---|---|---|
| P1 | switching、Hamilton坐标、finite Bloch、lift/dihedral/zone folding | [§2正文](../paper_strengthening/manuscript_period8_jgt/sections_en/02_switching_bloch.tex)；[不变性证明](../paper_strengthening/symmetry_invariance_lemmas.md) | 直接复用；一般奇跳长的lift关系另查 |
| P2 | `8x8→4x4→2x2`，四次式`P(y,c)` | [§4正文](../paper_strengthening/manuscript_period8_jgt/sections_en/04_period8_exact.tex) | 已有解析推导；G4中`s=2`特例 |
| P3 | 四平方色散支、简单fiber、本征谱带和gap | [全色散证明](../paper_strengthening/full_period8_dispersion.md) | s=2精细结果；不是一般s的完整根式谱 |
| P4 | 每个`L>=1`正holonomy平方半径`eta=4+sqrt(10+2sqrt5)` | [精确有限边](../paper_strengthening/task1A_exact_finite_edge.md) | 指定witness，不是全局最小值 |
| P5 | 每个有限`L>=1`负holonomy平方半径`r(2cos(pi/L))<eta` | [负sector证明](../paper_strengthening/task1B_alpha_negative_sector.md) | 纠错后结尾必须用这个更强上界 |
| P6 | `L>=4`正holonomy严格优于twisted | [§4比较](../paper_strengthening/manuscript_period8_jgt/sections_en/04_period8_exact.tex) | G7的s=2精细有限阈值；有有限正式kernel |
| P7 | 最小sub-eight本原周期为8 | [最小周期证明](../paper_strengthening/task2A_minimal_period.md)；[验证器](../paper_strengthening/verifiers/verify_minimal_period.py) | s=2；解析矩归约+9项小型精确证书 |
| P8 | period8内对径双缺陷为唯一sub-eight轨道 | [§5正文](../paper_strengthening/manuscript_period8_jgt/sections_en/05_first_rigidity.tex)；[小递推](../analytic_inventory/period8_two_defect_closed_walk_lemma.md) | 含必要的有限整数递推，不能称完全无计算 |
| P9 | s=2任意周期的M1–M3及必要缺陷障碍 | [一般缺陷证明](../analytic_inventory/general_period_defect_obstruction.md) | 一般s不自动继承这些系数；不充分分类 |
| P10 | 对指定单项式类的负半胞flux iff | [§3正文](../paper_strengthening/manuscript_period8_jgt/sections_en/03_chiral.tex) | G3的s=2特例 |
| P11 | `m(8L,2)=sqrt(eta)`可能在无限子族成立 | [旧结尾](../paper_strengthening/manuscript_period8_jgt/sections_en/07_conclusion.tex) | **被P5否定**；已在独立纠错分支修复，原冻结文件保留 |

## C. Lean 的实际边界

[顶层导入文件](../../formal/TargetA/AllTheorems.lean)导入
[Period8BlochAction.lean](../../formal/TargetA/Period8BlochAction.lean)。
`TargetA.period8_alpha_plus_main_theorem` 的实际类型是：`L>=4` 时，
每个 Hermitian eigenvalue 的平方严格小于 twisted squared benchmark。
它使用 Mathlib 的 Hermitian eigenvalue 列表，当前不是直接以
`spectralRadius` 为结论名的包装。不要把更早用户要求的 API 包装
与实际源代码混写。

本轮静态查看无 `sorry`/`admit`/作者新增 `axiom` 命中；**没有重新运行
Lean build**。既有完整构建记录属于之前轮次。精确半径等式、负sector、
P7/P8/P9及一般跳长新定理没有被本文件正式化。

## D. 历史成果的可复用性

| 模块 | 具体入口 | 当前处理 | 何时值得复用 |
|---|---|---|---|
| 原32阶最小反例与8–30全覆盖 | [历史全局索引](../paper/proof_completion/TARGET_A_FINAL_CLAIM_INVENTORY_V2.md) T8/C1–C2 | 历史计算辅助，当前稿不依赖其“最小”声明 | 若论文明确研究最小阶数，先重放证书链 |
| period<=16/24前沿 | [低周期前沿](../proofs/TARGET_A_LOW_PERIOD_SPECTRAL_FRONTIER.md)；同上A3/C9 | 有界范围与严格证书，不升为全周期定理 | 研究更一般周期分类时 |
| gap/charge/sector arithmetic | [历史索引](../paper/proof_completion/TARGET_A_FINAL_CLAIM_INVENTORY_V2.md) T3 | 简短解析工具，可复核复用 | 新问题确实涉及接口/缺陷拼接时 |
| discrete IMS | 同上T6.1；[证明图](../proof_closure/THEOREM_DEPENDENCY_DAG.md) | 解析工具，但常数和局部patch需核对 | 研究非整胞有限环时 |
| G6精确物理谱边、局域态 | 同上T4；[标量化方向](../analytic_inventory/g6_scalar_problem.md) | 历史计算辅助物理分支选择，非本轮新主定理 | 单独接口谱文章或确切复用需求 |
| R2 bulk/response | [响应递推](../analytic_inventory/r2_response_recurrence.md)；[tail草稿](../analytic_inventory/r2_tail_majorant_lemma.md)；[审计](../analytic_inventory/r2_tail_line_audit.md) | bulk工具与tail证明状态分别记录；tail草稿未自动晋升 | 真正需要非0模8全长族时 |
| R4/R6 all-length接口 | [模板审计](../analytic_inventory/r46_block_template_audit.md) | 开放/条件性，不能作完整解析定理 | 另开明确数学需求后 |
| 全偶阶真假分类`32,40,>=48` | [旧闭环状态](../proof_closure/FINAL_MATHEMATICAL_PROOF_STATUS.md)；[解析缺口](../proof_closure/ANALYTIC_GAP_AUDIT_CURRENT.md) | 历史计算辅助声明；不是“全部m_n”或“解析证明完备” | 不靠添加“工作量”放回当前正文 |
| 旧猜想/poset方向 | `codex/old-conjecture-audit-phase1` 的 `research/STATUS.md` | 独立研究线，156项分叉路径；不合并 | 与当前论文无直接依赖 |

主线目前最有意义的组合是 G1–G7 加 P2–P8 的精细特例；历史接口与
全偶阶计算包不因数量多就自动成为正文。最终整合与投稿等级判断见
[初步评估](PAPER_ASSESSMENT.md)。
