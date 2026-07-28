# 体系结构：Filter → D/T → 底层 dictionary

> 与 `drafts/review-integrated.md` §6–§7 同步（Day 6）。  
> 小组绘制；对应原文 §3.1、Claim 13、§5。

```text
                    Theorem 10  Dynamic Filter
                              │
              ┌───────────────┼───────────────┐
              │ 全局哈希 h    │  前缀长度 ℓ_i  │  FP 并合
              └───────────────┼───────────────┘
                              ▼
                    Lemma 11  Prefix Matching
                              │
                    Claim 13  未知规模拼装
           ┌──────────────────┼──────────────────┐
           │                  │                  │
      Truth table T_j    查询活跃四元组      已知容量 D_j
      (短串)            D_{i-1},D_i,         = D(m,ℓ)
                        T_{i-1},T_i          (长串)
           │             i = i★(n)=⌈log n⌉      │
           │                                     │
           │              main table ──► subtable
           │                                 ├─ adaptive prefixes
           │                                 ├─ navigators
           │                                 └─ data blocks
```

**注意**：下一层可能已 initialize，但 Lookup **只**查四元组。  
贯穿示例 `n=1…8` 的活跃列见整合稿 §6.5 与 `growth-process.md`。
