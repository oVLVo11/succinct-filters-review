# 体系结构：Filter → D/T → 底层 dictionary

> Day 3 · 成员 B · 对应 `notes/memberB/core-components.md`

```text
                    Theorem 10  Dynamic Filter
                              │
              ┌───────────────┼───────────────┐
              │ 全局哈希 h    │  前缀长度 ℓ_i  │  FP 并合
              │ (组件1)       │  (组件2)       │  式(2)
              └───────────────┼───────────────┘
                              ▼
                    Lemma 11  Prefix Matching
                              │
                    Claim 13  未知规模拼装
           ┌──────────────────┼──────────────────┐
           │                  │                  │
      Truth table T_j    活跃四元组         已知容量 D_j
      (短串, |s|=j)     D_{i-1},D_i,       = D(m,ℓ)
                        T_{i-1},T_i        (长串 prefix matching)
           │                  │                  │
           │            (组件4–9)            (组件10 / §5)
           │                                     │
           │              main table ──► subtable
           │                                 ├─ adaptive prefixes
           │                                 ├─ navigators
           │                                 └─ data blocks
           │                                      (动态 + 后台重组静态)
```

## 层间一句话

1. **Filter 层**：只决定存多长的 `h(x)` 前缀、如何控制 ε。
2. **Claim 13 层**：用两代 `D/T` + 去均摊迁移，把未知规模变成“始终只碰常数个已知容量结构”。
3. **§5 层**：实现单个 `D(m,ℓ)`，把长串 prefix matching 做到 succinct + 最坏 O(1)（whp）。

## 与操作流的链接

| 结构图节点 | 组件小节 | 操作流节点 |
|---|---|---|
| 全局哈希 / ℓ_i | 组件 1–2 | Insert 取前缀；Lookup 算 h(y) |
| 四元组 D/T | 组件 5–7 | Lookup 四个 query；维护迁移 |
| 去均摊 | 组件 8–9 | Insert 后 10 轮维护 |
| D(m,ℓ) | 组件 10 | 底层 insert/query/decrement |
