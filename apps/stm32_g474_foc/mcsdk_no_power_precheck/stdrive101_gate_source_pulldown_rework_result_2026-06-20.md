# STDRIVE101 Gate-Source Pulldown Rework Result - 2026-06-20

## Boundary

This record captures the user-reported no-power follow-up after the
STDRIVE101 single-input wake result where `REG12 = 12 V` and `nFAULT = 0 V`.

This is no-power DMM evidence only. It does not authorize repeat powered wake,
alternate input stimulus, firmware implementation, generated-code edits,
CubeMX / Workbench edits, flash, Run / Debug, motor connection, Gate PWM,
Motor Pilot, Motor Profiler, Hall closed-loop validation, sensorless
validation, power-stage readiness, or motor readiness.

## Context

The user reported an intermediate abnormal gate-source path around the phase
gate pulldown network:

```text
Q2 / Q4 / Q6 low-side gate-source paths were initially found around 3.7 kohm
Q1 high-side gate-source path was normal
Q3 / Q5 high-side gate-source paths were being debugged around their 10 kohm
pulldown resistors and OUT2 / OUT3 source nodes
```

After focused rework and retest, the user reported the final six-route
gate-source check as:

```text
VS_OFF_V = 0 V
10k_removed = yes

Q1_GS = 10 kohm
Q3_GS = 10 kohm
Q5_GS = 10 kohm
Q2_GS = 10 kohm
Q4_GS = 10 kohm
Q6_GS = 10 kohm
```

The user confirmed `VS_OFF_V = 0 V` after the gate-source readings. This
closes the missing power-off-voltage field for this no-power record. The
power-off state must still be rechecked before any later wiring change or
powered retest.

## Interpretation

The six reported gate-source pulldown readings are now symmetric and match the
nominal `10 kohm` pulldown intent on the marked source schematic.

This closes the specific no-power branch that suspected a stable gate-source
short, missing pulldown, or wrong high-side source-node measurement around the
phase gate network.

This does not prove the original powered `nFAULT = 0 V` cause. It only means
the obvious gate-source pulldown fault branch is no longer indicated in the
latest no-power readings.

## Remaining Hardware Boundary

Before any future powered retest is proposed or executed, the setup must be
confirmed again:

```text
VS / 24V_FUSED < 1 V before changing wiring
10 kohm stimulus removed
Motor disconnected
USB/ST-LINK unplugged
No PWM / firmware run / Motor Pilot / Motor Profiler
```

Any future repeat of the single-input wake diagnostic must be a separate
bounded decision and must keep the original stop rules:

```text
HSPY 24 V / 0.2 A
CN3_14 / 3V3 -> 10 kohm series resistor -> CN3_2 / LIN1
record HSPY CV/CC, current, LIN1, nFAULT, REG12
HSPY OFF immediately on CC, current anomaly, nFAULT low, unstable reading, or
any physical abnormality
```

## Decision

`STDRIVE101 gate-source pulldown rework result / Q1-GS 10 kohm / Q3-GS
10 kohm / Q5-GS 10 kohm / Q2-GS 10 kohm / Q4-GS 10 kohm / Q6-GS 10 kohm /
previous gate-source pulldown anomaly branch no longer indicated / original
nFAULT cause not proven / no repeat powered wake yet / no PWM-output
validation / no powered-drive readiness`.

## Next User Checkpoint

Decide whether to keep collecting no-power evidence or prepare a separate
bounded single-input wake retest plan. Do not connect a motor or run PWM.
