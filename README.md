# Signed circulant spectral research

本仓库研究固定 circulant 底图上的边符号与谱半径。当前研究分支是
[`research/circulant-1s-extension`](https://github.com/whzy3185/math/tree/research/circulant-1s-extension)。
目录保留历史结构；请从本页进入，不要把旧文件中的“CURRENT”“READY”
当作全仓库最新状态。

## 先读这些

| 需要了解什么 | 入口 |
|---|---|
| 所有主线有哪些成果、证据是什么 | [成果—证据—复用索引](research/repository_guide/RESULTS_INDEX.md) |
| 哪一份文章应该阅读 | [分支与稿件地图](research/repository_guide/BRANCH_AND_PAPER_MAP.md) |
| 哪些文件已过时，哪些只是退出当前正文 | [历史状态与替代关系](research/repository_guide/SUPERSESSION_MAP.md) |
| 现稿的主要优点、问题与整合判断 | [稿件初步评估](research/repository_guide/PAPER_ASSESSMENT.md) |
| 本次究竟检查了多少内容 | [覆盖范围与交付记录](research/repository_guide/COVERAGE_AND_COMPLETION.md) |
| 网页端 GPT 接手一般跳长研究 | [研究情况说明](research/generalization/circulant_1s/extension_20260905/REPOSITORY_STATUS_20260905.md) |

## 当前三份对象

- **冻结八周期稿：** `6766ecb`，标签 `freeze/period8-jgt-2026-09-05`。
  原文件保持不变，结尾有已记录的有限全局极小值问题。
- **纠错后的八周期稿：**
  [`paper/period8-conclusion-correction`](https://github.com/whzy3185/math/tree/paper/period8-conclusion-correction)，
  提交 `2dc5b90`。中英文结尾已修复，PDF 已重新编译。
- **一般跳长成果：** [独立研究目录](research/generalization/circulant_1s/extension_20260905/)。
  包括全部偶跳长的 sub-eight 构造与多项式谱隙；尚未写入正式稿。

已有推广证明不等于已经完成新论文，也不等于得到全部最优符号。
现有 Lean kernel 只覆盖显式正 holonomy 八周期 witness 的逐特征值
严格比较；具体边界见成果索引。

本轮仅整理、索引和已知错误修复，没有新增数学探索、合并历史 theorem
范围或启动大规模计算。下一阶段的优先任务是论文级独立审查与文献比较。
