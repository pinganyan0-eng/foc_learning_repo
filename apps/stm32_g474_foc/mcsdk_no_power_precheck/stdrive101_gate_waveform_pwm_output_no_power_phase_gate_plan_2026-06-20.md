# STDRIVE101 Gate-Waveform / PWM-Output No-Power Phase-Gate Plan - 2026-06-20

## Summary

- Evidence ID:
  `EV-2026-06-20-STDRIVE101-GATE-WAVEFORM-PWM-OUTPUT-NO-POWER-PHASE-GATE-PLAN-001`.
- Task ID:
  `TASK-2026-06-20-stdrive101-gate-waveform-pwm-output-no-power-phase-gate-plan`.
- Scope:
  no-power phase-gate plan for the next higher-risk gate-waveform /
  PWM-output branch after the manual gate-test 24V static lockout
  carry-forward result.
- Hardware action:
  none in this record. No 24 V is applied by this plan.
- Firmware runtime action:
  none in this record. No flash, no Run / Debug, no USB runtime execution,
  and no Gate PWM output.
- Decision:
  `STDRIVE101 gate-waveform PWM-output no-power phase-gate plan / 24V static
  lockout carry-forward result accepted as static boundary evidence /
  linked lockout image and USB-only runtime lockout result carried forward as
  driver-input-low evidence / normal generated MCSDK PWM path remains blocked /
  future gate-waveform execution gates, instrumentation requirements,
  rollback path, and stop rules named as future-only items / phase-gate plan
  only / no flash / no Run Debug / no 24 V / no Gate PWM output / no Motor
  Pilot / no Motor Profiler / no motor connection / no powered-drive
  readiness`.

## Boundary

This record is planning only. It does not authorize:

- firmware flash;
- Run / Debug;
- USB runtime execution;
- applying 24 V;
- Gate PWM output;
- oscilloscope probing on live gate or phase nodes;
- normal generated MCSDK application execution;
- `MC_StartMotor1`, `MCI_START`, PC13 start / stop, MCP command ingress,
  `R3_2_TurnOnLowSides`, `PWMC_SwitchOnPWM`, or
  `LL_TIM_EnableAllOutputs` from the normal generated path;
- Motor Pilot;
- Motor Profiler;
- motor connection;
- Hall closed loop;
- sensorless operation;
- power-stage readiness or motor readiness claims.

The practical conclusion is narrow:

```text
static all-inputs-low evidence
+ reviewed USB-only lockout runtime evidence
-> next work may define a future gate-waveform phase-gate ladder
-> no waveform or PWM execution is opened by this record
```

## Evidence Accepted For Planning

Latest 24 V static lockout carry-forward result:

```text
apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_24v_static_lockout_carry_forward_result_2026-06-20.md
```

Accepted static boundary:

| Item | Carried-forward value |
| --- | --- |
| USB + 24 V static source | `stdrive101_usb24_static_recheck_result_2026-06-20.md` |
| HSPY state | `CV` |
| HSPY current | about `0.045 A` |
| `CN3_1` through `CN3_6` | all close to `0 V` |
| `CN3_13 / nFAULT` | `3.3 V` |
| `CN3_14 / 3V3` | `3.3 V` |
| `REG12` | `0.3 V` |
| User correction | no repeated 24 V static table is needed unless image, wiring, board condition, or tool state changes |

Accepted USB-only lockout evidence:

| Item | Carried-forward value |
| --- | --- |
| ELF SHA256 | `87BF3F7A28949F8DB654927292083609E52AB46C511CB6191D03B280DBFFE9B6` |
| BIN SHA256 | `CBF833C8E9289D8B4A952C32C641CAA94928F1F8119C5DC528EBD779915EA6BE` |
| `CN3_1` through `CN3_6` | all `0 V` |
| `CN3_13 / nFAULT` | `3.3 V` |
| `CN3_14 / 3V3` | `3.3 V` |
| `REG12` | `0 V` |
| Driver-input stop rule | not hit |

Accepted linked-image boundary evidence:

```text
apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_linked_image_build_only_record_2026-06-20.md
```

That record proves only that the isolated lockout image is linkable and
reviewable. It does not prove that any PWM-output or gate-waveform image is
safe or ready.

Accepted source-risk evidence:

```text
apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_pwm_gate_test_no_power_source_review_2026-06-20.md
apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_r3_2_mcsdk_pwm_output_path_source_closure_2026-06-20.md
```

Those records keep the normal generated MCSDK start path blocked for powered
PWM. A future waveform branch must not start from normal generated
`MC_StartMotor1()` / `MCI_START`.

## Future Phase-Gate Ladder

The next branch must progress in separate dated records. This plan names the
ladder only; it does not execute any rung.

