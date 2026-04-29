# protocol

        ## 通信边界

        STM32 负责 FOC 实时控制，ESP32-C3 只做边缘网关和可视化。两者之间采用 UART DMA + IDLE 接收，应用层使用一行一个 JSON 帧，`
` 结尾。

        ## 基础帧格式

        ```json
        {"cmd":"set_speed","rpm":1200,"seq":17}
        ```

        - `cmd`：命令名，必填。
        - `seq`：上位机序号，可选，回包时原样带回。
        - 每帧最大建议 256 字节。
        - STM32 端必须做末字节、长度、JSON、字段类型、状态机五层校验。

        ## 命令

        | 命令 | 参数 | 允许状态 | 动作 |
        | --- | --- | --- | --- |
        | `heartbeat` | 无 | 任意 | 回 ACK |
        | `arm` | 无 | `IDLE` | 进入 `ARMED` |
        | `set_speed` | `rpm` 整数 | `ARMED`/`RUNNING` | 设定目标转速 |
        | `stop` | 无 | `ARMED`/`RUNNING` | 目标转速清零，回 `IDLE` |
        | `clear_fault` | 无 | `FAULT` | 清故障并回 `IDLE` |

        ## 错误码

        | 码 | 名称 | 含义 |
        | --- | --- | --- |
        | 0 | `OK` | 成功 |
        | 100 | `ERR_BAD_JSON` | JSON 解析失败 |
        | 101 | `ERR_BAD_FRAME` | 空帧、过长、非对象、缺字段 |
        | 102 | `ERR_UNKNOWN_CMD` | 未知命令 |
        | 103 | `ERR_BAD_VALUE` | 字段类型或取值非法 |
        | 104 | `ERR_STATE` | 当前状态不允许该命令 |
        | 105 | `ERR_FAULT` | 故障态未清除，拒绝运行命令 |

        ## 速度命令约束

        - 默认限幅：`-4000 <= rpm <= 4000`。
        - `rpm = 0` 表示保持已使能但不转，或由 `stop` 回到 `IDLE`。
        - 任何来自 ESP32/Web 的命令不能直接改 PI 参数或进入 JEOC 实时环；实时环只读已经校验过的目标值。

        ## 实时中断原则

        - JEOC/FOC ISR 中禁止 `printf`、`HAL_Delay`、JSON 解析、WebSocket、动态内存和长耗时分支。
        - ISR 只做采样读取、坐标变换、PI/FOC、PWM 更新、短故障标志。
        - 日志放到低优先级任务或主循环中，通过环形缓冲输出。
