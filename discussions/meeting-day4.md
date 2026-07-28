# Day 4 会议记录

日期：2026-07-22  
状态：A、B、C 的书面讲解与交叉追问已汇总

---


## 记录

| 提问人 | 问题 | 回答摘要 | 纠错 |
|---|---|---|---|
| A | failure 与 FP 为何不能相加成一个错误率？ | FP 是无 failure 条件下对固定非成员查询的碰撞概率；failure 是内部结构放弃保证的整段事件。 | B 原回答只说“不是一回事”，补上条件概率与时间范围。 |
| C | 查询只看四结构，是否足以证明空间峰值？ | 不足；下一层可能已初始化但未查询，旧层可能待销毁。 | A 在空间笔记中改按 Lemma 11 总界与生命周期解释。 |
| B | 式 (2) 的求和按存储层还是插入阶段？ | 按插入时采用 `ℓ_i` 的阶段；迁移不重新分配误报预算。 | 已写入 A §2。 |
| A | Resizable Retrieval 是否全面支配本文？ | 不能；支持删除和当前规模空间是新进展，但额外项、参数和 whp 口径不同。 | 采用 C 的多维比较，不作单一排名。 |

---

## 互述

- B 复述 A 的 FP 并合骨架：每阶段至多 `2^i` 个前缀，各碰撞概率 `2^{-ℓ_i}`，跨阶段调和求和小于 `ε`。
- A 复述 B 的 Insert 工作量分解：一次写入加原文十轮常数黑盒维护；最坏时间还依赖“写入层提前就绪”。
- C 复述 A 的 failure 链：式 (3)–(5) 先把单个 `D_i` 压到 `u^{-2C}`，再对至多 `log u` 层并合至 `u^{-C}`。

---

## 与证明表同步的决议

- 无 FN / 查询时间 / 插入时间：以 B 伪代码+证明笔记为操作侧初稿。  
- FP / 空间 / 式(3)(4)(5)：等 A 补齐后合并。  
- Q3 字面 10：不阻塞 Day 5，正文用“常数轮 + 原文取 10”。  
- Q1 阶段下标：阻塞“已证不变式”表述，不阻塞伪代码控制流。

---

## B 当日产物

- [x] `notes/memberB/pseudocode.md`
- [x] `notes/memberB/proof-notes.md`（无漏报与时间）
- [x] `notes/proof-table.md`（B 列）
- [x] `discussions/review-day4.md`（B→A）
- [x] questions / AI 日志更新

## A 当日产物

- [x] `notes/memberA/probability-and-space-proof.md`
- [x] `notes/proof-table.md`（A 列）
- [x] `discussions/review-day4.md`（A→B 与回应 B→A）
- [x] `ai-usage/member-A-log.md`（Day 4 记录）
