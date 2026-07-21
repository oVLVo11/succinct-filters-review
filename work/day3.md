# Day 3 工作分配：补齐入口条件，拆解核心技术和基础构造

日期：2026-07-21  
角色不变：A 刘威（问题模型、理论背景与下界）；B 张书铖（核心技术、实现与正确性）；C 陈戚（相关研究、后续研究与总体评价）。

## 一、与 Day 1、Day 2 的衔接

Day 1、Day 2 已形成的可用基础包括：

- 刘威已完成正式模型、Theorem 1/10 参数差异、空间下界疑问和概率语义的阶段性整理；
- 张书铖已完成构造路线、变长前缀、四个活跃结构、8 元素教学示例及两份流程图文字稿；
- `discussions/questions.md` 已把 Claim 13、常数 10、底层 `D(m, ell)`、空间峰值和 failure 分析等问题分成 Q1—Q3；
- `discussions/meeting-day2.md` 已记录 A、B 的阶段性结论和待复核点。

但 Day 2 的入口条件尚未全部满足：陈戚负责的个人阅读笔记、经典文献矩阵、来源清单、BibTeX、AI 日志和对 B 示例的交叉审阅仍缺失；A 对 C 文献矩阵的审阅也因此无法执行。Day 3 不把欠账掩盖为“已完成”，而是采用以下顺序：

1. C 先补齐 Day 1/2 的资料入口和经典文献矩阵；
2. A、B 在不依赖该矩阵的技术部分继续精读；
3. C 交付矩阵后，A 立即完成模型可比性审阅；
4. 三人共同确认入口条件后，再把 Day 3 标记为正式完成。

今天仍以“理解和验证”为主，不写完整 Review 正文，也不把 AI 输出直接拼入草稿。

## 二、Day 3 共同目标

1. 将论文构造拆成可独立解释、可定位原文、可相互验证的技术组件；
2. 建立从底层 dictionary 到 unknown-size filter 的证明依赖图；
3. 补齐并核验经典相关工作资料，形成 2020 年后研究的候选清单；
4. 集中处理 Day 2 遗留的 Q1/Q2/Q3，尤其是 Claim 13、`D(m, ell)` 和常数 10；
5. 留下个人笔记、会议记录、交叉审阅、Issue、AI 使用记录和分阶段提交。

## 三、成员 A：刘威

### 1. 主任务：引理依赖、空间分解与随机性假设

精读 Theorem 10、Lemma 11、Claim 13 以及它们引用的底层 dictionary 结果。新建 `notes/memberA/lemma-dependency-and-space.md`，至少完成：

1. 按“底层接口 → 中间引理 → filter 主定理”列出证明依赖；
2. 对每个引理记录：前提、结论、在最终证明中的用途、原文页码/章节；
3. 分解总空间中的：
   - `n log(1/epsilon)`；
   - `n log log n`；
   - `O(n log log log u)`；
   - `u^c` 预计算空间；
   - truth table、元数据和新旧结构并存的开销；
4. 标明哪些是主项、低阶项或输入无关预计算项，以及各自成立的参数范围；
5. 核查哈希随机性、独立性、操作序列和 oblivious adversary 假设；找不到明确表述时标为 Q3，不得自行补充假设；
6. 继续核查 PSW 下界，但只写可由原文支持的证明骨架和编码直觉，未读懂的步骤保留为 Q1/Q2。

### 2. 承接 Day 2 的修补任务

- 正式复核张书铖的 8 元素示例，确认其能否作为教学例子；
- 复核 Claim 13 中 `i=ceil(log n)` 与阶段区间的下标边界；
- 陈戚提交文献矩阵后，检查其中容量假设、空间界和时间保证是否与本文模型可比。

### 3. 当日产物与提交节奏

- `notes/memberA/lemma-dependency-and-space.md`；
- 更新 `notes/memberA/lower-bound-notes.md`；
- 参与 `figures/proof-dependency.md`；
- 在 `discussions/questions.md` 更新相关 Q1/Q2/Q3 状态；
- 更新 `ai-usage/member-A-log.md`（如未使用 AI，也明确记录）。

