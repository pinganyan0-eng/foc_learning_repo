# ESP32 Command Frame

ESP32-C3 从网页按钮或本地策略生成命令帧，转发给 STM32。

```json
{"cmd":"set_speed","rpm":1200,"seq":17}
```

ESP32 不直接修改 PI 参数、不直接控制 PWM、不进入 FOC 实时环。
