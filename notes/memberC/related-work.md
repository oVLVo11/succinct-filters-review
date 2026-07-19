# 相关工作分类框架（第一轮）

- 日期：2026-07-19
- 负责人：陈戚（成员 C）
- 状态：分类与比较问题已建立；只有标成“已读相关章节”的内容可视为读过正文片段

## 使用规则

本文件不以“谁更快、谁支持删除”作单轴排名。每类都围绕本文的目标组合核查：

```text
空间随当前 n 变化
+ approximate membership 无漏报
+ 总误报率受控
+ 空间接近相应信息论下界
+ 操作具有可比较的最坏/期望/均摊保证
```

统一状态：`候选`、`仅看摘要`、`已读相关章节`、`已核查定理`、`已排除`。

## 1. 经典 Bloom filter 与 approximate membership

### 解决什么问题

Bloom filter 用位数组与多个哈希函数紧凑表示集合，支持插入和 approximate membership query。Carter 等人的 approximate membership testers 给出更一般的问题表述和空间下界基础。

### 与本文模型的比较

- 容量是否预知：经典参数设置通常需要预估要存的元素数，从而选择位数组大小和哈希函数个数。
- 动态插入：支持，直到接近设计容量；继续超额插入会提高误报率。
- 删除：经典 Bloom filter 不直接支持安全删除；counting 变体是另一模型。
- 空间：经典 Bloom filter 以 `n log(1/epsilon)` 为量级，但不是本文追求的 unknown-size 精确领先常数结果。
- 时间：每次执行与哈希函数个数相关；“常数”依赖怎样处理 `epsilon`，与本文 word-RAM 定理不能直接等同。
- 与本文关系：基础背景；Bloom 1970 未出现在原论文参考文献表，Carter et al. 是原论文 [8]。

### 当前核验

- Bloom 1970：仅核查正式元数据和摘要级问题；`仅看摘要`。
- Carter et al. 1978：已核查原论文引用 [8] 与正式摘要；`仅看摘要`。
- 待核验：经典最优哈希数、1.44 常数及其参数条件，不在本轮写入复杂度矩阵。

## 2. Dynamic / scalable Bloom filter

### 解决什么问题

Guo et al. 的 dynamic Bloom filter 与 Almeida et al. 的 scalable Bloom filter 都试图避免单个固定 Bloom filter 超容量：在需要时增加新的组件，并控制整体误报率。前者强调动态集合与网络应用，后者明确以“不预知最终元素数且保持最大误报率”为动机。

### 与本文模型的比较

- 容量是否预知：不要求一次知道最终总量，但每个组件仍有设计容量/阈值。
- 动态插入：支持。
- 删除：原始版本是否支持严格删除语义，`待核验`；不能由名字 “dynamic” 推断。
- 空间：依赖组件序列和误报预算；尚未核查是否以当前 `n` 达到 PSW unknown-size 下界。
- 查询：通常需检查多个组件；组件数如何随 `n` 增长需读正文后填写。
- 与本文关系：Scalable Bloom Filters 是原论文 [1]，Dynamic Bloom Filters 是 [16]；二者用于说明实际系统常只有粗容量估计。它们不是原论文声称的直接理论前作，直接前作是 PSW。

### 当前核验

- Almeida et al. 2007：正式出版摘要已读，确认“动态适应元素数并保证最大误报率”的目标；`仅看摘要`。
- Guo et al. 2006：摘要已读，确认通过标准 Bloom filter 组件数适应当前规模，且摘要说空间可接受需实际规模不要过度偏离预设阈值；`仅看摘要`。
- 具体空间、查询、删除格均保持 `待核验`。

## 3. Succinct dictionary 与 succinct membership

### 解决什么问题

目标是把 exact set representation 压到信息论最小空间附近，同时保留快速查询和更新。Raman-Rao 的结构是本文扩展数组模型和 PSW 黑盒构造的重要基础；Demaine et al.、Backyard Cuckoo Hashing、Bercea-Even 分别提供不同空间/最坏时间组合。

### 与本文模型的比较

