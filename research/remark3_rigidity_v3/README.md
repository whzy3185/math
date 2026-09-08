# Remark 3：完整分类、不可约刚性与最高齐次项障碍（v3）

工作分支：`research/remark3-leading-form-v3-20260908`。
目录：`research/remark3_rigidity_v3/`。
本分支从 v2 研究稿继续推进，不修改 `main`。

## 本轮新增结论

研究方程

`product_i (D_i u)^mu_i = p exp(g)`,  `D_i=sum_j a_ij partial_zj`,  `A in GL_n(C)`。

一般非零 `p` 的规范形、自动有限增长、有限因子分配和径向积分恢复仍完整保留在父分支。v3 在不可约全方向情形进一步得到三个更直接的结果。

### 1. 原坐标方向导数判据

若 `p` 在 `C[z]` 上不可约且 `D_i p != 0` 对所有 `i`，记 `M=sum mu_i`。可解当且仅当存在唯一活动指标 `k` 使：

- `mu_k=1`；
- `D_j g=0` 对所有 `j!=k`；
- `D_k g != 0`；
- `D_j p = theta_j D_k g`，其中 `theta_j` 是非零常数。

这意味着在不可约全方向情形，除验证不可约性外，不必先分解 `p` 或枚举因子分配即可判定可解性。

令 `ell_i(z)=(A^{-T}z)_i`、`lambda_j=M theta_j`，则 `g=gamma(ell_k)`，并且

`p=b(ell_k)+D_k g * sum_{j!=k} theta_j ell_j`。

全部解显式为

`u=c[ exp(gamma(ell_k)/M) sum_{j!=k} lambda_j ell_j + int_0^{ell_k} b(t)exp(gamma(t)/M)dt ]+C`,

其中 `c^M product_{j!=k} lambda_j^mu_j=1`。因此模加法常数恰有 `M` 个解；无权重时恰有 `n` 个。

### 2. 次数与最高齐次项障碍

若上述不可约全方向方程可解，记 `D=deg p`、`d=deg g`，则必有 `1 <= d <= D`。而且对唯一活动方向 `ell_k`，最高齐次项必须满足

`p_D = ell_k^(D-1) * L`

其中 `L` 为一次齐次式；若 `D>d`，则更强地 `p_D` 必须是 `ell_k^D` 的非零常数倍。

直接得到：

- `deg g > deg p` 时无解；
- `D>=3` 且 `p_D` 平方自由时无解；
- `D=2` 且最高二次型秩至少为 3 时无解。

### 3. 泛型无解

固定矩阵 `A`、权重和次数 `D>=2`。可解的不可约全方向多项式的最高齐次项只能落在

`union_k ell_k^(D-1) * L_1`

中，其中 `L_1` 是所有一次齐次式空间。每个分支仅有维数 `n`，而全部 `D` 次齐次式空间维数为 `binom(n+D-1,D)>n`。因此这一必要条件是一个真 Zariski 闭约束：最高次系数泛型地避开它，所以对任意多项式相位 `g` 均无整函数解。

## PDF 渲染审计

本地合并后的 v3 论文实际编译为 13 页 A4 PDF。已用 PDFium 与 Poppler 两个渲染器逐页检查，两者在 150 dpi 下逐像素一致；未发现裁切、公式重叠、黑块或缺字。PDF 可正常打开、未加密、非扫描件，字体均嵌入。LaTeX 最终日志没有 overfull box，仅参考文献首项存在一个 underfull hbox，属于断行松散的排版提示，不影响内容或可读性。第 13 页主要为参考文献并留有较大底部空白，这是分页结果，不是渲染故障；没有为了减少一页而缩小正文或压缩公式。

详见 `render_audit.md`。

## 精确验证

- v2 的 `verify.py`：93 项精确符号检查通过；
- v3 新增 `verify_v3.py`：18 项精确符号检查通过，覆盖原坐标方向判据、非平凡矩阵换元、次数障碍、最高齐次项正例、平方自由三次障碍和二次型秩障碍。

这些有限检查用于回归和算例核验，不替代一般解析证明，也不是 Lean 形式化。

## 文献定位

原问题来自 Feng Lü 的 arXiv:2605.09585v1 第 6 页 Remark 3。Chen–Han 2022 已有二维不可约相关结果；公开文章页面和 Xu 等 2023 的转述可核对 Theorem 1.4 的二维结构，因此本文不把二维特例声明为首次。Xu–Ding 2026 的公开摘要明确其主结果针对 `C^3` 中有限阶超越整函数和广义线性指数右端；这与本文任意多项式因子 `p`、不预设有限阶的范围不同，但由于尚未取得全文逐定理核对，仍不作“完全无重叠”的优先权声明。

## 文件

- `manuscript_v3_addendum.tex`：可直接插入 v2 第 6 节不可约定理之后的三个新推论与完整证明；
- `verify_v3.py` / `verification_v3.json`：v3 新推论的 18 项精确验证；
- `proof_audit_v3.md`：新增证明的依赖与边界；
- `literature_update_v3.md`：本轮文献范围核验；
- `render_audit.md`：PDF 预检、双渲染器检查与页面问题记录；
- `build_record_v3.json`：页面、渲染器、验证数量和文件散列记录。

父分支 `research/remark3-explicit-classification-v2-20260908` 中保留完整 v2 论文源码；本轮对话同时生成了已合并上述 addendum 的完整 v3 PDF/LaTeX 交付件。当前仍是研究稿，不是独立同行审定、正式发表或 Lean 形式化成果。
