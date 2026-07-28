# 相关研究、评价与后续工作（章节初稿）

- **作者**：陈戚（成员 C）
- **版本**：v0.1（Day 5–6 初稿，待成员 C 审核）
- **日期**：2026-07-28
- **依据**：主论文 §1–§3、Theorem 10、Claim 13；PSW 2013 Theorem 3.1；成员 C 已核验的经典/后续文献矩阵
- **引用约定**：文中方括号给出 `references/bibliography.bib` 的 key；E3 表示已读原文关键定义、定理和引用语境，E2/E1 不承担确定性技术比较
- **未关闭项**：InfiniFilter 与 Li 等人 2023/2024 尚未完成全文核验；2026 工作须在最终提交前再次检查版本

---

## 1. 比较之前：先固定问题模型

本文中的 `n` 按主定理的插入序列口径理解；“unknown size”指事前没有一个紧的最终容量上界，而不是算法不知道当前已经处理了多少次插入。本文的目标组合是：

```text
插入序列最终规模未知
+ 空间随当前插入规模变化
+ 已插入元素不漏报
+ 非成员误报率至多 ε
+ 无 failure 时插入和查询均为 worst-case O(1)
```

比较相关工作时至少要分开六个维度：空间按固定容量、历史峰值还是当前规模计；是否支持用户删除；误报如何累计；操作时间是 expected、amortized、worst-case 还是 whp；是否给可运行实现；结论是否依赖 failure、宇宙大小和预计算空间。缺少这些限定时，“动态”“可扩容”或“更优”都不足以构成可验证结论。

---

## 2. 经典起点：Bloom filter 与 approximate membership

Bloom filter 是 approximate membership 的经典起点：它允许非成员偶尔被回答为 YES，但不允许把已插入成员回答为 NO [bloom1970space]。Carter 等人把 exact/approximate membership 作为更一般的表示问题研究，为已知规模情形的空间下界提供理论基础 [carter1978membership]。本章只用这两项说明历史起点，不采用尚未从全文复核的具体最优哈希数或常数。

经典 Bloom filter 通常要根据目标容量预先选择位数组大小和哈希函数个数。若实际插入数持续超过设计容量，误报率会偏离原目标。因此它与 Liu–Yin–Yu（下称 LYY）的差别不是“是否允许插入”，而是能否在没有紧最终容量的情况下，同时维持当前规模空间、严格误报预算和可比的最坏情况时间。

---

## 3. 多组件增长：Scalable 与 Dynamic Bloom filter

Scalable Bloom Filter（SBF）在当前组件达到阈值后增加新组件，并把各组件误报预算按几何级数收紧；查询需要测试每一个现有组件。组件容量指数增长时，组件数随集合规模呈对数增长 [almeida2007scalable, §4–§5]。Dynamic Bloom Filter（DBF）也用多个等参数 Bloom 组件增长，但其论文给出的查询平均复杂度依赖组件数，误报表达式也随组件数变化 [guo2006dynamic, §III、式 (3)]。

普通读者可以把两者的查询路径画成：

```text
query ──► Filter_0 ──► Filter_1 ──► … ──► Filter_s
              任一组件回答 YES，则总体回答 YES
```

SBF/DBF 说明“不预知最终规模”在工程上可以通过组件追加处理，但它们并不自动获得 LYY 的全部组合保证：LYY 的查询只检查常数个相邻结构，空间结论以 word-RAM 位复杂度和信息论下界为目标。反过来，SBF/DBF 的实现简单性也不能由 LYY 的渐近定理否定。这里应写“模型目标和保证不同”，而不是“LYY 全面优于 Bloom filter”。

---

## 4. Succinct dictionary、动态 hashing 与去均摊化背景

Exact dictionary 保存足够信息以精确区分集合；其稀疏空间基准接近

```text
log binom(u,n) ≈ n log(u/n) + O(n),
```

而 filter 允许误报，主空间基准是 `n log(1/ε)`。两者编码对象不同，所以不能把 dictionary 的 `log(u/n)` 与 filter 的 `log(1/ε)` 直接按数值排名。

