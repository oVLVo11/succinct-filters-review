# Succinct Filters for Sets of Unknown Sizes 论文 Review 项目

本仓库用于三人小组研读论文 *Succinct Filters for Sets of Unknown Sizes*，并逐步完成一篇以中文为主体的论文 review。仓库重点保存从资料收集、论文阅读、问题讨论、草稿提纲、交叉审阅到最终成稿的过程记录。

## 论文信息

- 论文题目：*Succinct Filters for Sets of Unknown Sizes*
- 作者：Mingmou Liu, Yitong Yin, Huacheng Yu
- arXiv：`arXiv:2004.12465`
- 本地论文文件：`Succinct Filters for Sets of Unknown Sizes.pdf`
- 主题关键词：Bloom filters, approximate membership, succinct data structures, dynamic dictionaries, unknown-size filters

## 小组分工

| 角色 | 姓名 | 主要负责内容 |
|---|---|---|
| 成员 A | 刘威 | 问题模型、基本定义、理论背景、空间下界、参数关系 |
| 成员 B | 张书铖 | 核心构造、prefix matching、阶段迁移、数据结构实现、证明依赖 |
| 成员 C | 陈戚 | 相关研究、后续研究、参考文献、论文评价 |

交叉审阅安排：

- B 审阅 A 的问题定义、术语和下界解释。
- C 审阅 B 的技术路线和实现说明。
- A 审阅 C 的相关工作分类和理论结果表述。

## 当前进度

目前处于 Day 2 收尾阶段：

- 已创建 GitHub 仓库并建立初始版本历史。
- 已保存论文 PDF、课程要求和工作计划。
- 成员 A 已完成正式模型、Theorem 1/10 参数、空间下界和高概率语义的 Day 2 核查。
- 成员 B 已完成公式 (2)、Claim 13、8 元素阶段示例及查询/插入流程的 Day 2 核查。
- 已将 A/B 阶段结论汇总到 `discussions/meeting-day2.md`。
- 已将 review 提纲更新为 Day 2 A/B 材料整合版：`drafts/outline-v1.md`。
- 已按 Q0-Q4 更新问题清单：`discussions/questions.md`。
- 已建立 AI 使用记录目录：`ai-usage/`。
- 成员 C 的相关工作笔记、来源清单和文献矩阵仍待补齐，因此 Day 2 尚未三人完整验收。

## 仓库结构

```text
.
├── README.md
├── AGENTS.md
├── Plan.md
├── Succinct Filters for Sets of Unknown Sizes.pdf
├── ai-usage/
│   ├── member-A-log.md
│   └── member-B-log.md
├── discussions/
│   ├── meeting-day2.md
│   └── questions.md
├── drafts/
│   └── outline-v1.md
├── figures/
│   ├── growth-process.md
│   └── query-insert-flow.md
├── notes/
│   ├── memberA/
│   │   ├── paper-reading.md
│   │   ├── definitions.md
│   │   └── lower-bound-notes.md
│   ├── memberB/
│   │   ├── paper-reading.md
│   │   ├── construction-notes.md
│   │   └── proof-notes.md
│   └── memberC/
└── work/
    └── day1.md
```

## 主要入口

- 工作计划：`Plan.md`
- 课程/项目要求：`AGENTS.md`
- Review 初版提纲：`drafts/outline-v1.md`
- 问题清单：`discussions/questions.md`
- 成员 A 笔记：`notes/memberA/`
- 成员 B 笔记：`notes/memberB/`
- 图示文字版：`figures/`
- AI 使用记录：`ai-usage/`

## 过程记录原则

本项目重视过程分，因此每次推进应尽量满足：

- 每位成员每天至少产生 2 次有实际内容的 commit。
- commit 信息要说明具体工作，不使用 `update`、`final`、`修改` 这类模糊信息。
- 重要理解、疑问和争议进入 `discussions/questions.md` 或成员个人笔记。
- AI 辅助必须记录问题、回答摘要、人工核查方式和最终使用方式。
- 主要章节后续尽量通过分支和 Pull Request 合并，保留审阅痕迹。

推荐 commit message 示例：

```text
notes(A): clarify unknown-size filter model
notes(B): explain prefix matching construction
refs(C): add related work comparison entries
draft: revise review outline
ai-log(A): record verification of lower-bound question
```

## AI 使用说明

允许使用 AI 辅助理解概念、整理核查问题、检查逻辑跳跃或格式问题，但不接受 AI 代写最终 review。所有 AI 使用应写入 `ai-usage/`，并由对应成员对照原论文或正式文献人工核查。

当前记录：

- `ai-usage/member-A-log.md`
- `ai-usage/member-B-log.md`

## Git 使用说明

查看当前状态：

```powershell
git status
```

提交一次明确的工作：

```powershell
git add <文件路径>
git commit -m "类型: 具体说明"
git push
```

同步远程更新：

```powershell
git pull
```

建议成员在修改前先 `git pull`，避免多人同时修改同一文件造成冲突。

## 后续待办

- 陈戚补充 `notes/memberC/` 中的相关研究笔记。
- 建立 `references/bibliography.bib`、`references/source-list.md`、`references/literature-matrix.md`。
- 陈戚审阅张书铖的 8 元素示例，刘威审阅相关工作矩阵。
- 刘威正式审阅张书铖的阶段示例，张书铖复核刘威对审阅意见的修改。
- Day 3 解决 Claim 13 下标对齐、常数 10 配平及底层 `D(m,ell)` 的 Q1/Q2 问题。
- 将 `figures/` 中已经同步的文字流程说明逐步转为正式图。
- 在证据核查完成后，将 `drafts/outline-v1.md` 逐步扩展为分章节草稿。
