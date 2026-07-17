# 刘威 Day 1 下界与参数疑问

日期：2026-07-17

本文件只记录 Day 1 初读时对下界和参数的理解与疑问，不作为最终证明。

## 1. 已确认的原文线索

摘要和引言中提到：

- 已知容量 `N` 的 approximate membership filter 下界为 `N log(1/epsilon)` bits。
- 若希望空间随当前集合大小 `n` 变化，Pagh、Segev、Wieder 给出信息论下界：

```text
(1 - o(1)) n (log(1/epsilon) + (1 - O(epsilon)) log log n)
```

- 这说明未知规模场景中，除了误报率成本 `log(1/epsilon)` 外，每个 key 还需要额外约 `log log n` bits。
- 本文目标之一是达到：

```text
(1 + o(1)) n (log(1/epsilon) + log log n)
```

从而把 `log log n` 项的领先常数 pin down 到 1。

## 2. 初步直觉

如果初始化时知道最终容量 `N`，结构可以直接按照最终规模规划 hash 范围和误报率预算。若不知道最终规模，只能随着插入逐步扩容。

对 filter 来说，扩容带来两个额外困难：

1. 旧 filter 通常不能恢复原始 key，不能像 exact dictionary 那样完整迁移；
2. 保留多个阶段结构时，一个非成员查询可能在任一阶段误报，因此总误报率要对多个阶段做 union bound。

因此，未知规模并不是工程上的“数组变大”问题，而是信息论层面的“当前阶段信息和未来增长信息如何编码”的问题。

## 3. 需要继续核查的具体问题

### Q1. `log log n` 下界到底来自哪里？

目前只知道它和 unknown size 有关，但还没有读下界证明。需要查 Pagh、Segev、Wieder [28] 的证明，或者原论文是否复述了关键思想。

待核查内容：

- 是否通过构造多个可能的当前规模来证明结构必须区分阶段；
- 是否和误报集合在不同阶段的累积有关；
- 下界是否对所有 insertion/query 时间都成立。

### Q2. `(1 - O(epsilon)) log log n` 中的 `(1 - O(epsilon))` 如何理解？

当 `epsilon = o(1)` 时，该系数趋近 1。本文摘要说 achieves optimal leading constant for all `epsilon = o(1)`。

待核查：

- 若 `epsilon` 是常数，该项领先常数是否仍是 1；
- 本文 Theorem 1 的正式条件是否限制 `epsilon`。

### Q3. 为什么需要 `n > u^0.001`？

摘要和 Theorem 1 informal 都出现此条件。可能用于：

- 保证某些低阶项是 `o(n log log n)`；
- 保证哈希、bucket、data block 的高概率事件成立；
- 避免极小 `n` 时空间主项不支配辅助结构。

需要查正式定理和参数设置。

### Q4. `O(log log log u)` 在 dictionary 结果中是否影响 filter？

Theorem 2 的 dictionary 空间有 `O(log log log u)`。Our Techniques 中说新的 membership structure 对 filter 只引入约 `log log log n` 级别低阶冗余，从而不破坏 `log log n` 的领先常数。

待核查：

- filter 中 `u`、`n`、`epsilon` 与 hash 字符串长度 `ell` 的关系；
- `log log log u` 如何变成低阶项；
- 是否依赖 `n > u^0.001`。

### Q5. 高概率最坏情况常数时间如何与空间下界并存？

已有工作能达到 succinct space 但 insertion 只是 expected amortized constant，或者能 worst-case constant 但空间多一个常数因子。本文声称同时达到二者。

待核查：

- 去均摊化迁移过程中是否需要额外保存旧结构和新结构；
- “几乎原地”的迁移如何不导致空间峰值超过目标界；
- 查询中间态如何保持常数时间。

## 4. 后续阅读计划

- Day 2：精读正式模型、Theorem 1/2 的完整表述、参数范围。
- Day 3：整理所有与空间界相关的引理。
- Day 4：与组员合作完成证明表，标记每一步使用的概率界、并合界和低阶项估计。
