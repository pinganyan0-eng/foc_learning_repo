# Current Learning Sprint

Last updated: 2026-05-13

This is the short execution layer for the current teaching plan. It turns the long B algorithm delivery plan into a concrete sprint with deliverables, review priority, and exit criteria.

## Sprint Identity

- Sprint ID: P2-S1-MCSDK-NO-POWER-PRECHECK
- Stage: P2 MCSDK no-power precheck.
- Status: in progress. P1 concept-layer checks are passed, and the first P2 artifact now contains a tool/version status table, baseline `.ioc` readback, pin/config draft, local ST PDF mirror note, online ST source cross-check, pin-function conflict resolution pass, shell GUI evidence probe, and expanded future Motor Profiler stop plan.
- Owner split: ChatGPT teaches tool roles and safety boundaries; Codex writes artifacts, verifies files, records evidence, and keeps unsafe hardware actions blocked.
- Safety boundary: no 24V, no power board, no motor, no PWM Gate, no real Motor Profiler run, no Hall closed-loop, no SMO claim, and no claim that `SET_RPM` controls real speed.

## Why This Sprint

P1 NUCLEO UART command handling and DMA + IDLE concept checks are recorded as passed. The next useful move is no longer more verbal review of STOP/DMA basics; it is creating the P2 no-power artifact set that will let the team approach MCSDK safely.

The first P2 card now exists at `deliverables/2026-05-13_p2_mcsdk_no_power_precheck.md`. It deliberately found and preserved configuration conflicts instead of hiding them:

- `PA2/PA3` are convenient for P1 ST-LINK VCP but conflict with OPAMP/PGA planning.
- `PC5` appeared as both a V9 nFAULT candidate and an OPAMP2 feedback-related pin; the official pin-function pass now rejects `PC5` and prefers `PB12/TIM1_BKIN` as the draft nFAULT candidate.
- `PB3` is current SWO in the baseline but a Hall B candidate in V9; the current policy is to keep SWD and release/isolate SWO if Hall B stays on `PB3/TIM2_CH2`.
- V-phase low-side PWM differs across materials (`PB14` in V9, `PA12` in older notes); the current draft prefers `PB14/TIM1_CH2N` and treats `PA12` only as a board-routing alternate.
- Frequently used ST PDFs are mirrored under `materials/raw/st_manuals/`, including `st_stdrive101_datasheet` for STDRIVE101 gate-driver protection review.

## Required Deliverables

| Deliverable | Target File | Current Status | Done When |
| --- | --- | --- | --- |
| P2 no-power precheck card | `deliverables/2026-05-13_p2_mcsdk_no_power_precheck.md` | in progress | Card includes tool roles, allowed/forbidden scope, tool/status table, baseline `.ioc` readback, pin/config draft, official-source cross-check, conflict resolution pass, Motor Profiler plan, and risk/no-go checklist. |
| Tool version/status evidence | same card plus `workflow/windows_toolchain_status.md` | partially filled | Local evidence states what is available, what is missing from PATH, and what still needs GUI screenshot or exact path proof. |
| ST official local mirror | `materials/raw/st_manuals/`, `references/st_manuals_index.md` | filled, including STDRIVE101 | Frequently used ST PDFs are repo-local, indexed, hash-recorded, and paired with extracted text for retrieval. |
| Workbench/CubeMX config evidence | future screenshot or `.stmcx` placeholder | blocked on GUI/user evidence | A real GUI screenshot or `.stmcx` placeholder is captured without running Motor Profiler or touching power hardware. Current shell probe did not find a Workbench executable path or existing `.stmcx`. |
| Pin/config conflict resolution | same card, then future config file | partially resolved | `PA2/PA3`, `PC5`/nFAULT, `PB3`, and V low-side PWM conflicts are resolved at pin-function policy level; CubeMX/Workbench and board-routing evidence still must confirm the choices. |
| Motor Profiler plan | same card or a later P3 plan file | expanded for future P3 | Plan lists required hardware, current limit, motor information, stop conditions, abort criteria, instrument/log needs, and rollback path; no live profiler run occurs in P2. |
| Evidence register and submission checklist | `workflow/evidence_register.md`, `deliverables/submission_checklist.md` | updated for first P2 card | P2 planning evidence is registered without overstating it as MCSDK, Hall, power, or motor validation. |

## Review Priority

1. P0: safety boundary remains stable: no power, no motor, no Profiler, no PWM Gate.
2. P1: learner can explain why P2 config artifacts do not prove motor-control behavior.
3. P2: finish the artifact set by adding GUI/config evidence and resolving pin conflicts before any generated project.

Use `learning/NEXT_LESSON.md` for the exact teaching script, but treat this file as the current execution state.

## Exit Criteria

The sprint can close when:

- `deliverables/2026-05-13_p2_mcsdk_no_power_precheck.md` has all required P2 sections filled.
- Workbench/CubeMX screenshot or `.stmcx` placeholder exists and is linked.
- The nFAULT pin decision is no longer internally conflicted and is confirmed against CubeMX/Workbench plus CN8/EDA/netlist evidence.
- The P1 `PA2/PA3` UART path is either explicitly excluded from the MCSDK FOC config or proven safe by CubeMX/MCSDK.
- Any generated project, if created, is built without connecting power hardware.
- `workflow/evidence_register.md` and `deliverables/submission_checklist.md` reflect the final P2 status.
- `python -m unittest discover -s tests` passes after repo updates.

## No-Go Criteria

Do not move to P3 if any of these are true:

- Any config still routes nFAULT to `PC5` or another OPAMP/VCP-related pin without documented safe mode and board-routing proof.
- The MCSDK config reuses `PA2/PA3` without resolving OPAMP/PGA implications.
- Workbench/CubeMX evidence is only verbal.
- Motor Profiler would require a real motor or power chain.
- Any request would require power-board connection, 24V, PWM Gate output, Hall closed-loop, or SMO validation before phase gates are ready.
