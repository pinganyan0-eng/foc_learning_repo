# STM32G474 FOC 学习助手入口

这个工作区已经把项目资料抽取成可检索语料，后续我会默认参考这里的内容来做学习辅导、代码解释、排查清单和报告审稿。

## 我现在的默认设定
- 默认辅导对象：B 同学，算法工程师/主控同学。
- 项目主线：STM32G474 + STDRIVE101 + 三相 BLDC + Hall 保底 + SMO 无感冲刺 + ESP32-C3 边缘网关。
- 工具链口径：VS Code + STM32CubeIDE 插件 + STM32CubeMX + MCSDK；不使用独立 STM32CubeIDE 作为主 IDE。
- 资料优先级：V9/V8/硬件审查意见 > 技术报告 > 8 周/56 天学习计划 > 早期 V7.1。
- 工程原则：先让电机安全转起来，再做无感、性能优化和答辩亮点。

## 已配置的本地资料库
- `assistant_profile.md`：我的学习助手身份和项目优先级。
- `linked_article_rules.md`：共享链接文章固化出的助手规则、项目红线和学习路线。
- `source_manifest.json`：已摄入文件清单。
- `extracted/`：每份 HTML/PDF/DOCX 抽取后的文本。
- `extracted/st_manuals/`：ST 官方手册和应用笔记的本地文本抽取。
- `../references/st_manuals_index.md`：已摄入 ST 官方 PDF 的索引、用途和检索优先级。
- `../vector_store/`：本仓库资料生成的本地检索索引。
- `../tools/ask_local.py`：本地资料检索问答工具。
- `../CURRENT_STATUS.md`：项目总控页，记录当前阶段、缺口和下一步。
- `../workflow/algo_b_teaching_delivery_plan.md`：B 算法/主控计划的执行版，规定教学进度、补课机制、每课/每周上交物和禁止推进范围。
- `../learning/NEXT_LESSON.md`：下一课执行卡，给出当前最该教什么、先复习什么、产出什么。
- `../learning/MASTERY_MAP.md`：掌握证据地图，避免反复问已经证明的低价值问题。
- `../workflow/current_learning_sprint.md`：当前学习 sprint，列出 P2 MCSDK 无功率预检交付物、冲突清单和退出条件。
- `../workflow/phase_gate_checklist.md`：阶段闸门表，判断能不能进入下一阶段。
- `../workflow/intake_checklist.md`：首次资料导入清单，判断新资料应该放哪里。

## 常用检索命令
```powershell
python tools/ask_local.py "STDRIVE101 SCREF"
```

```powershell
python tools/ask_local.py "HAL_UARTEx_ReceiveToIdle_DMA"
```

## 当前第一阶段建议
1. 先确认 Windows 开发工具：VS Code、STM32CubeIDE 插件、STM32CubeMX、MCSDK、CubeMonitor、ST-LINK 驱动、Arduino IDE。
2. B 同学已完成当前 P1 概念层检查，下一步先做 P2 MCSDK 无功率预检：工具版本/status、Workbench/CubeMX 配置证据、pin/config 冲突清单。
3. Motor Profiler 仍只是计划项；真实扫电机参数、Hall 闭环和 PI 调参必须等后续阶段闸门。
4. 硬件板未完全确认前，不做 24V 大电流实测；首次上电必须限流 0.2A。

## 你可以直接这样叫我
- “今天学什么”
- “带我做 Day 1”
- “帮我排查 UART DMA + IDLE”
- “帮我看 MCSDK 配置”
- “帮我审硬件风险”
- “帮我改技术报告”
