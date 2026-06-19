# STDRIVE101 REG12 Single-Input Wake Diagnostic Plan - 2026-06-19

## Boundary

This is a planning artifact only. It defines a later bounded diagnostic for
checking whether STDRIVE101 leaves standby and raises `REG12` when one logic
input is driven high.

This plan does not authorize executing the diagnostic yet. It is not PWM
validation, not Gate PWM validation, not motor validation, not Hall closed-loop
validation, not sensorless validation, and not powered-drive readiness.

Hard stops remain active until a separate user-confirmed execution gate opens:

- Do not connect a motor.
- Do not start PWM.
- Do not run Motor Pilot.
- Do not run Motor Profiler.
- Do not use MCU firmware to generate motor-control outputs.
- Do not use a direct wire to force any CN3 input high.
- Do not install or remove any jumper while HSPY output is on.

## Evidence Inputs

This plan depends on these 2026-06-19 records:

- `stdrive101_reg12_standby_review_2026-06-19.md`
- `cn3_driver_input_rail_short_check_result_2026-06-19.md`
- `cn3_driver_input_adjacent_short_check_result_2026-06-19.md`
- `static_24v_baseline_repeat_check_2026-06-19.md`
- `out1_output_node_no_power_short_check_result_2026-06-19.md`

Relevant STDRIVE101 datasheet facts from
`materials/extracted/st_manuals/st_stdrive101_datasheet.txt`:

- Logic input recommended operating range is `0 V` to `5 V`
  (`:147` to `:168`).
- Logic high threshold is `2 V`, logic "1" input bias current is in the
  microamp range, and the input pull-down is about `132 kohm` to `275 kohm`
  in the datasheet test table (`:366` to `:379`).
- `REG12` is the 12 V linear regulator output and gate-driver supply
  (`:149` to `:154`, `:268` to `:276`, and `:610` to `:612`).
- `REG12` UVLO turn-on threshold is `5.5 V`
  (`:237` to `:240`).
- With `DT/MODE` shorted to ground, the device operates in `INHx/INLx` mode
  and no internal deadtime is generated
  (`:803` to `:811`, `:867` to `:871`).
- In `INHx/INLx` mode, `INxH=L` and `INxL=H` commands low-side on
  (`:813` to `:818`).
- All input lines have internal pull-downs
  (`:811` to `:812`).
- The device leaves standby after at least one logic input is set high, then
  becomes operative only after `REG12` rises above UVLO
  (`:880` to `:885`).
- After leaving standby, bootstrap-capacitor charging via low-side turn-on is
  required, and the internal regulator current is limited by `IREG12lim`
  (`:752` to `:755`).

## Chosen Single Input

Use only this candidate input for the later diagnostic:

```text
CN3_2 / LIN1
```

Reason:

- Current board-side mapping labels `CN3_2` as `LIN1`.
- In `INHx/INLx` mode, raising a low-side input while the paired high-side
  input remains low commands low-side on.
- This avoids intentionally commanding a high-side gate during this diagnostic.
- ST notes that bootstrap charging after standby involves low-side turn-on.

Important consequence:

```text
CN3_2 / LIN1 high can turn on the phase-1 low-side MOSFET gate after REG12
comes up.
```

Therefore this is not a harmless logic-only check. It remains a bounded
power-stage diagnostic with motor disconnected and strict current-limit stop
rules.

Do not use `CN3_1 / HIN1`, `CN3_3 / HIN2`, or `CN3_5 / HIN3` for this
diagnostic, because those are high-side input labels.

## Required Extra No-Power Check Before Execution

Before any later execution, perform this extra no-power check with:

```text
HSPY output: OFF
24 V input: disconnected
USB/ST-LINK: unplugged
Motor: disconnected
DMM: continuity or resistance mode only
```

Required output-node hard-short screen:

```text
J_MOTOR / OUT1 / phase-U output -> VS / 24V_FUSED: no beep, high resistance
J_MOTOR / OUT1 / phase-U output -> GND: no beep, high resistance
```

If the exact `OUT1` / phase-U point cannot be confidently identified, do not
execute the wake diagnostic. If either row beeps or reads near `0 ohm`, stop
and open a hardware correction record.

## Later Execution Setup

This setup is required if, and only if, a later message explicitly opens the
execution gate:

```text
Motor: disconnected
USB/ST-LINK: unplugged unless the execution gate explicitly says otherwise
HSPY: 24 V, 0.2 A current limit, output OFF before wiring changes
CN3: connected as in the static 24 V check
Stimulus: 10 kohm series resistor from CN3_14 / 3V3 to CN3_2 / LIN1
No direct 3V3-to-LIN1 wire
No firmware PWM
No Motor Pilot / Profiler
```

