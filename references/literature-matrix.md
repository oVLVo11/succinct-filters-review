# 文献比较矩阵（第一轮）

- 日期：2026-07-19
- 负责人：陈戚（成员 C）
- 规则：`待核验` 不得在后续改写时自动变成肯定结论。

| 工作 | 年份 | 问题模型 | 容量是否预知 | 插入 | 查询 | 删除 | 空间 | 误报模型 | 最坏情况保证 | 与本文关系 | 核验状态 | 证据位置 |
|---|---:|---|---|---|---|---|---|---|---|---|---|---|
| Bloom filter | 1970 | approximate membership | 通常预先按目标 `n` 设参 | 支持 | 与哈希数有关 | 原版不支持 | `Theta(n log(1/epsilon))` 量级，常数非本文最优目标 | 无 FN；FP 由参数控制 | 待核验 | 基础背景；原文未直接引用 | 仅看摘要 | DOI 出版元数据 |
| Carter et al. | 1978 | exact / approximate membership testers | 固定集合规模模型 | 待核验 | 待核验 | 待核验 | 原论文用作 `N log(1/epsilon)` 下界来源之一 | 一侧错误 | 待核验 | 理论基础，[8] | 仅看摘要 | 原论文 79:2；正式摘要 |
| Scalable Bloom Filters | 2007 | 可增长 Bloom filter 组件序列 | 最终容量不预知；单组件有初始容量，需选增长因子 `s` | 支持；满后新增组件 | 测试每个现有组件；指数增长时组件数为 `O(log n)` | 原始 SBF 未给删除操作 | 相对最终规模静态 BF 为常数因子波动；不是本文的信息论空间式 | 无 FN；以 `P_i=P_0r^i` 使总体 FP 有预设上界 | 未给随 `n` 无关的最坏常数查询 | 满足未知最终规模与固定 FP，但不满足本文全部组合保证，[1] | 已读原文相关章节 | §4-5，PDF pp.4-8 |
| Dynamic Bloom Filters | 2006 | `s` 个等参数 Bloom filter 组成动态集合 | 最终规模不固定；每个组件使用预定义 `m,k,n_0` | 平均 `O(k)` | 平均 `O(k(s+1)/2)` | 原始 DBF 算法未给删除操作 | `s*m` bits；仅在规模估计偏差不大时称可接受 | 无 FN；式 (3) 的 FP 随组件数增长 | 论文给平均复杂度，不是本文的 worst-case `O(1)` | 动态工程对照，不保持固定总体 `epsilon`，[16] | 已读原文相关章节 | §III、式 (3)、Algorithms 1-2，PDF pp.3-6；结论 p.12 |
| FKS perfect hashing | 1984 | static exact membership | 静态 `n` 已知 | 不支持动态 | `O(1)` worst-case | 不支持动态 | `O(n)` words（原论文转述） | 无误报 | 查询最坏 `O(1)` | 静态时间基点，[15] | 已读主论文相关章节 | 79:3 §1.2 |
| Raman-Rao | 2003 | dynamic exact dictionary | 空间可随当前 `n` | expected amortized `O(1)` | worst-case `O(1)` | 摘要支持，expected amortized | `B+o(B)` | exact | 更新不是最坏 | PSW 黑盒与内存模型，[29] | 仅看摘要 | 原论文 79:2/79:4；正式摘要 |
| Deamortized/Backyard cuckoo hashing | 2009/2010 | dynamic exact dictionary | 待核验 | worst-case `O(1)` whp | worst-case `O(1)` whp | 待核验 | 2010 摘要有 `(1+o(1))B` 变体 | exact | 多项式序列 whp | 去均摊与 succinct 背景，[2]/[3] | 仅看摘要 | 79:4；arXiv:0912.5424 |
| Pagh-Pagh-Rao | 2005 | 已知容量 succinct filter | 已知 `N` | expected amortized `O(1)` | `O(1)` | 摘要支持 | `(1+o(1))N log(1/epsilon)`（原论文转述） | 一侧错误 | 更新为均摊期望 | 已知容量最优对照，[27] | 仅看摘要 | 79:2/79:4；SODA 摘要 |
| Pagh-Segev-Wieder | 2013 | unknown-size filter | 否 | expected amortized `O(1)`（本文转述） | worst-case `O(1)`（本文转述） | 待核验 | 下界与 `n(log(1/epsilon)+O(log log n))` 上界 | 无 FN；FP `epsilon` | 另有多空间的 whp 最坏版本 | 最直接前作，[28] | 仅看摘要 | 79:2-79:5；PSW 摘要 |
| Liu-Yin-Yu | 2020 | unknown-size filter | 否 | worst-case `O(1)` | worst-case `O(1)` | 用户删除不支持 | `n(log(1/epsilon)+log log n+O(log log log u)) + u^c` | 条件于无 failure，FP ≤ `epsilon`；无 FN | ever-failure ≤ `u^{-C}` | 本项目主论文 | 已核查定理 | Theorem 10, 79:9 |
| Liu-Yin-Yu dictionary | 2020 | unknown-size exact key-value dictionary | 否 | worst-case `O(1)` | worst-case `O(1)` | 主定理未列 | `n(log(u/n)+v+O(log log log u)) + u^c` | exact，条件于无 failure | ever-failure ≤ `u^{-C}` | 本文第二主结果 | 已核查定理 | Theorem 12, 79:11 |
| Adaptive filter (Bender et al.) | 2018 | 对历史查询自适应的 AMQ | 待核验 | 摘要称更新 whp 最坏常数 | 摘要称 whp 最坏常数 | 待核验 | 本地组件 lower-order optimal（完整系统待核） | 每次查询对历史保持 `epsilon` | 摘要级 | 不同的“adaptive”轴，[5] | 仅看摘要 | arXiv 摘要；79:4 |
| Quotient filter | 2012 | fingerprint AMQ / 外存友好 | `m=2^q` 个槽并依赖负载率；可由 fingerprint 恢复而 resize | 支持；需移动 cluster | 扫描 cluster；平均 cluster `O(1)` | 支持 | 每槽 `r+3` bits，FP 至多约 `2^{-r}`；空间取决于负载 | 一侧错误 | 最长 cluster 受概率界控制，但不是本文的确定最坏常数保证 | 原文未引用的工程对照；resize/删除不等同本文模型 | 已读原文相关章节 | PVLDB §3-4，PDF pp.1-6 |
| Cuckoo filter | 2014 | 两候选桶 fingerprint AMQ | 固定桶数 `m`、桶容量 `b` 和目标负载；需留空槽 | 支持；递归 relocation 可能失败 | 查询两个桶 | 支持 | 实用配置按 `alpha` 计 bits/item；partial-key 失败分析要求 `f=Omega(log(n/b))` | 一侧错误 | 原文以实验和部分失败分析为主，不能写成无条件最坏常数 | 原文未引用的工程对照；删除/吞吐是不同评价轴 | 已读原文相关章节 | CoNEXT §1、§4-5，式 (3)，PDF pp.1、6-7 |
| InfiniFilter | 2023 | 无限扩展 tabular filter | 最终容量不预知 | 支持 | 会随辅助表增长，细节待核 | 支持情况待核 | memory-FPR tradeoff，公式待核 | 一侧错误 | 待核验 | 后续工程候选 | 仅看摘要 | DOI 摘要 |
| Aleph Filter | 2024 | 无限扩展、支持删除的 filter | 可无限增长；预测模式可给估计 | 论文称常数 | 论文称常数 | 支持 | 与静态 filter 的 memory-FPR 权衡，非本文同一公式 | 一侧错误 | 定理细节待核 | 明确引用本文；不同维度增强 | 已读相关章节 | PVLDB 摘要、§6 |
| Li et al. lower bound | 2023 | dynamic succinct dictionary cell-probe 下界 | 容量参数为 `n` | 更新下界 | 操作下界 | 支持动态 | wasted bits `O(log^(k)n)`/key | exact | expected `Omega(k)` 下界 | 后续 dictionary 理论 | 仅看摘要 | FOCS/arXiv 摘要 |
| Li et al. subconstant waste | 2024 | dynamic exact dictionary | 容量/当前规模关系待核 | `O(log* n+log(n/R))` 摘要级 | 同左 | 摘要称动态 | 总冗余 `R=o(n)` | exact | 摘要级 | 后续 dictionary 上界 | 仅看摘要 | SODA 出版摘要 |
| Kuszmaul-Walzer | 2024 | 支持插入/删除、容量 `n` 的 dynamic filter | 有容量约束 | 支持 | 时间不作为下界条件 | 支持 | `n log(1/epsilon)+Omega(n)` 下界（摘要级） | 一侧错误 | 与时间无关的空间下界 | deletion-dynamic，不同于 unknown-size | 仅看摘要 | STOC 出版摘要 |
| Resizable Retrieval | 2026 | 空间随当前 `n` 的 retrieval/filter 推论 | 否 | 摘要称支持 | 摘要称支持 | 摘要称支持 | 摘要给 retrieval 界；filter 推论待核 | 待核验 | 待核验 | 高相关预印本候选 | 仅看摘要 | arXiv:2606.15944 |

## 矩阵回答的当前结论

第一轮没有发现一个已核查工作可以在同一模型下同时替代本文的全部组合保证。Aleph/InfiniFilter 更接近可实现的无限扩展与删除；后续 succinct dictionary 研究更精细的冗余-时间权衡；STOC 2024 的 dynamic filter 下界主要研究删除。因此最终 Review 应做多维比较，而不是给出单一“最好”排名。

这一结论仍是检索阶段判断，须由成员 C 阅读各候选正文后复核。
