# 2020 年后相关工作核验矩阵（成员 C，第二轮）

- 核验日期：2026-07-21
- 负责人：陈戚（成员 C）
- 当前状态：**成员 C 已审核并纳入过程记录；不是 Review 正文**
- 目标：回答“哪些工作直接引用 Liu--Yin--Yu（LYY），它们改进了什么，以及模型是否真的可比”。

## 证据等级

- **E3**：阅读原论文全文中的定义、定理/推论和引用语境，并记录页码。
- **E2**：阅读原论文摘要/元数据，同时用另一篇后续原论文定位其关系；不能据此断言未见部分。
- **E1**：仅元数据或摘要，所有技术结论保留为待核验。

## 矩阵

| 候选工作 | 出版 / DOI / 原文 | 是否直接引用 LYY，语境 | 与 LYY 是否同一 unknown-size 模型 | 改进或研究维度 | 时间保证类型 | 关系判断与原文证据 | 等级 / 状态 |
|---|---|---|---|---|---|---|---|
| Dayan et al., **InfiniFilter** | PACM MOD 1(2), 2023, article 140；[DOI](https://doi.org/10.1145/3589285) | **本轮未取得可搜索的正式全文，不能判断是否直接引用** | 不完全相同：它是可实现的 quotient-filter 系结构，强调扩容、删改、吞吐和 FPR/内存权衡；LYY 是 word-RAM 理论保证 | 工程化无限扩展；变长 fingerprint；支持插入/查询/删除 | 摘要称性能稳定；本轮未核对最坏/期望/均摊定理 | InfiniFilter 摘要；Aleph §1（PDF p.1）把它列为前一代方案，并指出 void entries 可能导致查询/删除搜索多个表 | **E2 / 保留为工程直接后续，引用状态待原文** |
| Dayan, Bercea, Pagh, **Aleph Filter** | PVLDB 17(11), 2024, pp.3644--3656；[DOI](https://doi.org/10.14778/3681954.3682027)；[官方 PDF](https://www.vldb.org/pvldb/vol17/p3644-dayan.pdf) | **是**。§7（PDF p.12，正文 pp.3654--3655）称 LYY 操作为常数时间 whp、每项额外 `lg lg N + O(lg lg lg N)`（在 `N,U` 多项式相关时），但未显示支持删除，且增长受宇宙 `U` 限制 | 部分重叠但不相同：都研究未知增长与 AMQ；Aleph 允许删除和不受固定 `U` 的工程化无限扩展，并引入预测增长模式 | 删除、无限增长、FPR--内存权衡、可运行实现与实验 | 摘要/结论称所有操作 constant time；但 void duplicate 清理在 §5.2（PDF p.8）明确按生命周期 **amortized constant**，不能改写成 LYY 式 whp worst-case | §7（PDF p.12）明确列四项比较；Abstract（p.1）；§5.2（p.8） | **E3 / 高相关，允许进入后续研究证据池** |
| Li et al., **Tight Cell-Probe Lower Bounds for Dynamic Succinct Dictionaries** | FOCS 2023, pp.1842--1862；[DOI](https://doi.org/10.1109/FOCS57990.2023.00112)；[arXiv](https://arxiv.org/abs/2306.02253) | 待全文核验 | 不是同一问题：exact dynamic dictionary、cell-probe 冗余--时间下界；与 LYY 的 dictionary 结果相关，不是 filter 上界的直接替代 | 动态字典的 redundancy--update-time 下界 | 下界论文；不能把下界写成其数据结构的操作保证 | 出版元数据和摘要；Resizable Retrieval Theorem 4.5 复述其一个动态字典下界（PDF p.22） | **E1（另有后续论文转述）/ 保留为理论旁支** |
| Li et al., **Dynamic Dictionary with Subconstant Wasted Bits per Key** | SODA 2024, pp.171--207；[DOI](https://doi.org/10.1137/1.9781611977912.9)；[arXiv](https://arxiv.org/abs/2310.20536) | 待全文核验 | exact dynamic dictionary；不等于 LYY unknown-size filter | 次常数 wasted bits/key 的字典上界 | 摘要级，尚未核对 worst-case / expected / amortized 的精确条件 | DOI / arXiv 元数据；尚未读取关键定理 | **E1 / 不进入正文结论** |
| Kuszmaul, Walzer, **Space Lower Bounds for Dynamic Filters and Value-Dynamic Retrieval** | STOC 2024, pp.1153--1164；[DOI](https://doi.org/10.1145/3618260.3649649)；[KIT PDF](https://publikationen.bibliothek.kit.edu/1000183467/162992578) | **是**。§1（PDF p.3）在“可任意增长的 incremental filter”最优空间式中以 [28] 引用 LYY | **不是同一模型**：该文 dynamic filter 允许插入与删除，`n` 是任一时刻集合大小的容量上界；LYY 主过滤器只处理插入序列且最终大小未知 | 证明删除型 fully dynamic filter 相比静态过滤器必须有线性冗余 | 信息论空间下界，**与运行时间无关** | 定义在 PDF p.1；主结论 p.1；Theorem 3.1（p.4）在其参数区间给出超过 `0.35n-o(n)` 的线性额外空间；LYY 引用在 p.3 与 references p.12 | **E3 / 高相关但必须标“删除动态、容量约束”** |
| Kuszmaul et al., **Resizable Retrieval** | [arXiv:2606.15944v1](https://arxiv.org/abs/2606.15944), 2026-06-14；**预印本，未核验正式发表** | **是**。Introduction（PDF pp.2--4）把 LYY/PSW 作为 extendable filters 前作；references [LYY20]；讨论能否直接扩展它们得到当前 `n` 的过滤器界 | 更强但参数不同：支持插入/删除，空间按当前 `n`；同时引入 `U/n`、`U^δ` 哈希空间和“时间 whp in n”等条件，不能说无条件支配 LYY | resizable retrieval；由 retrieval 导出动态 filter；当前规模空间；匹配型下界 | Corollary 3.14：constant-time operations **with high probability in `n`** | Theorem 1.1（PDF p.2 / p.20）；Corollary 3.14（pp.20--21）给 `n log(1/ε)+O(n log log(U/n))+polylog U+O(U^δ)` bits；支持当前 `n` 下的动态过滤器 | **E3 / 最直接新进展，但只能按预印本引用** |

## 三项全文核验后的可用结论

1. **没有单一“后作全面取代 LYY”的结论。** Aleph 更偏可实现的无限扩展与删除；STOC 2024 研究删除型 dynamic filter 的信息论下界；Resizable Retrieval 把空间参数推进到当前 `n`，但保证、额外项和随机模型均与 LYY 不同。
2. **“dynamic”至少有三种含义，正文必须拆开。** LYY/PSW 的未知最终插入规模、容量固定但支持删除的 fully dynamic filter，以及空间按当前规模收缩的 resizable 结构，不能混成同一列。
3. **时间措辞要逐篇保留。** LYY 是无 failure 条件下的 worst-case `O(1)`；Aleph 的公开摘要说 constant time，但部分删除清理分析是 amortized；STOC 2024 下界不依赖时间；Resizable Retrieval 是 operations constant-time whp in current `n`。

## 人工复核清单

- [ ] 成员 C 打开 Aleph PDF p.12，确认对 LYY 的四项比较没有被矩阵夸大。
- [ ] 成员 C打开 STOC 2024 PDF pp.1、3--4，能口头说明 incremental 与 dynamic 的区别。
- [ ] 成员 C 打开 Resizable Retrieval v1 PDF pp.2、20--21，复算 Corollary 3.14 的各空间项。
- [ ] 若最终采用 InfiniFilter，补取正式全文并搜索 LYY / Liu / unknown sizes，不能以“未搜到”代替“不引用”。
- [ ] Li 2023/2024 未完成全文核验前，不写进 Review 的确定性比较句。