建议至少两个有效提交：

```text
proof(A): map lemma dependencies and randomness assumptions
proof(A): decompose space bound and review stage boundaries
```

## 四、成员 B：张书铖

### 1. 主任务：逐组件拆解核心构造

新建 `notes/memberB/core-components.md`。按照论文逻辑，而非仅按已有示例，分别解释：

1. 哈希表示；
2. 变长前缀存储；
3. prefix matching；
4. 分阶段增长；
5. `D_{i-1}, D_i, T_{i-1}, T_i` 的组织；
6. 新旧结构并存；
7. 长串、短串的迁移去向；
8. destroy、initialize 与 decrement/迁移工作的去均摊化；
9. 最坏情况 `O(1)` 的工作量控制；
10. filter 如何建立在底层 dictionary `D(m, ell)` 之上。

每个组件必须使用同一模板：输入/输出、保存的信息、解决的问题、缺失时的后果、依赖的接口或假设、原文位置、当前理解状态（已核实/Q1/Q2/Q3）。

### 2. 重点攻关 Day 2 遗留问题

- 用严格阶段区间重写 Claim 13 的状态不变式，避免 `ceil(log n)` 边界歧义；
- 拆解常数 10 的配平：每个阶段最多需要多少 decrement、destroy、initialize 调用，以及为什么能在下一阶段前完成；
- 定义底层 `D(m, ell)` 的接口、core set、长字符串 prefix matching 的处理方式；
- 区分“教学示例表现出的直觉”和“证明 worst-case/空间/概率保证所需的正式论证”；
- 在无法从原文推出常数或接口细节时，明确列为 Q3。

### 3. 图示和 Issue

- 新建或修订 `figures/architecture.md`，展示 filter、`D/T` 子结构和底层 dictionary 的关系；
- 修订 `figures/query-insert-flow.md`，使每个流程节点能链接到 `core-components.md` 的对应小节；
- 创建至少一个具体 Issue，例如“Claim 13 中常数 10 的配平如何逐项成立”，写明原文位置、当前推导和验收条件。

### 4. 当日产物与提交节奏

- `notes/memberB/core-components.md`；
- 修订 `notes/memberB/construction-notes.md` 与两份图示；
- 与 A 共同完成 `figures/proof-dependency.md`；
- 更新 `discussions/questions.md` 和 `ai-usage/member-B-log.md`。

建议至少两个有效提交：

```text
notes(B): decompose dictionary and filter components
proof(B): formalize stage invariant and migration schedule
figures(B): connect architecture and operation flow
```

## 五、成员 C：陈戚

### 1. 第一优先级：补齐 Day 1/2 前置欠账

在开始后续研究前，分批提交以下文件：

- `notes/memberC/paper-reading.md`；
- `notes/memberC/related-work.md`；
- `notes/memberC/post-2020-work.md`（先标候选/待核查）；
- `references/source-list.md`；
- `references/bibliography.bib`；
- `references/literature-matrix.md`；
- `ai-usage/member-C-log.md`。

经典文献矩阵至少覆盖 Bloom filter、dynamic Bloom filter、scalable Bloom filter、quotient filter、cuckoo filter、succinct dictionary 和 PSW unknown-size filter。复杂度、容量假设和删除支持必须回到原论文或正式出版页面核查，并记录页码、定理或章节。

### 2. 主任务：2020 年后研究候选检索

完成前置欠账后，沿两条路线检索：

1. 明确引用《Succinct Filters for Sets of Unknown Sizes》的论文；
2. 研究同一或高度相近问题、但未引用本文的工作。

在 `notes/memberC/post-2020-work.md` 中为每个候选记录：标题、作者、年份、发表状态、正式入口、摘要层面的主要结果、与本文关系、是否引用本文、当前核查深度和下一步。不得仅凭搜索摘要或 AI 输出填写技术结论。

