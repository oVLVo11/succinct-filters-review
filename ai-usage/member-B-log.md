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

---

## 2026-07-28

### 使用者
张书铖（成员 B）

### 使用工具
Cursor Agent

### 提问目的
按 `work/day5.md` 撰写技术章节初稿，并完成对 A 的第一审阅、事实核查与会议记录中的 B 部分。

### AI 回答摘要
- 协助按 day5 十节结构组织 `drafts/section-B-technique-and-proof.md`。
- 协助写入缺口口径（常数 10、阶段下标）、回应证明表中 C 对“线性 initialize”的批评。
- 协助起草 B→A 的 6 条审阅意见与 fact-check 术语表。

### 人工核查方式
- 对照 Claim 13、式 (2)、Thm 10 与既有 `pseudocode.md`/`proof-table.md`。
- 对照 A 的 `probability-and-space-proof.md` 检查衔接句。
- 章节由笔记改写，未整段粘贴 AI 成稿；禁止性措辞已自检。

### 核查结论
- 初稿可送 C 审阅；开放 Q1/Q3 已在章首与正文标明。
- 对 A 的审阅待 A 章节定稿后关闭。

### 最终使用方式
辅助提纲与组织；正文依据个人笔记与原文核查。建议 commit：`draft(B): explain prefix matching and staged construction` / `draft(B): write operations correctness and complexity` / `review(B): verify model parameters and lower-bound wording`。

---

## 2026-07-28（Day 6）

### 使用者
张书铖（成员 B）

### 使用工具
Cursor Agent

### 提问目的
按 `work/day6.md` 完成 B 的整合、图同步、读者测试、Issue/会议记录与 PDF v1 尝试。

### AI 回答摘要
- 协助将 §6–§9 写入 `drafts/review-integrated.md`（15 部分骨架；A/C 章标桥接）。
- 协助生成 `issues-day6.md`、`review-day6.md`（B 测 C 相关工作笔记 ≥5 条）、`meeting-day6.md`、`references/citation-audit.md`（B 技术引用抽查 + 待 C）。
- 协助同步 `figures/{architecture,growth-process,query-insert-flow,proof-dependency}.md`。
- 协助检测本机无 pandoc/xelatex，按规则记录 PDF 失败而非伪造。

### 人工核查方式
- 对照 Day 5 `section-B`、Claim 13、`pseudocode.md`、开放 Issue。
- 对照 `notes/memberC/related-work.md` 做普通读者测试。
- 强断言清单自检：字面 10、阶段归纳、ε≠δ、¬failed。

### 核查结论
- B 主责技术章已入整合稿；A/C 桥接未替换前不可称全文完成。
- PDF v1 未生成（环境缺工具）；md 为可追溯源。

### 最终使用方式
辅助组织与过程文件；正文由笔记改写并人工定稿。建议 commit：`integrate(B): unify construction implementation and proof` / `figures(B): align diagrams with draft` / `review(B): verify stage invariants and operation bounds`。

