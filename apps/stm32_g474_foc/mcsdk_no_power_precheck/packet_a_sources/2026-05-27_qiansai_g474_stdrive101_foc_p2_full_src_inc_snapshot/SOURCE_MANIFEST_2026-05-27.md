# QIANSAI G474 STDRIVE101 FOC P2 Full Src/Inc Snapshot Manifest - 2026-05-27

## Source

- External Workbench project path:
  `C:\Users\gregrg\.st_workbench\projects\QIANSAI_G474_STDRIVE101_FOC_P2`
- Repository snapshot path:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-27_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot/`
- Capture type: no-power file copy only.
- External project modification: none.

## Scope

Copied into this snapshot:

- `Src/`: 30 files.
- `Inc/`: 28 files.
- `cmake/`: 3 files.
- Top-level project/build metadata: 11 files.
- `SHA256SUMS.txt`: 72 hash entries for the copied source/metadata files.

Not copied:

- `Drivers/`
- `MCSDK_v6.4.2-Full/`
- `ftl/`
- build output directories

The omitted folders are vendor/tool package material, not the project-owned
generated `Src/` / `Inc` evidence requested for this no-power source review.

## Key Evidence Files Present

- `Src/hall_speed_pos_fdbk.c`
- `Inc/hall_speed_pos_fdbk.h`
- `Src/speed_torq_ctrl.c`
- `Inc/speed_torq_ctrl.h`
- `Src/mc_tasks.c`
- `Inc/mc_tasks.h`
- `Src/mc_tasks_foc.c`
- `Src/mc_interface.c`
- `Inc/mc_interface.h`
- `Src/mc_api.c`
- `Inc/mc_api.h`
- `Src/mc_app_hooks.c`
- `Inc/mc_app_hooks.h`
- `Src/mc_config.c`
- `Inc/mc_config.h`
- `Src/mc_config_common.c`
- `Inc/mc_config_common.h`
- `Src/mc_parameters.c`
- `Inc/mc_parameters.h`
- `Src/motorcontrol.c`
- `Inc/motorcontrol.h`
- `Inc/mc_type.h`
- `Src/stm32g4xx_it.c`
- `Inc/stm32g4xx_it.h`
- `Src/stm32g4xx_mc_it.c`
- `Src/pwm_curr_fdbk.c`
- `Inc/pwm_curr_fdbk.h`
- `Inc/register_interface.h`
- `Src/mc_configuration_registers.c`
- `Inc/mc_configuration_registers.h`
- `Src/usart_aspep_driver.c`
- `Src/aspep.c`
- `Inc/aspep.h`

## Noted Absence

- `Inc/usart_aspep_driver.h` is not present in the generated `Inc/` folder.
  The generated source provides `Src/usart_aspep_driver.c`; this absence is
  recorded and must not be silently treated as an accepted interface header.

## Safety Boundary

This snapshot is source evidence only. It does not authorize firmware edits,
generated-code edits, build execution, flash, 24V, power-board connection,
motor connection, Gate PWM output, Motor Profiler, Motor Pilot, Hall
closed-loop, or sensorless / SMO claims.
