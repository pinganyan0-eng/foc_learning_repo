# Waveform evidence naming

本目录预留给未来单独批准的动态任务。本次准备任务不应产生 PWM/Gate 波形。

## Naming Format

```text
YYYY-MM-DD_WF-XX_signal_condition_scope-model.png
YYYY-MM-DD_WF-XX_signal_condition_scope-model.md
```

Example:

```text
2026-06-xx_WF-01_hin1_lin1_unloaded_SCOPEMODEL.png
```

## Sidecar Metadata

每张截图必须有同名 Markdown，至少记录：

- Evidence ID 和任务 ID。
- 板卡版本、固件 commit、`.ioc`/MCSDK 版本。
- 电源电压、限流、CV/CC 和输入电流。
- 电机是否断开。
- 探头型号、倍率、带宽限制和耦合方式。
- 每个通道的信号名、参考点、量程和探头类型。
- 时间基准、采样率、触发源和触发电平。
- nFAULT、REG12 和异常现象。
- 截图能证明的结论及不能证明的结论。

## Prohibited Evidence

- 无通道标签或无参考点说明的截图。
- 用普通探头地夹连接 OUTx/BOOTx 得到的截图。
- 无固件 commit、无供电条件或无探头型号的截图。
- 只截一小段波形却声称已证明三相、死区或保护全部正常。

