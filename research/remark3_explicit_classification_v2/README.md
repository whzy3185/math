# Remark 3：完整分类与不可约情形的精确计数（v2）

工作分支：`research/remark3-explicit-classification-v2-20260908`。
基于既有分支 `research/remark3-polynomial-exponential-20260908` 的提交
`d579b4f290881968c5b6011ae213b594645417f1` 创建，保留旧稿和全部已有研究文件；不修改或合并 main。
本修订稿目录：`research/remark3_explicit_classification_v2/`。

## 本轮实质进展

`manuscript.tex` 是可独立阅读的完整中文论文，不是只有结论的补充说明。
它重给一般正整数权重方程的增长闭合、规范形必要充分证明、有限分类与积分恢复，
并加入不可约全变量因子的显式可解性判据、精确解数、无解二次族及有限求导积分公式。

对于标准方程 `product_i(v_wi)^mu_i = P exp(G)`，设 P 在 C 上不可约且每个偏导 P_wi 非零。
记 M=sum(mu_i)。可解当且仅当存在 k 满足 mu_k=1，且

    G = gamma(w_k),
    P = b(w_k) + gamma'(w_k)/M * sum_{j!=k} lambda_j w_j,

其中 gamma 非常数、b 为一元多项式、lambda_j 为非零常数。
全部解是

    v = c [exp(gamma(w_k)/M) sum_{j!=k}lambda_j w_j
           + integral_0^{w_k} b(t)exp(gamma(t)/M)dt] + C,
    c^M * product_{j!=k}lambda_j^mu_j = 1.

故模加法常数恰有 M 个解。无权重时恰有 n 个。
“全变量依赖”是针对 w=A^{-T}z 中的 P=p(A^T w)，不能忽略坐标变换。
特别地，`P=1+sum_i w_i^2`、n>=2 时，对任意多项式 G 和正整数权重都没有整函数解。

若一个块的相位满足 h_wa=alpha!=0 为常数，则其闭多项式梯度的原函数是 R exp(h)，
R 可由有限几何级数 `sum_l (-1)^l alpha^(-l-1) partial_a^l Q_a` 算出。
因此仿射 G 的全部解都是有限项多项式乘指数之和，再加多项式。

## 复现

需要 Python 3.10+，以及含 ctex、Fandol、XeLaTeX 和 latexmk 的 TeX Live。

```sh
python -m pip install -r requirements.txt
python verify.py --output verification_results.json
latexmk -xelatex -interaction=nonstopmode -halt-on-error manuscript.tex
```

本轮实际运行 `verify.py`：93 项精确符号检查通过。
一般枚举函数接受调用者提供的完整 C 上不可约分解，不自动证明该分解完备。
不可约专用判据的否定结论依赖不可约前提；程序不把 Q 上不可约误当成 C 上不可约。
本轮未重跑父分支的旧 14 组测试；93 项是新脚本的独立实际运行结果。

## 文件

- `manuscript.tex`：完整论文，含全部核心解析证明。
- `verify.py` / `verification_results.json`：一般规范族枚举、不可约判据、积分公式及精确测试。
- `proof_audit.md`：证明依赖、假设与逐项核查。
- `literature_review.md`：已核对来源及未取得全文的限制。
- `Makefile` / `requirements.txt`：复现入口。

PDF 与包含 PDF 的源文件包通过本次对话交付；仓库提交可重建的文本源文件。
不公开上传用户提供的原论文全文。

## 学术状态

这是已给出解析推导并通过所列符号测试的研究稿，不是已经独立同行审定、发表或 Lean 形式化的论文。
二维不可约特例已有 Chen–Han 结果，本次依据 Xu 等 2023 年论文 Theorem D 的明确转述核对，不作首次声明。
Xu–Ding 2026 年三维近题论文尚未取得全文，故新颖性比对没有被宣称完成。
作者署名待确认，不承诺期刊接收或分区。