- 容量是否预知：Raman-Rao 可使空间依赖当前 `n`，但更新为 expected amortized；其他结构是否可按当前 `n` succinct 地增长需逐篇核查。
- 动态插入/删除：Raman-Rao 摘要明确支持；不同论文模型不完全一致。
- 误报：dictionary 是 exact，不存在 `epsilon` 误报参数。
- 空间：信息论基准是表示 `n` 元子集所需的 `log binom(u,n)`，稀疏区近似 `n log(u/n)+O(n)`，不能直接与 filter 的 `n log(1/epsilon)` 比。
- 与本文关系：原论文 §1.2 明确讨论 [3]、[6]、[11]、[29]；本文的长串 prefix matching 结构与 dictionary 构造建立在这条技术线上。

### 当前核验

- Raman-Rao 2003：正式摘要已读；查询最坏 `O(1)`，更新 expected amortized `O(1)`，空间 `B+o(B)`；`仅看摘要`。
- Demaine et al. 2006：摘要已读；在 word RAM 中 `Theta(n log(u/n))` bits、每操作高概率常数时间，但是否满足本文“当前 n 的 leading-constant succinct”要求仍需正文；`仅看摘要`。
- Arbitman-Naor-Segev 2010：摘要已读；有 `(1+o(1))B` 变体和多项式操作序列上 whp 最坏常数操作；与 unknown-size 扩容关系待核；`仅看摘要`。
- Bercea-Even 2019/2020：摘要已读；fully dynamic、常数内存访问、支持删除；原论文指出直接扩展到当前 `n` 会有 `Omega(n log log u)` 加性项；`已读原论文相关章节`，尚未读其正文定理。

## 4. Dynamic hashing 与 deamortization

### 解决什么问题

这条线研究 exact dictionary 的哈希表示、碰撞处理以及怎样把一次昂贵 rebuild 拆成每次更新的有限工作。FKS 是静态最坏常数查询基点；dynamic perfect hashing 给出动态更新；real-time hashing、de-amortized cuckoo hashing 追求高概率最坏常数操作。

### 与本文模型的比较

- 容量/当前 `n`：线性“机器字”空间不自动等于 bit-level succinct，也不自动解决 unknown-size filter 的原 key 丢失。
- 插入/查询/删除：各工作保证不同，必须区分 static、expected amortized、worst-case whp。
- 与本文关系：技术背景和去均摊思想来源；不是 approximate membership 空间下界的直接竞争方案。

### 当前核验

- FKS [15]：仅按原论文 §1.2 记为静态 `O(n)` 空间、最坏常数查询；`已读原论文相关章节`。
- Dietzfelbinger et al. [12]：按原论文记为最坏常数查询、expected amortized 常数插入；`已读原论文相关章节`。
- Dietzfelbinger-Meyer auf der Heide [13]：按原论文记为高概率最坏常数更新；`已读原论文相关章节`。
- Arbitman-Naor-Segev [2]/[3]：前者去均摊 cuckoo，后者 succinct 表示；两者不能合并成同一个结果；`仅看摘要/原论文相关章节`。

## 5. Unknown-size filter

### 直接前作：Pagh-Segev-Wieder 2013

- 问题：元素在线到达，最终 `n` 未知，希望任一时刻的空间按当前规模计算。
- 容量是否预知：不预知最终大小。
- 插入：原论文转述为 expected amortized `O(1)`。
- 查询：原论文转述为 worst-case `O(1)`。
- 删除：本轮未见其作为主操作，`待核验`。
- 空间下界：原论文转述为
  `(1-o(1))n(log(1/epsilon)+(1-O(epsilon))log log n)`。
- 上界：原论文转述为 `(1+o(1))n log(1/epsilon)+O(n log log n)`（在相应规模条件下）。
- 与本文关系：最直接前作。Liu-Yin-Yu 的改进是 `log log n` 领先常数与去均摊的最坏时间保证。
- 状态：PSW 摘要已读，Liu-Yin-Yu 对其比较已读；PSW 下界定理尚未读，`仅看摘要`。

### 当前论文：Liu-Yin-Yu 2020

- 这是本项目主论文，不在比较表中用一句“更优”概括；应分别比较空间主项、预计算位、参数区间、操作语义和失败模型。
- 状态：`已核查定理`（Theorem 10/12）、证明细节未完成。

## 6. Adaptive filter

### 解决什么问题

