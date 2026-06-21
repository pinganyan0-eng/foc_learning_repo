# STDRIVE101 Manual Gate-Test 24V Static Lockout Phase-Gate Plan - 2026-06-20

## Summary

- Evidence ID:
  `EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-24V-STATIC-LOCKOUT-PHASE-GATE-PLAN-001`.
- Task ID:
  `TASK-2026-06-20-stdrive101-manual-gate-test-24v-static-lockout-phase-gate-plan`.
- Scope:
  phase-gate plan for a later bounded 24 V static lockout check after the
  USB-only lockout result.
- Hardware action:
  none in this record. No 24 V is applied by this plan.
- Firmware runtime action:
  none in this record. No flash, no Run / Debug, and no normal MCSDK app run.
- Decision:
  `STDRIVE101 manual gate-test 24V static lockout phase-gate plan / USB-only
  runtime lockout result accepted as driver-input-low evidence / earlier USB
  plus 24V static baseline carried forward / candidate 24V static lockout
  execution preconditions, measurement table, rollback path, and stop rules
  named / phase-gate plan only / no 24V execution in this record / no Gate PWM
  output / no Motor Pilot / no Motor Profiler / no motor connection / no
  powered-drive readiness`.

## Boundary

This record is a phase-gate plan only. It does not authorize:

- applying 24 V now;
- firmware flash;
- Run / Debug;
- normal generated MCSDK application execution;
- Gate PWM output or PWM validation;
- oscilloscope gate probing;
- Motor Pilot;
- Motor Profiler;
- motor connection;
- Hall closed loop;
- sensorless operation;
- power-stage readiness or motor readiness claims.

The practical conclusion is narrow: the project may prepare a later, separate
24 V static lockout execution-entry record, but only if fresh physical
preconditions are confirmed at that later moment.

## Evidence Accepted For Planning

Latest USB-only lockout runtime result:

```text
apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_usb_only_runtime_lockout_result_2026-06-20.md
```

Accepted USB-only evidence:

| Item | Value |
| --- | --- |
| ELF SHA256 | `87BF3F7A28949F8DB654927292083609E52AB46C511CB6191D03B280DBFFE9B6` |
| BIN SHA256 | `CBF833C8E9289D8B4A952C32C641CAA94928F1F8119C5DC528EBD779915EA6BE` |
| Download path | ST-LINK mass storage `D:` / `NOD_G474RE`; no `FAIL.TXT` after copy |
| `CN3_1` through `CN3_6` | all user-reported `0 V` |
| `CN3_13 / nFAULT` | user-reported `3.3 V` |
| `CN3_14 / 3V3` | user-reported `3.3 V` |
| `REG12` | user-reported `0 V` |
| Driver-input stop rule | not hit |

Earlier bounded static baseline carried forward:

```text
apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_usb24_static_recheck_result_2026-06-20.md
```

That earlier record reported USB/ST-LINK connected, HSPY `24 V / 0.2 A`,
motor disconnected, no flash / Run / Debug command, HSPY `CV`, current about
`0.045 A`, `CN3_1` through `CN3_6` close to `0 V`,
`CN3_13 / nFAULT = 3.3 V`, `CN3_14 / 3V3 = 3.3 V`, and `REG12 = 0.3 V`.

These two records support planning for one later static lockout check. They do
not prove PWM behavior, gate-driver output behavior, motor behavior, or general
powered-drive readiness.

## Preconditions For A Later 24V Static Execution Entry

A later record may open only a bounded 24 V static lockout check if all
preconditions below are confirmed in that later record before HSPY output is
enabled.

