# 成员刘威 AI 使用记录

## 2026-07-28（Day 4）

### 使用者、工具与任务

刘威；Codex / 本地 PDF 文本定位。任务是依据 `work/day4.md` 补齐概率、空间、渐近条件与交叉审阅过程材料，不生成可直接提交的 Review 终稿。

### AI 辅助内容

- 定位并整理原论文式 (2) 的逐阶段误报求和；
- 将第 5 节式 (3)–(5) 的三类失败事件与 Claim 13 的跨层 union bound 对齐；
- 代入 Lemma 11 空间式并核查 Theorem 10 到 Theorem 1 的低阶项吸收；
- 对 B 的伪代码和 C 的后续研究矩阵形成审阅问题与谨慎表述；
- 更新证明表、提纲、会议记录和项目总览。

### 人工核查要求与采用边界

成员 A 需逐式对照原论文第 9–16 页的 Theorem 10、式 (2)、Lemma 11、Claim 13、式 (3)–(5)，并由 B/C 复核。阶段下标、字面常数 10、位级临时空间峰值和自适应对手口径没有被 AI 宣布为已解决。产物只作为阅读与写作过程证据，最终 Review 必须由成员本人改写并能口头解释。

### 对应文件

`notes/memberA/probability-and-space-proof.md`、`notes/proof-table.md`、`discussions/review-day4.md`、`discussions/meeting-day4.md`、`drafts/outline-v1.md`、`README.md`。

---

## 2026-07-30（Day 5–Day 6 章节成稿与整合）

### 使用者与原始任务

刘威（成员 A）。原始请求：B、C 已完成最新 Day 5、Day 6 工作，根据当前进度和工作规划补齐 A 的相关内容，随后选择直接形成完整成稿，暂不创建 Git commit 或推送。

### AI 读取的本地证据

- `work/day5.md`、`work/day6.md`、`discussions/issues-day6.md`；
- A 的 `definitions.md`、`lower-bound-notes.md`、`probability-and-space-proof.md`；
- B 的技术章与证明材料，C 的相关研究章和引用审计；
- 本地 LYY 论文 PDF 中 Theorem 1、Theorem 10、式 (2)、Lemma 11、Claim 13 及第 5 节的概率链；
- 本地 PSW PDF 中 Theorem 3.1、Lemmas 3.2–3.4、式 (3.1)–(3.2)。

### AI 辅助完成的内容

1. 新建 `drafts/section-A-problem-and-significance.md`，系统解释模型、Theorem 1/10、式 (2)、PSW 压缩下界、空间/failure 计算、研究意义和限制。
2. 补入 A 对 B 的七条文本审阅和对 C 的五项比较措辞核查。
3. 将 A 负责的摘要、引言、定义、主结果、PSW 下界、空间与 failure 论证整合进 `drafts/review-integrated.md`。
4. 更新 Day 5/6 事实核查、问题清单、读者测试、会议准备和八项正文—文献对应抽查。

### 关键核查与修正

- 正式 Theorem 10 是 `n=ω(log u)`、`n<u`；Theorem 1 的 `n>u^{0.001}` 只服务于 `(1+o(1))` 化简展示。
- PSW Theorem 1.1 字面给出 `Ω(n log log n)`；更精细的 `(1-O(ε))` 领先系数来自 Theorem 3.1 的参数化形式。
- LYY 式 (2) 只解释本构造的上界直觉，不替代 PSW 的普遍下界证明。
- `ε` 与 `δ=u^{-C}` 分别表示 no-failure 查询误报与序列级结构 failure，未合并为“总错误率”。
- Claim 13 阶段下标、字面常数 10 和位级迁移峰值仍保留为 Q1/Q3，没有伪装成小组已独立证明。

### 当时的限制与后续复核（历史记录）

- AI 没有替代真实组会、脱稿复述或 B/C 的最终签字审阅；这些在当时会议记录中保持未完成，后经小组决定不再形成 Day 7 文件。
- 成员 A 可按新章节末的证据定位表，逐项回到两篇 PDF 重新计算和用自己的语言复述。
- 最终对外使用前，需重新核对 2026 预印本状态，并运行完整参考文献生成与排版流程。

