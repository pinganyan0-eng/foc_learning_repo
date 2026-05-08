# 首次资料导入清单

用途：新资料进入仓库时，先按本清单分类、命名和检查，避免资料堆在一起后无法追溯。

## 导入前先判断类型

| 资料类型 | 放置位置 | 命名建议 | 导入后先检查 |
| --- | --- | --- | --- |
| STM32CubeMX/MCSDK 工程 | `apps/stm32_g474_foc/` | 保持 ST 生成原目录和文件名 | `.ioc`、`Core/`、`Drivers/`、`Middlewares/`、`MotorControl/` 是否齐全 |
| ESP32-C3 工程 | `apps/esp32_c3_gateway/` | 保持 ESP-IDF 原结构 | `CMakeLists.txt`、`main/`、`components/` 是否齐全 |
| 原理图 | `hardware/schematic/` | `YYYY-MM-DD_board_rev_schematic.pdf` | STDRIVE101、采样、保护、接口、供电页是否清楚 |
| PCB 截图或布局文件 | `hardware/pcb/` | `YYYY-MM-DD_board_rev_pcb.*` | 功率环路、Kelvin、GND 平面、Gate 走线是否可审 |
| BOM | `hardware/bom/` | `YYYY-MM-DD_board_rev_bom.xlsx` | MOSFET、采样电阻、DC-DC、保护器件型号是否完整 |
| Gerber/坐标文件 | `hardware/fabrication/` | `YYYY-MM-DD_board_rev_gerber.zip` | 板层、坐标、装配方向是否明确 |
| 串口日志 | `experiments/YYYY-MM-DD_topic/logs/` | `uart_raw_YYYY-MM-DD_HHMM.txt` | 保留原始日志，不只贴截图 |
| 示波器截图 | `experiments/YYYY-MM-DD_topic/waveforms/` | `gate_uvw_YYYY-MM-DD_HHMM.png` | 标明通道、探头倍率、时间基准和电压基准 |
| Motor Profiler 结果 | `experiments/YYYY-MM-DD_motor_profiler/` | `motor_profiler_result.*` | Rs、Ls、Ke、极对数、额定电压/电流是否记录 |
| 报告/PPT/视频脚本 | `deliverables/` | 按子目录规则命名 | 卖点是否能追溯到来源或实验 |
| 官方资料 PDF | `references/` 或 `materials/extracted/st_manuals/` | 保留官方文件名或加 ST 文档号 | 记录标题、版本、用途和优先级 |

## 导入后必须补的元信息

- 来源：文件来自哪里，是否官方，是否用户实测。
- 日期：资料生成或导入日期。
- 版本：板卡版本、固件版本、工具版本或文档版本。
- 可信度：官方资料、项目当前方案、实测记录、历史参考、临时草稿。
- 关联：它影响硬件、固件、协议、测试、报告还是答辩。

## Codex 接到新资料后的默认动作

1. 先分类放置，不改变原始工程生成结构。
2. 更新 `CURRENT_STATUS.md` 的当前阶段和资料缺口。
3. 必要时更新 `materials/source_manifest.json`、`docs/file_map.md` 或 `references/` 索引。
4. 如果资料进入 `materials/`、`docs/`、`references/` 或 `workflow/`，重建 `vector_store/`。
5. 如果进入源码或协议，运行相关测试；没有测试时说明测试缺口。

## 不要这样做

- 不把真实工程放到 `materials/` 或 `docs/`。
- 不把实验日志只贴在聊天里，必须落到 `experiments/`。
- 不把早期方案覆盖 V9/current status，冲突时先记录冲突。
- 不把 PDF 截图当作唯一证据，能保留原文件就保留原文件。
- 不为美观拆散 CubeMX、MCSDK 或 ESP-IDF 自动生成目录。

