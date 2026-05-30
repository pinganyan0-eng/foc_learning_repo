# Motor No-Power Measurement Log - 2026-05-16

This file records low-risk motor information that can be collected with the
motor unpowered and disconnected from all electronics.

It is not Motor Profiler data, not a Hall validation, not a PI tuning input,
and not permission to run the motor.

## Safety Boundary

- Motor disconnected from the power board.
- Motor disconnected from NUCLEO.
- No 24V.
- No bench supply.
- No Motor Profiler.
- No spinning command.
- Hall wires are identified visually only; do not power Hall sensors in this
  step.

## Identity

| Field | Value |
| --- | --- |
| Motor model / marking | Vendor candidate `57BLF01`; physical marking photo still TBD. |
| Vendor / source | Supplier parameter image, candidate only |
| Nameplate photo path | `hardware/motor/2026-05-17_vendor_57blf01_motor_parameters.jpg` is vendor data, not a physical nameplate photo taken by the project. |
| Harness photo path | `hardware/motor/2026-05-18_57blf01_motor_wiring_definition.jpg` is a wiring-definition image, not a project physical harness photo. |
| Measurement date | 2026-05-16 / 2026-05-18 source intake |
| Instrument | Digital multimeter |
| Instrument model | TBD |
| Ambient note | TBD |

## Vendor Parameter Clue

The supplier image is archived at:

`hardware/motor/2026-05-17_vendor_57blf01_motor_parameters.jpg`

Extracted review note:

`hardware/motor/2026-05-17_vendor_57blf01_motor_parameters.md`

| Field | Supplier value | Status |
| --- | --- | --- |
| Model | `57BLF01` | Candidate |
| Magnetic pole count | `4` | Candidate; pole-pair interpretation must be confirmed. |
| Phase count | `3` | Candidate |
| Rated voltage | `24 VDC` | Candidate |
| Rated speed | `3000 rpm` | Candidate |
| Output power | `63 W` | Candidate |
| Peak current | `9.6 A` | Candidate; not a powered current-limit setting. |
| Line resistance | `0.6 ohm` | Supplier clue only. |
| Line inductance | `0.75 mH` | Supplier clue only. |
| Back EMF | `6.23 V/kRPM` | Supplier clue only. |

If Workbench requires a motor entry before saving, use
`57BLF01_VENDOR_CANDIDATE` as the no-power vendor-candidate label. Do not treat
that label as measured motor proof.

## Vendor Wiring Definition Clue

The user-provided wiring image is archived at:

`hardware/motor/2026-05-18_57blf01_motor_wiring_definition.jpg`

Extracted review note:

`hardware/motor/2026-05-18_57blf01_motor_wiring_definition.md`

This is still source-clue data, not project measurement.

| Wire group | Image label | Color | Status |
| --- | --- | --- | --- |
| Phase | U | Yellow | Candidate image clue |
| Phase | V | Red | Candidate image clue |
| Phase | W | Black | Candidate image clue |
| Hall | `HU` | Yellow | Candidate image clue |
| Hall | `HV` | White | Candidate image clue |
| Hall | `HW` | Blue | Candidate image clue |
| Hall supply | `H+` / `+5V` | Red | Candidate image clue; do not power in P2 |
| Hall return | `H-` / `GND` | Black | Candidate image clue; do not power in P2 |

## Wire Color Record

| Wire group | Color / label | No-power observation |
| --- | --- | --- |
| Phase U candidate | Yellow thick wire | Vendor wiring image clue only; verify on actual harness. |
| Phase V candidate | Red thick wire | Vendor wiring image clue only; verify on actual harness. |
| Phase W candidate | Black thick wire | Vendor wiring image clue only; verify on actual harness. |
| Hall VCC candidate | Red thin wire, `H+` / `+5V` | Vendor wiring image clue only; do not power in P2. |
| Hall GND candidate | Black thin wire, `H-` / `GND` | Vendor wiring image clue only; do not power in P2. |
| Hall A / `HU` candidate | Yellow thin wire | Vendor wiring image clue only; project `HA/HU` mapping still needs later confirmation. |
| Hall B / `HV` candidate | White thin wire | Vendor wiring image clue only; project `HB/HV` mapping still needs later confirmation. |
| Hall C / `HW` candidate | Blue thin wire | Vendor wiring image clue only; project `HC/HW` mapping still needs later confirmation. |

## Phase Resistance Record

Before measuring the motor, short the meter probes together and record the
residual lead resistance.

| Measurement | Raw reading | Meter range | Probe short residual | Corrected clue | Status |
| --- | --- | --- | --- | --- | --- |
| Probe short | TBD | TBD | TBD | N/A | TBD |
| U-V | TBD | TBD | TBD | TBD | TBD |
| V-W | TBD | TBD | TBD | TBD | TBD |
| W-U | TBD | TBD | TBD | TBD | TBD |

## Interpretation Rules

- If the three phase-to-phase readings are close, record them as a low-grade
  symmetry clue only.
- If one reading is clearly different, mark the motor or wire labeling as
  suspect and do not use the values in Workbench.
- If readings are near the meter's low-ohm limit, keep them as low-precision
  clues only.
- Do not derive `Rs`, `Ls`, `Ke`, Hall angle, PI gains, current limits, or
  speed-loop parameters from this file.

## Current Decision

No measured motor-control parameter is accepted yet. Workbench may use a
vendor-candidate motor label only until a later accepted measurement or
Profiler stage exists. The 2026-05-18 wiring definition image adds candidate
wire-color clues only; it does not prove physical harness inspection,
continuity, Hall power behavior, phase/Hall alignment, or `J_HALL` numbering.
