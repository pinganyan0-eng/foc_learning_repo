# STDRIVE101 PA7 LIN1 Wake nFAULT 1.3V Fault Isolation Result - 2026-06-21

## Summary

- Evidence ID:
  `EV-2026-06-21-STDRIVE101-PA7-LIN1-WAKE-NFAULT-1V3-FAULT-ISOLATION-001`.
- Task ID:
  `TASK-2026-06-21-stdrive101-pa7-lin1-wake-nfault-1v3-fault-isolation`.
- Context:
  after the open-loop / CN3 no-waveform correction, the diagnostic returned to
  a minimal `PA7 hold high` firmware image to isolate whether the MCU output,
  power-board input route, STDRIVE101 wake, or `nFAULT` path was the blocker.
- Firmware image:
  `.tmp/stdrive101_pa7_hold_high_2026-06-21_clean/stdrive101_pa7_hold_high_image.bin`,
  size `716` bytes, SHA256
  `1446F3E8A297FB82AAD4FA2710082C76245407116D3E83A21506B38912977F77`.

## User-Reported Measurements

- `NUCLEO CN10-15 / PA7 = 3.3 V` after the PA7 hold-high image was copied.
- Power-board `CN8 P2 / LIN1 = 3.3 V`, so the `PA7 -> LIN1` wire / connector
  route was not the immediate blocker.
- With HSPY applied at the bounded static check, user reported:
  `VS / 24V_FUSED = 24 V`, `REG12 = 12 V`, and `nFAULT = 1.3 V`.
- `CN8 P13 / nFAULT = 1.3 V` and `NUCLEO CN10-16 / PB12 = 1.3 V`.
- After disconnecting the `nFAULT -> PB12` wire, power-board
  `CN8 P13 / nFAULT` remained `1.3 V`, localizing the pull-down / fault
  condition to the power board or STDRIVE101 side rather than the NUCLEO PB12
  side.
- No-power R3 pull-up checks were corrected by the user to:
  `R3 body = 10 kohm`,
  `R3 3V3 side -> CN8 P14 / 3V3 = 0 ohm`, and
  `R3 nFAULT side -> CN8 P13 / nFAULT = 0 ohm`.
- No-power SCREF-related checks reported:
  `SCREF -> GND = 33 kohm`, `SCREF -> 3V3 = 33 kohm`,
  `R1 / R2 body = 33 kohm / 20 kohm`, and both checked R2 endpoint
  continuities as `0 ohm`.

## Interpretation

The `PA7 -> LIN1` route and STDRIVE101 wake path are now separated from the
fault symptom:

```text
PA7 / CN10-15 = 3.3 V
-> CN8 P2 / LIN1 = 3.3 V
-> VS / 24V_FUSED = 24 V
-> REG12 = 12 V
-> nFAULT remains around 1.3 V on the power-board side
```

This means `REG12` can rise and the driver is leaving standby under the LIN1
stimulus. The remaining blocker is not that PA7 failed to drive LIN1, and it
is not explained by an open R3 pull-up chain. Because disconnecting PB12 did
not restore `nFAULT`, the fault symptom is localized to the power-board /
STDRIVE101 side.

The strongest current working hypothesis remains a STDRIVE101 fault condition
triggered by the `LIN1 -> GLS1 -> Q2 low-side -> OUT1 / phase-U ->
GND_POWER` path, such as VDS monitoring seeing an unexpected OUT1 / low-side
state. This is still an inference, not a confirmed component failure.

## Decision

`STDRIVE101 PA7 LIN1 wake nFAULT 1.3V fault isolation result / PA7 hold-high
image copied by ST-LINK mass storage / PA7 CN10-15 = 3.3 V / CN8 P2 LIN1 =
3.3 V / VS 24V_FUSED = 24 V / REG12 = 12 V / nFAULT = 1.3 V on both CN8 P13
and NUCLEO CN10-16 / nFAULT remains 1.3 V after PB12 wire disconnected /
R3 pull-up body and endpoint continuity corrected as 10 kohm and 0 ohm / R3
pull-up value and NUCLEO PB12 not primary blocker / STDRIVE101 wakes but
reports or holds a power-board-side fault state / current primary hypothesis
is low-side phase-U VDS or related driver-output path after LIN1 stimulus /
no repeated motor run / no Motor Pilot / no Motor Profiler / no Hall
closed-loop validation / no sensorless claim / no power-stage readiness / no
motor-readiness claim`.

## Boundary

This record is fault-isolation evidence only. It does not validate PWM output,
phase-output behavior, power-stage readiness, motor readiness, Hall closed
loop, sensorless operation, or safe drive operation.

Do not install a `100 ohm` `nFAULT` pull-up. It would force excessive sink
current if the driver pulls `nFAULT` low and would not address the current
evidence that R3 is already populated and connected.

## Next Checkpoint

Do not repeat the motor-connected open-loop run from this state.

The next useful hardware discussion with the teacher is to distinguish:

- `LIN1`-specific low-side / phase-U / VDS path fault; from
- common STDRIVE101 protection / CP / SCREF / soldering / chip issue.

The lowest-risk next diagnostic, only after teacher review and with the motor
disconnected, is a bounded wake comparison using a high-side input such as:

```text
3.3 V -> 10 kohm -> CN8 P1 / HIN1
LIN1 disconnected
HSPY 24 V / 0.2 A
measure REG12 and nFAULT
```

If `REG12 = 12 V` and `nFAULT` returns near `3.3 V` under `HIN1`, the issue
is more likely concentrated around the `LIN1 / GLS1 / Q2 / OUT1` low-side
path. If `nFAULT` remains around `1.3 V`, the issue is more likely a common
driver / protection / soldering problem.
