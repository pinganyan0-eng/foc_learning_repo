# MCSDK / Host-Side Signed Reverse Speed Command Snapshot Sequence Bridge Review

Date: 2026-06-23

## Decision

`MCSDK host-side signed reverse speed command snapshot sequence bridge / host-side no-power replay-step semantic translation only / no firmware implementation / no generated-code edit / no MCSDK observer equivalence / no MCSDK integration / no sensorless claim / no PWM output / no motor readiness`.

## Scope

This record closes the host-side no-power evidence chain from the completed
signed reverse speed/current replay fixture into the MCSDK-shaped comparison
bridge:

```text
signed reverse sensorless replay
-> lock-aware speed/current command policy
-> per-step SensorlessReplayResult snapshots
-> signed MCSDK-shaped q15 speed/current metadata
```

It does not change host-side control behavior. It adds fixture coverage for the
existing `sensorless_replay_to_mcsdk_speed_command_snapshots(...)` translation
path, using the same reverse replay semantics already frozen by
`signed_reverse_speed_current_command_holds_until_lock_and_after_loss`.

## Code And Fixture

- `tests/fixtures/foc_mcsdk_bridge_vectors.json`
  - adds `sensorless_replay_speed_command_snapshot_sequence_cases`;
  - preserves the earlier forward 3-step speed-command replay snapshot case as
    `forward_speed_command_replay_steps_map_to_q15`;
  - adds
    `signed_reverse_speed_command_replay_steps_map_to_q15`, an 8-step signed
    reverse replay sequence;
  - freezes `target_omega_q15`, `measured_omega_q15`, `requested_iq_q15`,
    `effective_iq_q15`, `locked`, `limited`, and `reason` for each step.
- `tests/test_mcsdk_foc_bridge_vectors.py`
  - reads speed-command replay snapshot sequence cases from the JSON fixture;
  - keeps `hold_when_unlocked` when building `SensorlessSpeedLoopConfig`;
  - validates each snapshot returned by
    `sensorless_replay_to_mcsdk_speed_command_snapshots(...)`.

## Protected Reverse Snapshot Sequence

The protected reverse case is
`signed_reverse_speed_command_replay_steps_map_to_q15`.

It freezes the bridge output for startup-before-lock, pending-lock, tracking,
short confidence dip, confirmed loss, startup after loss, and relock. The
expected q15 sequence is:

```text
target_omega_q15:    [0, 0, -32768, -32768, -32768, -32768, -32768, -32768]
measured_omega_q15:  [1638, 3277, -16384, -16384, -16384, -14746, -13107, -16384]
requested_iq_q15:    [0, 0, -24576, -32768, -32768, 0, 0, -32768]
effective_iq_q15:    [0, 0, -24576, -24576, -24576, 0, 0, -24576]
locked:              [false, false, true, true, true, false, false, true]
limited:             [false, false, false, true, true, false, false, true]
```

The unlocked steps are still metadata snapshots of zero effective current
command in this host-side replay. The locked steps preserve negative speed and
negative current-command metadata, including symmetric locked current limiting.

## Subagent Protocol

Read-only helper Bacon reviewed only the filtered bridge/frontend fixture slice
and identified this missing sequence bridge as the smallest high-value
follow-on after the signed reverse speed/current replay fixture. The main agent
kept all repo writes in the owner path and used the helper digest only as
decision-relevant evidence for this no-power increment.

## Boundary

This is host-side no-power comparison evidence only.

It is not firmware.
It is not generated-code edit permission.
It is not MCSDK integration.
It is not MCSDK numerical equivalence.
It is not MCSDK speed-loop hook evidence.
It is not firmware speed-loop behavior.
It is not firmware current limiting.
It is not a firmware reverse-startup strategy.
It is not MCSDK Observer PLL equivalence.
It is not MCSDK Observer CORDIC equivalence.
It is not SMO implementation or validation.
It is not sensorless / SMO validation.
It is not compare-register evidence.
It is not Gate PWM validation.
It is not hardware validation.
It is not power-stage readiness.
It is not motor readiness.

Forbidden actions and claims remain:

- No flash.
- No Run / Debug.
- No 24 V.
- No power-board connection.
- No motor connection.
- No Gate PWM output.
- No Motor Pilot / Profiler.
- No Hall closed-loop claim.
- No sensorless / SMO claim.

## Verification

- `python -m json.tool tests\fixtures\foc_mcsdk_bridge_vectors.json` passed.
- `python -m unittest tests.test_mcsdk_foc_bridge_vectors` passed:
  13 tests OK.
