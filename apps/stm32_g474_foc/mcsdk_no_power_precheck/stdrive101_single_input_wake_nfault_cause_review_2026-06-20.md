# STDRIVE101 Single-Input Wake nFAULT Cause Review - 2026-06-20

## Boundary

This is a no-power / source-review artifact after the 2026-06-19 bounded
single-input wake result.

It does not authorize a repeat powered wake diagnostic, a different input
stimulus, firmware implementation, generated-code edits, CubeMX / Workbench
edits, flash, Run / Debug, motor connection, Gate PWM, Motor Pilot,
Motor Profiler, Hall closed-loop validation, sensorless validation,
power-stage readiness, or motor readiness.

## Trigger Evidence

The review is triggered by:

```text
CN3_14 / 3V3 -> 10 kohm -> CN3_2 / LIN1
wake_supply_state = CV
wake_supply_current_A = 0.046 A
wake_CN3_2_LIN1_V = 3 V
wake_CN3_13_nFAULT_V = 0 V
wake_REG12_V = 12 V
post_off_VS_or_24V_FUSED_V = 0 V
```

Recorded in:

```text
apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_reg12_single_input_wake_fault_result_2026-06-19.md
```

## Source Facts Used

From the repo-local extracted STDRIVE101 datasheet:

- `SCREF` sets the VDS monitoring threshold, and the pin description says it
  has an internal pull-down (`st_stdrive101_datasheet.txt:608` to `:610`).
- VDS protection is enabled below the disable threshold and disabled when
  `SCREF` is above the disable voltage (`:170` to `:176`, `:426` to `:431`).
- The device leaves standby after at least one logic input is set high, then
  returns operative after `REG12` crosses the UVLO turn-on threshold; after
  standby exit, bootstrap charging through low-side turn-on is required
  (`:880` to `:885`).
- For UVLO / overtemperature handling, the datasheet table shows `nFAULT` low
  for `VREG12` UVLO and open for `VBOOTx` UVLO (`:930` to `:943`).
- The datasheet notes a special external-REG12-supply sequence where `nFAULT`
  can go low after leaving standby even without a REG12 UVLO condition
  (`:968` to `:970`).
- VDS monitoring compares MOSFET VDS against the SCREF-derived threshold; if
  triggered, all gate outputs are forced low, `nFAULT` is forced low, and the
  protection is latched until standby (`:986` to `:1009`).
- The overcurrent comparator on `CP` can force gate outputs low and force
  `nFAULT` low, then auto-release after its disable time (`:1012` to `:1016`).
- Thermal shutdown switches off the regulator and forces `nFAULT` low
  (`:1017` to `:1021`).

Project source clues:

- Current PCB2 route records `CN3_2 / LIN1 -> PB3`, `CN3_13 / nFAULT -> PB12`,
  `CN3_14 / 3V3`, and `CN3_15 / GND` continuity from the user-reported DMM
  summary.
- The 2026-05-19 PCB2 mapping note records `DT/MODE = GND`, `CP = 100 nF to
  GND`, `SCREF = 33 k to 3.3 V plus 20 k to GND`, and `nFAULT = 10 k pull-up
  to 3.3 V` as source clues, not final route proof.
- `protection_thresholds.md` already warns that VDS / SCREF proof remains
  partial and the earlier threshold calculation is not accepted as a safe
  project threshold.

## Cause Ranking

### 1. VDS monitoring triggered after low-side command

Status: primary review target.

Reasoning:

```text
LIN1 high
-> standby exit
-> REG12 rises
-> in INHx/INLx mode, HIN1 low + LIN1 high can command low-side 1
-> if OUT1 is not pulled near ground while GLS1 is commanded high, VDS
   monitoring can see an abnormal low-side VDS
-> VDS protection can latch nFAULT low
```

This matches the observed pattern better than a pure REG12 failure because
`REG12` was reported as `12 V` and HSPY remained `CV`.

This is still an inference. It is not proven until board-level `SCREF`,
`OUT1`, `GLS1`, `BOOT1`, `GND`, and MOSFET routing / assembly evidence is
reviewed.

### 2. Transient or sequence-related REG12 / external-REG12 issue

Status: secondary review target.

The steady DMM value `REG12 = 12 V` argues against a steady `VREG12` UVLO at
the time of the reading. However, a transient drop during bootstrap charging,
wrong REG12 loading / decoupling, or an accidental external REG12 supply/tie
cannot be ruled out from one DMM result.

The external-REG12 special case is not the leading interpretation because the
project records treat `REG12` as the internal LDO output with only local
decoupling, and the baseline was `REG12 = 0.33 V`. Still, the earlier REG12
misidentification / anomaly history means the `REG12` net must remain on the
review list.

