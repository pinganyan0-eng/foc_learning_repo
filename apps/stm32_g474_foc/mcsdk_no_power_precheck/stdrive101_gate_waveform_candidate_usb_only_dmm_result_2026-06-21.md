# STDRIVE101 Gate-Waveform Candidate USB-Only DMM Result - 2026-06-21

## Summary

- Evidence ID:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-CANDIDATE-USBONLY-DMM-RESULT-001`.
- Task ID:
  `TASK-2026-06-21-stdrive101-gate-waveform-candidate-usbonly-dmm-result`.
- Scope:
  user-reported USB-only DMM readings after the waveform candidate USB-only
  ST-LINK mass-storage download result.
- Prior download result:
  `stdrive101_gate_waveform_candidate_usb_only_download_result_2026-06-21.md`.
- Decision:
  `STDRIVE101 gate-waveform candidate USB-only DMM result / user-reported
  CN3_1 through CN3_6 all 0 V / user-reported CN3_13 = 3 V / user-reported
  CN3_14 = 3 V / user-reported VS / 24V_FUSED = 2 V / user-reported
  REG12 = 0.3 V / board heat smell sound reset-loop status not reported in
  this latest row / six driver-input stop-rule not hit / VS residual-voltage
  boundary is active because VS / 24V_FUSED is above the prior <1 V USB-only
  boundary / USB-only DMM result is not a pass for upward hardware progression
  / no Run Debug / no 24 V command / no Gate PWM output / no Motor Pilot / no
  Motor Profiler / no motor connection / no powered-drive readiness`.

## Boundary

This result records static DMM readings only. It does not authorize:

- applying 24 V;
- power-board powered runtime;
- Run / Debug;
- normal generated MCSDK application execution;
- Gate PWM output or PWM validation;
- Motor Pilot;
- Motor Profiler;
- motor connection;
- Hall closed loop;
- sensorless operation;
- power-stage readiness or motor readiness claims.

Because `VS / 24V_FUSED = 2 V` is above the prior USB-only residual-voltage
boundary of `< 1 V`, this result blocks upward hardware progression until a
separate residual-voltage isolation check resolves whether the reading clears
after USB / ST-LINK is disconnected.

## Image And Download Context

| Item | Value |
| --- | --- |
| Prior download result | `stdrive101_gate_waveform_candidate_usb_only_download_result_2026-06-21.md` |
| ELF SHA256 | `10BA818730E259AEBA8A5C5E5C96CFBA32FCB90AAA4136B775022B9D69ADCE7C` |
| MAP SHA256 | `170EA77C566F98CF9EF2AC88F76B154238A5404DC705AAE3917BEAE7C1503D4C` |
| BIN SHA256 | `362C510E4F682751F0721B54F306F6E144951F03F9FF875E68E238D92A29BB31` |
| BIN size | `1852` bytes |
| ST-LINK copy result | no `FAIL.TXT` before or after copy; target BIN not retained on `D:` after copy |

This record does not re-copy the BIN and does not use Run / Debug.

## User-Reported DMM Table

User-reported rows:

```text
CN3_1 to CN3_6 are all 0 V
CN3_13 is 3 V
CN3_14 is 3 V
VS / 24V_FUSED = 2 V
REG12 = 0.3 V
```

Recorded table:

| Item | Reading | Status |
| --- | --- | --- |
| `CN3_1` driver input | `0 V` | reported |
| `CN3_2 / LIN1` | `0 V` | reported |
| `CN3_3` driver input | `0 V` | reported |
| `CN3_4` driver input | `0 V` | reported |
| `CN3_5` driver input | `0 V` | reported |
| `CN3_6` driver input | `0 V` | reported |
| `CN3_13 / nFAULT` | `3 V` | reported exactly as `3 V` |
| `CN3_14 / 3V3` | `3 V` | reported exactly as `3 V` |
| `VS / 24V_FUSED` | `2 V` | reported; above prior `< 1 V` USB-only boundary |
| `REG12` | `0.3 V` | reported |
| board heat / smell / sound / reset loop | not reported | missing in latest row |

## Stop-Rule Evaluation

- `CN3_1` through `CN3_6` were all reported as `0 V`.
- The six driver-input stop-rule was not hit because no `CN3_1` through
  `CN3_6` reading was stably above `0.3 V`.
- The board abnormal-condition stop rule cannot be evaluated from this latest
  row because board heat / smell / sound / reset-loop status was not reported.
- The voltage-boundary stop condition is active for upward progression:
  `VS / 24V_FUSED = 2 V` is above the prior `< 1 V` USB-only boundary. Treat
  this as unresolved residual voltage or backfeed evidence until a separate
  no-power isolation check shows otherwise.

## Next Checkpoint

Do not proceed to 24 V, Gate PWM output, Motor Pilot, Motor Profiler, or motor
connection from this result.

Next bounded action is a residual-voltage isolation check only:

1. Keep HSPY / 24 V OFF and physically disconnected.
2. Keep the motor disconnected.
3. Do not install a `10 kohm` wake resistor or LIN1 stimulus.
4. Do not use Run / Debug, Motor Pilot, Motor Profiler, or PWM output.
5. Disconnect USB / ST-LINK.
6. Wait 30 to 60 seconds.
7. With black probe on GND, remeasure only:
   - `VS / 24V_FUSED`;
   - `REG12`.
8. If `VS / 24V_FUSED` remains above `1 V`, keep the board unpowered and
   report the raw value for no-power source / board review.
9. If `VS / 24V_FUSED` falls below `1 V`, record that the elevated USB-only
   value was cleared by USB removal or discharge; this still does not open
   motor or PWM work without a separate later phase-gate decision.

Do not repeat the whole CN3 table for this checkpoint unless the physical
state, firmware image, wiring, or measured value changes.
