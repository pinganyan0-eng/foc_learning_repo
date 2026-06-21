# STDRIVE101 Gate-Waveform Neutral-Wrapper USB-Only Download Execution Entry - 2026-06-21

## Summary

- Evidence ID:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-USBONLY-DOWNLOAD-EXECUTION-ENTRY-001`.
- Task ID:
  `TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-usbonly-download-execution-entry`.
- Scope:
  execution-entry record for one USB-only ST-LINK mass-storage copy of the
  neutral-wrapper BIN artifact.
- User request:
  `现在仍是 USB-only，24V 断开，电机断开，允许复制 neutral-wrapper BIN 到 D:`
- User-confirmed physical boundary:
  USB-only; 24 V disconnected; motor disconnected.
- Decision:
  `STDRIVE101 gate-waveform neutral-wrapper USB-only download execution entry /
  user confirmed USB-only, 24V disconnected, motor disconnected, and allowed
  copying neutral-wrapper BIN to D: / candidate ELF hash matched neutral-wrapper
  build-only record / candidate BIN hash matched neutral-wrapper BIN artifact
  record / D: volume label NOD_G474RE detected and FAIL.TXT absent before copy /
  opens exactly one USB-only mass-storage BIN copy / no Run Debug / no 24 V /
  no Gate PWM output / no Motor Pilot / no Motor Profiler / no motor
  connection / no powered-drive readiness`.

## Boundary

This record opens exactly one USB-only copy of the neutral-wrapper BIN to the
ST-LINK mass-storage volume. It does not open any other firmware workflow.

Still forbidden:

- 24 V;
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
| Transfer target | `D:\stdrive101_gate_waveform_neutral_wrapper_image.bin` |
| ST-LINK volume | `D:` / `NOD_G474RE` |

Accepted source/build evidence:

- `stdrive101_gate_waveform_neutral_wrapper_build_only_record_no_power_2026-06-21.md`;
- `stdrive101_gate_waveform_neutral_wrapper_bin_artifact_record_no_power_2026-06-21.md`;
- retained ELF symbol screen includes
  `gate_waveform_neutral_wrapper_hold_idle_forever`;
- retained ELF symbol screen has no
  `gate_waveform_candidate_run_once`.

## Allowed Execution Envelope

Only this envelope is opened:

| Item | Allowed state |
| --- | --- |
| Power | USB / ST-LINK only |
| HSPY / 24 V | disconnected |
| Motor | disconnected |
| Transfer method | direct mass-storage copy to `D:\NOD_G474RE` |
| Runtime goal | prepare for USB-only neutral-state DMM measurement |
| Result check | check whether `D:\FAIL.TXT` appears after copy |

Do not use Motor Pilot, Motor Profiler, normal MCSDK start buttons, PC13
start/stop, MCP commands, Run / Debug, or any command path that requests PWM
output.

## Minimum Execution Steps

Use these steps only while the boundary above remains true:

1. Confirm `D:` is `NOD_G474RE`.
2. Confirm source BIN SHA256 is
   `CA2A42F2F83C42EA9E7BEC628BD8656A422DBE767CFFD5A5865BE781603D3D71`.
3. Confirm no `D:\FAIL.TXT` is present before copy.
4. Copy only
   `.tmp/gwnw_build_2026-06-21_clean/stdrive101_gate_waveform_neutral_wrapper_image.bin`
   to `D:\stdrive101_gate_waveform_neutral_wrapper_image.bin`.
5. Check whether `D:\FAIL.TXT` is present after copy.
6. Do not proceed to 24 V, Motor Pilot, Motor Profiler, Gate PWM output, or
   motor connection.

## Result Status

This record opens the USB-only mass-storage copy but does not contain the copy
result or measured neutral-state result yet.

After the copy command and `FAIL.TXT` check, create a separate download result
record or append a dated result record that names the observed outcome.

After the user reports the DMM table, create a separate USB-only neutral-state
runtime result record.
