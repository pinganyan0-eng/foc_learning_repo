# Workbench TIM1 Adapter Follow-up - 2026-05-20

## Scope

This is a no-power follow-up to the blocked Workbench FOC custom-board capture.
It tries to resolve Workbench compatibility issues without pretending that the
current PCB2 physical route has changed.

No Generate, build, flash, 24V, power-board connection, motor connection, Gate
PWM output, Motor Profiler, Motor Pilot, Hall closed-loop, or sensorless / SMO
claim was made.

## TIM1 Adapter Result

A no-power candidate board was created and installed locally:

- Repo source:
  `QIANSAI_STDRIVE101_TIM1_ADAPTER_POWER.no_power_candidate_2026-05-20.json`
- Workbench user-board install:
  `C:\Users\gregrg\.st_workbench\hardware\board\power\QIANSAI_STDRIVE101_TIM1_ADAPTER_POWER.json`
- SHA256:
  `6DDD08BCDCCD70CA231F73FCB7BEAAE6226EEB97F332FD9CFDB381995017D2D0`

The candidate keeps the board explicitly marked as an adapter / rework route,
not the current PCB2 as-built route. It maps the six STDRIVE101 PWM inputs to a
consistent `TIM1` complementary set:

| Signal | Connector | MCU pin | Timer |
| --- | --- | --- | --- |
| `PWM_CHU_H` | `MR23` | `PA8` | `TIM1_CH1` |
| `PWM_CHV_H` | `MR21` | `PA9` | `TIM1_CH2` |
| `PWM_CHW_H` | `MR33` | `PA10` | `TIM1_CH3` |
| `PWM_CHU_L` | `MR30` | `PB13` | `TIM1_CH1N` |
| `PWM_CHV_L` | `MR28` | `PB14` | `TIM1_CH2N` |
| `PWM_CHW_L` | `MR26` | `PB15` | `TIM1_CH3N` |

Workbench accepted this enough for:

- `PWM Generation`: green check
- `Driver Protection`: green check
- `UART Communication`: green check
- `Current Sensing`: still red X
- `Create`: still disabled

The Workbench log no longer contains the previous timer mismatch error.

Archived log:

`logs/2026-05-20_connectAlgo_tim1_adapter_pwm_pass_current_sensing_blocked.log`

SHA256:

`3A6109B82EAB2FDF21C97C989640EC8A7F2B99B7B00B312EA6E33A287A583D3C`

Key log lines:

```text
INFO - --root assets --control NUCLEO-G474RE --power '~QIANSAI_STDRIVE101_TIM1_ADAPTER_POWER'
DEBUG - PVConnect: DrivingHighAndLowSides Timer Candidate  TIM1
DEBUG - PVConnect: DrivingHighAndLowSides  Signal connectivity High  cost 0 PWM_CHU_H MR23_1 PA8 TIM1_CH1
DEBUG - PVConnect: DrivingHighAndLowSides  Signal connectivity High  cost 0 PWM_CHV_H MR21_1 PA9 TIM1_CH2
DEBUG - PVConnect: DrivingHighAndLowSides  Signal connectivity High  cost 0 PWM_CHW_H MR33_1 PA10 TIM1_CH3
DEBUG - PVConnect: DrivingHighAndLowSides Global processing completed
DEBUG - SWConnect: SingleErrorTrigger_FixedReference Global processing completed
```

## Current-sensing blocker

The first TIM1 adapter kept the current PCB2 source clue:

| Signal | Connector | MCU pin |
| --- | --- | --- |
| `CURRENT_SHUNT_UP` | `ML32` | `PA4` |
| `CURRENT_SHUNT_VP` | `ML34` | `PB0` |
| `CURRENT_SHUNT_WP` | `MR11` | `PA5` |

Workbench still showed `ThreeShunt_RawCurrents_SingleEnded` under
`Current Sensing` with a warning. Local MCSDK `ConnectionParameters.json`
maps G4 `ThreeShunt_RawCurrents_SingleEnded` to internal/external OPAMP
variants. The current PCB2 clue is therefore not accepted as an internal
OPAMP/PGA route: `PA4` is not an OPAMP VINP in the local Workbench MCU asset,
and `PA5` is not a matching non-inverting current input for the required
three-shunt internal-gain route.

This does not prove the physical current-sense circuit is wrong. It proves
that the current saved Board Designer representation is not accepted by
Workbench as a FOC current-sense configuration.

## OPAMP adapter candidate

A second no-power candidate board was created and installed locally:

- Repo source:
  `QIANSAI_STDRIVE101_TIM1_OPAMP_ADAPTER_POWER.no_power_candidate_2026-05-20.json`
- Workbench user-board install:
  `C:\Users\gregrg\.st_workbench\hardware\board\power\QIANSAI_STDRIVE101_TIM1_OPAMP_ADAPTER_POWER.json`
