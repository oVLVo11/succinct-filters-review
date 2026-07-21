# 证明笔记（Day 4：无漏报与时间框架）

- **负责人**：张书铖（B）
- **日期**：2026-07-22
- **配套**：`pseudocode.md`；共同表 `notes/proof-table.md`（B 列）；空间/FP 精算以 A 为准

> 区分：**论文命题** / **小组解释** / **未验证缺口**。

---

## 1. 依赖总图（保留）

（同 Day 1–3；详见 `figures/proof-dependency.md`。）

---

## 2. 无 false negative（漏报）

### 2.1 精确命题（论文）

在未报告 failure 的条件下，对任意已成功插入的 key `x`，`Lookup(x)` 返回 YES。  
原文：§3.1 化归直觉；Claim 13“every query is answered correctly if no fail”；Thm 10 第 4 条（filter 语义）。

### 2.2 所需不变式

1. **写入不变式**：第 `n` 次成功插入时，要么写入 `s=Pref(h(x),ℓ_{i★(n)})` 到 `D_{i★}`，要么库中已有更短前缀覆盖 `s`。
2. **迁移不丢串**：`decrement` 取出的串立即 `insert` 到 `T_i` 或 `D_i`（Claim 13 步骤 1–2）。
3. **查询覆盖（意图）**：`Lookup` 用 `i=i★(n)` 检查的 `D_{i-1},D_i,T_{i-1},T_i` 覆盖所有仍可能存有该前缀的层。

### 2.3 三种状态论证（小组解释）

| 状态 | 为何不漏报 |
|---|---|
| **插入前**（对已在库中的旧 key） | 旧前缀已在某层；迁移只搬不删“无接收方”的串 |
| **迁移中** | 串要么仍在旧层（尚未 decrement），要么已在新层；四结构同时包含旧层与新层 |
| **迁移后** | 旧层销毁前必须 Empty；串已在新层；查询转向新的 `i★` 时仍覆盖 |

对**刚插入**的 `x`：`s` 在 `D_i`（或被更短前缀覆盖）。`h(x)` 以 `s` 为前缀 ⇒ `D.query(D_i,h(x))` 或更短 `T` 命中 ⇒ YES。

### 2.4 缺口

- 存储覆盖与 `i★`/`epoch` 半开区间句的形式统一未关闭（issue-stage-index）。  
- 在缺口关闭前：控制流层无 FN **已核实**；完整归纳标 **Q1**。

---

## 3. 查询 worst-case O(1)

### 3.1 命题

无 failure 时，每次 `Lookup` 最坏常数时间。  
原文：Claim 13 末；Thm 10 第 2 条。

### 3.2 步骤

1. 计算 `h(x)`：Thm 7 下 O(1)。
2. 至多 4 次底层 `query`（两个 `D`、两个 `T`）。
3. 黑盒/`T` 单次 query 为 O(1)（Claim 13 假设 / 真值表随机访问）。

**合计 O(1)**。不随 `n` 增加结构个数。

### 3.3 条件

`¬failed`；底层接口 O(1)。

---

## 4. 插入 worst-case O(1) 与常数轮维护

### 4.1 命题

无 failure 时，每次 `Insert` 最坏常数时间。  
原文：Claim 13；Thm 10；§1.4 去均摊叙述。

### 4.2 单次 Insert 工作量分解

```text
AlreadyHasPrefix 检查     O(1)   （抽象为常数次查询）
D.insert                  O(1)
MigrateOneStep × 10       O(1)   （每轮常数次底层调用）
```

§5 内部：data block 重组同样拆成每次插入推进常数步（论文叙述）；上层证明依赖“底层已保证单次 O(1)”。

### 4.3 “为何常数轮足够”（两层）

| 层次 | 结论 | 状态 |
|---|---|---|
| 渐近 | 阶段长 `Θ(2^i)`，init/destroy/decrement 总需求 `O(2^i)`，故存在常数 `c` 使每插 `c` 轮足够 | **Q1**（机制清楚） |
| 字面 10 | 原文采用 10；黑盒只给 `O(m)`，不能推出“10 必然够” | **Q3**（issue-constant-10） |

### 4.4 destroy / initialize / decrement 同时推进

单轮 `MigrateOneStep` 按固定优先级：先尝试迁 `T`/`D`，再 destroy，再 initialize 下一层。  
一轮可能只推进一类工作；经多轮插入交错完成。  
**小组解释**：非“一轮做完一切”，而是“流水线”。

---

## 5. 底层 dictionary 保证如何上传到 filter

```text
§5 实现 D(m,ℓ)
  → 接口：insert/query/decrement/init/destroy 各 O(1)，空间与 failure 界
Claim 13 假设该接口
  → 拼装未知规模 prefix matching（Lemma 11）
§3.1 加 h 与 ℓ_i
  → Theorem 10 filter
```

因此：上层时间证明**不重新分析**桶内编码，只引用黑盒；黑盒 failure 并合到 δ（式 (3)(4)(5) 由 A 主核，B 负责指出事件落在哪些结构）。

---

## 6. Failure 对公开 API 的影响

| 项目 | 含义 |
|---|---|
| 触发 | `D.insert` 等报告失败 ⇒ `failed←true`（Claim 13 / Thm 10） |
| 概率 | 任意插入序列上，曾 failure 的概率 ≤ δ（对预计算随机比特） |
| 与 FP 区别 | FP 是无 failure 时对非成员的错误 YES；failure 是结构放弃保证 |
| Rebuild | 非主定理接口；见 `pseudocode.md` §7 |

---

## 7. 误报率 / 空间（交叉对齐，不替代 A）

- FP：式 (2) + 并合；B 确认求和指标是**阶段下标**与每阶段至多 `2^i` 个键的前缀碰撞。  
- 空间：Lemma 11 代入 `ℓ_{⌈log n⌉}`；B 确认并存层数常数、不引入 `log n` 个全量结构。  
详细求和与渐近吸收见 A 的 Day 4 概率/空间笔记（若尚未提交则表中标待 A）。

---

## 8. PSW `gamma` 独立复算（回应 A Day 3 安排）

依据仓库 `1304.1188v2.pdf` 与 A `lower-bound-notes.md` §14：

1. Theorem 3.1 含参数 `gamma≥2` 与块大小 `gamma^i`。  
2. 为使 `1-1/gamma → 1` 且 `log log_gamma(1/α)` 接近 `log log n`，需令 `gamma` **随 n 缓慢增长**（A 记 `gamma = 2^{(log n)^η}`，`0<η<1`）。  
3. **B 复算结论**：该选择使  
   `log log_gamma(1/α) = (1-η)log log n - O(1)`，  
   再令 `η→0`（缓慢）可得 `log log n - o(log log n)`，与文中 `(1-O(ε))log log n` 叙述兼容。  
4. **状态**：机制复算 **Q0（与 A 一致）**；写入 Liu–Yin–Yu Review 时的措辞仍由 A/C 统一，避免过度声称对所有固定 ε 最优。

---

## 9. Day 4 缺口汇总

| ID | 内容 | 阻塞 Day 5？ |
|---|---|---|
| issue-stage-index | 存储归纳下标 | 是（若正文写“已证不变式”） |
| issue-constant-10 | 字面 10 | 否（可写抽象常数轮 + 原文取 10） |
| data-block 冗余 | §5 逐项 | 部分（空间低阶项） |
| 式 (3)(4)(5) 并合 | A 主核 | 高概率行 |

---

## 10. 旧表（历史）

Day 1–3 的简表保留于 git 历史；正式六行见 `notes/proof-table.md`。
