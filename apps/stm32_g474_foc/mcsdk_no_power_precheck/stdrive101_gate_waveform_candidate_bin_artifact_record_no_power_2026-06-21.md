# STDRIVE101 Gate-Waveform Candidate BIN Artifact Record No-Power - 2026-06-21

## Summary

- Evidence ID:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-CANDIDATE-BIN-ARTIFACT-RECORD-NO-POWER-001`.
- Task ID:
  `TASK-2026-06-21-stdrive101-gate-waveform-candidate-bin-artifact-record-no-power`.
- Scope:
  downloadable BIN artifact preparation for the existing Gate E2 waveform
  candidate linked image.
- Source image:
  `.tmp/manual_gate_waveform_build_only_2026-06-21_clean/stdrive101_gate_waveform_candidate_image.elf`.
- Source MAP:
  `.tmp/manual_gate_waveform_build_only_2026-06-21_clean/stdrive101_gate_waveform_candidate_image.map`.
- Generated BIN:
  `.tmp/manual_gate_waveform_build_only_2026-06-21_clean/stdrive101_gate_waveform_candidate_image.bin`.
- Decision:
  `STDRIVE101 gate-waveform candidate BIN artifact record no-power / Gate E2
  waveform candidate linked ELF converted to downloadable BIN / converter
  output validated against the prior neutral-wrapper objcopy BIN / candidate
  ELF SHA256 10BA818730E259AEBA8A5C5E5C96CFBA32FCB90AAA4136B775022B9D69ADCE7C
  / candidate MAP SHA256
  170EA77C566F98CF9EF2AC88F76B154238A5404DC705AAE3917BEAE7C1503D4C /
  candidate BIN SHA256
  362C510E4F682751F0721B54F306F6E144951F03F9FF875E68E238D92A29BB31 /
  candidate BIN size 1852 bytes / retained MAP symbol
  gate_waveform_candidate_run_once at 0x080005bc / no forbidden normal-MCSDK
  MAP symbols found in the checked screen / BIN artifact only / no USB copy /
  no flash / no Run Debug / no 24 V execution / no Gate PWM output / no Motor
  Pilot / no Motor Profiler / no motor connection / no powered-drive
  readiness`.

## Conversion Evidence

The external STM32Cube GNU Arm `objcopy` executable in `AppData` was not
available through the current sandbox approval path. The fallback converter
used the ELF32 little-endian program-header `PT_LOAD` data range only.

Before generating the candidate BIN, the same converter was checked against
the already-recorded neutral-wrapper objcopy BIN:

| Check | Value |
| --- | --- |
| Neutral-wrapper converter output SHA256 | `CA2A42F2F83C42EA9E7BEC628BD8656A422DBE767CFFD5A5865BE781603D3D71` |
| Existing neutral-wrapper objcopy BIN SHA256 | `CA2A42F2F83C42EA9E7BEC628BD8656A422DBE767CFFD5A5865BE781603D3D71` |
| Match | yes |
| Neutral-wrapper BIN size | `1044` bytes |

Candidate ELF load-image layout:

| Field | Value |
| --- | --- |
| Load base | `0x08000000` |
| Load end | `0x0800073c` |
| `PT_LOAD` file size | `1852` bytes |
| `PT_LOAD` memory size | `1852` bytes |
| `PT_LOAD` flags | `5` |

## Artifact Identity

| Artifact | Size | SHA256 |
| --- | ---: | --- |
| `.tmp/manual_gate_waveform_build_only_2026-06-21_clean/stdrive101_gate_waveform_candidate_image.elf` | `26132` | `10BA818730E259AEBA8A5C5E5C96CFBA32FCB90AAA4136B775022B9D69ADCE7C` |
| `.tmp/manual_gate_waveform_build_only_2026-06-21_clean/stdrive101_gate_waveform_candidate_image.map` | `32352` | `170EA77C566F98CF9EF2AC88F76B154238A5404DC705AAE3917BEAE7C1503D4C` |
| `.tmp/manual_gate_waveform_build_only_2026-06-21_clean/stdrive101_gate_waveform_candidate_image.bin` | `1852` | `362C510E4F682751F0721B54F306F6E144951F03F9FF875E68E238D92A29BB31` |

## Symbol Boundary

The candidate MAP retains the waveform entry point:

```text
0x080005bc gate_waveform_candidate_run_once
```

It also retains:

```text
0x0800051c wait_for_pwm_periods_or_fault
0x080005a4 gate_waveform_candidate_force_idle_low
```

The checked MAP screen found no matches for:

```text
MC_StartMotor1
MCI_START
PC13
MCP
ASPEP
Motor Profiler
Motor Pilot
R3_2_TurnOnLowSides
PWMC_SwitchOnPWM
LL_TIM_EnableAllOutputs
HALL_M1
HAL_Delay
printf
malloc
free
_sbrk
```

## Boundary

This record creates a candidate BIN artifact only. It does not copy the BIN to
ST-LINK mass storage, does not change the image currently on the board, and
does not execute the waveform window.

It does not authorize or prove:

- flash / Run / Debug;
- 24 V execution;
- Gate PWM output on hardware;
- waveform correctness on hardware;
- Motor Pilot;
- Motor Profiler;
- motor connection;
- Hall closed loop;
- sensorless operation;
- power-stage readiness or motor readiness.

## Next Checkpoint

The next engineering checkpoint may only be a separate waveform-candidate
USB-only download execution entry after explicit user confirmation that:

- HSPY / 24 V is OFF and physically disconnected;
- motor is disconnected;
- Motor Pilot / Profiler are closed;
- no `10 kohm` wake resistor or LIN1 stimulus is installed;
- the user explicitly authorizes copying
  `stdrive101_gate_waveform_candidate_image.bin` to the ST-LINK mass-storage
  drive.

After that separate USB-only download record, the later hardware checkpoint is
still no-motor, short-window, instrumented waveform observation only.
