# 刘威 Day 1 基本定义整理

日期：2026-07-17

本文件记录 Day 1 从原论文摘要、第 1 节和第 2 节中整理出的基础定义。后续需要补充正式页码、定理编号和更精确的符号约定。

## 1. 基本对象

| 术语 | Day 1 定义 | 原文位置 | 待核查 |
|---|---|---|---|
| Universe / key space | 全集 `[u] = {0, ..., u - 1}`，所有 key 都来自这里。 | 第 1 节脚注 1 | 后续统一中文译名：全集 / 键空间 |
| Set `S` | 当前维护的 key 集合，`S subseteq [u]`。 | 摘要 | 插入是否允许重复需要查正式模型 |
| Current size `n` | 当前集合大小，`n = |S|`。 | 摘要、第 1 节 | 与插入次数是否总一致需核查 |
| Capacity `N` | 初始化时给出的容量上界，传统结构按它预分配空间。 | 第 1 节 | 与 unknown size 问题对比使用 |
| Dictionary | 精确回答 membership query 的数据结构。 | 摘要 | 本文还讨论 key-value dictionary |
| Filter | 允许小概率 false positive 的 approximate membership 结构。 | 摘要、第 1 节 | 不允许 false negative |

## 2. 操作语义

### `insert(x)`

将 `x` 插入当前集合或数据库。

Day 1 需要注意：filter 虽然不保存完整元素，但逻辑上仍然维护一个已插入集合。证明无漏报时，要以这个逻辑集合为对象。

### `lookup(x)`

如果 `x` 属于集合，必须返回 YES；如果 `x` 不属于集合：

- dictionary 必须返回 NO；
- filter 可以以概率至多 `epsilon` 返回 YES。

## 3. 错误类型

| 错误类型 | 含义 | filter 是否允许 |
|---|---|---|
| False positive | `x notin S`，但结构回答 YES。 | 允许，但概率需受 `epsilon` 控制 |
| False negative | `x in S`，但结构回答 NO。 | 不允许 |

直觉：filter 的空间节省来自允许 false positive；如果允许 false negative，membership 问题会变成不同模型，本文不是这个方向。

## 4. Unknown sizes 的含义

本文中的 unknown sizes 不是说 `u` 未知，也不是说当前 `n` 无法知道，而是说最终集合大小或一个紧的容量上界 `N` 在初始化时不可用。结构需要随着当前 `n` 动态增长，并使空间依赖当前 `n`，而不是依赖保守估计的最大容量。

## 5. Succinct 的含义

论文脚注中说明：succinct data structure 使用“信息论最小空间 + 渐近更小的冗余项”。因此本文不是只要求 `O(...)` 级别空间，而是追求接近信息论最优，并关心 `log log n` 项的领先常数。

Day 1 暂定表述：

> 在本文语境下，succinct 意味着空间不只是渐近同阶，而是主项达到信息论下界，额外冗余相对主空间为低阶。

## 6. 传统已知容量 filter 的空间

当最多存储 `N` 个 key、误报率为 `epsilon` 时，经典下界约为：

N log(1/epsilon) bits
```

原文提到 Pagh、Pagh、Rao 的结构可达到 `(1 + o(1)) N log(1/epsilon)` bits。

需要后续核查：

- 下界文献对应 Carter et al. / Pagh et al. 的具体引用编号；
- log 默认底数为 2；
- `epsilon` 的取值范围对公式是否有额外限制。

## 7. 未知规模 filter 的额外成本

Pagh、Segev、Wieder 的下界显示，若空间要依赖当前 `n`，filter 需要约：

n (log(1/epsilon) + log log n) bits
```

更精确地，摘要中写作：

(1 - o(1)) n (log(1/epsilon) + (1 - O(epsilon)) log log n)
理解：

- `log(1/epsilon)` 是控制误报率的基本成本；
- `log log n` 是未知最终规模、阶段增长和误报预算分配带来的额外成本；
- 本文贡献之一是把该额外项的领先常数也做到最优。

## 8. 高概率最坏情况常数时间

 暂定理解：

> 不是“每次操作期望常数时间”，而是除一个很小失败概率外，一段多项式长度操作序列中的每次插入和查询都在最坏情况常数时间内完成。

待核查：

- 正式失败概率是 `1/poly n` 还是相对于 `u` 或操作序列长度；
- 该保证是否同时覆盖 insert 和 lookup；
- rebuild 失败时如何处理。

## 9. Prefix / prefix matching

Previous Construction 和 Our Techniques 中反复出现 prefix。

定义：

- 元素先通过全局 hash 函数映射为二进制串；
- 不同阶段保存不同长度的 hash 前缀；
- 查询 `y` 时，需要判断 `h(y)` 的某个前缀是否已经出现在结构中。

待细化：
- 为什么保存前缀足以控制误报；
- 为什么不同长度前缀造成 prefix matching 问题；
- 本文新的 dictionary 为什么能自动解决长字符串 prefix matching。
