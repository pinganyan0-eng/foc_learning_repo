# STDRIVE101 Gate-Waveform Neutral-Wrapper BIN Artifact Record No-Power - 2026-06-21

## Summary

- Evidence ID:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-BIN-ARTIFACT-RECORD-NO-POWER-001`.
- Task ID:
  `TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-bin-artifact-record-no-power`.
- Scope:
  generated and checked the downloadable BIN artifact for the previously
  recorded neutral-wrapper linked image.
- Hardware action:
  none in this record. No board write, no ST-LINK copy, no flash, no Run /
  Debug, no USB runtime execution, and no 24 V.
- Decision:
  `STDRIVE101 gate-waveform neutral-wrapper BIN artifact record no-power /
  neutral-wrapper ELF converted to BIN with STM32Cube GNU Arm objcopy /
  ELF hash matches the neutral-wrapper build-only record /
  BIN artifact produced and hashed / retained ELF symbol screen keeps
  gate_waveform_neutral_wrapper_hold_idle_forever and has no retained
  gate_waveform_candidate_run_once / first drive enumeration had no ST-LINK
  mass-storage volume / later drive enumeration detected D: NOD_G474RE with
  no FAIL.TXT before copy / no copy performed because explicit USB-only
  download authorization was not received / artifact preparation only / no
  flash / no Run Debug / no USB runtime execution / no 24 V / no Gate PWM
  output / no Motor Pilot / no Motor Profiler / no motor connection / no
  powered-drive readiness`.

## Artifact Identity

| Item | Value |
| --- | --- |
| Source ELF | `.tmp/gwnw_build_2026-06-21_clean/stdrive101_gate_waveform_neutral_wrapper_image.elf` |
| ELF size | `12044` bytes |
| ELF SHA256 | `C47C02D379DC5312095DF786BF8C99B58D42323AD9227D0903BCB8C98AAD9591` |
| Source MAP | `.tmp/gwnw_build_2026-06-21_clean/stdrive101_gate_waveform_neutral_wrapper_image.map` |
| MAP SHA256 | `5FB24B2735EFFD402C26BDC3B0D267B26B06DC6522A6B5B5D876491BA9A42A83` |
| Generated BIN | `.tmp/gwnw_build_2026-06-21_clean/stdrive101_gate_waveform_neutral_wrapper_image.bin` |
| BIN size | `1044` bytes |
| BIN SHA256 | `CA2A42F2F83C42EA9E7BEC628BD8656A422DBE767CFFD5A5865BE781603D3D71` |
| Conversion tool | `C:\Users\gregrg\AppData\Local\stm32cube\bundles\gnu-tools-for-stm32\14.3.1+st.2\bin\arm-none-eabi-objcopy.exe` |
| Conversion command | `arm-none-eabi-objcopy -O binary <ELF> <BIN>` |

This is the first neutral-wrapper downloadable artifact for the `C47C...`
image. It is not the earlier lockout image whose ELF SHA256 was
`87BF3F7A28949F8DB654927292083609E52AB46C511CB6191D03B280DBFFE9B6`.

## Symbol Boundary Recheck

The retained ELF symbol screen for the neutral-wrapper image includes:

```text
08000374 T gate_waveform_neutral_wrapper_hold_idle_forever
```

No retained ELF symbol was found for:

- `gate_waveform_candidate_run_once`;
- `main_waveform_candidate`;
- `MC_StartMotor1`;
- `MCI_START`;
- `R3_2_TurnOnLowSides`;
- `PWMC_SwitchOnPWM`;
- `LL_TIM_EnableAllOutputs`;
- `MotorPilot`;
- `Profiler`;
- Hall / PID / speed-loop terms from the normal generated MCSDK app.

The section table remains consistent with the build-only record:

| Section | Size | VMA |
| --- | ---: | --- |
| `.isr_vector` | `0x1d8` | `0x08000000` |
| `.text` | `0x23c` | `0x080001d8` |
| `.data` | `0x0` | `0x20000000` |
| `._user_heap_stack` | `0x600` | `0x20000000` |

## ST-LINK Mass-Storage Check

Initial logical-disk enumeration during this record returned only these
mounted volumes:

| Drive | Volume label | Drive type |
| --- | --- | --- |
| `C:` | `OS` | local disk |
| `E:` | `D` | local disk |
| `F:` | local non-ST-LINK volume | local disk |

After the user reported that the ST-LINK drive was present, a follow-up
enumeration detected:

| Drive | Volume label | Drive type | Free space |
| --- | --- | --- | ---: |
| `D:` | `NOD_G474RE` | removable disk | `1581056` bytes |

The `D:\` directory contained `DETAILS.TXT`, `MBED.HTM`, and `GETSTART.HTM`;
`D:\FAIL.TXT` was not present before any copy attempt.

No BIN copy was attempted in this record because copying to `D:\NOD_G474RE`
is the firmware-download action, and a separate explicit USB-only copy
authorization was not received after the drive appeared. Therefore no
post-copy `FAIL.TXT` result exists for this neutral-wrapper image.

## Boundary

This record moves the work from "linked image exists" to "downloadable BIN
artifact exists and is hashed, with ST-LINK mass storage detected later". It
still does not execute the firmware.

It does not authorize:

- firmware flash or ST-LINK copy;
- Run / Debug;
- USB runtime execution;
- applying 24 V;
- Gate PWM output on hardware;
- oscilloscope probing on live gate or phase nodes;
- normal generated MCSDK application execution;
- Motor Pilot;
- Motor Profiler;
- motor connection;
- Hall closed loop;
- sensorless operation;
- power-stage readiness or motor readiness claims.

## Next Real Checkpoint

The next real hardware-side step is a separate USB-only neutral-wrapper
download / neutral-state execution-entry followed by the actual BIN copy. That
future entry must name this exact BIN hash and must still keep:

- HSPY / 24 V output `OFF` and physically disconnected;
- `VS / 24V_FUSED < 1 V`;
- motor disconnected;
- `10 kohm` wake resistor / `LIN1` stimulus removed;
- Motor Pilot / Profiler closed;
- no abnormal heat, smell, sound, reset loop, or visible issue.

The ST-LINK mass-storage volume was detected as `D:\NOD_G474RE` in the latest
check. The next action is not another plan-only record; it is explicit
USB-only copy authorization followed by copying this BIN to `D:\` and checking
for `FAIL.TXT`. Do not connect 24 V and do not connect a motor for that step.

Still blocked after this artifact record:

- motor power-up;
- any 24 V plus firmware runtime step;
- Gate PWM output;
- Motor Pilot / Profiler;
- power-stage readiness or motor readiness.
