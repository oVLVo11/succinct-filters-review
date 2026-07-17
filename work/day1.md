Day 1 总目标

第一天重点不是写正文，而是留下“真实开始研究”的过程痕迹：建仓库结构、通读论文、明确问题、建立个人笔记、开会记录、形成初版提纲。三人各自至少 2 个有效 commit，合计至少 6 个有效 commit。

成员 A：问题模型与基本定义

阅读范围：

论文标题、摘要、引言；

问题定义相关部分；

主要结果陈述；

涉及 unknown size、approximate membership query、filter、dictionary、false positive / false negative 的段落；

初步浏览下界或空间复杂度相关定理，只记录“不懂点”，不要求当天完全证明。

需要提交到 GitHub 的文件：

notes/member-A/paper-reading.md

notes/member-A/definitions.md

notes/member-A/lower-bound-notes.md

参与更新 drafts/outline-v1.md 中“问题与重要性”部分

若使用 AI，更新 ai-usage/member-A-log.md

当天任务：

整理核心术语表：universe、set size、epsilon、lookup、insert、filter、dictionary、false positive、false negative、unknown size；

写出“这篇论文到底解决什么问题”的 500-800 字初稿；

记录至少 5 个暂时不懂的问题，尤其是下界、空间公式、参数限制；

给 B 的技术路线图提出至少 2 个问题或评论。

成员 B：核心构造与技术路线

阅读范围：

摘要、引言、论文结构；

构造总览部分；

数据结构、hash、prefix、stage、growth、migration、deamortization 相关段落；

初步浏览主要定理依赖的引理列表。

需要提交到 GitHub 的文件：

notes/member-B/paper-reading.md

notes/member-B/construction-notes.md

notes/member-B/proof-notes.md

可新建或草拟 figures/growth-process.drawio / figures/query-insert-flow.drawio 的文字说明版

若使用 AI，更新 ai-usage/member-B-log.md

当天任务：

列出论文中出现的所有技术组件，并说明每个组件“解决什么小问题”；

画出或文字描述整体构造路线：元素如何被 hash，如何用 prefix 表示，为什么要分阶段，扩容时发生什么；

标记主定理依赖哪些 lemma / invariant / probabilistic argument；

给 C 的相关工作分类提出至少 2 个“是否和本文模型一致”的核查问题。

成员 C：相关工作与资料入口

阅读范围：

论文的 related work、introduction 中比较已有工作的部分；

参考文献列表；

Bloom filter、dynamic/scalable filter、quotient filter、cuckoo filter、succinct dictionary、hashing/deamortization 相关引用；

初步搜索论文发表后的相关研究，但第一天只做候选清单，不急着下结论。

需要提交到 GitHub 的文件：

notes/member-C/paper-reading.md

notes/member-C/related-work.md

notes/member-C/post-2020-work.md

references/source-list.md

references/bibliography.bib

若使用 AI，更新 ai-usage/member-C-log.md

当天任务：

提取原论文正式链接、arXiv 链接、BibTeX；

把参考文献初步分成五类：Bloom filter、动态/可扩展 filter、succinct dictionary、quotient/cuckoo filter、hashing 与 deamortization；

每类至少记录 2-3 个条目，包括标题、作者、年份、来源、与本文关系；

给 A 的定义和问题描述提出至少 2 个“是否需要补充背景”的问题。

共同提交文件

第一天结束前应共同完成或初始化：

README.md

drafts/outline-v1.md

discussions/meeting-day1.md

discussions/questions.md

三人的个人阅读笔记

三人的 AI 使用日志文件，即使当天没有使用 AI，也写明“今日未使用”或“未采纳 AI 输出”

交叉审阅安排

第一轮交叉审阅：

B 审阅 A：检查问题定义、术语、unknown size 的解释是否清楚；

C 审阅 B：检查技术路线是否能被未读过论文的人看懂；

A 审阅 C：检查相关工作分类是否贴合本文问题，而不是单纯罗列文献。

审阅要求：

每人至少给另一位成员留下 2 条实质性评论；

评论必须写入 GitHub PR、Issue、commit discussion，或 discussions/meeting-day1.md；

每条评论要具体指出文件、段落、问题，例如“这里没有说明 false positive 与 false negative 的区别”。

Day 1 会议安排

建议当天结束前开 20-30 分钟同步会，记录到 discussions/meeting-day1.md。会议必须回答：

论文研究对象是什么？

“unknown sizes” 到底未知的是什么？

为什么不能简单预先设置一个足够大的容量？

论文主要结果分别是什么？

filter 和 dictionary 的结构区别是什么？

每个人今天还有哪些 Q1/Q2 问题？

当天验收标准

硬性验收：

三人每人至少 2 个有效 commit；

每人至少 1 份个人阅读笔记；

至少 1 份共同会议记录；

至少 1 份初版 review 提纲；

至少 1 份参考文献或来源清单；

至少完成一轮交叉评论；

所有内容已推送到公开 GitHub 仓库。

理解验收：

每人都能用 3 分钟解释：为什么这篇论文不是简单设计一个可以扩容的 Bloom filter；

每人都能说出自己当天读了论文哪几部分、提交了哪些文件、还有哪些没懂；

任何 AI 辅助都必须留下问题、回答摘要、人工核查方式和最终使用方式。

