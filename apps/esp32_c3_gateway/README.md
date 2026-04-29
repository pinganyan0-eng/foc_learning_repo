# ESP32-C3 边缘网关工程

这里放真实 ESP32-C3 工程。推荐按 ESP-IDF 习惯组织：

- `main/`：入口和轻量 glue code。
- `components/uart_bridge/`：STM32 UART 透传。
- `components/websocket_server/`：WebSocket 服务。
- `components/web_ui/`：本地看板资源。
- `components/telemetry_protocol/`：帧解析、校验、序号和错误处理。
