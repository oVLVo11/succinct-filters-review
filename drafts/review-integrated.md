# Succinct Filters for Sets of Unknown Sizes：论文 Review（整合稿 v0.1）

- **状态**：Day 6 第一版整合；**非终稿**
- **整合说明**：技术直觉 / 实现 / 正确性与时间证明由张书铖（B）定稿并入；问题定义、主结果、下界、相关研究、评价等章在 A/C 的 Day 5 章节定稿前，仅保留**可追溯的笔记级桥接**，并标【待 A】【待 C】。未关闭 Q1/Q3 在正文中显式保留。
- **贯穿教学示例**：连续插入 8 个抽象元素 `x1…x8`（§6.5）；不承担一般证明。
- **图示**：`figures/architecture.md`、`figures/query-insert-flow.md`、`figures/growth-process.md`、`figures/proof-dependency.md`

---

## 1. 摘要

【待 A 定稿】桥接要点：在集合最终规模未知时，维护动态 approximate membership（filter）与 dictionary；filter 空间在适当条件下达 `(1+o(1))n(log(1/ε)+log log n)` 位，插入与查询在无 failure 时为 worst-case `O(1)`（整段序列 failure 概率 ≤ `δ`）。本 Review 解释问题为何难、相对 PSW 的改进、构造与证明如何核查，并标明小组未关闭缺口。

---

## 2. 引言

【待 A 定稿】桥接要点：membership 应用广泛；dictionary 精确、filter 允许误报但不允许漏报；传统结构常按容量上界 `N` 占空间；当 `n≪N` 或 `N` 不可靠时浪费严重。核心问题：空间能否始终依赖当前规模，同时保持误报、无漏报与最坏情况常数时间？

下文先给出问题与结果（A），再述相关工作（C），然后展开构造与证明（B），最后评价与后续（C）。

---

## 3. 问题定义和研究意义

【待 A 整合 `definitions.md` / Day 5 问题章】

**全局符号（全文统一；`log` 以 2 为底）**

| 符号 | 含义 |
|---|---|
| `[u]` | 全集 `{0,…,u−1}` |
| `n` | 插入次数（insertion-sequence）；与去重后 `|S|` 的差别见 A |
| `ε` | 误报率（false positive rate） |
| `δ=u^{−C}` | 曾报告 failure 的概率上界 |
| `N` | 传统预置容量上界（本文希望摆脱对紧 `N` 的依赖） |

**口径**：正确性与时间保证均 **conditioned on no failure**；`ε` 与 `δ` 不可混用。

---

## 4. 相关研究

【待 C 整合】读者测试意见见 `discussions/review-day6.md`（B 测相关工作笔记）。分层提醒：Bloom / scalable·dynamic Bloom / succinct dictionary / quotient·cuckoo / PSW / 2020 后工作不可排成单一“更优”序列。

---

## 5. 论文主要结果

【待 A 定稿】与构造对照时采用：

- **正式 Theorem 10**：`n=ω(log u)`、`n<u`；主体空间 `n(log(1/ε)+log log n+O(log log log u))` + 输入无关 `u^c`；无 failure 时 FP≤`ε`、操作 O(1)；failure≤`δ`。
- **非正式 Theorem 1**：`n>u^{0.001}` 等条件下写成 `(1+o(1))…`；**不得**把该条件写成 Thm 10 的唯一前提。
- **相对 PSW**：在 `ε=o(1)` 等条件下钉死 `log log n` 领先常数，并给出 whp 最坏 O(1) 而非期望均摊插入（评价措辞见 C；最优性依赖 PSW 下界）。

---

## 6. 核心技术直觉

### 6.1 总路线

在最终规模未知时，构造目标是：空间跟随当前 `n`，无漏报，误报 ≤ `ε`，且在无 failure 时插入/查询为 worst-case `O(1)`。

总路线：

1. 全局哈希 `h` 把 key 映成长比特串，**不保存**原始 key。
2. 第 `n` 次插入只写入 `h(x)` 的前 `ℓ_{i★(n)}` 位，其中 `i★(n)=⌈log n⌉`。
3. 查询化为 prefix matching：是否存在已存串 `s` 为 `h(y)` 的前缀。
4. 短前缀用真值表 `T`，长前缀用已知容量结构 `D(m,ℓ)`；未知规模由「两代 `D/T` 并存 + 后台迁移」拼装（Claim 13 → Lemma 11 → Theorem 10）。

相对 PSW：真值表处理短串；去均摊、可查询的迁移；更紧底层冗余以支撑 `log log n` 项领先常数（条件见 A）。

体系结构见 `figures/architecture.md`。

### 6.2 变长前缀与误报预算

**论文命题**（§3.1 式 (2)）：

```text
ℓ_i = i + log(1/ε) + log i + log log log u + 2
```

