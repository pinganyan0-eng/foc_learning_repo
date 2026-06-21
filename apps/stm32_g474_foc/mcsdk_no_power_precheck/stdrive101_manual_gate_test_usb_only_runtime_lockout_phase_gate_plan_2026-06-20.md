# STDRIVE101 Manual Gate-Test USB-Only Runtime Lockout Phase-Gate Plan - 2026-06-20

## Summary

- Evidence ID:
  `EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-USBONLY-RUNTIME-LOCKOUT-PHASE-GATE-PLAN-001`.
- Task ID:
  `TASK-2026-06-20-stdrive101-manual-gate-test-usbonly-runtime-lockout-phase-gate-plan`.
- Scope:
  phase-gate plan for a later USB-only runtime lockout check.
- Hardware action:
  none.
- Firmware runtime action:
  none; no flash, no Run / Debug, and no USB runtime execution in this record.
- Decision:
  `STDRIVE101 manual gate-test USB-only runtime lockout phase-gate plan no-power /
  linked-image build-only record accepted as image-boundary evidence /
  candidate USB-only runtime preconditions, measurement table, and stop rules
  named / phase-gate plan only / no flash / no Run Debug / no USB runtime
  execution / no 24 V / no PWM-output validation / no powered-drive
  readiness`.

## Boundary

This record is a phase-gate plan only. It does not authorize:

- firmware flash;
- Run / Debug;
- USB runtime execution;
- 24 V;
- power-board powered connection;
- Gate PWM output;
- oscilloscope gate probing;
- Motor Pilot;
- Motor Profiler;
- motor connection;
- Hall closed loop;
- sensorless operation;
- power-stage readiness or motor readiness.

The practical boundary is still no Gate PWM output, no motor action, and no
readiness claim.

Decision boundary shorthand: no powered-drive readiness.

## Build Evidence Accepted For Planning

The latest accepted image-boundary evidence is:

```text
apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_linked_image_build_only_record_2026-06-20.md
```

Candidate image identity for a later USB-only runtime phase:

| Item | Value |
| --- | --- |
| Target | `stdrive101_gate_lockout_image` |
| ELF | `.tmp/manual_gate_test_lockout_linked_image/stdrive101_gate_lockout_image.elf` |
| ELF SHA256 | `87BF3F7A28949F8DB654927292083609E52AB46C511CB6191D03B280DBFFE9B6` |
| MAP | `.tmp/manual_gate_test_lockout_linked_image/stdrive101_gate_lockout_image.map` |
| MAP SHA256 | `A020546A3D1D56B1C509939161BD80E5A25EC5843C928B9BC13E8D07684FF6C0` |
| Toolchain | STM32Cube GNU Arm GCC `14.3.1` |
| CMake system | `Generic` / `arm` |
| Build type | `Debug` |

The build-only record also shows:

- ELF and MAP were produced and hashed;
- key startup / lockout symbols were present;
- source grep, ELF symbol screen, and MAP screen were clean for forbidden
  normal MCSDK start / command-ingress / PWM-output symbols;
- linked source still uses the isolated lockout path that forces the six
  MCU-facing STDRIVE101 inputs low and keeps TIM1 outputs disabled.

This accepted evidence is enough to write a USB-only runtime phase-gate plan.
It is not enough to flash or execute runtime.

## Preconditions For A Later Runtime Record

A later record may open only a USB-only lockout runtime if all preconditions
below are confirmed in that later record before any flash or run action.

| Gate | Required before later execution |
| --- | --- |
| Explicit action request | User explicitly asks to execute the USB-only lockout runtime check, not just to plan. |
| Image identity | ELF path and SHA256 match the candidate image above, or a new linked-image build-only record replaces it. |
| No normal MCSDK ingress | The later record re-confirms no `MC_StartMotor1`, `MCI_START`, PC13 start/stop, MCP / Motor Pilot ingress, `R3_2_TurnOnLowSides`, `PWMC_SwitchOnPWM`, or `LL_TIM_EnableAllOutputs` in the image path. |
| Physical power state | HSPY / 24 V is OFF and physically not powering the board. |
| `VS / 24V_FUSED` | DMM confirms below `1 V` before USB-only runtime. |
| Motor state | Motor disconnected. |
| Wake stimulus | The `10 kohm` wake resistor / LIN1 stimulus is removed. |
| Tools | Motor Pilot and Motor Profiler closed / unused. |
| Debug scope | Only the reviewed lockout image may be flashed or run; no normal generated MCSDK app. |
| Rollback / stop path | Stop rules below are visible and accepted before execution. |

If any gate is missing, the later task must stay at planning or source/build
review and must not execute runtime.

## Candidate Later USB-Only Measurement Table

Do not fill this table in this record. Use it only in a later explicitly opened
USB-only runtime record.

| Item | Required or expected value |
| --- | --- |
| Record date/time | `___` |
| Operator confirmation | `USB-only lockout runtime explicitly requested` |
| ELF path | `___` |
| ELF SHA256 | `___` |
| HSPY / 24 V | `OFF / disconnected` |
| `VS / 24V_FUSED` before USB | `< 1 V`, raw reading `___ V` |
| Motor | `disconnected` |
| Wake resistor | `removed` |
| Motor Pilot / Profiler | `closed / unused` |
| `CN3_1` driver input | `___ V` |
| `CN3_2 / LIN1` | `___ V` |
| `CN3_3` driver input | `___ V` |
| `CN3_4` driver input | `___ V` |
| `CN3_5` driver input | `___ V` |
| `CN3_6` driver input | `___ V` |
| `CN3_13 / nFAULT` | `___ V` |
| `CN3_14 / 3V3` | `___ V` |
| `REG12` | `___ V`; record only, no 12 V expectation in USB-only state |
| Stop-rule hit | `yes / no`, raw reason `___` |

Expected safe result for the six driver-input rows is close to `0 V`. Treat any
stable reading above `0.3 V` on `CN3_1` through `CN3_6` as a stop-rule event,
not as a value to tune around.

## Stop Rules For The Later Runtime

Stop immediately, remove USB power / stop the debug session, and return to
source/build review if any of these occur:

- any of `CN3_1` through `CN3_6` is stable above `0.3 V`;
- `VS / 24V_FUSED` is not below `1 V` before USB-only runtime;
- ELF hash or image provenance does not match the reviewed lockout image;
- the debugger enters normal MCSDK application code instead of the lockout
  loop;
- any instruction path asks for 24 V, Gate PWM, Motor Pilot, Motor Profiler,
  or motor connection;
- the board resets repeatedly, heats, smells, makes sound, or LEDs behave
  unexpectedly;
- a probe slips or a measurement point is uncertain.

Do not continue by trying one more time after a stop-rule event. Record the raw
observation and return to no-power source/build review.

## Decision For Progress

The next engineering checkpoint is not motor power. It is a later, separate,
explicit USB-only runtime execution record only if the user asks to execute it
and the preconditions above are still true at that later moment.

Still forbidden after this plan:

- flash;
- Run / Debug;
- USB runtime execution;
- 24 V;
- Gate PWM output;
- Motor Pilot / Profiler;
- motor connection;
- power-stage readiness or motor readiness claims.
