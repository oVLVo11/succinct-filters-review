# Succinct Filters for Sets of Unknown Sizes 论文 Review 项目

本仓库记录三人小组研读 Liu、Yin、Yu 的 *Succinct Filters for Sets of Unknown Sizes* 并逐步撰写中文 Review 的全过程。当前材料属于阅读笔记、证据矩阵、证明核查和草稿提纲，不是可直接提交的 AI 代写终稿。

## 论文与目标

- 原论文：`Succinct Filters for Sets of Unknown Sizes.pdf`（ICALP 2020，arXiv:2004.12465）
- PSW 下界原文：`1304.1188v2.pdf`
- 核心问题：最终集合大小未知时，能否让 approximate membership filter 的空间随当前 `n` 增长，同时保持无漏报、误报率 `ε` 和高概率最坏常数操作时间？
- 核心结果：主体空间为 `n(log(1/ε)+log log n+O(log log log u))` 位，另有输入无关的 `u^c` 位预计算空间；无 failure 时插入和查询均为 worst-case `O(1)`。

## 小组分工

| 成员 | 姓名 | 主责 | Day 4 状态 |
|---|---|---|---|
| A | 刘威 | 模型、理论背景、概率、空间、下界和参数 | 已补误报预算、两级 failure 并合、空间与渐近条件，并审阅 B/C |
| B | 张书铖 | 核心构造、prefix matching、阶段迁移、伪代码和时间证明 | 已完成抽象伪代码、无漏报与时间框架、证明表操作列 |
| C | 陈戚 | 经典/后续研究、引用、评价和可读性审阅 | 已完成 2020 年后矩阵、三篇 E3 核验及共同证明表审阅 |

交叉审阅：A 审 B 的伪代码和复杂度；B 审 A 的概率/空间推导；C 审 A+B 的证据可追溯性；A+B 核查 C 的模型可比性。

## 当前进度（Day 4 整合）

已完成：

- A：`notes/memberA/probability-and-space-proof.md`
- B：`notes/memberB/pseudocode.md`、`notes/memberB/proof-notes.md`
- C：`notes/memberC/post-2020-work.md`、`references/post-2020-matrix.md`
- 共同证明链：`notes/proof-table.md`
- 第二轮审阅与会议：`discussions/review-day4*.md`、`discussions/meeting-day4.md`
- 三人 AI 使用日志：`ai-usage/`
- Day 4 三人材料整合提纲：`drafts/outline-v1.md`

仍未关闭：

- Claim 13 的阶段下标与存储归纳；
- 原文字面常数 10 的隐藏常数配平；
- 初始化/销毁/临时副本的位级空间峰值；
- 底层 data block 冗余的逐项展开；
- 自适应对手是否落在原文概率口径内。

这些项目必须在正文中标为条件或缺口，不得改写成小组已经独立证明。

## 目录导航

```text
AGENTS.md                    课程与学术诚信要求
Plan.md                      总体工作计划
work/day1.md ... day4.md     每日任务分配
notes/memberA/               A 的模型、下界、概率与空间笔记
notes/memberB/               B 的构造、伪代码与证明笔记
notes/memberC/               C 的相关工作与评价证据
notes/proof-table.md         六类结论共同证明表
references/                  文献清单、BibTeX 和比较矩阵
discussions/                 会议、问题、审阅和 Issue 记录
drafts/outline-v1.md         当前 Review 提纲
figures/                     结构、流程与证明依赖图
ai-usage/                    三位成员的 AI 使用及人工核查记录
```

## 证据状态约定

- Q0：已回原文核查到当前所需精度；
- Q1：结论明确但仍需证明或交叉复核；
- Q2：核心机制尚未理解；
- Q3：论文省略或黑盒内部细节需要展开；
- Q4：成员表述存在分歧。

后续研究另用 E1–E3 标注阅读深度。引用某论文、标题相近或支持“dynamic”都不等于在同一 unknown-size 模型下改进本文。

## 版本与学术诚信

- 每位成员应分批提交个人笔记、审阅回应和修订，不在截止日前一次性上传完整文稿。
- commit 信息应说明具体贡献，例如 `proof(A): derive false-positive budget`。
- AI 只用于定位、解释、列核查问题和检查逻辑；每次使用须在 `ai-usage/` 写明原问题、回答摘要、人工核查来源和采用边界。
- 最终 Review 由成员本人阅读原文后撰写。每位成员必须能解释核心论点、负责内容、主要参考文献、修改过程和 AI 使用情况。

## 下一阶段

Day 5 可在现有证据基础上分别起草“问题与重要性”“核心技术与实现”“相关研究与评价”，但所有 Q1/Q3 项须保留引用和限制条件。建议先由三位成员分别人工审核自己的 Day 4 产物，再形成分阶段 commit 与交叉 review。