### 对应修改文件

```text
drafts/section-A-problem-and-significance.md
drafts/review-integrated.md
discussions/review-day5.md
discussions/fact-check-day5.md
discussions/meeting-day5.md
discussions/issues-day6.md
discussions/review-day6.md
discussions/meeting-day6.md
references/citation-audit.md
ai-usage/member-A-log.md
```

---

## 2026-07-17

### 使用者

刘威

### 使用工具

Codex / ChatGPT

### 提问目的

根据本地 `Plan.md` 和论文 PDF，帮助建立 Day 1 的阅读笔记、定义表、问题清单和提纲框架。用途是辅助整理过程材料，不作为最终 review 正文直接提交。

### 原始问题

用户请求：“现在作为成员A，逐步完成Day1的工作”

### AI 回答摘要

AI 根据 `Plan.md` 中 Day 1 对成员 A 的要求，读取论文前几页内容，整理了：

- 成员 A 的通读范围；
- approximate membership、dictionary、filter、false positive、false negative、unknown sizes 等基础定义；
- 论文主要结果的初步表述；
- 为什么 filter 不能简单像 exact dictionary 一样扩容；
- 下界和参数限制的待核查问题；
- Day 1 会议记录模板和 review 提纲中的本人 主责部分。

### 人工核查方式

需要本人后续人工核查：

- 对照原论文摘要、第 1 节 Introduction、第 1.1 节 Main Results、第 1.3 节 Previous Construction、第 1.4 节 Our Techniques；
- 对照 Pagh、Segev、Wieder [28] 的原论文，确认 unknown-size filter 下界；
- 在 Day 2 精读正式定理，确认 `n > u^0.001`、`epsilon` 范围和 high probability 的精确定义；
- 与组员核查 prefix matching 和迁移过程；
- 与组员核查参考文献编号和相关工作分类。

### 核查结论

部分正确，待人工继续核查。当前内容只作为 Day 1 阅读过程记录和待验证草稿，不作为最终正文。

### 最终使用方式

- 用于建立阅读笔记和问题清单；
- 需要成员 A 用原论文逐条核查后，再改写为 review 正文；
- 未核查的复杂度、下界和参数结论不得直接写入终稿。

### 对应 Commit 或 PR

待提交。建议 commit：

```text
notes(A): add day 1 reading notes and definitions
ai-log(A): record AI-assisted day 1 setup
```

---

## 2026-07-21（Day 3）

### 使用者

刘威

### 使用工具与目的

Codex / ChatGPT、本地 PDF 文本提取、PDF 页面渲染与视觉核对。用途是协助定位引理、整理依赖关系、复算空间项，并发现需要人工复核的原文细节；不作为最终 Review 正文直接提交。

### 原始任务

“完成 A 的 Day3 相关工作，完成后告知修改了哪些文件，提供给我进行审核。”

### 实际读取材料

- `AGENTS.md`、`Plan.md`、`work/day1.md`、`work/day2.md`、`work/day3.md`；
- A 的 `definitions.md`、`lower-bound-notes.md`、`paper-reading.md`；
- B 的 `construction-notes.md`、增长图和查询/插入流程图；
- `discussions/questions.md`、`discussions/meeting-day2.md`；
- 原论文 PDF 第 8--13 页及第 5 节相关文本，重点核查 Theorem 7--10、Lemma 11、Claim 13、公式 (2)--(3)。

### AI 辅助形成的内容

1. 新建 A 的引理依赖、空间分解和随机性假设笔记；
2. 新建证明依赖图初稿；
3. 续写 PSW 下界核查边界；
4. 对 B 的 8 元素示例作正式审阅；
5. 识别 Claim 13 阶段区间与 `ceil(log n)` 的下标不一致风险；
6. 判断“常数轮迁移”的渐近机制可理解，但无法从 `O(m)` 黑盒接口推出字面常数 10 的完整常数配平。

### 人工核查方式

审核者应逐项对照：

