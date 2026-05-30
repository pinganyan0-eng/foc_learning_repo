# 2026-05-12 P1 Catch-up Delivery Pack

## Summary

- Period / phase: P1-S1, NUCLEO basics and UART command handling.
- Corresponding original plan: Week 1, reduced to safe NUCLEO-only firmware practice.
- Current real stage: NUCLEO baseline command path is validated over COM5; P1 teaching artifacts are now packaged.
- Pace at package creation: catch-up, not yet on-track.
- 2026-05-13 update: learner independently passed the P0 STOP and DMA `Size` transfer checks, completed current-layer command/callback concept checks, and verification commands passed. P2 MCSDK no-power precheck may now be treated as the next candidate lesson, still with no 24V, no power board, no motor, no PWM Gate, and no real Motor Profiler run.

## Submitted Artifacts

| Artifact | Path | Status |
| --- | --- | --- |
| UART command classification and side-effect table | `docs/05_test_and_logs/week1_nucleo_baseline.md` | packaged |
| DMA + IDLE receive flow and `Size` rule | `docs/04_iot_gateway/uart_dma_idle.md` | packaged |
| COM5 serial validation evidence | `experiments/2026-05-09_nucleo_baseline/logs/2026-05-12_com5_set_rpm_validation.md` | validated |
| Mastery / gap map | `learning/MASTERY_MAP.md` | active |
| Review queue | `learning/review_queue.md` | active |
| Sprint tracker | `workflow/current_learning_sprint.md` | active |

## What Is Proven

- `PING` and `MODE?` are read-only commands in the NUCLEO baseline.
- `ARM` is accepted only from `IDLE` and increments `mode_change_count` only when the state changes.
- `SET_RPM` rejects parse errors, range errors, and `IDLE` state; it updates only a simulated `target_rpm` in `ARMED` / `RUN_SIM`.
- `STOP` always clears `target_rpm`; it changes `app_mode` and increments `mode_change_count` only when the previous mode was not `IDLE`.
- COM5 evidence proves the NUCLEO command/guard path, not motor-control behavior.

## Learner Evidence

Use `learning/MASTERY_MAP.md` as the source of truth:

- Demonstrated: baseline serial observation, basic state-machine idea, `strcmp(...) == 0` command matching, guided `Size` count/index repair, and `SET_RPM` guard reasoning.
- 2026-05-13 update: current-layer STOP, ARM, MODE?, command side-effect reading, DMA `Size`, and DMA + IDLE callback flow checks are recorded as passed in `learning/session_notes.md` and `learning/MASTERY_MAP.md`.

## Open Weak Points

At package creation, the P0 checks were:

1. Predict final `mode`, `target_rpm`, and `mode_change_count` for `ARMED,target_rpm=1200,count=5 + STOP`.
2. Compare with `IDLE,target_rpm=1200,count=5 + STOP`.
3. Explain why `Size = 10` means process `rx_buf[0..9]`.
4. State the loop condition: `i < Size`.

2026-05-13 update: these P0 checks have now passed. Use `learning/NEXT_LESSON.md` for the next P2 no-power precheck candidate.

## Progress Debt

- The teaching artifacts are now in the repo, and the learner has independently passed the final P0 transfer check after packaging.
- DMA + IDLE is documented and conceptually connected to `AppFeedRxByte(...)`, but firmware has not yet been changed to real `HAL_UARTEx_ReceiveToIdle_DMA(...)`.
- No MCSDK motor-control project, Motor Profiler result, Hall run, power-board waveform, CORDIC/FMAC profile, SMO result, or ESP32 real gateway validation exists yet.

## Next Goal

Next teaching turn:

1. Start from `learning/NEXT_LESSON.md`.
2. Do not repeat low-value P1 drills unless a new mistake appears.
3. Move to P2 MCSDK no-power precheck candidate: tool roles, no-power artifacts, Motor Profiler plan only, and risk/no-go checklist.
4. Keep the safety boundary explicit and do not claim any MCSDK, Motor Profiler, Hall, power-board, or motor-control validation yet.

## Forbidden Scope

- No 24V.
- No power board.
- No motor.
- No PWM Gate.
- No Motor Profiler.
- No Hall closed-loop.
- No SMO.
- No claim that `SET_RPM` controls real speed.
