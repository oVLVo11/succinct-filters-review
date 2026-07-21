# 刘威 Day 3：引理依赖、空间分解与随机性假设核查

日期：2026-07-21  
负责人：刘威（成员 A）  
核查范围：原论文 §2.3、§2.4、§3.1、§4、§5 开头，重点为 Theorem 7--10、Lemma 11、Claim 13、公式 (2)--(5)。

## 0. 核查边界

本笔记只把原论文明确给出的命题和可以逐步复算的推导写成结论。以下内容不在本次核查中被假定为已证明：

- PSW [28] 下界的完整编码证明（首轮尚未核查；现已在下界笔记 §14 补齐证明骨架）；
- Claim 13 中字面常数 10 对所有底层接口隐藏常数都足够的严格配平；
- Claim 13 阶段区间与 `ceil(log n)` 下标差异是排版错误还是另有隐含约定；
- 第 5 节底层结构的全部位级实现细节。

## 1. 从底层工具到 Dynamic Filter 的依赖链

### 1.1 Theorem 7：有限独立哈希函数

**前提。** 字长 `w = Omega(log u)`，值域大小 `r=poly(u)`，独立性参数 `k=u^{o(1)}`。  
**结论。** 以至少 `1-1/u` 的概率成功构造可求值的 `k`-wise independent 函数；表示占 `u^{c1}` 位，每次求值 worst-case 常数时间（常数依赖 `c1`）。  
**在本文中的用途。** Theorem 10 先用全局哈希 `h:[u] -> [u^{c2}]` 将任意固定 key 序列变成具有 `(c1 log u)`-wise independence 的随机串序列。两两独立性足以支持公式 (2) 的单次前缀碰撞计算；更高有限独立性用于 Lemma 11 底层桶负载和失败概率分析。  
**原文位置。** 第 8 页 Theorem 7；第 10 页公式 (2) 前。

### 1.2 Theorem 8：有限独立条件下的 Chernoff 界

**前提。** 布尔变量是 `k`-wise independent，且 `k` 足够覆盖所需偏差。  
**结论。** 在有限独立而非完全独立下仍能取得指数型尾界。  
**用途。** 第 5 节控制主表 entry/subtable 的最大负载；例如公式 (3) 把单个 entry 超过 `c3 log u` 的概率压低，再对所有 entry 并合。  
**原文位置。** 第 8 页 Theorem 8；第 13 页公式 (3)。

### 1.3 Theorem 9：adaptive prefixes

**前提。** 输入是有限独立的随机长串序列；常数 `c0>c1>1`。  
**结论。** 以高概率存在从至少 `log log u` 位开始的最短区分前缀集合，并能以 `O(log u)` 位表示一个小集合，支持 worst-case 常数时间的 `insert/lookup/lowerbound`。  
**用途。** 第 5 节用 fingerprints/adaptive prefixes 在 data block 中压缩并定位字符串，是已知容量结构 `D(m,ell)` 的底层组成。  
**原文位置。** 第 9 页 Theorem 9；第 14 页起的 fingerprints 分析。

### 1.4 已知容量 prefix matching 结构 `D(m,ell)`

**参数。** 容量 `m<u`，字符串长度上界 `ell <= log u`。  
**接口。** `initialize`、`destroy`、`insert`、`query`、`decrement`。  
**空间接口。** 插入 `q` 个长度位于 `(log m,ell]` 的字符串后：

```text
q(ell-log m+2 log log log u) + O(m) bits
```

另有输入无关的 `u^c` 位预计算表。  
**概率接口。** 对规定分布中的 core strings，某一实例曾失败的概率至多 `u^{-2C}`。  
**迁移接口。** `decrement` 成功删除一个串时释放 `ell-log m` 位；空调用总数至多 `m`。初始化、销毁分别需连续调用 `O(m)` 次。  
**用途。** 它是 Claim 13 假设存在的“已知容量黑盒”，Claim 13 用多个实例把它提升为容量未知的 prefix matching。  
**原文位置。** 第 11--12 页，Claim 13 之前。

### 1.5 Claim 13：从已知容量到 unknown-size prefix matching

