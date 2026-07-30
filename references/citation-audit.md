# 引用审计（成员 C，Day 6）

- **主责**：陈戚（C）
- **日期**：2026-07-28
- **适用稿件**：`drafts/section-C-related-work-and-evaluation.md` v0.1、`drafts/review-integrated.md`
- **页码口径**：优先记录论文印刷节号；“PDF p.”指下载文件页序，最终排版前应统一
- **证据等级**：E3=核验原文关键定义/定理/引用语境；E2=摘要/元数据加后作转述；E1=元数据或摘要，不承担确定性技术比较

## 1. 正文引用与证据位置

| 正文主张 / 用法 | BibTeX key | 正式来源 / DOI | 原文证据位置 | 等级 | 状态与限制 |
|---|---|---|---|---|---|
| 主论文结果、Theorem 10、Claim 13、式 (2) | `liu2020succinct` | DOI `10.4230/LIPIcs.ICALP.2020.79` | §1–§3；Thm 10（印刷 79:9）；Claim 13 | E3 | 已核；所有正确性/时间措辞带 no-failure 条件 |
| Bloom filter 历史起点 | `bloom1970space` | DOI `10.1145/362686.362692` | 元数据、摘要 | E1 | 只写历史功能，不写未核常数/最优参数 |
| Approximate membership 理论起点 | `carter1978membership` | DOI `10.1145/800133.804332` | 元数据、摘要；LYY [8] | E1 | 只作问题背景 |
| SBF 追加组件、逐组件查询、几何误报预算 | `almeida2007scalable` | DOI `10.1016/j.ipl.2006.10.007` | §4–§5，PDF pp.4–8 | E3 | 已核；原始结构未给用户删除 |
| DBF 多组件、查询/FPR 随组件数 | `guo2006dynamic` | DOI `10.1109/INFOCOM.2006.325` | §III、式 (3)、Algorithms 1–2，PDF pp.3–6；结论 p.12 | E3 | 已核；时间写“平均”，不写 worst-case |
| Raman–Rao succinct dictionary 背景 | `raman2003succinct` | DOI `10.1007/3-540-45061-0_30` | 正式摘要；LYY §1.2/§2.2 转述 | E2 | 只作技术谱系，不作精细同模型排名 |
| 动态 succinct hashing 背景 | `demaine2006dictionariis` | DOI `10.1007/11682462_34` | 正式摘要；LYY §1.2 转述 | E2 | 不扩张到 current-`n` leading constant |
| 去均摊/Backyard cuckoo 背景 | `arbitman2010backyard` | arXiv `0912.5424` | 摘要；LYY §1.2 | E2 | 只作去均摊与 succinct 背景 |
| 已知容量 succinct filter 对照 | `pagh2005optimal` | DOI `10.1145/1070432.1070548` | 正式摘要；LYY §1.2 转述 | E2 | 不写成 unknown-size 结果 |
| PSW unknown-size 直接前作与下界 | `pagh2013unknown` | DOI `10.1109/FOCS.2013.17` | §1.3；Thm 3.1、Lemmas 3.2–3.4，仓库 PDF pp.7–10 | E3 | key 已纠正；精细系数来自 Thm 3.1 参数化形式 |
| Quotient filter 删除/resize/负载依赖 | `bender2012quotient` | DOI `10.14778/2350229.2350275` | §3–§4，PDF pp.1–6 | E3 | 原文未被 LYY 引用；标为外补工程对照 |
| Cuckoo filter 两桶、删除、插入失败约束 | `fan2014cuckoo` | DOI `10.1145/2674005.2674994` | §1、§4–§5、式 (3)，PDF pp.1、6–7 | E3 | 不由标题“Practically Better”推出全面更优 |
| InfiniFilter 工程前代 | `dayan2023infinifilter` | DOI `10.1145/3589285` | 摘要；Aleph §1 转述 | E2 | 不写是否直接引用 LYY或精确最坏时间 |
| Aleph 对 LYY 的直接比较、删除与时间边界 | `dayan2024aleph` | DOI `10.14778/3681954.3682027` | Abstract；§5.2（PDF p.8）；§7（p.12） | E3 | constant-time 总述与 amortized 清理分开写 |
| 删除型 dynamic filter 线性冗余下界 | `kuszmaul2024dynamicfilters` | DOI `10.1145/3618260.3649649` | 定义/主结论 pp.1、3；Thm 3.1 p.4；refs p.12 | E3 | 容量+删除模型，不反推 LYY 错误 |
| 当前 `n` 的 resizable filter 推论 | `kuszmaul2026resizable` | arXiv `2606.15944` | Intro pp.2–4；Thm 1.1 p.2/20；Cor. 3.14 pp.20–21 | E3 | 2026-07-28 仍为 arXiv/CoRR 预印本；不称正式发表 |

## 2. 未进入确定性比较的研究条目

