# Review 提纲 v1

日期：2026-07-17

状态：Day 1 初版。本文档用于记录小组对 review 结构的早期规划，后续会随着精读和交叉审阅继续调整。

## 1. 摘要

- 用中文概括论文研究的问题：未知集合规模下的动态 filter / dictionary。
- 概括论文核心贡献：当前规模空间、最优 `log log n` 领先常数、最坏情况常数时间。
- 说明 review 的组织方式。

## 2. 引言

- 从 membership query 的应用场景引入。
- 解释 dictionary 与 filter 的区别。
- 说明为什么 Bloom filter 及其变体很重要。
- 引出“最终集合大小未知”的困难。

## 3. 问题定义与研究意义（A 主责）

### 3.1 近似成员查询问题

- 全集 `[u]`。
- 当前集合 `S` 与当前大小 `n = |S|`。
- `insert(x)` 与 `lookup(x)`。
- dictionary：精确回答。
- filter：允许 false positive，不允许 false negative。

### 3.2 已知容量与未知容量的区别

- 已知容量 `N` 时，结构可按 `N` 预分配空间。
- 当实际 `n << N` 时，空间浪费。
- 若 `N` 只是保守估计，浪费更严重。
- 本文目标：空间依赖当前 `n`，不是依赖最大估计 `N`。

### 3.3 为什么 filter 的动态扩容更难

- exact dictionary 可以枚举旧元素并搬迁。
- filter 为节省空间丢失了原始 key 信息，不能直接恢复旧集合。
- 保留多个阶段 filter 会引入查询次数和误报率累积问题。

### 3.4 空间下界与问题重要性

- 已知容量 approximate membership 的经典空间约为 `N log(1/epsilon)` bits。
- 未知规模且空间随当前 `n` 变化时，已有下界包含额外 `log log n`。
- 本文将额外项做到领先常数 1，并同时实现高概率最坏情况常数时间。

## 4. 相关研究（C 主责，A 参与理论核查）

- Bloom filter 与 approximate membership。
- Dynamic / scalable filter。
- Succinct dictionary。
- Quotient filter / cuckoo filter。
- Deamortization 与 worst-case constant time hashing。
- Pagh、Segev、Wieder 关于 unknown-size filter 的前作。
- 2020 年之后的后续研究。

## 5. 论文主要结果

- Dynamic filter 的 informal theorem。
- Dynamic dictionary 的 informal theorem。
- 结果中的参数限制：`n > u^0.001`、`epsilon = o(1)` 等。
- 与前作的空间和时间保证对比。

## 6. 核心技术直觉（B 主责，A 审阅定义）

- 哈希为二进制串。
- 不同阶段保存不同长度前缀。
- 查询转化为 prefix matching。
- 短字符串用 truth table 处理。
- 长字符串用新的 exact membership data structure 处理。
- 随着 `n` 增长进行阶段式扩容和渐进迁移。

## 7. 数据结构实现细节

- 阶段划分。
- 新旧结构并存。
- 插入流程。
- 查询流程。
- 迁移流程。
- 去均摊化。

## 8. 正确性证明框架

- 无 false negative。
- 误报率不超过 `epsilon`。
- Prefix matching 的正确性。
- 迁移中间态仍可查询。

## 9. 空间复杂度证明框架（A、B 共同）

- 主项 `n log(1/epsilon)`。
- 未知规模额外项 `n log log n`。
- 本文低阶冗余为什么不破坏领先常数。
- 与 Pagh、Segev、Wieder 下界对齐。

## 10. 时间复杂度证明框架

- lookup 最坏情况常数时间。
- insert 最坏情况常数时间。
- 高概率保证与失败事件。
- 与 expected amortized constant time 的区别。

## 11. 技术优越性与局限

- 优越性：空间领先常数、当前规模、自适应增长、去均摊化。
- 局限：参数范围、模型假设、实现复杂度、随机性假设。
- 需要避免夸大：不能简单说“全面优于 Bloom filter”。

## 12. 后续研究与评价

- 论文发表后的相关方向。
- 是否有直接改进本文的工作。
- 是否与 learned Bloom filter、adaptive filter 等方向有模型差异。

## 13. 结论

- 总结本文问题、技术和理论意义。
- 总结小组对其贡献的评价。

## Day 1 待补充

- C 补充参考文献表和正式 BibTeX。
- B 补充构造路线图。
- A 在 Day 2 核查正式模型和下界来源。
