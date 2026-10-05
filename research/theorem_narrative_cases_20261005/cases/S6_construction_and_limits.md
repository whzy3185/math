# S6：先让局部障碍可见，再让定量放大变得有意义

Naserasr, Pham, Pujol, Zhou, *Fractional balanced chromatic number and arboricity of planar (signed) graphs*.

- 精读版本：[arXiv:2505.16808v1](https://arxiv.org/pdf/2505.16808v1)，arXiv日期2025-05-22，16页；题名页另印2025-06-13
- arXiv DOI：[10.48550/arXiv.2505.16808](https://doi.org/10.48550/arXiv.2505.16808)
- Journal of Graph Theory113(1)(2026),5–18；在线2026-04-18；[期刊 DOI](https://doi.org/10.1002/jgt.70047)
- 本次重点：pp.1–3,6–7,9–11,14–15；Theorems13–16、Remark17；期刊正文不等同于该预印本

## 源文叙事地图（限量概述）

Title: two related fractional parameters. Abstract: conjecture obstruction followed by quantitative construction. Prior work: a historical planar gadget (§1). Gap: whether the proposed bound two survives fractionalization. Obstruction: local coloring constraints enforced by the gadget (§2). Architecture: first prove a qualitative violation, then quantify and iterate it; give explicit coloring witnesses (§§3–5). Sharpness/limits: 83/41 is a limit for the signed construction, not an exhibited finite attaining example. However, Theorem16 and Remark17 give a finite graph attaining fractional arboricity 2+2/25. The preprint abstract's limit wording for arboricity must not override this theorem. Closing material explains the construction method's ceiling rather than claiming a universal optimum. The journal abstract explicitly identifies a 34-vertex example.

## 对 C029 的原创分析

C029也有“有限对象引出无限族”的机会，但必须选对层次。有限有理数种子不是一串越来越精细的实验记录；它的数学责任是进入一个可以证明不变与收缩的区域。然后分析论证覆盖所有更长链，最后二关联估计覆盖所有单元数。这样读者理解的是有限理由如何支持无限量词。

可以把原稿第四节第一段改成一个明确请求：我们需要的不是长链的每个特征值，而是内部消去之后留给端部的响应，以及对汇合相邻响应后的接点核心的统一正定控制。这个请求让递推、响应衰减、极限矩阵各有必要性。

数值的身份也要分开。7.90537是一个认证谱帽；one-cell的supremum位于宽10^{-6}的区间；这既不是精确supremum，也不是已经证明谱半径序列收敛。故事不能把“逼近共同边界模型”偷换成“整个图的谱半径收敛到这个小数”。

## 为何是数学文章范例

局部构造先回答是否可能，后续定量论证再回答能推进多远。给出上方着色见证与下方障碍，使具体构造不只是图片或计算样本。可学的是从一个可理解的障碍长出问题，而不是复制四着色历史作为任何图论文的开头。
