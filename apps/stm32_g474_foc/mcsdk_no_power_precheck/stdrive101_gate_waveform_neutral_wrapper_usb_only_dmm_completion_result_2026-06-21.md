# STDRIVE101 Gate-Waveform Neutral-Wrapper USB-Only DMM Completion Result - 2026-06-21

## Summary

- Evidence ID:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-USBONLY-DMM-COMPLETION-RESULT-001`.
- Task ID:
  `TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-usbonly-dmm-completion-result`.
- Scope:
  completed user-reported USB-only DMM table after the neutral-wrapper
  USB-only ST-LINK mass-storage download and the earlier partial DMM result.
- Carried-forward physical boundary:
  USB-only; 24 V disconnected; motor disconnected.
- Decision:
  `STDRIVE101 gate-waveform neutral-wrapper USB-only DMM completion result /
  user-reported CN3_1 through CN3_6 all 0 V / user-reported P13 = 3.3 V and
  P14 = 3.3 V, recorded as the requested CN3_13 / nFAULT and CN3_14 / 3V3
  labels if P13/P14 map to that header / user-reported VS / 24V_FUSED = 2 V /
  user-reported REG12 = 0.5 V / no board heat smell sound reset-loop reported /
  six driver-input stop-rule not hit / VS residual boundary is not clean
  because VS / 24V_FUSED is above the prior <1 V USB-only boundary / USB-only
  DMM table complete but not a pass for upward hardware progression / no Run
  Debug / no 24 V / no Gate PWM output / no Motor Pilot / no Motor Profiler /
  no motor connection / no powered-drive readiness`.

## Boundary

This result completes the direct USB-only DMM table. It does not authorize:

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

The completed table is not treated as a clean neutral-state pass because
`VS / 24V_FUSED = 2 V` is above the prior USB-only residual-voltage boundary
of `< 1 V`.

## Image And Download Context

| Item | Value |
| --- | --- |
| Prior download result | `stdrive101_gate_waveform_neutral_wrapper_usb_only_download_result_2026-06-21.md` |
| Prior partial DMM result | `stdrive101_gate_waveform_neutral_wrapper_usb_only_dmm_partial_result_2026-06-21.md` |
| ELF SHA256 | `C47C02D379DC5312095DF786BF8C99B58D42323AD9227D0903BCB8C98AAD9591` |
| MAP SHA256 | `5FB24B2735EFFD402C26BDC3B0D267B26B06DC6522A6B5B5D876491BA9A42A83` |
| BIN SHA256 | `CA2A42F2F83C42EA9E7BEC628BD8656A422DBE767CFFD5A5865BE781603D3D71` |
| ST-LINK copy result | no `FAIL.TXT` before or after copy; target BIN not retained on `D:` after copy |

This completion result does not re-copy the BIN and does not perform Run /
Debug.

## Completed DMM Table

User-reported rows carried forward from the partial result:

```text
CN3-1 to CN3-6 are all 0 V; P13 and P14 are both 3.3 V.
```

New user-reported completion rows:

```text
VS / 24V_FUSED = 2 V
REG12 = 0.5 V
board heat / smell / sound / reset loop = none
```

Recorded table:

| Item | Reading | Status |
| --- | --- | --- |
| `CN3_1` driver input | `0 V` | carried forward from partial result |
| `CN3_2 / LIN1` | `0 V` | carried forward from partial result |
| `CN3_3` driver input | `0 V` | carried forward from partial result |
| `CN3_4` driver input | `0 V` | carried forward from partial result |
| `CN3_5` driver input | `0 V` | carried forward from partial result |
| `CN3_6` driver input | `0 V` | carried forward from partial result |
| `CN3_13 / nFAULT` | `3.3 V` | carried forward as `P13`; label mapping from requested table |
| `CN3_14 / 3V3` | `3.3 V` | carried forward as `P14`; label mapping from requested table |
| `VS / 24V_FUSED` | `2 V` | reported; above prior `< 1 V` USB-only boundary |
| `REG12` | `0.5 V` | reported |
| board heat / smell / sound / reset loop | none reported | reported |

## Stop-Rule Evaluation

- `CN3_1` through `CN3_6` were all reported as `0 V`.
- The six driver-input stop-rule was not hit because no `CN3_1` through
  `CN3_6` reading was stably above `0.3 V`.
- Board abnormal-condition stop rule was not hit in the reported rows because
  the user reported no heat, smell, sound, or reset-loop symptom.
- The voltage-boundary stop condition is active for upward progression:
  `VS / 24V_FUSED = 2 V` is above the prior `< 1 V` USB-only boundary. Treat
  this as unresolved residual voltage or backfeed evidence until a separate
  no-power recheck shows otherwise.

## Next Checkpoint

Do not proceed to 24 V, Gate PWM output, Motor Pilot, Motor Profiler, or motor
connection from this result.

Next bounded action is a residual-voltage isolation recheck only:

1. Keep HSPY / 24 V OFF and physically disconnected.
2. Keep the motor disconnected.
3. Do not use Run / Debug, Motor Pilot, Motor Profiler, or PWM output.
4. Disconnect USB / ST-LINK.
5. Wait 30 to 60 seconds.
6. With black probe on GND, remeasure only:
   - `VS / 24V_FUSED`;
   - `REG12`.
7. If `VS / 24V_FUSED` remains above `1 V`, keep the board unpowered and
   report the raw value for no-power source / board review.
8. If `VS / 24V_FUSED` falls below `1 V`, record that the elevated USB-only
   value was cleared by USB removal or discharge; this still does not open
   motor or PWM work without a separate later phase-gate decision.

Still blocked after this completion result:

- 24 V;
- Gate PWM output;
- Motor Pilot;
- Motor Profiler;
- motor connection;
- power-stage readiness or motor readiness.
