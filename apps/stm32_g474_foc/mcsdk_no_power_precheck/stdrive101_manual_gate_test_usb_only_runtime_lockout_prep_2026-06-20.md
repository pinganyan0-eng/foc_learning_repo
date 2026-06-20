# STDRIVE101 Manual Gate-Test USB-Only Runtime Lockout Prep - 2026-06-20

## Summary

- Evidence ID:
  `EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-USBONLY-RUNTIME-LOCKOUT-PREP-001`.
- Task ID:
  `TASK-2026-06-20-stdrive101-manual-gate-test-usbonly-runtime-lockout-prep`.
- Scope:
  Gate C preparation record for a future USB-only runtime lockout check.
- Hardware action:
  none.
- Firmware runtime action:
  none; no flash, no Run / Debug, no USB runtime execution in this record.
- Decision:
  `STDRIVE101 manual gate-test USB-only runtime lockout preparation no-power /
  object-only lockout build pass carried forward / exact source and object
  provenance recorded / future runtime must be USB-only with no 24 V, motor
  disconnected, power board not powered, and six driver inputs expected low /
  preparation only / no flash / no runtime / no PWM-output validation / no
  powered-drive readiness`.

## Boundary

This record is a preparation gate only. It does not authorize:

- firmware flash;
- Run / Debug;
- USB runtime execution;
- 24 V;
- power-board powered connection;
- Gate PWM output;
- oscilloscope gate probing;
- Motor Pilot;
- Motor Profiler;
- motor connection;
- Hall closed loop;
- sensorless operation;
- power-stage readiness or motor readiness.

## Inputs Carried Forward

The current accepted source package is:

```text
apps/stm32_g474_foc/mcsdk_no_power_precheck/manual_gate_test_lockout_build_only_2026-06-20/
```

Source and build-file provenance:

| File | SHA256 |
| --- | --- |
| `Inc/gate_test_lockout.h` | `E1E69943BFEBC50C12C8FAAEE12203BD4FE5D9A6474E318C9EC10AA8111A9862` |
| `Src/gate_test_lockout.c` | `C5277630BC99E4BA1966799699F6660CA6ABB361EE17FF0AC89D8369135B264B` |
| `Src/main_lockout.c` | `D6BD1CB9BA4C54774E06C4B9381EA94C86903F7FB08426CAC904AEFB1DFB3EE3` |
| `CMakeLists.txt` | `B3887E85544EF5BB89309200689276312CF2D6BA0287CCAA89684B1F23190CE1` |

The current object-only build pass is recorded in:

```text
stdrive101_manual_gate_test_lockout_object_build_pass_2026-06-20.md
```

Object files from that pass:

| Object file | Size | SHA256 |
| --- | ---: | --- |
| `gate_test_lockout.c.obj` | `2084` bytes | `C395D049FDCFC3213B65DF2813E07A663B5BF09D7C983BD2FBEC7025F0B79FE8` |
| `main_lockout.c.obj` | `924` bytes | `B2C77D50306258F7A7FFAE745119B17F9E18E703DC39A98CDC0810ACC4C66D98` |

No lockout ELF, HEX, BIN, or MAP linked firmware image exists in the current
evidence chain.

## Future Flash Image Boundary

Before any later USB-only runtime lockout execution can be opened, a separate
dated phase gate must record a linked firmware image boundary.

That future record must include:

| Requirement | Required evidence before execution |
| --- | --- |
| Same lockout source | All source hashes above either match exactly or a new source review replaces this record. |
| Link provenance | Exact linker script, startup file, vector table source, compiler, generator, build command, and output path are recorded. |
| Image artifacts | ELF and MAP are recorded at minimum; HEX or BIN only if explicitly used for flash. |
| Forbidden ingress absent | Static grep confirms no `MC_StartMotor1`, `MCI_START`, PC13 start/stop, MCP / Motor Pilot ingress, `R3_2_TurnOnLowSides`, `PWMC_SwitchOnPWM`, or `LL_TIM_EnableAllOutputs` in the lockout image path. |
| Output lock retained | The image path still forces `PA8`, `PA9`, `PA10`, `PB13`, `PB14`, and `PB15` low as GPIO outputs, keeps `PB12 / nFAULT` input, keeps TIM1 `CCER = 0`, clears `MOE` / `AOE`, and leaves break enabled. |
| Rollback image | Prior known firmware state or an explicit do-not-restore decision is recorded before flash. |

