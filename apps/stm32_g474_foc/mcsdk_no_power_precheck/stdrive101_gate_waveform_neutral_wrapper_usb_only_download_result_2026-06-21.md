# STDRIVE101 Gate-Waveform Neutral-Wrapper USB-Only Download Result - 2026-06-21

## Summary

- Evidence ID:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-USBONLY-DOWNLOAD-RESULT-001`.
- Task ID:
  `TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-usbonly-download-result`.
- Scope:
  result record for one USB-only ST-LINK mass-storage copy of the
  neutral-wrapper BIN artifact opened by
  `stdrive101_gate_waveform_neutral_wrapper_usb_only_download_execution_entry_2026-06-21.md`.
- User-confirmed physical boundary:
  USB-only; 24 V disconnected; motor disconnected.
- Decision:
  `STDRIVE101 gate-waveform neutral-wrapper USB-only download result /
  neutral-wrapper BIN copied once to D: NOD_G474RE by ST-LINK mass storage /
  source BIN SHA256 CA2A42F2F83C42EA9E7BEC628BD8656A422DBE767CFFD5A5865BE781603D3D71 /
  no FAIL.TXT before copy / no FAIL.TXT after copy / target BIN not retained
  on D: after copy, consistent with ST-LINK mass-storage consumption /
  download result only / no DMM neutral-state measurement result yet / no
  Run Debug / no 24 V / no Gate PWM output / no Motor Pilot / no Motor
  Profiler / no motor connection / no powered-drive readiness`.

## Boundary

This result records the USB-only mass-storage download of the neutral-wrapper
image. It does not record the CN3 / REG12 neutral-state DMM result yet.

It does not authorize:

- applying 24 V;
- power-board powered runtime;
- Run / Debug;
- normal generated MCSDK application execution;
- Gate PWM output or PWM validation;
- oscilloscope probing on live gate or phase nodes;
- Motor Pilot;
- Motor Profiler;
- motor connection;
- Hall closed loop;
- sensorless operation;
- power-stage readiness or motor readiness claims.

## Image Identity

| Item | Value |
| --- | --- |
| ELF | `.tmp/gwnw_build_2026-06-21_clean/stdrive101_gate_waveform_neutral_wrapper_image.elf` |
| ELF SHA256 | `C47C02D379DC5312095DF786BF8C99B58D42323AD9227D0903BCB8C98AAD9591` |
| MAP | `.tmp/gwnw_build_2026-06-21_clean/stdrive101_gate_waveform_neutral_wrapper_image.map` |
| MAP SHA256 | `5FB24B2735EFFD402C26BDC3B0D267B26B06DC6522A6B5B5D876491BA9A42A83` |
| BIN | `.tmp/gwnw_build_2026-06-21_clean/stdrive101_gate_waveform_neutral_wrapper_image.bin` |
| BIN size | `1044` bytes |
| BIN SHA256 | `CA2A42F2F83C42EA9E7BEC628BD8656A422DBE767CFFD5A5865BE781603D3D71` |
| Copy target | `D:\stdrive101_gate_waveform_neutral_wrapper_image.bin` |
| ST-LINK volume | `D:` / `NOD_G474RE` |

The accepted MAP SHA256 for this image matches the neutral-wrapper build-only
record.

## Pre-Copy Check

Immediately before copy:

| Item | Observed value |
| --- | --- |
| Drive | `D:` |
| Volume label | `NOD_G474RE` |
| Drive type | removable disk |
| Source BIN exists | yes |
| Source BIN size | `1044` bytes |
| Source BIN SHA256 | `CA2A42F2F83C42EA9E7BEC628BD8656A422DBE767CFFD5A5865BE781603D3D71` |
| `D:\FAIL.TXT` before copy | absent |
| Target BIN before copy | absent |

The visible files before copy were `DETAILS.TXT`, `MBED.HTM`, and
`GETSTART.HTM`. `DETAILS.TXT` reported:

```text
Version: V3J17M10
Build:   Oct 17 2025 15:12:06
```

## Copy Result

Executed once:

```powershell
Copy-Item -LiteralPath .tmp\gwnw_build_2026-06-21_clean\stdrive101_gate_waveform_neutral_wrapper_image.bin -Destination D:\stdrive101_gate_waveform_neutral_wrapper_image.bin -Force
```

Post-copy check after a short wait:

| Item | Observed value |
| --- | --- |
| `D:` still present | yes |
| Volume label | `NOD_G474RE` |
| `D:\FAIL.TXT` after copy | absent |
| Target BIN after copy | absent |
| `DETAILS.TXT` | `Version: V3J17M10`; `Build: Oct 17 2025 15:12:06` |

The copied target not remaining visible on `D:` is treated as the ST-LINK
mass-storage interface consuming the BIN, not as a failure, because no
`FAIL.TXT` appeared.

## Next Measurement Table

The next evidence must be direct DMM readings with USB-only still active and
24 V still disconnected. Do not infer values from the download result.

| Item | Reading |
| --- | --- |
| `VS / 24V_FUSED` | `___ V` |
| `CN3_1` driver input | `___ V` |
| `CN3_2 / LIN1` | `___ V` |
| `CN3_3` driver input | `___ V` |
| `CN3_4` driver input | `___ V` |
| `CN3_5` driver input | `___ V` |
| `CN3_6` driver input | `___ V` |
| `CN3_13 / nFAULT` | `___ V` |
| `CN3_14 / 3V3` | `___ V` |
| `REG12` | `___ V` |
| board heat / smell / sound / reset loop | `none / describe` |
| stop-rule hit | `yes / no`; reason `___` |

Expected safe neutral-wrapper USB-only result for `CN3_1` through `CN3_6`:
close to `0 V`. If any of those six readings is stably above `0.3 V`, stop,
disconnect USB if needed, keep 24 V disconnected, and report the raw reading.

## Next Checkpoint

Create a separate neutral-wrapper USB-only neutral-state runtime result record
after the user reports the DMM table.

Still blocked after this download result:

- 24 V;
- Gate PWM output;
- Motor Pilot;
- Motor Profiler;
- motor connection;
- power-stage readiness or motor readiness.
