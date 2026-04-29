from __future__ import annotations

        import subprocess
        import sys
        from datetime import datetime
        from pathlib import Path


        ROOT = Path(__file__).resolve().parents[1]
        TARGET = ROOT / "src" / "protocol_model.py"
        LOG = ROOT / "workflow" / "suggest_autoedit_rehearsal.md"


        def run(args: list[str]) -> tuple[int, str]:
            proc = subprocess.run(args, cwd=ROOT, text=True, capture_output=True)
            return proc.returncode, (proc.stdout + proc.stderr).strip()


        def main() -> None:
            original = TARGET.read_text(encoding="utf-8")
            edited = original.replace(
                "MAX_SPEED_RPM = 4000\n",
                "MAX_SPEED_RPM = 4000\nMIN_SPEED_RPM = -MAX_SPEED_RPM\n",
            ).replace(
                "return max(-MAX_SPEED_RPM, min(MAX_SPEED_RPM, value))",
                "return max(MIN_SPEED_RPM, min(MAX_SPEED_RPM, value))",
            )
            if edited == original:
                raise RuntimeError("auto edit target text was not found")

            before_code, before_out = run([sys.executable, "-m", "unittest", "discover", "-s", "tests"])
            TARGET.write_text(edited, encoding="utf-8")
            edited_code, edited_out = run([sys.executable, "-m", "unittest", "discover", "-s", "tests"])
            TARGET.write_text(original, encoding="utf-8")
            rollback_code, rollback_out = run([sys.executable, "-m", "unittest", "discover", "-s", "tests"])

            status = "完成" if before_code == edited_code == rollback_code == 0 else "失败"
            LOG.write_text(
                f'''# 本地 Suggest -> Auto Edit -> 手动验证 -> 回滚演练

状态：{status}
时间：{datetime.now().isoformat(timespec='seconds')}

## 1. Suggest

项目结构讲解使用 Codex CLI 只读模式生成，见 `workflow/project_structure_suggest.md`。
如果该文件不存在，说明 CLI Suggest 步骤未成功，需要重新运行只读命令。

## 2. Auto Edit

对 `src/protocol_model.py` 做低风险内部重构：

- 新增 `MIN_SPEED_RPM = -MAX_SPEED_RPM`
- `clamp_rpm()` 从直接写 `-MAX_SPEED_RPM` 改为使用 `MIN_SPEED_RPM`

## 3. 手动验证

编辑前测试退出码：{before_code}

```text
{before_out}
```

编辑后测试退出码：{edited_code}

```text
{edited_out}
```

## 4. 回滚

已恢复 `src/protocol_model.py` 的原始内容。

回滚后测试退出码：{rollback_code}

```text
{rollback_out}
```

## 5. 信任边界

- 真实固件工程未提供前，只能在学习助手仓库里演练流程。
- 对真实 STM32 工程执行 Auto Edit 前，必须先有 Git 基线、可重复测试、明确回滚方式。
- 硬件相关改动即使测试通过，也不能替代限流上电、空载 PWM、示波器波形和故障链路验证。
''',
                encoding="utf-8",
            )
            print(status)


        if __name__ == "__main__":
            main()
