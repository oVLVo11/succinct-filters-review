# 成员 C 第一轮论文阅读笔记

- 阅读日期：2026-07-19
- 负责人：陈戚（成员 C）
- 当前状态：第一轮阅读与证据定位，成员 C 已审核本轮记录；外部文献待按标记继续核验
- 论文：Mingmou Liu, Yitong Yin, Huacheng Yu, *Succinct Filters for Sets of Unknown Sizes*, ICALP 2020

## 1. 实际读取范围与来源

本轮实际读取了：

- 仓库中的 `README.md`、`AGENTS.md`、`Plan.md`、`work/day1.md`；
- `drafts/outline-v1.md`、`discussions/questions.md`；
- 成员 A、B 的全部笔记和 `figures/` 中两份文字图；
- 论文正式 ICALP 版本的 Abstract、§1、§1.1、§1.2、§1.3、§1.4、§1.4.1；
- 正式 Theorem 10、Lemma 11、Theorem 12、Claim 13；
- §5 的结构概览、§7 的 allocate-free 空间结果、References。

论文证据入口：

- 正式出版页：https://doi.org/10.4230/LIPIcs.ICALP.2020.79
- arXiv 完整版：https://arxiv.org/abs/2004.12465

环境说明：仓库中的本地 PDF 已确认存在，但本机缺少 Poppler、pypdf 等解析器，无法直接提取本地文件。本轮实际阅读的是同一论文的 Dagstuhl 正式在线 PDF，并对重点页进行了页面渲染核查。因此下文的页码采用正式版页码 `79:x`，不声称本地 PDF 已被工具直接解析。

## 2. 当前理解的研究问题

论文维护当前集合 `S ⊆ [u]`，支持插入与成员查询。精确回答的是 dictionary；允许对非成员以至多 `epsilon` 的概率回答 YES、但对成员必须回答 YES 的是 filter。

标准结构初始化时常取得容量上界 `N` 并按 `N` 分配空间。本文关注的 `unknown sizes` 是：初始化时不知道最终集合大小或紧容量上界，但结构在任一时刻仍应让空间依赖当前 `n = |S|`，而不是依赖保守估计的 `N`。

难点不只是数组扩容。exact dictionary 保存足以恢复 key 的信息，容量翻倍时可以枚举并迁移；filter 为节省空间有意丢失原 key，通常无法从旧状态恢复全部 key 并重新计算更大值域中的哈希。保留多个旧 filter 虽可避免恢复 key，却会增加查询结构数量，并要求跨阶段分配误报预算。

证据位置：正式版 79:2-79:3（§1 Introduction），尤其关于容量、迁移困难和 PSW 下界的段落。

## 3. 当前理解的主要结果

### 3.1 Filter：非正式结果与正式结果必须分开

| 层次 | 原论文声明 | 证据位置 |
|---|---|---|
| 非正式 Theorem 1 | 当 `n > u^0.001` 时，空间为 `(1 + o(1)) n (log(1/epsilon) + log log n)` bits；所有插入与查询以高概率最坏情况常数时间。 | 79:3，Theorem 1 |
| 正式 Theorem 10 | 对 `n = omega(log u)` 且 `n < u`，操作序列相关空间为 `n(log(1/epsilon) + log log n + O(log log log u))` bits，另有与输入无关的 `u^c` 预计算位；每次操作最坏 `O(1)`；任意插入序列中曾报告 failure 的概率至多 `delta = u^{-C}`；条件于不失败，每次查询误报率至多 `epsilon`。 | 79:9，Theorem 10 |

当前结论：仓库现有材料常把 `n > u^0.001` 与正式定理条件混在一起。二者不是同一句定理。需要由成员 A/B 进一步写清：怎样从正式的加性 `O(log log log u)` 表述，在相应参数区间推出非正式的 `(1 + o(1))` 表述。

### 3.2 Dictionary

正式 Theorem 12 对 key-value universe `[u] × {0,1}^v` 给出：当 `n = omega(log u)` 且 `n < u` 时，操作序列相关空间为

```text
n(log(u/n) + v + O(log log log u)) bits,
```

