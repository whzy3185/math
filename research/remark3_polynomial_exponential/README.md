# Remark 3：带多项式因子的乘积型 PDE

分支：`research/remark3-polynomial-exponential-20260908`。目录：`research/remark3_polynomial_exponential/`。

来源为用户上传的 Feng Lü, *On entire solutions for a class of product-type nonlinear PDEs in C^n*, arXiv:2605.09585v1（2026-05-10），第 6 页 Remark 3，式 (1.8)–(1.9)。

## 结果

对可逆常系数矩阵 A、非零多项式 p、多项式 g 及正整数权重 mu_i，研究

`product_i (sum_j a_ij u_zj)^mu_i = p exp(g)`。

稿件给出无预设有限阶条件的解析论证：全部解自动具有有限增长；g 非常数时阶恰为 deg(g)，g 为常数时解为多项式。全部解由有限次变量分块、不可约因子分配、常数比例与环路一致性检验及显式积分生成。每个规范族只有一个乘法约束与一个任意加法常数，总参数维数不超过 n；连通图情形忽略加法常数后只有有限多个解。

所有权重取 1 得到原问题。p=1 时恢复一元积分的线性分块形式；一般 p 时该形式不再成立，例如 u=exp(xy)。p=0 的无限维退化情形单独分类。

## 文件与实际验证

| 文件 | 内容 |
|---|---|
| `manuscript.tex` | 完整中文论文；实际编译为 13 页 PDF |
| `proof_audit.md` | 证明依赖、边界条件、证据等级 |
| `literature_review.md` | 原文对应位置、外部来源与新颖性限制 |
| `verify.py` | 有限分类数据的精确枚举与符号验证 |
| `verification_results.json` | 实际运行：14 组测试通过 |
| `build_record.json` | 编译、页面检查、版本与文件散列 |
| `Makefile` / `requirements.txt` | 复现入口 |

PDF 随本次对话交付；仓库存放可重建的 LaTeX 源文件，未提交二进制 PDF。下载的论文包同时包含 PDF 与源文件。

## 复现

使用 Python 3.10+、带 ctex/Fandol 的 TeX Live、XeLaTeX 和 latexmk：

```sh
python -m pip install -r requirements.txt
python verify.py --output verification_results.json
latexmk -xelatex -interaction=nonstopmode -halt-on-error manuscript.tex
```

测试使用明确的复不可约线性因子。对其他输入，调用者必须提供完整的 C 上不可约分解；程序不自行证明不可约性，亦不能以浮点近似代替恒等式判定。

## 状态与归属

本稿具有完整解析证明，但不是已经独立同行审定、发表或 Lean 形式化的论文。符号测试不替代一般解析论证。原文的图分块思想与换元明确引用；带代数零因子的增长闭合、正整数权重、有限参数族与计数为本次推导。

已检索到 Xu–Ding 2026 年题目接近的论文，但尚未取得全文逐定理比较，因此不作“首次”“无文献重叠”或期刊接收承诺。署名待确认。未修改 main，未合并其他研究分支，未将用户上传的原论文全文复制到公开仓库。