候选按以下标签分类：直接后续、相邻理论、工程实现/实验、应用论文、排除项。至少形成 5 个值得 Day 4 读正文核查的候选；若不足 5 个，应如实记录检索式、引用网络和“未发现”的证据，不凑数。

### 3. 交叉审阅与 Issue

- 补做对张书铖 8 元素示例及增长图的正式审阅，至少 2 条实质性意见；
- 阅读 B 的 `core-components.md`，从未读过论文者视角指出至少 2 个断点；
- 创建至少一个具体 Issue，例如“哪些 2020 年后论文直接引用并实质扩展本文结果”，列明候选和核验标准。

### 4. 当日产物与提交节奏

由于存在前置欠账，建议至少三个有效提交：

```text
notes(C): restore related-work notes and verified source map
refs(C): complete classic-filter literature matrix
refs(C): add post-2020 candidate studies with verification status
```

## 六、共同任务与交叉审阅

### 1. 证明依赖图

A 主持、B 补充，新建 `figures/proof-dependency.md`，至少表示：底层 dictionary 接口、Lemma 11、Claim 13、Theorem 10，以及无漏报、误报率、空间、时间和 failure 保证之间的依赖关系。图中每条边必须有一句文字解释。

### 2. 问题清单

三人共同更新 `discussions/questions.md`：

- 已用原文核实的移入 Q0；
- 有推导但待复核的保留 Q1；
- 未理解的核心机制保留 Q2；
- 原文省略或接口未展开的列 Q3；
- 表述冲突列 Q4，并写出双方版本和裁决所需证据。

所有 Q2、Q4 必须指定负责人、复核人和 Day 4/Day 5 截止点。

### 3. 审阅链

- 张书铖审阅刘威的引理依赖和随机性假设；
- 陈戚审阅张书铖的组件说明和流程图；
- 刘威审阅陈戚的文献矩阵和模型可比性。

每人至少留下 2 条可追溯、可回应的评论，记录被审文件/小节、证据缺口、修改建议和处理结果。

## 七、Day 3 会议与过程记录

新建 `discussions/meeting-day3.md`。由三人轮流讲解，不直接复制个人笔记：

1. B 用 10 分钟从 key 讲到 prefix、`D/T`、迁移和底层 dictionary；
2. A 用 8 分钟解释依赖图、空间各项和概率/对手假设；
3. C 用 8 分钟解释经典矩阵中哪些方案与本文模型真正可比，并报告后续候选；
4. 三人共同逐项处理 Q2/Q4；
5. 每人复述一项非本人负责内容，记录错误和纠正。

当天每人至少 2 个有效 commit；C 因补欠账建议至少 3 个。每人更新 AI 日志并及时推送到各自分支，主要文件通过 PR 审阅，避免当天末尾一次性上传。

## 八、Day 3 验收与 Day 4 入口

### 文件验收

- [ ] A 完成引理依赖、空间分解和随机性假设笔记
- [ ] B 完成十个核心组件说明和阶段不变式初稿
- [ ] C 补齐 Day 1/2 文件并完成经典矩阵
- [ ] C 形成带核查状态的 2020 年后候选列表
- [ ] 完成证明依赖图和第一版体系结构图
- [ ] 至少创建两个具体 GitHub Issue
- [ ] 完成 Day 3 会议记录、交叉审阅和 AI 日志
- [ ] 三人均有分阶段 commit 和公开远程历史

### 理解验收

- [ ] 三人都能解释 filter 为什么要化为变长 prefix matching
- [ ] 三人都能说明为何只查询常数个活跃结构
- [ ] A、B 能说明常数后台工作如何与阶段长度配平；若尚未证明，能准确指出缺口
- [ ] C 能区分直接后续研究、相邻研究和仅工程相关工作
- [ ] 每个关键公式、复杂度和文献判断都能回到原文核查

只有在底层接口、阶段不变式、证明依赖和经典文献矩阵均形成可审阅版本后，Day 4 才进入系统证明表和伪代码级说明。
