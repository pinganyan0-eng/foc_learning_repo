# STDRIVE101 Gate-Waveform Isolated Source Package Review No-Power - 2026-06-21

## Summary

- Evidence ID:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-ISOLATED-SOURCE-PACKAGE-REVIEW-NO-POWER-001`.
- Task ID:
  `TASK-2026-06-21-stdrive101-gate-waveform-isolated-source-package-review-no-power`.
- Gate:
  Gate E1 from the gate-waveform / PWM-output no-power phase-gate ladder.
- Scope:
  no-power source-package review for a future isolated waveform image.
- Source package:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/manual_gate_waveform_source_package_2026-06-21/`.
- Hardware action:
  none in this record. No 24 V is applied by this review.
- Build or runtime action:
  none in this record. No object build, linked-image build, flash, Run /
  Debug, USB runtime execution, or Gate PWM output is performed or opened.
- Decision:
  `STDRIVE101 gate-waveform isolated source package review no-power / Gate E1
  source package created for review only / package has no CMakeLists and has a
  Gate E2 compile-acknowledgement #error guard / future isolated waveform
  image remains separate from normal generated MCSDK app and lockout image /
  candidate driver inputs fixed as PA8 PA9 PA10 PB13 PB14 PB15 / startup and
  shutdown force all six low / waveform constants frozen at 1 kHz, 100
  permille duty, 16 period window, 8 pre-idle periods, 32 post-idle periods,
  DTG 0x90 / TIM1 MOE CCER break AOE and dead-time policy visible in source /
  nFAULT stop path disables TIM1 outputs and forces all six low / source
  review only / no build / no flash / no Run Debug / no USB runtime / no
  24 V / no Gate PWM output / no Motor Pilot / no Motor Profiler / no motor
  connection / no powered-drive readiness`.

## Boundary

This record is Gate E1 source review only. It does not authorize:

- object-only build;
- linked-image build;
- HEX / BIN / ELF production;
- firmware flash;
- Run / Debug;
- USB runtime execution;
- applying 24 V;
- Gate PWM output;
- oscilloscope probing on live gate or phase nodes;
- normal generated MCSDK application execution;
- Motor Pilot;
- Motor Profiler;
- motor connection;
- Hall closed loop;
- sensorless operation;
- power-stage readiness or motor readiness claims.

The package intentionally has no `CMakeLists.txt`. The header also contains:

```c
#if !defined(GATE_WAVEFORM_CANDIDATE_GATE_E2_BUILD_ACK)
#error "Gate E1 source package only: open and record a dated Gate E2 build-only boundary before compiling."
#endif
```

That guard is part of the evidence boundary: this source package is readable
review evidence, not a build target.

## Files And Hashes

| File | SHA256 |
| --- | --- |
| `manual_gate_waveform_source_package_2026-06-21/README.md` | `76561ED11BC298AF8166326C143DB7207A23F7802AA8E469173BA9CCDC8C5FED` |
| `manual_gate_waveform_source_package_2026-06-21/Inc/gate_waveform_candidate.h` | `9C60AC9D81C5CF29E83C73E4A37947CB25A26D43FCABFF3C9B9E4B55B24068F8` |
| `manual_gate_waveform_source_package_2026-06-21/Src/gate_waveform_candidate.c` | `EF356C1507BDE3B34F6EB74A56AE45455635B947F59E5ED1AD4EB1099B1C2900` |
| `manual_gate_waveform_source_package_2026-06-21/Src/main_waveform_candidate.c` | `768787DAEEA90363943B43D514F4D394FB6F1B7DDED53AF8478303D54F8BF3C4` |

## Source Shape Reviewed

The package is intentionally separate from:

- the normal generated MCSDK app;
- the Gate D `stdrive101_gate_lockout_image`;
- Motor Pilot / Motor Profiler command paths.

Reviewed source properties:

