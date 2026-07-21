# 成员 C AI 使用记录

## 2026-07-19：第一轮论文阅读与相关工作资料整理

### 使用者与工具

- 使用者：陈戚（成员 C）
- 辅助工具：Codex；网页检索与 PDF 在线阅读工具

### 本次工作的分工与边界

成员 C 确定本轮任务范围、研究问题和核验标准：先留下可追溯的阅读与资料收集过程，重点梳理论文定位、相关工作分类和 2020 年后的研究线索；无法从可靠来源确认的结论必须明确标为“待核验”，不得直接写成最终 Review 的定论。

Codex 在这一范围内承担资料整理和机械执行工作，包括仓库盘点、来源定位、书目信息初步汇总、表格与笔记框架整理。研究范围、比较维度、材料是否采用以及本轮提交范围均由成员 C 决定。本轮材料不是由 AI 直接生成后未经审阅地作为课程论文提交。

### 成员 C 完成的工作

1. 明确成员 C 当前负责相关工作、后续研究和过程记录，并确定第一轮不撰写最终 Review；
2. 确定相关工作应区分理论前作、工程型过滤器、动态字典和论文发表后的扩展，避免把不同模型中的结果直接横向比较；
3. 审阅本轮拟提交的非讨论类阅读笔记、相关工作笔记、后续研究清单、来源清单和文献矩阵；
4. 检查材料中的证据等级和“待核验”标记，确认尚未精读的外部论文不会被表述成已经证明或已经全面优于本文；
5. 决定本轮暂不处理成员间讨论及对成员 B 草稿的审阅内容，该文件不纳入本次拟上传范围。

### AI 提供的辅助

1. 盘点当前分支、工作区、已有笔记和最近的版本记录；
2. 定位主论文正式在线版本中的摘要、主要定理、Claim 13、技术概览和参考文献页，供成员 C 核对；
3. 根据 DOI、出版社页面、DBLP 和 arXiv 汇总第一批候选文献的书目信息；
4. 按成员 C 指定的比较维度整理阅读笔记、来源清单、文献矩阵和 BibTeX 初稿；
5. 提醒区分非正式与正式定理、unknown-size/resizable 与 fully dynamic、理论结果与工程结果，并把证据不足的项目保留为“待核验”。

### AI 输出的采用方式

- AI 输出只作为检索、整理和文字修订的辅助材料，不替代成员 C 对论文内容和最终论点的判断。
- 成员 C 已审核本轮拟提交的非讨论类内容，并认可其作为第一轮过程记录的结构、范围与状态标记。
- “已审核”不等于把所有候选文献自动升级为“已精读”。每条材料仍以来源清单和文献矩阵中记录的证据等级为准。
- 最终 Review 中是否采用某一比较或结论，需要在后续精读原文、记录定理位置并与组员讨论后再决定。

### 后续仍需完成的研究工作

- 精读 PSW 2013 下界与上界定理全文；
- 核对 Scalable/Dynamic Bloom Filter 的空间、查询结构数、删除与误报预算；
- 核对 Raman--Rao、Demaine、Arbitman 等字典工作的正式定理和容量模型；
- 确认 InfiniFilter、Li et al.、Kuszmaul--Walzer 等工作是否直接引用本文，以及引用发生在什么语境；
- 继续核对 `bibliography.bib` 中作者拼写、页码、DOI 和正式发表状态；
- 后续再单独处理成员间讨论与成员 B 技术解释的审阅。

### 本轮拟上传范围

- `notes/memberC/paper-reading.md`
- `notes/memberC/related-work.md`
- `notes/memberC/post-2020-work.md`
- `references/source-list.md`
- `references/literature-matrix.md`
- `references/bibliography.bib`
- `ai-usage/member-C-log.md`

`notes/memberC/review-of-memberB.md` 属于暂不考虑的讨论/审阅内容，不纳入本轮拟上传范围。

### 审核与提交状态

成员 C 已审核上述非讨论类材料，确认它们可以作为第一轮研究过程记录；其中外部文献的阅读深度和待核验项仍按各文件中的明确标记保留。

本轮尚未执行 commit、push 或 Pull Request。待成员 C 检查本次修改并明确确认后，再提交和上传。

## 2026-07-20：Day 2 模型可比性第一批原文核验

### 成员 C 确定的任务

成员 C 要求根据 `work/day2.md` 重新核对本人分工，并继续推进尚未完成的工作，同时遵守课程对真实过程、原始来源、人工判断和 AI 使用披露的要求。本轮选择先处理两项可独立验证的模型问题：

1. scalable/dynamic Bloom filter 是否满足本文全部 unknown-size 保证；
2. quotient/cuckoo filter 是否仍依赖容量或负载上界。

本轮不撰写 Review 正文，不把摘要级信息直接升级为结论，也不替成员 C 声称已完成人工复述或组员交叉审阅。

### AI 辅助范围

- 对照 Day 2 清单审计成员 C 现有文件和证据状态；
- 定位并阅读四篇原始论文的相关章节；
- 将可定位到章节、公式或算法的事实整理进个人笔记、文献矩阵和来源清单；
- 对“dynamic”“resize”“unknown size”“worst-case”等容易混淆的术语做逐维比较。

### 本轮使用的原始来源与定位

