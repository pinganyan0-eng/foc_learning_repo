# STDRIVE101 Manual Gate-Test 24V Static Lockout Carry-Forward Result - 2026-06-20

## Summary

- Evidence ID:
  `EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-24V-STATIC-LOCKOUT-CARRY-FORWARD-RESULT-001`.
- Task ID:
  `TASK-2026-06-20-stdrive101-manual-gate-test-24v-static-lockout-carry-forward-result`.
- Scope:
  no-repeat carry-forward result after the user clarified that the equivalent
  USB + 24 V static all-inputs-low check had already been measured and
  recorded.
- Hardware action:
  none in this record. No repeated 24 V measurement is requested or performed
  by this record.
- Decision:
  `STDRIVE101 manual gate-test 24V static lockout carry-forward result /
  no repeated measurement / existing USB plus 24V static recheck carried
  forward with HSPY CV about 0.045 A, CN3_1 through CN3_6 all close to 0 V,
  nFAULT 3.3 V, CN3_14 3.3 V, REG12 0.3 V / USB-only lockout runtime result
  carried forward as reviewed lockout image driver-input-low evidence /
  static baseline accepted for no-repeat gating only / no claim of new 24V
  lockout measurement under lockout image / no Gate PWM output / no Motor
  Pilot / no Motor Profiler / no motor connection / no powered-drive
  readiness`.

## Boundary

This is a consolidation record, not a new hardware measurement.

It does:

- acknowledge the user's correction that the USB + 24 V static state had
  already been measured and recorded;
- carry forward the earlier USB + 24 V static recheck as the static
  all-inputs-low 24 V evidence;
- carry forward the USB-only lockout runtime result as reviewed lockout-image
  driver-input-low evidence;
- remove the need to repeat the same static 24 V table unless wiring,
  firmware image, board condition, or tool state changes.

It does not:

- claim a new 24 V measurement happened after the
  `stdrive101_manual_gate_test_24v_static_lockout_execution_entry_2026-06-20.md`
  entry;
- claim a simultaneous "lockout image + 24 V" fresh direct measurement;
- authorize firmware flash, new Run / Debug, normal generated MCSDK app run,
  Gate PWM output, Motor Pilot, Motor Profiler, motor connection, Hall closed
  loop, sensorless operation, power-stage readiness, or motor readiness.

## Carry-Forward Evidence

Existing USB + 24 V static recheck:

```text
apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_usb24_static_recheck_result_2026-06-20.md
```

Accepted static rows from that record:

| Item | Existing recorded value |
| --- | --- |
| USB/ST-LINK | connected |
| HSPY setting | `24 V / 0.2 A` current limit |
| HSPY state | `CV` |
| HSPY current | about `0.045 A` |
| Motor | disconnected |
| Wake stimulus | `10 kohm` wake resistor / `LIN1` stimulus removed |
| Flash / Run / Debug command | none |
| `CN3_1` through `CN3_6` | all close to `0 V` |
| `CN3_13 / nFAULT` | `3.3 V` |
| `CN3_14 / 3V3` | `3.3 V` |
| `REG12` | `0.3 V` |

The existing record reports the six driver input pins as a group rather than
as a per-pin numeric table. Treat it as a bounded static summary reading, not
as a pin-by-pin waveform or runtime proof.

USB-only lockout runtime result:

```text
apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_usb_only_runtime_lockout_result_2026-06-20.md
```

Accepted lockout rows from that record:

| Item | Existing recorded value |
| --- | --- |
| ELF SHA256 | `87BF3F7A28949F8DB654927292083609E52AB46C511CB6191D03B280DBFFE9B6` |
| BIN SHA256 | `CBF833C8E9289D8B4A952C32C641CAA94928F1F8119C5DC528EBD779915EA6BE` |
| Copy result | ST-LINK mass storage `D:` / `NOD_G474RE`; no `FAIL.TXT` after copy |
| `CN3_1` | `0 V` |
| `CN3_2 / LIN1` | `0 V` |
| `CN3_3` | `0 V` |
| `CN3_4` | `0 V` |
| `CN3_5` | `0 V` |
| `CN3_6` | `0 V` |
| `CN3_13 / nFAULT` | `3.3 V` |
| `CN3_14 / 3V3` | `3.3 V` |
| `REG12` | `0 V` |
| Driver-input stop rule | not hit |

## Relationship To The Execution Entry

The execution entry
`stdrive101_manual_gate_test_24v_static_lockout_execution_entry_2026-06-20.md`
opened a possible bounded static pass based on freshly confirmed
preconditions. After that, the user correctly pointed out that the equivalent
USB + 24 V all-inputs-low static check had already been recorded.

This carry-forward result therefore closes the duplicate-measurement branch
without asking for the same static table again.

The practical decision is narrow:

```text
existing USB+24V static all-inputs-low evidence
+ USB-only reviewed lockout-image driver-input-low evidence
-> no repeated 24V static table needed before the next planning gate
```

This is not a powered-drive result and not PWM validation.

## Stop / Re-Measure Conditions

Do not repeat the 24 V static table unless one of these changes occurs:

- the lockout image changes or is rebuilt;
- wiring changes on CN3, HSPY, USB/ST-LINK, `VS / 24V_FUSED`, `REG12`,
  `nFAULT`, or any driver input;
- the motor is connected or the wake resistor / `LIN1` stimulus is reinstalled;
- Motor Pilot, Motor Profiler, normal MCSDK Run / Debug, PC13 start / stop, or
  MCP command ingress is opened;
- the board shows heat, smell, sound, unstable LEDs, reset looping, or a
  changed current draw;
- a later phase gate explicitly requires a fresh per-pin table.

If a repeat is ever required, it must be opened by a new dated entry and must
use the same hard stop rules: HSPY current limit, motor disconnected, no Gate
PWM, no Motor Pilot, no Motor Profiler, and rollback by HSPY output OFF first.

## Next Boundary

The next engineering checkpoint may move to a no-power phase-gate plan for
the next higher-risk step, such as gate-waveform / PWM-output planning.

That next checkpoint is still planning/review only unless a later dated
execution-entry explicitly opens a bounded measurement.

Still forbidden after this carry-forward result:

- Gate PWM output;
- Motor Pilot;
- Motor Profiler;
- motor connection;
- Hall closed loop;
- sensorless operation;
- power-stage readiness or motor readiness claims.
