# Day 5 工作分配：三个主体章节初稿与第三轮交叉审阅

> **完成状态（2026-07-30）**：A/B/C 三章均已入库并完成交叉回应，已合入 `review-integrated.md`；本文件以下内容作为原计划和验收轨迹保留。

计划日期：Day 4 验收后执行  
角色：A 刘威；B 张书铖；C 陈戚。

## 一、Day 5 入口与写作边界

Day 4 已形成 A 的概率/空间核查、B 的伪代码与时间证明框架、C 的后续研究矩阵，以及共同证明表。Day 5 开始写主体章节，但不是把过程笔记直接拼成终稿。

进入写作前共同确认：

- `notes/proof-table.md` 六行均有原文位置、条件和当前缺口；
- Q2、Q4 已关闭，或明确标为阻塞项；
- 阶段下标、字面常数 10、位级空间峰值、data block 冗余细节和自适应对手口径仍按 Q1/Q3 处理；
- C 的 E1/E2 文献不得写成正文中的确定技术结论；
- AI 生成文字不得直接作为章节正文，章节作者须依据个人笔记和原文自行组织、逐句核查。

## 二、共同目标与文件约定

1. 分别完成“问题与重要性”“核心技术与实现”“相关研究与评价”三个可审阅初稿；
2. 每个关键结论标明证据来源，区分论文命题、小组解释和未关闭缺口；
3. 统一符号、术语、概率口径和时间口径；
4. 每人完成第一审阅和第二核查各一次；
5. 形成引用与事实待核查清单，为 Day 6 整合提供入口。

建议新建：

```text
drafts/section-A-problem-and-significance.md
drafts/section-B-technique-and-proof.md
drafts/section-C-related-work-and-evaluation.md
discussions/review-day5.md
discussions/fact-check-day5.md
discussions/meeting-day5.md
```

章节文件统一在开头记录作者、版本、引用依据、未关闭问题；正文中的数学符号首次出现必须定义。

## 三、成员 A：刘威

### 1. 主任务：问题、结果、下界与重要性章节

新建 `drafts/section-A-problem-and-significance.md`，至少包含：

1. approximate membership 的背景与典型需求；
2. dictionary、filter、false positive、false negative、`[u]`、`S`、`n`、`ε` 的正式定义；
3. “unknown size” 未知的究竟是什么；
4. 为什么 filter 不能像 exact dictionary 那样直接枚举旧 key 后扩容；
5. Theorem 1 与 Theorem 10 的精确结果、参数范围及差异；
6. PSW 下界的命题、证明直觉及其与本文上界的关系；
7. 为什么 `n log log n` 是理论成本而非普通实现浪费；
8. 本文在领先常数、worst-case 时间和当前规模空间方面的重要性；
9. 至少一段限制说明：`ε=o(1)`、`n` 范围、`u^c` 预计算空间、无 failure 条件。

写作要求：不得把式 (2) 的上界直觉当作 PSW 下界证明；不得把 Theorem 1 的 `n>u^0.001` 写成 Theorem 10 的正式条件。

### 2. 审阅职责

- 第一审阅 B 的正确性、概率和复杂度段，检查结论是否与共同证明表一致；
- 第二核查 C 对“最优”“改进”“同一模型”的表述；
- 对 B 至少提出 5 条实质性评论，其中必须包含一个逻辑跳跃、一个缺少来源处和一个普通读者断点。

### 3. 建议提交节奏

```text
draft(A): write problem model and main results
draft(A): explain lower bound and research significance
review(A): audit technique proof and comparison claims
```

## 四、成员 B：张书铖

### 1. 主任务：技术、实现与证明章节

新建 `drafts/section-B-technique-and-proof.md`，至少包含：

1. 从 filter 到随机哈希前缀集合的技术总览；
2. 变长前缀、逐阶段误报预算和 prefix matching 的直觉；
3. `D_{i-1},D_i,T_{i-1},T_i` 的职责与生命周期；
4. 新键写入、短串/长串迁移、初始化和销毁；
5. 查询为何只访问常数个结构；
6. 插入如何用后台常数轮工作去均摊化；
7. 无 false negative 的写入、迁移和查询覆盖不变式；
8. 误报率、failure、时间和空间证明的依赖链；
9. 底层 `D(m,ℓ)` 的接口、data block 角色及抽象边界；
10. 一个贯穿插入—迁移—查询的教学示例，并明确它不代替一般证明。

写作要求：伪代码必须标为抽象说明；不能声称小组已证明字面常数 10；阶段下标形式归纳未关闭前，用“原文 Claim 13 给出，当前解释仍有下标核查项”的口径。

### 2. 审阅职责

- 第一审阅 A 的模型、定理参数、下界和概率语义；
- 第二核查 C 的工程 filter 是否被错误地与 word-RAM 理论结果直接排名；
- 对 A 至少提出 5 条实质性评论，并检查所有符号首次定义。

