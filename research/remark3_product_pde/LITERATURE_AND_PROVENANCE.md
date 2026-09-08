# 文献、来源与新颖性边界

核验日期：2026-09-08。只将实际读到的全文、出版方记录或索引描述作为相应层级的证据。以下不是穷尽性文献综述。

## 用户提供的直接来源

Feng Lü, *On entire solutions for a class of product-type nonlinear PDEs in C^n*, arXiv:2605.09585v1，提交于2026-05-10。

- 公开记录：https://arxiv.org/abs/2605.09585
- 本次实际阅读全文：用户上传的11页PDF，文件名2605.09585v1.pdf。
- 第3–4页：定理2，右端为e^g的分类，不预设有限阶。
- 第5页：式(1.6)为z=A^T w；备注2给出g为超越整函数时的反例。
- 第6页：Remark 3式(1.8)和式(1.9)，分别对应e^g和p e^g。
- 第6–10页：原文定理2证明。

本次稿件明确把p=1的原问题标为原文定理经换元的展开，不主张该结论是本次新发现。用户原PDF没有上传到公共仓库；本地来源SHA256记录于verification/REPORT.md。

## 已核验的解析工具

A. Vitter, *The lemma of the logarithmic derivative in several complex variables*, Duke Mathematical Journal 44(1) (1977), 89–104。

DOI：https://doi.org/10.1215/S0012-7094-77-04404-0

出版方记录：https://projecteuclid.org/journals/duke-mathematical-journal/volume-44/issue-1/The-lemma-of-the-logarithmic-derivative-in-several-complex-variables/10.1215/S0012-7094-77-04404-0.full

核验层级：原始文献的出版方书目信息；不是声称取得其付费全文。

Qi Han and Jingbo Liu, *A Short Proof of the Lemma of the Logarithmic Derivative in Several Complex Variables*, Complex Analysis and Operator Theory 19, Article92 (2025)，2025-05-28发表。

全文：https://link.springer.com/article/10.1007/s11785-025-01701-x

核验层级：出版方开放全文及定理1.1的显式双半径不等式。作者是Han与Liu两人，不是Han单人。该引理估计的是接近函数m；本稿另证极点项N=O(log r)，才得到完整特征函数T的估计。

## 背景文献

Feng Lü and Zimeng Ma, *Entire solutions of product type nonlinear partial differential equations in C^n*, Glasgow Mathematical Journal 68(2) (2026), 257–262；在线发表日期2025-08-12。

DOI：https://doi.org/10.1017/S0017089525100657

核验层级：Cambridge出版方摘要及卷期、页码、在线日期。摘要处理右端1和有限阶条件。在线年份2025与正式卷期2026不能混淆。

H. Y. Xu, K. Liu and Z. X. Xuan, *Results on solutions of several product type nonlinear partial differential equations in C^3*, Journal of Mathematical Analysis and Applications 543 (2025),128885。

DOI：https://doi.org/10.1016/j.jmaa.2024.128885

核验层级：用户上传论文的参考文献与出版方书目信息；本稿不声称已逐页审查这篇21页论文。

W. Chen and Q. Han, *On entire solutions to eikonal-type equations*, Journal of Mathematical Analysis and Applications 506(1) (2022),124704。

DOI：https://doi.org/10.1016/j.jmaa.2020.124704

核验层级：出版方记录、作者机构页面及上传论文参考文献。仅作为相关背景，不据未取得的全文虚构具体比较结论。

## 重要的潜在重叠：尚须全文比对

H. Y. Xu and X. Ding, *Description of entire solutions of the product type nonlinear PDEs with a generalized exponential term in C^3*, Journal of Mathematical Analysis and Applications 561(2) (2026),130680，25页。

DOI：https://doi.org/10.1016/j.jmaa.2026.130680

出版方页面：https://www.sciencedirect.com/science/article/abs/pii/S0022247X26002921

核验层级：出版方索引与期刊卷期页；索引描述将其定理2.1概括为满秩条件下的有限阶超越整函数分类。多次全文访问未取得可读内容，故不能确定其所有假设、是否涉及完全相同的前因子、以及与本稿各推论的重合范围。

不得把题目相近推断成结论完全相同，也不得反向推断成“本稿从未被研究”。本文能够主张的是给出了独立的完整解析推导；优先权、创新程度和投稿定位必须在全文核对及专家审查后再评估。

## 本稿内容的证据标签

原文e^g分类及换元：来源已有结果。自动有限阶、带多项式前因子的必要充分标准形、有限线性判定、加权推广、连通解上界和单项式算术准则：本稿提供解析证明，尚无外部认证。代码实例：精确有限验证。未进行Lean认证、同行评审或投稿；没有以实验现象冒充普遍定理，也没有将自行推导直接标成出版事实。
