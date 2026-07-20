# Day 2 会议记录

日期：2026-07-20  
状态：B（张书铖）先写入本人讲解要点与交叉审阅；A/C 讲解与共同结论待会后补全。

---

## B 口头讲解要点（不照抄笔记）

1. 全局 `h` 把 key 变成长比特串；第 n 次插入只存前 `ℓ_i` 位，`i=⌈log n⌉`。
2. `ℓ_i = i + log(1/ε) + log i + log log log u + 2`：`log(1/ε)` 管误报，`i/log i` 管多阶段并合，其余为冗余/松弛。
3. Lookup = 问“已存串是否为 `h(y)` 的前缀”；实现上只查四个结构。
4. 8 元素例子：新键进 `D_i`；每次插入重复 10 次维护，慢慢搬 `T_{i-1}/D_{i-1}`；教学用示意前缀，非真实哈希。
5. 相对 PSW：把短串真值表 + 可 in-place 迁移的 membership + 去均摊，用来同时钉死 `log log n` 前导常数与 whp 最坏 `O(1)`。

---

## 交叉审阅

### B 审 A：`notes/memberA/definitions.md`

| # | 位置 | 问题 | 建议 | 作者回应 |
|---|---|---|---|---|
| 1 | §1.2 当前集合 `n` | “第 n 次插入”与去重后 `|S|` 可能混淆 | 主定理陈述改用 insertion sequence；若假设无重复插入，写明假设 | 待 A |
| 2 | 概率/时间保证（请对照 Thm 10 与引言脚注） | 需写清：failure 是整段序列概率 ≤ `δ`；whp worst-case O(1) ≠ PSW 的 expected amortized O(1) | 单独小节对比两种时间语义 | 待 A |

### C 审 B（待 C）

待审文件：`notes/memberB/construction-notes.md` §6、`figures/growth-process.md`。  
关注：未读论文者能否跟随；是否把教学示意当成真实算法。

### A 审 C（待 A）

待审文件：`references/literature-matrix.md`。

---

## 共同讨论题（会后填写：已核实 / 小组解释 / 仍待验证）

1. `log(1/ε)` 为何是误报率成本  
2. `log log n` 与未知规模、阶段误报预算  
3. `(1+o(1))` 修饰哪个表达式、参数范围  
4. whp worst-case O(1) vs expected amortized O(1)  
5. 8 元素示例是否忠实 Claim 13（B 自检：骨架忠实；不变式下标对齐仍标 Q1）  
6. 文献矩阵中哪些真正 unknown size  
7. 今日关闭的 Q1 / 新增 Q2  
8. 三人互述核心结论  

---

## B 自检：8 元素示例 vs Claim 13

| 点 | 判断 |
|---|---|
| `i=⌈log n⌉`、新键进 `D_i`、10 次维护、四结构查询 | 与原文一致 |
| 短/长串迁移去向 | 与原文一致 |
| `n∈[2^i,2^{i+1})` 不变式下标与 `⌈log n⌉` 的逐点对齐 | 仍待验证（questions Q1.5） |
| 示意比特串 | 仅教学，非算法输出 |
