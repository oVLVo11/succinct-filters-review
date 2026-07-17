# 查询 / 插入流程

> 来源：论文 §3.1、Claim 13。  

---

## A. Lookup(y) — Filter 层

```text
输入 y ∈ [u]
   │
   ▼
计算 h(y)          （全局哈希）
   │
   ▼
设 i ← ⌈log n⌉     （当前阶段）
   │
   ├─► query(D_{i-1}, h(y))
   ├─► query(D_i,     h(y))
   ├─► query(T_{i-1}, h(y) 的前 i-1 位)
   └─► query(T_i,     h(y) 的前 i 位)
   │
   ▼
任一返回 YES ⇒ 输出 YES
全部 NO     ⇒ 输出 NO
```

**性质（失败未发生时）**

- 真成员：其插入时前缀仍在某个 `T` 或 `D` 中 ⇒ 无 FN。
- 非成员：误报由各阶段前缀碰撞并合控制 ≤ `ε`。
- 时间：只碰常数个结构 ⇒ `O(1)`。

---

## B. Insert(x) — Filter / Prefix-matching 层

```text
输入 x（第 n 次插入），i ← ⌈log n⌉
   │
   ▼
取前缀 s ← h(x) 的前 ℓ_i 位
   │
   ▼
若还没有 s 的更短前缀已在库中:
      insert(D_i, s)     （若失败则报告 failure）
   │
   ▼
重复约 10 次 MaintainStep():     ← 去均摊关键
   │
   ├─ (1) 若 T_{i-1} 非空:
   │       y ← decrement(T_{i-1})
   │       若得到 y: insert(T_i, y∘0) 与 insert(T_i, y∘1)
   │
   ├─ (2) 若 D_{i-1} 非空:
   │       y ← decrement(D_{i-1})
   │       若得到 y:
   │          |y| > i  → insert(D_i, y)
   │          否则     → insert(T_i, y)
   │
   ├─ (3) 若旧结构已空但未销毁 → destroy(...)
   │
   └─ (4) 若旧结构已销毁 → initialize(T_{i+1}) / initialize(D_{i+1})
```


 `initialize` / `destroy` 本身也是“调用很多次才完成”，进度摊到各次插入。
 因此单次 Insert 的 wall-clock 步数为常数，同时推进迁移。

---

## C. 底层 `D(m, ℓ)` 内的 Insert/Query

```text
Insert into D:
  x → st(x) 选 subtable
    → 写入最新 dynamic data block
    → 更新 adaptive prefixes / indicators / buffers
    → 若块满：启动重组，后续每次插入推进常数步排序/写回静态块

Query in D:
  x → st(x) 选 subtable
    → adaptive prefixes 找到候选唯一前缀
    → navigator / indicator 定位 data block（静态或动态）
    → 在块内解码比对 rt 等字段
    → 返回是否存在前缀匹配
```

---
