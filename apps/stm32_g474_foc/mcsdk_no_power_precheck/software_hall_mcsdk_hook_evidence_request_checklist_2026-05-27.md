# 软件 Hall MCSDK Hook 证据请求清单 - 2026-05-27

Decision:
`Software Hall MCSDK hook evidence request checklist / no firmware implementation / no MCSDK hook / no Hall readiness`.

## 中文结论

这份清单不是让你现在写代码。它只回答一个工程问题：
以后如果真的要把 `PA0/PA1/PB4` 软件 Hall 接入 MCSDK，必须先拿到哪些真实源代码、接口说明和回滚证据。

当前路线仍然保持：

```text
HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4
PB3 = LIN1，不参与 Hall
P14/P15 = 3V3/GND
```

PCB2 仍未焊接完成。DMM 连续性 / 短路表暂缓，不是通过。

## 功能句

```text
before any software Hall -> MCSDK hook
-> archive exact generated / MCSDK interface source files
-> review call timing, data units, ownership, rollback, and hard stops
-> only then decide whether a hook proposal can be written
```

中文说法：现在不是接线、不是上电、不是改 `HALL_M1`，而是像采购清单一样列出“缺哪些源代码证据”。缺证据时，任何 hook 都不能开写。

## Source Clues Used

Read-only generated log clues from:
`packet_a_sources/2026-05-21_qiansai_g474_stdrive101_foc_p2_generated_project/QIANSAI_G474_STDRIVE101_FOC_P2.log`.

The log names these generated files, but most of them are not archived in the current Packet A folder:

- `motorcontrol.c/.h`
- `mc_type.h`
- `speed_torq_ctrl.c/.h`
- `mc_tasks.h`
- `mc_tasks.c`
- `mc_tasks_foc.c`
- `mc_api.c/.h`
- `mc_config.c/.h`
- `mc_config_common.c/.h`
- `pwm_curr_fdbk.c/.h`
- `mc_interface.c/.h`
- `mc_parameters.c/.h`
- `register_interface.h`
- `usart_aspep_driver.c`
- `mc_configuration_registers.c/.h`
- `aspep.c/.h`
- `hall_speed_pos_fdbk.c/.h`
- `mc_app_hooks.c/.h`

2026-05-27 update: the existing external Workbench project was found at
`C:\Users\gregrg\.st_workbench\projects\QIANSAI_G474_STDRIVE101_FOC_P2` and
its generated `Src/`, `Inc/`, `cmake/`, and top-level project/build metadata
were archived at
`packet_a_sources/2026-05-27_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot/`.
That resolves source availability for read-only MCSDK interface review only.
It does not authorize firmware implementation, generated-code edits, MCSDK
hook work, build claims, or Hall readiness.

Archived local clues already reviewed:

- `main.c`
- `mc_config.c`
- `parameters_conversion.h`
- `QIANSAI_G474_STDRIVE101_FOC_P2.ioc`
- `QIANSAI_G474_STDRIVE101_FOC_P2.log`

## Evidence Request Table

