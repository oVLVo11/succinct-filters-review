# Day 2 工作分配：精读问题模型、主要结果与经典相关背景

日期：2026-07-20  
衔接状态：Day 1 已完成刘威（A）的定义、问题模型和下界疑问笔记，张书铖（B）的构造路线、证明依赖笔记及两份流程图文字稿；陈戚（C）的相关工作笔记、来源清单、BibTeX 和 AI 使用日志尚未形成有效内容。Day 2 在执行原计划的同时，必须补齐这些缺口。

## 一、Day 2 共同目标

今天不开始代写完整 Review 正文，重点是把 Day 1 的“初步理解”推进到“能够定位原文、说明参数并相互核查”：

1. 准确说明论文的正式模型、主要结果和参数限制；
2. 用一个小规模例子讲清变长前缀、阶段增长和迁移直觉；
3. 建立可追溯的经典相关工作比较表；
4. 对 `discussions/questions.md` 中的 Q1 问题给出带原文位置的阶段性答案；
5. 留下个人笔记、会议记录、交叉审阅、AI 使用记录和分阶段 commit。

当天结束时，三人都应能解释：

- `log(1/epsilon)` 与 `log log n` 分别对应什么成本；
- `1 + o(1)` 在本文空间结果中意味着什么；
- “以高概率最坏情况 `O(1)`”与“期望/均摊 `O(1)`”有什么区别；
- 为什么本文结果不能简单等同于 scalable Bloom filter。

## 二、成员 A：刘威

角色保持不变：问题模型、基本定义、理论背景、空间下界和参数关系。

### 1. 精读范围

- 论文摘要、§1.1 Main Results、正式 filter 定理（非正式 Theorem 1 与正式 Theorem 10）；
- §3.1 中 filter 到 prefix matching 的化归及前缀长度公式；
- 与 Theorem 1/10 有关的模型说明、脚注和概率保证；
- Pagh–Segev–Wieder 下界在本文引言和 related work 中的表述。

### 2. 具体任务

在已有 `notes/memberA/definitions.md` 基础上修订，禁止另写一份互相矛盾的定义：

1. 明确写出 `U=[u]`、当前集合 `S`、`n=|S|`、误报率 `epsilon`；
2. 分别定义 `lookup`、`insert`、filter 和 dictionary；
3. 说明 filter 为什么不允许 false negative，以及 false positive 概率针对什么随机性；
4. 准确解释 unknown size：未知的是最终规模/紧容量上界，不是结构不知道当前 `n`；
5. 解释本文中 succinct 的比较基准，而不是只写“占用空间小”；
6. 对照原文列出 Theorem 1/10 对 `n`、`u`、`epsilon`、操作序列和失败概率的完整限制；
7. 说明已知容量时的经典空间基准，以及未知规模为何出现额外 `log log n` 项；
8. 把下界证明中仍未理解的部分继续留在 `notes/memberA/lower-bound-notes.md`，不得把猜测写成结论。

### 3. 当日产物

- 修订 `notes/memberA/definitions.md`；
- 修订 `notes/memberA/lower-bound-notes.md`；
- 在 `discussions/questions.md` 中对 Q1.1、Q1.2、Q1.3、Q1.4 写阶段性核查结果，每条附论文页码、章节、定理或公式位置；
- 若使用 AI，追加 `ai-usage/member-A-log.md`，写明问题、回答摘要、人工核查位置和是否采纳。

### 4. 建议提交节奏

- Commit A1：正式模型、操作语义和参数限制；
- Commit A2：空间基准、`log log n` 解释及 Q1 核查。

建议提交信息：

```text
notes(A): verify formal filter model and theorem parameters
proof(A): trace known-size baseline and unknown-size overhead
```

## 三、成员 B：张书铖

角色保持不变：核心构造、prefix matching、阶段迁移、数据结构实现与证明依赖。

### 1. 精读范围

- §1.3 Previous Construction 与 §1.4 Our Techniques；
- §3.1 的哈希前缀长度、prefix matching 化归和 Lemma 11；
- Claim 13 的阶段结构、查询、插入和迁移流程；
- 已有 `construction-notes.md` 中涉及 `T_{i-1}, T_i, D_{i-1}, D_i` 的原文依据。

### 2. 具体任务