| Future gate | Future evidence required | Opened by this record |
| --- | --- | --- |
| Gate E0 | no-power waveform-image design plan that defines the exact intended pin pattern, duty, timing, dead-time assumptions, disabled command ingress, and rollback path | no |
| Gate E1 | isolated waveform source package, separate from the all-low lockout image and separate from normal MCSDK start | no |
| Gate E2 | object-only and linked-image build-only record for the waveform candidate, with source / ELF / MAP forbidden-symbol screens | no |
| Gate E3 | USB-only runtime neutral-state check for the waveform candidate before any 24 V, proving reset / idle still keeps `CN3_1` through `CN3_6` safe | no |
| Gate E4 | future scope-only, no-motor gate-waveform execution-entry, with explicit user request and fresh physical gates | no |
| Gate E5 | future gate-waveform result record with raw scope / DMM evidence and stop-rule outcome | no |

Do not skip from this plan to Gate E4. The next allowed engineering action is
Gate E0 planning, or source/build review that remains no-power.

## Minimum Requirements For Any Future Waveform Candidate

A later waveform candidate must be rejected before build or execution if it
does not satisfy all of these design constraints:

- no normal generated MCSDK start path;
- no Motor Pilot / Profiler ingress;
- no PC13 start / stop ingress;
- no MCP / ASPEP command ingress;
- no motor connection;
- explicit idle state that forces `PA8`, `PA9`, `PA10`, `PB13`, `PB14`, and
  `PB15` low before and after the candidate window;
- explicit TIM1 `MOE`, `CCER`, break, automatic-output, and dead-time policy;
- explicit candidate waveform pattern, frequency, duty, duration, and repeat
  count;
- explicit proof that high-side / low-side complementary overlap is blocked
  by design, not by hope;
- explicit nFAULT handling and stop path;
- explicit "HSPY output OFF first" rollback.

If any item is missing, stay in no-power source/build review.

## Candidate Future Execution Preconditions

Do not use this table to execute now. A later execution-entry must restate and
freshly confirm every row before any powered or waveform action.

| Gate | Required before any later waveform execution |
| --- | --- |
| Explicit action request | User explicitly asks to execute the named gate-waveform check, not just to continue planning. |
| Prior records | Gate E0 through Gate E3 records exist and are still valid for the exact image. |
| Image hash | ELF and BIN hashes are recorded for the waveform candidate; the image is not the normal generated MCSDK app. |
| HSPY initial state | HSPY output is `OFF` before wiring, scope connection, or probing. |
| `VS / 24V_FUSED` before any change | DMM confirms below `1 V`. |
| Motor state | Motor disconnected. |
| Wake stimulus | `10 kohm` wake resistor / `LIN1` stimulus removed. |
| Tools | Motor Pilot and Motor Profiler closed / unused. |
| Normal app ingress | `MC_StartMotor1`, `MCI_START`, PC13 start / stop, MCP command ingress, and normal generated MCSDK app run remain blocked. |
| Instrumentation | Scope reference, probe type, node names, bandwidth / attenuation, and ground safety are named before power. |
| Current limit | HSPY current limit and abort threshold are named in the later execution-entry. |
| Stop authority | Operator keeps immediate access to HSPY output OFF and USB disconnect. |
| Closeout | Later record must end with HSPY output `OFF` and `VS / 24V_FUSED < 1 V` before any wiring change. |

## Future Stop Rules

A later waveform execution-entry must stop immediately, turn HSPY output OFF,
and return to no-power review if any of these occur:

- the actual image hash does not match the approved future waveform record;
- motor is connected or can move;
- Motor Pilot, Motor Profiler, PC13 start / stop, or MCP command ingress is
  open;
- `CN3_13 / nFAULT` falls low or is unstable before the planned waveform
  window;
- any driver input is high outside the explicitly planned candidate window;
- HSPY enters `CC`, current rises unexpectedly, or the later entry's abort
  threshold is crossed;
- scope reference, probe ground, or measurement point is uncertain;
- high-side / low-side overlap, missing dead-time, abnormal gate ringing, or
  unexpected phase-node behavior is observed;
- board heats, smells, makes sound, resets repeatedly, or LEDs behave
  unexpectedly;
- any instruction path asks to continue by retrying after a stop-rule event.

Do not continue by trying one more time after a stop-rule event. Record the raw
observation and return to no-power source/build review.

## Decision For Progress

The next engineering checkpoint is not motor power and not Gate PWM output.
It is Gate E0 only: a separate no-power waveform-image design plan, or a
source/build review that keeps all execution actions closed.

Still forbidden after this plan:

- flash;
- Run / Debug;
- 24 V;
- Gate PWM output;
- Motor Pilot / Profiler;
- motor connection;
- Hall closed loop;
- sensorless operation;
- power-stage readiness or motor readiness claims.
