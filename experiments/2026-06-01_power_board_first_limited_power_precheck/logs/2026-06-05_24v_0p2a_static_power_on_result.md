# 2026-06-05 24V/0.2A static power-on result

Evidence ID: `EV-2026-06-05-HW-STATIC-PWR-001`

## Scope

This record captures the first user-reported limited static power-on result for the self-designed STDRIVE101 power board.

Boundary:

- Power board only.
- No motor connected.
- No NUCLEO/MCU drive connected.
- No PWM output.
- HSPY supply current limit kept at the 0.2A level.
- This result does not authorize motor connection, PWM output, or higher current testing.

## Equipment

| Item | Record |
| --- | --- |
| Power supply | Han Sheng Pu Yuan HSPY-30-05 |
| Supply target | 24V |
| Current limit | 0.2A level |
| Meter | User-reported DMM readings |

## Measurements

| Item | Result | Judgment |
| --- | --- | --- |
| Supply mode | CV | Pass |
| Input current | 0.04A | Pass |
| 5V -> GND | 5V | Pass |
| 3V3 -> GND | 3.34V | Pass |
| REG12 -> GND | 12V | Pass |
| nFAULT -> GND | 3.3V | Pass |
| Abnormal smell/sound/fast heating | None reported | Pass |

## Conclusion

The first 24V/0.2A-level limited static power-on check passed based on the user-reported measurements above. The basic supply rails and nFAULT state look normal under limited static conditions.

This proves only static supply sanity under current limit. It does not prove Gate waveform correctness, dead-time correctness, current-sense correctness, phase output correctness, motor-drive capability, or FOC closed-loop capability.

## Next Allowed Work

The next allowed work is a separately planned MCU connection and empty PWM/Gate waveform check:

- Keep motor disconnected.
- Keep supply current-limited.
- Confirm nFAULT, VS/REG12/VREG, and logic rails before PWM.
- Use an oscilloscope for Gate/input waveform review.
- Do not move to motor connection until empty PWM, Gate waveform, dead time, and current-sense sanity checks have passed.
