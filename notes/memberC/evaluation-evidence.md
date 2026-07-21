# 优点、局限、适用条件与未来方向：证据清单（成员 C，待审）

- 日期：2026-07-21
- 状态：**待成员 C 审核；仅供后续人工组织观点，不是 Review 正文**
- 规则：每条先写可核验事实，再写允许形成的判断；没有原文位置的句子不得升级为最终论断。

## 可据证据讨论的优点

| 编号 | 可核验事实 | 证据位置 | 可形成的审慎判断 |
|---|---|---|---|
| S1 | Theorem 10 同时给未知插入规模、无 FN、FP 至多 `ε`、无 failure 时插入/查询 worst-case `O(1)`，并给整段插入序列的 failure 概率界 | LYY Theorem 10（仓库主论文 PDF p.9） | 贡献的非凡之处是**组合保证**，而非任一单项首次出现 |
| S2 | 空间主项随当前插入数 `n`，并出现 unknown-size 下界要求的 `n log log n` 量级项 | LYY Theorem 10；PSW Theorem 3.1；A 的 `lower-bound-notes.md` | 在对应 insertion-only unknown-size 模型里，主项与已知下界对齐 |
| S3 | Claim 13 通过相邻层 `D/T`、增量迁移和固定轮维护，把扩容工作拆到每次插入 | LYY Claim 13；B 的构造笔记与伪代码 | 直觉亮点是“只查常数个相邻结构，同时后台搬迁”，可作为技术讲解主线 |
| S4 | 论文把 prefix matching 黑盒继续实现到数据块编码，目标不仅是存在性上界，还保留最坏常数操作 | LYY §5；A/B 依赖图 | 证明工程复杂，但组合了 succinctness 与 deamortization 两类困难 |

## 局限与适用条件

| 编号 | 事实 / 条件 | 证据位置 | 正文可写边界 |
|---|---|---|---|
| L1 | 主过滤器接口没有用户删除操作；保证针对插入序列 | LYY Theorem 10；Aleph §7（PDF p.12）明确称尚未显示支持删除 | 不适合直接宣称解决 fully dynamic 集合 |
| L2 | 数据结构可报告 failure；正确性和时间保证以未 failure 为条件，整段失败概率至多 `u^{-C}` | LYY Theorem 10.3--10.4 | “whp 成功的数据结构”不等于完全确定性结构 |
| L3 | 空间式含 `u^c` 预计算随机比特/表，且正式定理有 `n=ω(log u)` 等参数范围 | LYY Theorem 10；A 的参数表 | 小规模 `n` 或超大 `u` 下，不能只展示每 key 主项 |
| L4 | 核心实现和 failure 事件分散在 Claim 13 与 §5 多层编码中；字面常数 10 和阶段下标在小组复核中仍有解释缺口 | `discussions/issues/issue-constant-10.md`；`issue-stage-index.md` | Review 必须区分论文原命题、讲解直觉与小组尚未闭合的复算 |
| L5 | 后续删除型 dynamic filter 存在线性额外空间下界；这是不同模型，不能反向说 LYY 空间式错误 | Kuszmaul--Walzer 2024, Theorem 3.1（PDF p.4） | 删除能力改变信息论约束，是适用边界而非对 LYY 的否定 |

## 后续工作带来的评价修正

| 后作 | 对 LYY 的补充或修正 | 证据 |
|---|---|---|
| Aleph Filter (2024) | 说明实践导向方案可加入删除和不受固定宇宙限制的扩展，但其 FPR/内存与时间分析口径不同 | Aleph Abstract、§5.2、§7 |
| Space Lower Bounds for Dynamic Filters (2024) | 说明 fully dynamic（插入+删除）过滤器相对静态最优需要 `Ω(n)` 冗余；不能用 insertion-only 的界直接推断删除模型 | STOC 2024 pp.1、4 |
| Resizable Retrieval (2026 preprint) | 把空间界推进为按当前 `n`，并给 dynamic filter 推论；同时带 `O(n log log(U/n))`、哈希函数空间和 whp-in-`n` 条件 | Theorem 1.1、Corollary 3.14 |

## 可讨论的未来方向（不能写成论文已解决）

1. 在保留可核验最坏时间口径的同时支持删除，并明确空间是否按当前 `n`、历史峰值 `n_max` 或固定容量计。
2. 降低或消除 `u^c` 级全局随机性/预计算项，并给出更贴近实现的常数。
3. 将 Claim 13 和 §5 的多层结构转化为可复现实验实现，测量迁移峰值与 cache / I/O 行为。
4. 对 adaptive query / adaptive adversary 给出明确模型；当前小组未找到 LYY 对该术语的直接承诺。
5. 对 2026 Resizable Retrieval 的 filter 推论进行正式发表状态与后续版本核验，避免引用 v1 后公式变更。

## 成员 C 审核问题

- [ ] 我能否用自己的话解释“组合保证”为什么比单纯 `O(1)` 查询更强？
- [ ] 我能否解释 LYY、deletion-dynamic、resizable-current-`n` 三个模型的差别？
- [ ] 我是否同意把 L4 作为 Review 的方法论局限，而不是武断地说原论文有错误？
- [ ] 最终每条评价是否至少保留一个原文定位，并删除所有无法口头解释的句子？