| BibTeX key | 当前证据 | 正文处理 |
|---|---|---|
| `li2023cellprobe` | E1；仅元数据/摘要，另有后作转述 | 保留在研究矩阵，不写成 LYY filter 的直接改进 |
| `li2024subconstant` | E1；仅元数据/摘要 | 保留在研究矩阵，不进入确定性技术结论 |
| `bender2018adaptivity` | E1/E2；摘要与 LYY 背景 | 只说明 adaptive query 是另一比较轴 |
| `bercea2019fullydynamic` | E1/E2；摘要与 LYY 转述 | 不据此给 current-`n` 的精细结论 |

这些条目暂留 `bibliography.bib` 是为了保存资料筛选过程；最终参考文献表若要求“只列正文已引”，应在最终稿生成阶段单独过滤，而不是删除研究记录。

## 3. 强断言逐句审计

| 高风险词 | 当前处理 | 依据 |
|---|---|---|
| “首次” | 只说 PSW 是本项目所述 unknown-size filter 的直接前作；不说 LYY 首次提出问题 | PSW 2013；LYY §1 |
| “最优” | 改为“在 `ε=o(1)` 等条件下与 PSW 参数化下界的 `log log n` 领先项对齐” | PSW Thm 3.1；LYY Thm 1/10 |
| “优于 Bloom” | 禁止单轴结论，改为空间/时间/删除/工程实现分维度 | SBF/DBF/QF/CF 原文关键章节 |
| “常数时间” | 逐篇保留 worst-case、amortized、whp、no-failure 等条件 | LYY Thm 10；Aleph §5.2；Resizable Cor. 3.14 |
| “支持删除” | LYY 明确写不支持；Aleph/fully dynamic/resizable 另列 | LYY Thm 10；Aleph §7；后作定义 |
| “后续取代本文” | 删除；改为“扩大模型或改变保证，不能无条件支配” | 三篇 E3 后作逐维比较 |
| “最新/已发表” | Resizable Retrieval 只写“2026 预印本” | arXiv 2606.15944；DBLP CoRR 记录 |

## 4. 图、表、公式与外部事实来源

| 对象 | 来源 / 性质 | 状态 |
|---|---|---|
| 前缀长度式 (2) | LYY §3.1 | 已标论文命题 |
| 四结构、迁移箭头 | LYY Claim 13；小组重画 | 图注须写“小组据 Claim 13 重画” |
| 8 元素示例 | 小组教学示例 | 已明确不承担一般证明 |
| PSW 下界依赖链 | PSW Thm 3.1、Lemmas 3.2–3.4；小组归纳 | 已写入 A 章 §6 与整合稿 §5.2 |
| C 章多维比较表 | 成员 C 据上述 E3 来源整理 | 已标“可靠评价”，不作新定理 |
| Resizable Cor. 3.14 空间式 | arXiv:2606.15944v1 pp.20–21 | 已核；版本变化需复查 |

## 5. 本轮结论与遗留

- `pagh2013approximate` 是旧占位 key，仓库实际 key 为 `pagh2013unknown`，本审计已统一。
- C 章所有确定性跨论文比较均有 E3 原文定位；E1/E2 仅作背景或明确保留。
- A 章已入库，PSW 引用已对应到章节 §6 与整合稿 §5.2；最终生成参考文献表时仍需运行 BibTeX 完整性检查。
- 最终提交前重新打开 arXiv:2606.15944，检查版本号、公式编号和正式发表状态。

## 6. A 的八项正文—文献对应抽查

| 抽查项 | 正文位置 | BibTeX key | 原文定位 | 结论 |
|---|---|---|---|---|
| Theorem 10 正式参数与空间 | A §4.1；整合稿 §5.1 | `liu2020succinct` | Thm 10，印刷页 79:9 | 对应正确 |
| Theorem 1 的 `n>u^{0.001}` | A §4.2；整合稿 §5.1 | `liu2020succinct` | Thm 1，印刷页 79:3 | 与 Thm 10 条件已分层 |
| 式 (2) 与 FP 求和 | A §5；整合稿 §6.2/§8.2 | `liu2020succinct` | §3.1 式 (2)，79:10 | 对应正确 |
| Lemma 11 空间代入 | A §7；整合稿 §9.2 | `liu2020succinct` | Lemma 11，79:10 | 对应正确 |
| Claim 13 四结构与 10 轮 | 整合稿 §6.3/§7.1 | `liu2020succinct` | Claim 13，79:12–13 | 保留 Q1/Q3 |
| PSW 参数化下界 | A §6.1；整合稿 §5.2 | `pagh2013unknown` | Thm 3.1，PDF p.7 | 对应正确 |
| PSW 固定随机性 | A §6.2 步骤 1 | `pagh2013unknown` | Lemma 3.2，PDF p.8 | 对应正确 |
| PSW 几何块、旧误报与编码 | A §6.2 步骤 2–6 | `pagh2013unknown` | Lemmas 3.3–3.4、式 (3.1)–(3.2)，PDF pp.8–10 | 对应正确 |