Raman–Rao 的 succinct dynamic dictionary 与 extendable-array 思想为“空间按当前规模变化”提供背景 [raman2003succinct]；Demaine 等人与 Backyard Cuckoo Hashing 分别代表紧凑动态字典和去均摊 cuckoo hashing 的技术线 [demaine2006dictionariis; arbitman2010backyard]。LYY 的技术困难正位于两条线的交叉处：既要把表示压到 bit-level succinct，又要把扩容、迁移和块重组拆成每次操作的常数工作。

这里的相关性是技术背景，而不是等价替代。Exact dictionary 不允许误报，并且通常保留的可恢复信息多于 filter；“线性机器字空间”也不等于“接近信息论下界的位空间”。

---

## 5. 原文未引用的工程对照：Quotient 与 Cuckoo filter

Quotient filter 把 fingerprint 分成 quotient 与 remainder，利用表位置和槽内信息支持查询、删除、合并与 resize；其操作和空间分析依赖槽数、负载率以及 cluster 长度 [bender2012quotient, §3–§4]。Cuckoo filter 把 fingerprint 放进两个候选桶，查询只需检查两个桶，但插入可能发生递归 relocation，并在高负载时失败；其容量、桶大小、目标负载与 fingerprint 长度共同影响保证 [fan2014cuckoo, §4–§5]。

这两篇论文没有出现在 LYY 的参考文献表中，本 Review 把它们标为外补的工程/模型对照。它们在删除、局部性和实现吞吐等维度很重要，但“可 resize”不等于已经证明 LYY 的 unknown-size 信息论空间式，“查询两个桶”也不等于 LYY 在相同随机模型下的序列级 worst-case 保证。

---

## 6. 直接理论谱系：PSW 2013 到 LYY 2020

Pagh–Segev–Wieder（PSW）首次直接处理本项目所关心的 unknown-size approximate membership：最终规模未知，但结构在各个中间规模都要受空间约束 [pagh2013unknown]。PSW Theorem 3.1 的编码下界说明，这种要求除 `n log(1/ε)` 外，还会产生约 `n log log n` 的额外信息成本；该下界不依赖操作时间。

PSW 同时给出接近下界的结构，但 LYY 转述其插入为 expected amortized `O(1)`，而 `log log n` 上界项没有钉死领先常数。LYY 的贡献不是重新提出 unknown-size 问题，而是在相应参数条件下把两件事同时推进：

1. Theorem 10 给出
   `n(log(1/ε)+log log n+O(log log log u))+u^c`
   的空间式；
2. 在 `ε=o(1)` 等条件下，`log log n` 项的领先常数与 PSW 参数化下界对齐；
3. 无 failure 时，插入和查询均为 worst-case `O(1)`，整段序列 failure 概率受 `u^{-C}` 控制 [liu2020succinct]。

因此可靠措辞是“LYY 在 insertion-only unknown-size 模型中同时收紧空间领先项与时间语义”，而不是无条件“达到全部信息论最优”。

---

## 7. 原文提及但没有充分展开的工作

LYY 的引言把大量既有结果压缩在很短的篇幅中。至少有三类背景需要 Review 主动展开：

1. **已知容量 succinct filter**：Pagh–Pagh–Rao 代表已知容量下接近 `N log(1/ε)` 的结构 [pagh2005optimal]。它说明主误报空间可接近下界，但不能直接解决最终 `N` 不知的问题。
2. **动态 exact dictionary**：Raman–Rao、Demaine 等工作解释了当前规模空间与动态操作为何可能共存，但 exact dictionary 的信息论基准和 filter 不同。
3. **deamortization / adaptive prefixes**：去均摊 cuckoo hashing 和 adaptive-filter 技术为最坏情况更新、前缀表示提供组件；它们本身并不自动证明 LYY 的整体空间式。

