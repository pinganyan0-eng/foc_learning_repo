# STDRIVE101 Manual Gate-Test USB-Only Runtime Lockout Execution Entry - 2026-06-20

## Summary

- Evidence ID:
  `EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-USBONLY-RUNTIME-LOCKOUT-EXECUTION-ENTRY-001`.
- Task ID:
  `TASK-2026-06-20-stdrive101-manual-gate-test-usbonly-runtime-lockout-execution-entry`.
- Scope:
  execution-entry record for one later USB-only lockout flash / run
  measurement pass.
- User request:
  `USB-only lockout runtime 检查`.
- User physical confirmations:
  HSPY / 24 V `OFF` and physically disconnected; `VS / 24V_FUSED < 1 V`;
  motor disconnected; `10 kohm` wake resistor / `LIN1` stimulus removed;
  Motor Pilot / Profiler closed; no abnormal heat / smell / sound.
- Decision:
  `STDRIVE101 manual gate-test USB-only runtime lockout execution entry /
  user confirmed HSPY 24 V OFF and physically disconnected, VS 24V_FUSED
  below 1 V, motor disconnected, wake stimulus removed, Motor Pilot and Motor
  Profiler closed, no abnormal heat smell sound / linked-image ELF hash matched
  / opens exactly one USB-only lockout flash-run measurement pass / no 24 V /
  no PWM-output validation / no Motor Pilot / no Motor Profiler / no motor
  connection / no powered-drive readiness`.

## Boundary

This record opens only one USB-only lockout flash / run measurement pass using
the exact candidate image below.

Still forbidden:

- 24 V;
- power-board powered connection;
- Gate PWM output or PWM validation;
- oscilloscope gate probing;
- Motor Pilot;
- Motor Profiler;
- motor connection;
- Hall closed loop;
- sensorless operation;
- power-stage readiness or motor readiness claims;
- any normal generated MCSDK application run.

If any instruction, tool, or screen tries to use the normal MCSDK project,
Motor Pilot, Motor Profiler, 24 V, PWM, or motor connection, stop and return
to source/build review.

## Image Identity

Candidate image:

| Item | Value |
| --- | --- |
| Target | `stdrive101_gate_lockout_image` |
| ELF | `.tmp/manual_gate_test_lockout_linked_image/stdrive101_gate_lockout_image.elf` |
| ELF SHA256 | `87BF3F7A28949F8DB654927292083609E52AB46C511CB6191D03B280DBFFE9B6` |
| MAP | `.tmp/manual_gate_test_lockout_linked_image/stdrive101_gate_lockout_image.map` |
| MAP SHA256 | `A020546A3D1D56B1C509939161BD80E5A25EC5843C928B9BC13E8D07684FF6C0` |

Accepted source/build evidence:

- `stdrive101_manual_gate_test_linked_image_build_only_record_2026-06-20.md`;
- source grep, ELF symbol screen, and MAP screen were clean for forbidden
  normal MCSDK start / command-ingress / PWM-output symbols;
- linked source forces the six MCU-facing STDRIVE101 inputs low and keeps TIM1
  outputs disabled.

## Allowed Execution Envelope

Only this envelope is opened:

| Item | Allowed state |
| --- | --- |
| Power | USB / ST-LINK only |
| HSPY / 24 V | OFF and physically disconnected |
| `VS / 24V_FUSED` | Confirmed below `1 V` before execution |
| Motor | Disconnected |
| Wake stimulus | Removed |
| Tooling | Direct flash / run of the reviewed lockout ELF only |
| Runtime goal | Observe static MCU-facing inputs and support rails |
| Runtime duration | Short enough to record the table below, then stop |

Do not use Motor Pilot, Motor Profiler, normal MCSDK start buttons, PC13
start/stop, MCP commands, or any command path that requests PWM output.

## Minimum Execution Steps

Use these steps only while the boundary above remains true:

1. Keep HSPY / 24 V physically disconnected.
2. Confirm `VS / 24V_FUSED < 1 V` before connecting / running USB.
3. Connect USB / ST-LINK only.
4. Flash and run only the reviewed
   `.tmp/manual_gate_test_lockout_linked_image/stdrive101_gate_lockout_image.elf`.
5. Do not press any normal MCSDK start button and do not open Motor Pilot or
   Motor Profiler.
6. Measure and record the table below.
7. Stop the debug session / remove USB after the measurements are recorded.

## Measurement Table To Fill

Do not infer values. Fill only from direct measurement.

| Item | Reading |
| --- | --- |
| `VS / 24V_FUSED` before USB | `___ V` |
| ELF hash shown / confirmed | `___` |
| HSPY / 24 V state | `OFF / physically disconnected` |
| motor disconnected | `yes / no` |
| wake resistor removed | `yes / no` |
| Motor Pilot / Profiler closed | `yes / no` |
| `CN3_1` driver input | `___ V` |
| `CN3_2 / LIN1` | `___ V` |
| `CN3_3` driver input | `___ V` |
| `CN3_4` driver input | `___ V` |
| `CN3_5` driver input | `___ V` |
| `CN3_6` driver input | `___ V` |
| `CN3_13 / nFAULT` | `___ V` |
| `CN3_14 / 3V3` | `___ V` |
| `REG12` | `___ V`; record only, no 12 V expectation in USB-only state |
| stop-rule hit | `yes / no`; reason `___` |

Expected safe result for `CN3_1` through `CN3_6`: close to `0 V`.

## Stop Rules

Stop immediately, stop the debug session / remove USB, and report the raw
observation if any of these occur:

- any of `CN3_1` through `CN3_6` is stable above `0.3 V`;
- `VS / 24V_FUSED` is not below `1 V`;
- the ELF hash or image path differs from the reviewed candidate image;
- the debugger enters normal MCSDK application code instead of the lockout
  loop;
- any tool asks for 24 V, Gate PWM, Motor Pilot, Motor Profiler, or motor
  connection;
- the board resets repeatedly, heats, smells, makes sound, or LEDs behave
  unexpectedly;
- a probe slips or a measurement point is uncertain.

Do not continue by trying one more time after a stop-rule event.

## Result Status

This record opens the USB-only lockout measurement pass but does not contain
the measured runtime result yet.

Status shorthand: does not contain the measured runtime result yet.

After the user reports the measurement table, create a separate runtime result
record. Until that result record exists, no USB-only runtime pass is claimed.

Next-record shorthand: create a separate runtime result record.

Still no 24 V, no PWM-output validation, no Motor Pilot, no Motor Profiler, no
motor connection, no powered-drive readiness, and no motor readiness.
