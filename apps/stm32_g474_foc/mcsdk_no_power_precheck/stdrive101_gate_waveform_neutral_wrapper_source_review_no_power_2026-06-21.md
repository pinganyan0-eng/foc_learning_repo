# STDRIVE101 Gate-Waveform Neutral-Wrapper Source Review No-Power - 2026-06-21

## Summary

- Evidence ID:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-SOURCE-REVIEW-NO-POWER-001`.
- Task ID:
  `TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-source-review-no-power`.
- Scope:
  source-side neutral-wrapper review only after the Gate E3 USB-only
  neutral-state phase-gate plan.
- Source package:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/manual_gate_waveform_neutral_wrapper_source_package_2026-06-21/`.
- Related source carried forward:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/manual_gate_waveform_source_package_2026-06-21/`.
- Hardware action:
  none in this record. No 24 V is applied by this review.
- Build or runtime action:
  none in this record. No object build, linked-image build, flash, Run /
  Debug, USB runtime execution, or Gate PWM output is performed or opened.
- Decision:
  `STDRIVE101 gate-waveform neutral-wrapper source review no-power /
  source-side wrapper package created for review only / package has no
  CMakeLists and has GATE_WAVEFORM_NEUTRAL_WRAPPER_BUILD_ACK #error guard /
  wrapper replaces future candidate entry point only / wrapper calls
  gate_waveform_candidate_force_idle_low before the forever loop and inside
  the forever loop / wrapper source contains no gate_waveform_candidate_run_once
  call / no TIM1 waveform-window or output-enable path in wrapper source /
  current Gate E2 run_once image remains unsuitable for proving no boot
  transient with DMM-only evidence / source review only / no build / no flash /
  no Run Debug / no USB runtime execution / no 24 V / no Gate PWM output / no
  Motor Pilot / no Motor Profiler / no motor connection / no powered-drive
  readiness`.

## Boundary

This record is source-review evidence only. It does not authorize:

- object-only build;
- linked-image build;
- HEX / BIN / ELF / MAP production;
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

No object file, ELF, MAP, HEX, or BIN is produced by this package.

The neutral-wrapper package intentionally has no `CMakeLists.txt`. The header
contains:

```c
#if !defined(GATE_WAVEFORM_NEUTRAL_WRAPPER_BUILD_ACK)
#error "Neutral-wrapper source package only: open and record a dated build-only boundary before compiling."
#endif
```

That guard is part of the evidence boundary. The package is readable source
review evidence, not a build target.
The package is readable source review evidence, not a build target.

## Why This Wrapper Exists

The Gate E3 plan records a limitation in the Gate E2 linked image:

```text
main()
-> gate_waveform_candidate_run_once()
-> forever loop calling gate_waveform_candidate_force_idle_low()
```

That image can support a future post-window steady-state DMM check, but it
cannot prove absence of a reset-time or boot-time transient with DMM-only
evidence.

The neutral wrapper narrows a future candidate image to:

```text
main()
-> gate_waveform_neutral_wrapper_hold_idle_forever()
-> gate_waveform_candidate_force_idle_low()
-> forever loop calling gate_waveform_candidate_force_idle_low()
```

This source review does not prove runtime behavior. It only proves the wrapper
entry source has no deliberate waveform-window call.

## Files And Hashes

| File | SHA256 |
| --- | --- |
| `manual_gate_waveform_neutral_wrapper_source_package_2026-06-21/README.md` | `AE04E5D1FE022F0B730F968E1CD82131A37CA6DC75E66EC9B51C87F26450C25D` |
| `manual_gate_waveform_neutral_wrapper_source_package_2026-06-21/Inc/gate_waveform_neutral_wrapper.h` | `4E541FF0E4D64AAA8CADFA3182A257843C94B10A7F2EA4E954A55346751B363B` |
| `manual_gate_waveform_neutral_wrapper_source_package_2026-06-21/Src/main_neutral_wrapper.c` | `265587CDBE9CB63E2A95D5D06C4F7BBEEE967BDAECE88383782C794DF9A76310` |

## Source Shape Reviewed

| Area | Neutral-wrapper source-review observation |
| --- | --- |
| Build gate | No `CMakeLists.txt`; header requires `GATE_WAVEFORM_NEUTRAL_WRAPPER_BUILD_ACK` before compilation. |
| Entry point | `main_neutral_wrapper.c` defines `main()` and calls `gate_waveform_neutral_wrapper_hold_idle_forever()`. |
| Idle function | `gate_waveform_neutral_wrapper_hold_idle_forever()` calls `gate_waveform_candidate_force_idle_low()` once before the loop and then forever inside the loop. |
| Waveform window | Wrapper source has no `gate_waveform_candidate_run_once()` call and no TIM1 waveform-window helper. |
| Future link requirement | A future build-only package must include reviewed `gate_waveform_candidate.c`, exclude old `main_waveform_candidate.c`, and use this wrapper `main_neutral_wrapper.c` as the only entry point. |
| Command ingress | No normal generated MCSDK app, PC13 start / stop, MCP / ASPEP, Motor Pilot, or Motor Profiler path is present in the wrapper `Inc/` or `Src/`. |

## Static Screens

Forbidden wrapper source screen:

```powershell
rg -n "gate_waveform_candidate_run_once|configure_tim1_for_candidate_window|arm_candidate_outputs|TIM_BDTR_MOE|TIM_CCER|MC_StartMotor1|MCI_START|PC13|MCP|ASPEP|Motor Pilot|Motor Profiler|R3_2_TurnOnLowSides|PWMC_SwitchOnPWM|LL_TIM_EnableAllOutputs|HALL_M1|PID_|STC_|HAL_Delay|printf|malloc|free" apps\stm32_g474_foc\mcsdk_no_power_precheck\manual_gate_waveform_neutral_wrapper_source_package_2026-06-21\Inc apps\stm32_g474_foc\mcsdk_no_power_precheck\manual_gate_waveform_neutral_wrapper_source_package_2026-06-21\Src
```

Result:

- no forbidden source matches in wrapper `Inc/` or `Src/`;
- no `gate_waveform_candidate_run_once()` call appears in wrapper source;
- no TIM1 waveform-window or TIM1 output-enable helper appears in wrapper
  source;
- no `MC_StartMotor1`, `MCI_START`, PC13, MCP, ASPEP,
  `R3_2_TurnOnLowSides`, `PWMC_SwitchOnPWM`,
  `LL_TIM_EnableAllOutputs`, Hall, PID, speed-loop, blocking delay, printf,
  or dynamic-allocation source path was found in wrapper `Inc/` or `Src/`.

Build-gate screen:

```powershell
rg -n "GATE_WAVEFORM_NEUTRAL_WRAPPER_BUILD_ACK|#error|CMakeLists|add_executable|add_library" apps\stm32_g474_foc\mcsdk_no_power_precheck\manual_gate_waveform_neutral_wrapper_source_package_2026-06-21
```

Result:

- README states the package intentionally has no `CMakeLists.txt`;
- header contains the `GATE_WAVEFORM_NEUTRAL_WRAPPER_BUILD_ACK` `#error`
  guard;
- no `add_executable` or `add_library` build target exists in the package.

## Remaining Review Risks

This record still does not prove:

- that the wrapper compiles;
- that a linked neutral-wrapper image exists;
- that the future link excludes the old `main_waveform_candidate.c`;
- reset-time or runtime pin behavior on real hardware;
- that all six candidate driver-input pins are low after reset;
- that USB-only DMM readings will be idle-low;
- that any 24 V or Gate PWM action is acceptable;
- that Motor Pilot, Motor Profiler, or a motor can be used.

Those require later separate gates and direct evidence. Do not infer them from
this source review.

## Next Allowed Checkpoint

The next allowed repository-side checkpoint is only:

```text
neutral-wrapper build-only boundary plan or build-only record
```

That future checkpoint must be separate and dated. It must still produce only
build evidence unless a later separate execution-entry explicitly opens a
runtime action. It must name the exact source inputs, prove the old
`main_waveform_candidate.c` is excluded, record object / ELF / MAP artifacts
if built, and repeat forbidden source / ELF / MAP screens.

Still forbidden after this neutral-wrapper source review:

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