| Gate | Required before later execution |
| --- | --- |
| Explicit action request | User explicitly asks to execute the 24 V static lockout check, not just to plan. |
| Image state | The intended firmware state is still the reviewed lockout image, or a new dated record re-validates the exact image before any hardware action. |
| No normal MCSDK ingress | No `MC_StartMotor1`, `MCI_START`, PC13 start/stop, MCP / Motor Pilot ingress, `R3_2_TurnOnLowSides`, `PWMC_SwitchOnPWM`, or `LL_TIM_EnableAllOutputs` path is used. |
| HSPY initial state | HSPY output is `OFF` before wiring or probing. |
| HSPY limit | HSPY is set to `24 V / 0.2 A` current limit for the later static check only. |
| `VS / 24V_FUSED` before HSPY ON | DMM confirms below `1 V` before the later static check starts. |
| Motor state | Motor disconnected. |
| Wake stimulus | The `10 kohm` wake resistor / `LIN1` stimulus is removed. |
| USB/ST-LINK state | USB/ST-LINK may be connected only for the lockout static state; no Run / Debug command. |
| Tools | Motor Pilot and Motor Profiler closed / unused. |
| DMM reference | Black lead on board GND, such as `CN3_15 / GND`; red lead moves point by point. |
| Rollback path | HSPY output OFF first, then confirm `VS / 24V_FUSED < 1 V` before any wiring change. |

If any gate is missing, the later task must stay at planning or source/build
review and must not apply 24 V.

## Candidate Later Measurement Table

Do not fill this table in this record. Use it only in a later explicitly opened
24 V static lockout execution/result record.

| Item | Required or expected value |
| --- | --- |
| Record date/time | `___` |
| Operator confirmation | `24 V static lockout check explicitly requested` |
| HSPY initial output | `OFF` |
| HSPY setting | `24 V / 0.2 A` |
| `VS / 24V_FUSED` before HSPY ON | `< 1 V`, raw reading `___ V` |
| Motor | `disconnected` |
| Wake resistor | `removed` |
| Motor Pilot / Profiler | `closed / unused` |
| USB/ST-LINK | `connected / no Run Debug` |
| HSPY state after ON | `CV / CC`, raw state `___` |
| HSPY current after ON | `___ A` |
| `CN3_1` driver input | `___ V` |
| `CN3_2 / LIN1` | `___ V` |
| `CN3_3` driver input | `___ V` |
| `CN3_4` driver input | `___ V` |
| `CN3_5` driver input | `___ V` |
| `CN3_6` driver input | `___ V` |
| `CN3_13 / nFAULT` | `___ V` |
| `CN3_14 / 3V3` | `___ V` |
| `REG12` | `___ V` |
| Stop-rule hit | `yes / no`, raw reason `___` |
| Closeout | HSPY output `OFF`, `VS / 24V_FUSED = ___ V` |

Expected static result for the six driver-input rows is close to `0 V`. Treat
any stable reading above `0.3 V` on `CN3_1` through `CN3_6` as a stop-rule
event, not as a value to tune around.

## Stop Rules For The Later Static Check

Stop immediately, turn HSPY output OFF, remove USB power if needed, and return
to source/build review if any of these occur:

- any of `CN3_1` through `CN3_6` is stable above `0.3 V`;
- HSPY enters `CC`, current rises unexpectedly, or current is above `0.08 A`
  in the static all-inputs-low state;
- `CN3_13 / nFAULT` falls low or is unstable;
- `REG12` rises unexpectedly above `1 V` in the all-inputs-low static state;
- `CN3_14 / 3V3` is not near `3.3 V`;
- the board resets repeatedly, heats, smells, makes sound, or LEDs behave
  unexpectedly;
- a probe slips or a measurement point is uncertain;
- any instruction path asks for Gate PWM, Motor Pilot, Motor Profiler, a motor
  connection, or normal generated MCSDK Run / Debug.

Do not continue by trying one more time after a stop-rule event. Record the raw
observation and return to no-power source/build review.

## Decision For Progress

The next engineering checkpoint is not motor power. It is a later, separate,
explicit 24 V static lockout execution-entry record only if the user asks to
execute it and the preconditions above are still true at that later moment.

Still forbidden after this plan:

- 24 V execution by default;
- flash;
- Run / Debug;
- Gate PWM output;
- Motor Pilot / Profiler;
- motor connection;
- power-stage readiness or motor readiness claims.