| 文献 | 核查位置 | 本轮确认的事实 |
|---|---|---|
| Almeida et al. 2007, *Scalable Bloom Filters* | §4-5，PDF pp.4-8 | 查询测试每个现有组件；误报预算按几何级数收紧；指数增长时组件数为对数级；原始 SBF 未给删除操作 |
| Guo et al. 2006, *Dynamic Bloom Filters* | §III、式 (3)、Algorithms 1-2，PDF pp.3-6；结论 p.12 | 插入平均 `O(k)`；查询平均 `O(k(s+1)/2)`；FP 随组件数增长；算法未定义删除 |
| Bender et al. 2012, *Don't Thrash* | §3-4，PDF pp.1-6 | QF 支持删除、resize 与合并；结构和操作依赖槽数、负载率及 cluster 长度 |
| Fan et al. 2014, *Cuckoo Filter* | §1、§4-5、式 (3)，PDF pp.1、6-7 | 支持增删；插入成功依赖桶容量和留白；partial-key 方案的 fingerprint 长度存在随 `n/b` 增长的失败约束 |

### 采用与保留意见

- 已采用：把四项材料从“仅看摘要”提升为“已读原文相关章节”，并补入可复查位置。
- 已采用：将两个 Day 2 问题的阶段答案写入 `notes/memberC/related-work.md` 和 `references/literature-matrix.md`。
- 未采用：没有把工程吞吐、删除或可 resize 直接解释为在 Liu-Yin-Yu 同一理论模型上更优。
- 仍保留：四篇论文与本文的完整空间常数、所有最坏时间保证及实现比较尚未穷尽，不能据本轮记录写“全面优于/全面不如”。

### 工具限制与人工复核点

Dynamic Bloom Filter、Quotient Filter 和 Cuckoo Filter 通过在线 PDF 的页码文本与页面截图核对。Scalable Bloom Filters 的作者存档 PDF 因环境缺少 Poppler，使用临时 `pypdf` 提取文字和页码；临时 PDF 与解析库已删除，仓库未增加依赖或生成物。

成员 C 后续复核时可直接打开上述四篇原文，检查对应页码，并用自己的话回答：哪些结构不知道最终规模、哪些仍扫描多个组件、哪些依赖表负载，以及这些差异为什么阻止“全面替代本文”的结论。复核完成前，本节只作为 AI 辅助研究过程记录。

### 提交状态

本次修改尚未 commit 或 push，等待成员 C 查看差异并确认下一步。

## 2026-07-21：Day 3--4 第二轮文献核验与交叉审阅草案

### 成员 C 的工作目标与决定

成员 C 要求直接推进本人仍需完成的过程材料，并在完成后先交本人审核。成员 C 已审核此前两轮材料，本轮沿用其确定的分工：后续研究核验、来源维护、对 A/B 构造和证明材料的交叉审阅，以及优点/局限证据整理。本轮不撰写最终 Review 正文，也不替成员 C 声称已经阅读、同意或能够解释尚未亲自核查的内容。

### AI 执行的辅助工作

1. 对照 `work/day3.md`、`work/day4.md` 和仓库最新文件审计成员 C 的验收缺口。
2. 阅读 Aleph Filter、Kuszmaul--Walzer 2024、Resizable Retrieval 三篇原始 PDF 的关键页，记录定义、定理/推论、直接引用语境和时间保证类型。
3. 建立 `references/post-2020-matrix.md`，把 unknown-size insertion-only、支持删除的 capacity-dynamic、按当前 `n` 的 resizable 三种模型分开。
4. 检查 B 的 8 元素示例、构造拆解和伪代码，形成 `review-day3-C.md`、`review-day4-C.md` 审阅草案；指出 `ell(0)`、当前层初始化、迁移 failure 传播等可定位问题。
5. 将可核验的优点、局限、适用条件和未来方向整理为证据清单，未将其润色为课程论文段落。

### 本轮原始来源与核验位置

| 来源 | 阅读位置 | 用途 |
|---|---|---|
| Dayan et al., *Aleph Filter* (PVLDB 2024) | Abstract；§5.2；§7，PDF pp.1、8、12 | 直接引用 LYY；删除、无限增长、空间与 amortized 清理边界 |
| Kuszmaul--Walzer, *Space Lower Bounds for Dynamic Filters...* (STOC 2024) | 定义与主结果；§1 引用；Thm 3.1；PDF pp.1、3--4、12 | 区分 deletion-dynamic 与 unknown-size；核对线性冗余下界 |
| Kuszmaul et al., *Resizable Retrieval* (arXiv v1, 2026) | Introduction；Thm 1.1；Cor. 3.14；PDF pp.2--4、20--21 | 当前 `n` 空间、动态 filter 推论、预印本状态 |

### 人工审核边界

- 所有新建审阅文件均明确标为“待成员 C 审核”；AI 没有把待审状态改成成员 C 已完成或队友已接受。
- InfiniFilter 与 Li 2023/2024 未完成原始全文核验，仍保留摘要级/待核验标签。
- 2026 工作只按 arXiv v1 预印本引用，最终提交前需再次核对版本和发表状态。
- 成员 C 应逐项打开矩阵记录的页码，用自己的话复述模型、定理和比较理由；无法复述的内容应删除或退回待核验。

### 工作区与提交状态

本轮只修改课程仓库内的过程材料，没有 commit、push 或创建 PR。既有未跟踪文件 `notes/memberC/review-of-memberB.md` 未被修改，也未纳入本轮材料；待成员 C 审核本轮差异后再决定是否提交。
