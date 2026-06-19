# STDRIVE101 REG12 Wake Official Web Review - 2026-06-19

## Boundary

This record is an official-source review and engineering decision note only.
It does not authorize executing the wake diagnostic.

Still forbidden by this record:

- no motor connection;
- no PWM output;
- no Motor Pilot;
- no Motor Profiler;
- no firmware-generated motor-control output;
- no powered-drive readiness claim;
- no motor readiness claim.

## Sources

Official sources checked on 2026-06-19:

- STDRIVE101 datasheet:
  `https://www.st.com/resource/en/datasheet/stdrive101.pdf`
- EVLDRIVE101-HPD product page:
  `https://www.st.com/en/evaluation-tools/evldrive101-hpd.html`
- EVLDRIVE101-HPD databrief:
  `https://www.st.com/resource/en/data_brief/evldrive101-hpd.pdf`

The STDRIVE101 datasheet is the controlling source for the driver behavior.
The EVLDRIVE101-HPD page/databrief are useful ST reference-design context for
STDRIVE101-based motor-control boards, but they are not proof of this custom
PCB's routing or soldering state.

## Official Facts Used

From the STDRIVE101 datasheet:

- `REG12` is the 12 V linear regulator output and gate-driving supply.
- Logic input recommended operating range is `0 V` to `5 V`.
- Logic inputs are compatible with 3.3 V logic and are 5 V tolerant under the
  datasheet's stated operating conditions.
- Logic high threshold is `2 V`.
- Logic input pull-down is about `132 kohm` to `275 kohm` at the datasheet
  test condition.
- If `DT/MODE` is shorted to ground, the device operates in `INHx/INLx` mode.
- In `INHx/INLx` mode, `INxH=L` and `INxL=H` commands the low-side gate on.
- Standby mode forces all output drivers low, disables OC/VDS/UVLO protection,
  and switches off the 12 V LDO.
- At power-up, if all driving inputs are low, the device enters standby.
- The device leaves standby after at least one logic input is set high.
- After leaving standby, the device becomes operative only after `REG12`
  rises above the UVLO turn-on threshold.
- After standby exit, bootstrap-capacitor charging via low-side turn-on is
  required.
- Outside standby, VREG12 UVLO drives `nFAULT` low; this differs from standby,
  where UVLO is disabled.

## Project Evidence Used

Current 2026-06-19 custom-board evidence:

- `static_24v_baseline_repeat_check_2026-06-19.md`:
  `VS / 24V_FUSED = 24 V`, `CN3_14 / 3V3 = 3.3 V`,
  `CN3_13 / nFAULT = 3.3 V`, `REG12 = 0.3 V`, supply current about
  `0.036 A`, supply state `CV`, and `CN3_1` to `CN3_6` remain `0 V`.
- `stdrive101_reg12_standby_review_2026-06-19.md`:
  explains why `REG12 = 0.3 V` with all six driving inputs low is compatible
  with STDRIVE101 standby rather than immediate evidence of a failed 12 V
  regulator.
- `cn3_driver_input_rail_short_check_result_2026-06-19.md`:
  no beep / high resistance from `CN3_1` to `CN3_6` against GND, 3V3, VS, and
  REG12.
- `cn3_driver_input_adjacent_short_check_result_2026-06-19.md`:
  no beep, about `90 kohm` between adjacent `CN3_1` to `CN3_6` input pairs.
- `stdrive101_reg12_single_input_wake_plan_2026-06-19.md`:
  defines the proposed later diagnostic using `CN3_2 / LIN1` through a
  `10 kohm` series stimulus resistor.

## Engineering Analysis

The official data supports the current standby interpretation:

```text
all six driver inputs low
-> STDRIVE101 standby
-> 12 V LDO switched off
-> REG12 low
-> UVLO disabled in standby
-> nFAULT can remain high
```

Therefore the present combination:

```text
VS = 24 V
3V3 = 3.3 V
nFAULT = 3.3 V
REG12 = 0.3 V
CN3_1..CN3_6 = 0 V
current = 0.036 A / CV
```

is consistent with standby and does not by itself prove a REG12 regulator
failure.

The official data also supports using a 10 kohm series stimulus from 3.3 V for
a later wake diagnostic. With a 10 kohm series resistor and the datasheet's
132 kohm to 275 kohm input pull-down range, the driven input should stay above
the 2 V high-level threshold if the 3.3 V source is really present in the
exact execution setup.

However, the same official data makes the risk boundary stricter:

```text
CN3_2 / LIN1 high
-> one STDRIVE101 logic input high
-> standby exit
-> REG12 may rise
-> INH1 low and LIN1 high
-> phase-1 low-side gate may turn on after REG12 is available
```

So the proposed `CN3_2 / LIN1` wake check is not a harmless logic-only check.
It is a bounded power-stage diagnostic. The low-side choice is still better
than intentionally selecting a high-side input for this first wake check, but
it requires the motor disconnected, 24 V current limiting, and the extra
output-node no-power short screen before any powered attempt.

## Decision

Keep the current diagnostic direction:

```text
REG12 low with all inputs low
-> treat as STDRIVE101 standby-compatible
-> do not replace parts or declare REG12 failure yet
-> next diagnostic target is controlled standby exit
-> preferred candidate remains CN3_2 / LIN1 through 10 kohm
```

Do not execute it yet.

The previously added execution condition remains mandatory:

```text
CN3_14 / 3V3 must be confirmed as 3.3 V in the exact execution setup.
If USB/ST-LINK is unplugged and CN3_14 / 3V3 is not present, stop and do not
install the stimulus resistor.
```

The next allowed user-facing action is still no-power only:

```text
J_MOTOR / OUT1 / phase-U output -> VS / 24V_FUSED: no beep, high resistance
J_MOTOR / OUT1 / phase-U output -> GND: no beep, high resistance
```

If either row beeps or reads near `0 ohm`, stop and record a hardware fault
investigation instead of attempting wake.

## Explicit Non-Pass

This review does not prove:

- custom PCB output-node isolation;
- MOSFET soldering correctness;
- bootstrap behavior on this board;
- gate waveform correctness;
- VDS/OC protection behavior on this board;
- firmware runtime behavior;
- PWM readiness;
- motor readiness;
- powered-drive readiness.
