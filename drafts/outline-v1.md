# Review 提纲 v1.1

初建日期：2026-07-17
最近更新：2026-07-20
状态：Day 2 A/B 材料整合版。成员 A 已核查正式模型、Theorem 1/10、参数和下界表述；成员 B 已核查公式 (2)、Claim 13，并完成 8 元素阶段示例。第 4、12 节仍等待成员 C 的文献矩阵，不能视为完成。

## 0. 小组分工

| 角色 | 姓名 | 主责内容 | 交叉职责 |
|---|---|---|---|
| 成员 A | 刘威 | 问题模型、基本定义、理论背景、空间下界、参数关系 | 审阅 C 的理论类相关工作；核查 B 的空间与正确性表述 |
| 成员 B | 张书铖 | 核心构造、prefix matching、阶段迁移、数据结构实现、证明依赖 | 审阅 A 的定义和问题动机；向 C 解释本文技术与已有 filter 的区别 |
| 成员 C | 陈戚 | 相关研究、后续研究、参考文献、论文评价 | 审阅 B 的技术解释是否清楚；与 A 核查相关工作的理论结果 |

## 1. 摘要

- 用中文概括论文研究的问题：在集合最终大小未知时，维护动态 approximate membership filter / dictionary。
- 概括 filter 的核心结果：空间达到 `(1 + o(1)) n (log(1/epsilon) + log log n)` bits，且插入和查询以高概率最坏情况常数时间。
- 概括 dictionary 的核心结果：空间随当前 `n` 变化，接近 `(1 + o(1)) n log(u/n)`，并支持常数时间操作。
- 明确本文 review 的重点：问题为什么难、已有方案差在哪里、本文技术如何绕开迁移和空间峰值问题、证明如何核查。

## 2. 引言

- 从 membership query 的应用场景引入：数据库、缓存、病毒扫描、网络设备等。
- 解释 dictionary 与 filter 的区别：
  - dictionary 精确回答；
  - filter 允许 false positive，但不允许 false negative。
- 说明传统 Bloom filter / dictionary 通常需要初始化容量 `N`，空间按 `N` 占用。
- 引出核心矛盾：实际当前大小 `n` 可能远小于 `N`，或者最终大小根本无法可靠预估。
- 提出 review 的主问题：能不能让空间始终随当前 `n` 变化，同时保持误报率、无漏报和最坏情况常数时间？

## 3. 问题定义与研究意义（刘威主责）

### 3.1 近似成员查询模型

- 全集 / 键空间 `[u] = {0, ..., u - 1}`。
- 当前集合 `S subseteq [u]`，当前大小 `n = |S|`。
- 说明论文按 insertion sequence 划分阶段；若讨论重复插入，需要额外说明“插入次数”与不同 key 数量的关系。
- 操作：
  - `insert(x)`：插入元素；
  - `lookup(x)`：判断元素是否属于集合。
- dictionary：精确回答 membership query。
- filter：对 `x in S` 必须回答 YES；对 `x notin S` 可以以概率至多 `epsilon` 回答 YES。
- 区分两种概率：
  - 数据结构报告 failure 的概率；
  - 无 failure 条件下 filter 的 false positive rate。

### 3.2 已知容量 `N` 与未知最终规模

- 已知容量 `N` 时，经典 filter 空间主项约为 `N log(1/epsilon)` bits。
- 当 `n << N` 时，按 `N` 预分配导致空间浪费。
- 当 `N` 只是保守估计时，浪费可能长期存在。
- 本文的 unknown sizes 指：初始化时没有紧的最终规模上界，但结构仍需让空间依赖当前 `n`。

### 3.3 为什么 filter 不能简单扩容

- exact dictionary 保存足够信息，可以扩容后枚举旧 key 并重建。
- filter 为节省空间丢失原始 key 信息，旧结构通常不能恢复完整集合。
- 保留多个旧 filter 虽然避免迁移，但会导致：
  - 查询可能检查多个阶段结构；
  - 总误报率需要对各阶段做 union bound；
  - 空间中出现额外 `log log n` 成本。

### 3.4 空间下界与重要性

- Pagh、Segev、Wieder 对 unknown-size filter 给出信息论下界：
  `(1 - o(1)) n (log(1/epsilon) + (1 - O(epsilon)) log log n)`。
- 因此 `log log n` 不是普通工程实现造成的浪费，而是未知规模模型中的理论成本。
- 本文重要性在于：
  - 把 `log log n` 项的领先常数做到 1；
  - 同时避免 expected amortized insertion，达到以高概率最坏情况常数时间。
- 谨慎说明：
  - 本文公式 (2) 解释构造中 `log log n` 如何产生；
  - “任何 unknown-size filter 都不可避免该项”来自 PSW 信息论下界；
  - 在没有精读 PSW 原文前，不展开声称其完整证明已经验证。