继续修订 `notes/memberB/construction-notes.md`，把 Day 1 的组件清单推进为可验证的小例子：

1. 说明元素如何经全局哈希变成二进制串；
2. 写出阶段 `i` 的前缀长度公式，并逐项解释用途；
3. 说明为何查询能化为“某个已存字符串是否为查询哈希串的前缀”；
4. 说明为什么要按集合规模翻倍划分阶段；
5. 给出连续插入 8 个抽象元素的示例，至少列出：
   - 每次插入所处阶段；
   - 当前活跃的 `T`、`D` 结构；
   - 新元素进入哪里；
   - 哪一步推进旧结构迁移；
   - 查询需要检查哪些结构；
6. 例子只用于解释状态变化，不得虚构具体哈希碰撞概率；若选用具体比特串，明确标注为教学示例；
7. 核查 Day 1 笔记中“每次插入做 10 轮维护”“阶段边界”和“短串/长串去向”的原文位置；
8. 把 `figures/growth-process.md` 改成能与 8 元素示例一一对应的阶段增长示意图说明。

### 3. 当日产物

- 修订 `notes/memberB/construction-notes.md`；
- 修订 `figures/growth-process.md`；
- 必要时同步修订 `figures/query-insert-flow.md`，保证流程与例子一致；
- 在 `discussions/questions.md` 中记录例子暴露出的不变式或迁移疑问；
- 若使用 AI，追加 `ai-usage/member-B-log.md` 并记录人工核查。

### 4. 建议提交节奏

- Commit B1：哈希前缀、prefix matching 与阶段划分的原文核查；
- Commit B2：8 元素增长示例和图示修订。

建议提交信息：

```text
notes(B): verify prefix matching and stage transitions
figures(B): add eight-insertion growth example
```

## 四、成员 C：陈戚

角色保持不变：相关研究、后续研究、参考文献和总体评价。由于 Day 1 产物缺失，今天先补齐资料入口，再执行 Day 2 的经典文献比较；这属于恢复计划进度，不改变角色。

### 1. 第一阶段：补齐 Day 1 缺口

先完成并分别保存：

- `notes/memberC/paper-reading.md`：原论文引言、related work 和参考文献的阅读记录；
- `notes/memberC/related-work.md`：将原论文相关工作分为 Bloom filter、动态/可扩展 filter、succinct dictionary、quotient/cuckoo filter、hashing/deamortization；
- `notes/memberC/post-2020-work.md`：今天只建立候选清单，明确“尚未核查”，不急于下结论；
- `references/source-list.md`：原论文正式页面、arXiv、会议版本及经典文献入口；
- `references/bibliography.bib`：只收录已经核对作者、标题、年份和出处的条目；
- `ai-usage/member-C-log.md`：即使没有使用 AI，也写明“今日未使用 AI”。

### 2. 第二阶段：完成 Day 2 文献矩阵

新建 `references/literature-matrix.md`，至少覆盖：

- Bloom filter；
- dynamic Bloom filter；
- scalable Bloom filter；
- quotient filter；
- cuckoo filter；
- succinct dictionary；
- Pagh–Segev–Wieder unknown-size filter（作为最直接前作单列）。

每项必须记录：

1. 解决的问题；
2. 是否要求预知容量或负载上界；
3. 是否支持删除；
4. 空间复杂度；
5. 查询和插入复杂度，区分 worst-case、expected、amortized、with high probability；
6. 与本文的直接关系；
7. 结论来源的论文页码、章节、定理或正式网页；
8. “已核查 / 待核查”状态。

禁止仅凭博客、搜索摘要或 AI 回答填写理论结论。二手材料可用于找线索，但最终应回到原论文或正式出版页面。

### 3. 当日产物

- 补齐上述 6 份 Day 1 缺失文件；
- 新建 `references/literature-matrix.md` 初版；
- 在 `discussions/questions.md` 回应 B 在 Day 1 提出的两项可比性问题：
  - scalable/dynamic Bloom filter 是否满足本文全部模型要求；
  - quotient/cuckoo filter 是否依赖容量或负载上界；
- 将无法确认的结论明确标为待核查。

### 4. 建议提交节奏

C 的工作量较多，应至少拆成三个有意义的提交，不能在当天结束时一次性上传：

