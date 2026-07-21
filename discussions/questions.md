# 问题清单

初建日期：2026-07-17
最近更新：2026-07-20（根据 A、B Day 2 材料整理）

分类：

- Q0：已通过本文原文核查到当前所需精度；
- Q1：有明确结论，但还需要进一步证明或交叉复核；
- Q2：核心机制仍未理解；
- Q3：论文细节需要展开验证；
- Q4：成员表述存在分歧。

## Q0：Day 2 已解决

### A：模型、参数与空间

1. **Unknown sizes 未知的是什么？**
   - 结论：未知的是最终集合大小或紧容量上界 `N`；全集 `u` 和当前大小并非该短语所说的“未知”。
   - 位置：第 1-2 页；A `definitions.md` §6。

2. **Filter 是否允许 false negative？**
   - 结论：不允许；对成员必须回答 YES，对非成员可有至多 `epsilon` 的 false positive rate。
   - 位置：第 2 页；Theorem 10 第 4 条。

3. **`log(1/epsilon)` 与 `log log n` 分别是什么成本？**
   - 结论：前者是控制误报的基本信息成本；本文构造中的后者来自多阶段误报预算的 `log i`，其普遍不可避免性由 PSW 下界证明。
   - 位置：第 2 页、公式 (2)；A `lower-bound-notes.md` §2-3。

4. **Theorem 1 与 Theorem 10 的 `n` 条件为何不同？**
   - 结论：非正式 Theorem 1 用 `n>u^0.001` 给出 `(1+o(1))` 简洁空间；正式 Theorem 10 适用于 `n=omega(log u), n<u`，并保留 `O(log log log u)` 和 `u^c` 预计算空间。
   - 渐近衔接：选 `c<0.001` 时 `u^c=o(n)`，且 `log log log u=o(log log n)`。
   - 位置：第 3 页 Theorem 1；第 9 页 Theorem 10。

5. **High probability worst-case `O(1)` 是什么意思？**
   - 结论：正式定理令 `delta=u^{-C}`。对任意插入序列，曾报告 failure 的概率至多 `delta`；无 failure 时，每次插入与查询为 worst-case `O(1)`。
   - 注意：failure 概率与 filter 的 false positive rate 是两种概率。
   - 位置：Theorem 10 第 2-4 条。

6. **`epsilon=o(1)` 有什么作用？**
   - 结论：使 PSW 下界中 `(1-O(epsilon))` 趋近 1，因此本文可以声称 `log log n` 项达到最优领先常数。
   - 位置：摘要；A `lower-bound-notes.md` §5。

### B：构造与迁移

7. **每次插入是否执行 10 轮维护？**
   - 结论：是。原文写明 “execute the following procedure for 10 times”。
   - 位置：Claim 13 证明。

8. **新插入默认进入 `D_i` 还是 `T_i`？**
   - 结论：若没有更短已存前缀，新串进入 `D_i`；`T_i` 主要处理迁移得到的短串。
   - 位置：Claim 13。

9. **查询是否只检查常数个结构？**
   - 结论：检查 `D_{i-1},D_i,T_{i-1},T_i`。
   - 位置：Claim 13 末段。

10. **8 元素示例中的比特串能否用于概率证明？**
    - 结论：不能。它们只是演示状态变化的人为示意前缀。
    - 位置：B `construction-notes.md` §6。

## Q1：有结论但仍需验证

1. **PSW 下界的完整证明如何推出 `log log n` 不可避免？**
   - 当前结论：本文只引用该信息论下界；阶段误报预算只能解释本文上界，不能代替下界证明。
   - 下一步：精读 PSW [28] 的编码对象、关键规模和误报集合。
   - 负责人：刘威，陈戚协助核查文献。

2. **`n>u^0.001` 是否还用于其他概率步骤？**
   - 当前结论：其主要作用是吸收 `u^c` 和 `O(log log log u)`，但不能在未逐节核查前断言它与后续概率分析完全无关。
   - 下一步：检查第 5 节全部参数调用。
   - 负责人：刘威、张书铖。

3. **Claim 13 的阶段下标如何与 `i=ceil(log n)` 严格对齐？**
   - 问题：原文不变式使用 `n∈[2^i,2^{i+1})`，操作中又令 `i=ceil(log n)`；需要统一自由变量。
   - 下一步：对照附录伪代码和阶段边界重写一份不变式。
   - 负责人：张书铖，刘威复核。

