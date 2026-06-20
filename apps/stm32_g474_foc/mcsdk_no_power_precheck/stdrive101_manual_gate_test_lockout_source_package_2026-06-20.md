# STDRIVE101 Manual Gate-Test Lockout Source Package - 2026-06-20

## Summary

- Evidence ID:
  `EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-LOCKOUT-SOURCE-PACKAGE-NO-POWER-001`.
- Task ID:
  `TASK-2026-06-20-stdrive101-manual-gate-test-lockout-source-package-no-power`.
- Scope:
  Gate B no-power source-package implementation and static lockout review.
- Hardware action:
  none.
- Firmware runtime action:
  none; no flash, no Run / Debug, no 24 V runtime.
- Decision:
  `STDRIVE101 manual gate-test lockout source package no-power / repo-local
  isolated lockout source added / six driver input pins forced GPIO low /
  PB12 nFAULT kept as input / TIM1 CCER cleared / TIM1 MOE and automatic
  output cleared / TIM1 break left enabled / forbidden normal MCSDK start and
  command ingress symbols absent from lockout Src and Inc / source package only
  / no embedded build target yet / no flash / no runtime / no PWM-output
  validation / no powered-drive readiness`.

## Boundary

This record is still no-power evidence only. It does not authorize:

- firmware flash;
- Run / Debug;
- 24 V powered runtime;
- Gate PWM output;
- oscilloscope gate probing;
- Motor Pilot;
- Motor Profiler;
- motor connection;
- Hall closed loop;
- sensorless operation;
- power-stage readiness or motor readiness.

## Added Source Package

Directory:

```text
apps/stm32_g474_foc/mcsdk_no_power_precheck/manual_gate_test_lockout_build_only_2026-06-20/
```

Files:

| File | Purpose |
| --- | --- |
| `README.md` | Package boundary and use limits. |
| `Inc/gate_test_lockout.h` | Public state and API for lockout polling. |
| `Src/gate_test_lockout.c` | GPIO low-state lock, `PB12 / nFAULT` input readback, TIM1 output lock. |
| `Src/main_lockout.c` | Minimal foreground loop that repeatedly reapplies the lockout state. |

The package is intentionally separate from:

- the archived Packet A generated-source snapshot;
- the external Workbench project under `.st_workbench`;
- the normal generated MCSDK start path.

## Implemented Lockout Shape

The source package explicitly implements these no-power-review requirements:

| Requirement | Evidence in package |
| --- | --- |
| `PA8` low | `configure_pin_as_output_low(GPIOA, 8u)` |
| `PA9` low | `configure_pin_as_output_low(GPIOA, 9u)` |
| `PA10` low | `configure_pin_as_output_low(GPIOA, 10u)` |
| `PB13` low | `configure_pin_as_output_low(GPIOB, 13u)` |
| `PB14` low | `configure_pin_as_output_low(GPIOB, 14u)` |
| `PB15` low | `configure_pin_as_output_low(GPIOB, 15u)` |
| `PB12 / nFAULT` input only | `configure_pin_as_input(GPIOB, GATE_TEST_NFAULT_PIN)` |
| TIM1 channel outputs disabled | `TIM1->CCER = 0u` |
| TIM1 main output disabled | `TIM1->BDTR` clears `TIM_BDTR_MOE` |
| TIM1 automatic output disabled | `TIM1->BDTR` clears `TIM_BDTR_AOE` |
| TIM1 break retained | `TIM1->BDTR` sets `TIM_BDTR_BKE` |
| Foreground lock maintenance | `main_lockout.c` repeatedly calls `gate_test_lockout_poll()` |

The source does not configure the six driver pins to TIM1 alternate function.
It keeps them as GPIO outputs low for the first lockout image.

## Static Forbidden-Symbol Check

Command run from repo root:

```powershell
rg -n "MC_StartMotor1|MCI_StartMotor|MCI_START|MX_MotorControl_Init|MCboot|UI_HandleStartStopButton_cb|MX_USART2_UART_Init|ASPEP|MCP|LL_TIM_DisableBRK|R3_2_TurnOnLowSides|PWMC_SwitchOnPWM|LL_TIM_EnableAllOutputs" apps\stm32_g474_foc\mcsdk_no_power_precheck\manual_gate_test_lockout_build_only_2026-06-20\Src apps\stm32_g474_foc\mcsdk_no_power_precheck\manual_gate_test_lockout_build_only_2026-06-20\Inc
```

Result:

```text
exit code 1
no matches
```

Interpretation:

- No forbidden normal MCSDK start, command-ingress, or TIM1 output-enable
  symbols were found in the lockout package `Src` or `Inc`.
- This is a static source check only.

## Build / Target Status

No embedded object build was completed for this lockout source package in this
record.

A later record added a repo-local object-only CMake target:

```text
stdrive101_manual_gate_test_lockout_object_target_2026-06-20.md
```

That target intentionally compiles only object files and does not link an ELF,
HEX, or BIN image. Its first configure attempt was blocked by sandboxed access
to external Ninja, and the escalation path returned 503 from the automatic
approval service. No object build pass is claimed yet.

Original reason this source-package record did not claim a build:

- the repo-local Packet A source snapshot is evidence and must not be edited;
- the external Workbench project is outside the repo evidence path;
- at the time of this source-package record, the lockout package did not yet
  have a separate repo-local embedded build target with CMSIS include paths.

A smaller object-only syntax compile was attempted with the local STM32Cube
`arm-none-eabi-gcc.exe`, but execution of the external compiler was blocked by
the sandbox and the escalation request was rejected because the workspace was
out of credits. No compiler output, object-file evidence, link result, or
embedded build pass is claimed.

Therefore the current upgraded statement is only:

```text
The repo now contains an isolated STDRIVE101 manual lockout source package
whose source statically avoids the blocked normal MCSDK start/output paths.
```

It does not prove:

- the package compiles in the embedded toolchain;
- the image can be flashed;
- MCU pins are physically low at runtime;
- `REG12` behavior under a lockout image;
- gate waveform behavior;
- motor-control behavior;
- power-stage or motor readiness.

## Next Allowed Checkpoint

The next no-power checkpoint is a build-target integration decision:

1. create a separate repo-local build target for the lockout package, or
2. explicitly copy this package into a separate external Workbench clone and
   record the source hashes before a compile-only build.

Still forbidden at that checkpoint:

- flash;
- Run / Debug;
- 24 V;
- Gate PWM output;
- Motor Pilot / Profiler;
- motor connection.
