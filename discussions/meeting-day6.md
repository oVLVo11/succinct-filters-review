# Day 6 会议记录

日期：2026-07-28  
状态：A/B/C 负责的正文已整合并输出最终 PDF；过期 A/C 桥接已清除。Q1/Q3 作为最终公开技术限制保留。经小组决定，Day 7 口头交流与签字/审阅不再形成仓库文件。

---

## B 五分钟全文主线（可脱稿）

问题：unknown-size 下 filter 要空间跟 `n`、无漏报、FP≤ε、whp 最坏 O(1)。  
难处：filter 丢原键，不能随意重建。  
路线：哈希前缀 → prefix matching → `T`/`D` 两代 + 每插常数轮迁移。  
结果：主项含 `log log n`；相对 PSW 钉领先常数并去均摊。  
诚实：下标归纳与字面 10 未关闭；ε≠δ。

---

## 六类证明抽问（B 自答备忘）

1. 无漏报：写入+迁移不丢+四结构；条件 ¬failed；归纳开放。  
2. FP：式 (2) 并合（A）。  
3. 扩容不慢：每插 10 轮维护（原文）；非单次线性 rebuild。  
4. 查询常数：只四结构。  
5. 空间接近最优：主项对齐 PSW；条件见 A；结构层数常数。  
6. failure≠FP：δ vs ε。

---

## PDF v1 生成记录（B 负责，历史记录）

建议命令（需本机安装 Pandoc 与中文字体）：

```text
pandoc drafts/review-integrated.md -o drafts/review-integrated-v1.pdf --pdf-engine=xelatex -V CJKmainfont="SimSun"
```

若失败：保留 Markdown 为唯一可追溯源，在 `issues-day6.md` D6-12 记原因；**禁止**手工改不可复现 PDF。  
**实际执行结果（2026-07-28，B）**：

首次尝试：系统 PATH 中无 `pandoc`/`xelatex`（winget 直连 GitHub 下载亦卡住）。  
随后：用镜像解压得到 `pandoc 3.10`（`%LOCALAPPDATA%\Pandoc\pandoc-3.10\pandoc.exe`）；本机仍无 XeLaTeX，故改用 **Pandoc→HTML→Edge headless print-to-PDF**：

```powershell
$pandoc = "$env:LOCALAPPDATA\Pandoc\pandoc-3.10\pandoc.exe"
$root   = "c:\This_is_new\tcs\workspace\succinct-filters-review"
& $pandoc "$root\drafts\review-integrated.md" -o "$root\drafts\review-integrated-v1.html" --standalone --metadata title="Succinct Filters Review (v1)" -V lang=zh-CN
& "${env:ProgramFiles(x86)}\Microsoft\Edge\Application\msedge.exe" --headless --disable-gpu --no-pdf-header-footer --print-to-pdf="$root\drafts\review-integrated-v1.pdf" (([Uri]"$root\drafts\review-integrated-v1.html").AbsoluteUri)
```

结果：`drafts/review-integrated-v1.pdf` 已生成（约 1.1 MB）。中间产物：`drafts/review-integrated-v1.html`。  
说明：此为 **v1 可复现路径**（非 xelatex）；公式/表格视觉由 A/C 抽查；若日后装好 TeX，可改回 `xelatex` 命令重跑。

可选原计划（需 XeLaTeX + 中文字体）：

```text
pandoc drafts/review-integrated.md -o drafts/review-integrated-v1.pdf --pdf-engine=xelatex -V CJKmainfont="SimSun"
```

### v1.0 当前版本生成与复核（2026-07-30）

完整参考文献和 A/B/C 三章合入后，已用仓库内脚本重新生成 HTML 与 PDF：

```text
node work/render-review.mjs
python work/render_review_pdf.py
```

当前产物为 `drafts/review-integrated-v1.html` 与 `drafts/review-integrated-v1.pdf`。PDF 共 8 页，已逐页渲染检查：正文、表格和参考文献均未越界，无标题重复、文字重叠、黑块或空白页，页脚包含 1–8 页码。数学表达采用统一的可读文本式排版；若以后配置 XeLaTeX，可进一步升级为专业公式排版，但这不再构成当前版本的内容阻塞。

Day 7 最终渲染已另行输出为 `output/pdf/succinct-filters-review-final.pdf`：增加正式封面，正文页码为 1–8，移除封面过程状态与过程附录，正文引用统一显示为编号，并完成第二轮逐页视觉复核。该文件作为最终提交候选版。

---

## Issue 决议

| ID | 最终关闭 / 降级结果 |
|---|---|
| D6-08 字面 10 | 已按原文归属降级；作为最终 Q3 限制保留，不再等待成员补写 |
| D6-09 下标 | 已按原文归属降级；作为最终 Q1 限制保留，不再等待成员补写 |
| D6-11 A 章 | A 章已入库并替换桥接；文本阻塞解除 |
| D6-12 PDF | 已重生成并完成 8 页逐页复核；当前验收通过 |

---

## B 当日产物