- Commit C1：个人阅读笔记、分类和资料入口；
- Commit C2：已核对的 BibTeX 与经典文献矩阵；
- Commit C3：可比性结论、待核查项和 AI 使用记录。

建议提交信息：

```text
notes(C): add related-work reading notes and source map
refs(C): build verified classic-filter literature matrix
discussion(C): assess model comparability of prior filters
```

## 五、共同讨论与 Day 2 会议

新建 `discussions/meeting-day2.md`。会议建议 30—40 分钟，由三人分别口头讲解自己的材料，不直接复制个人笔记。记录中必须包含：

1. `log(1/epsilon)` 为什么是误报率成本；
2. `log log n` 为什么与未知规模和阶段误报预算有关，以及哪些结论仍需下界证明支持；
3. `(1+o(1))` 修饰的是哪个空间表达式、在什么参数范围成立；
4. “whp worst-case O(1)”和“expected amortized O(1)”的差别；
5. 8 元素示例是否忠实反映 Claim 13；
6. 文献矩阵中哪些方案真正允许 unknown size，哪些只是工程可扩容；
7. 今天解决了哪些 Q1，新增了哪些 Q2/Q3/Q4；
8. 三人各自能否复述另外两人的核心结论。

会议结论必须区分：

- 已由原论文/正式文献核实；
- 小组当前解释；
- 仍待验证。

## 六、交叉审阅

角色沿用计划，不交换：

- 张书铖（B）审阅刘威（A）的 `definitions.md`：重点检查术语、概率语义、参数条件和 high probability 表述；
- 陈戚（C）审阅张书铖（B）的 8 元素示例与增长图：重点检查未读过论文的人能否跟随，以及示例是否混淆真实算法与教学简化；
- 刘威（A）审阅陈戚（C）的 `literature-matrix.md`：重点检查模型是否可比、空间/时间保证是否准确、是否有正式来源。

每人至少留下 2 条实质性审阅意见。意见应进入 PR、Issue 或 `discussions/meeting-day2.md`，并包含：

- 被审文件和具体小节；
- 问题是什么；
- 建议如何核查或修改；
- 作者是否接受及修改结果。

## 七、过程记录与提交要求

1. 刘威、张书铖各至少 2 个有效 commit，陈戚至少 3 个有效 commit；
2. 三人都要更新自己的工作/阅读记录；
3. 三人都要留下至少一次交叉审阅；
4. AI 使用记录必须写清问题、回答摘要、人工验证和最终判断；不得把 AI 生成内容直接作为 Review 正文；
5. 尽量使用各自分支和 PR，保留评论与修订过程；
6. 每个阶段完成后及时推送公开 GitHub，不要在截止前一次性上传；
7. commit 信息要描述内容，不使用 `update`、`修改`、`final` 等模糊词。

## 八、Day 2 验收清单

### 文件验收

- [ ] 刘威修订 `notes/memberA/definitions.md`
- [ ] 刘威修订 `notes/memberA/lower-bound-notes.md`
- [ ] 张书铖完成 8 元素阶段增长示例
- [ ] 张书铖修订阶段增长图说明
- [ ] 陈戚补齐 Day 1 的个人笔记、来源、BibTeX 和 AI 日志
- [ ] 陈戚完成 `references/literature-matrix.md` 初版
- [ ] 三人更新 `discussions/questions.md`
- [ ] 新建 `discussions/meeting-day2.md`
- [ ] 三人均留下可追溯的交叉审阅意见

### 理解验收

- [ ] 刘威能不看笔记完整说明 filter 正式模型、参数限制和两个空间成本
- [ ] 张书铖能用 8 元素示例解释阶段、四个活跃结构和后台迁移
- [ ] 陈戚能逐项说明至少六类相关工作为何与本文相同或不同
- [ ] 三人都能解释论文相对 PSW 前作的核心改进
- [ ] 所有关键数字、公式和复杂度都能定位到原论文或正式文献

### Day 3 入口条件

只有在正式模型、主要结果、经典文献矩阵和阶段示例均完成初步交叉核查后，Day 3 才进入底层 `D(m, ell)`、truth table、data block 和去均摊化组件的逐项拆解。未解决的问题保留编号进入 Day 3，不用为了“完成”而强行下结论。
