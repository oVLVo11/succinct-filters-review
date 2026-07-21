# 证明依赖与主定理草图

- **目的**：标记主定理依赖哪些 lemma / invariant / 概率论证
- **对应**：Thm 10（Filter）、Lemma 11、Claim 13、§5 失败概率；Dictionary Thm 12 仅列依赖入口


---

## 1. 主定理依赖图

```text
Thm 10 (Dynamic Filter, formal)
 ├── 化归：AMQ + 全局哈希 h + 前缀长度 ℓ_i
 │     ├── 正确性直觉：存的是 h(x) 前缀 ⇒ 无 FN
 │     └── FP：并合界 ∑_i 2^i · 2^{-ℓ_i} ≤ ε   （式 (2) 的选择）
 ├── Lemma 11 (Prefix Matching 上界)
 │     ├── Claim 13：若存在已知容量 D(m, ℓ) 接口，则 Lemma 11 成立
 │     │     ├── 不变式：第 n 次插入后，数据在 {D_{i-1}, T_{i-1}, D_i, T_i}
 │     │     ├── 迁移进度：每次插入常数步 decrement/initialize/destroy
 │     │     ├── 短串：truth table T_i
 │     │     └── 失败并合：每个 D_i 失败 ≤ u^{-2C}，对 i 并合 ≤ δ
 │     └── §5：实现 D(m, ℓ)
 │           ├── Thm 7：k-wise hash 的存在/求值
 │           ├── Thm 8：有限独立 Chernoff ⇒ 主表负载
 │           ├── Thm 9：adaptive prefixes 表示与 O(1) 操作
 │           ├── Data block 静态空间：≈ ℓ − log m + O(log log log u)/键
 │           ├── 去均摊重组：O(log u / log log u) 工作拆成每次 O(1)
 │           └── 失败事件并合：式 (5) → ≤ u^{-2C}
 ├── Thm 7 额外：存 h 的 u^c 预计算比特（与输入无关）
 └── 空间代数：n(ℓ_{⌈log n⌉} − log n + O(log log log u))
               = n(log(1/ε) + log log n + O(log log log u))

Thm 12 (Dictionary)
 └── §6：在 prefix-matching/membership 骨架上加 Feistel 等
       └── 负载均衡不差于随机情形的概率比较（文中式 (6) 一类论证）
```

---

## 2. 结论 → 依赖表（Day 4 会扩成完整证明表）

| 结论 | 要证明什么 | 主要依赖 | 原文 |
|---|---|---|---|
| 无 false negative | 已插入键查询必 YES | 插入存 `h(x)` 前缀；查询做前缀匹配 | §3.1 |
| FP ≤ `ε` | 非成员误报概率 | `ℓ_i` 设定 + pairwise/并合 | §3.1 |
| 空间界 | 位数公式 | Lemma 11 空间 + `ℓ_i` 代入 | §3.1 末 |
| 查询 `O(1)` | 只查常数个结构 | Claim 13：查 `D_{i-1}, D_i, T_{i-1}, T_i` | Claim 13 |
| 插入 `O(1)` 最坏 | 含迁移也不超时 | 每次常数次维护 + 块重组去均摊 | §1.4, §5 |
| 高概率不失败 | 失败总概率 ≤ `δ` | 桶负载、fingerprint、hd/hs 碰撞等并合 | §5 式 (3)(4)(5) |
| Dictionary 正确 | 最坏输入仍对 | Feistel / 有限独立置换替代 | §6 |

---

## 3. 关键不变式 / 概率论证清单

### 3.1 不变式（确定性，失败除外）

1. **存储不变式**：任一已接受的插入串，要么在某个 `T_*`，要么在某个 `D_*`。
2. **阶段不变式**：`n ∈ [2^i, 2^{i+1})` 时，活跃结构主要是 `D_{i-1}, T_{i-1}, D_i, T_i`；阶段结束时旧结构销毁、新结构初始化完毕。
3. **前缀自由 / core set**：迁入 `D_i` 的串来自 core set `B_{(i, ℓ_i]}`（无互相为前缀的冗余），以便随机性假设成立。
4. **块状态不变式**：每桶至多两个动态块（在建 + 在重组）；重组在下一块填满前完成。

### 3.2 概率论证

1. **误报并合**：对非成员 `y`，`Pr[∃i 匹配] ≤ ∑_i 2^i · 2^{-ℓ_i}`。
2. **主表负载**：`k`-wise + Chernoff（Thm 8）⇒ 每桶 `O(log u)` whp。
3. **Adaptive prefixes 可表示**：Thm 9，随机串假设下 `O(log u)` 比特/桶 whp。
4. **hd∘hs 碰撞**：组合界式 (4)。
5. **总失败概率**：式 (5) 并合到 `u^{-2C}`，再对阶段并合到 `δ`。

### 3.3 Day 3 状态

| 项 | 状态 | 指针 |
|---|---|---|
| 字面常数 10 配平 | Q3 | `discussions/issues/issue-constant-10.md` |
| `i★` vs 半开区间存储归纳 | Q3/Q1 | `discussions/issues/issue-stage-index.md`；`core-components.md` 组件 4 |
| `D(m,ℓ)` 黑盒接口 | 已核实 | `core-components.md` 组件 10 |
| Data block 冗余逐项 | Q2 | Day 4 |
| Feistel dictionary | 未展开 | §6 / Day 4+ |

### 3.4 已核对（构造层）

- 式 (2)、新键进 `D_i`、四结构查询、短/长串迁移、每次维护 10 次（字面）：Claim 13 / §3.1。
- 十组件拆解：`core-components.md`。
- 依赖图补注：`figures/proof-dependency.md`。

---