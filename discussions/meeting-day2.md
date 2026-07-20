# Day 2 会议记录：正式模型、主要结果与阶段构造

日期：2026-07-20

记录性质：根据刘威（A）和张书铖（B）已完成的 Day 2 笔记整理，用于会前/会中同步和后续追踪。陈戚（C）的相关工作矩阵与交叉审阅尚未完成，因此本文不把 C 的观点或三人共同结论写成已确认事实。

## 1. 当前完成情况

| 成员 | 已完成内容 | 对应文件 | 状态 |
|---|---|---|---|
| A 刘威 | 正式模型、Theorem 1/10 参数区别、空间下界与高概率语义 | `notes/memberA/definitions.md`、`lower-bound-notes.md`、`paper-reading.md` | 已完成初稿并对照本文核查 |
| B 张书铖 | 哈希前缀、公式 (2)、Claim 13、8 元素阶段示例、查询/插入图 | `notes/memberB/construction-notes.md`、`proof-notes.md`、`figures/*.md` | 已完成初稿并对照本文核查 |
| C 陈戚 | 经典相关工作矩阵、来源清单、对 B 示例的审阅 | 计划中的 `notes/memberC/`、`references/` | 尚未完成 |

“已完成初稿”不等于可直接进入终稿。PSW 下界证明、Claim 13 常数 10 的配平、底层 `D(m,ell)` 空间等仍需 Day 3 继续核查。

---

## 2. A 刘威讲解要点：问题模型与参数

### 2.1 模型

- 全集为 `[u]={0,1,...,u-1}`，当前逻辑集合为 `S`，当前大小为 `n=|S|`。
- `insert(x)` 插入 key；`lookup(x)` 查询 key 是否在集合中。
- Dictionary 必须精确回答。
- Filter 对成员必须回答 YES，即不允许 false negative；对非成员可以以至多 `epsilon` 的概率回答 YES。
- “Unknown sizes”指初始化时不知道最终集合大小或紧容量上界 `N`，不是说全集 `u` 或当前 `n` 未知。

### 2.2 两类概率不能混淆

Theorem 10 区分：

1. 数据结构报告 failure 的概率；
2. 无 failure 条件下 filter 的 false positive rate。

正式定理令 `delta=u^{-C}`，其中 `C>1`。对任意插入序列，整个过程中曾报告 failure 的概率至多为 `delta`。在无 failure 条件下，每个查询的误报率至多为 `epsilon`，且没有漏报。

### 2.3 Theorem 1 与 Theorem 10

| 项目 | 非正式 Theorem 1 | 正式 Theorem 10 |
|---|---|---|
| `n` 条件 | `n>u^0.001` | `n=omega(log u)` 且 `n<u` |
| 主体空间 | `(1+o(1))n(log(1/epsilon)+log log n)` | `n(log(1/epsilon)+log log n+O(log log log u))` |
| 额外空间 | 简洁表述中未单列 | 输入无关的 `u^c` 位预计算空间 |
| 时间 | whp worst-case `O(1)` | 每次操作 worst-case `O(1)`，整个失败事件概率至多 `u^{-C}` |

当 `n>u^0.001` 且选取 `c<0.001` 时，`u^c=o(n)`；同时 `log log log u=o(log log n)`，所以正式空间式可整理成 Theorem 1 的 succinct 表达。

### 2.4 下界的严谨表述

- 已知容量 filter 的经典空间基准为 `N log(1/epsilon)` bits。
- PSW 对 unknown-size filter 给出
  `(1-o(1))n(log(1/epsilon)+(1-O(epsilon))log log n)` 下界。
- 本文公式 (2) 可以解释本文构造为什么出现 `log log n`，但不能代替 PSW 的信息论下界证明。
- 当 `epsilon=o(1)` 时，`1-O(epsilon)` 趋近 1，本文才能明确声称 `log log n` 项达到最优领先常数。

---

## 3. B 张书铖讲解要点：构造与 8 元素示例

### 3.1 从 key 到变长前缀