If any item is missing, the later phase stops at build evidence and does not
execute runtime.

## Future USB-Only Physical Boundary

If a later phase explicitly opens USB-only runtime execution, the bench state
must be:

| Item | Required state |
| --- | --- |
| HSPY / 24 V | OFF and physically not powering the board. |
| `VS / 24V_FUSED` | Confirmed below `1 V` before USB runtime. |
| Motor | Disconnected. |
| Gate / phase loads | No motor and no intentional phase load. |
| Wake resistor | Removed; no `10 kohm` wake stimulus installed. |
| Motor Pilot / Profiler | Closed / unused. |
| Debugger action | Only the explicitly reviewed USB-only lockout image may be flashed or run. |

This future state is still no-24V and no-motor. It is not a gate waveform test.

## Expected Future USB-Only Readback

The future USB-only runtime check should measure only MCU-facing static states:

| Measurement | Expected safe reading |
| --- | --- |
| `CN3_1` driver input | close to `0 V` |
| `CN3_2 / LIN1` | close to `0 V` |
| `CN3_3` driver input | close to `0 V` |
| `CN3_4` driver input | close to `0 V` |
| `CN3_5` driver input | close to `0 V` |
| `CN3_6` driver input | close to `0 V` |
| `CN3_13 / nFAULT` | high if pulled by the USB-side circuit; record raw value |
| `CN3_14 / 3V3` | about `3.3 V` if USB/ST-LINK supplies it |
| `VS / 24V_FUSED` | below `1 V` |
| `REG12` | no required 12 V expectation because 24 V is absent |

Do not judge `REG12` wake behavior in USB-only runtime. `REG12` behavior was a
24 V STDRIVE101 wake diagnostic and is not the target of this no-24V phase.

## Stop Rules For The Future Phase

Stop immediately and remove USB power / stop debug session if any of these
occur during a later approved USB-only runtime:

- any of `CN3_1` through `CN3_6` is stable above `0.3 V`;
- `VS / 24V_FUSED` is not below `1 V`;
- the flashed image provenance does not match the reviewed lockout image;
- the debugger enters normal MCSDK application code instead of the lockout
  loop;
- the board resets repeatedly, heats, smells, makes sound, or LEDs behave
  unexpectedly;
- a probe slips or a measurement point is uncertain.

Do not continue by "trying one more time" after a stop-rule event. Record the
raw observation and return to no-power source review.

## User Table For The Future Phase

Do not fill this table from memory. Use it only if a later dated phase opens
USB-only runtime execution.

| Item | Reading |
| --- | --- |
| image name / path | `___` |
| image hash | `___` |
| HSPY state | `OFF / disconnected` |
| `VS / 24V_FUSED` before USB | `___ V` |
| motor disconnected | `yes / no` |
| wake resistor removed | `yes / no` |
| `CN3_1` | `___ V` |
| `CN3_2 / LIN1` | `___ V` |
| `CN3_3` | `___ V` |
| `CN3_4` | `___ V` |
| `CN3_5` | `___ V` |
| `CN3_6` | `___ V` |
| `CN3_13 / nFAULT` | `___ V` |
| `CN3_14 / 3V3` | `___ V` |
| `REG12` | `___ V` |

## Next Allowed Checkpoint

The next allowed checkpoint after this preparation record is a linked-image
build-boundary plan or build-only record for the lockout image.

Still forbidden until another dated phase gate opens it:

- flash;
- Run / Debug;
- USB runtime execution;
- 24 V;
- Gate PWM output;
- Motor Pilot / Profiler;
- motor connection.
