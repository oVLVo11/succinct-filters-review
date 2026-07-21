# Day 3 交叉审阅：张书铖（B）审阅刘威（A）

日期：2026-07-21  
审阅人：张书铖（B）  
被审文件：`notes/memberA/lemma-dependency-and-space.md`、`figures/proof-dependency.md`


## 意见 1：依赖图边 “Claim 13 → Lemma 11” 应标明下标缺口

**位置。** `figures/proof-dependency.md` 边 5；`lemma-dependency-and-space.md` §1.5。  
**问题。** 图把 Claim 13 画成已支撑 Lemma 11 的完整节点，但双方已确认阶段下标冲突未关闭。读者可能以为存储不变式已证毕。  
**建议。** 在该边注释加“算法控制流已核实；半开区间存储归纳待 issue-stage-index”。  
**B 已做：** 在 `proof-dependency.md` 追加 B 补注（见该文件文末）。

## 意见 2：随机性假设表需区分“filter FP”与“D failure”

**位置。** `lemma-dependency-and-space.md` §2 表与对手模型 Q3。  
**问题。** 表中 FP 依赖 pairwise，failure 依赖更高独立与 §5；一处合并叙述时易被读成同一概率空间事件。  
**建议。** 保持分列，并在会议中口头强调：ε 是查询正确性条件下的误报；δ 是结构 failure。A 正文已大体分开，建议在依赖图表下加一行免责声明。  
**处理结果。** 待 A 回应。

## 意见 3（复核 Q1.5）

A 在 `definitions.md` 用 insertion-sequence 模型处理“第 n 次插入”与 `|S|`：**接受，关闭该项 Q4/Q1.5 分歧**。
