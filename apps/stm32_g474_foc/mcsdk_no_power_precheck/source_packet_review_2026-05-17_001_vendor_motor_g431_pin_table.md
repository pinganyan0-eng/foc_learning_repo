# P2 Source Packet Review - 2026-05-17-001 - Vendor Motor And G431 Pin Table

Review template source:
`source_packet_review_template_2026-05-14.md`.

This review covers two newly provided no-power source clues:

- vendor motor-parameter image for `57BLF01`;
- hardware teammate PDF pin-assignment table titled for `STM32G431RB`.

## Packet Metadata

| Field | Value |
| --- | --- |
| Review ID | `P2-SOURCE-REVIEW-2026-05-17-001` |
| Packet type | Packet A/B preparation clue |
| Motor source | `hardware/motor/2026-05-17_vendor_57blf01_motor_parameters.jpg` |
| Motor note | `hardware/motor/2026-05-17_vendor_57blf01_motor_parameters.md` |
| Pin table source | `hardware/schematic/2026-05-17_stm32g431rb_pin_assignment_hw_teammate.pdf` |
| Pin table note | `hardware/schematic/2026-05-17_stm32g431rb_pin_assignment_hw_teammate.md` |
| MCU pin cross-check | `mcu_pin_compatibility_check_2026-05-17.md` |
| Provided by | User; pin table attributed to hardware teammate; motor data attributed to seller. |
| User caveat | Not guaranteed 100% correct; `J_HALL` pin numbering is uncertain. Hardware teammate says the G431/G474 pins used by the table are the same. |

## Extracted Motor Facts

| Field | Extracted value | Decision |
| --- | --- | --- |
| Model | `57BLF01` | Candidate vendor clue. |
| Phase count | `3` | Candidate vendor clue. |
| Rated voltage | `24 VDC` | Candidate vendor clue. |
| Rated speed | `3000 rpm` | Candidate vendor clue. |
| Rated / holding torque | `0.2 N-m` | Candidate vendor clue. |
| Output power | `63 W` | Candidate vendor clue. |
| Peak torque | `0.6 N-m` | Candidate vendor clue. |
| Peak current | `9.6 A` | Candidate vendor clue; not a power-stage current-limit setting. |
| Line resistance | `0.6 ohm` | Candidate vendor clue; not a project DMM measurement. |
| Line inductance | `0.75 mH` | Candidate vendor clue; not a project LCR measurement. |
| Back EMF | `6.23 V/kRPM` | Candidate vendor clue. |
| Pole count | `4` | Ambiguous; if it means total poles, MCSDK pole pairs would be `2`, but this is not accepted yet. |

Workbench label decision: if Workbench requires a motor entry, use
`57BLF01_VENDOR_CANDIDATE` rather than the old
`PLACEHOLDER_not_profiled_2026-05-16`. This is a better label, not measured
motor proof.

## Extracted Pin Table Facts

The PDF records a structured mapping for `STM32G431RB NUCLEO`, STDRIVE101, and
3-shunt current sensing. The user added that the hardware teammate says these
G431/G474 pins are the same. A local MCSDK asset check compared
`STM32G431RBTx.json` with `STM32G474RETx.json` and confirmed the same relevant
pin positions and signal functions for the key rows:

- TIM1 complementary PWM candidates: `PA8`, `PB13`, `PA9`, `PB14`, `PA10`,
  `PB15`;
- fault candidate: `PB12 / TIM1_BKIN`;
- current-sense candidates: `PA1/PA0`, `PA7/PA3`, `PB0/PB1`;
- Hall candidates: `PA15`, `PB3`, `PB10`;
- VCP policy: keep `PA2/PA3` for NUCLEO VCP;
- SWO conflict: `PB3` remains blocked until SWO release / isolation evidence;
- signal supply clues: `3V3` and `GND_SIGNAL`.

## Review Decision

Overall decision: `Partial clue`.

Accepted from this source:

- the repo now has archived source files for the supplier motor parameter table
  and the hardware teammate pin table;
- `57BLF01` is the current vendor-candidate motor identity for no-power
  Workbench naming;
- the pin table provides a concrete candidate map to compare against
  Workbench/CubeMX and the current board route evidence.
- the G431-to-G474 pin-function compatibility concern is reduced for the
  compared key rows: TIM1 PWM, `PB12/TIM1_BKIN`, TIM2 Hall candidates,
  `PA2/PA3`, and OPAMP-related current-sense candidates.

Still not accepted:

- measured motor parameters;
- pole-pair count for MCSDK;
- current limits, PI parameters, Ke, Ls, Rs, or Hall angle;
- unreviewed `STM32G431RB` rows outside the compared key set as direct
  `STM32G474RETx` proof;
- CN8 endpoint proof;
- `J_HALL` pin numbering;
- `PB3` Hall B readiness;
- OPAMP2 internal-output feasibility;
- generated-project trust.

## Forbidden Conclusions

Do not claim from these sources that:

- Do not claim Motor Profiler data exists;
- Do not claim the motor has been tested or is ready to run;
- Do not claim Hall wiring or Hall closed-loop behavior is validated;
- Do not claim the G431 table proves CN8 routing, J_HALL numbering, or the final G474
  board-level pinout;
- Do not claim CN8 routing is accepted;
- Do not claim STDRIVE101 protection paths are accepted;
- Do not claim build-only, flash, power, Gate PWM, or motor actions are allowed.

## Required Follow-Up

1. Compare the PDF pin candidates against the actual Workbench/CubeMX
   `NUCLEO-G474RE` configuration before accepting any Packet A selected field.
2. Confirm `J_HALL` connector pin numbering from board source or continuity
   evidence before using Hall mapping.
3. Confirm whether motor "magnetic pole count 4" means total poles or pole
   pairs.
4. Fill no-power motor photo, wire-color, and DMM resistance records before
   treating the motor source as anything more than a vendor clue.
5. Keep generated-project trust `Not allowed` until Packet A selected fields
   are accepted.
