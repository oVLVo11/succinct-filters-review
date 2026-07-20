# 刘威论文阅读记录：Day 1 通读与 Day 2 精读

负责人：刘威（成员 A）
Day 1 日期：2026-07-17
Day 2 日期：2026-07-20

## 1. 阅读范围

### Day 1 通读

- 题目、摘要、第 1 节 Introduction；
- §1.1 Main Results；
- §1.2 Related Work 总体分类；
- §1.3 Previous Construction；
- §1.4 Our Techniques 高层直觉；
- §2.1、§2.2 字符串和计算模型。

### Day 2 精读

- 第 1-3 页：问题模型、known capacity 与 unknown size 的差别；
- 第 4-6 页：前作、多阶段 filter、prefix matching 和本文技术概览；
- 第 9-10 页：Theorem 10、公式 (2)、Lemma 11；
- 第 11-13 页：Theorem 12、Claim 13 及阶段迁移证明框架。

## 2. 用自己的话概括论文问题

这篇论文研究一种动态成员查询结构。我们不断插入 key，并随时询问某个 key 是否已经插入。

如果答案必须完全正确，结构叫 dictionary；如果允许对“没有插入的 key”偶尔回答 YES，但绝不能漏掉已经插入的 key，结构叫 filter。

传统 filter 往往要求初始化时先给出最大容量 `N`，之后一直按 `N` 占空间。现实中最终会插入多少 key 可能无法准确预测。若把 `N` 估得太大，会浪费空间；估得太小，又会溢出。

Exact dictionary 扩容时可以读取旧 key 并重新插入。Filter 为了省空间没有保存完整 key，通常无法恢复全部旧元素，所以不能简单照搬动态数组的扩容方法。

本文要同时做到三件事：

1. 不预知最终大小，空间仍随当前 `n` 增长；
2. 空间接近 unknown-size filter 的信息论下界；
3. 每次插入和查询都具有高概率最坏情况常数时间，而不是只保证平均或均摊时间。

## 3. Day 2 对 Day 1 理解的修正

### 修正 1：正式定理不只写 `n>u^0.001`

Day 1 只记录了摘要中的 `n>u^0.001`。精读后发现：

- 非正式 Theorem 1 用 `n>u^0.001` 给出简洁的 `(1+o(1))` 空间；
- 正式 Theorem 10 的条件是 `n=ω(log u)` 且 `n<u`；
- 正式空间还包含 `O(log log log u)` 每 key 冗余和输入无关的 `u^c` 位预计算空间。

所以最终 review 应先给简洁结论，再单独交代正式条件，不能只引用摘要。

### 修正 2：高概率保证可以写得更具体

Day 1 猜测失败概率可能是 `1/poly(n)`。正式 Theorem 10 写的是：

```text
δ = u^{-C}，C>1
```

对任意插入序列，整个过程中曾报告 failure 的概率至多 `δ`。概率取自预计算随机比特。

引言把相关文献中的 high probability 通俗描述为：除 `1/poly(n)` 的概率外，一段 `poly(n)` 长操作序列中的每个操作都在常数时间内完成。本文正式定理则使用关于 `u` 的更明确表达。因此写作时要注明引用的是引言解释还是 Theorem 10。

### 修正 3：`log log n` 的“构造来源”和“下界来源”不同

本文公式 (2) 中的 `log i` 解释了构造为什么多用约 `log log n` 位。但任何数据结构都不可避免这一项，是 PSW 信息论下界给出的结论。

不能把“阶段多”直接当成完整下界证明。

## 4. 本文主要结果

### 4.1 Dynamic filter

非正式结果：

```text
(1+o(1))n(log(1/epsilon)+log log n) bits
```

适用于摘要所写的 `n>u^0.001`，每次插入和查询以高概率具有最坏情况常数时间。

正式 Theorem 10：

```text
n(log(1/epsilon)+log log n+O(log log log u)) + u^c bits
```

其中：

- `0<epsilon<1`；
- `n=ω(log u)` 且 `n<u`；
- `0<c<1` 可取任意小常数；
- `u^c` 位与输入无关；
- failure 总概率至多 `u^{-C}`；
- 无 failure 时误报率至多 `epsilon`，没有漏报。

### 4.2 Dynamic dictionary

正式 Theorem 12 的空间为：

```text
n(log(u/n)+v+O(log log log u)) + u^c bits
```

机器字长为 `Θ(v+log u)`，每次插入和查询为 worst-case `O(1)`，failure 总概率至多 `u^{-C}`。A 只记录该结果与 filter 的关系，详细构造由 B 负责。

