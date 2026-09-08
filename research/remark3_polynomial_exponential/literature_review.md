# 文献与来源核验

检索日期：2026-09-08。原文依据是用户实际上传的 `2605.09585v1.pdf`，不是仅凭截图猜测上下文。

## 1. 用户指定来源

Feng Lü, *On entire solutions for a class of product-type nonlinear PDEs in C^n*, arXiv:2605.09585v1, 2026-05-10。

https://arxiv.org/abs/2605.09585

第 3–4 页：混合偏导关系、图分块及 p=1 的 Theorem 2。第 5 页：z=A^T w 换元。第 6 页：Remark 3 的 (1.8)、(1.9)。第 7–9 页：图内指数比较及连通块分析。当前检索到的 arXiv 页面仅列出 v1。

**准确边界**：原文对 (1.8) 说省略换元后的细节，对 (1.9) 只说明该方法可能适用并需要更精细分析。原文并没有直接提供本文的带多项式因子的必要充分有限分类、加权计数或有限参数族定理。因此这些内容标为本次推导，而非原文结论的转述。

## 2. 实际用于证明的外部分析输入

Qi Han and Jingbo Liu, *A Short Proof of the Lemma of the Logarithmic Derivative in Several Complex Variables*, Complex Analysis and Operator Theory 19 (2025), 92。

https://doi.org/10.1007/s11785-025-01701-x

已读取公开正文 Theorem 1.1。条件为 n>=2、f 亚纯且非常数、f(0) 非零有限。它给出任意 0<r<R 的两半径邻近函数估计，没有有限阶假设。本稿另证共同半径选择，且另计代数零点导致的极点项；不把邻近函数 m 偷换成特征函数 T。

Al Vitter, *The lemma of the logarithmic derivative in several complex variables*, Duke Math. J. 44 (1977), 89–104。

https://doi.org/10.1215/S0012-7094-77-04404-0

已核对出版方元数据。本稿的具体不等式引用的是上面的 Han–Liu 已读全文，而非声称已重读 Vitter 全文。

W. Stoll, *Holomorphic Functions of Finite Order in Several Complex Variables*, CBMS 21, AMS, 1974。

https://www.ams.org/books/cbms/021/

R. C. Gunning and H. Rossi, *Analytic Functions of Several Complex Variables*, Prentice-Hall, 1965。

https://bookstore.ams.org/view?ProductCode=CHEL%2F368.H

Piotr Achinger, *Fundamental groups in algebraic geometry*, notes dated 2025-03-19, Section 3.2：解析化保持连通分量。已读取相关段落（PDF 第 35 页）。

https://achinger.impan.pl/pi1/notes.pdf

## 3. 必须补齐全文比对的相关论文

Hong Yan Xu and Xin Ding, *Description of entire solutions of the product type nonlinear PDEs with a generalized exponential term in C^3*, J. Math. Anal. Appl. 561 (2026), 130680。

https://doi.org/10.1016/j.jmaa.2026.130680
https://www.sciencedirect.com/science/article/abs/pii/S0022247X26002921

出版方检索结果确认题名和主题；其他出版方参考文献确认卷号与文章号。直接打开 ScienceDirect 正文失败，尚未取得全部定理，故**不能**断言该文要求有限阶，不能断言它没有处理某些 p exp(g) 情形，也不能据此宣称本文首次完成相关推广。

Wei Chen and Qi Han, *On entire solutions to eikonal-type equations*, J. Math. Anal. Appl. 506 (2022), 124704。

https://doi.org/10.1016/j.jmaa.2020.124704

确认书目信息与相关主题；尚未逐条比对全文定理。尤其注意已有二维加权乘积类研究可能与本文二维推论重叠。

Feng Lü and Z. M. Ma, *Entire solutions of product type nonlinear partial differential equations in C^n*, Glasgow Math. J., DOI 10.1017/S0017089525100657。原上传文献称 2025 online；当前出版方页面可检索。

https://doi.org/10.1017/S0017089525100657

## 4. 当前可支持与不可支持的表述

可支持：本文对用户给定 Remark 3 的方程给出一条明确、可逐步核查的解析证明和有限代数参数化；不需要假设解的有限阶；含正整数权重扩展。

不可支持：已经证实无文献重叠；已经同行认可；已发表或已录用；保证任何分区期刊接收；符号测试或本次内部审计等于 Lean 形式化。
