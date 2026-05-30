# Packet A Source Candidate - My_First_FOC.stwb6

This directory preserves a local MCSDK 6 Workbench project candidate found on
2026-05-15.

2026-05-16 user clarification: this file is a previous Workbench learning
artifact. Its `EVALSTDRIVE101` power-board choice was arbitrary and must not be
used as the custom STDRIVE101 board configuration source.

## Source

| Field | Value |
| --- | --- |
| Original path | `F:\STMCSDK\My_First_FOC.stwb6` |
| Preserved path | `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-15_my_first_foc/My_First_FOC.stwb6` |
| Original timestamp | 2026-04-27 16:37:42 |
| Workbench launcher | `F:\STMCSDK\MC_SDK_6.4.2\Utilities\PC_Software\STMCWB\STMCWB.exe` |
| Workbench version | 6.4.2 |
| Project format | MCSDK 6 Workbench `.stwb6` |

## Extracted Readback

The file is JSON-readable and records:

- `algorithm`: `FOC`
- `workBenchVersion`: `6.4.2`
- control board: `NUCLEO-G474RE`
- MCU: `STM32G474RETx`
- power board: `EVALSTDRIVE101`
- motor: `R57BLB50L2`

## Limits

This is a legacy Packet A source candidate, not a final accepted configuration
for the competition board.

It does not prove CN8 routing, the custom power-board endpoint map,
STDRIVE101 protection paths, Gate PWM behavior, Motor Profiler results, Hall
behavior, motor behavior, power-stage readiness, or sensorless behavior.

It also does not authorize generated-project trust. The dated review explains
which fields are accepted, partial, or still blocked.
