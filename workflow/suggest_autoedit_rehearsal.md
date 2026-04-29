# 本地 Suggest -> Auto Edit -> 手动验证 -> 回滚演练

状态：完成
时间：2026-04-30T01:55:13

## 1. Suggest

项目结构讲解见 `workflow/project_structure_suggest.md`。
本次 `codex exec -s read-only` 在当前桌面会话被系统权限拦截，错误为 `Access is denied`，所以先固化只读等价稿；真实 CLI Suggest 需要在可运行 `codex exec` 的终端复跑。

## 2. Auto Edit

对 `src/protocol_model.py` 做低风险内部重构：

- 新增 `MIN_SPEED_RPM = -MAX_SPEED_RPM`
- `clamp_rpm()` 从直接写 `-MAX_SPEED_RPM` 改为使用 `MIN_SPEED_RPM`

## 3. 手动验证

编辑前测试退出码：0

```text
.........
----------------------------------------------------------------------
Ran 9 tests in 0.000s

OK
```

编辑后测试退出码：0

```text
.........
----------------------------------------------------------------------
Ran 9 tests in 0.000s

OK
```

## 4. 回滚

已恢复 `src/protocol_model.py` 的原始内容。

回滚后测试退出码：0

```text
.........
----------------------------------------------------------------------
Ran 9 tests in 0.000s

OK
```

## 5. 信任边界

- 真实固件工程未提供前，只能在学习助手仓库里演练流程。
- 对真实 STM32 工程执行 Auto Edit 前，必须先有 Git 基线、可重复测试、明确回滚方式。
- 硬件相关改动即使测试通过，也不能替代限流上电、空载 PWM、示波器波形和故障链路验证。