| Evidence item | Why it is needed before hook | Current status | Acceptance rule |
| --- | --- | --- | --- |
| Exact `hall_speed_pos_fdbk.c/.h` from the same generated project | Proves how MCSDK standard Hall feedback object computes angle, speed, validity, direction, and timeout. | Log-only clue. | Must archive full source from the same Workbench project/version; snippets or screenshots are not enough. |
| Base speed / position feedback interface source or official interface docs | Proves the required API, struct layout, units, validity flags, and call ownership. | Missing. | Must identify the exact interface consumed by MCSDK speed / position feedback, not guessed names. |
| Exact `speed_torq_ctrl.c/.h` | Proves what the speed loop consumes and what must not be written directly. | Log-only clue. | Must be reviewed before any `speed_candidate` path is proposed. |
| Exact `mc_tasks.c`, `mc_tasks.h`, and `mc_tasks_foc.c` | Proves medium-frequency / high-frequency call timing and where feedback is read. | Log-only clue. | Must prove the hook does not run in JEOC / FOC ISR and does not change TIM1 PWM timing. |
| Exact `mc_interface.c/.h` and `mc_api.c/.h` | Proves external control API boundaries and whether read-only debug access exists. | Log-only clue. | Must be reviewed before exposing software Hall debug or candidate speed through MCSDK APIs. |
| Exact `mc_config.c/.h` and `mc_config_common.c/.h` | Proves generated object ownership, including `HALL_M1`, `SpeednTorqCtrlM1`, `PIDSpeedHandle_M1`, `pSTC`, `MCI_Handle_t`, and `FOCVars`. | Partial: `mc_config.c` archived; headers missing. | Must not modify generated object wiring without a separate reviewed hook plan. |
| Exact `mc_parameters.c/.h` and `parameters_conversion.h` | Proves constants, scaling, speed units, timer periods, filters, and selected sensor mode. | Partial: `parameters_conversion.h` archived; `mc_parameters.*` missing. | Must prove unit conversion before any `speed_candidate` is consumed. |
| Exact `motorcontrol.c/.h` and `mc_type.h` | Proves public motor-control types and possible API contracts. | Log-only clue. | Must be reviewed before adding any public adapter type or callback. |
| Exact `mc_app_hooks.c/.h` | Proves whether Workbench generated safe hook locations exist. | Log-only clue. | Hook files are not usable until full source and call timing are reviewed. |
| Exact interrupt source files, if generated, such as `stm32g4xx_it.c/.h` | Proves ISR ownership for `TIM2_IRQHandler`, EXTI handlers, and MCSDK interrupts. | Missing from Packet A folder. | Must be reviewed before any EXTI / timer ISR wiring. |
| Exact `pwm_curr_fdbk.c/.h` and current-sense backend files | Proves current feedback and PWM timing ownership. | Log-only clue. | Read-only review only; software Hall must not alter current feedback or PWM timing. |
| Exact `register_interface.h`, `mc_configuration_registers.c/.h`, `usart_aspep_driver.c`, and `aspep.c/.h` | Proves MCSDK monitor / ASPEP / USART ownership and debug transport risk. | Log-only clue. | Must be reviewed before reusing USART2, ASPEP, MCP, or register paths for debug output. |
| Exact build system files and compiler command records | Proves a no-power build-only path can compile the proposed boundary. | Current CLI build remains blocked by toolchain path. | Build success can prove only no-power compile evidence, not Hall or hardware readiness. |

## Rejected Evidence Types

These do not authorize a hook:

- log-only generated file names;
- screenshots of source code without full files;
- files from a different Workbench project;
- files from a different MCSDK version without version review;
- AI summaries of MCSDK internals;
- successful host Python tests;
- successful no-power build-only result by itself;
- user memory of how MCSDK works;
- any powered result without prior no-power gates.

## Hook Review Questions Required Later

A future hook proposal must answer all of these before code:

- Which exact source file owns speed / position feedback data?
- Which exact function or virtual table, if any, is safe to implement or wrap?
- Which context calls the feedback update: EXTI, TIM2, medium-frequency task, or FOC high-frequency task?
- What units are used for speed, angle, direction, and time delta?
- How are invalid Hall states `000/111` represented to MCSDK?
- How are repeated states, abnormal jumps, bounce candidates, timeout, and zero speed represented?
- How is direction convention calibrated against the real motor after hardware is safe?
- What happens during startup before the first valid Hall transition?
- How does the hook avoid `printf`, JSON, UART transmit, blocking delay, and dynamic allocation in ISR?
- How does the hook avoid TIM1 PWM, JEOC / FOC ISR, current-feedback paths, and Gate PWM output?
- What is the compile-time feature flag or rollback switch?
- Which files are generated and must not be hand-edited?
- Which files are project-owned adapter files and safe to edit after gates open?

## Allowed Current Use

This checklist can be used to request source files from the generated Workbench project or MCSDK package.
It can also be used to reject premature code proposals that try to directly patch `HALL_M1`, `SpeednTorqCtrlM1`, speed PID, JEOC / FOC ISR, or TIM1 PWM.

## Not Allowed Current Use

This checklist does not allow:

- firmware implementation;
- MCSDK hook implementation;
- generated-code editing;
- CubeMX / Workbench setting edits;
- flashing STM32;
- no-power build claim;
- DMM pass claim;
- Hall closed-loop claim;
- Motor Profiler / Motor Pilot;
- 24V, power-board connection, motor connection, or Gate PWM output.

## Next External Evidence Request

When the generated project source folder is available, copy the full generated `Src/` and `Inc/` files named above into a dated Packet A source folder, then run a new source review before any hook proposal.

No user hardware action is needed while PCB2 is unpopulated.