- SHA256:
  `2FE6319BED061B1CE5CC426CFC59BD17A065C0DE6E19A33766C854E96528126E`

It keeps the same TIM1 PWM and `PB12/TIM1_BKIN` nFAULT route. The power-board
side remains `ThreeShunt_RawCurrents_SingleEnded`, while the selected morpho
pins are chosen so Workbench can try to map the route onto G474 internal
OPAMP/PGA-compatible inputs:

| Signal | Connector | MCU pin | OPAMP clue |
| --- | --- | --- | --- |
| `CURRENT_SHUNT_UP` | `ML30` | `PA1` | `OPAMP1 VINP` |
| `CURRENT_SHUNT_VP` | `MR15` | `PA7` | `OPAMP1/OPAMP2 VINP` |
| `CURRENT_SHUNT_WP` | `ML34` | `PB0` | `OPAMP2/OPAMP3 VINP` |

This candidate is not current PCB2 proof. It requires adapter, flying-wire, or
PCB rework before any hardware use. It also conflicts with the current PCB2
Hall clue because current PCB2 records `PA1` as part of the `PA0/PA1/PB4`
software-Hall route.

Initial GUI search did not show the candidate because the first JSON revision
used `ThreeShunt_RawCurrents_SingleEnded_InternalGain` directly on a power
board, which can be filtered by Workbench. The source was corrected to use the
power-board-side `ThreeShunt_RawCurrents_SingleEnded` type, keeping the
`PA1/PA7/PB0` OPAMP/PGA candidate route. The next no-power GUI action is to
restart Workbench, select `QIANSAI_STDRIVE101_TIM1_OPAMP_ADAPTER_POWER`, and
stop at the summary before `Create`.

## Short-name alias after GUI search miss

The user reported that searching `OPAMP` in the Workbench GUI still did not
show `QIANSAI_STDRIVE101_TIM1_OPAMP_ADAPTER_POWER`. A read-only API check
against the running Workbench instance confirmed that the long-name candidate
was present in `http://localhost:8009/api/hardware/usr/power`, so the issue is
treated as a GUI search/filter visibility problem rather than a missing
Workbench user-board file.

A short-name no-power alias was added and installed:

- Repo source:
  `QS_TIM1_OPAMP_PWR.no_power_candidate_2026-05-20.json`
- Workbench user-board install:
  `C:\Users\gregrg\.st_workbench\hardware\board\power\QS_TIM1_OPAMP_PWR.json`
- Workbench app-asset install:
  `F:\STMCSDK\MC_SDK_6.4.2\Utilities\PC_Software\STMCWB\assets\hardware\board\power\QS_TIM1_OPAMP_PWR.json`
- SHA256:
  `79BABB221D6F488FB63B79E73B62B9500CEC19BDE96D9FCCB7308A2882B00141`

Workbench API and log evidence show the alias is visible to the running
Workbench backend. It first appeared in the user-board API; after the GUI still
did not show it, the app-asset copy was added and Workbench was restarted. The
app power-board API then listed it as a normal power-board asset:

```text
name                  PN                 shortDescription
QS_TIM1_OPAMP_PWR     QS-TIM1-OPAMP-PWR  QS TIM1 OPAMP PWR

loading Json User Hardware: QS_TIM1_OPAMP_PWR.json
successfully parsed User Hardware: QS_TIM1_OPAMP_PWR.json

loading assets Hardware: QS_TIM1_OPAMP_PWR.json
successfully parsed assets Hardware: QS_TIM1_OPAMP_PWR.json
```

The alias uses the same no-power TIM1 PWM, `PA1/PA7/PB0` OPAMP/PGA candidate
current-sense route, and `PB12/TIM1_BKIN` nFAULT route as the long-name
candidate. It is still only an adapter/rework candidate, not current PCB2
as-built proof.

## Screenshot Evidence

Additional screenshots captured under `screenshots/`:

- `2026-05-20_workbench_tim1_adapter_board_select_page.png`
- `2026-05-20_workbench_tim1_adapter_after_power_confirm.png`
- `2026-05-20_workbench_tim1_adapter_components_after_control_motor.png`
- `2026-05-20_workbench_tim1_adapter_summary_after_components.png`
- `2026-05-20_workbench_tim1_adapter_current_sensing_redx_detail.png`
- `2026-05-20_workbench_power_change_attempt_after_plus.png`

## Decision

`Partial clue / PWM compatibility solved in GUI / current sensing still blocked`.

Packet A is still not accepted. The next candidate to test in the GUI is the
short-name `QS_TIM1_OPAMP_PWR` board from a fresh Workbench `New Project` path.
Even if Workbench marks it green later, it remains an adapter/rework candidate
until board-route evidence and no-power continuity checks prove the physical
path.
