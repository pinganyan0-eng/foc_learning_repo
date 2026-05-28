# Current Snapshot

Last updated: 2026-05-28

This is the short current-state page for low-token AI handoff. It summarizes
the current project stage and safety boundary. Historical detail remains in
`CURRENT_STATUS.md`.

## Current Stage

- Main project: STM32G474 edge-gateway FOC drive learning and competition
  project.
- Current stage: P2 MCSDK no-power precheck and software Hall no-power
  firmware-entry planning.
- No-power build-only status: Debug build command completed with exit code `0`
  on 2026-05-27 for
  `QIANSAI_G474_STDRIVE101_FOC_P2`; this is local compile evidence only.
- Strategy: use ST MCSDK for the motor-control framework, keep Hall
  closed-loop as the safe fallback path, and treat SMO/PLL sensorless as a
  later stretch goal.
- Real-time boundary: STM32 owns FOC. ESP32-C3 displays, forwards, and alerts
  only.

## Current PCB2 Route

- Current Hall planning route: `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`.
- `PB3=LIN1` and is not current PCB2 Hall.
- `P14/P15=3V3/GND`.
- PCB2 is still unpopulated, so DMM continuity / short-check evidence is
  hardware-side deferred. Deferred does not mean passed.

## Current Software Hall State

- Host-side and document-side no-power software Hall preparation exists:
  state-machine rules, pseudocode, host model, golden vectors, MCSDK integration
  clues, firmware-entry checklist, GPIO/EXTI boundary review,
  timestamp-source review, debug-output route review, MCSDK firmware-integration boundary review, and MCSDK hook evidence request checklist.
- A Chinese-first no-power firmware-entry plan now exists at
  `software_hall_firmware_entry_plan_2026-05-28.md`. It locks
  `PA0/PA1/PB4` as the future software GPIO/EXTI Hall route, keeps
  `PB3=LIN1` out of Hall, defines the debug-only adapter layers, state-machine
  order, ISR limits, debug fields, MCSDK hard stops, and user checkpoint.
  Decision:
  `Software Hall firmware-entry plan / debug-only no-power boundary / no firmware implementation / no MCSDK hook / no Hall readiness`.
- The external Workbench project
  `C:\Users\gregrg\.st_workbench\projects\QIANSAI_G474_STDRIVE101_FOC_P2`
  exists and its generated `Src/`, `Inc/`, `cmake/`, and top-level build
  metadata are now archived as
  `packet_a_sources/2026-05-27_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot/`
  with a manifest, hash list, and source review.
- A read-only MCSDK speed / position feedback interface review now exists at
  `software_hall_mcsdk_speed_position_feedback_interface_review_2026-05-27.md`.
  It traces `HALL_M1`, `HALL_CalcAvrgMecSpeedUnit`, `STC_GetSpeedSensor`,
  `SPD_GetAvrgMecSpeedUnit`, and `SPD_GetElAngle`, and records that future
  software Hall must remain debug-only unless a separate reviewed
  `SpeednPosFdbk`-compatible component proposal is created.
- No-power build-only result now exists at
  `build_only_result_2026-05-27_qiansai_g474_stdrive101_foc_p2_debug.md`.
  It records `cmake --build ... --config Debug`, exit code `0`, `ninja: no
  work to do`, and `.elf` / `.map` artifacts from the external Workbench build
  directory.
- These are no-power planning and host-model evidence only.
- They do not prove GPIO runtime behavior, MCSDK Hall integration, MCSDK hook
  readiness, DMM continuity, Hall closed-loop behavior, flash readiness, or
  powered readiness.

## Current AI Architecture Work

- This repository now treats AI assistance as an evidence-first workflow:
  short context, grounded retrieval, one active task, explicit safety boundary,
  contract checks, and evidence records.
- `docs/00_project_truth/ai_architecture.md` is the architecture contract.
- `tools/build_context_pack.py` is the first low-token context-pack generator.
- `tools/check_ai_contracts.py` is the first no-power workflow consistency
  checker.
- Dual-teacher concept-only role guard is now explicit: ChatGPT teaches pure
  theory/concept turns, while Codex provides the ChatGPT prompt, reviews and
  records returned learning evidence, and keeps repo-side engineering work.

## Current Safety Boundary

Unless a later dated phase-gate decision explicitly opens the action:

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

Current Packet A and software Hall artifacts may be accepted only as no-power
configuration, planning, host-model, or generated-source clues. They do not
prove PCB2 physical routing, continuity, protection behavior, firmware runtime
behavior, or powered behavior.

## Default Read Order

1. `AI_CONTEXT.md`
2. `workflow/CURRENT_SNAPSHOT.md`
3. `workflow/ACTIVE_TASK.md`
4. `docs/00_project_truth/project_context.md`
5. Mode-specific files named by `tools/build_context_pack.py`

Open `CURRENT_STATUS.md`, `workflow/evidence_register.md`, historical Packet
records, manuals, and generated directories only for concrete evidence,
hardware-safety, phase-gate, or implementation tasks.
