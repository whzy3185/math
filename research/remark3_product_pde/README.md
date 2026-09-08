# Remark 3：乘积型非线性偏微分方程

研究分支：`research/remark3-product-pde-20260908`。本目录独立于仓库原有图论研究，不改动其结论或冻结稿。

## 文稿与复现入口

完整中文解析论文见 [paper/main_zh.tex](paper/main_zh.tex)，完整英文稿见 [paper/main.tex](paper/main.tex)。两稿分别编译为10页、12页PDF；PDF由本目录构建命令生成，仓库提交的是可复现的论文源码。验证程序的GitHub写入调用被工具拦截，因此程序及测试源码在本次交付的完整ZIP中提供，仓库保留论文、文献、构建文件和实际核验记录。参考文献正文见 [paper/bibliography.tex](paper/bibliography.tex)，另附BibTeX导出文件。

[文献及来源记录](LITERATURE_AND_PROVENANCE.md)区分用户提供的原文结果、本文推导、文献核验及尚未完成的全文比对。[证明审计说明](PROOF_AUDIT.md)列出关键依赖和容易发生的错误。[核验报告](verification/REPORT.md)记录实际运行的31项测试及其边界。

## 原问题和本文定理

基础文献是Feng Lü，*On entire solutions for a class of product-type nonlinear PDEs in C^n*，arXiv:2605.09585v1，第6页Remark 3。考察

\[
\prod_{i=1}^n D_i u=p e^g,\qquad
D_i=\sum_j a_{ij}\partial_{z_j},\quad A\in\operatorname{GL}_n(\mathbb C),
\]

其中`p,g`均为多项式。`p=1`对应原文式(1.8)，一般`p`对应式(1.9)。原文已经给出无零点方程的定理2，不能把它重新标成新成果。

本文还允许正整数权重：`∏(D_i u)^{μ_i}=p e^g`。令

\[
z=A^T w,\quad v=u\circ A^T,\quad P=p\circ A^T,\quad G=g\circ A^T,
\quad M=\sum_i\mu_i.
\]

链式法则准确给出`v_i=(D_i u)∘A^T`，最终回代为`u(z)=v(A^{-T}z)`。

**自动增长定理。** 对`P≠0`，不假设有限阶，直接证明每个整函数解自动有限阶。`G`非常数时`ρ(v)=deg G`；`G`为常数时`v`是多项式，且

\[
\deg v\le1+\left\lfloor\frac{\deg P}{\min_i\mu_i}\right\rfloor.
\]

无权情形即`deg u≤deg p+1`，这个次数上界是尖锐的。

**完整标准形。** 遍历坐标划分`𝒫`。对每一块`B`，令

\[
G_0=G(0),\quad \lambda=e^{G_0/M},\quad m_B=\sum_{i\in B}\mu_i,
\quad G_B(w_B)=G(\iota_Bw_B)-G_0,\quad H_B=G_B/m_B.
\]

只保留满足下列多项式恒等式的数据：

\[
G=G_0+\sum_B G_B,\qquad q_i\in\mathbb C[w_B]\setminus\{0\}\ (i\in B),
\qquad\prod_i q_i^{\mu_i}=P,
\]
\[
\partial_jq_i+q_i\partial_jH_B=
\partial_iq_j+q_j\partial_iH_B\qquad(i,j\in B).
\]

那么全部解，且仅有这些解，为

\[
v(w)=C+\lambda\sum_B\int_0^1 e^{H_B(tw_B)}
\sum_{i\in B}w_iq_i(tw_B)\,dt.
\]

梯度为`v_i=λq_i e^{H_B}`。必要性由增长闭合、多项式除子分解和混合导数相等证明；充分性由径向原函数公式证明。规范最细划分是`v_ij≢0`定义的混合Hessian图的连通分量。

这不是只给出若干例子或重新引入未知整函数：固定`P,G`后，所有多项式形状由`P`的有限次不可约因子分配确定；其系数满足显式齐次线性系统，最后只需要共同标量归一化和积分。

## 可解性、计数与一个显式无限族

若`P=c∏π_ν^{e_ν}`，枚举`∑_i μ_i a_{iν}=e_ν`，令`R_i=∏π_ν^{a_{iν}}`。闭性变为关于非零常数`c_i`的齐次线性系统。其零空间含全部坐标非零的向量，当且仅当每个坐标泛函在零空间上都不恒零；共同缩放可强制`∏c_i^{μ_i}=c`。

连通解模加法常数后的数目至多为

\[
M\prod_\nu\#\{a\in\mathbb Z_{\ge0}^n:\sum_i\mu_i a_i=e_\nu\}.
\]

无权时为`n∏ binom(e_ν+n-1,n-1)`。若`G`不允许任何非平凡坐标可加分离，或`P`有全变量支撑的不可约因子，则全部解都连通。

令`s=w_1⋯w_n`，`h`为非常数一元多项式。对于

\[
\prod_i v_i^{\mu_i}=\left(\prod_j w_j^{k_j}\right)e^{M h(s)},
\]

存在整函数解当且仅当存在共同整数`b≥1`使`k_j=Mb-μ_j`。此时全部解为

\[
v=C+\zeta\int_0^s t^{b-1}e^{h(t)}dt,\qquad\zeta^M=1.
\]

二维无权时，`v_xv_y=(xy)^k e^{2h(xy)}`可解当且仅当`k`为奇数。例如`xy e^{2xy}`恰有`C±e^{xy}`，而`x²y²e^{2xy}`无整函数解。这些是解析证明的结论，不是有限搜索猜想。

## 运行与构建

从仓库构建论文可直接运行`make paper`。验证程序和测试源码在本次交付的完整ZIP中；在解压后的完整目录运行：

```sh
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
make paper
```

Python需要3.10或更高版本；本次核验使用SymPy 1.14.0。英文PDF使用pdfLaTeX；中文PDF使用XeLaTeX、ctex及系统安装的Noto CJK字体。不需要BibTeX，因为两稿使用共同的`bibliography.tex`。字体文件不包含在本项目中。

最小使用例：

```python
import sympy as sp
from src.normal_form import enumerate_families, validate_datum
x, y = sp.symbols('x y')
families = list(enumerate_families(
    x*y, 2*x*y, (x, y), (1, 1), ((x, 1), (y, 1))))
q = families[0].normalized_example()  # (y, x)
validate_datum(x*y, 2*x*y, (x, y), (1, 1), ((0, 1),), q)
```

程序输入的因子分解必须是在复数域上的绝对不可约分解。程序检查乘积一致性，但不自动证明高次因子的绝对不可约性；测试中的分解均为线性因子。`normalized_example()`只选一个归一化根，不声称返回全部根或全部参数。无浮点输入，也不使用有限阶先验。

## 证据状态

本目录的分类、增长界和算术判据具有完整解析证明；尚未经过独立同行评审或Lean核验。31项测试全部通过只说明所列有限代数实例与实现一致。Xu–Ding的2026年相关论文已检索到，但完整定理逐项比对尚待取得全文，因此不作“首次解决”或“已达投稿标准”的声明。

`P=0`必须独立处理：全部解是至少独立于某一个坐标的整函数的并集，可有无限阶。`A`奇异或`g`不是多项式时，主定理不适用，稿件中附有边界说明。用户上传的原论文PDF不在公共仓库重新分发。
