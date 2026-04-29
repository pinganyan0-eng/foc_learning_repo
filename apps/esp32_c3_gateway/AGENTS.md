# ESP32-C3 网关工程规则

1. UART 协议必须以 `interfaces/uart_protocol.md` 为准。
2. 不要随意改 STM32 侧字段名。
3. WebSocket 推送频率默认 20Hz。
4. 串口收包必须考虑断帧、丢包、checksum、seq。
5. 源文件多时拆 `components/`，不要全部塞进 `main/`。
6. ESP32-C3 只做边缘网关，不进入 STM32 FOC 实时控制环。
