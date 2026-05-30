# Workbench FOC Capture Blocker - 2026-05-20

## Scope

This is a no-power Workbench GUI capture attempt for:

- Project title: `QIANSAI_G474_STDRIVE101_FOC_P2`
- Algorithm target: `FOC`
- Control board: `NUCLEO-G474RE`
- MCU: `STM32G474RETx`
- Power board: `QIANSAI_STDRIVE101_PCB2_POWER`
- Temporary motor placeholder: `R57BLB50L2`

`R57BLB50L2` is only a Workbench placeholder selected after user approval. It
is not accepted as measured project motor data and does not imply Motor
Profiler evidence.

## Result

Stopped before create/generate.

Workbench accepted the component selections far enough to show the custom
power board in the summary, but it left the project in an error state:

- `Current Sensing`: red X, with child item `ThreeShunt_RawCurrents_SingleEnded`
- `PWM Generation`: red X, with child item `DrivingHighAndLowSides`
- `Driver Protection`: green check
- `Create`: disabled

No `.stwb6` was saved for this capture because Workbench did not expose a valid
pre-generate save path while the summary remained blocked.

## Primary Log Evidence

Archived log:

`logs/2026-05-20_connectAlgo_qiansai_pwm_blocker.log`

SHA256:

`0CBA4EB7971759C2716709411121816629AAE113D99EF5A53343F6BECBDEE0E3`

Key log lines:

```text
INFO - --root assets --control NUCLEO-G474RE --power '~QIANSAI_STDRIVE101_PCB2_POWER'
DEBUG - PVConnect: DrivingHighAndLowSides Global processing start
ERROR - PVConnect: DrivingHighAndLowSides No timer matches all signals requirement
DEBUG - PVConnect: DrivingHighAndLowSides Global processing completed
```

## PWM Mapping That Triggered The Blocker

The saved custom power board maps the six STDRIVE101 inputs as follows through
the NUCLEO-G474RE Morpho connector:

| Signal | Connector | MCU pin | Relevant timer signals |
| --- | --- | --- | --- |
| `PWM_CHU_H` | `ML17` | `PA15` | `TIM1_BKIN`, `TIM2_CH1`, `TIM8_CH1` |
| `PWM_CHV_H` | `MR25` | `PB10` | `TIM1_BKIN`, `TIM2_CH3` |
| `PWM_CHW_H` | `MR21` | `PA9` | `TIM1_CH2`, `TIM2_CH3` |
| `PWM_CHU_L` | `MR31` | `PB3` | `TIM8_CH1N`, `TIM2_CH2`, `SYS_JTDO-SWO` |
| `PWM_CHV_L` | `MR23` | `PA8` | `TIM1_CH1` |
| `PWM_CHW_L` | `MR33` | `PA10` | `TIM1_CH3` |

This cannot form one consistent `TIM1` complementary three-phase set
(`CH1/CH2/CH3` plus `CH1N/CH2N/CH3N`). Workbench therefore cannot accept
`DrivingHighAndLowSides` for this board/control-board pairing.

For comparison, a timer-consistent `TIM1` NUCLEO-G474RE candidate would need to
be reviewed against the real PCB route before use, for example:

- High sides: `PA8/PA9/PA10` (`MR23/MR21/MR33`) as `TIM1_CH1/CH2/CH3`
- Low sides: `PB13/PB14/PB15` (`MR30/MR28/MR26`) as `TIM1_CH1N/CH2N/CH3N`

This note does not authorize changing the board definition to those pins. It
only records why the current saved definition is blocked.

## Screenshot Evidence

Selected screenshots captured under `screenshots/`:

- `2026-05-20_workbench_launch_home.png`
- `2026-05-20_workbench_new_project_page.png`
- `2026-05-20_workbench_custom_power_board_selected.png`
- `2026-05-20_workbench_after_custom_power_board_confirm.png`
- `2026-05-20_workbench_control_board_nucleo_g474re_search.png`
- `2026-05-20_workbench_after_nucleo_g474re_confirm.png`
- `2026-05-20_workbench_motor_select_page.png`
- `2026-05-20_workbench_components_nucleo_qiansai_r57.png`
- `2026-05-20_workbench_summary_project_named.png`
- `2026-05-20_workbench_current_sensing_redx_detail.png`
- `2026-05-20_workbench_pwm_generation_redx_detail.png`
- `2026-05-20_workbench_pwm_high_low_subitem_clicked.png`
- `2026-05-20_workbench_error_panel_clicked.png`

## Decision

`Partial clue / Workbench FOC GUI path reached / Packet A still blocked`.

The custom board is visible in Workbench and was not replaced by
`EVALSTDRIVE101`, but the current saved PWM signal mapping is not accepted by
Workbench for FOC `DrivingHighAndLowSides`. Packet A cannot be accepted from
this attempt.

## No-Power Boundary

No Generate, build, flash, 24V, power-board connection, motor connection, Gate
PWM output, Motor Profiler, Motor Pilot, Hall closed-loop, or sensorless / SMO
claim was made.
