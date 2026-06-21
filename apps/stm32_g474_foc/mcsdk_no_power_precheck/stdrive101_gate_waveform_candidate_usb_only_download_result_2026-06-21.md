# STDRIVE101 Gate-Waveform Candidate USB-Only Download Result - 2026-06-21

## Summary

- Evidence ID:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-CANDIDATE-USBONLY-DOWNLOAD-RESULT-001`.
- Task ID:
  `TASK-2026-06-21-stdrive101-gate-waveform-candidate-usbonly-download-result`.
- Scope:
  result record for one USB-only ST-LINK mass-storage copy of the waveform
  candidate BIN artifact opened by
  `stdrive101_gate_waveform_candidate_usb_only_download_execution_entry_2026-06-21.md`.
- User authorization:
  `允许复制 candidate BIN 到 D:`.
- Decision:
  `STDRIVE101 gate-waveform candidate USB-only download result / candidate BIN
  copied once to D: NOD_G474RE by ST-LINK mass storage / source BIN SHA256
  362C510E4F682751F0721B54F306F6E144951F03F9FF875E68E238D92A29BB31 /
  no FAIL.TXT before copy / no FAIL.TXT after copy / target BIN not retained
  on D: after copy, consistent with ST-LINK mass-storage consumption /
  candidate board image download result only / no CN3 DMM post-download result
  yet / no measured waveform result yet / no Run Debug / no 24 V command / no
  Motor Pilot / no Motor Profiler / no motor connection / no powered-drive
  readiness`.

## Boundary

This result records the USB-only mass-storage download of the waveform
candidate image. The board image is now treated as the waveform candidate image
for the next bounded checks. Because this candidate image calls
`gate_waveform_candidate_run_once()` once after reset and then holds idle low,
this record does not prove absence of a boot-time output transition. It also
does not prove CN3 pin state, waveform correctness, power-stage behavior, or
motor behavior.

It does not authorize:

- Run / Debug;
- normal generated MCSDK application execution;
- Motor Pilot;
- Motor Profiler;
- motor connection;
- Hall closed loop;
- sensorless operation;
- power-stage readiness or motor readiness claims.

No 24 V action is authorized by this result. A later 24 V no-motor step must be
a separate explicit execution entry with current limit, probe points, rollback,
and stop rules.

## Image Identity

| Item | Value |
| --- | --- |
| ELF | `.tmp/manual_gate_waveform_build_only_2026-06-21_clean/stdrive101_gate_waveform_candidate_image.elf` |
| ELF SHA256 | `10BA818730E259AEBA8A5C5E5C96CFBA32FCB90AAA4136B775022B9D69ADCE7C` |
| MAP | `.tmp/manual_gate_waveform_build_only_2026-06-21_clean/stdrive101_gate_waveform_candidate_image.map` |
| MAP SHA256 | `170EA77C566F98CF9EF2AC88F76B154238A5404DC705AAE3917BEAE7C1503D4C` |
| BIN | `.tmp/manual_gate_waveform_build_only_2026-06-21_clean/stdrive101_gate_waveform_candidate_image.bin` |
| BIN size | `1852` bytes |
| BIN SHA256 | `362C510E4F682751F0721B54F306F6E144951F03F9FF875E68E238D92A29BB31` |
| Copy target | `D:\stdrive101_gate_waveform_candidate_image.bin` |
| ST-LINK volume | `D:` / `NOD_G474RE` |

The accepted MAP SHA256 for this image matches the Gate E2 build-only record.

## Pre-Copy Check

Immediately before copy:

| Item | Observed value |
| --- | --- |
| Drive | `D:` |
| Volume label | `NOD_G474RE` |
| Source BIN exists | yes |
| Source BIN size | `1852` bytes |
| Source BIN SHA256 | `362C510E4F682751F0721B54F306F6E144951F03F9FF875E68E238D92A29BB31` |
| `D:\FAIL.TXT` before copy | absent |
| Target BIN before copy | absent |

`DETAILS.TXT` reported:

```text
Version: V3J17M10
Build:   Oct 17 2025 15:12:06
```

## Copy Result

Executed once:

```powershell
Copy-Item -LiteralPath .tmp\manual_gate_waveform_build_only_2026-06-21_clean\stdrive101_gate_waveform_candidate_image.bin -Destination D:\stdrive101_gate_waveform_candidate_image.bin
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

## Runtime Interpretation Limit

This is a download result, not an oscilloscope or DMM result. The candidate
firmware may have already run its one-shot USB-only startup window after the
ST-LINK copy/reset. No probe was used in this record, so there is no measured
waveform result and no evidence of the exact transient shape or timing.

## Next USB-Only Measurement Table

The next evidence must be direct post-download readings with the motor still
disconnected. Do not infer values from the download result.

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

Expected steady post-window candidate result for `CN3_1` through `CN3_6`:
close to `0 V`. If any of those six readings is stably above `0.3 V`, stop,
disconnect USB if needed, keep the motor disconnected, and report the raw
reading.

## Next Checkpoint

Create a separate waveform-candidate USB-only post-download measurement result
after the user reports the table.

Still blocked after this download result:

- 24 V no-motor waveform execution until a separate execution entry;
- Motor Pilot;
- Motor Profiler;
- motor connection;
- power-stage readiness or motor readiness.
