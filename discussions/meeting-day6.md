# Day 6 会议记录

日期：2026-07-28  
状态：B 已完成技术整合；C 已完成相关研究/评价第一轮整合与引用审计；A 章桥接待替换；PDF 仍为 B 生成的 v1，尚未按 v0.2 源文重生成。

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

## PDF v1 生成记录（B 负责）

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

---

## Issue 决议（会后填）

| ID | 关闭 / 降级 / 带入 Day 7 |
|---|---|
| D6-08 字面 10 | 降级措辞已写入；Issue 带入 Day 7 |
| D6-09 下标 | 带入 Day 7 |
| D6-11 A 章 | C 已替换；A 仍阻塞，Day 7 前必须替换桥接 |

---

## B 当日产物

- [x] `drafts/review-integrated.md`（§6–9 定稿级；其余桥接）
- [x] `discussions/issues-day6.md`、`review-day6.md`、本会议 B 部分
- [x] 图示与正文同步说明（architecture / growth / query-insert / proof-dependency）
- [x] AI 日志

---

## C 五分钟相关研究与评价主线（待本人演练）

1. 先固定比较坐标：空间按什么 `n`、是否删除、时间是 expected/amortized/worst-case/whp、有无 failure。
2. SBF/DBF 通过追加组件解决增长，但查询与误报语义仍依赖组件序列；不能与 LYY 单轴排名。
3. Exact dictionary 的基准是 `log binom(u,n)`，filter 是 `n log(1/ε)`；succinct dictionary 与去均摊 cuckoo 只是技术背景。
4. PSW 是直接前作：下界证明 `log log n` 成本普遍存在；LYY 收紧领先项并把插入推进到 no-failure worst-case `O(1)`。
5. 后作分三类：Aleph 的删除/工程无限增长、KW 的删除型下界、Resizable 的 current-`n` 动态推论。没有“全面取代”。
6. 本文优势是组合保证；局限是无删除、固定宇宙、`u^c`、实现复杂和概率条件。

### C 的口头抽问入口

| 问题 | 回答要点 | 状态 |
|---|---|---|
| SBF 为什么不是同一保证？ | 追加多个组件；查询扫组件；空间/时间口径不同 | 待成员 C 用自己的话演练 |
| `log log n` 为什么不是实现浪费？ | 式 (2) 解释上界；PSW 编码下界证明普遍不可避免 | 待演练 |
| Aleph 是否全面优于 LYY？ | 删除/工程实现维度更强；空间、清理时间与概率口径不同 | 待演练 |
| dynamic 三种含义？ | insertion-only unknown-size；含删除容量型；current-`n` resizable | 待演练 |
| AI 使用边界？ | AI 协助检索、整理和一致性核查；成员 C 必须逐条复核、重述并决定采用 | 待本人确认 |

---

## C 对 v1 PDF 的视觉核查

核查日期：2026-07-28。

对象：`drafts/review-integrated-v1.pdf`（8 页，B 生成；对应整合稿 v0.1）。

方法：逐页渲染为临时 PNG，检查字体、断行、表格、页边距、重叠和内容版本；临时文件不进入仓库。

### 通过项

- 8 页均可打开，中文正文、粗体标题和英文术语总体清晰；
- 未见正文或表格越过页面边界；
- 未见文字重叠、黑块、整页缺字或图片低清问题；
- 第 4、6、8 页的表格均在页宽内，行列仍可辨认。

### 必须修订

1. **内容已过期**：PDF 仍显示整合稿 v0.1，§4、§10–§12、§15 仍是【待 C】桥接；当前 Markdown 已为 v0.2，不能把该 PDF 当作最新交付版。
2. **标题重复**：第一页同时出现 Pandoc metadata 标题 “Succinct Filters Review (v1)” 与 Markdown 一级标题，占用较大空间。
3. **无页码/页眉页脚**：口头核查和引用页面时不便定位。
4. **数学符号渲染不统一**：`D_{i-1}`、`T_{i-1}`、`u^{-C}` 等多处保留原始下划线/花括号；`⌈log n⌉` 等符号出现替代显示。虽然可读，但不满足最终公式排版。
5. **参考文献未成表**：第 15 节仍是占位说明，没有生成完整参考文献列表。

### 结论

v1 只能证明 B 的 HTML→PDF 路径基本可用，不能通过当前内容验收。应在 A 章替换、C 稿获本人确认、引用表完成后，由源 Markdown 统一重生成新版 PDF，再做一次全页视觉核查；不应手工编辑现有 PDF。
