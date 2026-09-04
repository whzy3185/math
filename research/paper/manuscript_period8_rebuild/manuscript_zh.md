# 周期八解析反例族：带符号谱半径极小化

## 1. 引言与主定理

研究固定图 `C_n(1,2)` 的边符号与邻接谱半径。自然的 twisted 候选并非最优：
对所有 `n=8L, L>=4`，显式的 alpha = +1 周期八 Hamilton 规范符号给出严格更小的谱半径。

## 2. 规范坐标与有限 Bloch 分解

介绍 switching、Hamilton gauge、三角形字 `tau`、holonomy 与有限 cell 分解；有限相位满足 `z^L=alpha`。

## 3. 手性周期八 fiber

固定 `tau=(+,+,-,+,-,-,+,-)`，给出 `8 x 8` fiber、手性对合及
`8 x 8 -> 4 x 4 -> 2 x 2` 约化，得到多项式 `P(y,c)`。

## 4. 一致多项式证书

解析证明当 `y>=1561/200`、`c<=2` 时 `P(y,c)>0`，故所有有限 fiber 的平方本征值严格小于该阈值。

## 5. 无穷反例族

证明 twisted benchmark 的平方严格大于 `1561/200`，完成主定理比较。

## 6. 为什么周期八特殊

给出局部平方恒等式、周期八 trichotomy 与唯一的 sub-eight antipodal two-defect phase。小型 recurrence 仅作为精确整数计算披露。

## 7. 一般周期 defect 障碍

通过 `M1,M2,M3` 推导 defect 密度与聚集的必要不等式；不作全周期分类主张。

## 8. 结论与范围

明确不处理 R2/R4/R6/G6、旧枚举、all-even 分类或全部 minimizer。

### Lean 说明

Sections 2--5 的 alpha = +1 显式 witness 核已由 Lean 独立验证。该说明不覆盖 alpha = -1 包装或第 6--7 节的结构性推广。