**输入组件。** `D(m,ell)` 和处理短串的 truth table `T_i`。  
**关键不变式（原文意图）。** 当前只保留相邻两个层级的 `D/T` 结构；旧层逐步 decrement、destroy，新层逐步 initialize；查询同时检查四个活跃结构。  
**用途。** 证明 Lemma 11：在 unknown size 下获得 succinct 空间、worst-case 常数时间、正确 prefix matching 和总失败概率界。  
**原文位置。** 第 12--13 页 Claim 13。

### 1.6 Lemma 11：unknown-size prefix matching

**结论。** 插入 `n` 个来自 `D_{c1 log u}` 的变长字符串后，使用

```text
n(ell_{ceil(log n)} - log n + O(log log log u)) bits
```

加输入无关的 `u^c` 位；插入/查询 worst-case `O(1)`；总失败概率至多 `delta=u^{-C}`；无 failure 时精确回答 prefix matching。  
**用途。** 它直接承接 filter 的哈希前缀序列。  
**原文位置。** 第 10 页 Lemma 11。

### 1.7 公式 (2) + Lemma 11 => Theorem 10

阶段 `i` 保存长度

```text
ell_i = i + log(1/epsilon) + log i + log log log u + 2
```

的哈希前缀。把 `ell_{ceil(log n)}-log n` 代入 Lemma 11，得到主体空间

```text
n(log(1/epsilon)+log log n+O(log log log u)) bits.
```

成员查询的已存前缀必然仍是其哈希串前缀，故无漏报；对非成员使用公式 (2) 的 union bound 控制误报。全局哈希、预计算表合计记为额外 `u^c` 位输入无关空间。  
**原文位置。** 第 9--10 页 Theorem 10、公式 (2)、Lemma 11 后两段。

## 2. 六个最终保证分别依赖什么

| 最终保证 | 直接依据 | 仍依赖的前提 |
|---|---|---|
| 无 false negative | 插入 `h(x)` 的前缀；Claim 13 四结构覆盖不变式 | 无底层 failure；迁移不丢串 |
| false positive `< epsilon` | 公式 (2)，对阶段/key 做 union bound | 查询 key 与已插入 key 的哈希前缀碰撞概率为 `2^{-ell_i}`；至少两两独立 |
| 主体空间界 | Lemma 11 空间式代入 `ell_i` | Claim 13/第 5 节对 `D/T` 并存和元数据的空间实现 |
| lookup worst-case `O(1)` | 只查 `D_{i-1},D_i,T_{i-1},T_i` | 每个底层 query worst-case `O(1)` |
| insert worst-case `O(1)` | 每次插入后执行常数轮四步维护 | 每个底层调用 worst-case `O(1)`；迁移进度能在阶段边界前完成 |
| failure 至多 `u^{-C}` | 每个 `D_i` 至多 `u^{-2C}`，对至多 `log u` 层 union bound | 第 5 节各底层 failure 界；全局哈希成功构造事件需纳入整体参数选择 |

## 3. 空间复杂度逐项分解

### 3.1 `n log(1/epsilon)`：基本误报成本（主项）

来自 `ell_i` 中的 `log(1/epsilon)`。它与已知容量 filter 的经典信息论基准相对应；`epsilon` 越小，每个 key 需要更长前缀。

### 3.2 `n log log n`：未知规模阶段成本（主项）

`ell_i` 中的 `log i` 用于让各阶段误报预算可求和；当前阶段 `i` 约为 `log n`，故为每个 key 带来约 `log log n` 位。本构造中的来源由公式 (2) 可核查；其普遍不可避免性依赖 PSW [28] 下界，而不是由公式 (2) 自行证明。

### 3.3 `O(n log log log u)`：底层冗余和误报余量（低阶候选）

来源至少包括：

- `ell_i` 中的 `log log log u`；
- `D(m,ell)` 每个串空间接口中的 `2 log log log u`；
- 第 5 节 fingerprints、data block 等压缩元数据。

