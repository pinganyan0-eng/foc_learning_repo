# STDRIVE101 Gate-Waveform Candidate USB-Only Download Execution Entry - 2026-06-21

## Summary

- Evidence ID:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-CANDIDATE-USBONLY-DOWNLOAD-EXECUTION-ENTRY-001`.
- Task ID:
  `TASK-2026-06-21-stdrive101-gate-waveform-candidate-usbonly-download-execution-entry`.
- Scope:
  execution-entry record for one USB-only ST-LINK mass-storage copy of the
  waveform candidate BIN artifact.
- User request:
  `允许复制 candidate BIN 到 D:`.
- Operational boundary used for the copy:
  USB / ST-LINK mass storage only; no Run / Debug; no Motor Pilot; no Motor
  Profiler; no motor connection requested or performed by Codex.
- Decision:
  `STDRIVE101 gate-waveform candidate USB-only download execution entry /
  user explicitly authorized copying candidate BIN to D: / candidate BIN SHA256
  362C510E4F682751F0721B54F306F6E144951F03F9FF875E68E238D92A29BB31 matched
  the candidate BIN artifact record / D: volume label NOD_G474RE detected /
  FAIL.TXT absent before copy / opens exactly one USB-only ST-LINK
  mass-storage candidate BIN copy / no Run Debug / no 24 V command / no Motor
  Pilot / no Motor Profiler / no motor connection / no powered-drive
  readiness`.

## Boundary

This record opens exactly one USB-only copy of the waveform candidate BIN to
the ST-LINK mass-storage volume. It does not open any normal debug workflow or
motor workflow.

Still forbidden:

- Run / Debug;
- normal generated MCSDK application start commands;
- Motor Pilot;
- Motor Profiler;
- motor connection;
- Hall closed loop;
- sensorless operation;
- power-stage readiness or motor readiness claims.

No 24 V action is authorized by this record. A later 24 V no-motor step must be
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
| Transfer target | `D:\stdrive101_gate_waveform_candidate_image.bin` |
| ST-LINK volume | `D:` / `NOD_G474RE` |

Accepted source/build evidence:

- `stdrive101_gate_waveform_build_only_record_no_power_2026-06-21.md`;
- `stdrive101_gate_waveform_candidate_bin_artifact_record_no_power_2026-06-21.md`;
- retained MAP symbol includes
  `gate_waveform_candidate_run_once` at `0x080005bc`;
- the checked forbidden normal-MCSDK MAP screen had no matches.

## Allowed Execution Envelope

Only this envelope is opened:

| Item | Allowed state |
| --- | --- |
| Transfer method | direct ST-LINK mass-storage copy to `D:\NOD_G474RE` |
| Image | waveform candidate BIN named above |
| Result check | check whether `D:\FAIL.TXT` appears after copy |
| Debugger | not used |
| Motor tools | Motor Pilot / Motor Profiler not used |
| Motor | disconnected / not connected by this action |

Do not use Motor Pilot, Motor Profiler, normal MCSDK start buttons, PC13
start/stop, MCP commands, or Run / Debug from this entry. Because the
candidate image is a `run_once()` image, the later download result must not
claim that no MCU output transition occurred; it may only claim no measured
waveform validation unless a separate instrumented measurement records it.

## Minimum Execution Steps

Use these steps only while the boundary above remains true:

1. Confirm `D:` is `NOD_G474RE`.
2. Confirm source BIN SHA256 is
   `362C510E4F682751F0721B54F306F6E144951F03F9FF875E68E238D92A29BB31`.
3. Confirm no `D:\FAIL.TXT` is present before copy.
4. Copy only
   `.tmp\manual_gate_waveform_build_only_2026-06-21_clean\stdrive101_gate_waveform_candidate_image.bin`
   to `D:\stdrive101_gate_waveform_candidate_image.bin`.
5. Check whether `D:\FAIL.TXT` is present after copy.
6. Do not proceed to 24 V, Motor Pilot, Motor Profiler, or motor connection
   from this entry.

## Result Status

This record opens the USB-only mass-storage copy but does not contain the copy
result or measured post-download CN3 / REG12 result yet.

After the copy command and `FAIL.TXT` check, create a separate download result
record that names the observed outcome.
