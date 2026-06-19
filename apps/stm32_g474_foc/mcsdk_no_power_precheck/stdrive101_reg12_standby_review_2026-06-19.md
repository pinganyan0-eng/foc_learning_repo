# STDRIVE101 REG12 Standby Review - 2026-06-19

## Boundary

This record explains the repeated static `REG12 = 0.3 V` measurement using
the archived STDRIVE101 datasheet and the 2026-06-19 user-reported static
measurements.

This is documentation and measurement interpretation only. It is not motor
validation, PWM validation, Gate PWM validation, Hall closed-loop validation,
sensorless validation, or powered-drive readiness.

Hard stops remain active:

- Motor disconnected.
- No Gate PWM output.
- No Motor Pilot.
- No Motor Profiler.
- No Hall closed-loop claim.
- No sensorless claim.
- No powered-drive readiness claim.

## Inputs Reviewed

Project evidence:

- `static_24v_baseline_repeat_check_2026-06-19.md`
- `static_24v_baseline_gate_summary_2026-06-19.md`
- `no_power_reg12_vs_identity_check_2026-06-19.md`
- `cn3_b1_static_power_nfault_measurement_2026-06-19.md`
- `hardware/bom/2026-05-09_user_provided_power_stage_parts.md`

Official ST source archived locally:

- `materials/extracted/st_manuals/st_stdrive101_datasheet.txt`
- Official ST URL recorded by the digest:
  `https://www.st.com/resource/en/datasheet/stdrive101.pdf`

## Relevant STDRIVE101 Datasheet Facts

The archived STDRIVE101 datasheet text states:

- `REG12` is the 12 V linear regulator output and gate-driver supply
  (`materials/extracted/st_manuals/st_stdrive101_datasheet.txt:674` to
  `:690`).
- The 12 V LDO regulator is disabled during standby
  (`materials/extracted/st_manuals/st_stdrive101_datasheet.txt:674` to
  `:676`).
- In standby, the 12 V LDO linear regulator is switched off
  (`materials/extracted/st_manuals/st_stdrive101_datasheet.txt:872` to
  `:879`).
- The device enters standby when all driving input pins are kept low for at
  least `tSTBY`; at power-up, if all driving inputs are low, the device is
  immediately put in standby
  (`materials/extracted/st_manuals/st_stdrive101_datasheet.txt:880` to
  `:884`).
- The device leaves standby only after at least one logic input is set high,
  and it becomes operative only after `REG12` rises above the UVLO turn-on
  threshold
  (`materials/extracted/st_manuals/st_stdrive101_datasheet.txt:881` to
  `:885`).
- In standby, UVLO protection is disabled
  (`materials/extracted/st_manuals/st_stdrive101_datasheet.txt:873` to
  `:878`).
- Outside standby, the datasheet lists `nFAULT` low for `VREG12` UVLO
  (`materials/extracted/st_manuals/st_stdrive101_datasheet.txt:935` to
  `:940`).

Project hardware notes also identify the board-level `REG12` node as the
STDRIVE101 internal gate-driver related node with `C4 4.7 uF + C5 100 nF` to
GND, not an external supply rail
(`hardware/bom/2026-05-09_user_provided_power_stage_parts.md:40` and `:64`
to `:65`).

## User-Reported Static Measurements

The relevant final static condition was:

```text
USB/ST-LINK connected
CN3 connected
Motor disconnected
B1 not pressed, then B1 once and returned to IDLE
HSPY: 24 V / 0.2 A current limit
Supply current: 0.036 A
Supply state: CV
VS / 24V_FUSED: 24 V
CN3_14 / 3V3: 3.3 V
CN3_13 / nFAULT: 3.3 V
REG12 at C4/C5 positive side: 0.3 V
CN3_1..CN3_6: 0 V
```

The no-power identity check reported no obvious hard short:

```text
REG12 correct point -> VS / 24V_FUSED: 0.5 Mohm
REG12 correct point -> GND: 3 Mohm
VS / 24V_FUSED -> GND: 0.2 Mohm
REG12 correct point -> 24V input positive: 25 Mohm
REG12 correct point -> CN3_14 / 3V3: 0.4 Mohm
```

The user also confirmed that the `C2/C3` positive side was `VS / 24V_FUSED`
and the `C4/C5` positive side was the intended `REG12` point.

## Interpretation

The repeated `REG12 = 0.3 V` reading is consistent with the STDRIVE101 being
in standby under the current static condition:

- `VS / 24V_FUSED = 24 V` proves the device supply node reached the local VS
  capacitor point.
- `CN3_1..CN3_6 = 0 V` means the measured driver-command inputs remained low
  under this test condition.
- The baseline firmware review and follow-up measurements did not show any
  CN3 input going high after B1; B1 changed only the app state, not the
  measured driver inputs.
- The datasheet says all-low driving inputs at power-up put the device in
  standby.
- In standby, the 12 V LDO is switched off, so a low `REG12` voltage is
  expected instead of evidence by itself of a failed 12 V regulator.
- Because UVLO protection is disabled in standby, `nFAULT = 3.3 V` does not
  contradict `REG12 = 0.3 V` in this specific all-low standby interpretation.

This means the earlier question "why is REG12 not 12 V?" is now explained for
the static all-inputs-low condition. The current evidence does not require a
REG12-to-VS short explanation and does not indicate a high-current fault,
because the supply stayed at `0.036 A` in `CV` and the no-power DMM readings
did not show an obvious hard short.

## Non-Pass Limits

This explanation is limited:

- It does not prove every CN3 input net endpoint unless schematic or netlist
  evidence is separately reviewed.
- It does not prove bootstrap charging.
- It does not prove low-side or high-side gate output behavior.
- It does not prove fault protection behavior under active drive.
- It does not authorize PWM, Motor Pilot, Motor Profiler, or motor connection.

## Decision

`STDRIVE101 REG12 static-low explanation / all measured CN3 drive inputs low /
datasheet standby behavior explains REG12 LDO off / nFAULT high is compatible
with standby because UVLO is disabled / no hard-short indication from no-power
DMM / no PWM-output validation / no powered-drive readiness`.

## Next Boundary

Close only the REG12-static-low explanation gate for the all-inputs-low
condition.

The next useful step should remain non-escalating:

1. Keep the board in the known safe static baseline.
2. Record that `REG12 = 0.3 V` is expected while all STDRIVE101 drive inputs
   remain low and the device is in standby.
3. Do not perform a wake-up or bootstrap-charge experiment until a separate
   bounded plan exists with:
   - motor disconnected;
   - current limit defined;
   - exact input to be driven high identified;
   - expected `REG12`, `nFAULT`, and supply-current windows defined;
   - rollback rule if current rises, CC appears, nFAULT drops, or any voltage
     leaves the expected range.
