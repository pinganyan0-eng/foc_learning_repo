---
type: index
status: active
area: engineering
tags:
  - foc/engineering
---

# 工程索引

## 代码与契约

- STM32 工程：[[apps/stm32_g474_foc/README]]
- ESP32-C3 工程：[[apps/esp32_c3_gateway/README]]
- UART 协议：[[interfaces/uart_protocol]]
- 状态帧：[[interfaces/stm32_status_frame]]
- 命令帧：[[interfaces/esp32_command_frame]]
- 故障码：[[interfaces/fault_codes]]

## 关键规则

- STM32 负责 FOC 实时环。
- ESP32-C3 只做显示、转发、告警和非实时命令入口。
- 任何协议字段先改 `interfaces/`，再改代码和文档。

## 工程任务

```tasks
not done
path includes notes/20_engineering
sort by priority
sort by due
```