全局哈希 `h` 把 key 变成足够长的二进制串。第 `n` 次插入令 `i=ceil(log n)`，保存前 `ell_i` 位：

```text
ell_i = i + log(1/epsilon) + log i + log log log u + 2
```

- `i` 抵消阶段内约 `2^i` 个 key 的匹配机会；
- `log(1/epsilon)` 对应基本误报预算；
- `log i` 让不同阶段的误报概率可以求和；
- `log log log u` 和常数 2 提供低阶冗余与概率余量。

### 3.2 查询化为 prefix matching

插入时保存 `h(x)` 的前缀；查询 `y` 时检查是否有已存字符串是 `h(y)` 的前缀。

当当前阶段为 `i` 时，只检查：

```text
D_{i-1}, D_i, T_{i-1}, T_i
```

结构数量恒为常数，因此上层查询不需要扫描 `O(log n)` 个历史 filter。

### 3.3 8 元素示例的结论

| 当前 `n` | `i=ceil(log n)` | 新元素主要进入 | 查询结构 |
|---:|---:|---|---|
| 1 | 0 | `D0` | `D0,T0` |
| 2 | 1 | `D1` | `D0,D1,T0,T1` |
| 3-4 | 2 | `D2` | `D1,D2,T1,T2` |
| 5-8 | 3 | `D3` | `D2,D3,T2,T3` |

示例中的具体前缀是教学设定，不代表真实哈希输出，也不能用于证明碰撞概率。

### 3.4 每次插入后的维护

每次插入后，Claim 13 把以下过程重复 10 轮：

1. 从旧 `T_{i-1}` 取短串，扩展为两个孩子写入 `T_i`；
2. 从旧 `D_{i-1}` 取串，按长度迁入 `D_i` 或 `T_i`；
3. 旧结构为空后逐步 destroy；
4. 旧结构销毁后逐步 initialize 下一阶段结构。

已确认原文确实写“重复 10 次”，但“为什么常数 10 对所有进度都足够”的配平证明仍待 Day 3 展开。

---

## 4. 共同讨论题的阶段结论

以下结论由 A、B 已完成材料共同支持；正式会议后仍应由本人确认记录是否准确。

### 4.1 `log(1/epsilon)` 是什么成本

这是降低非成员误报概率所需的基本区分信息。`epsilon` 越小，`log(1/epsilon)` 越大，每个 key 平均需要更多位。

状态：**已由本文公式与经典空间基准核实。**

### 4.2 `log log n` 是什么成本

- 构造直觉：阶段编号 `i` 约为 `log n`，阶段误报预算带来 `log i≈log log n`。
- 理论不可避免性：来自 PSW 信息论下界，而不是仅由本文分阶段设计推出。

状态：**上界来源已核实；PSW 完整下界证明待查。**

### 4.3 `(1+o(1))` 修饰什么

它修饰：

```text
n(log(1/epsilon)+log log n)
```

表示总空间与该主表达式之比趋近 1，不代表小规模实例没有常数开销。简洁表达需要 `n>u^0.001` 等条件来吸收低阶项和预计算空间。

状态：**已核实。**

### 4.4 whp worst-case 与 expected amortized

- expected：对随机性取平均后为常数；
- amortized：一串操作平均为常数，某次可能很慢；
- worst-case：每次操作本身为常数；
- 本文：除概率至多 `u^{-C}` 的 failure 事件外，每次插入和查询都满足 worst-case `O(1)`。

状态：**已核实。**

### 4.5 8 元素示例是否忠实 Claim 13

忠实部分：

- `i=ceil(log n)`；
- 新前缀默认进入 `D_i`；
- 查询四个结构；
- 每次插入后执行 10 轮维护；
- 长短串迁移去向。

仍待验证部分：

- Claim 13 阶段不变式的下标与 `ceil(log n)` 在边界处的逐项对齐；
- 常数 10 的完整配平；
- 示例未展示底层 `D(m,ell)`。

状态：**教学骨架可用，但不能代替证明。**

### 4.6 哪些文献真正满足 unknown-size 模型

