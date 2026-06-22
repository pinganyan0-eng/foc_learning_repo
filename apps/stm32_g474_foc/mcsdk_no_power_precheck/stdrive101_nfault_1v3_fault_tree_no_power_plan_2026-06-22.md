# STDRIVE101 nFAULT 1.3V Fault-Tree No-Power Plan - 2026-06-22

## Summary

- Evidence ID:
  `EV-2026-06-22-STDRIVE101-NFAULT-1V3-FAULT-TREE-NO-POWER-PLAN-001`.
- Task ID:
  `TASK-2026-06-22-stdrive101-nfault-1v3-fault-tree-no-power-plan`.
- Decision:
  `STDRIVE101 nFAULT 1.3V fault-tree no-power plan / power-board-side fault localized / no-power source and photo evidence only / HIN1 comparison remains future teacher-reviewed phase gate / no repeat powered wake / no PWM output / no motor readiness`.
- Subagent synthesis:
  the safety helper identified the current project blocker as a
  power-board / STDRIVE101-side `nFAULT = 1.3 V` condition after successful
  `PA7 -> LIN1` wake, and recommended a no-power fault-tree plan rather than
  another powered or motor-connected action. Other helper slices were
  rate-limited, so the main agent recovered by inspecting the local evidence
  files directly before writing this plan.

This is a planning and source-review artifact only. It consolidates the latest
fault evidence into a bounded no-power fault tree for teacher / hardware
teammate review.

## Evidence Carried Forward

- Latest PA7 / LIN1 result:
  `stdrive101_pa7_lin1_wake_nfault_1v3_fault_isolation_result_2026-06-21.md`.
- Earlier cause review:
  `stdrive101_single_input_wake_nfault_cause_review_2026-06-20.md`.
- Marked schematic source packet:
  `stdrive101_fault_review_schematic_marking_2026-06-20.md`.
- Protection-node no-power DMM result:
  `stdrive101_protection_nodes_no_power_dmm_result_2026-06-20.md`.

Current strongest evidence chain:

```text
PA7 / CN10-15 = 3.3 V
-> CN8 P2 / LIN1 = 3.3 V
-> VS / 24V_FUSED = 24 V
-> REG12 = 12 V
-> nFAULT = 1.3 V on CN8 P13 and NUCLEO CN10-16
-> nFAULT remains 1.3 V on CN8 P13 after PB12 is disconnected
```

The user-corrected R3 evidence is:

```text
R3 body = 10 kohm
R3 3V3 side -> CN8 P14 / 3V3 = 0 ohm
R3 nFAULT side -> CN8 P13 / nFAULT = 0 ohm
```

This localizes the latest symptom away from PA7, the LIN1 jumper, the R3
pull-up value, and NUCLEO PB12. It does not prove the exact STDRIVE101 fault
cause.

## Fault Tree

| Branch | Current interpretation | No-power evidence still useful |
| --- | --- | --- |
| `LIN1 / GLS1 / Q2 / OUT1` low-side phase-U path | Primary working hypothesis. `LIN1` wake can command the phase-U low side, and a VDS / output-path abnormality can fit the fault pattern. | Clear board photo or EDA crop identifying `GLS1`, Q2 gate, Q2 source, Q2 drain / `OUT1`, R24, R25, `ADC_U`, and `GND_POWER`; no-power resistance / diode rows only after pads are certain. |
| Common protection or STDRIVE101-side fault | Still possible because `nFAULT` remains 1.3 V on the power-board side with PB12 disconnected. | Photo / EDA crop around U1, `CP`, `SCREF`, `REG12`, `VS`, `nFAULT`, C1, C4/C5, R1/R2, R3, LED1, and nearby solder joints. |
| `SCREF` threshold / divider problem | Not proven. Prior no-power rows reported `SCREF -> 3V3 = 12 kohm` and `SCREF -> GND = 12 kohm`, which do not show a rail hard short but do not validate the threshold. | Re-check source values and physical population for R1/R2 only with power off; do not infer a safe VDS threshold from in-circuit resistance alone. |
| `CP` / overcurrent comparator path | Possible but not the leading branch from the recorded supply current. Prior `CP-GND` was megaohms and rising with no beep. | Photo / EDA crop and capacitor / solder review around C1 and U1 pin 1. |
| `REG12` sequence or load issue | Less likely as a steady fault because `REG12 = 12 V` was reported, but transient or loading behavior is not ruled out. | No-power review of C4/C5, bootstrap diode network, and any accidental external REG12 tie; no direct external REG12 supply. |
| External `nFAULT` pull-down / indicator loading | Lower likelihood after PB12 disconnect and R3 continuity correction, but LED / solder / trace loading remains possible. | No-power source/photo review of R3, LED1, `nFAULT` trace, and any downstream connector loading. |

## Allowed Next Evidence

Allowed now, with all power removed:

```text
HSPY output OFF
VS / 24V_FUSED confirmed near 0 V
10 kohm LIN1 stimulus removed
Motor disconnected
USB / ST-LINK disconnected unless a photo task needs the NUCLEO nearby
DMM continuity / resistance / diode mode only
```

Allowed repo-side or teammate-side evidence:

- a clear board photo of U1 STDRIVE101 and phase-U low-side area;
- an EDA schematic/netlist crop for U1, Q1/Q2, `OUT1`, `GLS1`, `GHS1`,
  `SCREF`, `CP`, `REG12`, `nFAULT`, and ground domains;
- no-power raw resistance / diode results only after physical pads are
  confidently identified;
- a teacher-reviewed fault-tree comment that chooses between the
  `LIN1 / GLS1 / Q2 / OUT1` branch and common protection / assembly branches.

## Forbidden Now

This plan does not authorize:

- flash;
- Run / Debug;
- repeat 24 V wake;
- any `HIN1` comparison execution;
- power-board action beyond no-power inspection;
- motor connection;
- Gate PWM output;
- Motor Pilot;
- Motor Profiler;
- Hall closed-loop claim;
- sensorless / SMO claim;
- power-stage readiness;
- motor readiness;
- safe drive operation.

The earlier HIN1 comparison idea remains a future teacher-reviewed phase gate
only. It must not be executed from this plan.

## Next Teacher / Hardware Packet

Ask the hardware teammate or teacher for this packet before any further
powered diagnostic:

```text
1. Board photo or EDA crop showing U1 STDRIVE101, Q1/Q2, OUT1, GLS1, R24,
   R25, ADC_U, GND_POWER, SCREF R1/R2, CP C1, REG12 C4/C5, R3, LED1.
2. Confirmation that HSPY is OFF, VS / 24V_FUSED is near 0 V, motor is
   disconnected, and LIN1 10 kohm stimulus is removed before any DMM row.
3. If pads are certain, raw no-power rows:
   Q2 gate-source = ___
   Q2 source to GND_POWER / CN3_15 = ___
   OUT1 / Q2 drain to Q2 source diode mode = ___
   OUT1 to VS / 24V_FUSED diode mode = ___
   nFAULT to 3V3 = ___
   nFAULT to GND = ___
4. Teacher judgment: does the evidence point first to phase-U low-side VDS /
   output path, or to common STDRIVE101 protection / soldering / chip fault?
```

If any physical point is uncertain, stop and request a clearer photo or EDA
crop instead of probing by guesswork.
