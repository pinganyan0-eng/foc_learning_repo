# STDRIVE101 PWM Gate-Test No-Power Source Review - 2026-06-20

## Summary

- Evidence ID:
  `EV-2026-06-20-STDRIVE101-PWM-GATE-TEST-NO-POWER-SOURCE-REVIEW-001`.
- Task ID:
  `TASK-2026-06-20-stdrive101-pwm-gate-test-no-power-source-review`.
- Scope:
  no-power source/configuration review for a future explicit PWM / gate-test
  phase gate.
- Hardware action:
  none in this review.
- Firmware action:
  no edit, no flash, no Run / Debug, no Motor Pilot, no Motor Profiler.
- Decision:
  `STDRIVE101 PWM gate-test no-power source review / static hardware screen
  passed for planning only / generated MCSDK direct PWM gate remains blocked by
  command-ingress, external R3_2 implementation, BKIN polarity, Hall-route, and
  generation-log trust gaps / no PWM-output validation / no powered-drive
  readiness`.

## Boundary

This record does not authorize motor connection, Gate PWM output, Motor Pilot,
Motor Profiler, firmware Flash / Run / Debug, Hall closed loop, sensorless
operation, power-stage readiness, or motor readiness.

2026-06-20 follow-up source closure has now been recorded. The current safe
next work is a separate no-power-only manual gate-test firmware plan. No
powered PWM action is opened by this file.

## Inputs

Recent bounded hardware evidence used as context:

- `stdrive101_reg12_single_input_wake_retest_clean_result_2026-06-20.md`:
  clean `LIN1` wake retest with HSPY `CV`, `0.048 A`, `LIN1 = 3.13 V`,
  `nFAULT = 3.3 V`, and `REG12 = 12 V`; recovery returned `REG12` to
  `0.33 V` with `nFAULT = 3.3 V`.
- `stdrive101_all_inputs_low_static_recheck_result_2026-06-20.md`:
  after removing the `10 kohm` wake stimulus, `CN3_1` through `CN3_6` were
  reported close to `0 V`, `nFAULT = 3.3 V`, and `REG12 = 0.3 V`.
- `stdrive101_usbonly_mcu_default_input_state_result_2026-06-20.md`:
  USB/ST-LINK connected, no 24 V, `CN3_1` through `CN3_6` were reported close
  to `0 V`.
- `stdrive101_usb24_static_recheck_result_2026-06-20.md`:
  USB/ST-LINK connected and HSPY 24 V / 0.2 A, HSPY stayed `CV`, current was
  about `0.045 A`, `CN3_1` through `CN3_6` were reported close to `0 V`,
  `nFAULT = 3.3 V`, and `REG12 = 0.3 V`.

Source snapshot reviewed:

`packet_a_sources/2026-05-27_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot/`

## Source Findings

### Pin and Route Findings

- Generated PWM pin macros in `Inc/main.h` map:
  - `M1_PWM_UH = PA8`
  - `M1_PWM_VH = PA9`
  - `M1_PWM_WH = PA10`
  - `M1_PWM_UL = PB13`
  - `M1_PWM_VL = PB14`
  - `M1_PWM_WL = PB15`
- Generated protection / fault pin macro maps `M1_DP = PB12`.
- `stm32g4xx_hal_msp.c` configures `PB12` as `TIM1_BKIN` with pull-up.
- Generated Hall macros still map Hall to `PA15 / PB3 / PB10`, while the
  accepted PCB2 no-power continuity table maps the project Hall candidates to
  `PA0 / PA1 / PB4` and maps `CN3_2 / LIN1` to `PB3`.
- Therefore the generated Hall route is not usable as a PCB2 Hall proof.

### Default Boot / No-Autostart Findings

- `main.c` initializes GPIO, DMA, ADCs, `TIM1`, `USART2`, MotorControl, and
  NVIC, then enters an empty `while (1)`.
- No direct `MC_StartMotor1()` call was found in `main.c`.
- `motorcontrol.c` calls `MCboot(pMCI)` through `MX_MotorControl_Init()`.
- `MCboot()` initializes the motor-control stack and starts timers, but the
  generated `mc_config.c` initializes `Mci[M1].DirectCommand =
  MCI_NO_COMMAND` and `Mci[M1].State = IDLE`.
- `FOC_Clear()` calls `PWMC_SwitchOffPWM()` during initialization.

Interpretation: the generated application does not show a direct `main()`
autostart, but initialization still brings up the MCSDK runtime and timer /
interrupt environment.

### Command-Ingress Findings

- `Start_Stop` is defined on `PC13` with `EXTI15_10_IRQn`.
- `UI_HandleStartStopButton_cb()` calls `MC_StartMotor1()` when motor state is
  `IDLE`.
- `MC_StartMotor1()` routes into `MCI_StartMotor()`, which sets
  `DirectCommand = MCI_START` when the state is `IDLE` and there are no
  blocking faults.
