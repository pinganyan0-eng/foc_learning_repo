# STDRIVE101 Gate-Waveform USB-Only Neutral-State Phase-Gate Plan - 2026-06-21

## Summary

- Evidence ID:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-USBONLY-NEUTRAL-STATE-PHASE-GATE-PLAN-001`.
- Task ID:
  `TASK-2026-06-21-stdrive101-gate-waveform-usbonly-neutral-state-phase-gate-plan`.
- Gate:
  Gate E3 from the gate-waveform / PWM-output no-power phase-gate ladder.
- Scope:
  phase-gate plan only for a future USB-only neutral-state check of the Gate
  E2 waveform candidate image.
- Candidate image boundary:
  `.tmp/manual_gate_waveform_build_only_2026-06-21_clean/stdrive101_gate_waveform_candidate_image.elf`.
- Hardware action:
  none in this record. No 24 V is applied by this plan.
- Firmware runtime action:
  none in this record. No flash, no Run / Debug, no USB runtime execution,
  and no Gate PWM output.
- Decision:
  `STDRIVE101 gate-waveform USB-only neutral-state phase-gate plan / Gate E3
  plan only / Gate E2 linked-image build-only record accepted as image-boundary
  evidence / candidate ELF and MAP hashes carried forward / current waveform
  candidate main calls gate_waveform_candidate_run_once once and then loops
  forcing idle low / DMM-only future check can prove only post-window steady
  idle and cannot prove absence of a reset-time or boot-time transient /
  later USB-only execution-entry must separately name flash or transfer
  method, exact image hash, measurement instrument, pre/post measurement
  table, rollback path, and stop rules / phase-gate plan only / no flash / no
  Run Debug / no USB runtime execution / no 24 V / no Gate PWM output / no
  Motor Pilot / no Motor Profiler / no motor connection / no powered-drive
  readiness`.

## Boundary

This record is planning only. It does not authorize:

- firmware flash;
- Run / Debug;
- USB runtime execution;
- applying 24 V;
- Gate PWM output on hardware;
- oscilloscope probing on live gate or phase nodes;
- normal generated MCSDK application execution;
- Motor Pilot;
- Motor Profiler;
- motor connection;
- Hall closed loop;
- sensorless operation;
- power-stage readiness or motor readiness claims.

The practical conclusion is narrow:

```text
Gate E2 proves a linkable waveform candidate image exists
-> Gate E3 may plan a later USB-only neutral-state check
-> this record does not run, flash, power, or validate the image
```

## Evidence Accepted For Planning

Gate E2 build-only record:

```text
apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_build_only_record_no_power_2026-06-21.md
```

Accepted build-only image boundary:

| Item | Carried-forward value |
| --- | --- |
| Source package | `manual_gate_waveform_source_package_2026-06-21/` |
| Build-only package | `manual_gate_waveform_build_only_2026-06-21/` |
| Object target | `stdrive101_gate_waveform_candidate_objects` |
| Linked target | `stdrive101_gate_waveform_candidate_image` |
| Clean ELF | `.tmp/manual_gate_waveform_build_only_2026-06-21_clean/stdrive101_gate_waveform_candidate_image.elf` |
| ELF SHA256 | `10BA818730E259AEBA8A5C5E5C96CFBA32FCB90AAA4136B775022B9D69ADCE7C` |
| Clean MAP | `.tmp/manual_gate_waveform_build_only_2026-06-21_clean/stdrive101_gate_waveform_candidate_image.map` |
| MAP SHA256 | `170EA77C566F98CF9EF2AC88F76B154238A5404DC705AAE3917BEAE7C1503D4C` |
| Size | `text=1852`, `data=0`, `bss=1544`, `dec=3396`, `hex=d44` |
| Forbidden screens | source/build, ELF-symbol, and MAP screens clean |

Gate E1 source behavior carried forward:

```text
apps/stm32_g474_foc/mcsdk_no_power_precheck/manual_gate_waveform_source_package_2026-06-21/Src/main_waveform_candidate.c
```

The current candidate `main()` performs:

```text
gate_waveform_candidate_run_once()
-> forever loop calling gate_waveform_candidate_force_idle_low()
```

This matters for Gate E3: the candidate is not a pure all-low lockout image.
A future DMM-only USB check can record only the steady post-window idle state
after the one-shot candidate has completed. It cannot prove that no short
reset-time or boot-time waveform occurred.
In short: future DMM-only USB check can record only steady post-window idle state; it cannot prove there was no reset-time or boot-time transient.

Prior lockout USB-only runtime result:

```text
apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_usb_only_runtime_lockout_result_2026-06-20.md
```

That result is useful only as earlier lockout-image evidence. It does not
prove this Gate E2 waveform candidate's runtime behavior.

## Future Gate E3 Execution Preconditions

Do not use this table to execute now. A later execution-entry must restate and
freshly confirm every row before any USB-only runtime action.

| Gate | Required before any later USB-only neutral-state execution |
| --- | --- |
| Explicit action request | User explicitly asks to execute the Gate E3 USB-only neutral-state check, not just to continue planning. |
| Image identity | Candidate image path and ELF SHA256 match the Gate E2 record exactly, or a replacement Gate E2 record exists. |
| Transfer method | A later execution-entry names the exact no-Run/Debug transfer method and any generated BIN hash. This plan creates no BIN and performs no flash. |
| HSPY / 24 V | HSPY output is `OFF` and physically disconnected from the board. |
| `VS / 24V_FUSED` | DMM confirms below `1 V` before USB runtime. |
| Motor state | Motor disconnected. |
| Wake stimulus | `10 kohm` wake resistor / `LIN1` stimulus removed. |
| Tools | Motor Pilot and Motor Profiler closed / unused. |
| Normal app ingress | `MC_StartMotor1`, `MCI_START`, PC13 start / stop, MCP / ASPEP command ingress, and normal generated MCSDK app run remain blocked. |
| Measurement method | Later execution-entry chooses DMM post-idle check only, or separately names a USB-only logic probe / scope capture on MCU-facing CN3 driver-input pins. |
| Probe boundary | No probing of live gate, phase, high-side, low-side, or 24 V nodes. |
| Stop authority | Operator keeps immediate access to USB disconnect and HSPY output OFF. |

## Future Measurement Table

Do not fill this table in this record.

A later Gate E3 execution-entry and result record may use this table only
after the preconditions above are freshly true:

| Measurement point | Future expected USB-only neutral-state result | Meaning limit |
| --- | --- | --- |
| `VS / 24V_FUSED` before USB runtime | below `1 V` | Confirms no 24 V path is active before USB-only action. |
| `CN3_1` driver input, steady post-idle | close to `0 V` | DMM proves only steady post-idle, not boot transient. |
| `CN3_2 / LIN1`, steady post-idle | close to `0 V` | DMM proves only steady post-idle, not boot transient. |
| `CN3_3` driver input, steady post-idle | close to `0 V` | DMM proves only steady post-idle, not boot transient. |
| `CN3_4` driver input, steady post-idle | close to `0 V` | DMM proves only steady post-idle, not boot transient. |
| `CN3_5` driver input, steady post-idle | close to `0 V` | DMM proves only steady post-idle, not boot transient. |
| `CN3_6` driver input, steady post-idle | close to `0 V` | DMM proves only steady post-idle, not boot transient. |
| `CN3_13 / nFAULT` | expected `3.3 V` if USB-only logic rail is present | Not a powered-drive readiness claim. |
| `CN3_14 / 3V3` | expected `3.3 V` if USB-only logic rail is present | Confirms logic rail only. |
| `REG12` | expected `0 V` with no 24 V | Any rise requires stop and record. |
| Board state | no abnormal heat, smell, or sound | Still not powered readiness. |

If a later Gate E3 check needs to prove "no transient", DMM is not enough.
The later execution-entry must name a USB-only logic-probe or scope method on
the MCU-facing CN3 driver-input pins only, with HSPY / 24 V still OFF and
disconnected.

## Stop Rules

In any later Gate E3 execution-entry or result, stop immediately if:

- image hash does not match the Gate E2 record;
- a BIN is needed but no separate hash is recorded;
- HSPY / 24 V is connected or not physically confirmed OFF;
- `VS / 24V_FUSED` is not below `1 V` before USB-only action;
- motor is connected;
- Motor Pilot or Motor Profiler is open;
- any `CN3_1` through `CN3_6` steady post-idle reading is above `0.3 V`
  when the check expects idle-low;
- `CN3_13 / nFAULT` falls low;
- `REG12` rises above `1 V` with no 24 V applied;
- any abnormal heat, smell, sound, or visible issue appears.

Stop means:

```text
disconnect USB if needed
keep HSPY OFF
do not retry
record the raw condition
return to repo-side review
```

Do not continue by trying one more time.

## Next Allowed Checkpoint

The next possible checkpoint after this Gate E3 plan is only one of:

- a separate Gate E3 USB-only neutral-state execution-entry record, after
  explicit user request and freshly confirmed preconditions; or
- a source-side neutral-wrapper review if the team decides the current
  `run_once()` image is not acceptable for a DMM-only neutral-state check.

This record does not open Gate E4. Gate E4 remains future-only scope / waveform
execution-entry work and still requires separate dated records, no motor,
fresh physical gates, and explicit user request.

Still forbidden after this Gate E3 plan:

- flash;
- Run / Debug;
- USB runtime execution;
- 24 V;
- Gate PWM output;
- oscilloscope probing on live gate or phase nodes;
- Motor Pilot / Profiler;
- motor connection;
- Hall closed loop;
- sensorless operation;
- power-stage readiness or motor readiness claims.