## 4. 相关研究与对比框架（陈戚主责，刘威/张书铖协助核查）

这一节不能只列文献，需要围绕“是否真正解决本文问题”来比较。

### 4.1 Bloom filter 与 approximate membership

- 说明 Bloom filter 解决的是允许误报的成员查询。
- 对比点：
  - 是否需要预知容量；
  - 是否无 false negative；
  - 空间是否达到信息论意义上的 succinct；
  - 是否支持最坏情况常数时间。

### 4.2 Dynamic / scalable Bloom filter

- 重点核查 Almeida et al. scalable Bloom filter、dynamic Bloom filter 等工程扩容方案。
- 不可直接写成“已经解决本文问题”，除非逐项满足：
  - 不预知最终 `n`；
  - 总误报率严格受控；
  - 空间相对当前 `n` 达到本文所需的理论界；
  - 查询和插入具有最坏情况常数时间或可比较保证。
- 成员 B 已指出：若只是工程上可扩容、空间多常数因子或查询需多个结构，则只能作为相关方案，不能视为本文结果的替代。

### 4.3 Succinct dictionary 与动态 hashing

- Raman and Rao 的 succinct membership / dictionary：空间随当前 `n`，但插入为 expected amortized constant time。
- FKS、Dietzfelbinger 等动态 hashing：提供 worst-case / high probability 时间保证，但空间是否 succinct 需要区分。
- Arbitman、Naor、Segev 的 de-amortized cuckoo hashing：用于解释 worst-case constant time with high probability 的技术背景。

### 4.4 Quotient filter / cuckoo filter

- 需要避免只从“是否支持删除”“实际性能好不好”比较。
- 本 review 应核查：
  - 是否依赖容量或负载因子上界；
  - 是否允许 unknown-size 增长；
  - 删除支持是否与本文模型可比；
  - 空间和误报率是否达到本文级别的理论保证。

### 4.5 Pagh、Segev、Wieder 的 unknown-size filter

- 这是本文最直接的前作：
  - 给出 unknown-size filter 的信息论下界；
  - 构造空间接近下界；
  - 插入为 expected amortized constant time；
  - `log log n` 项领先常数未完全钉死。
- 本文相对它的改进：
  - `log log n` 项领先常数达到 1；
  - 插入和查询均为 worst-case `O(1)` with high probability。

### 4.6 后续研究

- 成员 C 后续补充 2020 年之后研究。
- 比较表至少包含：
  - 问题模型；
  - 是否需要容量上界；
  - 是否支持删除；
  - 空间界；
  - 查询 / 插入时间；
  - 是否引用或改进本文；
  - 结论来源：摘要、正文、定理或实验。

## 5. 论文主要结果

### 5.1 Dynamic filter

- 非正式结果：维护 approximate membership，误报率 `epsilon`，当前大小 `n > u^0.001` 时使用
  `(1 + o(1)) n (log(1/epsilon) + log log n)` bits。
- 插入和查询：worst-case constant time with high probability。
- 正式 Theorem 10：
  - `0<epsilon<1`；
  - `n=omega(log u)` 且 `n<u`；
  - 主体空间为
    `n(log(1/epsilon)+log log n+O(log log log u))` bits；
  - 另有与输入无关的 `u^c` 位预计算空间；
  - 对任意插入序列，曾报告 failure 的概率至多 `delta=u^{-C}`；
  - 无 failure 时，每个查询的误报率至多 `epsilon`。
- Theorem 1 与 Theorem 10 的衔接：
  - `n>u^0.001` 时，`log log log u=o(log log n)`；
  - 选 `c<0.001` 时，`u^c=o(n)`；
  - 因而低阶项可吸收到 `(1+o(1))`。
- `epsilon=o(1)` 的作用：使 PSW 下界中的 `(1-O(epsilon))` 趋近 1，从而支持“`log log n` 领先常数最优”的表述。

### 5.2 Dynamic dictionary

- 非正式结果：维护 key-value pairs，空间约为
  `(1 + o(1)) n (log(u/n) + v + O(log log log u))` bits。
- 当 `v = 0` 时退化为 membership。
- 与 filter 的关系：filter 可通过哈希前缀 / prefix matching 使用 dictionary 类结构作为底层引擎。

### 5.3 与前作的结果对比

- 已知容量 filter：空间主项 `N log(1/epsilon)`。
- PSW unknown-size filter：有理论下界和近似匹配构造，但插入为均摊期望，且 `log log n` 项领先常数未定。
- 本文：当前规模空间 + 最优领先常数 + 去均摊化最坏情况常数时间。

## 6. 核心技术直觉（张书铖主责）

### 6.1 全局哈希与变长前缀