C 的文献矩阵尚未完成，A/B 目前只能提出判断标准：

- 是否无需紧容量上界；
- 空间是否依赖当前 `n`；
- 是否严格控制总误报率；
- 查询和插入保证属于 worst-case、expected 还是 amortized；
- 是否达到 succinct 而不只是工程可扩容。

状态：**待 C 查证，不能形成小组结论。**

---

## 5. 交叉审阅与回应

### 5.1 B 审 A

| # | 被审位置 | B 的意见 | A 已做修改 | 当前状态 |
|---|---|---|---|---|
| 1 | `definitions.md` 当前 `n` | “第 n 次插入”可能与去重后的 `|S|` 混淆 | A 已增加重复插入说明，并说明 review 采用论文 insertion-sequence 模型 | 已回应，待 B 复核 |
| 2 | `definitions.md` 概率/时间 | failure 应是整段序列概率，不是单次独立失败；需区别 expected amortized | A 已分节说明 `u^{-C}`、false positive、expected/amortized/worst-case | 已回应，待 B 复核 |

### 5.2 A 对 B 的核查问题

A 在 `paper-reading.md` 中提出：

1. 8 元素例子是否始终只查询四个结构；
2. 是否区分迁移、destroy 和 initialize；
3. 教学哈希串是否明确标为人为设定。

B 的现有材料已经分别说明四结构查询、四步维护和教学示意前缀。
当前状态：**材料层面已回应，待 A 正式留下审阅结论。**

### 5.3 C 审 B

待 C 审阅：

- `notes/memberB/construction-notes.md` 第 6 节；
- `figures/growth-process.md`；
- `figures/query-insert-flow.md`。

重点检查未读论文者能否跟随，以及是否误把教学示例当成正式概率证明。

### 5.4 A 审 C

由于 `references/literature-matrix.md` 尚不存在，本项无法执行。C 完成矩阵后，由 A 核查空间/时间界和模型可比性。

---

## 6. 问题状态变化

### Day 2 已关闭

1. unknown size 的基本定义；
2. Theorem 10 的正式 `n`、空间和 failure 条件；
3. `log(1/epsilon)` 与构造中 `log log n` 的来源；
4. `(1+o(1))` 的含义；
5. whp worst-case 与 expected amortized 的区别；
6. 新元素去向、四结构查询和 10 轮维护的原文位置。

### 仍待 Day 3

1. PSW 下界的完整证明；
2. Claim 13 下标边界的严格对齐；
3. 常数 10 的配平证明；
4. 四个活跃结构并存时的严格空间峰值；
5. truth table 的 `O(n)` 空间如何吸收；
6. 底层 `D(m,ell)` 怎样自动支持长字符串 prefix matching；
7. 经典相关工作和 2020 年后工作矩阵。

---

## 7. 会议后行动项

| 行动 | 负责人 | 产物 | 截止阶段 |
|---|---|---|---|
| 复核 A 对两条审阅意见的修改 | 张书铖 | PR/会议记录中的确认 | Day 2 收尾 |
| 对 B 的 8 元素示例留下正式审阅 | 刘威 | 至少 2 条具体评论 | Day 2 收尾 |
| 补齐相关工作矩阵和来源 | 陈戚 | `references/literature-matrix.md` 等 | 进入 Day 3 前 |
| 审阅 B 示例是否清楚 | 陈戚 | 至少 2 条具体评论 | 进入 Day 3 前 |
| 精读 Claim 13 常数配平和下标 | 刘威、张书铖 | 问题结论或证明表 | Day 3 |

## 8. 口头检查

A、B 当前应能分别讲清自己的主责内容，还应进行一次互换复述：

- 刘威复述：8 元素示例中新 key、旧结构迁移和四结构查询；
- 张书铖复述：Theorem 1/10 区别、`u^{-C}` 与 `epsilon` 的区别、PSW 下界的严谨表述。

C 完成材料后，三人再回答“scalable Bloom filter 为什么不能直接替代本文结果”，届时才把 Day 2 会议标记为三人完整完成。
