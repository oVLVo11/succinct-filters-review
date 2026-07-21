# 成员 B AI 使用日志

按 `AGENTS.md` / `Plan.md`：允许辅助理解与检索，不接受代写 Review 正文。

---

## 2026-07-17

让 AI 搭建提交文件结构，辅助部分章节翻译与定理理解；大部分阅读由人工完成。

---

## 2026-07-20

### 使用者
张书铖（成员 B）

### 使用工具
Cursor Agent

### 提问目的
按 `work/day2.md` 完成构造侧任务：核查 Claim 13、写 8 元素阶段示例、修订增长/查询图、更新 questions 与会议中的 B 部分。

### 原始问题（摘要）
担任 member B，根据 day2 要求完成任务。

### AI 回答摘要
- 协助对照 ar5iv/PDF 定位 Claim 13：`i=⌈log n⌉`、for 10 times、四结构查询、短/长串迁移。
- 协助整理 n=1..8 状态表与 `figures/growth-process.md` 逐 n 对照。
- 标出不变式段落 `n∈[2^i,2^{i+1})` 与 `⌈log n⌉` 可能的下标对齐问题，写入 Q1，未当作已证明结论。

### 人工核查方式
- 对照本地 PDF 与 ar5iv html（2004.12465）Claim 13 证明段、§3.1 式 (2)、§3.1 阶段定义。
- 8 元素示例明确标注为教学示意前缀，不写入碰撞概率或最终 Review 正文。

### 核查结论
- 插入/查询/10 次维护/迁移去向：与原文一致，写入笔记。
- 不变式下标对齐：部分存疑，标 Q1，待 Day 3。
- 未把 AI 表述直接当作正式证明。

### 最终使用方式
仅用于定位原文与组织笔记；示例与结论均经 PDF 核对后改写。

---

## 2026-07-21

### 使用者
张书铖（成员 B）

### 使用工具
Cursor Agent

### 提问目的
按 `work/day3.md` 完成十组件拆解、阶段不变式、`D(m,ℓ)` 接口、常数 10 分析、体系结构图、Issue、审阅 A。

### AI 回答摘要
- 协助按统一模板写 10 个组件；引入 `i★`/`epoch`；区分字面 10 与渐近配平。
- 协助 `architecture.md`、流程挂接、两个 Issue 验收条件。

### 人工核查方式
对照 Claim 13 接口与维护循环、式 (2)、A 的 `review-day3-A.md` 与引理笔记；未关闭下标归纳与字面 10。

### 核查结论
接口/控制流已核实；阶段下标与字面 10 保留 Issue；§5 data block 未展开。

### 最终使用方式
仅辅助组织；结论经原文核对后写入笔记。建议 commit：`notes(B): decompose dictionary and filter components` 等（见 day3.md）。

---

## 2026-07-22

### 使用者
张书铖（成员 B）

### 使用工具
Cursor Agent

### 提问目的
按 `work/day4.md` 完成伪代码、无漏报/时间证明框架、证明表 B 列、审阅 A、会议与问题清单更新。

### AI 回答摘要
- 协助定义 FilterState 与 Initialize/Lookup/Insert/MigrateOneStep 等抽象伪代码。
- 协助整理三种状态下无 FN 论证与插入工作量分解；区分 failure API 与引言 rebuild 脚注。
- 协助填写 `proof-table.md` 的不变式/操作列，并为 A 留出概率/空间空位。

### 人工核查方式
- 对照 Claim 13、Thm 10、式 (2)；对照 A 下界笔记 §14 复算 gamma 叙述。
- 明确 FinalizeStage/StartNewStage/HandleFailureOrRebuild 的“抽象/非主定理 API”边界。
- 未将字面 10 或存储归纳标为已证。

### 核查结论
- 伪代码与时间/无 FN 控制流框架：可进入 Day 5（带条件）。
- 证明表 B 列已交；A 列待补。
- gamma 机制复算与 A 一致。

### 最终使用方式
辅助组织；全部结论经原文核对。建议 commit：`impl(B): define state and pseudocode for all operations` / `proof(B): verify migration invariants and worst-case work` / `review(B): align probability proof with stage construction`。

