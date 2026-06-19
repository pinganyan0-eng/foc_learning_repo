# CN3 B1 Static Power nFAULT Measurement - 2026-06-19

## Scope

This file records user-reported bench measurements from a bounded hardware
check:

```text
CN3 connected
B1 not pressed, then B1 pressed briefly for comparison
Bench supply 24 V / 0.2 A current limit
No motor connected
No PWM or gate-output readiness claimed
```

This record is measurement evidence only. It does not authorize flashing,
Run/Debug, Motor Profiler, Motor Pilot, motor connection, gate PWM output, Hall
closed loop, sensorless operation, or power-stage readiness.

## Setup

- Bench supply: HSPY-30-05, 24.00 V setpoint, 0.200 A current limit.
- Supply state during static checks: CV.
- CN3 connected to NUCLEO-side harness during powered checks.
- Motor: not connected.
- B1: not pressed for the main static check; briefly pressed only after
  USB-only input checks showed all HIN/LIN lines remained 0 V.

## Raw Measurements

Initial powered check before LED1 removal:

```text
24V / 24V_FUSED / VS: 24 V
3V3: 3.3 V
REG12: 0.5 V, later 0.3 V at the confirmed REG12 capacitor side
nFAULT / CN3_13 / PB12: 1.7 V
Supply current: 0.036 A, CV
```

Power-off resistance and continuity checks:

```text
REG12 -> GND: 11 Mohm
24V input -> GND: 0.3 Mohm
nFAULT -> GND: 55 Mohm
R_GND_ISO: continuity present
24V negative -> CN3_15/P15 GND: continuity present
R3-A -> R3-B: 10 kohm
R3-A -> CN3_14 / 3V3: 0 ohm
R3-B -> CN3_14 / 3V3: 10 kohm
R3-A -> CN3_13 / nFAULT: 10 kohm
R3-B -> CN3_13 / nFAULT: 0 ohm
```

LED1 check before removal:

```text
LED1 one side -> R3-B / CN3_13 / nFAULT: continuity present
LED1 other side -> GND: continuity present
Diode mode, red nFAULT and black GND: about 1.7 V
Diode mode, red GND and black nFAULT: about 0.6 V
```

Checks after LED1 removal:

```text
CN3_13 / nFAULT -> CN3_14 / 3V3: about 10 kohm
Diode mode, red nFAULT and black GND: open
Supply current: 0.036 A, CV
CN3_14 / 3V3: 3.3 V
CN3_13 / nFAULT: 3.3 V
REG12: 0.3 V
```

Input-state checks:

```text
USB-only, B1 not pressed: HIN1/LIN1/HIN2/LIN2/HIN3/LIN3 all 0 V
USB-only, B1 pressed: HIN1/LIN1/HIN2/LIN2/HIN3/LIN3 all 0 V
24 V / 0.2 A, B1 not pressed: nFAULT 3.3 V, REG12 0.3 V, current 0.036 A
24 V / 0.2 A, B1 pressed briefly: nFAULT 3.3 V, REG12 0.3 V, current 0.036 A
```

Firmware identity query:

```text
COM5 detected as STMicroelectronics STLink Virtual COM Port
115200 8N1 read-only probe: no periodic output
Sent PING: no reply
Sent MODE?: no reply
```

## Decisions

- The original `nFAULT = 1.7 V` reading was explained by LED1 being connected
  from nFAULT to GND. With R3 = 10 kohm to 3V3, that path held nFAULT near the
  LED forward voltage.
- After LED1 removal, nFAULT returned to 3.3 V under the bounded static
  condition. This supports only the static nFAULT pull-up/release check.
- VS reached the STDRIVE101 local supply capacitors at 24 V, while REG12 stayed
  at 0.3 V. Because all HIN/LIN inputs were 0 V and B1 did not change them,
  this is treated as standby or not-yet-woken behavior pending firmware and
  driver-state evidence, not as active gate-drive validation.
- The NUCLEO firmware identity is unknown. It did not respond to the previous
  baseline safety commands `PING` or `MODE?`.

## Next Gate

Before any further powered or PWM-related experiment:

1. Keep HSPY output off and motor disconnected.
2. Confirm or install a known USB-only safety firmware through a separately
   approved flash gate.
3. Prove the safety firmware keeps all CN3 HIN/LIN outputs low at reset and
   does not set TIM output enable or start motor-control PWM.
4. Only after that evidence exists, define a new bounded REG12 wake-up check.

Do not use this record to claim motor readiness, power-stage readiness, gate PWM
safety, Hall readiness, or sensorless readiness.