另有与输入无关的 `u^c` 预计算位；插入与查询最坏 `O(1)`；任意插入序列上曾报告 failure 的概率至多 `u^{-C}`；条件于不失败，查询正确。证据位置：79:11，Theorem 12。

当前结论：非正式 Theorem 2 的 succinct 说法与正式定理的加性冗余也需要分开陈述。`v = 0` 给出 exact membership，但这仍是 dictionary，不是允许误报的 filter。

## 4. 与成员 C 职责直接有关的相关工作分类

原论文 §1.2 自己按三条主线组织相关工作：

1. **最坏情况常数时间 membership**：FKS、dynamic perfect hashing、real-time hashing、de-amortized/backyard cuckoo hashing；
2. **succinct membership**：Raman-Rao、Pagh-Pagh-Rao、adaptive filter、Bercea-Even；
3. **unknown-size membership**：Raman-Rao 的当前 `n` 解释与 Pagh-Segev-Wieder 的 filter 下界/上界。

成员 C 的外部补充还应单列：

- Bloom filter、dynamic/scalable Bloom filter：动机或工程扩容对照；
- quotient/cuckoo filter：工程实现对照，不能自动视为本文理论模型的竞争结果；
- 2020 年后的 expandable filter、dynamic succinct dictionary 与相关下界。

## 5. 十二个基础问题的当前回答

以下回答只是本轮可回溯的理解，不替代成员本人复核。

### 5.1 dictionary 与 filter 的区别

dictionary 对成员与非成员都精确；filter 只保证成员查询必为 YES，对非成员允许概率至多 `epsilon` 的 YES。正式版 79:1-79:2。

### 5.2 false positive 与 false negative

- false positive：`x notin S` 却回答 YES；filter 允许但概率受控。
- false negative：`x in S` 却回答 NO；本文模型不允许。

### 5.3 为什么本文 filter 不允许 false negative

这是 approximate membership 的一侧错误语义，而不是由实现偶然决定。若允许漏报，过滤器无法再作为“回答 NO 即可安全跳过后端访问”的前置结构，问题模型也会改变。正式版 79:2 定义和 79:10 的化归说明无漏报。

### 5.4 `unknown sizes` 未知什么

未知最终 `|S|` 或紧容量上界；全集大小 `u` 仍是模型参数，当前 `n` 可用于确定阶段。正式版 79:2、79:9。

### 5.5 为什么按 `N` 预分配会浪费

标准结构按容量设置 `Theta(N)` 桶或等价空间；当前 `n << N` 或 `N` 只是保守估计时，空间仍长期按 `N` 占用。正式版 79:2。

### 5.6 为什么 filter 不能像保存完整 key 的 dictionary 一样直接迁移

过滤器状态没有保存完美数据库信息，容量改变时无法恢复原 key 并把它们重新哈希到扩大后的范围。这正是 filter 节省空间的代价。正式版 79:2、79:4。

### 5.7 filter 的主要空间结果

正式式为 `n(log(1/epsilon)+log log n+O(log log log u))` 个与操作相关的位，加 `u^c` 个输入无关预计算位；非正式 succinct 形式在相应参数区间写成 `(1+o(1))n(log(1/epsilon)+log log n)`。不能漏掉两种表述的条件差异。

### 5.8 dictionary 的主要空间结果

正式式为 `n(log(u/n)+v+O(log log log u))` 个与操作相关的位，加 `u^c` 个输入无关预计算位。正式版 79:11。

### 5.9 `expected amortized O(1)` 与 `worst-case O(1) with high probability`

前者只约束长期平均且再对随机性取期望，个别操作可能很慢；后者说除一个小概率失败事件外，多项式长度序列中的每次操作都满足最坏常数时间。原论文在 79:3 脚注 4 给出这一解释。正式 Theorem 10/12 又把“每次操作最坏 O(1)”和“曾报告 failure 的概率”拆开列出，写作时应保留这种精确性。

### 5.10 相对 Pagh-Segev-Wieder 的主要改进

原论文明确声称两点：把 `log log n` 项的领先常数钉到 1（对 `epsilon=o(1)` 的非正式 succinct 结论），并把 PSW 的 expected amortized insertion 提升为高概率最坏常数时间。正式出版页摘要与 79:3-79:4。

