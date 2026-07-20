# 查询 / 插入流程（与 8 元素示例一致）

> 来源：§3.1、Claim 13。  
> 与 `notes/memberB/construction-notes.md` §6、`figures/growth-process.md` 同步。

---

## A. Lookup(y)

```text
输入 y ∈ [u]
   │
   ▼
h(y) ← 全局哈希
   │
   ▼
i ← ⌈log n⌉
   │
   ├─► query(D_{i-1}, h(y))
   ├─► query(D_i,     h(y))
   ├─► query(T_{i-1}, h(y) 的前 i-1 位)
   └─► query(T_i,     h(y) 的前 i 位)
   │
   ▼
任一 YES → YES；全 NO → NO
```

8 元素对照：

| 当前 n | i | 实际检查 |
|---|---|---|
| 1 | 0 | `D0, T0` |
| 2 | 1 | `D0,D1,T0,T1` |
| 3–4 | 2 | `D1,D2,T1,T2` |
| 5–8 | 3 | `D2,D3,T2,T3` |

失败未发生时：无 FN；FP ≤ `ε`；时间 `O(1)`。

---

## B. Insert（第 n 个元素）

```text
i ← ⌈log n⌉
s ← h(x) 的前 ℓ_i 位
若尚无 s 的前缀在库中:
      insert(D_i, s)          ← 新元素默认进 D_i（不是 T_i）

重复 10 次:                   ← Claim 13 原文 “for 10 times”
  (1) T_{i-1} 非空 → decrement；若得 y → insert(T_i, y∘0) 与 y∘1
  (2) D_{i-1} 非空 → decrement；若得 y →
        |y| > i → insert(D_i, y)
        否则     → insert(T_i, y)
  (3) 旧空未销毁 → destroy
  (4) 旧已销毁   → initialize(T_{i+1} / D_{i+1})
```

`initialize` / `destroy` 本身也需多次调用；进度摊在各次插入上。

---

## C. 底层 `D(m,ℓ)`（Day 3，此处仅接口）

```text
Insert/Query into D:
  按 st(x) 进 subtable → adaptive prefixes → data block
  （细节见 §5；本图不展开）
```