- 第 8 页 Theorem 7、8：有限独立哈希与 Chernoff 前提；
- 第 9 页 Theorem 9、10：adaptive prefixes 和正式 filter 保证；
- 第 10 页公式 (2)、Lemma 11：误报求和与 prefix matching 空间；
- 第 11--12 页 `D(m,ell)` 接口：空间、failure、decrement、初始化/销毁调用次数；
- 第 12--13 页 Claim 13：四步维护、常数 10、阶段区间和查询下标；
- 第 13 页公式 (3) 及第 5 节：底层 failure 的来源。

还需另行取得 PSW [28] 原文后核查完整下界证明。本次没有从摘要或 AI 推测补写该证明。

### 当前判断

Theorem 10 上界依赖链、空间主项/低阶项和两类概率的区分已由本地 PDF 核对。Claim 13 的下标和字面常数配平仍标为 Q3；这两点不得在人工复核前写成已解决。

### 最终使用方式

- 作为刘威 Day 3 个人精读记录；
- 作为 A/B 共同证明表和组会讨论的输入；
- 作为后续 Review “空间与正确性证明”部分的事实清单；
- 经成员本人和交叉审阅确认后再改写，不直接复制为终稿。

---

## 2026-07-20（Day 2）

### 使用者

刘威

### 使用工具

Codex / ChatGPT，本地论文 PDF 文本提取与页面核对工具。

### 提问目的

根据 Day 2 工作安排，辅助完成成员 A 负责的正式问题模型、基本定义、主定理参数、空间下界和参数关系笔记。

本次 AI 用途是：

- 帮助定位原论文中的定理、公式和相关段落；
- 检查 Day 1 初步理解中不够准确的地方；
- 区分论文已经证明的结论、帮助理解的直觉和仍需查阅原始文献的问题。

本次输出属于阅读辅助材料和过程笔记，不直接作为最终 Review 正文。

### 原始问题

### AI 实际读取的材料

- `AGENTS.md` 中的课程要求；
- `Plan.md` 中成员 A 的角色和 Day 2 工作安排；
- `work/day1.md` 与 `work/day2.md`；
- `notes/memberA/definitions.md`；
- `notes/memberA/lower-bound-notes.md`；
- `notes/memberA/paper-reading.md`；
- 本地论文 *Succinct Filters for Sets of Unknown Sizes*：
  - 摘要和第 1 节；
  - §1.1 Main Results；
  - §1.3 Previous Construction；
  - §1.4 Our Techniques；
  - §3.1 Theorem 10；
  - 公式 (2)；
  - Lemma 11；
  - Claim 13；
  - Theorem 12 的结果陈述。

AI 没有在本次工作中阅读 PSW [28] 的原论文，因此没有把 PSW 下界的完整证明写成已经核实的内容。

### AI 回答与修改摘要

AI 对 `notes/memberA/` 下的三份文件进行了扩展和修订。

#### 1. `definitions.md`

补充和解释了：

- 全集 `[u]`、当前集合 `S`、当前大小 `n` 和容量 `N`；
- `insert`、`lookup`、dictionary 和 filter 的正式语义；
- false positive 与 false negative 的区别；
- `unknown size` 未知的是最终规模或紧容量上界，而不是全集 `u` 或当前 `n`；
- 本文中 succinct 的含义；
- 已知容量 filter 的经典空间基准；
- 公式 (2) 中前缀长度各项的直觉；
- Theorem 10 的参数、空间、时间、failure 概率和误报保证；
- Theorem 1 与 Theorem 10 表述不同的原因；
- expected、amortized、worst-case 和 high-probability worst-case 的区别。

#### 2. `lower-bound-notes.md`

补充和区分了：

- 已知容量下的 `N log(1/epsilon)` 空间基准；
- PSW unknown-size filter 下界；
- `log(1/epsilon)` 和 `log log n` 两种成本；
- “本文构造为什么出现 `log log n`”与“PSW 为什么证明它不可避免”的区别；
- `(1-O(epsilon))` 在 `epsilon=o(1)` 和常数 `epsilon` 下的不同解释；
- `n>u^0.001` 与正式条件 `n=omega(log u)` 的关系；
- `O(log log log u)` 和 `u^c` 何时能被吸收到低阶项；
- Day 1 五个疑问的阶段性结论和仍待核查部分。