- Once the medium-frequency state machine sees `MCI_START`, the generated path
  reaches `R3_2_TurnOnLowSides()` during `CHARGE_BOOT_CAP` handling and later
  `PWMC_SwitchOnPWM()`.

Interpretation: even without a direct `main()` autostart, runtime start
commands are a real gate risk. Any future gate-test firmware plan must block
or isolate PC13 start/stop and Motor Pilot / MCP-style command ingress before
hardware output validation.

### TIM1 Break / nFAULT Findings

- `main.c` configures a TIM1 break input source on `TIM_BREAKINPUTSOURCE_BKIN`
  with `TIM_BREAKINPUTSOURCE_POLARITY_LOW`.
- The same `MX_TIM1_Init()` configures break/dead-time with
  `BreakState = TIM_BREAK_ENABLE`, `BreakPolarity = TIM_BREAKPOLARITY_HIGH`,
  and `AutomaticOutput = TIM_AUTOMATICOUTPUT_DISABLE`.
- `.ioc.wb` source clues state `PB12.GPIO_Label=M1_DP`,
  `PB12.Signal=TIM1_BKIN`, `PB12.GPIO_PuPd=GPIO_PULLUP`, and
  `M1_DP_BKIN_POLARITY=EMSTOP_ACTIVE_LOW`.
- Because the user-observed `nFAULT` is active-low and the generated import log
  includes TIM1 / BKIN-related invalid-value messages, the exact register-level
  fault-polarity behavior must be closed before any PWM output test.

### External MCSDK Implementation Gap

- `mc_config.c` binds PWM callbacks to `R3_2_SwitchOffPWM`,
  `R3_2_SwitchOnPWM`, and `R3_2_TurnOnLowSides`.
- The packet-local generic `pwm_curr_fdbk.c` only delegates these callback
  calls.
- `cmake/stm32cubemx/CMakeLists.txt` includes the actual R3_2 implementation
  from an external path:
  `../../MCSDK_v6.4.2-Full/MotorControl/MCSDK/MCLib/G4xx/Src/r3_2_g4xx_pwm_curr_fdbk.c`.
- That exact file is not packet-local in this source snapshot.

Interpretation: the bottom PWM-output implementation is not fully captured in
this evidence packet. It must be captured and reviewed, or bypassed by a
separate explicitly bounded manual gate-test plan, before any PWM-output phase
gate.

### Generation-Log Trust Gap

The generated project log contains import / validation errors on parameters
that are directly relevant to a PWM/gate test, including:

- `HWV_PWM`
- `LOW_SIDE_SIGNALS_ENABLING`
- `M1_DP_BKIN_FILTER`
- `M1_DP_BKIN_MODE`
- `M1_DP_BKIN_POLARITY`
- `M1_PWM_CHARGE_BOOT_CAP_DUTY_CYCLES`
- `M1_PWM_TIMER_BRK_IRQ`
- `M1_PWM_TIMER_UP_IRQ`
- `PHASE_U_PWM_CHANNEL`
- `PHASE_V_PWM_CHANNEL`
- `PHASE_W_PWM_CHANNEL`
- `PWM_FREQUENCY`
- `PWM_TIMER_SELECTION`
- `TIM_SlaveMode`
- `SourceBRK2DigInputPolarity`

Interpretation: the generated source cannot be treated as a high-trust
drop-in PWM/gate-test firmware solely because it builds or because static
hardware checks passed.

## Decision

The recent bounded hardware evidence is good enough to say the immediate
static screen is clean for planning:

- `REG12` wake/recovery worked under the single `LIN1` stimulus.
- `nFAULT` stayed high in the clean retest.
- all six driver inputs were reported low in all-inputs-low static, USB-only,
  and USB + 24 V static states.

It is not enough to enter PWM output:

- runtime start-command ingress exists,
- start-command state flow reaches low-side / PWM routines,
- the exact R3_2 PWM implementation is not packet-local,
- BKIN / `nFAULT` polarity behavior is not closed at register level,
- generated Hall pins do not match the accepted PCB2 Hall continuity route,
- and the generation log contains PWM / BKIN / MotorControl parameter errors.

## Next Allowed Checkpoint

2026-06-20 follow-up:

`stdrive101_r3_2_mcsdk_pwm_output_path_source_closure_2026-06-20.md` now
records the exact local Workbench MCSDK `r3_2_g4xx_pwm_curr_fdbk.c` source
identity and PWM-output-path review. That review closes the previous external
R3_2 source-review gap for planning, but it confirms normal generated MCSDK
start remains blocked for powered PWM.

The remaining no-power branch before any powered PWM step is:

1. Manual gate-test firmware plan only:
   write a separate no-power plan that disables or isolates PC13 start/stop,
   Motor Pilot / MCP command ingress, Hall closed-loop paths, speed-loop paths,
   and normal MCSDK start-state flow before any later implementation.

No motor, PWM output, Motor Pilot, Motor Profiler, firmware Flash / Run /
Debug, Hall closed loop, sensorless operation, power-stage readiness, or motor
readiness is authorized by this review.
