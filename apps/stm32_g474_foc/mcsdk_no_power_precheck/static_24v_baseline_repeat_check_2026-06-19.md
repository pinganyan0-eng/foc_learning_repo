# Static 24 V Baseline Repeat Check - 2026-06-19

## Boundary

This record covers a repeated current-limited static 24 V observation after the
no-power REG12 / VS identity check and the user confirmation that the REG12 /
VS measurement points were not misidentified.

This is static measurement evidence only. It is not motor validation, PWM
validation, Gate PWM validation, Hall closed-loop validation, sensorless
validation, or powered-drive readiness.

Hard stops remain active:

- Keep motor disconnected.
- Do not start PWM.
- Do not run Motor Pilot or Motor Profiler.
- Do not claim power-stage readiness from this record.

## Prior Context

Prior records established:

- reviewed `nucleo_g474re_baseline` firmware;
- serial app state returned to `IDLE` after `STOP`;
- no-power REG12 / VS identity check found no obvious hard short;
- user confirmed REG12 / VS measurement points were not misidentified.

Related records:

- `static_24v_baseline_gate_summary_2026-06-19.md`
- `no_power_reg12_vs_identity_check_2026-06-19.md`

## User-Reported Raw Measurement

The requested repeat check was:

```text
USB/ST-LINK connected
CN3 connected
Motor disconnected
B1 not pressed
HSPY: 24 V / 0.2 A current limit
```

The user reported the result was unchanged from the previous static check.

Interpreted raw values:

```text
Supply current: 0.036 A
Supply state: CV
VS / 24V_FUSED: 24 V
CN3_13 / nFAULT: 3.3 V
REG12 at C4/C5 positive side: 0.3 V
CN3_1..CN3_6: 0 V
```

## Interpretation

Repeat observations:

- supply current remains stable at `0.036 A` in `CV`;
- `VS / 24V_FUSED` remains `24 V`;
- `nFAULT` remains high at `3.3 V`;
- `CN3_1..CN3_6` remain `0 V`;
- `REG12` remains low at `0.3 V`.

This repeat result suggests the powered-static behavior is stable under the
reported conditions, not a single transient or one-off reading.

Important non-pass limit:

- The stable `REG12 = 0.3 V` result still does not prove active gate-drive
  supply readiness. It remains an unresolved behavior that should be explained
  from STDRIVE101 documentation or a later separately gated diagnostic plan
  before any PWM or motor step.

## Decision

`Static 24 V repeat check / stable 0.036 A CV / nFAULT high / CN3 inputs low /
VS present / REG12 remains low / close current static observation gate / no
PWM-output validation / no powered-drive readiness`.

This closes the current static input/nFAULT observation gate. It does not open
motor connection, PWM output, Motor Pilot, or Motor Profiler.

## Next Step

Do not continue escalating hardware power actions from this gate.

The next useful project step is documentation / source review only:

- explain whether `REG12 = 0.3 V` is expected when STDRIVE101 inputs are all
  low and no gate-drive activity is commanded;
- use official STDRIVE101 documentation or already archived high-trust project
  references;
- keep motor disconnected and do not start PWM while this is unresolved.