把这些脉络展开后，本文的非凡之处更清楚：它不是发明了每一个局部组件，而是把前缀误报预算、两代结构迁移、短串 truth table、长串 succinct prefix matching 和底层块级重组组合成同一条可证明的依赖链。

---

## 8. 2020 年后的研究：三种不能混用的“动态”

### 8.1 Aleph Filter：工程化无限增长与删除

Aleph Filter 正文直接比较 LYY，并指出 LYY 给出常数时间的 unknown-size 理论结构，但主过滤器没有展示删除且增长受固定宇宙约束 [dayan2024aleph, §7]。Aleph 强调可运行的无限增长、删除和内存—误报率权衡。其摘要使用 constant-time 表述，但 §5.2 的 void duplicate 清理按生命周期作 amortized 分析，因此不能直接改写为 LYY 的“无 failure 时 worst-case `O(1)`”。

关系判断：Aleph 在删除、无限增长和工程实现维度更进一步；它的空间参数、清理成本和随机保证不同，不能据此说它在同一模型上全面取代 LYY。

### 8.2 Kuszmaul–Walzer 2024：删除改变空间下界

Kuszmaul–Walzer 研究支持插入和删除、容量受 `n` 约束的 fully dynamic filter，并证明相对静态最优还必须有线性额外空间；其 Theorem 3.1 在给定参数区间给出超过 `0.35n-o(n)` 的额外项 [kuszmaul2024dynamicfilters]。该结论是与运行时间无关的信息论下界。

关系判断：这项工作解释了为什么不能把 LYY 的 insertion-only 空间式直接外推到删除模型。它不是对 LYY 正确性的反驳，而是说明增加删除后问题本身的信息成本发生变化。

### 8.3 Resizable Retrieval 2026：空间按当前集合大小

*Resizable Retrieval* 把 retrieval 的空间改为按当前集合大小 `n` 计，并由此导出支持插入、删除的 dynamic filter 推论。其 Corollary 3.14 给出

```text
n log(1/ε)
+ O(n log log(U/n))
+ polylog U
+ O(U^δ)
```

位，操作为相对当前 `n` 的 constant time with high probability [kuszmaul2026resizable, Cor. 3.14]。该文直接把 PSW/LYY 作为 extendable-filter 前作讨论。

关系判断：它把“可增长”推进到“空间按当前规模收缩并支持删除”，但额外项依赖 `U/n`，还有 `polylog U`、`U^δ` 和 whp-in-`n` 条件，不能说无条件支配 LYY。截至 2026-07-28，arXiv 与 DBLP 仍把它列作 CoRR 预印本；本 Review 不声称已经正式发表。

### 8.4 暂不进入确定性比较的旁支

InfiniFilter 目前只有 E2 证据：可作为 Aleph 的工程前代提及，但尚未从正式全文确认它是否直接引用 LYY及精确时间语义 [dayan2023infinifilter]。Li 等人 2023/2024 的 dynamic succinct dictionary 工作目前为 E1，它们研究 exact dictionary 的冗余—时间权衡，不作为本章的确定性 filter 比较结论。

---

## 9. 多维评价：本文强在哪里，又没有解决什么

| 维度 | LYY 2020 | 可靠评价 |
|---|---|---|
| 空间 | 当前插入规模主项含 `log(1/ε)+log log n`，另有低阶项和 `u^c` | 在相应 unknown-size 参数区间与 PSW 下界的领先项对齐 |
| 时间 | 无 failure 时插入、查询 worst-case `O(1)` | 比 PSW 的 expected amortized 插入语义更强；不等于工程吞吐更快 |
| 删除 | 主过滤器接口不支持用户删除 | fully dynamic 不是本文已解决范围 |
| 增长 | 不需紧最终容量，但固定宇宙 `[u]` | 不等于不受宇宙限制的无限增长 |
| 实现性 | 依赖多层哈希、adaptive prefixes、data blocks 与后台重组 | 理论组合精细，实际实现和常数尚未由本文实验展示 |
| 证明强度 | 同时给误报、failure、时间和位空间依赖链 | 定理很强，但保证带参数范围和 no-failure 条件 |