#### 3. `paper-reading.md`

记录了：

- Day 2 实际精读范围；
- 对 Day 1 参数理解的修正；
- Dynamic filter 与 dynamic dictionary 的主结果；
- 无漏报、误报率、查询时间、插入时间和空间界的证明路线；
- 为什么本文不能简单等同于 scalable Bloom filter；
- 给张书铖和陈戚的交叉核查问题；
- 下一阶段仍需解决的证明细节。

### AI 发现并修正的 Day 1 问题

#### 修正 1：正式定理的 `n` 条件

Day 1 主要记录了摘要和非正式 Theorem 1 中的：

```text
n > u^0.001
```

AI 对照论文第 9 页 Theorem 10 后指出，正式定理实际写为：

```text
n = omega(log u)，且 n < u
```

同时正式空间式还保留 `O(log log log u)` 和输入无关的 `u^c` 位预计算空间。笔记因此将非正式结论和正式结论分开表述。

#### 修正 2：high probability 的具体含义

Day 1 只猜测失败概率可能是 `1/poly(n)`。Theorem 10 正式写出：

```text
delta = u^{-C}，其中 C > 1
```

对任意插入序列，整个过程中曾报告 failure 的概率至多为 `delta`，概率取自预计算随机比特。

笔记还区分了：

- 数据结构报告 failure 的概率；
- filter 对非成员产生 false positive 的概率。

#### 修正 3：没有把构造直觉当成下界证明

公式 (2) 中的 `log i` 可以解释本文上界为什么出现 `log log n`，但它不能单独证明所有 unknown-size filter 都必须付出这一成本。

AI 将笔记修改为：

- 构造来源：多阶段误报预算；
- 不可避免性：PSW 的信息论下界；
- PSW 完整证明：尚未在本次工作中核查。

### 原论文定位记录

| 核查内容 | 原论文位置 |
|---|---|
| `[u]` 的定义、`insert` 与 `lookup` | 第 1 页，第 1 节及脚注 1 |
| filter 的误报与无漏报语义 | 第 2 页 |
| succinct 的定义、`log` 底数 | 第 2 页脚注 2、3 |
| 已知容量空间与 PSW 下界 | 第 2 页 |
| high probability 的引言解释 | 第 2-3 页及脚注 4 |
| 非正式 Dynamic filter 结果 | 第 3 页 Theorem 1 |
| Previous Construction 与阶段误报预算 | 第 4-5 页 §1.3 |
| 本文技术概览与低阶冗余 | 第 5-6 页 §1.4 |
| 正式 Dynamic filter 结果 | 第 9 页 Theorem 10 |
| 前缀长度与误报率计算 | 第 10 页公式 (2) |
| Prefix matching 空间与失败保证 | 第 10 页 Lemma 11 |
| 四个活跃结构与后台迁移 | 第 11-13 页 Claim 13 |
| 正式 Dynamic dictionary 结果 | 第 11 页 Theorem 12 |

### 人工核查方式

审核本次内容时应进行以下操作：

1. 对照原论文第 9 页 Theorem 10，逐项检查 `epsilon`、`n`、`u`、`w`、`c`、`C` 和 `delta`；
2. 对照第 10 页公式 (2)，检查前缀长度和 union bound 的抄写；
3. 对照第 12-13 页 Claim 13，检查四个活跃结构及“每次执行 10 轮维护”的表述；
4. 确认笔记中对 `n>u^0.001` 的解释只是渐近关系分析，没有被写成论文逐字给出的证明；
5. 后续阅读 PSW [28] 原论文，核查下界的完整证明，不直接采用 AI 对下界直觉的概括；
6. 与张书铖核查 prefix matching、迁移和底层数据结构部分；
7. 与陈戚核查 PSW 及其他相关工作的书目信息和理论比较。

### 当前核查结论

