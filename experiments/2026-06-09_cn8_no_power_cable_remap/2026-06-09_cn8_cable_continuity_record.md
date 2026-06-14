# CN3 15-pin control cable continuity record

Date: 2026-06-09

Field update: 2026-06-10 user confirmed all disconnected before continuity
work.

Task: `TASK-2026-06-09-L3-cn8-no-power-cable-remap`

Planned evidence ID after acceptance:
`EV-2026-06-09-HW-CN8-CABLE-CONTINUITY-001`

## Connector naming correction

2026-06-12 photo review correction: the populated long 15-pin control
connector on the PCB silkscreen is `CN3`. Earlier schematic/history records
refer to the same control-interface pin list as `CN8`. This continuity record
therefore treats `CN3 Pn` as the physical connector and `CN8 Pn` as a legacy
alias only.

The separate 6-pin connector is not the 15-pin PWM/control interface and must
not be used for this TIM1 cable.

## Hard stop

Do not continue unless all five conditions are true:

- [x] NUCLEO USB is disconnected.
- [x] Power-board 24 V is disconnected and the board is discharged.
- [x] Motor and all three phase wires are disconnected.
- [x] CN3/CN8-alias cable is disconnected from the power board.
- [x] All loose wires are disconnected from the NUCLEO.

If any condition is false or uncertain, stop.

## Meter baseline

Meter mode: continuity / low resistance

| Check | Raw result | Status |
| --- | --- | --- |
| Probe-tip short resistance | Beep, 0.1 ohm | `PASS` |
| Open probes do not beep | No beep | `PASS` |

## Required cable map

| Wire | Physical PCB end | Legacy alias | Signal | NUCLEO loose-wire end | Continuity result | Resistance | Status |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | CN3 P1 | CN8 P1 | HIN1 | PA8 / CN10-23 | Stable beep | 0.1 ohm | `PASS` |
| 2 | CN3 P2 | CN8 P2 | LIN1 | PA7 / CN10-15 | Stable beep | 0.1 ohm | `PASS` |
| 3 | CN3 P3 | CN8 P3 | HIN2 | PA9 / CN10-21 | Stable beep | 0.1 ohm | `PASS` |
| 4 | CN3 P4 | CN8 P4 | LIN2 | PB14 / CN10-28 | Stable beep | 0.1 ohm | `PASS` |
| 5 | CN3 P5 | CN8 P5 | HIN3 | PA10 / CN10-33 | Stable beep | 0.1 ohm | `PASS` |
| 6 | CN3 P6 | CN8 P6 | LIN3 | PB15 / CN10-26 | Stable beep | 0.1 ohm | `PASS` |
| 7 | CN3 P13 | CN8 P13 | nFAULT | PB12 / CN10-16 | Stable beep | 0.1 ohm | `PASS` |
| 8 | CN3 P15 | CN8 P15 | GND_SIGNAL | reviewed NUCLEO GND wire | Stable beep | 0.1 ohm | `PASS` |

Acceptance for each row:

- stable beep;
- resistance approximately equal to the probe-tip baseline;
- no intermittent result when the wire is moved gently;
- no other NUCLEO endpoint beeps from the same CN3/CN8-alias pin.

## Open-pin check

| Physical PCB pins | Legacy alias | Required state | Raw result | Status |
| --- | --- | --- | --- |
| CN3 P7-P12 | CN8 P7-P12 | no installed wire | Open / no installed wire | `PASS` |
| CN3 P14 / 3V3 | CN8 P14 / 3V3 | no installed wire | Open / no installed wire | `PASS` |

P14 is a hard stop: do not install or bridge it during this stage.

## Isolation check

Keep one probe on the named wire and touch the other probe to every other
installed wire.

| Reference wire | Must not beep to | Raw result | Status |
| --- | --- | --- | --- |
| P1 / HIN1 | P2-P6, P13, P15 | No beep | `PASS` |
| P2 / LIN1 | P3-P6, P13, P15 | No beep | `PASS` |
| P3 / HIN2 | P4-P6, P13, P15 | No beep | `PASS` |
| P4 / LIN2 | P5-P6, P13, P15 | No beep | `PASS` |
| P5 / HIN3 | P6, P13, P15 | No beep | `PASS` |
| P6 / LIN3 | P13, P15 | No beep | `PASS` |
| P13 / nFAULT | P15 | No beep | `PASS` |

Any stable or intermittent beep is a failure. Stop and correct the cable
before repeating the complete continuity and isolation checks.

## Photo review

| Photo | Requirement | Status |
| --- | --- | --- |
| Full loose cable | both disconnected ends visible | `PASS`: supported by the installed-end photos and prior DMM continuity record |
| CN3 15-pin end | pin 1 marker and P1-P15 orientation visible | `PASS`: physical CN3 connector confirmed, P1-P6 input-resistor end and P13/P15 opposite end accepted |
| NUCLEO end | all eight destination labels/positions visible | `PASS WITH LIMITATION`: photo confirms CN10/Morpho-area installation; prior eight-row DMM continuity is the primary endpoint evidence |
| P14 evidence | P14 visibly unpopulated | `PASS`: P14/3V3 position remains visually open between P13 and P15 |

## Post-installation no-power sanity check

2026-06-12 user-reported targeted DMM checks after the reviewed cable was
installed into the physical `CN3` 15-pin control connector. All supplies
remained disconnected.

| Check | Required result | Raw result | Status |
| --- | --- | --- | --- |
| CN3/CN8-alias P14 / 3V3 to P15 / GND | no continuity | No beep | `PASS` |
| P1 / HIN1 to P2 / LIN1 | no continuity | No beep | `PASS` |
| P3 / HIN2 to P4 / LIN2 | no continuity | No beep | `PASS` |
| P5 / HIN3 to P6 / LIN3 | no continuity | No beep | `PASS` |
| P13 / nFAULT to P15 / GND | no continuity | No beep | `PASS` |

This post-installation check is a final no-power sanity check only. It does not
replace the full disconnected-end continuity/isolation table above and does not
prove powered STDRIVE101 input behavior.

## Decision

Overall result:
`PASS FOR NO-POWER CABLE INSTALLATION AND POST-INSTALLATION SANITY CHECK ONLY`

The cable installation into the physical `CN3` 15-pin control connector is
accepted for no-power review. This closes the current continuity/orientation
task and authorizes only planning a separate reviewed next task. It does not
authorize NUCLEO USB, 24 V, PWM, Gate probing, or motor connection.
