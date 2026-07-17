# 通读笔记（Day 1）

- **论文**：Mingmou Liu, Yitong Yin, Huacheng Yu. *Succinct Filters for Sets of Unknown Sizes*. ICALP 2020 / arXiv:2004.12465
- **阅读范围**：摘要、引言、§1.3–1.4 技术概览、§3 未知规模数据结构、§4–5 前缀匹配与已知容量构造的骨架；对引理列表做初步浏览
- **日期**：2026-07-17
- **负责人**：张书铖

---

## 1. 论文在解决什么

标准 filter / dictionary 在初始化时要给定容量上界 `N`，之后空间长期按 `N` 占用。实际集合大小 `n` 可能远小于 `N`，或根本没有可靠上界。

对 **dictionary（精确成员）**，可以用“容量翻倍 + 重建迁移”把空间压到接近当前 `n`。对 filter（允许误报 `ε`）则更难：filter 为了省空间并不保存原始元素，扩容后无法简单重算更大值域上的哈希；若保留旧结构不迁移，又会拖累查询与空间。

Pagh–Segev–Wieder (FOCS'13) 给出未知规模 filter 的信息论下界，并给出接近下界、但插入为期望均摊常数时间、且 `log log n` 项前导常数未钉死的构造。

本文目标（非正式）：

1. **Filter**（Thm 1 / 正式 Thm 10）：空间 `(1+o(1)) n (log(1/ε) + log log n)`（在合适参数下），插入与查询均为最坏情况 `O(1)`（高概率）。
2. **Dictionary**（Thm 2 / 正式 Thm 12）：空间 `(1+o(1)) n log(u/n)`（另有 `v` 与低阶项），同样最坏情况常数时间（高概率）。

---

## 2. 论文结构

| 部分 | 内容 |
|---|---|
| §1 Intro / Results / Related | 问题动机、主定理、相关工作 |
| §1.3 Previous Construction | PSW 的全局哈希 + 前缀 + 短串复制进单一字典 |
| §1.4 Our Techniques | 真值表处理短串；新 membership；分阶段 in-place 迁移 |
| §2 Preliminaries | 字符串记号、extendable array、k-wise hash、adaptive prefixes |
| §3 Filters & Dictionaries | 化归到 prefix matching；前缀长度 `ℓ_i`；空间推导 |
| §4 Prefix Matching Upper Bound | Claim 13 + 真值表 + `D_i` 多结构并存与迁移循环 |
| §5 Known-capacity Prefix Matching | Main table / subtable / data block / 去均摊重组 |
| §6 Unconditional Dictionary | Feistel 置换等 |
| §7 Allocate-Free Model | 另一内存模型下的空间 |

---

## 3. 核查问题

1. **Scalable / Dynamic Bloom Filter（如 Almeida et al. 2007；Guo et al. Dynamic Bloom）**  
   它们是否同样要求：**无预知最终 `n`**、**无 false negative**、**空间相对当前 `n` 达到信息论意义上的 succinct（含 `log log n` 项）**、以及 **最坏情况 `O(1)`（高概率）**？若只是工程上可扩容、空间为 `O(n log(1/ε))` 再乘常数，则不宜写成“已解决本文问题”。

2. **Quotient Filter / Cuckoo Filter**  
   多数实现/分析是否仍依赖容量/负载因子上界？删除支持是否改变与本文（论文主结果似乎不强调删除）的可比性？写入比较表时请标明：**known capacity vs unknown size**、**amortized vs worst-case whp**。

---
