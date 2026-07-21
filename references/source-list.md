# 文献来源清单（第一轮）

- 日期：2026-07-19 建表；2026-07-20 完成第一批正文核验
- 负责人：陈戚（成员 C）
- 原则：先整理原论文明确讨论的工作，再补充原文未引用的工程对照与后续候选。

状态含义：`候选`、`仅看摘要`、`已读相关章节`、`已核查定理`、`已排除`。

| 文献 | 类别 | 原论文引用编号 | 原论文出现位置 | 为什么相关 | 当前阅读状态 | 下一步核验内容 | 正式来源 |
|---|---|---:|---|---|---|---|---|
| Liu, Yin, Yu, *Succinct Filters for Sets of Unknown Sizes* (2020) | 主论文 / unknown-size filter | - | 全文 | 本项目对象 | 已核查 Theorem 10/12、Claim 13 | 精读 §5/§6 与附录 | https://doi.org/10.4230/LIPIcs.ICALP.2020.79 |
| Bloom, *Space/Time Trade-offs in Hash Coding with Allowable Errors* (1970) | 经典 Bloom filter | 未引用 | 原文仅使用 “Bloom filters” 主题词 | 历史起点；固定容量工程背景 | 仅看摘要 | 原始参数与时间/空间分析 | https://doi.org/10.1145/362686.362692 |
| Carter et al., *Exact and Approximate Membership Testers* (1978) | approximate membership / 下界 | [8] | §1、§1.2、References | 已知容量近似成员表示的理论基础 | 仅看摘要 | 原始下界的精确概率模型 | https://doi.org/10.1145/800133.804332 |
| Almeida et al., *Scalable Bloom Filters* (2007) | scalable Bloom filter | [1] | §1、§1.2、References | 不预知最终元素数、固定总体 FP 的组件扩容对照 | 已读原文 §4-5 | 若进入正文，复算相对空间曲线；原始构造未给删除 | https://doi.org/10.1016/j.ipl.2006.10.007；PDF pp.4-8 |
| Guo et al., *Theory and Network Applications of Dynamic Bloom Filters* (2006) | dynamic Bloom filter | [16] | §1、References | 多组件动态增长；查询和 FP 随组件数变化 | 已读原文 §III 与结论 | 若进入正文，复核式 (3) 各符号；原始算法未给删除 | https://doi.org/10.1109/INFOCOM.2006.325；PDF pp.3-6、12 |
| Arbitman, Naor, Segev, *De-amortized Cuckoo Hashing* (2009) | hashing / deamortization | [2] | §1.2、References | whp 最坏常数时间技术背景 | 候选 | 原定理、序列长度、空间单位 | 原论文 References [2]；DOI 待核验 |
| Arbitman, Naor, Segev, *Backyard Cuckoo Hashing* (2010) | succinct dictionary / cuckoo hashing | [3] | §1.2、References | 结合 succinct 表示与 whp 最坏常数操作 | 仅看摘要 | 容量与当前 `n` 的关系 | https://arxiv.org/abs/0912.5424 |
| Bender et al., *Bloom Filters, Adaptivity, and the Dictionary Problem* (2018) | adaptive filter | [4]/[5] | §1.2、§1.4.1、References | adaptive queries 与 adaptive prefixes 背景 | 仅看摘要 | 本地/远端组件、空间定理、容量假设 | https://arxiv.org/abs/1711.01616 |
| Bercea, Even, *Fully-Dynamic Space-Efficient Dictionaries and Filters...* (2019 preprint) | fully dynamic succinct dictionary/filter | [6] | §1.2、§1.4.1、References | 本文比较其扩展冗余；底层构造背景 | 已读主论文对它的讨论；候选正文仅看摘要 | 正式版本、当前 `n` 扩展与 `Omega(n log log u)` 推导 | https://arxiv.org/abs/1911.05060 |
| Demaine et al., *De Dictionariis Dynamicis Pauco Spatio Utentibus* (2006) | dynamic succinct hashing | [11] | §1.2、References | `O(n log(u/n))` bits 与 whp 常数操作背景 | 仅看摘要 | bit-level leading constant 与扩容模型 | https://doi.org/10.1007/11682462_34 |
| Fredman, Komlós, Szemerédi, *Storing a Sparse Table with O(1) Worst Case Access Time* (1984) | FKS perfect hashing | [15] | §1.2、References | 静态最坏常数 membership 基点 | 已读主论文相关章节 | 原始空间与模型 | 原论文 References [15]；DOI 待核验 |
| Pagh, Pagh, Rao, *An Optimal Bloom Filter Replacement* (2005) | succinct filter | [27] | §1、§1.2、References | 已知容量近最优 filter；更新为均摊期望 | 仅看摘要 | 精确空间、删除及哈希假设 | https://doi.org/10.1145/1070432.1070548 |
| Pagh, Segev, Wieder, *How to Approximate a Set Without Knowing Its Size in Advance* (2013) | unknown-size filter | [28] | Abstract、§1、§1.2、§1.3、References | 最直接前作与下界来源 | 仅看摘要；已读主论文转述 | 下界定理、上界和参数条件 | https://doi.org/10.1109/FOCS.2013.17 |
| Raman, Rao, *Succinct Dynamic Dictionaries and Trees* (2003) | succinct dictionary / extendable arrays | [29] | §1、§1.2、§1.3、§1.4、§2.2、References | PSW 黑盒、当前 `n` 空间和内存模型基础 | 仅看摘要 | extendable array 与更新定理全文 | https://doi.org/10.1007/3-540-45061-0_30 |
| Bender et al., *Don't Thrash: How to Cache Your Hash on Flash* (2012) | quotient filter | 未引用 | 无 | 删除、resize、局部性；依赖槽数和负载率 | 已读原文 §3-4 | 若进入正文，区分内存 QF 与 BQF/CF 的复杂度 | https://doi.org/10.14778/2350229.2350275；PDF pp.1-6 |
| Fan et al., *Cuckoo Filter: Practically Better Than Bloom* (2014) | cuckoo filter | 未引用 | 无 | 动态增删和实践吞吐；容量/负载及插入失败对照 | 已读原文 §1、§4-5 | 原论文未给 unknown-size resize 定理；最坏时间仍不可直接填写 | https://doi.org/10.1145/2674005.2674994；PDF pp.1、6-7 |
| Dayan et al., *InfiniFilter* (2023) | 后续 expandable filter | 未引用（后发） | 无 | 无限扩展、FPR/内存/性能权衡 | 摘要 + Aleph §1 对照 | 取得正式全文后核对是否引用本文；当前不判定 | https://doi.org/10.1145/3589285 |
| Dayan, Bercea, Pagh, *Aleph Filter* (2024) | 后续 expandable filter | 未引用（后发） | 无 | 正文明示比较本文；加入删除与无限增长 | 已读 Abstract、§5.2、§7 | 区分公开 constant-time 与部分清理 amortized 口径 | https://doi.org/10.14778/3681954.3682027；官方 PDF pp.1、8、12 |
| Li et al., *Tight Cell-Probe Lower Bounds for Dynamic Succinct Dictionaries* (2023) | 后续 dictionary 下界 | 未引用（后发） | 无 | redundancy-time tradeoff 的后续理论 | 仅看摘要 | 是否引用本文、定理模型 | https://doi.org/10.1109/FOCS57990.2023.00112 |
| Li et al., *Dynamic Dictionary with Subconstant Wasted Bits per Key* (2024) | 后续 dictionary 上界 | 未引用（后发） | 无 | `R=o(n)` 冗余区间 | 仅看摘要 | 与本文 dictionary 的模型/空间对齐 | https://doi.org/10.1137/1.9781611977912.9 |
| Kuszmaul, Walzer, *Space Lower Bounds for Dynamic Filters and Value-Dynamic Retrieval* (2024) | 后续 dynamic filter 下界 | 未引用（后发） | 无 | 说明 deletion-dynamic 与 incremental unknown-size 的区别 | 已读定义、主结论、Thm 3.1、引用 | 已确认 [28]=LYY；正文使用时保留容量 `n` 与删除模型 | https://doi.org/10.1145/3618260.3649649；KIT PDF pp.1、3--4、12 |
| Kuszmaul et al., *Resizable Retrieval* (2026) | 后续 resizable retrieval/filter | 未引用（后发） | 无 | 空间按当前 `n`，含 filter 推论 | 已读 Intro、Thm 1.1、Cor. 3.14 | 已确认引用 LYY；提交前复核预印本版本/发表状态 | https://arxiv.org/abs/2606.15944；v1 PDF pp.2--4、20--21 |

## 需特别说明的缺口

- 原论文 References 没有直接列 Bloom 1970、quotient filter、2014 cuckoo filter；最终 Review 必须标成“原文未引用但相关”，不能伪装成原论文比较对象。
- 原论文 [6] 引用的是 2019 arXiv；与 2020 SWAT 正式版本的题名和结果对应关系尚待核验。
- 后续候选中 Aleph、Kuszmaul--Walzer 2024、Resizable Retrieval 已读关键全文段落；InfiniFilter 与 Li 2023/2024 仍不能升级为“已核查定理”。
- 后续工作的直接引用与模型口径以 `references/post-2020-matrix.md` 为准。
- `references/bibliography.bib` 仅收录本轮已核查元数据的条目；缺失条目不是不存在，而是尚未完成可靠 BibTeX 核验。
