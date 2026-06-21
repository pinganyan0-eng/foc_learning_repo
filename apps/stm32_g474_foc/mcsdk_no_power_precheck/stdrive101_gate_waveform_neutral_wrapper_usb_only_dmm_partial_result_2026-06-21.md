# STDRIVE101 Gate-Waveform Neutral-Wrapper USB-Only DMM Partial Result - 2026-06-21

## Summary

- Evidence ID:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-USBONLY-DMM-PARTIAL-RESULT-001`.
- Task ID:
  `TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-usbonly-dmm-partial-result`.
- Scope:
  partial user-reported DMM readings after the neutral-wrapper USB-only
  ST-LINK mass-storage download result.
- Carried-forward physical boundary:
  USB-only; 24 V disconnected; motor disconnected.
- Decision:
  `STDRIVE101 gate-waveform neutral-wrapper USB-only DMM partial result /
  user-reported CN3_1 through CN3_6 all 0 V / user-reported P13 = 3.3 V and
  P14 = 3.3 V, recorded as the requested CN3_13 / nFAULT and CN3_14 / 3V3
  labels if P13/P14 map to that header / six driver-input stop-rule not hit /
  VS / 24V_FUSED not reported in this partial record / REG12 not reported /
  board heat smell sound reset-loop status not reported / partial USB-only
  DMM evidence only / no full DMM neutral-state pass / no Run Debug / no 24 V /
  no Gate PWM output / no Motor Pilot / no Motor Profiler / no motor
  connection / no powered-drive readiness`.

## Boundary

This record captures the first direct DMM readings after the neutral-wrapper
BIN was downloaded through USB-only ST-LINK mass storage.

It does not authorize:

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

## Image And Download Context

| Item | Value |
| --- | --- |
| Prior download result | `stdrive101_gate_waveform_neutral_wrapper_usb_only_download_result_2026-06-21.md` |
| ELF SHA256 | `C47C02D379DC5312095DF786BF8C99B58D42323AD9227D0903BCB8C98AAD9591` |
| MAP SHA256 | `5FB24B2735EFFD402C26BDC3B0D267B26B06DC6522A6B5B5D876491BA9A42A83` |
| BIN SHA256 | `CA2A42F2F83C42EA9E7BEC628BD8656A422DBE767CFFD5A5865BE781603D3D71` |
| ST-LINK copy result | no `FAIL.TXT` before or after copy; target BIN not retained on `D:` after copy |

This partial DMM record relies on the same neutral-wrapper image identity as
the prior download result. It does not re-copy the BIN and does not perform
Run / Debug.

## User-Reported DMM Readings

Latest user report:

```text
CN3-1 to CN3-6 are all 0 V; P13 and P14 are both 3.3 V.
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
| `CN3_13 / nFAULT` | `3.3 V` | reported as `P13`; label mapping carried forward from the requested table |
| `CN3_14 / 3V3` | `3.3 V` | reported as `P14`; label mapping carried forward from the requested table |
| `VS / 24V_FUSED` | not reported in this partial record | still needed |
| `REG12` | not reported in this partial record | still needed |
| board heat / smell / sound / reset loop | not reported in this partial record | still needed |

## Stop-Rule Evaluation

For the six MCU-facing STDRIVE101 driver inputs only:

- `CN3_1` through `CN3_6` were all reported as `0 V`.
- The `CN3_1` through `CN3_6` stop rule was not hit because no reported
  driver-input reading was stably above `0.3 V`.

This is not a full USB-only neutral-state result yet, because
`VS / 24V_FUSED`, `REG12`, and the board abnormal-condition status were not
reported in this partial record.

## Next Checkpoint

Do not repeat the already reported `CN3_1` through `CN3_6` readings unless
something changes physically.

With black probe on GND, USB-only still active, 24 V still disconnected, and
the motor still disconnected, report only:

| Item | Reading |
| --- | --- |
| `VS / 24V_FUSED` | `___ V` |
| `REG12` | `___ V` |
| board heat / smell / sound / reset loop | `none / describe` |

If any later recheck of `CN3_1` through `CN3_6` is stably above `0.3 V`, stop,
keep 24 V disconnected, and record the raw reading.

Still blocked after this partial result:

- 24 V;
- Gate PWM output;
- Motor Pilot;
- Motor Profiler;
- motor connection;
- power-stage readiness or motor readiness.
