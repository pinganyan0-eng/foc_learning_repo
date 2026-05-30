# 2026-05-19 Packet A FOC Route Decision After MY_FOC Rollback

## Decision

`Route narrowed / GUI-created FOC source required / Packet A still blocked`.

Stable phrase: no generated-project trust.

This is a no-power Packet A route decision. It records what the latest
Workbench evidence allows, what failed, and what the next acceptable FOC
configuration capture must prove.

## Feature Sentence

After the `MY_FOC` one-field manual FOC edit failed Workbench reload, the next
valid Packet A path is a Workbench GUI-created or otherwise complete
reviewable FOC source, not another partial `.stwb6` text edit.

## Input Evidence

| Source | What It Proves | Why It Still Fails Packet A |
| --- | --- | --- |
| `packet_a_sources/2026-05-15_my_first_foc/My_First_FOC.stwb6` | A local Workbench 6.4.2 `.stwb6` can have top-level `"algorithm": "FOC"` with `NUCLEO-G474RE`, Hall sensor features, and current-sensing features. | It is a legacy learning leftover, uses built-in `EVALSTDRIVE101`, and keeps the demo motor clue `R57BLB50L2`. It is not the project self-developed STDRIVE101 board source. |
| `packet_a_sources/2026-05-19_my_foc_generated_project/MY_FOC.original_2026-05-19.stwb6` | The user-created `MY_FOC` source has `NUCLEO-G474RE`, a custom STDRIVE101 board description, Hall sensor feature data, current-sensing feature variants, and FOC listed as a compatible algorithm. | The saved top-level algorithm is `"sixStep"`, and generated outputs are `SIX_STEP`. The generated `.ioc` / `.wbdef` review shows current sensing and fault/break disabled. |
| `packet_a_sources/2026-05-19_my_foc_generated_project/MY_FOC.codex_foc_candidate_2026-05-19.stwb6` | A one-field change from `"algorithm": "sixStep"` to `"algorithm": "FOC"` is archived as negative evidence. | Workbench failed to load it. It must not be reused as a source. |
| `my_foc_foc_candidate_edit_2026-05-19.md` | The external `MY_FOC.stwb6` was restored from backup and again reads `"algorithm": "sixStep"`. | Rollback protects the tool state, but does not create valid FOC Packet A evidence. |

## Rule Table

| Rule | Decision |
| --- | --- |
| Manual `.stwb6` edit | Do not attempt another partial text edit of the Workbench source schema. The failed candidate proves that top-level `algorithm` alone is insufficient. |
| Preferred Packet A route | Use Workbench GUI to create a new FOC project or valid GUI conversion, then save the `.stwb6` and selected-field screenshots for review before any generation. |
| Board identity | The source must represent the self-developed STDRIVE101 board or a reviewable custom/user board artifact. Built-in `EVALSTDRIVE101`, `STEVAL-LVLP01`, and `EVLDRIVE101-HPD` remain non-substitutes. |
| Pin-change route | If pins can change, choose a Workbench/MCSDK expressible timer-compatible PWM and Hall route, then separately match the physical wiring or adapter evidence. |
| No-PCB-change route | If current PCB2 pins stay unchanged, `PA0/PA1/PB4` remains a software Hall design-review route only. It is not accepted as same-timer hardware Hall Packet A evidence. |
| Current sensing and fault | A future source must not leave current sensing disabled, bus-voltage monitoring disabled when required by the gate, or fault/break disabled. |
| Generated project | Do not build or trust generated output until a new dated Packet A source review accepts the FOC selected fields. |

## Function Responsibilities

| Function | Responsibility |
| --- | --- |
| Workbench GUI | Owns schema-consistent FOC project creation or conversion. |
| Board Designer / Board Manager | Owns any custom/user board artifact for the self-developed STDRIVE101 board. |
| Packet A source review | Accepts, partially accepts, or rejects the saved `.stwb6` and selected-field screenshots before generated-project trust can change. |
| Future build-only gate | May run only after accepted Packet A evidence, and still forbids flash, power, Motor Profiler, Motor Pilot, or Gate PWM output. |
| Hardware teammate / physical route | Owns proof that any changed pins or adapter route actually match the board and harness. |

## Next Acceptable Capture

The next Packet A attempt should capture these fields before clicking any
Generate or build action:

1. Workbench source saved as a new or corrected FOC project.
2. Top-level / project control mode visible as FOC or field-oriented control,
   not `SIX_STEP`.
3. Control board visible as `NUCLEO-G474RE` / `STM32G474RETx`.
4. Power board visible as a project custom/user STDRIVE101 board path, or a
   captured Board Designer / Board Manager source that represents it.
5. Current sensing selected and reviewable, not `M1_CUR_READING=false`.
6. Fault / break path selected and reviewable, not `TIM_BREAK_DISABLE`.
7. Hall or speed-sensor route selected and reviewable, with a clear note
   whether the route is a changed timer-compatible physical route or the
   current `PA0/PA1/PB4` software Hall design route.
8. PWM route selected and reviewable, with the physical match or rework path
   explicitly deferred to Packet B / hardware evidence.
9. Motor entry labeled as a source-level candidate, not an unqualified measured
   motor parameter claim.

## Hard Stops

- No Generate.
- No build.
- No flash.
- No 24V.
- No power-board connection.
- No motor connection.
- No Gate PWM output.
- No Motor Profiler run.
- No Motor Pilot.
- No Hall closed-loop claim.
- No sensorless / SMO claim.

## Result

Packet A remains blocked.

The project now has a clearer next move: create or capture a full Workbench
FOC source through the GUI, or stop and open hardware-rework / custom-board
planning if the GUI cannot express the self-developed STDRIVE101 route.