4. **B 的 8 元素示例是否可以作为 Review 教学例子？**
   - 当前判断：新串去向、四结构查询和迁移骨架与 Claim 13 一致。
   - 待完成：A、C 正式审阅；边界下标问题解决后再进入正文。

5. **重复插入时“第 n 次插入”与 `n=|S|` 如何处理？**
   - 当前结论：A 已在定义中说明 review 暂按论文 insertion-sequence 模型讲解；不能未经说明把重复插入次数等同于不同 key 数。
   - 待完成：B 复核该表述是否足够。

## Q2：仍未理解的核心机制

1. **常数 10 为什么足够？**
   - 需要证明它能同时覆盖 `decrement`、`destroy` 和 `initialize` 的全部进度，并在一个阶段结束前完成。
   - 计划：计算各接口最多需要多少次调用，与阶段长度 `Theta(2^i)` 配平。

2. **新的 exact membership 结构为什么能自动解决长字符串 prefix matching？**
   - 计划：Day 3 拆解 `D(m,ell)` 接口、core set 与查询方法。

3. **Data block 如何把每 key 冗余降低到 `O(log log log u)`？**
   - 计划：逐项分析动态块、静态块、adaptive prefix 和 navigator。

## Q3：需要展开验证的细节

1. 新旧结构“几乎原地”并存时，空间峰值如何严格控制？
2. Truth table 的 `O(n)` 空间如何吸收到总空间界？
3. 四个活跃结构的空间如何求和得到 Lemma 11？
4. 第 5 节各类 failure 如何通过式 (3)(4)(5) 并合到 `u^{-2C}`？
5. 实际实现中 `u^c` 预计算表和高独立性哈希的常数开销如何理解？
6. 8 元素教学例子没有展示真实 `ell_i` 长度差异，正式空间证明不能依赖该例子。

## Q4：成员理解差异

目前没有仍未记录处理方案的直接分歧。

Day 2 原有分歧“第 n 次插入与 `n=|S|` 是否混用”已转入 Q1.5：A 已修改，等待 B 复核，不再视为无人回应的分歧。

## C 材料缺口

以下问题必须等待陈戚的文献矩阵，A/B 现阶段不代替 C 下结论：

1. Dynamic/scalable Bloom filter 是否满足本文全部 unknown-size 模型要求？
2. Quotient/cuckoo filter 是否依赖容量或负载上界？
3. 2020 年后是否有直接引用、改进或否定本文结果的研究？
4. 各相关结构的空间和时间保证属于 worst-case、expected 还是 amortized？

---

## Day 3：刘威（A）核查更新（2026-07-21）

### 转入 Q0

1. **Theorem 7/8/9 -> `D(m,ell)` -> Claim 13 -> Lemma 11 -> Theorem 10 的依赖方向。**
   - 已按原论文第 8--13 页核实并记录于 `notes/memberA/lemma-dependency-and-space.md`。
2. **Truth table 和相邻容量元数据为何只贡献 `O(n)` 量级。**
   - 相邻两个二次幂容量求和为 `O(n)`；该结论解释量级，但不替代位级峰值证明。
3. **B 的 8 元素示例是否可作为教学例子。**
   - 有条件通过：可解释 `ceil(log n)` 版操作控制流，不可证明概率、空间领先常数或一般迁移配平。

### Q1 保留

1. **PSW 下界的完整证明。**
   - 本地仅有本文 PDF；本文引用结论但未重证。编码对象、关键规模和误报集合仍须阅读 [28] 原文。
   - 负责人：刘威；文献核验：陈戚。
2. **第 5 节全部 failure 事件如何汇总。**
   - 已核查公式 (3) 的负载事件与 Theorem 8 关系；公式 (4)(5)、fingerprint 和 navigator 事件待 Day 4 逐项完成。
   - 负责人：刘威、张书铖。

### Q2 状态调整

1. **常数 10 为什么足够？**
   - 机制已理解：一个 `Theta(2^i)` 长阶段内，每次常数轮维护提供 `Theta(2^i)` 次调用，能渐进覆盖线性迁移工作。
   - 但黑盒接口只给 initialize/destroy 为 `O(m)` 次，隐藏常数未展开，不能推出字面常数 10 的严格配平。
   - 从 Q2 转为 Q3（论文可能省略常数细节）。
2. **`D(m,ell)` 为何支持长串 prefix matching？**
   - 接口层已理解：它直接提供 `query(D,x)` 判断是否存在前缀；内部由 main table、subtable、adaptive prefixes/data blocks 实现。
   - 位级实现尚未全部展开，转为 Q1/Q3，B 主查、A 复核空间接口。