在非正式 Theorem 1 的 `n>u^{0.001}` 范围内，`log log log u=o(log log n)`，因此相对 `n log log n` 为低阶项。正式 Theorem 10 保留该项，不能无条件删去。

### 3.4 Truth tables 和结构元数据：`O(n)`（低阶/线性附加项）

`T_i` 是长度 `2^i` 的 bitmap。在相邻层并存时，单纯 bitmap 长度之和为 `O(2^i)=O(n)`；`D(m,ell)` 接口还含每实例 `O(m)` 项，相邻容量求和同样为 `O(n)`。只要 `log(1/epsilon)+log log n` 渐近增长，`O(n)` 可吸收到主体式的低阶项中。

严格提醒：Claim 13 在第 13 页直接给出总体空间式，但没有在该段逐项展开迁移期间复制/分裂的所有计数。因此“相邻容量之和为 `O(n)`”解释了量级，不足以单独重建领先常数证明；领先常数仍依赖第 5 节黑盒空间接口。

### 3.5 新旧结构并存的空间峰值

Claim 13 只让相邻两代 `D/T` 活跃，因此容量项不会累加成 `O(n log n)`。迁移通过 `decrement` 释放旧 `D` 中每个成功删除串的 `ell-log m` 位，再插入新结构；这是“边释放边迁移”的空间控制接口。

能确认的结论：由 Lemma 11/Claim 13 的正式命题，总空间满足目标式。  
不能仅凭第 12 页四步流程独立确认的细节：迁移瞬间的位级峰值和隐藏常数如何精确抵消。该细节应继续保留为 Q3，而不是用“四个结构都是 O(n)”替代 succinct 领先常数证明。

### 3.6 `u^c`：输入无关预计算空间

用于表示全局有限独立哈希和 Appendix A 的预计算 lookup tables。它不是随当前数据量线性增长的主体空间，但正式 Theorem 10 必须单列。在 `n>u^{0.001}` 且选 `c<0.001` 时，`u^c=o(n)`，可在非正式 Theorem 1 中吸收。

## 4. 概率来源、独立性和对手模型

### 4.1 可以从原文确认的随机性

1. Theorem 10 的概率取自预计算随机比特；插入序列可为任意固定序列。
2. 全局 `h` 是 `(c1 log u)`-wise independent；公式 (2) 只显式使用其两两独立子性质。
3. Lemma 11 本身是确定性数据结构对随机输入分布 `D_{c1 log u}` 的保证；随机性由全局 `h` 把固定 key 序列映射后产生。
4. 第 5 节用有限独立 Chernoff 和 adaptive-prefix 事件控制底层 failure。


### 4.2 两种概率不能混淆

- false positive：无 failure 条件下，非成员哈希串命中某个已存前缀的概率，目标为 `epsilon`；
- data-structure failure：底层负载、fingerprint 等坏事件导致结构报告 fail，整个插入过程中目标为 `u^{-C}`。

二者使用不同 union bound，也有不同条件。

## 5. Claim 13 下标边界复核

原文同时出现：

1. 第 `i` 阶段是第 `(2^{i-1}+1)` 次到第 `2^i` 次插入（第 9 页）；
2. 第 `n` 次插入令 `i=ceil(log n)`，新串进 `D_i`（第 12 页）；
3. 对 `n in [2^i,2^{i+1})`，串存于第 `i-1/i` 层（第 12 页）；
4. 查询再次令 `i=ceil(log n)` 并查第 `i-1/i` 层（第 13 页）。

第 2、4 项彼此一致，也与 B 的 8 元素表一致：`n=3,4` 时查第 1/2 层，`n=5..8` 时查第 2/3 层。但第 3 项若沿用同一个 `i`，例如 `n=3` 会得到 `i=1`，从而声称活跃层是 0/1，与查询第 1/2 层不一致。

**审阅结论：** B 的示例忠实采用了算法插入/查询中明确写出的 `ceil(log n)`，可以保留为“按伪代码语句绘制的教学示例”；但不能声称它已解决 Claim 13 证明段的区间下标冲突。应把第 3 项视为待作者原意核对的 Q3，并在正式证明中先定义唯一的阶段变量再书写不变式。

