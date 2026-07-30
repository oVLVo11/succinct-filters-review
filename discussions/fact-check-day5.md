# Day 5 事实核查与术语规范

日期：2026-07-28  
维护：三人共用；下表含 B 已登记项。

---

## 1. 术语统一表

| 术语 | 本章统一用法 | 勿写成 |
|---|---|---|
| filter | 允许误报、禁止漏报的近似成员结构 | “Bloom” 的同义词 |
| dictionary | 精确成员 / 键值结构 | 与 filter 混称 |
| approximate membership | 近似成员查询 | |
| unknown size | 无紧最终容量上界；空间跟当前 `n` | “不知道当前 n” |
| false positive | 非成员得 YES；概率 ≤`ε`（无 failure 时） | 与 failure 混用 |
| failure | 结构报告失败；序列级概率 ≤`δ` | “查询失败” |
| prefix matching | 判定是否存在已存前缀 | |
| truth table | 短串位图 `T_i` | |
| de-amortization | 去均摊；每操作推进常数步 | “摊还分析”单独代替最坏保证 |
| succinct | 接近信息论最小空间 + 低阶冗余 | 仅“比较省空间” |
| wasted bits | 相对信息论下界的多余比特 | |

---

## 2. 主张核查表（B 相关优先）

| 主张 | 章节位置 | 来源 | 核查人 | 状态 | 建议最终措辞 |
|---|---|---|---|---|---|
| 每次插入维护 10 次 | B §6 | Claim 13 | B | 属实 | “原文规定 10 次；字面配平未由小组证完（Q3）” |
| Lookup 只查四个结构 | B §5 | Claim 13 末 | B | 属实 | 保留；注明 `i=0` 边界 |
| 无 failure 时无 FN | B §7 | Thm 10.4；Claim 13 | B | 控制流属实；归纳 Q1 | “控制流论证 + 下标归纳未关闭” |
| worst-case O(1) 插入/查询 | B §5–6 | Thm 10.2 | B | 条件属实 | “conditioned on no failure；底层 O(1)” |
| 字面 10 已严格配平 | — | — | B | **禁止写入** | 不出现 |
| 阶段存储不变式已严格证明 | — | Claim 13 证明段 | B | **禁止无警告写入** | 标明核查项 |
| FP 并合 `<ε` | 依赖 A | 式 (2)；A 笔记 §2 | B 抽查 | 骨架同意 | 以 A 精算为准 |
| failure ≤`δ` | A 章、整合稿 §9.3 | Thm 10.3；式 (3)–(5) | A 展开，B 抽查 | **已修订** | 单层 `u^{-2C}`，再对 `O(log u)` 层并合到 `u^{-C}`；保留 `C>1`、`u` 足够大 |
| `(1+o(1))` 与 `n>u^{0.001}` | A 章 | Thm 1 vs 10 | 待与 A 对齐 | 待 | 不与 Thm 10 条件混淆 |
| 全面优于 Bloom | — | — | B | **禁止** | “在 unknown-size 理论目标下更强保证” |
| PSW 是直接前作，LYY 不是首次提出 unknown-size | C §6 / 整合稿 §4.3 | PSW 2013；LYY §1 | C | 已核 | “LYY 收紧领先项与时间语义” |
| `log log n` 领先常数最优 | A/C 比较段 | PSW Thm 3.1；LYY Thm 1/10 | C 二次核查 | 有条件成立 | 只在 `ε=o(1)` 等条件下说“领先项对齐” |
| Aleph 全部操作与 LYY 同口径 worst-case 常数 | C §8.1 | Aleph Abstract、§5.2、§7 | C | **禁止** | 总述与 amortized 清理分开 |
| 删除型 dynamic 下界否定 LYY | C §8.2 | Kuszmaul–Walzer Thm 3.1 | C | **禁止** | 删除改变模型的信息成本 |
| Resizable Retrieval 已正式发表 | C §8.3 | arXiv/DBLP CoRR | C | **禁止** | 截至 2026-07-28 只称“2026 预印本” |
| 后续工作全面取代 LYY | C §8 / 整合稿 §12 | 三篇 E3 后作 | C | **禁止** | 逐维说明扩大模型或改变保证 |

---

## 3. B 自检：高风险措辞

- [x] 未写“首次提出 unknown-size filter”（PSW 在先）
- [x] 未写“已证明常数 10”
- [x] 未把教学示例当证明
- [x] 区分 ε 与 δ
- [x] C 的读者断点已在 `review-day6.md` C1–C7 记录，A/B 已在章节与整合稿中响应
- [x] 已与 A 统一 `ℓ_0` / `i=0` 口径：有限初始规模单独处理，渐近求和从 `i≥1` 开始

---

## 4. C 自检：相关研究与评价

- [x] E1/E2 未承担确定性技术比较
- [x] 不把 insertion-only unknown-size、含删除 fully dynamic、current-`n` resizable 混称
- [x] expected / amortized / worst-case / whp / no-failure 条件逐项保留
- [x] Quotient/Cuckoo filter 标为“原文未引用的外补对照”
- [x] “优越性”拆为空间、时间、删除、扩展、实现与证明强度
- [x] 2026 工作只按预印本引用
- [x] A 已抽查 8 项核心正文—文献对应；小组最终决定不再为 B 的签字审阅形成文件

---

## 5. A 章强主张核查

| 主张 | 章节位置 | 来源 | 状态 | 最终措辞 |
|---|---|---|---|---|
| unknown size 未知的是最终规模/紧 `N` | A §1–§2；整合稿 §2–§3 | LYY §1、§1.3 | 已核 | 明确不是 `u` 或当前 `n` 未知 |
| Theorem 10 的正式 `n` 条件 | A §4.1；整合稿 §5.1 | LYY Thm 10 | 已核 | `n=ω(log u)` 且 `n<u` |
| Theorem 1 的 `n>u^{0.001}` | A §4.2；整合稿 §5.1 | LYY Thm 1 | 已核 | 只用于 `(1+o(1))` 展示，不写成 Thm 10 唯一条件 |
| FP≤`ε` | A §5；整合稿 §8.2 | LYY 式 (2) | 已核 | 按插入阶段 union bound；带 no-failure 口径 |
| failure≤`δ=u^{-C}` | A §7；整合稿 §9.3 | LYY Thm 10.3、式 (3)–(5)、Claim 13 | 已核 | 单层 `u^{-2C}` 再对 `O(log u)` 层并合 |
| PSW 下界不限制操作时间 | A §6.1 | PSW §3、Thm 3.1 | 已核 | 仅读状态做压缩论证 |
| PSW Thm 1.1 字面是 `Ω(n log log n)` | A §6.3；整合稿 §5.2 | PSW Thm 3.1 后参数代入 | 已核 | 精细系数来自参数化 Thm 3.1 |
| `log log n` 领先项对齐 | A §6.3、§8 | PSW Thm 3.1；LYY Thm 1/10 | 有条件成立 | 每次都在同句保留 `ε=o(1)` 等条件 |
| 全面优于 Bloom/filter 后作 | — | — | **禁止** | 只按空间、时间、删除、实现和概率口径分维比较 |