3. **Data block 每 key `O(log log log u)` 冗余。**
   - 仍为 Q2，属于第 5 节底层构造，A 本日只确认其在空间式中的位置，未完成实现证明。

### 新增或重写 Q3

1. **Claim 13 阶段下标冲突。**
   - 插入/查询令 `i=ceil(log n)`；证明段又写 `n in [2^i,2^{i+1})` 时使用第 `i-1/i` 层。例如 `n=3` 时两种写法给出不同层号。
   - 临时处理：教学图按明确的插入/查询语句绘制；正式归纳证明不得在未统一变量前关闭。
   - 负责人：张书铖；复核人：刘威。
2. **字面常数 10 的隐藏常数配平。**
   - 可证明常数轮渐近足够；无法由当前 `O(m)` 接口推出恰好 10。
3. **迁移瞬间位级空间峰值。**
   - 相邻层容量和为 `O(n)` 已确认；succinct 领先常数仍需结合 `decrement` 释放空间和第 5 节编码逐项核查。
4. **对手模型。**
   - 全文未找到 `oblivious adversary` 明文；定理对任意给定插入序列、以预计算随机比特为概率空间。是否覆盖 adaptive adversary 不作未经证明的扩展。

### 交叉审阅记录

刘威对张书铖材料的四条正式意见见 `discussions/review-day3-A.md`；需由 B 留下接受/修改/反驳及证据后关闭。

### PSW 原文加入后的状态更新（2026-07-21）

原 Q1“PSW 下界完整证明”转入 Q0。依据：仓库 `1304.1188v2.pdf` 第 7--10 页 Theorem 3.1、Lemma 3.2--3.4。

已核实的证明链：

1. 用 averaging/Markov 固定内部随机串，同时为至少一半插入序列保持正回答集合测度 `O(epsilon)`；
2. 将序列分成大小 `gamma^i` 的几何块，用抽屉原理选择正回答集合增长很小的一块；
3. 用 Chernoff 和 union bound 保证至少 `u^n/3` 条序列在该块开始前只有至多 `9epsilon` 比例的旧误报；
4. 保存块编号、块外元素、位置 bitmap、中间状态，并相对编码块内元素；
5. 若状态太小，总编码会短于 `log(u^n/3)`，产生计数矛盾；
6. 取 `alpha=1/sqrt(n)` 和适当增长的 `gamma`，得到额外 `Omega(n log log n)`，精细形式含 `(1-O(epsilon))` 系数。

新的核查点降为 Q1：由 Theorem 3.1 参数化公式写成 Liu--Yin--Yu 文中的精细领先系数时，请 B 独立复算 `gamma` 的选择，C 核查引用表述。A 的详细推导见 `notes/memberA/lower-bound-notes.md` §14。

---

## Day 3：张书铖（B）核查更新（2026-07-21）

### 转入 / 维持 Q0

1. **十组件接口层拆解**（哈希、变长前缀、prefix matching、四结构、迁移去向、`D(m,ℓ)` 黑盒接口）：见 `notes/memberB/core-components.md`。
2. **A 审阅四条**：全部接受；示例区分“查询活跃 / 已初始化”；证明边界写入笔记。
3. **Q1.5（重复插入与 n=|S|）**：复核 A 的 insertion-sequence 表述，**关闭分歧**。

### Q1 更新

1. **阶段下标**：升格为有明确临时变量的 Q1/Q3 混合项；操作跟 `i★`，存储归纳未关闭。负责人 B，复核 A，截止 Day 4。Issue：`discussions/issues/issue-stage-index.md`。
2. **`D(m,ℓ)` 长串 prefix matching**：接口层 Q0；§5 位级为何“membership 即 prefix matching”仍为 Q1/Q2。负责人 B，Day 4。
3. **PSW `gamma` 复算**：接受 A 安排，Day 4 独立复算后回报。

### Q2 / Q3

1. **常数 10**：维持 A 的判断——机制 Q1/渐近可讲，字面配平 **Q3**。Issue：`discussions/issues/issue-constant-10.md`。
2. **Data block `O(log log log u)`**：仍 Q2，Day 4 与 failure 式 (3)(4)(5) 一起攻。
3. **空间峰值**：仍 Q3，与 A 空间笔记对齐。

### 产物指针

- 组件：`notes/memberB/core-components.md`
- 结构图：`figures/architecture.md`
- 流程：`figures/query-insert-flow.md`
- 依赖图补注：`figures/proof-dependency.md`
- 审阅：`discussions/review-day3-B.md`
- 会议：`discussions/meeting-day3.md`
