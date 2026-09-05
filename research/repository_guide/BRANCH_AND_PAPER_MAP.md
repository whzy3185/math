# 分支与稿件地图

本表基于2026-09-05本地分支与tracking refs。不会以分支名中的
`complete`、`ready`推断数学完成。大部分旧Target A分支已是当前推广
分支的祖先，内容并未因分支停留在旧提交而丢失。

## 三个应当区分的版本

| 用途 | 分支/提交 | 内容 |
|---|---|---|
| 当前研究与导航 | `research/circulant-1s-extension` | 一般偶跳长、量化界和导航；不含纠错后的正文 |
| 冻结原稿 | `paper/jgt-authorial-rewrite` / `6766ecb` | 六节英文16页、中文15页；原结尾问题有误 |
| 纠错可读稿 | `paper/period8-conclusion-correction` / `2dc5b90` | 从冻结稿分出，仅修中英文结尾并重新编译 |

直接阅读纠错稿：
[英文PDF](https://github.com/whzy3185/math/blob/paper/period8-conclusion-correction/research/paper_strengthening/manuscript_period8_jgt/main_en.pdf)、
[中文PDF](https://github.com/whzy3185/math/blob/paper/period8-conclusion-correction/research/paper_strengthening/manuscript_period8_jgt/main_zh.pdf)、
[英文TeX入口](https://github.com/whzy3185/math/blob/paper/period8-conclusion-correction/research/paper_strengthening/manuscript_period8_jgt/main_en.tex)。

## 历史分支职责

| 分支 | 检查时commit | 与当前主线的关系 |
|---|---|---|
| `main` | `fb4375f`（整理前） | 23文件的初始化状态，不代表最新研究 |
| `agent/target-a-discovery-snapshot` | `0ebfc7b` | 历史研究/旧稿基线，已在主线祖先中 |
| `exp/circulant-1s-generalization` | `833face` | Task60一般模型、twisted基础，已继承 |
| `proof/complete-mathematical-closure` | `44ff33a` | 历史计算辅助分类及解析缺口，已继承 |
| `analytic-proof-first` | `7b6a351` | 八周期解析化与有限Lean kernel，已继承 |
| `research/spectral-related-work-refresh` | `ebc6de4` | 文献与文章结构资料，已继承 |
| `period8-paper-strengthening` | `1201d4e` | 精确谱、一般半胞机制、原稿和文献库，已继承 |
| `assist/workbuddy-analytic-support-20260902` | `01b82e1` | 本地协作worktree；该提交已在主线祖先中，未修改其工作区 |
| `codex/old-conjecture-audit-phase1` | `74e9735` | 独立旧猜想/poset方向，2个独有提交、156个相对共同祖先的变更路径；本轮只读状态及价值报告，不合并 |

机器分支树及每个分叉路径见 [INVENTORY_SUMMARY.json](INVENTORY_SUMMARY.json)。
此表区分branch tip、已提交继承关系与worktree未提交改动；后二者不能混淆。

本轮另为`main`增加一个仅含GitHub链接的根README，使默认仓库首页能
找到当前研究和纠错稿。其余早期文件保持原样；这不是把研究成果合入main。
上述机器清单仍对应整理前快照，不把导航新增误算成数学研究增量。

## 旧论文目录

`research/paper/manuscript_md`、`manuscript_tex`、`manuscript_tex_pub`、
`manuscript_tex_pub_zh`、`task58`、`manuscript_period8_rebuild` 保留历史范围。
它们可能包含all-even、G6、附录证书、旧作者配置，不能拼接成当前稿。
当前期刊稿始终从 `research/paper_strengthening/manuscript_period8_jgt`
读取，并明确所在分支。

## 当前不做的Git操作

本轮没有合并独立旧猜想分支，没有删除旧分支、tag或worktree，没有
覆盖任何预存未提交改动。纠错分支的两个PDF是可恢复的Git版本，原稿
可从freeze tag精确取回。新导航只改变入口，不改变数学证据历史。