- 使用全局 `(c_1 log u)`-wise independent hash `h:[u]→[u^{c_2}]` 把 key 映为长二进制串。
- 第 `i` 阶段保存长度约为
  `ell_i = i + log(1/epsilon) + log i + log log log u + 2`
  的前缀。
- 直觉：
  - 阶段 `i` 中约有 `2^i` 个匹配机会，`i` 抵消这一数量；
  - `i` 约为 `log n`；
  - 前缀越长，误报概率越小；
  - `log i` 对应总误报率并合预算；
  - 最终形成 `log log n` 级别的额外空间。
- 公式 (2) 的并合骨架：
  `sum_i 2^i 2^{-ell_i} < epsilon`。

### 6.2 Filter 到 prefix matching 的化归

- 插入 `x` 时保存 `h(x)` 的某个前缀。
- 查询 `y` 时检查数据库中是否存在某个已存字符串是 `h(y)` 的前缀。
- 若 `y` 已插入，则对应前缀存在，因此无 false negative。
- 若 `y` 未插入，则误报来自随机前缀碰撞，由前缀长度和 union bound 控制。

### 6.3 短字符串与长字符串分开处理

- 短前缀：用 truth table `T_i` 处理，大小约 `2^i = O(n)`。
- 长前缀：交给已知容量结构 `D(m, ell)`，支持 succinct 存储和 prefix query。
- 这一拆分避免 PSW 旧方案中短串复制到统一长度带来的复杂处理。

### 6.4 分阶段增长与后台迁移

- 阶段 `i` 处理大约第 `2^{i-1}+1` 到第 `2^i` 次插入。
- 活跃结构包括 `T_{i-1}, T_i, D_{i-1}, D_i`。
- 每次插入后将维护过程重复 10 轮：
  - 从旧 truth table 迁移到新 truth table；
  - 从旧 `D` 迁移到新 `D` 或 `T`；
  - 逐步 destroy 旧结构、initialize 下一阶段结构。
- 目标：扩容过程中仍可查询，且不会出现一次 `Theta(n)` 的慢插入。
- 8 元素教学示例用于解释：
  - `n=1,2,3-4,5-8` 时分别使用阶段 `i=0,1,2,3`；
  - 新前缀默认进入当前 `D_i`；
  - `T_i` 主要接收迁移得到的短串；
  - 示例哈希前缀是人为设定，不能用于证明概率。

### 6.5 Data block 的作用

- 底层 `D(m, ell)` 使用 main table / subtable / data block。
- data block 按插入时间分块：
  - 最新块支持动态插入；
  - 满块在后台重组为静态紧凑编码。
- B 的笔记指出：data block 是降低冗余的关键，使每 key 额外冗余从约 `O(log log u)` 降到约 `O(log log log u)`，从而不破坏 filter 的 `log log n` 领先常数。

## 7. 数据结构实现细节（张书铖主责）

### 7.1 Filter 层 Lookup 流程

- 输入 `y`。
- 计算 `h(y)`。
- 根据当前 `n` 得到阶段 `i`。
- 查询常数个结构：
  - `D_{i-1}`；
  - `D_i`；
  - `T_{i-1}`；
  - `T_i`。
- 任一命中则返回 YES，否则返回 NO。

### 7.2 Filter 层 Insert 流程

- 输入 `x`。
- 计算当前阶段前缀 `s`。
- 如果没有更短前缀已存在，则插入 `D_i`。
- 重复 10 轮维护步骤，推进旧结构到新结构的迁移：
  - `T_{i-1}` 中取出的串扩展两个孩子写入 `T_i`；
  - `D_{i-1}` 中取出的串按长度进入 `D_i` 或 `T_i`；
  - 逐步销毁旧结构并初始化下一层。
- 待证明：常数 10 为什么足以同时配平 `decrement`、`destroy` 和 `initialize`。

### 7.3 底层 `D(m, ell)` 的结构

- main table：按 `st(x)` 分桶。
- subtable：桶内组织数据。
- adaptive prefixes：用短唯一前缀定位候选 key / block。
- navigator / indicator：定位具体 data block。
- data block：静态块紧凑编码，动态块支持插入并后台重组。

### 7.4 去均摊化

- 将 initialize、destroy、decrement、block reorganization 等耗时过程拆成每次插入后的常数步。
- 证明目标：单次 insert 的真实耗时也是常数，而不是均摊常数。

## 8. 正确性证明框架（刘威、张书铖共同）

### 8.1 无 false negative

- 已插入元素的哈希前缀始终保存在某个活跃结构中。
- 迁移中间态必须保持“旧结构未删完前仍可查询，新结构已接收的也可查询”。

### 8.2 误报率不超过 `epsilon`