## 5. 正确性与优越性的初步证明路线

### 5.1 无 false negative

插入 key `x` 时保存 `h(x)` 的前缀；查询 `x` 时寻找 `h(x)` 的已存前缀。只要结构没有 failure，原来保存的前缀必然能被找到。

### 5.2 误报率

第 `i` 阶段保存：

```text
ell_i = i+log(1/epsilon)+log i+log log log u+2
```

位前缀。对阶段内所有 key 和所有阶段使用 union bound，误报总概率小于 `epsilon`。

### 5.3 查询时间

当 `n∈[2^i,2^{i+1})` 时，查询只检查：

```text
D_{i-1}, D_i, T_{i-1}, T_i
```

结构数量是常数，因此上层查询为常数时间。

### 5.4 插入时间

每次正常插入后执行 10 轮维护，逐步完成旧结构迁移、销毁和新结构初始化。这样把原本可能一次耗费 `Θ(n)` 的工作分散到很多次插入中。

“10 轮为什么一定够”和底层 `D(m,ell)` 的每个操作为何为常数时间，仍需结合 B 的构造笔记和第 5 节证明。

### 5.5 空间优越性

PSW 下界表明 unknown-size filter 需要：

```text
(1-o(1))n(log(1/epsilon)+(1-O(epsilon))log log n)
```

本文上界把 `log log n` 写成领先系数 1，并在 `epsilon=o(1)` 时与下界对齐；同时把插入从前作的 expected amortized constant 改进为 high-probability worst-case constant。

## 6. 为什么不是简单的 scalable Bloom filter

“可以不断增加新 filter”只是工程上的可扩展性。本文要求同时满足：

- 空间根据当前 `n` 达到接近信息论最优；
- 所有阶段总误报率严格不超过 `epsilon`；
- 查询不用扫描 `O(log n)` 个历史结构；
- 插入和查询均有最坏情况常数时间的高概率保证。

因此，其他 scalable/dynamic filter 即使能扩容，也必须逐项比较以上四点，不能仅凭名称说它已经解决本文问题。

## 7. 目前已经弄清的问题

1. unknown size 未知的是最终规模/紧容量上界；
2. filter 允许误报但不允许漏报；
3. `log(1/epsilon)` 是基础误报成本；
4. 构造中的 `log log n` 来自阶段误报预算，下界则由 PSW 独立证明；
5. Theorem 1 与 Theorem 10 的参数和空间写法为何不同；
6. high probability failure 与 false positive 是两种不同事件；
7. 本文相对 PSW 的两项核心改进：领先常数和最坏情况时间。

## 8. 仍未完全弄清的问题

1. PSW 下界完整证明如何编码不同规模下的状态；
2. Claim 13 中每次执行 10 轮维护为何对所有初始化、迁移、销毁都足够；
3. 四个活跃结构同时存在时，空间峰值怎样逐项压到 Lemma 11 的界；
4. 第 5 节 data block 的静态编码与动态重组空间如何求和；
5. 实际实现高独立性哈希和预计算表时的常数开销。

## 9. 给组员材料的核查问题

### 给张书铖（B）

1. 8 元素阶段例子是否始终只查询 `D_{i-1},D_i,T_{i-1},T_i`，阶段边界有没有多出第五个尚未初始化完成的结构？
2. “每次 10 轮维护”在例子中是否明确区分了迁移、destroy 和下一阶段 initialize？
3. 教学示例中的具体哈希串是否被明确标注为人为设定，而不是论文概率分布的真实样本？

### 给陈戚（C）

1. 文献矩阵是否区分 expected、amortized、worst-case 和 with high probability？
2. scalable/dynamic Bloom filter 是否真正让空间达到当前 `n` 的 succinct 界，还是只支持工程扩容？
3. 引用 PSW 下界时是否使用原论文或正式出版版本核对，而不是引用本文的二手概述？

## 10. 本次精读结论

本文解决的不是普通“让 Bloom filter 容量变大”，而是一个同时涉及信息论空间、概率正确性和动态最坏情况时间的问题。
可以先抓住三层结构：

1. **问题层：** 不知道最终 `n`，但空间要跟当前 `n`；
2. **表示层：** key 变成哈希前缀，查询变成 prefix matching；
3. **动态层：** 用分阶段后台迁移避免某次插入突然做大量工作。

然后再分别验证三件事：已插入元素不会漏掉、非成员误报不超过 `epsilon`、空间和时间达到定理中的界。这样比一开始直接钻进底层 data block 更容易建立整体理解。
