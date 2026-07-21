# Day 3 会议记录

日期：2026-07-21  
状态：B 先写入本人讲解与交叉审阅摘要；A/C 讲解与共同裁决待补。

---

## B 讲解提纲（约 10 分钟：从 key 到 dictionary）

1. Key → 全局 `h` → 只存 `ℓ_i` 前缀（组件 1–2）。
2. Lookup = prefix matching；实现只查 `D/T` 四元组（组件 3,5）。
3. 用 `i★=⌈log n⌉` 控制插入与维护；与证明段 `epoch` 下标冲突已建 Issue，教学图跟算法句。
4. 每次插入 10 轮：迁旧、destroy、initialize 下一层；渐近够、字面 10 为 Q3。
5. 短串进 `T`，长串进 `D`；`D(m,ℓ)` 黑盒提供长串 prefix matching，§5 用 data block 做 succinct（组件 10）。

复述检查（会后填）：A/C 各复述一项 B 内容。

---

## 交叉审阅摘要

| 方向 | 文件 | 结果 |
|---|---|---|
| A→B | construction / figures | 4 条；B 全部接受并改笔记 |
| B→A | lemma-dependency / proof-dependency | 2 条实质 + 关闭 Q1.5；见 `review-day3-B.md` |
| C→B | core-components / 8 元素示例 | **待 C** |

---

## Issues

1. `discussions/issues/issue-constant-10.md`
2. `discussions/issues/issue-stage-index.md`

---

## 共同讨论题（会后填：已核实 / 小组解释 / 仍待验证）

1. Filter 为何化为变长 prefix matching  
2. 为何只查常数个活跃结构  
3. 常数后台工作与阶段长度配平（缺口：字面 10）  
4. Q2/Q4 处理  
5. 互述非本人负责内容  

---

## B 当日产物清单

- [x] `notes/memberB/core-components.md`
- [x] 修订 `construction-notes.md`、`query-insert-flow.md`
- [x] `figures/architecture.md`；补注 `proof-dependency.md`
- [x] 两个 Issue；更新 questions / AI 日志 / 本会议 B 部分
