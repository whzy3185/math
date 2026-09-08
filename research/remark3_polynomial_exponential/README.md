# Remark 3：带多项式因子的乘积型 PDE

研究分支：`research/remark3-polynomial-exponential-20260908`。

来源：Feng Lü, *On entire solutions for a class of product-type nonlinear PDEs in C^n*, arXiv:2605.09585v1，用户上传的 2026-05-10 版本，第 6 页 Remark 3，式 (1.8)–(1.9)。

## 本次稿件的结论

在常系数矩阵 A 可逆、p 非零且 p,g 均为多项式时，对更一般的正整数权重方程

`product_i (sum_j a_ij u_zj)^mu_i = p exp(g)`

给出无预设增长阶条件的解析证明。所有整函数解都自动具有有限增长；g 非常数时解的阶恰为 deg(g)，g 为常数时解为多项式。更进一步，全部解通过有限次变量分块、不可约因子分配、常数比例与环路一致性检验以及显式积分得到。每个规范族只有一个乘法约束及一个任意加法常数，总参数维数不超过 n。

原问题的所有权重取 1。p=1 时恢复线性形式的一元积分分块结构；一般 p 时不可保留该结构，例如 u=exp(xy)。p=0 的无限维退化情形单独处理。

## 文件

- `manuscript.tex`：完整中文论文，包括主定理、全部证明、有限代数分类、计数界、算例和参考文献。
- `proof_audit.md`：证明依赖、边界条件及不可混淆的证据等级。
- `literature_review.md`：原文对应位置、外部检索与新颖性限制。
- `verify.py`：有限分类数据的精确符号检查及回归测试（另行写入）。
- `verification_results.json`：实际运行生成的结果（仅在运行成功后写入）。
- `Makefile`：XeLaTeX 编译与测试入口。

## 复现

安装带 ctex 和 Fandol 字体的 TeX Live、XeLaTeX、latexmk，并安装 `requirements.txt`。运行：

```sh
python verify.py --output verification_results.json
latexmk -xelatex -interaction=nonstopmode -halt-on-error manuscript.tex
```

## 状态与归属

这是附有完整解析论证的研究稿，不是已发表论文，不是已经独立同行审定的结论，也不是 Lean 形式化证明。程序只验证明确列出的有限符号实例与分类数据，不替代一般解析证明。

原文已有的 p=1 分块思想、线性换元和相关背景明确归属于原文。本文的新推导是带代数零因子的增长闭合、正整数权重、有限代数参数化及相应推论。2026 年 Xu–Ding 的相关论文已检索到，但尚未取得其全部定理文本逐项比对，因此不作“首次”“没有重叠”或期刊分区承诺。

不修改 main，不合并已有其他研究分支，不复制用户上传论文全文到公开仓库。