建议临时记号（小组解释，不冒充原文）：令 `s(n)=ceil(log n)`，只陈述“操作访问第 `s(n)-1` 和 `s(n)` 层”；对阶段边界的完整归纳证明待 Q3 关闭后补充。

## 6. 常数 10 的配平复核

一个阶段含 `Theta(2^i)` 次插入，每次做 10 轮四步维护，因此每个维护对象得到 `Theta(2^i)` 次调用机会。量级上足以覆盖：

- truth table 最多线性次 decrement/destroy/initialize；
- `D` 最多 `m` 次空 decrement，加至多与元素数相同的成功 decrement；
- 容量为相邻二次幂的结构所需 `O(m)` 次 initialize/destroy。

但是黑盒接口只写 `O(m)`，没有在 Claim 13 前给出这些 `O(m)` 的显式常数。仅凭该接口，无法形式化推出字面常数 10 必然大于所有初始化、销毁和空 decrement 的总常数。

**结论：** 可以确认“常数轮后台工作实现去均摊化”的量级证明；不能从当前文字重建“为什么恰好 10 足够”的完整常数证明。该问题从 Q2 调整为 Q3：机制已理解，论文省略了常数配平细节。

## 7. 对 B 的 8 元素示例正式审阅

### 可接受部分

- 新串默认进入 `D_i`，而不是 `T_i`；
- 查询按 `ceil(log n)` 检查 `D_{i-1},D_i,T_{i-1},T_i`；
- 短串由旧 `T` 展开成两个子串进入新 `T`；
- 旧 `D` 的串按长度进入新 `D` 或 `T`；
- 每次插入后执行 10 轮维护；
- 示例明确标注比特串是教学设定，不能用于概率证明。

### 必须修改或保留警告的部分

1. `n=1` 时直接写 `D0,T0` 是合理的初始化简化，但 Claim 13 初始还同时构造 `T1,D1`；图中应说明“查询实际需要”与“后台已初始化结构”不同。
2. 阶段表遵循 `ceil(log n)`，与 Claim 13 证明中的半开区间句存在下标冲突；必须链接本笔记 §5 的 Q3。
3. 8 个元素远不足以展示 `D(m,ell)` 的 failure、空间领先常数或常数 10 的一般配平；示例只能说明控制流。

## 8. PSW 下界与本文上界的关系（补充核查）

仓库新增 `1304.1188v2.pdf` 后，已核查 PSW Theorem 3.1 和 Lemma 3.2--3.4。PSW 下界不参与 Theorem 10 的构造正确性证明，而用于证明其空间上界的优越性：

```text
PSW Theorem 3.1
  -> 固定随机性，保留大量低误报序列
  -> 几何块中存在正回答集合增长很小的一块
  -> 用该块前后的正回答集合和中间状态编码插入序列
  -> 状态过小会违反至少 log(u^n/3) 位的计数下界
  -> unknown-size filter 必须支付 Omega(n log log n) 额外空间。
```

必须区分：公式 (2) 说明本文构造如何支付 `n log log n`；PSW 编码证明说明任何结构都无法普遍避开这一量级。完整证明骨架和参数转化见 `notes/memberA/lower-bound-notes.md` §14。

## 9. Day 3 结论与未决项

### 已核实

- Theorem 7/8/9、已知容量 `D(m,ell)`、Claim 13、Lemma 11、公式 (2)、Theorem 10 的依赖方向；
- 主空间项和低阶项的来源；
- false positive 与 failure 的概率空间不同；
- B 示例忠实反映 `ceil(log n)` 版操作流程；
- 常数轮迁移在渐近量级上足够支撑 worst-case 去均摊化。
- PSW 下界的 averaging、几何块选择、编码矛盾和参数代入已由原文核实。

### 仍待核查

- Claim 13 阶段区间的下标冲突；
- 字面常数 10 的隐藏常数配平；
- 迁移期间位级空间峰值的完整展开；
- 原文保证能否扩展到 adaptive adversary；
- PSW 精细领先系数的参数选择仍需组内交叉复算，但证明骨架已不再属于未读材料。