- 非成员误报等价于 `h(y)` 与某个已存前缀匹配。
- 对每个阶段估计碰撞概率。
- 对所有阶段做 union bound。
- 前缀长度 `ell_i` 的设置正是为了让总和不超过 `epsilon`。
- 必须写明该结论是在底层结构没有报告 failure 的条件下成立。

### 8.3 Prefix matching 正确性

- 短串由 truth table 覆盖。
- 长串由 `D(m, ell)` 处理。
- 需要证明查询只检查常数个结构仍不遗漏。

### 8.4 迁移正确性

- 关键不变式：
  - 任一已插入串在 `T_{i-1}, T_i, D_{i-1}, D_i` 中至少存在一个可查询表示；
  - 旧结构中元素被迁出后才可删除；
  - 阶段结束前下一阶段结构已准备好。
- 待核查：
  - Claim 13 中阶段不变式下标与 `i=ceil(log n)` 的边界对齐；
  - 每次 10 轮维护的严格进度配平。

## 9. 空间复杂度证明框架（刘威主责，张书铖协助）

- Lemma 11 给出 prefix matching 空间
  `n(ell_{ceil(log n)}-log n+O(log log log u))`。
- 代入前缀长度后得到
  `n(log(1/epsilon)+log log n+O(log log log u))`。
- 正式定理还需单列与输入无关的 `u^c` 位预计算空间。
- truth table 的 `O(n)` 空间需说明为何是低阶或可吸收。
- `D(m, ell)` 的额外冗余约 `O(log log log u)` / key，需要证明不破坏主项领先常数。
- 与 PSW 下界对齐：
  - 下界说明 `log log n` 不可避免；
  - 当 `epsilon=o(1)` 时，本文上界把该项领先常数做到 1。

## 10. 时间复杂度证明框架（张书铖主责，刘威核查）

- lookup：只查询常数个结构，所以最坏情况 `O(1)`。
- insert：本次插入 + 常数步后台维护，所以最坏情况 `O(1)`。
- 底层结构中的 block 重组也需证明被拆成常数步。
- 高概率保证来自：
  - bucket 负载集中；
  - adaptive prefixes 可维护；
  - hash / collision 失败事件总概率可并合。

## 11. 技术优越性与局限

### 11.1 优越性

- 空间依赖当前 `n`，不依赖预设容量 `N`。
- 达到 unknown-size filter 下界中的 `log log n` 领先常数。
- 同时支持 worst-case constant time with high probability，而不是 expected amortized insertion。
- 数据迁移过程中仍可查询，避免停机式重建。

### 11.2 局限与谨慎表述

- 区分非正式条件 `n>u^0.001` 与正式条件 `n=omega(log u), n<u`。
- 不隐藏输入无关的 `u^c` 位预计算空间。
- 模型依赖 RAM、extendable arrays、高独立性哈希或随机化假设。
- 实现复杂度远高于工程 Bloom filter。
- 不应写成“全面优于 Bloom filter”；更准确说是在特定理论模型和 unknown-size 目标下取得更强保证。

## 12. 后续研究与评价（陈戚主责）

- 2020 年之后是否有直接引用或改进本文的工作。
- learned Bloom filter、adaptive filter、dynamic filter、succinct hashing 等方向与本文模型是否一致。
- 对每篇后续文献记录：
  - 是否正式发表；
  - 是否引用本文；
  - 改进的是空间、时间、删除、适应性还是实现性能；
  - 结论来自摘要、正文还是定理。

## 13. 结论

- 本文解决的问题不是普通“可扩容 Bloom filter”，而是 unknown-size 场景下的最优空间和最坏情况时间同时达成。
- 论文核心技术路线：
  - 哈希前缀化；
  - prefix matching；
  - 短串 truth table；
  - 长串 succinct membership；
  - 分阶段后台迁移；
  - data block 降低冗余。
- 小组最终评价应同时说明理论贡献、模型限制和实现复杂度。

## Day 2 整合状态

### 已完成

- 刘威核查正式模型、Theorem 1/10、参数、failure 与 false positive 的区别；
- 刘威整理 PSW 下界的可靠表述，并明确完整证明仍待原文核查；
- 张书铖核查公式 (2)、Claim 13、四结构查询和 10 轮维护；
- 张书铖完成 8 元素阶段增长示例及查询/插入文字流程图；
- A、B 的材料已汇总到 `discussions/meeting-day2.md`。

### 进入 Day 3 前待补

- 陈戚补全相关工作笔记、来源、BibTeX 和 `references/literature-matrix.md`；
- 陈戚审阅 B 的 8 元素示例；
- 刘威对 B 的示例留下正式审阅结论；
- 张书铖复核 A 对 Day 2 审阅意见的修改；
- 解决 Claim 13 下标对齐和常数 10 的配平问题；
- 开始拆解底层 `D(m,ell)`、truth table 和 data block。
