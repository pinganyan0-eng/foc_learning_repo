# STDRIVE101 Manual Gate-Test 24V Static Lockout Execution Entry - 2026-06-20

## Summary

- Evidence ID:
  `EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-24V-STATIC-LOCKOUT-EXECUTION-ENTRY-001`.
- Task ID:
  `TASK-2026-06-20-stdrive101-manual-gate-test-24v-static-lockout-execution-entry`.
- Scope:
  execution-entry record for one bounded 24 V static lockout measurement pass
  after the USB-only lockout result and the 24 V static phase-gate plan.
- User request:
  start the next step after the 24 V static lockout phase-gate plan.
- User physical confirmations:
  all required gates are satisfied; HSPY output is `OFF`; HSPY is set to
  `24 V / 0.2 A`; `VS / 24V_FUSED` is close to `0 V` and below `1 V`;
  motor is disconnected; `10 kohm` wake resistor / `LIN1` stimulus is removed;
  Motor Pilot / Profiler are closed; no abnormal board heat, smell, or sound.
- Decision:
  `STDRIVE101 manual gate-test 24V static lockout execution entry / user
  confirmed HSPY output OFF, HSPY set to 24 V 0.2 A, VS 24V_FUSED close to
  0 V and below 1 V, motor disconnected, wake stimulus removed, Motor Pilot
  and Motor Profiler closed, no abnormal heat smell sound / USB-only lockout
  result accepted as driver-input-low evidence / opens exactly one bounded
  24 V static lockout measurement pass / no Gate PWM output / no Motor Pilot /
  no Motor Profiler / no motor connection / no powered-drive readiness`.

## Boundary

This record opens only one bounded 24 V static lockout measurement pass. It
does not contain the measured 24 V static result yet.

Allowed by this entry only:

- keep the reviewed lockout image state active;
- keep USB / ST-LINK connected if already in the lockout runtime state;
- keep Motor Pilot and Motor Profiler closed;
- keep the motor disconnected;
- keep the `10 kohm` wake resistor / `LIN1` stimulus removed;
- turn HSPY output ON once for the static all-inputs-low measurement;
- measure only the table below, then turn HSPY output OFF.

Still forbidden:

- firmware flash or any new Run / Debug action;
- normal generated MCSDK application execution;
- `MC_StartMotor1`, `MCI_START`, PC13 start / stop, MCP command ingress,
  `R3_2_TurnOnLowSides`, `PWMC_SwitchOnPWM`, or
  `LL_TIM_EnableAllOutputs` paths;
- Gate PWM output or PWM validation;
- oscilloscope gate probing;
- Motor Pilot;
- Motor Profiler;
- motor connection;
- Hall closed loop;
- sensorless operation;
- power-stage readiness or motor readiness claims.

If any instruction, tool, or screen tries to use normal MCSDK start, Motor
Pilot, Motor Profiler, Gate PWM, or a motor connection, stop and return to
source/build review.

## Evidence Carried Forward

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

Phase-gate plan:

```text
apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_24v_static_lockout_phase_gate_plan_2026-06-20.md
```

That plan named the later execution gates, measurement table, rollback path,
and stop rules. This entry records that the user has now confirmed the gates
for one bounded static pass.

## Entry Preconditions

| Gate | Entry value |
| --- | --- |
| Explicit action request | User asked to continue the next step after the phase-gate plan |
| Lockout image state | Reviewed lockout image remains the intended firmware state |
| Normal MCSDK ingress | Not used; no normal MCSDK start / command path opened |
| HSPY initial state | Output `OFF` |
| HSPY setting | `24 V / 0.2 A` current limit |
| `VS / 24V_FUSED` before HSPY ON | User-reported close to `0 V`, below `1 V` |
| Motor state | Disconnected |
| Wake stimulus | `10 kohm` wake resistor / `LIN1` stimulus removed |
| USB/ST-LINK state | May remain connected only for the lockout static state; no new Run / Debug |
| Tools | Motor Pilot and Motor Profiler closed / unused |
| Board condition | No abnormal heat, smell, or sound reported |
| DMM reference | Black lead stays on board GND, such as `CN3_15 / GND`; red lead moves point by point |
| Rollback path | HSPY output OFF first, then confirm `VS / 24V_FUSED < 1 V` before any wiring change |

## Allowed Static Measurement Steps

Use these steps only while all entry preconditions above remain true:

1. Keep the motor disconnected and keep the wake resistor removed.
2. Keep Motor Pilot and Motor Profiler closed.
3. Keep the DMM black lead on board GND, such as `CN3_15 / GND`.
4. Confirm HSPY is still `OFF` and set to `24 V / 0.2 A`.
5. Confirm `VS / 24V_FUSED` is still below `1 V`.
6. Turn HSPY output ON once.
7. Measure only the table below.
8. Turn HSPY output OFF.
9. Confirm `VS / 24V_FUSED < 1 V` before any wiring or probe change.

Do not press PC13, do not send commands, do not open Motor Pilot or Motor
Profiler, and do not use any normal generated MCSDK Run / Debug path.

## Measurement Table To Fill In The Result Record

Do not infer values. Fill only from direct measurement after this execution
entry.

| Item | Reading |
| --- | --- |
| HSPY initial output | `OFF` |
| HSPY setting | `24 V / 0.2 A` |
| `VS / 24V_FUSED` before HSPY ON | close to `0 V`, below `1 V` |
| Motor | `disconnected` |
| Wake resistor | `removed` |
| Motor Pilot / Profiler | `closed / unused` |
| USB/ST-LINK | `connected / no new Run Debug` |
| HSPY state after ON | `___` |
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

Expected static result for `CN3_1` through `CN3_6`: close to `0 V`. Treat any
stable reading above `0.3 V` on `CN3_1` through `CN3_6` as a stop-rule event,
not as a value to tune around.

## Stop Rules

Stop immediately, turn HSPY output OFF, remove USB power if needed, and report
the raw observation if any of these occur:

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

Do not continue by trying one more time after a stop-rule event.

## Result Status

This record opens one bounded 24 V static lockout measurement pass but does
not contain the measured result yet.

Status shorthand: does not contain the measured 24 V static result yet.

After the user reports the measurement table, create a separate 24 V static
lockout result record. Until that result record exists, no 24 V static
lockout pass result is claimed.

Still no Gate PWM output, no Motor Pilot, no Motor Profiler, no motor
connection, no powered-drive readiness, and no motor readiness.
