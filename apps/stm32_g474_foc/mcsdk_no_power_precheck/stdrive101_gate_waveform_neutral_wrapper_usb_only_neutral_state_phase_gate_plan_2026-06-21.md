# STDRIVE101 Gate-Waveform Neutral-Wrapper USB-Only Neutral-State Phase-Gate Plan - 2026-06-21

## Summary

- Evidence ID:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-USBONLY-NEUTRAL-STATE-PHASE-GATE-PLAN-001`.
- Task ID:
  `TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-usbonly-neutral-state-phase-gate-plan`.
- Scope:
  phase-gate plan only for a future USB-only neutral-state check of the
  neutral-wrapper linked image.
- Accepted build-only record:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_neutral_wrapper_build_only_record_no_power_2026-06-21.md`.
- Candidate image boundary:
  `.tmp/gwnw_build_2026-06-21_clean/stdrive101_gate_waveform_neutral_wrapper_image.elf`.
- Hardware action:
  none in this record. No 24 V is applied by this plan.
- Firmware runtime action:
  none in this record. No flash, no Run / Debug, no USB runtime execution,
  and no Gate PWM output.
- Decision:
  `STDRIVE101 gate-waveform neutral-wrapper USB-only neutral-state phase-gate
  plan / plan only / neutral-wrapper build-only record accepted as
  image-boundary evidence / neutral-wrapper ELF and MAP hashes carried forward
  / source-review packages remain source-review only and have no CMakeLists /
  build-only image uses main_neutral_wrapper.c and excludes old
  main_waveform_candidate.c / retained ELF symbol table has
  gate_waveform_neutral_wrapper_hold_idle_forever and has no
  gate_waveform_candidate_run_once / MAP lists gate_waveform_candidate_run_once
  only as a discarded zero-address input section from gate_waveform_candidate.c
  / future USB-only execution-entry must separately name transfer method,
  exact image hash, optional BIN hash if generated, measurement instrument,
  pre/post measurement table, rollback path, and stop rules / phase-gate plan
  only / no flash / no Run Debug / no USB runtime execution / no 24 V / no
  Gate PWM output / no Motor Pilot / no Motor Profiler / no motor connection /
  no powered-drive readiness`.

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

The practical boundary is narrow:

```text
neutral-wrapper source review exists
-> neutral-wrapper linked ELF / MAP build-only evidence exists
-> a future USB-only neutral-state execution-entry may be planned separately
-> this record does not run, flash, power, or validate the image
```

## Evidence Accepted For Planning

Neutral-wrapper build-only record:

```text
apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_neutral_wrapper_build_only_record_no_power_2026-06-21.md
```

Accepted image boundary:

| Item | Carried-forward value |
| --- | --- |
| Source package | `manual_gate_waveform_source_package_2026-06-21/` |
| Wrapper source package | `manual_gate_waveform_neutral_wrapper_source_package_2026-06-21/` |
| Build-only package | `manual_gate_waveform_neutral_wrapper_build_only_2026-06-21/` |
| Object target | `stdrive101_gate_waveform_neutral_wrapper_objects` |
| Linked target | `stdrive101_gate_waveform_neutral_wrapper_image` |
| Clean ELF | `.tmp/gwnw_build_2026-06-21_clean/stdrive101_gate_waveform_neutral_wrapper_image.elf` |
| ELF SHA256 | `C47C02D379DC5312095DF786BF8C99B58D42323AD9227D0903BCB8C98AAD9591` |
| Clean MAP | `.tmp/gwnw_build_2026-06-21_clean/stdrive101_gate_waveform_neutral_wrapper_image.map` |
| MAP SHA256 | `5FB24B2735EFFD402C26BDC3B0D267B26B06DC6522A6B5B5D876491BA9A42A83` |
| Size | `text=1044`, `data=0`, `bss=1536`, `dec=2580`, `hex=a14` |
| Memory | RAM `1536 B / 128 KB / 1.17%`, FLASH `1044 B / 512 KB / 0.20%` |
| HEX / BIN | none in the build-only record |

Build-only source boundary carried forward:

- the source-review packages still have no `CMakeLists.txt`;
- only the build-only package defines
  `GATE_WAVEFORM_CANDIDATE_GATE_E2_BUILD_ACK` and
  `GATE_WAVEFORM_NEUTRAL_WRAPPER_BUILD_ACK`;
- the build inputs include reviewed `gate_waveform_candidate.c` and wrapper
  `main_neutral_wrapper.c`;
- old `main_waveform_candidate.c` is excluded from the build-only
  `CMakeLists.txt` and from `build.ninja`;
- the retained ELF symbol table has
  `gate_waveform_neutral_wrapper_hold_idle_forever`;
- the retained ELF symbol table has no `gate_waveform_candidate_run_once` and
  no `main_waveform_candidate`;
- the MAP lists `.text.gate_waveform_candidate_run_once` only in the
  discarded input-section area at `0x00000000`, expected with
  `-ffunction-sections` and `--gc-sections`.

This is enough to plan a later USB-only neutral-state check. It is not enough
to flash or execute runtime.

## Meaning Of The Neutral Wrapper

