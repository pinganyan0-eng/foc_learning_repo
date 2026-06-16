# No-Power Boundary Reference

Use this reference before hardware-adjacent answers, CubeMX/MCSDK/Workbench
discussion, DMM/Hall/PWM/motor topics, generated-source interpretation, or
build-evidence interpretation.

## Current Boundary

Current project stage is P2 MCSDK no-power precheck. The local MCP status
records `mcsdk_motorcontrol_trust: blocked`.

The repo can currently support no-power planning artifacts, generated-source
review, interface review, host-side checks, and build-only records. It cannot
support powered behavior, motor behavior, Hall closed-loop behavior, or
sensorless behavior.

## Forbidden Actions And Claims

Unless a later dated phase-gate decision opens the action:

- No flash.
- No 24V.
- No power-board connection.
- No motor connection.
- No Gate PWM output.
- No Motor Profiler run.
- No Motor Pilot run.
- No Hall closed-loop claim.
- No sensorless / SMO claim.
- No powered readiness, motor readiness, or power-stage readiness claim.

Do not treat DMM pending as a passed result. Do not infer continuity, soldering
quality, protection behavior, runtime GPIO behavior, PWM safety, or motor
readiness from a config file, source snapshot, build, screenshot, or retrieval
hit.

## Current PCB2 / Hall Constraints

- Current Hall planning route: `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`.
- `PB3=LIN1` and is not current PCB2 Hall.
- `P14/P15=3V3/GND`.
- PCB2 is reported populated / in hand, but DMM continuity and short-check
  evidence is still pending.
- DMM work, when requested by the user, must remain board-unpowered and must
  record raw readings or beep states rather than conclusion-only summaries.

## Hardware-Adjacent Answer Pattern

When hardware risk is involved, answer in this order:

1. State the current no-power boundary.
2. Name the exact evidence the repo has and does not have.
3. Provide no-power checks or source-review steps first.
4. Require current limits, measurement points, rollback path, and phase-gate
   evidence before any later powered step.
5. Separate "planning evidence", "build evidence", "measurement evidence", and
   "powered validation".

## ISR / Real-Time Hard Stops

In JEOC, FOC ISR, Hall edge ISR, and other timing-critical paths, prohibit:

- `printf`
- `HAL_Delay`
- JSON parsing
- WebSocket work
- dynamic allocation
- blocking I/O
- long loops or long conditional processing

For future software Hall design, keep the edge ISR to raw state, timestamp, and
event counter capture only. State-machine classification belongs in a
lower-priority context unless a later reviewed design says otherwise.
