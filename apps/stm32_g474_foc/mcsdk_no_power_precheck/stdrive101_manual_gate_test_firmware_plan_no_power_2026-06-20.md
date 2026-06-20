# STDRIVE101 Manual Gate-Test Firmware Plan - No-Power Only - 2026-06-20

## Summary

- Evidence ID:
  `EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-FIRMWARE-PLAN-NO-POWER-001`.
- Task ID:
  `TASK-2026-06-20-stdrive101-manual-gate-test-firmware-plan-no-power`.
- Scope:
  no-power-only plan for a future isolated manual gate-test firmware path.
- Hardware action:
  none.
- Firmware action:
  no implementation, no edit to generated firmware, no flash, no Run / Debug.
- Decision:
  `STDRIVE101 manual gate-test firmware plan no-power / normal MCSDK start path
  remains blocked / future gate-test must use an isolated lockout firmware path
  that avoids MC_StartMotor1, MCI_START, PC13 start-stop, MCP command ingress,
  Motor Pilot, Hall closed-loop paths, speed-loop paths, and motor connection /
  plan only / no PWM-output validation / no powered-drive readiness`.

## Boundary

This document is a plan only. It does not authorize:

- motor connection;
- Gate PWM output;
- firmware Flash / Run / Debug;
- Motor Pilot;
- Motor Profiler;
- Hall closed-loop or sensorless operation;
- powered-drive readiness, power-stage readiness, or motor readiness.

The next executable step, if later opened, must be a no-power build-only
implementation review. Any flash, runtime, 24 V, or gate-output observation
requires a separate dated phase-gate record.

## Why Normal MCSDK Start Is Not The First Gate-Test Path

The current source evidence says:

- `stdrive101_r3_2_mcsdk_pwm_output_path_source_closure_2026-06-20.md`
  identified the exact local Workbench MCSDK
  `r3_2_g4xx_pwm_curr_fdbk.c` source and hash.
- `R3_2_TurnOnLowSides()` treats `ticks = 0` as low-sides ON.
- `R3_2_TurnOnLowSides()` calls `LL_TIM_EnableAllOutputs(TIMx)`.
- The generated state machine calls `LL_TIM_DisableBRK(TIM1)` before
  `R3_2_TurnOnLowSides(..., M1_CHARGE_BOOT_CAP_DUTY_CYCLES)`.
- Project parameters compute `M1_CHARGE_BOOT_CAP_DUTY_CYCLES` from `0.000`,
  i.e. the call uses the low-sides-on semantic.
- Later normal run calls `PWMC_SwitchOnPWM()`, which also enables TIM1 main
  outputs through `R3_2_SwitchOnPWM()`.

Therefore, the first gate-test firmware must not use normal MCSDK start,
Motor Pilot, PC13 start/stop, or any path that can set `MCI_START`.

## Inputs From Hardware Evidence

The following evidence supports planning only:

- Clean single-input wake retest:
  `LIN1 = 3.13 V`, `REG12 = 12 V`, `nFAULT = 3.3 V`, HSPY `CV`, `0.048 A`.
- Recovery:
  all-inputs-low returned `REG12` to about `0.33 V` with `nFAULT = 3.3 V`.
- Static USB + 24 V recheck:
  `CN3_1` through `CN3_6` all close to `0 V`, `nFAULT = 3.3 V`,
  `REG12 = 0.3 V`, HSPY `CV`, about `0.045 A`.
- No-power gate-source pulldown rework:
  final six-route gate-source readings were reported as `10 kohm`.

This does not prove gate waveforms, MOSFET switching safety, current-sense
correctness, Hall closed-loop behavior, or motor readiness.

## Rule Table

| Item | Rule | Reason |
| --- | --- | --- |
| Firmware base | Use a separate isolated manual-gate-test working tree or build target; do not edit the archived source packet. | The source packet is evidence, not the active firmware workspace. |
| MCSDK start | Do not call `MC_StartMotor1()`, `MCI_StartMotor()`, or set `MCI_START`. | Normal start reaches boot-cap and PWM output paths. |
| MotorControl init | First manual lockout build should not call `MX_MotorControl_Init()` / `MCboot()`. | `MCboot()` starts MCSDK runtime/timers and command machinery. |
| PC13 | Do not configure PC13 as Start/Stop EXTI in the manual gate-test image. | PC13 can call `MC_StartMotor1()` in generated code. |
| MCP / Motor Pilot | Do not initialize ASPEP/MCP command ingress for the first manual image. | Runtime commands can start the motor-control state machine. |
| Hall / speed loop | Do not initialize Hall closed-loop, speed loop, rev-up, or FOC state-machine paths. | Gate-test must not become a motor-control test. |
| TIM1 break | Do not call `LL_TIM_DisableBRK(TIM1)` in the manual lockout image. | The generated start path disables BRK before low-side boot-cap. |
| TIM1 outputs | In the first lockout image, keep `MOE = 0`, `CCER = 0`, and all six driver input pins low. | First step proves output lockout, not switching. |
| Output enable API | First lockout image must not call `LL_TIM_EnableAllOutputs()`, `R3_2_TurnOnLowSides()`, or `PWMC_SwitchOnPWM()`. | These are true output-enabling actions. |
| Debug output | Use only slow foreground status if later implemented; no ISR print, no blocking ISR logic. | Preserve real-time safety boundary. |
| Hardware | No motor, no PWM output, no 24 V, no flash, no Run / Debug in this plan. | Current phase is planning only. |

