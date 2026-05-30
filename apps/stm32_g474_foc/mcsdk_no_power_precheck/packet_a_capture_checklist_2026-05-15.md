# Packet A Capture Checklist - 2026-05-15

This checklist defines the next acceptable no-power capture for Packet A:
MCSDK / MotorControl configuration evidence.

It is not a build instruction, not a wiring instruction, not a profiler
procedure, and not hardware validation.

## Safety Boundary

- No 24V.
- No power-board connection.
- No motor connection.
- No Gate PWM output.
- No Motor Profiler run.
- No Hall closed-loop claim.
- No sensorless / SMO claim.

## Accepted Capture Types

One of these is enough to create a Packet A review record:

1. Real Workbench project file: `.stwb6` for MCSDK 6.x, or legacy `.stmcx`.
2. MotorControl / Workbench configuration screenshot.
3. Exact reproducible GUI launcher path plus captured version/config screen.

Generated MCSDK source without the matching Workbench project file or
configuration screen is not accepted as Packet A proof.

## Required Fields

| Field | Must be visible or recorded | Current policy |
| --- | --- | --- |
| MCU / board context | MCU, package, and NUCLEO/custom-board context. | Target remains `STM32G474RETx` unless a later source proves a different final context. |
| PWM / timer | TIM1 complementary PWM choices or explicit Workbench output mode. | Planning only; no Gate PWM output. |
| Fault input | Break/fault input selection. | Draft preference remains `PB12/TIM1_BKIN` unless a safer final source is proven. |
| Current sensing | 3-shunt / OPAMP / ADC selection. | Planning only; no current measurement claim. |
| Motor entry | Motor name and source if Workbench requires a motor selection. | Prefer `57BLF01_VENDOR_CANDIDATE` as a supplier-clue label; do not treat vendor values as measured Motor Profiler data. |
| Hall / sensorless | Hall choice, sensorless choice, or explicit absence. | No Hall validation and no SMO validation. |
| Debug / UART | Whether `PA2/PA3` are excluded or reused. | Default exclude from FOC UART until MCSDK/CubeMX proves reuse is safe. |
| `PB3` ownership | SWO or Hall B decision. | Blocked until SWO release/isolation evidence exists. |
| Tool/version context | Workbench/CubeMX/MCSDK version or visible project metadata. | Needed for repeatability and defense material. |

## Screenshot Storage

Store captures under:

`apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/`

For the 2026-05-16 custom NUCLEO + STDRIVE101 capture, store the `.stwb6`,
guide, pin table, motor no-power log, and screenshots under:

`apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/`

Use clear names such as:

- `2026-05-15_motorcontrol_project_context.png`
- `2026-05-15_motorcontrol_pwm_fault_current_sense.png`
- `2026-05-15_motorcontrol_hall_uart_pb3.png`

If a `.stwb6` or `.stmcx` is saved, place it under a dated Packet A directory
or the P2 no-power directory, and keep the original filename if it contains
project meaning.

## Review Procedure After Capture

1. Create a dated review from `source_packet_review_template_2026-05-14.md`.
2. Mark each required field `Accepted`, `Partial clue`, or `Blocked`.
3. Update `evidence_packet_2026-05-14.md` only for the fields visible in the
   source.
4. Update `workflow/evidence_register.md` with limits and forbidden claims.
5. Keep Packet B/C, `DT/MODE`, `STBY`, STM32 endpoint mapping, and PB3/SWO
   blockers unchanged unless separate accepted evidence exists.
6. Run `python -m unittest discover -s tests`.

## Rejected As Packet A Proof

- CubeMX home screenshot only.
- CubeMX `Pinout & Configuration` screenshot without MotorControl settings.
- NUCLEO `.ioc` readback by itself.
- Oral description of the GUI.
- Generated source without matching Workbench project file or configuration
  screen.
- Any capture taken during powered hardware, Motor Profiler, Gate PWM, Hall
  closed-loop, or sensorless operation.

## Current Decision

This checklist supplements Packet A. After the 2026-05-15 follow-up,
`My_First_FOC.stwb6` remains preserved as a legacy source candidate, but only
as `Partial clue`.

After the 2026-05-16 follow-up, the new custom NUCLEO + STDRIVE101 capture
package is prepared at
`packet_a_sources/2026-05-16_custom_nucleo_stdrive101/`. It is also only
`Partial clue / Preparation only` until a real `.stwb6` and Workbench GUI pages
show the selected PWM, fault, current-sense, Hall/sensorless, UART, and `PB3`
choices.

After the 2026-05-17 follow-up, supplier motor parameters and a hardware
teammate `STM32G431RB` pin table are archived and reviewed as `Partial clue`.
The hardware teammate states the relevant G431/G474 pins are the same, and the
local MCSDK asset comparison supports the compared key rows. This reduces the
MCU pin-function concern, but it still does not confirm CN8 routing, `J_HALL`
numbering, `PB3` SWO release, OPAMP2 internal-output feasibility, or any
measured motor parameter.
