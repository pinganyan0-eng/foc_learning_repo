# UART Protocol

## 2026-05-14 Host Model Status

- `src/protocol_model.py` now includes `LineFramer`.
- `LineFramer.feed(...)` accepts DMA/IDLE-like byte chunks and returns complete
  newline-terminated frames.
- Empty lines are ignored.
- Oversize partial frames are dropped until the next line ending and counted
  with `overflow_count`.
- `tests/test_protocol_model.py` covers chunk-split frames, multiple frames in
  one chunk, empty lines, oversize recovery, and recovery when the overlong
  frame spans DMA/IDLE-like chunks.

STM32 与 ESP32-C3 之间采用 UART DMA + IDLE 接收，一行一个 JSON 帧，`\n` 结尾。

## 基础命令帧

```json
{"cmd":"set_speed","rpm":1200,"seq":17}
```

## 基础状态帧

```json
{"type":"status","rpm":1180,"target_rpm":1200,"state":"RUNNING","fault":0,"seq":17}
```

## 规则

- 单帧建议不超过 256 字节。
- STM32 端必须做长度、末字节、JSON、字段类型、状态机五层校验。
- 速度命令进入实时环前必须被主循环校验并写入安全目标值。
- JEOC/FOC ISR 不解析 UART。
