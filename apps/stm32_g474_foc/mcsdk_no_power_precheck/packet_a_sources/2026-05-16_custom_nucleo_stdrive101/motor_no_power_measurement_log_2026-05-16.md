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
| Motor model / marking | TBD |
| Vendor / source | TBD |
| Nameplate photo path | TBD |
| Harness photo path | TBD |
| Measurement date | 2026-05-16 |
| Instrument | Digital multimeter |
| Instrument model | TBD |
| Ambient note | TBD |

## Wire Color Record

| Wire group | Color / label | No-power observation |
| --- | --- | --- |
| Phase U candidate | TBD | Visual only. |
| Phase V candidate | TBD | Visual only. |
| Phase W candidate | TBD | Visual only. |
| Hall VCC candidate | TBD | Visual only; do not power. |
| Hall GND candidate | TBD | Visual only; do not power. |
| Hall A candidate | TBD | Visual only; do not power. |
| Hall B candidate | TBD | Visual only; do not power. |
| Hall C candidate | TBD | Visual only; do not power. |

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
placeholder motor name only until a later accepted measurement or Profiler
stage exists.
