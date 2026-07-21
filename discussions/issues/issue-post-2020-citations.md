# Issue：2020 年后直接引用与模型可比性

- 创建人：成员 C（AI 辅助草案，待本人确认）
- 日期：2026-07-21
- 状态：OPEN
- 关联：`references/post-2020-matrix.md`

## 问题

最终 Review 若写“后续工作改进了 LYY”，必须同时回答：

1. 后作是否直接引用 LYY，引用发生在背景、相关工作还是技术定理语境；
2. 它研究的是未知最终插入规模、支持删除的固定容量 dynamic filter，还是空间按当前 `n` 的 resizable 结构；
3. 时间是 worst-case、amortized、expected，还是 with high probability；
4. 比较的是空间主项、冗余项、删除、无限增长还是工程性能。

## 已确认

- Aleph 2024 直接引用并比较 LYY，明确谈及删除、固定宇宙上界和额外空间；但其中部分删除清理为 amortized 分析。
- Kuszmaul--Walzer 2024 以 [28] 引用 LYY 的 incremental unknown-size 最优空间式；其主结果是允许删除、容量为 `n` 的 dynamic filter 下界。
- Resizable Retrieval 2026 v1 直接引用 LYY，并给空间按当前 `n` 的 dynamic filter 推论；目前仅为 arXiv 预印本。

## 未关闭项

- InfiniFilter 正文是否直接引用 LYY；需取得正式全文后搜索并读上下文。
- Li 2023/2024 对 LYY 的直接引用关系和精确定理条件。
- 2026 预印本在最终提交前是否出现新版或正式发表记录。

## 关闭条件

- 最终采用的每篇后作都有原文页码/定理或明确标为摘要级；
- 比较句包含模型与时间口径，不使用“全面优于/取代”一类无条件措辞；
- 成员 C 能口头解释矩阵前三篇 E3 文献的差别。