The 10 kohm resistor is a current-limiting stimulus. It is not a permanent
hardware modification. With the datasheet input pull-down range and a 3.3 V
source, a 10 kohm series stimulus should still drive the input above the
datasheet logic-high threshold. This assumes `CN3_14 / 3V3` is actually present
in the execution setup.

## Later Execution Sequence

This sequence is not authorized by this document. It is included so the future
gate can be reviewed before use.

1. With no stimulus resistor installed, HSPY output OFF, confirm:
   - motor disconnected;
   - USB/ST-LINK unplugged;
   - 24 V wiring polarity correct;
   - HSPY set to `24 V / 0.2 A`;
   - DMM black lead on GND.
2. Turn HSPY output ON for the known static baseline.
3. Confirm and record:
   - supply state `CV`;
   - supply current near the previous `0.036 A` baseline;
   - `VS / 24V_FUSED = 24 V`;
   - `CN3_14 / 3V3 = 3.3 V` in this exact setup;
   - `CN3_13 / nFAULT = 3.3 V`;
   - `REG12 = about 0.3 V`.
   If `CN3_14 / 3V3` is not present with USB/ST-LINK unplugged, stop and do
   not install the stimulus resistor.
4. Turn HSPY output OFF.
5. Wait until `VS / 24V_FUSED` is below `1 V`.
6. Install the 10 kohm series resistor between `CN3_14 / 3V3` and
   `CN3_2 / LIN1`.
7. Turn HSPY output ON.
8. Watch HSPY first, then record:
   - supply state `CV` or `CC`;
   - supply current;
   - `CN3_13 / nFAULT`;
   - `REG12`;
   - optional: `CN3_2 / LIN1` voltage if accessible without disturbing the
     setup.
9. Turn HSPY output OFF.
10. Wait until `VS / 24V_FUSED` is below `1 V`.
11. Remove the 10 kohm resistor.
12. Restore the all-inputs-low baseline and confirm `REG12` returns low.

## Expected Result

If the driver leaves standby cleanly:

```text
Supply state: CV
Supply current: may rise above 0.036 A during charge, then settle
CN3_13 / nFAULT: high, about 3.3 V after settling
REG12: rises above 5.5 V, expected near the 12 V regulator range
```

Use this practical steady-state expectation:

```text
REG12 expected window after settling: about 10 V to 13 V
```

The datasheet electrical table reports `VREG12` around `11.4 V` to `12.75 V`
under its stated test condition, but the bench diagnostic should treat
`10 V` to `13 V` as the practical DMM window before making any finer claim.

## Stop Rules

Immediately turn HSPY output OFF if any of these occur:

- HSPY enters `CC`;
- HSPY current exceeds `0.12 A` at any visible steady reading;
- HSPY current remains above `0.08 A` after about five seconds;
- `nFAULT` is below `3.0 V` after settling;
- `REG12` remains below `5.5 V` after `CN3_2 / LIN1` is driven high;
- any smell, heat, sound, visible LED anomaly, or unstable meter reading
  appears;
- the 10 kohm resistor or probes are bumped or uncertain.

After any stop-rule event:

1. leave HSPY output OFF;
2. remove the stimulus resistor only after VS falls below `1 V`;
3. do not retry until the result is recorded and reviewed.

## Decision

`STDRIVE101 REG12 single-input wake diagnostic plan / candidate input CN3_2
LIN1 through 10 kohm stimulus / low-side gate may turn on / requires motor
disconnected, extra OUT1 hard-short check, 24 V 0.2 A current limit, CV/CC
stop rules, nFAULT and REG12 windows / planning only / no execution
authorization / no PWM-output validation / no powered-drive readiness`.

## Current Status

The required OUT1 output-node no-power short screen is now recorded as
user-reported no beep / high-resistance evidence:

```text
J_MOTOR / OUT1 / phase-U output -> VS / 24V_FUSED: no beep, high resistance
J_MOTOR / OUT1 / phase-U output -> GND: no beep, high resistance
```

Execution is still not automatically authorized by this plan. A separate
explicit user-confirmed execution gate is required before applying 24 V for
the single-input wake diagnostic.

The next allowed user-facing step is the explicit execution-gate decision for
the bounded single-input wake diagnostic. If opened, it must follow this
candidate:

```text
CN3_2 / LIN1 through 10 kohm stimulus
Motor disconnected
HSPY 24 V / 0.2 A
No firmware PWM
Measure supply CV/CC, current, nFAULT, and REG12
```

No motor connection, PWM, Motor Pilot, or Motor Profiler is authorized.
