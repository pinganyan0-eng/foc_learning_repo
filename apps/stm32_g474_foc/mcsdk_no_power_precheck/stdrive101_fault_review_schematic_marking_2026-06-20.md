# STDRIVE101 Fault Review Schematic Marking - 2026-06-20

## Boundary

This is a no-power source-marking artifact after the single-input wake result
where `REG12 = 12 V` and `nFAULT = 0 V`.

It marks schematic nets and related components only. It does not authorize
repeat powered wake, alternate input stimulus, firmware implementation,
generated-code edits, CubeMX / Workbench edits, flash, Run / Debug, motor
connection, Gate PWM, Motor Pilot, Motor Profiler, Hall closed-loop
validation, sensorless validation, power-stage readiness, or motor readiness.

The marked images are not physical probing permission. Do not probe U1 pins,
MOSFET pins, or unknown pads by guesswork.

## Source Image

Source schematic screenshot:

```text
hardware/schematic/2026-05-15_power_board_cn8_stdrive101_schematic_candidate.png
```

The source schematic labels the control connector as `CN8`. Existing project
records and the user's bench measurements use `CN3` for the same board-facing
control header route. Treat `CN8` in this source image as the schematic-side
name for the user's measured `CN3` header unless a later board revision source
contradicts it.

## Marked Images

Generated marked images:

```text
hardware/schematic/annotated/stdrive101_fault_review_full_marked_2026-06-20.png
hardware/schematic/annotated/stdrive101_driver_control_nodes_marked_2026-06-20.png
hardware/schematic/annotated/stdrive101_phase_u_out1_gls1_q2_marked_2026-06-20.png
```

## Marked Nodes

| Label | Schematic item | Why it matters now |
| --- | --- | --- |
| 1 | `CN8` on the schematic, corresponding to the measured `CN3` header route | Connector-side map for `LIN1`, `nFAULT`, `3V3`, and `GND` evidence. |
| 2 | `CN3_2 / LIN1`: `CN8` pin 2 -> `R21 10R` -> U1 pin 10 `INL1/EN1` | This is the single-input stimulus path used in the wake test. |
| 3 | `CN3_13 / nFAULT`: `CN8` pin 13, U1 pin 6, `R3 10k` pull-up, `LED1` | This is the observed low fault output during the wake test. |
| 4 | `CP`: U1 pin 1 plus `C1 100 nF` to `GND_POWER` | CP comparator remains a secondary `nFAULT` review target. |
| 5 | `SCREF`: U1 pin 3, `R1 33k` to `3V3`, `R2 20k` to `GND_SIGNAL` | SCREF sets the VDS monitoring threshold and is the primary source-review focus. |
| 6 | `REG12`: U1 pin 5, `C4/C5`, bootstrap diodes `D1-D3` | `REG12` rose during the wake test; source marking confirms its local network. |
| 7 | `OUT1 / phase-U`: Q1 source plus Q2 drain, also `CN7` pin 1 | Low-side VDS monitoring depends on this node when `GLS1` is commanded. |
| 8 | `GHS1`: U1 pin 22 -> `R23 22R` -> Q1 high-side gate | High-side path is marked for context; it was not the intended commanded path. |
| 9 | `GLS1`: U1 pin 24 -> `R24 22R` -> Q2 low-side gate | `LIN1` high can command this low-side gate path after wake. |
| 10 | Q2 low-side source / `ADC_U` / `R25 20 mR` to `GND_POWER` | This is the low-side source / current-shunt return path for phase U. |
| 11 | `GND_SIGNAL` and `GND_POWER` through `R_GND_ISO 0R` | Ground-domain clue for interpreting no-power resistance paths. |

## Current Interpretation

The marked source supports the existing cause ranking:

```text
LIN1 high
-> U1 pin10 INL1/EN1 can command the phase-U low-side path
-> GLS1 drives through R24 to Q2 gate
-> OUT1 should be pulled toward the low-side source path if Q2 turns on
-> abnormal OUT1 / low-side VDS behavior can fit the latched nFAULT pattern
```

This remains an inference. The marking does not prove the board-level fault
cause and does not clear any repeat powered diagnostic.

## Safe Use

Use the images to locate source nets and to ask for board-level identification
of safe component pads. For DMM follow-up, measure only points that can be
confidently identified on the physical board and only with:

```text
HSPY output OFF
VS / 24V_FUSED < 1 V
10 kohm stimulus resistor removed
Motor disconnected
USB/ST-LINK unplugged unless a later no-power source-photo task needs it
DMM continuity / resistance mode only
```

If `SCREF`, `CP`, `REG12`, `OUT1`, `GLS1`, Q2 gate, Q2 drain, or Q2 source
cannot be identified with certainty on the real PCB, do not probe them. Provide
a board photo or EDA/netlist crop first.

## Decision

`STDRIVE101 fault review schematic marking / source image marked for CN8-CN3,
LIN1, nFAULT, CP, SCREF, REG12, OUT1, GHS1, GLS1, Q2 low-side path, and
GND domains / supports VDS-monitoring source review after LIN1 low-side
command / no unknown-node probing / no repeat powered wake / no PWM-output
validation / no powered-drive readiness`.

## Next User Checkpoint

No power. Use the marked images only to identify the physical board area. If a
point is not physically certain, send a clear board photo or EDA crop instead
of touching it with a probe.
