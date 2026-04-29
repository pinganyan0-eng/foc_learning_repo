# STM32G474 FOC 学习助手入口

这个工作区已经把项目资料抽取成可检索语料，后续我会默认参考这里的内容来做学习辅导、代码解释、排查清单和报告审稿。

## 我现在的默认设定
- 默认辅导对象：B 同学，算法工程师/主控同学。
- 项目主线：STM32G474 + STDRIVE101 + 三相 BLDC + Hall 保底 + SMO 无感冲刺 + ESP32-C3 边缘网关。
- 资料优先级：V9/V8/硬件审查意见 > 技术报告 > 8 周/56 天学习计划 > 早期 V7.1。
- 工程原则：先让电机安全转起来，再做无感、性能优化和答辩亮点。

## 已配置的本地资料库
- `assistant_profile.md`：我的学习助手身份和项目优先级。
- `linked_article_rules.md`：共享链接文章固化出的助手规则、项目红线和学习路线。
- `source_manifest.json`：已摄入文件清单。
- `corpus_all.txt`：所有资料合并语料。
- `extracted/`：每份 HTML/PDF/DOCX 抽取后的文本。
- `search_materials.py`：关键词检索工具。
- `today_template.md`：每日学习记录模板。

## 常用检索命令
```powershell
& 'C:\Users\gregrg\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' 'C:\Users\gregrg\Documents\Codex\2026-04-30\new-chat\learning_assistant\search_materials.py' STDRIVE101 SCREF
```

```powershell
& 'C:\Users\gregrg\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' 'C:\Users\gregrg\Documents\Codex\2026-04-30\new-chat\learning_assistant\search_materials.py' HAL_UARTEx_ReceiveToIdle_DMA
```

## 当前第一阶段建议
1. 先确认 Windows 开发工具：STM32CubeIDE、STM32CubeMX、MCSDK、CubeMonitor、ST-LINK 驱动、Arduino IDE。
2. B 同学先做 NUCLEO-G474RE 基础工程：点灯、串口 printf、UART DMA + IDLE。
3. 再进入 MCSDK：Motor Profiler 扫电机参数，Hall 闭环跑通，PI 调参。
4. 硬件板未完全确认前，不做 24V 大电流实测；首次上电必须限流 0.2A。

## 你可以直接这样叫我
- “今天学什么”
- “带我做 Day 1”
- “帮我排查 UART DMA + IDLE”
- “帮我看 MCSDK 配置”
- “帮我审硬件风险”
- “帮我改技术报告”