## Future Firmware Shape

If a later dated gate opens implementation, the first manual firmware should
have these modules or equivalent responsibilities:

| Module | Responsibility |
| --- | --- |
| `gate_test_main` | HAL/system init, then enter a locked foreground loop. No `MX_MotorControl_Init()`. |
| `gate_test_gpio_lock` | Configure `PA8`, `PA9`, `PA10`, `PB13`, `PB14`, and `PB15` as GPIO outputs low before any alternate-function setup. |
| `gate_test_fault_monitor` | Poll `PB12 / nFAULT` as input; if low, keep all driver input pins low and latch a fault state. |
| `gate_test_tim1_lock` | Optionally initialize TIM1 only with outputs disabled: `MOE = 0`, `CCER = 0`, automatic output disabled, break enabled. |
| `gate_test_ingress_lock` | Leave PC13 Start/Stop EXTI and ASPEP/MCP/Motor Pilot command paths absent. |
| `gate_test_assertions` | Compile-time and startup checks that reject any use of normal MCSDK start/output-enable symbols in the lockout image. |

This module list is a plan, not an implementation request.

## Required Static Checks For A Future Implementation

A later implementation must pass a source grep review showing absence of:

```text
MC_StartMotor1
MCI_StartMotor
MCI_START
MX_MotorControl_Init
MCboot
UI_HandleStartStopButton_cb
MX_USART2_UART_Init
ASPEP
MCP
LL_TIM_DisableBRK
R3_2_TurnOnLowSides
PWMC_SwitchOnPWM
LL_TIM_EnableAllOutputs
```

The first lockout implementation must explicitly show:

```text
PA8  = GPIO output low
PA9  = GPIO output low
PA10 = GPIO output low
PB13 = GPIO output low
PB14 = GPIO output low
PB15 = GPIO output low
PB12 = nFAULT input only
TIM1 MOE = 0
TIM1 CCER CH1/CH1N/CH2/CH2N/CH3/CH3N disabled
TIM1 AOE disabled
TIM1 break enabled
```

## Phase Gates

### Gate A - No-Power Plan

Status after this document:

```text
open for document review only
```

Allowed:

- review this plan;
- refine the future lockout source architecture;
- decide exact future files and build target.

Not allowed:

- firmware edits;
- build;
- flash;
- Run / Debug;
- 24 V;
- PWM output;
- motor.

### Gate B - No-Power Build-Only Implementation

Requires a later dated approval record before starting.

Allowed only after that record:

- create an isolated manual gate-test firmware draft;
- run compile-only checks;
- run grep-based lockout checks.

Still not allowed in Gate B:

- flash;
- Run / Debug;
- 24 V;
- PWM output;
- motor.

### Gate C - USB-Only Runtime Lockout Check

Requires a later dated approval record after Gate B passes.

Possible future checks:

- flash and run only the lockout image;
- no 24 V;
- motor disconnected;
- measure MCU-facing driver inputs;
- expect all six inputs low;
- verify `nFAULT` readback / status behavior if exposed.

This phase is not opened by this plan.

### Gate D - 24 V Static Lockout Check

Requires a later dated approval record after Gate C passes.

Possible future conditions:

- motor disconnected;
- HSPY `24 V / 0.2 A`;
- manual lockout image only;
- no output-enable call;
- expected HSPY `CV`, current near prior static baseline, all six inputs low,
  `nFAULT` high, and `REG12` low.

This phase is not opened by this plan.

### Gate E - First No-Motor Output Observation

Requires a later dated approval record after Gate D passes and after a specific
probe / rollback checklist is written.

This plan does not define the output vector yet. It only says the first output
observation must be compile-time fixed, no runtime command ingress, no motor,
current-limited, probe-defined, and stop-rule bounded.

## Stop Rules For Any Later Hardware Gate

Any later powered gate must stop immediately on:

- HSPY entering `CC`;
- current above the gate-specific limit;
- `nFAULT` low after stabilization;
- unexpected `REG12`;
- any driver input not matching the planned static state;
- heat, smell, sound, unstable reading, probe slip, or wiring uncertainty.

These stop rules are placeholders for a later detailed checklist; they do not
open powered work now.

## Decision

The project may continue with no-power planning for an isolated manual
gate-test firmware route. The normal MCSDK generated start path remains
blocked for first powered PWM/gate testing.

The next allowed action is to review this plan and, if accepted later, write a
no-power build-only implementation task package. No hardware action is opened.
