# STDRIVE101 Manual Gate-Test USB-Only Runtime Lockout Result - 2026-06-20

## Summary

- Evidence ID:
  `EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-USBONLY-RUNTIME-LOCKOUT-RESULT-001`.
- Task ID:
  `TASK-2026-06-20-stdrive101-manual-gate-test-usbonly-runtime-lockout-result`.
- Scope:
  measured result for the single USB-only lockout flash / run pass opened by
  `stdrive101_manual_gate_test_usb_only_runtime_lockout_execution_entry_2026-06-20.md`.
- Decision:
  `STDRIVE101 manual gate-test USB-only runtime lockout result / reviewed
  lockout ELF converted to BIN and copied through ST-LINK mass storage /
  no FAIL.TXT after copy / user-reported CN3_1 through CN3_6 all 0 V /
  nFAULT 3.3 V / CN3_14 3.3 V / REG12 0 V / driver-input stop rule not hit /
  USB-only runtime evidence only / no 24 V / no PWM-output validation /
  no Motor Pilot / no Motor Profiler / no motor connection / no
  powered-drive readiness`.

## Boundary

This result records one USB / ST-LINK-only lockout runtime measurement. It
does not authorize:

- 24 V;
- power-board powered runtime;
- Gate PWM output or PWM validation;
- oscilloscope gate probing;
- Motor Pilot;
- Motor Profiler;
- motor connection;
- Hall closed loop;
- sensorless operation;
- power-stage readiness or motor readiness claims;
- any normal generated MCSDK application run.

The practical conclusion is narrow: with USB / ST-LINK only and the reviewed
lockout image, the six MCU-facing STDRIVE101 driver inputs were reported at
`0 V`.

## Image And Download Evidence

Reviewed candidate image:

| Item | Value |
| --- | --- |
| ELF | `.tmp/manual_gate_test_lockout_linked_image/stdrive101_gate_lockout_image.elf` |
| ELF SHA256 | `87BF3F7A28949F8DB654927292083609E52AB46C511CB6191D03B280DBFFE9B6` |
| ELF section start | `.isr_vector` at `0x08000000` |
| BIN generated from ELF | `.tmp/manual_gate_test_lockout_linked_image/stdrive101_gate_lockout_image.bin` |
| BIN size | `1356` bytes |
| BIN SHA256 | `CBF833C8E9289D8B4A952C32C641CAA94928F1F8119C5DC528EBD779915EA6BE` |
| ST-LINK mass-storage drive | `D:` / `NOD_G474RE` |
| ST-LINK details | `Version: V3J17M10`, `Build: Oct 17 2025 15:12:06` |
| Copy target | `D:\stdrive101_gate_lockout_image.bin` |
| Copy result | no `FAIL.TXT` present after copy |

Additional local screens before download:

- ST-LINK debug, virtual COM `COM5`, and mass-storage interfaces were present.
- `arm-none-eabi-size` showed `text=1356`, `data=0`, `bss=1568`.
- `arm-none-eabi-nm` showed `lock_tim1_outputs`, `main`, and
  `Reset_Handler`; no normal MCSDK start / PWM-output enable symbol was used
  as a runtime path.

## Preconditions Carried Forward

The execution entry recorded the user-confirmed physical boundary before the
USB-only pass:

| Item | Confirmed state |
| --- | --- |
| HSPY / 24 V | `OFF` and physically disconnected |
| `VS / 24V_FUSED` | `< 1 V` before execution |
| Motor | disconnected |
| `10 kohm` wake resistor / `LIN1` stimulus | removed |
| Motor Pilot / Profiler | closed |
| Board abnormal heat / smell / sound | no abnormal condition reported |

## User-Reported Measurement Table

The user reported the following USB-only measurements after the lockout image
was downloaded:

| Item | Reading |
| --- | ---: |
| `CN3_1` driver input | `0 V` |
| `CN3_2 / LIN1` | `0 V` |
| `CN3_3` driver input | `0 V` |
| `CN3_4` driver input | `0 V` |
| `CN3_5` driver input | `0 V` |
| `CN3_6` driver input | `0 V` |
| `CN3_13 / nFAULT` | `3.3 V` |
| `CN3_14 / 3V3` | `3.3 V` |
| `REG12` | `0 V` |

Stop-rule status:

```text
stop-rule hit: no, based on CN3_1 through CN3_6 all reported at 0 V and no
new abnormal condition reported in this measurement reply.
```

## Interpretation

This is USB-only runtime evidence that the isolated lockout image held the six
MCU-facing STDRIVE101 driver inputs low in the measured state. `nFAULT` and
`3V3` were both reported at `3.3 V`, and `REG12` was reported at `0 V` in the
USB-only state.

This does not prove:

- 24 V runtime behavior;
- REG12 wake behavior under this firmware;
- TIM1 register readback;
- PWM waveform safety;
- gate-driver output behavior;
- motor behavior;
- Hall closed-loop behavior;
- sensorless behavior;
- power-stage readiness or motor readiness.

## Next Checkpoint

The next engineering checkpoint must be a separate dated phase-gate review
before any later 24 V static lockout check, PWM/gate waveform task, or motor
task is considered.

Still forbidden after this result:

- 24 V by default;
- Gate PWM output;
- Motor Pilot / Profiler;
- motor connection;
- power-stage readiness or motor readiness claims.