| Area | Gate E1 source-review observation |
| --- | --- |
| Build gate | No `CMakeLists.txt`; header requires `GATE_WAVEFORM_CANDIDATE_GATE_E2_BUILD_ACK` before compilation. |
| Candidate pins | `PA8`, `PA9`, `PA10`, `PB13`, `PB14`, and `PB15` only. |
| Initial idle | `gate_waveform_candidate_force_idle_low()` enables GPIO/TIM1 clocks, locks TIM1 outputs, forces all six candidate pins low as GPIO outputs, and configures `PB12 / nFAULT` as input. |
| Candidate constants | `170 MHz` timer clock assumption, `1 MHz` timer tick, `1 kHz` PWM, `100` permille duty, `16` period candidate window, `8` pre-idle periods, `32` post-idle periods, and `DTG 0x90`. |
| TIM1 output policy | Source makes `MOE`, `CCER`, break enable, automatic-output clear, dead-time, and complementary-output enable visible for review. |
| Command ingress | `gate_waveform_candidate_get_config()` reports `command_ingress_present = false`; no start button, serial, MCP, ASPEP, Motor Pilot, or Motor Profiler path is present in this package. |
| Fault handling | `wait_for_pwm_periods_or_fault()` polls `nFAULT`; if it falls low, it latches the fault, disables TIM1 outputs, and forces all six pins low. |
| Shutdown idle | After the candidate window, source disables TIM1 outputs, forces pins low, waits the post-idle period with outputs disabled, and calls `gate_waveform_candidate_force_idle_low()` again. |
| Main loop | `main_waveform_candidate.c` calls the candidate once, then loops forever forcing idle-low state. |

## Static Screens

Forbidden normal-app and command-ingress screen:

```powershell
rg -n "MC_StartMotor1|MCI_START|PC13|MCP|ASPEP|Motor Pilot|Motor Profiler|R3_2_TurnOnLowSides|PWMC_SwitchOnPWM|LL_TIM_EnableAllOutputs|HALL_M1|PID_|STC_|HAL_Delay|printf|malloc|free" apps\stm32_g474_foc\mcsdk_no_power_precheck\manual_gate_waveform_source_package_2026-06-21
```

Result:

- no forbidden source matches in `Inc/` or `Src/`;
- the only text hit was README boundary language for `Motor Pilot` /
  `Motor Profiler`;
- no `MC_StartMotor1`, `MCI_START`, PC13, MCP, ASPEP,
  `R3_2_TurnOnLowSides`, `PWMC_SwitchOnPWM`,
  `LL_TIM_EnableAllOutputs`, Hall, PID, speed-loop, blocking delay, printf,
  or dynamic-allocation source path was found.

Build-gate screen:

```powershell
rg -n "GATE_WAVEFORM_CANDIDATE_GATE_E2_BUILD_ACK|#error|CMakeLists|add_executable|add_library" apps\stm32_g474_foc\mcsdk_no_power_precheck\manual_gate_waveform_source_package_2026-06-21
```

Result:

- README states the package intentionally has no `CMakeLists.txt`;
- header contains the `GATE_WAVEFORM_CANDIDATE_GATE_E2_BUILD_ACK` `#error`
  guard;
- no `add_executable` or `add_library` build target exists in the package.

## Remaining Review Risks

This record still does not prove:

- that the source compiles;
- that the TIM1 register constants are accepted by the target headers;
- that the linked image contains only the reviewed paths;
- that the candidate idles safely after reset on real hardware;
- that the waveform appears on any physical pin;
- that dead-time, polarity, break input, gate-driver behavior, or phase-node
  behavior is safe under 24 V;
- that a motor can be connected.

Those require later separate gates. Do not infer them from this source review.

## Next Allowed Checkpoint

The next allowed repository-side checkpoint is Gate E2 only:

```text
object-only and linked-image build-only boundary plan or build-only record
for the exact reviewed source package
```

Gate E2 must still be no-power and must explicitly record the source hashes,
build target boundary, object/ELF/MAP artifacts if built, forbidden source /
ELF / MAP screens, and the statement that no flash, Run / Debug, USB runtime
execution, 24 V, Gate PWM output, Motor Pilot, Motor Profiler, motor
connection, or readiness claim is opened.

Still forbidden after this Gate E1 record:

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