| 项 | 作用 |
|---|---|
| `i` | 随阶段增长加长前缀 |
| `log(1/ε)` | 主误报成本 |
| `log i` | 跨阶段并合预算 |
| `log log log u`、`+2` | 冗余与并合余量 |

非成员误报经阶段内前缀数与 `2^{−ℓ_i}` 的 union bound 受控（**精算见 A**）。迁移只改存放位置，**不改变**该前缀写入时所按的 `ℓ_i` 预算。

### 6.3 四个活跃结构

操作参数 `i=i★(n)`：

| 结构 | 职责 |
|---|---|
| `D_i` | 当前长前缀主写入 |
| `D_{i−1}` | 旧长前缀；迁移源；仍可查 |
| `T_i` | 短串；接收迁移 |
| `T_{i−1}` | 更短层；迁出时扩展为 `y∘0,y∘1` |

「已初始化」的下一层可能存在，但 **Lookup 不查询它们**。

**开放缺口（Q1/Q3）**：Claim 13 证明段半开区间句与 `i★` 下标冲突未形式关闭；正文操作一律跟算法句 `i★`。见 `discussions/issues/issue-stage-index.md`。

**小边界**：`n=1` 时无 `D_{−1}/T_{−1}`；式 (2) 并合自 `i≥1`，`ℓ_0` 特判待与 A 统一。

### 6.4 为何不是“可扩容 Bloom”

工程 scalable/dynamic Bloom 可增长，但通常查询多个组件、空间/时间保证与本文 word-RAM 定理不同（C）。本文要同时：空间相对当前 `n` 的 succinct 主项、只查常数结构、whp 最坏 O(1)。

### 6.5 贯穿教学示例（唯一）

连续插入 `x1…x8`（人为示意前缀，**非**真实哈希，**不**证明概率/空间）：

| n | `i★` | 新键进入 | 查询活跃 | 维护推进 |
|---|---|---|---|---|
| 1 | 0 | `D0` | `D0,T0` | — |
| 2 | 1 | `D1` | `D0,D1,T0,T1` | 迁 `T0/D0`；init `T2/D2` |
| 3–4 | 2 | `D2` | `D1,D2,T1,T2` | 迁 `T1/D1`；init `T3/D3` |
| 5–8 | 3 | `D3` | `D2,D3,T2,T3` | 迁 `T2/D2`；init `T4/D4` |

同步图：`figures/growth-process.md`。

---

## 7. 数据结构详细实现

### 7.1 算法说明（抽象；非工程代码）

状态：`n`，`h`，`failed`，各层 `T[j],D[j]`，init/destroy 进度。  
`i★(n)=⌈log n⌉`，`ℓ_i` 如式 (2)，`Pref(z,L)` 为前 `L` 比特。

**Lookup(y)**（`¬failed`，`n≥1`）：`i←i★(n)`，`z←h(y)`；若 `D_{i−1}`/`D_i`/`T_{i−1}`/`T_i` 任一对相应前缀查询命中则 YES，否则 NO。至多四次底层 query。

**Insert(x)**：`n←n+1`，`i←i★(n)`，`s←Pref(h(x),ℓ_i)`；若无更短前缀覆盖则 `D.insert(D_i,s)`（失败则 `failed←true`）；再执行 **10** 次维护步（原文）。

**一轮维护（MigrateOneStep(i)）**，对应 Claim 13：

1. 若 `T_{i−1}` 非空：`decrement` 得 `y`，则写入 `T_i` 的 `y∘0` 与 `y∘1`；  
2. 若 `D_{i−1}` 非空：`decrement` 得 `y`，则 `|y|>i` 进 `D_i`，否则进 `T_i`；  
3. 旧层已空则推进 `destroy`；  
4. 旧层已销毁则推进 `initialize(T_{i+1}), initialize(D_{i+1})`。

完整状态机见 `notes/memberB/pseudocode.md`。  
**字面常数 10**：原文每次执行 10 轮；**小组未从黑盒 `O(m)` 隐藏常数独立复算其充分性**（Q3）。渐近上存在足够大的常数轮数。  
**写入层就绪**：单次 Insert **不得** while 到初始化完成；依赖阶段就绪不变式 + 每插常数轮推进。

### 7.2 底层 `D(m,ℓ)`

黑盒：`initialize`/`destroy`（各 O(m) 次调用完成）、`insert`、`query`（是否存在前缀）、`decrement`。空间约 `q(ℓ−log m+2 log log log u)+O(m)`。写入 `D_i` 的串来自 core set，以匹配随机性假设。

§5 内部：main table → subtable → adaptive prefixes / navigator → data blocks（动态插入 + 后台重组静态）。位级冗余与式 (3)(4)(5) 精算以 A 为准；未闭合细节为 Q2/Q3。

操作流图：`figures/query-insert-flow.md`。

---

