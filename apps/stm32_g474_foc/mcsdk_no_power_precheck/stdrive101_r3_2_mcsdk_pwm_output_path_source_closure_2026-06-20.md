# STDRIVE101 R3_2 MCSDK PWM Output Path Source Closure - 2026-06-20

## Summary

- Evidence ID:
  `EV-2026-06-20-STDRIVE101-R3-2-MCSDK-PWM-OUTPUT-PATH-SOURCE-CLOSURE-001`.
- Task ID:
  `TASK-2026-06-20-stdrive101-r3-2-mcsdk-pwm-output-path-source-closure`.
- Scope:
  no-power source review of the exact MCSDK `R3_2` PWM/current-feedback
  implementation referenced by the generated project.
- Hardware action:
  none.
- Firmware action:
  no edit, no flash, no Run / Debug, no Motor Pilot, no Motor Profiler.
- Decision:
  `STDRIVE101 R3_2 MCSDK PWM output path source closure / exact local
  Workbench MCSDK r3_2_g4xx_pwm_curr_fdbk.c found and hashed / R3_2 output
  enable behavior reviewed / normal generated MCSDK start remains blocked for
  powered PWM because start path disables BRK before low-side boot-cap and
  R3_2_TurnOnLowSides enables TIM1 main outputs with 0-tick low-sides-on
  semantics / no PWM-output validation / no powered-drive readiness`.

## Boundary

This is source evidence only. It does not authorize motor connection, Gate PWM
output, Motor Pilot, Motor Profiler, firmware Flash / Run / Debug, Hall closed
loop, sensorless operation, power-stage readiness, or motor readiness.

## Source Identity

The generated project's `cmake/stm32cubemx/CMakeLists.txt` references:

`../../MCSDK_v6.4.2-Full/MotorControl/MCSDK/MCLib/G4xx/Src/r3_2_g4xx_pwm_curr_fdbk.c`

The repository snapshot intentionally omits `MCSDK_v6.4.2-Full/`; its manifest
states vendor/tool package material was not copied.

The external Workbench project still contains the referenced MCSDK tree:

`C:\Users\gregrg\.st_workbench\projects\QIANSAI_G474_STDRIVE101_FOC_P2\MCSDK_v6.4.2-Full\MotorControl\MCSDK\MCLib\G4xx\Src\r3_2_g4xx_pwm_curr_fdbk.c`

Hash:

```text
SHA256 = D3787B25374154AB1DC6A2CABD05DE299D5691DA92DDC4DE4BEC93DE81BE2451
Length = 67184 bytes
LastWriteTime = 2026-04-21 12:15:27
```

The installed package copy at:

`C:\Users\gregrg\STM32Cube\Repository\MCSDK_v6.4.2-Full\MotorControl\MCSDK\MCLib\G4xx\Src\r3_2_g4xx_pwm_curr_fdbk.c`

has the same SHA256 hash:

```text
D3787B25374154AB1DC6A2CABD05DE299D5691DA92DDC4DE4BEC93DE81BE2451
```

This closes the local-source identity for the reviewed `R3_2` file, but it
does not make the repository snapshot self-contained.

## Output Path Findings

### TIM1 Channel Mask

The reviewed `R3_2` source defines `TIMxCCER_MASK_CH123` as channels
`CH1`, `CH1N`, `CH2`, `CH2N`, `CH3`, and `CH3N`.

Interpretation: when the reviewed code enables this mask, it is preparing both
high-side and complementary low-side TIM1 channel outputs.

### R3_2_TIMxInit

`R3_2_TIMxInit()`:

- disables the main TIM counter,
- configures preload and TRGO,
- clears BRK / BRK2 flags,
- enables TIM break interrupt,
- enables the `CH1/CH1N/CH2/CH2N/CH3/CH3N` channel mask,
- enables update interrupt.

No `LL_TIM_EnableAllOutputs()` call was observed in this init block.

Interpretation: init prepares TIM1 channel / interrupt state but does not by
itself prove gate-output enable. The later low-side and switch-on routines are
the output-enabling points.

### R3_2_TurnOnLowSides

`R3_2_TurnOnLowSides()` comments define:

- `ticks = 0`: low sides ON.
- `ticks = PWM_PERIOD_CYCLES / 2`: low sides OFF.

The function sets compare values for channels 1, 2, and 3 to `ticks`, then
calls `LL_TIM_EnableAllOutputs(TIMx)`.

Project parameters set:

- `LOW_SIDE_SIGNALS_ENABLING = LS_PWM_TIMER`
- `M1_CHARGE_BOOT_CAP_DUTY_CYCLES = (uint32_t)0.000 * (PWM_PERIOD_CYCLES / 2)`

Interpretation: in this generated project, the boot-cap call uses `0` ticks,
which matches the MCSDK comment's low-sides-on semantic, not a harmless
"zero output" semantic. This is a hard reason not to use the normal generated
start path as a first gate-output test.

### R3_2_SwitchOnPWM

`R3_2_SwitchOnPWM()`:

- clears `TurnOnLowSidesAction`,
- sets CH1/CH2/CH3 compare values to half-period derived values,
- sets CH4 trigger compare,
- sets OSSI in `BDTR`,
- calls `LL_TIM_EnableAllOutputs(TIMx)`,
- sets `PWMState = true`.