本文最值得肯定的不是某一个单项“首次”，而是**组合保证**：在 filter 丢弃原键、不能像 exact dictionary 那样直接枚举旧键重建的情况下，仍让空间随插入规模变化，只查常数个相邻结构，并用后台迁移获得最坏情况常数操作。短串 truth table 与长串 `D(m,ℓ)` 的分工也把“复制短前缀造成空间爆炸”的问题转化为可控的 truth-table 空间。

---

## 10. 局限性、适用范围与开放问题

1. **无用户删除**：Theorem 10 针对插入序列，不能称为 fully dynamic filter。
2. **概率保证有两层**：`ε` 是无 failure 时的误报率；`u^{-C}` 是整段序列报告 failure 的概率。二者不能相加成“总错误率”。
3. **参数与预计算**：正式定理要求 `n=ω(log u)`、`n<u`，并含输入无关的 `u^c` 位预计算空间；非正式 `(1+o(1))` 形式还有更强的展示条件。
4. **工程复杂度**：word-RAM 的 worst-case `O(1)` 不等于简单或高速实现。论文没有用实验把隐藏常数、缓存行为和迁移峰值转化为工程结论。
5. **小组核查边界**：Claim 13 阶段下标的形式归纳、字面常数 10 的隐藏常数配平，以及 §5 迁移瞬时位级峰值仍是本 Review 的公开核查项；这不等于断言原论文错误。
6. **对手模型**：原文不足以让本组无条件扩张到自适应查询对手，正文不作该承诺。

由这些边界可提出四个后续问题：

- 能否在保留可比的最坏时间和当前规模空间时支持删除？
- 能否降低或消除 `u^c` 级全局随机性/预计算项？
- 能否把 Claim 13 与 §5 转化为可复现实验实现，测量隐藏常数、迁移峰值和缓存行为？
- 对 adaptive queries / adaptive adversary，误报与 failure 保证需要怎样重述？

---

## 11. 文献时间线与证据说明

| 时间 | 工作 | 本章中的作用 | 证据等级 |
|---:|---|---|---|
| 1970/1978 | Bloom；Carter 等 | 历史与问题起点，不采用未复核常数 | E1 |
| 2003–2010 | succinct dictionary、动态 hashing、去均摊 cuckoo | 技术背景；不作同模型排名 | E1/E2 |
| 2006/2007 | DBF / SBF | 多组件增长与查询/FPR 对照 | E3（关键章节） |
| 2012/2014 | Quotient / Cuckoo filter | 原文未引的工程对照 | E3（关键章节） |
| 2013 | PSW unknown-size filter | 直接前作和下界 | E3（A 已核验 Theorem 3.1） |
| 2020 | LYY | 本项目主论文 | E3 |
| 2023/2024 | InfiniFilter / Aleph | 工程化扩展；前者仅 E2，后者 E3 | E2/E3 |
| 2024 | Kuszmaul–Walzer | 删除型 dynamic filter 下界 | E3 |
| 2026 | Resizable Retrieval | 当前 `n`、删除型新进展；预印本 | E3 |

引用与元数据逐项记录在 `references/citation-audit.md`。E1/E2 条目保留在研究矩阵中，是为了展示资料筛选过程；它们没有被悄悄升级为正文中的确定性技术结论。

---

## 12. 本章结论

LYY 应放在“经典 approximate membership → 多组件工程扩展 → succinct dictionary 与去均摊背景 → PSW unknown-size 直接前作 → 后续 deletion/resizable 研究”的时间线上理解。它最强的地方是把 unknown-size 空间主项、误报与无漏报、序列级 failure 和最坏情况常数操作组合在同一构造中；它的限制则集中在删除、固定宇宙、预计算空间、实现复杂度和概率条件。后续工作扩大了模型或实现能力，但目前没有证据支持把所有结果排成一条无条件的“更新论文全面优于旧论文”序列。
