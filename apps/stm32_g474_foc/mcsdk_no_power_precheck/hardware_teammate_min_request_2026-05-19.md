# Hardware Teammate Minimal Request - 2026-05-19

This is the short request to send to the hardware teammate first. It is derived
from `hardware_supplement_handoff_2026-05-19.md`.

It is not a wiring instruction, not a continuity record, not generated
firmware, and not hardware validation.

## Gate

| Field | Decision |
| --- | --- |
| Project goal | Advance the STM32G474 + self-developed STDRIVE101 driver-board P2 no-power precheck. |
| Learning goal | Get the smallest source packet that can turn board-side `CN3` clues into reviewable endpoint evidence. |
| Change scope | Hardware evidence request and later source-packet review only. |
| Forbidden scope | No 24V, no power-board connection, no motor connection, no Gate PWM output, no Motor Profiler, no source generation, no build, no flash. |

## Send This First

Please provide only these P0 materials first:

1. Confirm whether `Gerber_PCB2_2026-05-19.zip` is the exact PCB revision being
   fabricated, assembled, or tested.
2. Provide a complete `CN3 -> NUCLEO/CN8 -> STM32 pin` mapping table.
3. Provide marked evidence for `CN3` pin 1 and `J_HALL` pin 1 orientation.

Accepted source forms:

- marked board photo;
- order / fabrication screenshot;
- assembly drawing;
- EasyEDA Pro PCB screenshot or source;
- connector or harness drawing;
- readable table from the hardware teammate, with source date and board
  revision statement.

Oral description alone remains a clue and cannot unlock endpoint proof.

## Required Mapping Table

| CN3 pin | Board-side net | Hardware teammate must add |
| --- | --- | --- |
| 1 | `HIN1` | NUCLEO connector pin and STM32 pin |
| 2 | `LIN1` | NUCLEO connector pin and STM32 pin |
| 3 | `HIN2` | NUCLEO connector pin and STM32 pin |
| 4 | `LIN2` | NUCLEO connector pin and STM32 pin |
| 5 | `HIN3` | NUCLEO connector pin and STM32 pin |
| 6 | `LIN3` | NUCLEO connector pin and STM32 pin |
| 7 | `ADC_U` | NUCLEO connector pin and STM32 ADC / OPAMP endpoint |
| 8 | `ADC_V` | NUCLEO connector pin and STM32 ADC / OPAMP endpoint |
| 9 | `ADC_W` | NUCLEO connector pin and STM32 ADC / OPAMP endpoint |
| 10 | `IA` | NUCLEO connector pin and STM32 Hall endpoint |
| 11 | `IB` | NUCLEO connector pin and STM32 Hall endpoint |
| 12 | `IC` | NUCLEO connector pin and STM32 Hall endpoint |
| 13 | `NFAULT` | NUCLEO connector pin and STM32 break / fault endpoint |
| 14 | `3V3` | `3V3` source and connector endpoint |
| 15 | `GND_SIGNAL` | Ground endpoint and return path |

## Pin-1 Evidence

For `CN3` and `J_HALL`, please mark:

- the physical pin-1 location;
- the board side or viewing direction used in the photo or screenshot;
- any cable orientation, keyed connector, or silkscreen marker;
- whether the shown source matches the same PCB revision as the Gerber.

This prevents mirrored connector and Hall-order mistakes before any later
continuity or Workbench assignment review.

## Queued After P0

These are still needed, but they can follow the first P0 packet:

- Hall A/B/C relationship to `IA/IB/IC` and the actual Hall harness.
- If Hall B still uses `PB3/TIM2_CH2`, SWO release or isolation evidence;
  otherwise, the alternate Hall B endpoint.
- STDRIVE101 protection-chain details: `DT/MODE`, `STBY`, `CP`, `SCREF`
  threshold math, and `NFAULT` to STM32 break / fault path.
- EasyEDA Pro PCB layout source if available, not only Gerber.
- Later no-power DMM continuity / short-check table for `CN3`, `J_HALL`,
  motor phase connector, 24V/GND short check, and current-sense nets.

## Message Template

```text
我提供 P2 硬件最小补证。
文件路径：
来源日期/版本：
是否匹配当前打样/焊接/测试板：
补的是：Gerber PCB2 版本确认 / CN3-CN8-STM32 映射 / CN3 pin-1 / J_HALL pin-1
我没有接 24V、没有接功率板、没有接电机、没有运行 Motor Profiler、没有输出 Gate PWM。
```

## Current Decision

This file narrows the immediate hardware-teammate request. It does not upgrade
Packet A/B/C, PB3/SWO, `J_HALL`, generated-project trust, continuity, powered
readiness, motor readiness, Hall readiness, or sensorless readiness.