### 3. CP overcurrent comparator assertion

Status: possible, but not first target from the current evidence.

The bench supply did not enter current limit and the steady current was only
`0.046 A`, so a large sustained power input current fault was not observed.
The CP pin and its capacitor network are still only source clues, and CP noise
or wrong routing could assert the comparator. This needs source / no-power
review before any repeat powered step.

### 4. Thermal shutdown

Status: low-likelihood from the reported event, not fully excluded.

There was no reported heat, smell, sound, or abnormal supply current. Thermal
shutdown is therefore not the first explanation. It remains a datasheet
possible cause of `nFAULT` low, but the next review should focus elsewhere
unless physical inspection finds heat damage or soldering faults near the
driver / regulator area.

### 5. External nFAULT pull-down or measurement wiring issue

Status: lower-likelihood but easy to screen no-power.

The baseline had `nFAULT = 3.3 V`, and prior no-power checks reported no hard
short from `nFAULT` to `GND`. That makes a permanent external pull-down less
likely. A shifted probe, LED/pull-up assembly issue, or intermittent short
still belongs in the no-power check list.

## No-Power Evidence Needed Next

Before any repeat powered diagnostic, collect only no-power or source evidence:

```text
HSPY output OFF
VS / 24V_FUSED < 1 V
10 kohm stimulus resistor removed
Motor disconnected
USB/ST-LINK unplugged unless a source-photo task explicitly needs it off-board
DMM continuity / resistance mode only
```

Requested no-power table:

| Row | Check | Record raw result |
| --- | --- | --- |
| 1 | `CN3_2 / LIN1` to `CN3_14 / 3V3` after removing the stimulus | beep / ohms |
| 2 | `CN3_2 / LIN1` to `CN3_15 / GND` after removing the stimulus | beep / ohms |
| 3 | `CN3_13 / nFAULT` to `CN3_14 / 3V3` | beep / ohms |
| 4 | `CN3_13 / nFAULT` to `CN3_15 / GND` | beep / ohms |
| 5 | `SCREF` to `CN3_14 / 3V3`, if `SCREF` is safely identifiable | ohms |
| 6 | `SCREF` to `CN3_15 / GND`, if `SCREF` is safely identifiable | ohms |
| 7 | `CP` to `CN3_15 / GND`, if `CP` is safely identifiable | ohms / capacitor-charge behavior |
| 8 | `REG12` to `CN3_15 / GND` | ohms |
| 9 | `REG12` to `VS / 24V_FUSED` | ohms |
| 10 | `OUT1 / phase-U` to `CN3_15 / GND` | beep / ohms |
| 11 | `OUT1 / phase-U` to `VS / 24V_FUSED` | beep / ohms |

If `SCREF`, `CP`, `REG12`, or `OUT1` cannot be confidently identified, do not
probe them by guesswork. Request a marked board photo or the hardware
teammate's netlist / EDA screenshot instead.

## Source Packet Needed

Ask the hardware teammate for one source packet focused on U1 STDRIVE101:

```text
U1 STDRIVE101 local schematic/netlist crop:
DT/MODE, SCREF, CP, nFAULT, REG12, VS, BOOT1, OUT1, GLS1, GHS1,
Q1/Q2 gates/sources/drains, GND_POWER, GND_SIGNAL, R_GND_ISO

PCB crop:
U1, Q1/Q2, OUT1, REG12 capacitor C4/C5, SCREF divider R1/R2,
CP capacitor C1, nFAULT pull-up R3/LED1, bootstrap C22/D1
```

The packet must identify source date / version if possible. Screenshots are
acceptable as clues, but a netlist or EDA source export is stronger.

## Decision

`STDRIVE101 single-input wake nFAULT cause review / REG12 wake observed but
clean wake failed / primary review target VDS monitoring after LIN1 low-side
command / secondary targets REG12 sequence or accidental external REG12 tie,
CP comparator, thermal shutdown, external nFAULT pull-down / next step
no-power DMM and source packet only / no repeat powered wake / no PWM-output
validation / no powered-drive readiness`.

## Next User Checkpoint

Do not power the board for this checkpoint. Provide either:

```text
10k removed = yes
VS = ___ V
Rows 1-4 raw DMM results:
1. CN3_2-LIN1 to CN3_14-3V3 = ___
2. CN3_2-LIN1 to CN3_15-GND = ___
3. CN3_13-nFAULT to CN3_14-3V3 = ___
4. CN3_13-nFAULT to CN3_15-GND = ___
```

or provide a clear photo / source packet that identifies `SCREF`, `CP`,
`REG12`, and `OUT1` before probing rows 5-11.