Bender et al. 研究自适应查询：即使查询者根据过去回答选择下一查询，每个负查询仍需保持 `epsilon` 误报保证。这个“adaptive”描述的是 adversarial query history，而不是容量动态增长。

### 与本文模型的比较

- 容量是否预知：不是论文主要分类轴，`待核验`。
- 插入/删除：摘要说 AMQ 可支持更新，具体构造需看正文。
- 空间/时间：摘要声称本地组件低阶最优空间、查询与更新 whp 最坏常数；完整模型含远端字典，不能只截取这一句与本文比较。
- 与本文关系：原论文 [4]/[5]；为 adaptive prefixes 和 adversarial filter 背景。不是 unknown-size 的同义词。
- 状态：`仅看摘要`。

## 7. Quotient filter / cuckoo filter

### 解决什么问题

两者通常在紧凑哈希表中保存 fingerprint，以得到良好局部性、删除或工程吞吐。Quotient filter 可由 slot 地址与 remainder 组成 fingerprint；cuckoo filter 用两个候选桶和 cuckoo relocation。

### 与本文模型的比较

- 容量是否预知：基础结构通常按表容量和负载阈值设计；虽然可 resize，不等于空间满足 unknown-size 信息论界。
- 插入/查询：常见工程实现很快，但最坏情况、失败概率和 rebuild 语义必须查理论分析。
- 删除：二者常支持，但 deletion 是本文主定理没有提供的额外功能，而不是自动的理论优越性。
- 空间：实践 bits/key 与本文的渐近公式、预计算空间和参数模型不可直接横比。
- 与本文关系：原论文没有直接引用 quotient filter 或 2014 cuckoo filter；只能标为“原文未引用的工程/模型对照”。原文引用的是 cuckoo hashing 的去均摊工作。

### 当前核验

- Quotient filter：Bender et al. 2012 摘要已读，确认支持删除、动态 resize 和合并；`仅看摘要`。
- Cuckoo filter：Fan et al. 2014 论文首页/摘要已读，确认指纹哈希表、动态增删和实践比较；`仅看摘要`。
- 具体最坏时间、unknown-size 空间界：`待核验`。

## 8. 后续研究候选

本轮确认了三类候选，详细检索协议见 `post-2020-work.md`：

1. **直接工程后续**：InfiniFilter (2023)、Aleph Filter (2024)。Aleph 正文明确引用并比较 Liu-Yin-Yu；它增加删除与无限扩展，但模型和空间表述不同，不能直接写成全面改进。
2. **dynamic filter 下界**：Kuszmaul-Walzer (STOC 2024)。它的 “dynamic” 指支持插入/删除且有容量约束，与 unknown-size/resizable 不是同一轴，需防止术语误判。
3. **dynamic succinct dictionary**：Li-Liang-Yu-Zhou (FOCS 2023；SODA 2024)。研究 redundancy-time tradeoff，和本文 dictionary 线密切相关；是否直接引用、是否改进当前 `n` 结果尚待正文核验。

## 9. 第一轮评价问题，而非最终结论

- 理论价值：本文把 unknown-size filter 的领先常数与最坏时间保证结合，是对 PSW 两个开放方向的同时回答。
- 模型成本：`u^c` 输入无关预计算随机位、word RAM、extendable array、`n=omega(log u)` 等条件需要在评价中显式列出。
- 实现复杂度：多层哈希、adaptive prefixes、data blocks、后台重组和失败处理距离简单 Bloom filter 实现很远。
- 删除：filter 主定理不支持用户删除；后续工程 filter 在这一维更强，但不代表其空间下界结果更强。
- 待核验：作者是否公开实现；若无实现，不能把理论常数时间解释成实际吞吐优势。

## 10. 下一轮必须完成的核验

1. 精读 PSW 2013 的下界和上界定理；
2. 精读 Scalable Bloom Filter 的查询结构数、空间和 FPR 预算；
3. 精读 Aleph Filter §6 对本文的直接比较，并核对其定理而不只用摘要；
4. 从每篇 dictionary 后续论文正文确认是否引用 Liu-Yin-Yu；
5. 与成员 A 共同核对所有 `n/u/epsilon` 条件后，再把复杂度写入最终 Review。

成员 C 已于 2026-07-19 审核本轮内容，并确认其可作为第一轮过程记录。文献状态仍以本文件及来源清单中的证据等级为准。