- [x] `drafts/review-integrated.md`（§6–9 技术内容已整合；A/C 桥接已由后续成稿替换）
- [x] `discussions/issues-day6.md`、`review-day6.md`、本会议 B 部分
- [x] 图示与正文同步说明（architecture / growth / query-insert / proof-dependency）
- [x] AI 日志

---

## A 的 Day 6 整合与演练准备

### 已完成的文本整合

- [x] 统一摘要、引言、问题定义、Theorem 1/10 和 PSW 下界。
- [x] 定义 `n,u,ε,δ,c,C,w,N,S`，并分开 FP、failure 和无 FN 口径。
- [x] 补足式 (2) 误报求和、Lemma 11 空间代入、式 (3)–(5) 与跨层 failure union bound。
- [x] 将无条件“最优”降级为带 `ε=o(1)` 和模型范围的领先项对齐。
- [x] 对 C 的相关研究比较完成模型和时间口径抽查。

### A 五分钟主线（历史准备提纲）

1. unknown size 是没有紧最终 `N`，而不是不知当前 `n`。
2. Filter 扩容的核心障碍是无法从紧凑状态枚举原 key。
3. LYY 式 (2) 的 `log i` 解释上界中 `log log n` 的来源；PSW 压缩证明才排除其他方法逃避该成本的可能。
4. Theorem 10 保留 `n=ω(log u)`、`n<u`、`O(log log log u)` 和 `u^c`；Theorem 1 在 `n>u^{0.001}` 下吸收低阶项。
5. `ε` 是 no-failure 查询误报，`δ=u^{-C}` 是序列级结构 failure；不存在一个模糊的“总错误率”。
6. 技术章的四结构使查询只覆盖旧/新相邻两代，每插常数轮将迁移去均摊；Q1/Q3 仍公开保留。

### Day 7 最终决议

原计划中的五分钟脱稿复述、最终签字/PR 审阅以及口头纠错记录均不再形成仓库文件。本记录不把这些活动写成已经发生，也不再将其列为项目文件待办。

---

## C 五分钟相关研究与评价主线

1. 先固定比较坐标：空间按什么 `n`、是否删除、时间是 expected/amortized/worst-case/whp、有无 failure。
2. SBF/DBF 通过追加组件解决增长，但查询与误报语义仍依赖组件序列；不能与 LYY 单轴排名。
3. Exact dictionary 的基准是 `log binom(u,n)`，filter 是 `n log(1/ε)`；succinct dictionary 与去均摊 cuckoo 只是技术背景。
4. PSW 是直接前作：下界证明 `log log n` 成本普遍存在；LYY 收紧领先项并把插入推进到 no-failure worst-case `O(1)`。
5. 后作分三类：Aleph 的删除/工程无限增长、KW 的删除型下界、Resizable 的 current-`n` 动态推论。没有“全面取代”。
6. 本文优势是组合保证；局限是无删除、固定宇宙、`u^c`、实现复杂和概率条件。

### C 的口头抽问提纲（历史准备材料）

| 问题 | 回答要点 | 状态 |
|---|---|---|
| SBF 为什么不是同一保证？ | 追加多个组件；查询扫组件；空间/时间口径不同 | 原准备题，不再留口头记录 |
| `log log n` 为什么不是实现浪费？ | 式 (2) 解释上界；PSW 编码下界证明普遍不可避免 | 原准备题，不再留口头记录 |
| Aleph 是否全面优于 LYY？ | 删除/工程实现维度更强；空间、清理时间与概率口径不同 | 原准备题，不再留口头记录 |
| dynamic 三种含义？ | insertion-only unknown-size；含删除容量型；current-`n` resizable | 原准备题，不再留口头记录 |
| AI 使用边界？ | AI 协助检索、整理和一致性核查；成员 C 必须逐条复核、重述并决定采用 | 原准备题，不再留口头记录 |

---

## C 对旧版 v1 PDF 的视觉核查（历史记录）

核查日期：2026-07-28。

对象：`drafts/review-integrated-v1.pdf`（8 页，B 生成；对应整合稿 v0.1）。

方法：逐页渲染为临时 PNG，检查字体、断行、表格、页边距、重叠和内容版本；临时文件不进入仓库。

### 通过项

- 8 页均可打开，中文正文、粗体标题和英文术语总体清晰；
- 未见正文或表格越过页面边界；
- 未见文字重叠、黑块、整页缺字或图片低清问题；
- 第 4、6、8 页的表格均在页宽内，行列仍可辨认。

### 修订结果（2026-07-30）

1. **内容版本：已修订。** 当前 PDF 来自 `review-integrated.md` v1.0，A/B/C 正文和 §15 完整参考文献均已纳入。
2. **标题重复：已修订。** 当前首页只保留一个主标题。
3. **页码：已修订。** 当前 8 页均有连续页码。
4. **数学符号：已修订至可读文本式。** 下标、上标和常用符号已统一；专业公式排版属于可选的 XeLaTeX 后续优化，不再列为内容待办。
5. **参考文献：已修订。** §15 已列出正文使用的 15 项来源，并与引用审计表对应。
