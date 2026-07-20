# 问题清单

日期：2026-07-17（Day 1 建） / 2026-07-20（Day 2 增补）

分类说明：

- Q0：已经解决。
- Q1：有初步理解但需要验证。
- Q2：完全不理解。
- Q3：论文可能省略了细节。
- Q4：不同成员理解不一致。

## Q0：已经解决

### B / Day 2（构造侧，已对照 Claim 13）

1. **每次插入是否做 10 轮维护？**  
   - 结论：是。原文 “execute the following procedure for 10 times”。  
   - 位置：Claim 13 证明（ar5iv / PDF §4，接在 `insert(D_i,x)` 之后）。

2. **新插入默认进 `D_i` 还是 `T_i`？**  
   - 结论：默认 `insert(D_i, ·)`（若尚无更短前缀）；`T` 主要由迁移/扩展填充。  
   - 位置：Claim 13。

3. **查询是否只检查常数个结构？**  
   - 结论：检查 `D_{i-1}, D_i, T_{i-1}, T_i`，`i=⌈log n⌉`。  
   - 位置：Claim 13 末段。

## Q1：有初步理解但需要验证

1. `unknown sizes` 是否准确理解为“不预知最终集合大小或紧容量上界，而当前 `n` 可被结构知道”？
   - 验证方式：Day 2 精读正式模型和 Theorem 1。
   - **（A 主责）**

2. `log(1/epsilon)` 是否可以解释为误报率成本，`log log n` 是否可以解释为未知规模/阶段成本？
   - 验证方式：查 Pagh、Segev、Wieder 下界和本文空间分析。
   - **B 阶段性**：式 (2) 中 `log(1/ε)` 进入并合主项；`i` 与 `log i` 随阶段增长，空间代入后出现 `log log n`（§3.1 末 + Lemma 11）。是否“信息论必然”仍看 PSW 下界（A）。

3. Theorem 1 中 `n > u^0.001` 的作用是否只是技术条件？
   - 验证方式：查正式定理和后续证明中使用该条件的位置。
   - **B 注**：正式 Thm 10 写 `n=ω(log u)`；与非正式 `n>u^{0.001}` 的对齐仍由 A 主核。

4. 本文的 “with high probability worst-case constant time” 是否意味着一段 `poly(n)` 操作序列中所有操作同时常数时间？
   - 验证方式：查引言脚注和正式模型。
   - **（A 主责；B 构造侧只确认单次 Insert/Lookup 在未 failure 时步骤数为 O(1)）**

5. **（B / Day 2 新增）** Claim 13 中“`n ∈ [2^i, 2^{i+1})` 时数据在 `D_{i-1}…T_i`”的自由变量 `i`，与每次操作使用的 `i=⌈log n⌉` 在 `n∈(2^k,2^{k+1})` 时如何严格一致？
   - 验证方式：Day 3 对照附录伪代码；8 元素示例暂以 `⌈log n⌉` 的插入/查询定义为准。
   - 记录位置：`notes/memberB/construction-notes.md` §5。

## Q2：完全不理解

1. Pagh、Segev、Wieder 的信息论下界如何证明 `log log n` 项不可避免？
   - 计划：Day 3 前至少找到证明结构或二手解释。

2. 本文新的 exact membership data structure 为什么能“自动解决”长字符串 prefix matching？
   - 计划：Day 3 拆解技术组件。

3. **（B / Day 2 新增）** 常数 **10** 如何同时覆盖 `decrement`、`destroy`、`initialize` 全部进度（是否依赖 `initialize` 各需 `O(m)` 次调用与阶段长度 `Θ(2^i)` 的配平）？
   - 计划：Day 3 精读 Claim 13 与 §5 接口时间。

## Q3：论文可能省略了细节

1. 扩容迁移过程中，新旧结构“几乎原地”并存时，空间峰值如何严格控制？

2. truth table 处理短字符串时的 `O(n)` 空间如何纳入总空间低阶项？

3. **（B / Day 2）** 8 元素教学示例无法展示真实 `ℓ_i` 随 `i` 增长的比特差异；正式空间论证不能依赖该示例。

## Q4：不同成员理解不一致

1. **（B 审 A，待 A 回应）** `definitions.md` 中“第 n 次插入”与 `n=|S|`（去重后集合大小）是否在允许重复插入时被混用？建议统一为原文 insertion-sequence 语言。
