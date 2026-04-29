# AI 审查与测试生成接入方式

## 默认动作

1. 协议、错误码、状态机、速度命令控制有改动时，先跑 `python -m unittest discover -s tests`。
2. 如果涉及 JEOC/ADC/PWM/FOC ISR，再套用 `templates/jeoc_interrupt_review_template.md`。
3. Codex 生成测试时，必须覆盖正常帧、坏 JSON、未知命令、状态不允许、速度越界、故障态拒绝运行。
4. 测试通过只能说明协议模型没退化，不能替代真实硬件验证。

## 后续接入真实固件

- 把真实协议解析代码放入 `firmware/` 后，优先用 Unity/Ceedling 或 CMocka 做 C 侧单元测试。
- 若暂时没有 C 测试框架，先保留本仓库 Python 模型作为规格测试和审查基准。
