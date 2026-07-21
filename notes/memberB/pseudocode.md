# Day 4：抽象伪代码级实现说明

- **负责人**：张书铖（成员 B）
- **日期**：2026-07-22（按 Day 4 计划）
- **性质**：**抽象伪代码**（对照 Claim 13 / §3.1 接口，非可运行工程代码；不虚构内存布局）
- **对照**：`core-components.md`；底层 `D(m,ℓ)` 视为黑盒（§5 实现另文）

---

## 0. 全局状态定义

```text
状态 FilterState:
  u, ε, δ          // 参数；δ = u^{-C}
  h                // 全局 (c1 log u)-wise 哈希（Thm 7）；求值 O(1)
  n                // 已接受插入次数（insertion-sequence 模型）
  failed           // 布尔；一旦 true，后续正确性/时间保证按定理条件失效

  // 各层结构（仅少数层同时非空）
  T[0..⌈log u⌉]    // 真值表；T[j] 表示长度 j 的短串
  D[0..⌈log u⌉]    // D[j] = D(m=2^j, ℓ=ℓ_j) 黑盒实例；未创建则为 nil

  // 进度（去均摊）
  destroyProg[j]   // T[j]/D[j] 的销毁进度
  initProg[j]      // T[j]/D[j] 的初始化进度
  // decrement 游标内含于各结构（黑盒/真值表内部）

辅助:
  iStar(n)  := ⌈log n⌉          // 操作控制（Claim 13 算法句）
  ell(i)    := i + log(1/ε) + log i + log log log u + 2   // 式 (2)
  Pref(z, L) := z 的前 L 比特
```

**约定**

- `Lookup`/`Insert` 使用 `i = iStar(n)`；不把证明段半开区间句直接当作已证存储归纳（见 issue-stage-index）。
- 底层原语 `D.insert/query/decrement/initialize/destroy` 与 `T.*` 均假定单次 **worst-case O(1)**（Claim 13 假设）。
- `Initialize(D)`/`Destroy(D)` 需连续调用 **O(m)** 次才完成（黑盒）；本伪代码每次只推进常数步。

---

## 1. Initialize

```text
procedure Initialize(u, ε, C):
  n ← 0
  failed ← false
  h ← ConstructHash(u)           // Thm 7；失败则以小概率整体失败（并入 δ 参数选择）
  清空所有 T[*], D[*]
  // Claim 13 初始：T0,T1 与 D0=D(1,ℓ0), D1=D(2,ℓ1)
  完整初始化 T[0], T[1]          // 教学写法；实现上亦可摊到首次插入
  完整初始化 D[0], D[1]
  return
```

| 项 | 说明 |
|---|---|
| 前置 | 参数合法；字长等模型假设成立 |
| 修改 | 全部初始状态 |
| 不变式 | `n=0`；可查询结构为初始集；`failed=false` |
| 工作量 | 一次性初始化代价不计入单次操作；之后靠去均摊 |

---

## 2. Lookup(x)

```text
procedure Lookup(x):
  if failed: return ⊥ 或按约定拒绝保证   // 定理条件：无 failure
  if n = 0: return NO
  i ← iStar(n)
  z ← h(x)
  // 查询活跃四结构（≠ 所有已 initialize 的层）
  if D[i-1] ≠ nil and D.query(D[i-1], z): return YES
  if D[i]   ≠ nil and D.query(D[i],   z): return YES
  if T[i-1] ≠ nil and T.query(T[i-1], Pref(z, i-1)): return YES
  if T[i]   ≠ nil and T.query(T[i],   Pref(z, i)):   return YES
  return NO
```

| 项 | 说明 |
|---|---|
| 前置 | `¬failed`；底层未损坏 |
| 修改 | 无 |
| 不变式 | 若存在已存前缀 `s ⊑ z` 且落在查询活跃层，则返回 YES（无 FN 论证见 `proof-notes.md`） |
| 工作量 | ≤ 4 次底层 `query` = **O(1)** |

---

## 3. Insert(x)

```text
procedure Insert(x):
  if failed: return FAIL
  n ← n + 1
  i ← iStar(n)
  s ← Pref(h(x), ell(i))
  // 若已有更短前缀覆盖 s，则跳过写入（core set）
  if not AlreadyHasPrefix(s):
    ensure D[i] 可用（若仍在 initialize，先继续推进初始化直至可 insert；
                     抽象上 Claim 13 假定在需要时层已可用——细节 Q3）
    ok ← D.insert(D[i], s)
    if not ok: failed ← true; return FAIL

  repeat 10 times:                 // 原文字面；配平见 Q3 / issue-constant-10
    MigrateOneStep(i)

  return OK
```

| 项 | 说明 |
|---|---|
| 前置 | `¬failed` |
| 修改 | `n`；可能写入 `D[i]`；推进迁移/销毁/初始化进度；可能置 `failed` |
| 不变式 | 新前缀进入库或被更短前缀覆盖；维护推进旧→新 |
| 工作量 | 1 次 `D.insert` + 10 × `MigrateOneStep` = **O(1)**（在底层原语 O(1) 且字面/渐近配平成立时） |

`AlreadyHasPrefix`：可用一次 `Lookup` 语义在串上判定，或维护时保证；属抽象。

---

## 4. StartNewStage()