The neutral wrapper narrows the source-side entry path to:

```text
main()
-> gate_waveform_neutral_wrapper_hold_idle_forever()
-> gate_waveform_candidate_force_idle_low()
-> forever loop calling gate_waveform_candidate_force_idle_low()
```

The wrapper image is better suited than the earlier Gate E2 `run_once()` image
for a future DMM-only neutral-state check because the retained ELF does not
include a deliberate `gate_waveform_candidate_run_once()` call.

The remaining DMM limitation still matters:

```text
DMM can show steady neutral state after firmware reaches the wrapper loop
-> DMM cannot prove reset-time pin state before firmware control
-> DMM cannot prove absence of a very short transient on real hardware
```

Any future claim about reset-time or sub-millisecond transient behavior needs a
separate USB-only logic-probe or scope plan on MCU-facing CN3 driver-input
pins only, with HSPY / 24 V still OFF and disconnected.

## Future Execution-Entry Preconditions

Do not use this table to execute now. A later execution-entry must restate and
freshly confirm every row before any USB-only runtime action.

| Gate | Required before any later USB-only neutral-wrapper neutral-state execution |
| --- | --- |
| Explicit action request | User explicitly asks to execute the neutral-wrapper USB-only neutral-state check, not just to continue planning. |
| Image identity | Candidate image path and ELF SHA256 match the build-only record exactly, or a replacement build-only record exists. |
| Transfer method | A later execution-entry names the exact no-Run/Debug transfer method and any generated BIN hash. This plan creates no BIN and performs no flash. |
| HSPY / 24 V | HSPY output is `OFF` and physically disconnected from the board. |
| `VS / 24V_FUSED` | DMM confirms below `1 V` before USB runtime. |
| Motor state | Motor disconnected. |
| Wake stimulus | `10 kohm` wake resistor / `LIN1` stimulus removed. |
| Tools | Motor Pilot and Motor Profiler closed / unused. |
| Normal app ingress | `MC_StartMotor1`, `MCI_START`, PC13 start / stop, MCP / ASPEP command ingress, and normal generated MCSDK app run remain blocked. |
| Measurement method | Later execution-entry chooses DMM steady neutral-state check only, or separately names a USB-only logic probe / scope capture on MCU-facing CN3 driver-input pins. |
| Probe boundary | No probing of live gate, phase, high-side, low-side, or 24 V nodes. |
| Stop authority | Operator keeps immediate access to USB disconnect and HSPY output OFF. |

If any gate is missing, the later task must stay at planning or source/build
review and must not execute runtime.

## Future Measurement Table

Do not fill this table in this record.

A later execution-entry and result record may use this table only after the
preconditions above are freshly true:

| Measurement point | Future expected USB-only neutral-state result | Meaning limit |
| --- | --- | --- |
| `VS / 24V_FUSED` before USB runtime | below `1 V` | Confirms no 24 V path is active before USB-only action. |
| `CN3_1` driver input, steady state | close to `0 V` | DMM proves only steady firmware-controlled neutral state. |
| `CN3_2 / LIN1`, steady state | close to `0 V` | DMM proves only steady firmware-controlled neutral state. |
| `CN3_3` driver input, steady state | close to `0 V` | DMM proves only steady firmware-controlled neutral state. |
| `CN3_4` driver input, steady state | close to `0 V` | DMM proves only steady firmware-controlled neutral state. |
| `CN3_5` driver input, steady state | close to `0 V` | DMM proves only steady firmware-controlled neutral state. |
| `CN3_6` driver input, steady state | close to `0 V` | DMM proves only steady firmware-controlled neutral state. |
| `CN3_13 / nFAULT` | expected `3.3 V` if USB-only logic rail is present | Not a powered-drive readiness claim. |
| `CN3_14 / 3V3` | expected `3.3 V` if USB-only logic rail is present | Confirms logic rail only. |
| `REG12` | expected `0 V` with no 24 V | Any rise requires stop and record. |
| Board state | no abnormal heat, smell, or sound | Still not powered readiness. |

## Stop Rules

In any later execution-entry or result, stop immediately if:

- image hash does not match the neutral-wrapper build-only record;
- a BIN is needed but no separate hash is recorded;
- HSPY / 24 V is connected or not physically confirmed OFF;
- `VS / 24V_FUSED` is not below `1 V` before USB-only action;
- motor is connected;
- Motor Pilot or Motor Profiler is open;
- any `CN3_1` through `CN3_6` steady-state reading is above `0.3 V`
  when the check expects neutral low;
- `CN3_13 / nFAULT` falls low;
- `REG12` rises above `1 V` with no 24 V applied;
- any abnormal heat, smell, sound, reset loop, or visible issue appears.

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

The next possible checkpoint after this plan is only a separate
neutral-wrapper USB-only neutral-state execution-entry record after explicit
user request and freshly confirmed preconditions.

This record does not open Gate E4 and does not open hardware waveform work.
Gate E4 remains future-only scope / waveform execution-entry work and still
requires separate dated records, no motor, fresh physical gates, and explicit
user request.

Still forbidden after this neutral-wrapper USB-only neutral-state plan:

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
