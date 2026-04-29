# 本地 Suggest -> Auto Edit -> 手动验证 -> 回滚演练

状态：待执行。生成仓库后运行：

```powershell
python tools/run_rehearsal.py
```

目标：

- Suggest：用 Codex CLI 只读模式做项目结构讲解，不改文件。
- Auto Edit：对本仓库的协议模型做一个低风险内部重构。
- 手动验证：运行 `python -m unittest discover -s tests`。
- 回滚：恢复被改文件，再次运行测试，证明可以撤回。
