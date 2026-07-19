# 2020 年之后相关研究：检索方案与第一批候选

- 日期：2026-07-19
- 负责人：陈戚（成员 C）
- 当前阶段：检索路线已执行第一轮；候选不等于已证实改进

## 1. 检索数据库与入口

- Google Scholar：用于 “cited by” 网络；本轮工具环境未能直接访问，留给成员 C 人工复核。
- DBLP：核查作者、年份、正式会议/期刊与 DOI。
- arXiv：读取摘要与开放正文，记录版本日期。
- ACM Digital Library / IEEE Xplore / SIAM / PVLDB / Dagstuhl：确认正式发表信息与 DOI。
- 作者主页、学校论文页：只作为正式 PDF 入口，不替代出版元数据。
- Semantic Scholar / OpenAlex：可辅助找引用网络，但“引用本文”最终须在候选正文参考文献中确认。

## 2. 关键词

```text
"Succinct Filters for Sets of Unknown Sizes"
"How to Approximate a Set Without Knowing Its Size in Advance"
unknown-size filter
resizable filter
expandable filter
succinct filter dynamic
dynamic succinct dictionary
succinct hashing redundancy
approximate membership unknown capacity
deamortized dynamic dictionary
adaptive filter
learned Bloom filter
```

## 3. 两条检索路线

### 路线 A：明确引用本文

1. 从 DOI `10.4230/LIPIcs.ICALP.2020.79` 和 arXiv `2004.12465` 进入引用网络；
2. 对候选 PDF 查找完整标题、`Liu, Yin, Yu` 或 DOI；
3. 阅读引用所在段落，判断它只是背景引用、使用技术，还是声称改进；
4. 记录引用段落与该论文自己的主定理位置。

### 路线 B：同问题但未必引用本文

1. 用 `resizable/expandable filter` 查未知容量工程结构；
2. 用 `dynamic filter lower bound` 区分“支持删除”和“空间随当前 n”两种 dynamic；
3. 用 `dynamic succinct dictionary redundancy` 查 exact dictionary 后续；
4. learned/adaptive filter 只在模型交集明确时纳入，不因名字相近纳入。

## 4. 纳入与排除标准

### 纳入

- 研究 approximate membership、unknown-size/resizable filter、succinct dictionary 或直接使用本文技术；
- 有正式出版页、DOI 或可核查 arXiv 正文；
- 能说明与本文至少一个共同指标：容量、当前 `n` 空间、误报、时间、删除、模型。

### 排除

- 只在应用系统中顺带使用 Bloom filter；
- 只有搜索摘要或博客，找不到论文正文/正式元数据；
- “dynamic” 仅表示键值变化，但与 unknown size 没有可说明的关系；
- 只做 learned model 或 range filter，无法与本文 point membership 模型比较；
- 仅引用本文而无实质关系。

## 5. 怎样确认正式发表与是否引用本文

- 正式发表：优先查出版社页面 DOI，再用 DBLP 交叉核对；arXiv 单独标为预印本。
- 是否引用：必须在候选正文参考文献或引用段落找到本文，不使用搜索引擎的“相关”标签替代。
- 是否改进：必须找到候选自己的定理/实验目标，并逐项比较模型；引用本文不等于改进本文。

## 6. 怎样区分理论改进和应用/工程论文

理论改进至少应能对齐一个形式化保证，例如 bit 空间界、cell-probe/word-RAM 时间、失败概率或下界。工程论文可以在吞吐、缓存访问、删除、实现可行性上更强，但若没有相同模型中的空间/时间定理，只写成“工程对照或不同目标”。

## 7. 第一批候选

### C1. InfiniFilter: Expanding Filters to Infinity and Beyond

- 作者：Niv Dayan, Ioana O. Bercea, Pedro Reviriego, Rasmus Pagh
- 年份/位置：2023, Proceedings of the ACM on Management of Data 1(2)
- DOI：https://doi.org/10.1145/3589285
- 正式发表：是
- 是否引用本文：`待核验`（当前只确认其引用 PSW 2013）
- 研究问题：可无限扩展的 tabular/quotient-style filter，同时控制性能、FPR 与内存。
- 主要结果来源：正式摘要；理论与实验细节未读。
- 与本文关系：同样面对原 key 不可得时的扩容，但以可实现工程 filter 为中心；空间是否达到 Liu-Yin-Yu 的 bit-level unknown-size 上界待核。
- 是否真正改进本文：`待核验`，不可仅凭支持无限扩展宣布改进。
- 核验状态：`仅看摘要`

### C2. Aleph Filter: To Infinity in Constant Time

- 作者：Niv Dayan, Ioana-Oriana Bercea, Rasmus Pagh
- 年份/位置：2024, PVLDB 17(11): 3644-3656
- DOI：https://doi.org/10.14778/3681954.3682027
- 正式发表：是
- 是否引用本文：是；§6 “From Theory into Practice” 明确比较 Liu-Yin-Yu。
- 研究问题：无限扩展下让插入、查询、删除保持常数时间，并改善 memory-FPR tradeoff。
- 与本文的直接关系：正文称 Liu-Yin-Yu 在 `N` 与 `U` 多项式相关时给出 `log log N + O(log log log N)` overhead、whp 常数操作，但未证明删除且增长受 universe `U` 限制。
- 是否真正改进本文：在删除、无限增长和实践实现维度更强；是否在相同理论空间模型上改进，`否/不可直接比较`。
- 结论来源：摘要与 §6 相关工作段落；主算法定理尚未核。
- 核验状态：`已读相关章节`

