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

## Current Hardware Phrase Route

As of 2026-06-19, if the user says `开始单输入唤醒诊断`, `单输入唤醒`,
`STDRIVE101 唤醒`, or `REG12 唤醒`, treat it as the STDRIVE101
single-input wake diagnostic, not Codex mobile wakeup, CodexMobileWeb,
service wakeup, or automation wakeup.

Read these project files before giving steps:

- `AI_CONTEXT.md`
- `workflow/CURRENT_SNAPSHOT.md`
- `workflow/ACTIVE_TASK.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_reg12_single_input_wake_plan_2026-06-19.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_reg12_wake_official_web_review_2026-06-19.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/out1_output_node_no_power_short_check_result_2026-06-19.md`

The bounded diagnostic candidate is:

```text
CN3_14 / 3V3 -> 10 kohm series resistor -> CN3_2 / LIN1
HSPY: 24 V / 0.2 A
Motor: disconnected
No firmware PWM
No Motor Pilot / Profiler
```

This route still does not authorize motor connection, PWM validation,
Hall closed-loop, sensorless operation, power-stage readiness, or motor
readiness claims.

## Hardware Stage Sync Guard

Before any hardware-adjacent next-step answer, separate:

- repo snapshot;
- user's latest现场确认;
- raw measurement evidence.

If the repo snapshot and the user's latest现场确认 disagree, state the conflict
before giving a checklist. Do not silently fall back to an older repo gate. Use
the user's latest现场确认 only as the working stage for the next bounded
measurement, not as proof that the stage passed.

For example, if local status still says `DMM pending` but the user says `CN3 已
连接 + B1 不按 + 24V/0.2A 限流静态电源/nFAULT 检查`, treat the repo status as
possibly stale, repeat that现场 stage, and limit the response to static
power/nFAULT readings with current-limit and rollback rules. Do not claim
continuity, power-stage readiness, Hall readiness, motor readiness, or powered
validation without raw readings.

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