Interpretation: `PWMC_SwitchOnPWM()` is a true output-enabling action through
the bound `R3_2_SwitchOnPWM()` callback.

### R3_2_SwitchOffPWM

`R3_2_SwitchOffPWM()`:

- sets `PWMState = false`,
- clears `TurnOnLowSidesAction`,
- calls `LL_TIM_DisableAllOutputs(TIMx)`,
- only manipulates GPIO enable pins when `LowSideOutputs == ES_GPIO`.

Project configuration uses `LS_PWM_TIMER`, so the relevant shutoff action is
the TIM main-output disable.

## Generated State-Machine Findings

In `mc_tasks_foc.c`, when the state machine is in `IDLE` and sees
`MCI_START` or `MCI_MEASURE_OFFSETS`, the generated path calls:

```text
LL_TIM_DisableBRK(TIM1);
R3_2_TurnOnLowSides(pwmcHandle[M1], M1_CHARGE_BOOT_CAP_DUTY_CYCLES);
```

The same disable-BRK plus low-side call appears in the already-calibrated and
post-offset branches. Later, in the `CHARGE_BOOT_CAP` path where normal run is
entered, the generated code calls:

```text
R3_2_SwitchOffPWM(pwmcHandle[M1]);
LL_TIM_ClearFlag_BRK(TIM1);
LL_TIM_EnableBRK(TIM1);
...
PWMC_SwitchOnPWM(pwmcHandle[M1]);
```

Interpretation: normal generated start is not a cautious first gate-test
sequence. It explicitly disables TIM1 break before the low-side bootstrap
charge step, and that low-side step calls `LL_TIM_EnableAllOutputs()` with the
project's 0-tick low-sides-on setting.

## Protection Path Findings

The packet-local `stm32g4xx_mc_it.c` break interrupt handler:

- checks TIM1 `BRK`,
- clears the flag,
- calls `PWMC_DP_Handler(&PWM_Handle_M1._Super)`,
- checks TIM1 `BRK2`,
- calls `PWMC_OVP_Handler(&PWM_Handle_M1._Super, TIM1)`.

The packet-local `PWMC_DP_Handler()`:

- calls `PWMC_SwitchOffPWM()`,
- sets `driverProtectionFlag = true`.

The packet-local `PWMC_IsFaultOccurred()`:

- reports `MC_DP_FAULT` when `driverProtectionFlag` is set,
- reports `MC_OVER_VOLT` / `MC_OVER_CURR` for their flags.

The packet-local safety task calls `PWMC_IsFaultOccurred()`, processes the
fault through `MCI_FaultProcessing()`, and calls `PWMC_SwitchOffPWM()` plus
`FOC_Clear()` if a fault state is present.

Interpretation: there is a real MCSDK protection-reporting path after a BRK
interrupt, but the generated boot-cap path disables BRK before calling the
low-side output routine. That interaction must not be tested under power as a
first experiment.

## TIM1 BKIN / nFAULT Findings

The generated `MX_TIM1_Init()` configures:

- break input source `TIM_BREAKINPUTSOURCE_BKIN`,
- break input source polarity `TIM_BREAKINPUTSOURCE_POLARITY_LOW`,
- break state enabled,
- break polarity `TIM_BREAKPOLARITY_HIGH`,
- break filter `4`,
- automatic output disabled.

The previous source review already recorded generation-log invalid-parameter
messages around BKIN / PWM / MotorControl fields.

Interpretation: the active-low `nFAULT` intent is present in Workbench/.ioc
clues, but the generated HAL / LL break-polarity combination and boot-cap
disable-BRK behavior still require a separate register-level or manual-plan
review before any powered gate-output step.

## Decision

The exact local `R3_2` source used by the Workbench project is now identified
and reviewed by hash. This resolves the previous "external implementation not
reviewed" gap enough for planning, but it strengthens the block on direct
powered PWM:

- the normal start path can command low-side bootstrap charging;
- the low-side bootstrap helper treats `0` ticks as low-sides ON;
- that helper enables TIM1 main outputs;
- the generated state machine disables BRK before that helper;
- and normal run later calls `PWMC_SwitchOnPWM()`, which also enables TIM1
  main outputs.

Therefore the next allowed step is not powered PWM. It is a no-power-only
manual gate-test firmware plan that does not use normal MCSDK start, Motor
Pilot, PC13 start/stop, Hall closed-loop, speed loop, or motor connection.

## Next Allowed Checkpoint

Write a separate no-power-only manual gate-test firmware plan with these
minimum constraints:

- no motor connected;
- no Motor Pilot / Profiler;
- no normal `MC_StartMotor1()` / `MCI_START` path;
- PC13 start/stop and MCP command ingress isolated;
- TIM1 break / `nFAULT` polarity reviewed before any output enable;
- first implementation step, if later authorized, must be no-power build-only;
- first hardware observation, if later authorized by a separate phase gate,
  must use current-limited supply, defined probe points, rollback rules, and
  no motor.

No motor, PWM output, Motor Pilot, Motor Profiler, firmware Flash / Run /
Debug, Hall closed loop, sensorless operation, power-stage readiness, or motor
readiness is authorized by this source closure.