### 5.11 prefix matching 的作用

阶段 `i` 插入 key `x` 时保存全局哈希 `h(x)` 的长度 `ell_i` 前缀；查询 `y` 时判断数据库中是否有某个已存串是 `h(y)` 的前缀。真成员的对应前缀存在，所以不漏报；非成员的前缀碰撞用 `sum_i 2^i 2^{-ell_i}` 并合控制。正式版 79:9-79:10。

### 5.12 为什么不能只按“支持删除、运行很快”比较相关工作

删除、吞吐、缓存局部性属于不同维度。本文核心组合是：空间随当前 `n`、误报率受控、接近 unknown-size 信息论下界、操作具有特定最坏/高概率保证，并采用明确 RAM/内存模型。一个支持删除或实验更快的 quotient/cuckoo filter 可能仍需预知容量或只有均摊/实验保证，不能据此宣布理论上改进本文。

## 6. 技术直觉与证明骨架（用于口头检查）

1. 全局有限独立哈希把 key 转成随机长串；不同阶段只保存不同长度前缀。
2. `ell_i = i + log(1/epsilon) + log i + log log log u + 2` 使所有阶段的碰撞概率和小于 `epsilon`。
3. prefix matching 数据结构只保存 core set：若已有更短前缀，新串无需再保存；这点是空间和后续随机分布论证的入口。
4. 短串用 truth table；长串交给已知容量 `D(m, ell)`。
5. 每次插入执行常数次 `decrement / destroy / initialize`，逐步把旧阶段搬到新阶段；查询同时检查常数个新旧结构。
6. 底层 `D` 用 main table、subtable、adaptive prefixes 和 data blocks。data block 把动态块的高冗余限制在少量最新块，并在后台转为静态紧凑块。
7. 正确性分成：存储/迁移不变式给出无漏报；哈希前缀并合给出误报率；失败事件并合给出高概率保证；空间逐项求和；后台工作量给出最坏常数时间。

证据位置：79:5-79:7（技术直觉），79:9-79:10（filter 化归），79:11-79:13（Claim 13），79:13-79:17（已知容量结构）。

## 7. 已确认内容与仍待理解内容

### 已由原论文正式版确认

- 问题模型和一侧错误语义；
- Theorem 1/2 与 Theorem 10/12 的不同表述；
- PSW 是原论文最直接的 unknown-size filter 前作；
- prefix matching 化归、`ell_i` 公式与误报并合；
- Claim 13 的四类活跃结构与后台迁移接口；
- data block 是原论文自称的主要技术贡献之一；
- 论文没有把用户级删除列为 Theorem 10 的操作。

### 尚未理解或尚未独立验证

1. PSW 下界中 `(1-O(epsilon))log log n` 的完整证明；
2. 正式 Theorem 10 到非正式 Theorem 1 的精确参数推导；
3. Claim 13 中固定执行 10 次维护为何对全部初始化、销毁和空 `decrement` 足够；
4. §5 data block 各字段的逐项位数求和；
5. §6 无条件 dictionary 的 Feistel/散列变换如何同时保证负载并精确恢复 key；
6. extendable array 与 allocate-free 模型对真实实现常数和空间峰值的影响；
7. 预计算 `u^c` 随机位在工程实现中是否可接受。

## 8. 后续验证方式

- 对 1：精读 Pagh-Segev-Wieder 2013 正文和定理；
- 对 2、3：由成员 A/B 独立复算阶段区间、总工作量和低阶项；
- 对 4、5：逐段阅读 arXiv 完整版附录和伪代码；
- 对 6：对照 Raman-Rao 的 extendable array 模型；
- 对 7：在评价部分明确区分操作序列相关空间与输入无关预计算空间；
- 任何从本文外部文献得到的复杂度，先写入文献矩阵并标证据位置，不直接进入 Review 正文。

## 9. 本轮人工复核状态

本文件由 Codex 辅助整理。成员 C 已于 2026-07-19 审核本轮内容，并确认其可作为第一轮过程记录。这里的审核是对记录范围、主论文定位和状态标记的确认；尚未精读的外部文献仍按“待核验”处理。
