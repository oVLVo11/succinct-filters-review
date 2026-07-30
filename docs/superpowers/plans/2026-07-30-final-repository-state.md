# Final Repository State Implementation Plan

> **执行状态（2026-07-30）**：全部任务已完成并通过一致性验证；下列未勾选框保留实施前计划形态，不表示当前仍有待办。

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 将全部项目文件统一更新为最终状态，不再把 Day 7 口头交流、签字或最终审阅列为待办，同时保留真实历史轨迹。

**Architecture:** 先全仓库扫描当前待办表述，再按“历史计划”“当前状态”“最终交付”三层处理。历史文件追加最终决议，当前入口直接封口，最终 PDF 仅在源稿出现过程状态残留时重新生成和逐页验证。

**Tech Stack:** Markdown、PowerShell 文本检索、ReportLab PDF 渲染、Poppler 页面渲染、pypdf 内容检查。

## Global Constraints

- 不创建虚构的 Day 7 口头模拟、审阅、签字、错误回答或 PR 记录。
- Q1/Q3 保留为技术限制，不作为待成员完成的工作。
- 不创建 Day 7 口头交流或审阅文件。
- 不执行 Git commit 或 push。
- 最终 PDF 路径保持为 `output/pdf/succinct-filters-review-final.pdf`。

---

### Task 1: 全仓库最终状态扫描

**Files:**
- Inspect: `README.md`
- Inspect: `Plan.md`
- Inspect: `work/*.md`
- Inspect: `discussions/**/*.md`
- Inspect: `ai-usage/*.md`

**Interfaces:**
- Consumes: 已确认的最终状态设计。
- Produces: 需要区分为历史记录、当前待办和真实技术限制的命中清单。

- [ ] **Step 1: 搜索口头、签字和审阅待办**

```powershell
Get-ChildItem -Recurse -File -Filter *.md |
  Select-String -Pattern '待.*口头|待.*演练|待.*签字|待.*审阅|尚未发生的人工活动|Day 7|下一阶段'
```

- [ ] **Step 2: 分类命中项**

将结果分为：历史计划需追加决议、当前状态需改为完成、Q1/Q3 保留、无关正文无需修改。

- [ ] **Step 3: 保存实施依据**

以设计文件和本计划作为修改依据，不另建口头或审阅记录。

---

### Task 2: 封口历史计划与会议记录

**Files:**
- Modify: `Plan.md`
- Modify: `work/day6.md`
- Modify: `discussions/meeting-day5.md`
- Modify: `discussions/meeting-day6.md`
- Modify other historical files returned by Task 1 only when they can be误读为当前待办。

**Interfaces:**
- Consumes: Task 1 分类结果。
- Produces: 保留原始计划且带最终决议的过程文件。

- [ ] **Step 1: 在 Day 7 总计划处增加最终执行说明**

明确文本与 PDF 已完成，小组决定口头交流和最终审阅不再形成仓库文件。

- [ ] **Step 2: 修改 Day 6 出口状态**

把“仅保留真实口头演练、签字/PR 审阅”改为“这些活动按小组最终决议不再留档”。

- [ ] **Step 3: 保留历史问题而取消当前勾选框语义**

将会议中的未勾选人工活动改为决议说明，不填写虚构答案或签字人。

---

### Task 3: 统一当前入口、问题清单和日志

**Files:**
- Modify: `README.md`
- Modify: `discussions/questions.md`
- Modify: `discussions/issues-day6.md`
- Modify: `ai-usage/member-A-log.md`
- Modify: `ai-usage/member-B-log.md`
- Modify: `ai-usage/member-C-log.md`
- Modify review/status files returned by Task 1.

**Interfaces:**
- Consumes: Task 2 的最终决议措辞。
- Produces: 无口头/签字/最终审阅当前待办的仓库入口与状态记录。

- [ ] **Step 1: 更新 README 项目状态**

写明源稿、最终 PDF 和过程材料均已定稿；Day 7 不再新增口头或审阅文件。

- [ ] **Step 2: 更新问题清单和 Issue 出口**

删除口头或签字负责人待办；保留 Q1/Q3 为正文限制。

- [ ] **Step 3: 更新三位成员日志末尾状态**

记录“小组决定不再为 Day 7 口头交流和审阅形成文件”，不得写成活动已经发生。

---

### Task 4: 最终交付与一致性验证

**Files:**
- Verify: `drafts/review-integrated.md`
- Verify/Regenerate: `output/pdf/succinct-filters-review-final.pdf`
- Modify if needed: `work/render_review_pdf.py`

**Interfaces:**
- Consumes: 最终状态统一后的 Markdown 文件。
- Produces: 可提交 PDF 和无矛盾的仓库状态。

- [ ] **Step 1: 扫描残留当前待办**

```powershell
Get-ChildItem -Recurse -File -Filter *.md |
  Select-String -Pattern '待.*口头|待.*演练|待.*签字|待.*审阅|尚未发生的人工活动'
```

预期：仅历史引文或设计说明可命中；所有项目当前状态均已封口。

- [ ] **Step 2: 检查最终 PDF 内容标记**

```python
from pypdf import PdfReader
r = PdfReader("output/pdf/succinct-filters-review-final.pdf")
t = "\n".join((p.extract_text() or "") for p in r.pages)
assert "Day 6 完整整合版" not in t
assert "尚未发生的人工活动" not in t
assert "【待" not in t
assert len(r.pages) == 9
```

- [ ] **Step 3: 运行格式检查**

```powershell
git diff --check
```

预期：无空白字符错误。

- [ ] **Step 4: 核对最终文件存在**

确认 `output/pdf/succinct-filters-review-final.pdf` 可打开、含 1 页封面和 8 页正文，并清理临时页面图。

- [ ] **Step 5: 不执行提交**

输出完整修改文件名录，由小组自行决定 Git 提交拆分和推送。

## 自检结论

- 设计中的历史保留、当前待办清零、不虚构记录、Q1/Q3 保留、PDF 验证和不提交 Git 均有对应任务。
- 计划中没有 TBD、TODO 或未定义的实现步骤。
- 本任务是文档状态统一，不需要新增软件接口或测试框架。