### C3. Tight Cell-Probe Lower Bounds for Dynamic Succinct Dictionaries

- 作者：Tianxiao Li, Jingxun Liang, Huacheng Yu, Renfei Zhou
- 年份/位置：FOCS 2023, pp. 1842-1862
- DOI：https://doi.org/10.1109/FOCS57990.2023.00112
- arXiv：https://arxiv.org/abs/2306.02253
- 正式发表：是
- 是否引用本文：`待核验`
- 研究问题：动态 succinct dictionary 中每 key wasted bits 与操作时间的 cell-probe 下界。
- 摘要结果：当 `U=n^{1+Theta(1)}`，每 key 仅 `O(log^{(k)} n)` wasted bits 时，期望操作时间下界为 `Omega(k)`；带大 value 时给出更新下界。
- 与本文关系：属于本文 dictionary 结果的后续理论环境，但模型允许删除、空间参数和时间度量不同。
- 是否真正改进本文：下界而非直接上界改进；`待读正文后判断`。
- 核验状态：`仅看摘要`

### C4. Dynamic Dictionary with Subconstant Wasted Bits per Key

- 作者：Tianxiao Li, Jingxun Liang, Huacheng Yu, Renfei Zhou
- 年份/位置：SODA 2024, pp. 171-207
- DOI：https://doi.org/10.1137/1.9781611977912.9
- arXiv：https://arxiv.org/abs/2310.20536
- 正式发表：是
- 是否引用本文：`待核验`
- 研究问题：冗余总量 `R=o(n)` 的动态 dictionary。
- 摘要结果：当 `R >= n/polylog n`，操作时间 `O(log* n + log(n/R))`，并与相关下界匹配。
- 与本文关系：进一步探索 succinct dictionary 的极低冗余区间；不直接等于 unknown-size filter。
- 是否真正改进本文：指标和模型不同，`待核验/不可直接比较`。
- 核验状态：`仅看摘要`

### C5. Space Lower Bounds for Dynamic Filters and Value-Dynamic Retrieval

- 作者：William Kuszmaul, Stefan Walzer
- 年份/位置：STOC 2024, pp. 1153-1164
- DOI：https://doi.org/10.1145/3618260.3649649
- 正式发表：是
- 是否引用本文：`待核验`
- 研究问题：支持插入/删除、受容量 `n` 约束的 dynamic filter 的信息论空间下界。
- 摘要结果：证明 dynamic filter 相对静态 filter 的 `Theta(n)` 额外位是不可避免的；更精确常数需读正文。
- 与本文关系：同属 filter 下界，但这里的 dynamic 轴主要是 deletion，不是 unknown final size；可用于提醒读者两个“动态”问题不要混同。
- 是否真正改进本文：不是同模型的直接改进。
- 核验状态：`仅看摘要`

### C6. Resizable Retrieval

- 作者：William Kuszmaul, Aaron Putterman, Tingqiang Xu, Hangrui Zhou, Renfei Zhou
- 年份/位置：2026 arXiv 预印本
- arXiv：https://arxiv.org/abs/2606.15944
- 正式发表：否，当前仅确认预印本
- 是否引用本文：`待核验`
- 研究问题：让 retrieval 结构的空间按当前 key 数 `n` 而非容量 `N` 计算，并给出 filter 推论。
- 与本文关系：`resizable` 与 unknown-size 目标高度相近，且有 dynamic filter 推论；必须读正文后确定推论是否复用或改进本文。
- 是否真正改进本文：`候选，未证实`
- 核验状态：`仅看摘要`

## 8. 明确不在本轮下结论的方向

- learned Bloom filter：除非找到对 unknown capacity/当前 `n` 空间有形式化结果，否则暂不纳入主比较表。
- Prefix Filter、Vector Quotient Filter：可作性能或实现对照，但第一轮不声称改进 unknown-size 理论界。
- “最新/首次/最优”表述：没有正文定理和完整检索前一律不用。

## 9. 下一步核验顺序

1. 成员 C 人工使用 Google Scholar 的 “cited by” 核对 C1-C6 是否引用本文；
2. 精读 Aleph §6 和主结果，完成与本文的逐项同模型/异模型表；
3. 精读 C3/C4 的 related work 与定理，确认 dictionary 线的真实承接关系；
4. 精读 C5，明确 deletion-dynamic 与 resizable-dynamic 的下界差异；
5. C6 在正式发表前只保留为预印本候选。

成员 C 已于 2026-07-19 审核本轮内容，并确认其可作为第一轮过程记录。候选工作的事实状态仍以表内的“已核验/待核验”标记为准。