```text
procedure StartNewStage(i):
  // 抽象：当控制参数变为 i 时，确保 D[i],T[i] 作为“当前写入层”
  // 原文没有单独 API；由 Insert 内 iStar(n) 变化与 initialize(T_{i+1},D_{i+1}) 体现
  ensure initProg 针对 T[i], D[i] 最终完成
  return
```

| 项 | 说明 |
|---|---|
| 前置 | — |
| 修改 | 初始化进度 |
| 不变式 | 写入层存在 |
| 工作量 | 摊到多次 `MigrateOneStep`；非单次 Insert 独占 |

**说明**：此过程为**小组为可读性拆出的抽象**，原文嵌在 Insert 维护步骤 4。

---

## 5. MigrateOneStep(i)

对应 Claim 13 维护循环的**一轮**：

```text
procedure MigrateOneStep(i):
  // (1) 短串：T_{i-1} → T_i 的两个扩展
  if T[i-1] ≠ nil and not Empty(T[i-1]):
    y ← T.decrement(T[i-1])
    if y ≠ ⊥:
      T.insert(T[i], y ∘ 0)
      T.insert(T[i], y ∘ 1)

  // (2) 长/短：D_{i-1} → D_i 或 T_i
  if D[i-1] ≠ nil and not Empty(D[i-1]):
    y ← D.decrement(D[i-1])
    if y ≠ ⊥:
      if |y| > i:
        D.insert(D[i], y)
      else:
        T.insert(T[i], y)

  // (3) 销毁旧结构
  if T[i-1] ≠ nil and Empty(T[i-1]) and not Destroyed(T[i-1]):
    T.destroyOneStep(T[i-1])
  if D[i-1] ≠ nil and Empty(D[i-1]) and not Destroyed(D[i-1]):
    D.destroyOneStep(D[i-1])

  // (4) 初始化下一层（已初始化 ≠ 查询活跃）
  if Destroyed(T[i-1]) or T[i-1] = nil:
    ensure T[i+1] 存在；T.initializeOneStep(T[i+1])
  if Destroyed(D[i-1]) or D[i-1] = nil:
    ensure D[i+1] = D(2^{i+1}, ell(i+1))
    D.initializeOneStep(D[i+1])
  return
```

| 项 | 说明 |
|---|---|
| 前置 | `i = iStar(n)`；相关层指针合法 |
| 修改 | 旧层串迁出；新层写入；destroy/init 进度 |
| 不变式 | **迁移不丢串**：取出的 `y` 立即写入新位置；查询活跃层仍覆盖未迁完数据（意图；存储归纳见缺口） |
| 工作量 | 常数次底层调用 = **O(1)** |

---

## 6. FinalizeStage()

```text
procedure FinalizeStage(i):
  // 抽象目标（Claim 13 证明段意图）：
  // 当 n 到达相应幂次边界时，旧层 D_{i-1},T_{i-1} 已销毁，
  // 数据在 D_i,T_i，且 D_{i+1},T_{i+1} 已初始化。
  // 实现上由足够多次 MigrateOneStep 完成，无单独原文 API。
  assert 迁移与 init/destroy 进度满足边界条件  // 证明义务，非运行时 assert
  return
```

| 项 | 说明 |
|---|---|
| 前置 | 阶段内已执行足够维护步数 |
| 修改 | 无额外（进度应已完成） |
| 不变式 | 边界快照 |
| 工作量 | 0（逻辑检查） |

**缺口**：与 `i★`/`epoch` 对齐的形式断言仍挂 issue-stage-index。

---

## 7. HandleFailureOrRebuild()

```text
procedure HandleFailureOrRebuild():
  // 正式 Thm 10：插入后可报告 failure；概率对整段序列 ≤ δ。
  // 公开保证均以 “conditioned on no failure” 为条件。
  // 引言脚注：若发生罕见坏事件，可线性时间重建使期望仍为常数——
  // 这是讲解性备注，不是 Claim 13 给出的独立接口。
  if not failed: return
  // 可选（非形式化主定理必需）：
  //   丢弃结构；用当前逻辑集合（若仍可恢复）或外部日志重建
  // Filter 通常不能从结构本身恢复原 key → 重建依赖应用层保留的 key /
  //   或仅宣布失败。本文主定理不依赖自动 rebuild API。
  return
```

| 项 | 说明 |
|---|---|
| 前置 | `failed=true` |
| 修改 | 实现相关；主定理可不实现 |
| 不变式 | 无（已离开定理保证区） |
| 工作量 | 重建若做则为 `Θ(n)`；故主路径证明不依赖它 |

**结论**：伪代码**保留本过程仅作说明**；Review 正文应写“保证以无 failure 为条件”，不把 rebuild 写成已实现接口。

---

## 8. 状态 ↔ 原文映射

| 状态/过程 | 原文 |
|---|---|
| `h`, `ell(i)` | §3.1，式 (2)，Thm 7 |
| `T[j]`, `D[j]` | Claim 13 |
| `Insert` + 10×维护 | Claim 13 证明 |
| `Lookup` 四 query | Claim 13 末 |
| `D.*` 黑盒 | Claim 13 前接口；§5 实现 |
| `failed` / δ | Thm 10 第 3–4 条 |
| rebuild 脚注 | 引言关于期望时间的脚注 |

---

## 9. 未读读者检查清单（供 C 审阅）

1. 每个名字是否在 §0 定义？
2. `MigrateOneStep` 四步是否都能指回 Claim 13？
3. 是否误以为 `HandleFailureOrRebuild` 是主定理接口？
4. 是否用 8 元素例子代替本伪代码的一般性？