## 8. 正确性证明

对应 `notes/proof-table.md`。

### 8.1 无 false negative

**命题**：无 failure 时，已插入 key 的 Lookup 为 YES。  
**论证（控制流，已核实）**：写入前缀或被更短前缀覆盖；迁移边取边写、不丢串；Lookup 同时查旧层与新层。  
**缺口**：对所有 `n` 的形式存储归纳受阶段下标冲突阻塞（issue-stage-index）——**不写成已完全证明**。

### 8.2 误报率 ≤ `ε`

**命题**：无 failure 时，非成员误报概率 ≤ `ε`。  
**骨架**：式 (2) + 阶段/键 union bound（**A 精算**）；迁移不重复计费。依赖图：`figures/proof-dependency.md`。

### 8.3 Prefix matching 与四结构覆盖

短串 `T`、长串 `D`；查询固定四个活跃结构，避免扫 `Θ(log n)` 层历史 filter。

---

## 9. 时间和空间复杂度证明

### 9.1 时间（B）

| 操作 | 论证 | 条件 |
|---|---|---|
| Lookup | ≤4 次底层 query + `h` 求值 | `¬failed`；底层 O(1) |
| Insert | 1×`D.insert` + 10×维护轮；每轮常数次底层调用 | 同上；字面 10 为原文/Q3 |

§5 块重组同样去均摊到每次插入的常数步。

### 9.2 空间（A 主核；B 结构约束）

Lemma 11 代入 `ℓ_{⌈log n⌉}` 得主体 `n(log(1/ε)+log log n+O(log log log u))+u^c`。  
B 确认：同时仅常数层 `D/T` 全量活跃，不保留 `log n` 个独立全量 filter。位级迁移峰值仍为 Q3。

### 9.3 Failure ≤ `δ`（A）

每层 `D_i` 经式 (3)(4)(5) 等到 `u^{−2C}`，对 ≤`log u` 层并合到 `u^{−C}`。B 抽查骨架同意；自适应对手不作无条件扩张。

---

## 10. 技术优越性

【待 C；证据 S1–S4 见 `evaluation-evidence.md`】组合保证：unknown-size 空间主项 + 无 FN + FP≤`ε` + whp 最坏 O(1)。相对 PSW：领先常数与时间语义。非“全面优于 Bloom”。

---

## 11. 局限性与适用范围

【待 C】至少须保留：无用户删除；保证 conditioned on no failure；`u^c` 与 `n=ω(log u)`；实现远复杂于工程 Bloom；字面 10 与阶段下标为小组核查缺口（L4）；删除模型有不同下界，不能反推本文错误。

---

## 12. 后续研究

【待 C】区分 insertion-only unknown-size、fully dynamic（含删除）、resizable-current-`n`；E1/E2 不得作确定结论；2026 预印本标明状态。

---

## 13. 小组评价

【三人共同 · 待会后补】事实：论文在所述模型下给出同时达成空间主项与 whp 最坏常数时间的构造。观点：讲解主线宜强调四结构 + 去均摊迁移；Review 必须公开 Q1/Q3。

---

## 14. 结论

本文不是简单的“可扩容 Bloom”，而是 unknown-size 设定下，用哈希前缀、prefix matching、短串真值表、长串 succinct 结构与分阶段去均摊迁移，逼近信息论额外 `log log n` 成本并追求最坏情况常数时间。读者应同时看到定理条件、与 PSW/工程方案的模型差异，以及本文整合稿中仍开放的下标与常数配平缺口。

---

## 15. 参考文献

【待 C 统一 BibTeX】正文已用关键文献：Liu–Yin–Yu ICALP 2020 / arXiv:2004.12465；Pagh–Segev–Wieder FOCS 2013（仓库 `1304.1188v2.pdf`）。引用审计见 `references/citation-audit.md`（C 主责；B 抽查技术章引用）。

---

## 附录 A. 开放问题（带入 Day 7）

| ID | 内容 | 正文处理 |
|---|---|---|
| issue-stage-index | `i★` vs 半开区间存储归纳 | 操作跟 `i★`；不声称归纳已证 |
| issue-constant-10 | 字面常数 10 | 写原文 10 轮 + 未独立复算 |
| Q2 data-block | §5 位级冗余 | 综述级；精算归 A |
| Q3 空间峰值 | 迁移瞬时位级 | 量级 O(n) 层；位级开放 |
| A/C 章节 | Day 5 定稿未入库 | 桥接段待替换 |

## 附录 B. 整合贡献（过程）

| 部分 | 主整合 |
|---|---|
| §6–§9（技术/实现/正确性/时间）及贯穿示例、图同步 | B |
| §1–§3、§5、§9 空间/failure 精算 | A（待替换桥接） |
| §4、§10–§12、§15 | C（待替换桥接） |
| §13–§14 | 共同 |