本次 AI 已使用本地论文 PDF 对 Theorem 10、公式 (2)、Lemma 11、Claim 13 和 Theorem 12 的文字及页面进行了交叉检查，并修正了 Day 1 中关于正式参数和失败概率的不完整表述。

但是，下列内容仍须人工确认：

- PSW 下界的完整证明；
- `n>u^0.001` 在全文所有技术步骤中的用途；
- Claim 13 的常数 10 为什么足够完成全部迁移；
- 四个活跃结构并存时的严格空间求和；
- 实际实现中的哈希和预计算表常数开销。


### 最终使用方式
- 作为个人精读和参数核查记录；
- 作为组内讨论 Theorem 1、Theorem 10 和 PSW 下界时的材料；
- 作为后续撰写“问题模型”“研究意义”“空间下界”和“参数限制”章节的事实清单；
- 不直接复制为最终 Review 正文；

### 对应文件
```text
notes/memberA/paper-reading.md
notes/memberA/definitions.md
notes/memberA/lower-bound-notes.md
```

---

## 2026-07-21（Day 3，PSW 原文补充核查）

### 使用者与任务

刘威。继续完善 A 的 Day3 工作。

### 使用工具

Codex / ChatGPT、本地 PDF 文本提取、逐页渲染和视觉核对。PDF 页面只用于定位和核对公式，没有把 AI 生成内容当作原文引用。

### 实际核查范围

- PSW §1.3 的 lower-bound intuition；
- §3 The Lower Bound: From Approximate Membership to Compression；
- 第 7 页 Theorem 3.1；
- 第 8--10 页 Lemma 3.2、3.3、3.4、式 (3.1)、式 (3.2) 及最终编码不等式；
- Theorem 3.1 到 Theorem 1.1 的 `alpha`、`gamma` 参数代入。

### AI 回答摘要

AI 将下界证明整理为五步：固定随机性、选择正回答集合增长较小的几何块、控制块内旧误报、用中间状态编码、利用 `u^n/3` 条序列的计数下界导出状态空间下界。随后解释 `log log n` 来自对小增量候选集合大小取对数，而不是来自本文上界构造的阶段数本身。

### 人工核查方式与结论

已对 PSW PDF 第 7--10 页进行文本和页面图像交叉核对。Theorem 3.1 的条件、`1-1/gamma`、`1-9epsilon`、Lemma 3.2 的 `u^n/2`、Lemma 3.4 的 `u^n/3`、式 (3.2) 和最终 `b_i` 下界均已回到原页确认。

仍需组员独立复算：让 `gamma` 随 `n` 缓慢增长时，如何把参数化定理写成 Liu--Yin--Yu 使用的精细 `(1-O(epsilon))` 领先系数。PSW Theorem 1.1 字面只陈述 `Omega(n log log n)`，笔记已明确区分。

### 修改用途

- 完善 `notes/memberA/lower-bound-notes.md` §14；
- 更新 A 的依赖笔记、阅读记录、证明依赖图和问题状态；
- 作为后续人工撰写证明解释的事实底稿，不直接复制为最终 Review。

## 2026-07-30：全仓库状态回填与定稿产物复核

### 使用内容

- 检索全部 Markdown 中的“待定 / 待成员 / 待修订”状态，并依据 Day 5/6 后续文件逐项对账；
- 将已解决项改为“已修订”或补充后续证据位置，同时保留 Day 2–4 的历史快照；
- 生成 v1.0 HTML/PDF，并逐页检查 8 页的标题、页码、表格、边界和参考文献。

### 人工核查边界

- 未把阶段下标、字面常数 10 和位级峰值伪装为已独立证明，而是保留为 Q1/Q3；
- 未代替成员完成口头演练、签字或 PR 审阅；小组最终决定不再为这些活动建立 Day 7 文件；
- 本轮未提交或推送 Git 历史。

### 项目最终状态

源稿、引用审计、过程记录和最终 PDF 已定稿。Day 7 口头交流与最终审阅按小组决议不再留档；本日志不将其表述为已经发生。Q1/Q3 继续作为技术限制保留。