### 3. 建议提交节奏

```text
draft(B): explain prefix matching and staged construction
draft(B): write operations correctness and complexity
review(B): verify model parameters and lower-bound wording
```

## 五、成员 C：陈戚

### 1. 主任务：相关研究、评价与后续工作章节

新建 `drafts/section-C-related-work-and-evaluation.md`，至少包含：

1. Bloom filter 与 approximate membership 的起点；
2. dynamic/scalable Bloom filter、quotient filter、cuckoo filter 的可比维度；
3. succinct dictionary、动态 hashing、去均摊化 cuckoo hashing 的技术背景；
4. PSW unknown-size filter 与本文的直接承接关系；
5. 原文提及但未充分展开的工作；
6. 2020 年后的直接后续、相邻理论和工程研究；
7. Aleph、Kuszmaul–Walzer 2024、Resizable Retrieval 的同模型/异模型比较；
8. 本文优点、限制、适用范围和仍开放的问题；
9. 对“技术优越性”的多维评价：空间、时间、删除、增长范围、实现性和证明强度；
10. 文献时间线和引用来源说明。

写作要求：只允许 E3 结论进入确定性比较；E1/E2 只能作为待核查或旁支。Resizable Retrieval 必须标为 2026 预印本状态，不声称正式发表。

### 2. 审阅职责

- 第一审阅 B 的章节能否让未读原论文者重画数据结构并跟随证明；
- 第二核查 A 的下界、领先常数和“接近信息论最优”措辞；
- 对 B 至少提出 5 条实质性评论，并指出至少一个缺少原文定位的位置。

### 3. 建议提交节奏

```text
draft(C): write verified related-work timeline
draft(C): evaluate strengths limits and follow-up work
review(C): test technique chapter for reader traceability
```

## 六、第三轮交叉审阅

建议每位成员在个人分支发起一个 PR。若暂不能使用 PR，统一记录到 `discussions/review-day5.md`，但仍须保留被审版本、评论、作者回应和关闭依据。

每个第一审阅人至少留下 5 条实质性评论：

- 至少一个逻辑跳跃；
- 至少一个缺少来源或页码的位置；
- 至少一个普通读者可能看不懂的位置；
- 至少一个符号、术语或概率口径问题；
- 至少一个与另一章节的重复、矛盾或衔接问题。

审阅链：B→A，C→B，A→C。作者修改后，第二核查人分别为 C、A、B。第二核查不能只写“通过”，须说明抽查了哪些结论和来源。

## 七、事实核查和统一规范

新建 `discussions/fact-check-day5.md`，至少记录：主张、章节位置、来源、核查人、状态和最终措辞。优先检查：

- “首次”“最优”“达到下界”“worst-case O(1)”；
- `ε`、`δ`、high probability、conditioned on no failure；
- Theorem 1/10 与 PSW 下界的参数差异；
- 后续论文是否直接引用本文，以及是否处于同一模型；
- 所有 DOI、年份、页码、定理编号和 BibTeX key。

统一术语表至少包含：filter、dictionary、approximate membership、unknown size、false positive、failure、prefix matching、truth table、de-amortization、succinct、wasted bits。

## 八、会议与口头检查

新建 `discussions/meeting-day5.md`。每人用 8–10 分钟讲自己的章节，再由另两人追问。每人必须复述一个非本人负责章节的完整论证。记录至少包括一次错误或不完整回答、纠正证据和遗留问题。

重点问题：本文到底比 PSW 强在哪里；为何 FP 与 failure 不同；四结构如何覆盖迁移；为何后续研究不能排成单一“更优”序列。

## 九、Day 5 验收与 Day 6 出口

### 文件验收

- [ ] A、B、C 三个主体章节均有可审阅初稿
- [ ] 每章关键结论均有原文/正式来源或明确待核查标记
- [ ] 三个 PR 或等价的可追溯审阅链已经建立
- [ ] 第一轮至少 15 条实质性评论，作者已逐条回应
- [ ] 第二核查人完成抽查记录
- [ ] `fact-check-day5.md` 与术语规范已建立
- [ ] 三人均更新个人日志和 AI 使用记录
- [ ] 每人至少两个有意义的 commit，并已分批推送

### 理解验收

- [ ] A 能解释核心构造和四结构查询，而不只讲下界
- [ ] B 能解释 PSW 下界与本文上界的区别
- [ ] C 能解释式 (2) 的误报预算和 failure 并合骨架
- [ ] 三人都能指出当前 Q1/Q3，不把缺口隐藏在正文中
- [ ] 三章拼接前不存在明显参数、符号或时间口径冲突

只有三个章节都通过第一审阅并完成作者修订后，Day 6 才建立 `drafts/review-integrated.md`。未通过项进入全文问题清单，不能在整合时静默删除警告。
