# STDRIVE101 Gate-Waveform Image Design Plan No-Power - 2026-06-20

## Summary

- Evidence ID:
  `EV-2026-06-20-STDRIVE101-GATE-WAVEFORM-IMAGE-DESIGN-PLAN-NO-POWER-001`.
- Task ID:
  `TASK-2026-06-20-stdrive101-gate-waveform-image-design-plan-no-power`.
- Gate:
  Gate E0 from the prior gate-waveform / PWM-output no-power phase-gate
  ladder.
- Scope:
  no-power design-boundary plan for a future isolated waveform image.
- Hardware action:
  none in this record. No 24 V is applied by this plan.
- Firmware action:
  none in this record. No source package is created, no build is run, no
  flash, no Run / Debug, no USB runtime execution, and no Gate PWM output.
- Decision:
  `STDRIVE101 gate-waveform image design plan no-power / Gate E0 only /
  separate isolated waveform candidate required / normal generated MCSDK app
  and command ingress remain blocked / six candidate driver inputs fixed as
  PA8 PA9 PA10 PB13 PB14 PB15 / idle state must force all six low before and
  after any future candidate window / future TIM1 MOE CCER break AOE dead-time
  and complementary-overlap policy required before source or build / design
  plan only / no flash / no Run Debug / no 24 V / no Gate PWM output / no
  Motor Pilot / no Motor Profiler / no motor connection / no powered-drive
  readiness`.

## Boundary

This record is Gate E0 planning only. It does not authorize:

- source-code implementation;
- CMake edits;
- object-only build;
- linked-image build;
- firmware flash;
- Run / Debug;
- USB runtime execution;
- applying 24 V;
- Gate PWM output;
- oscilloscope probing on live gate or phase nodes;
- normal generated MCSDK application execution;
- Motor Pilot;
- Motor Profiler;
- motor connection;
- Hall closed loop;
- sensorless operation;
- power-stage readiness or motor readiness claims.

The narrow conclusion is:

```text
prior phase-gate plan
+ lockout image and USB-only lockout result
+ carried-forward static all-inputs-low evidence
-> a future isolated waveform image may be designed on paper
-> no source, build, flash, runtime, 24 V, or waveform output is opened here
```

## Carry-Forward Evidence

Gate E0 depends on these existing records:

| Source record | What is accepted here | What remains unproven |
| --- | --- | --- |
| `stdrive101_gate_waveform_pwm_output_no_power_phase_gate_plan_2026-06-20.md` | Gate E0 through Gate E5 ladder and the requirement not to skip to execution | any source package, build, runtime, 24 V, or gate waveform |
| `stdrive101_manual_gate_test_24v_static_lockout_carry_forward_result_2026-06-20.md` | no-repeat static boundary: prior USB + 24 V static all-inputs-low evidence can be carried forward for planning | waveform behavior under 24 V |
| `stdrive101_manual_gate_test_linked_image_build_only_record_2026-06-20.md` | isolated lockout image has a linkable build-only boundary and clean forbidden-symbol screens | any waveform image boundary |
| `stdrive101_manual_gate_test_usb_only_runtime_lockout_result_2026-06-20.md` | reviewed lockout image held `CN3_1` through `CN3_6` at `0 V` in the USB-only measured state | PWM-output behavior |
| `stdrive101_pwm_gate_test_no_power_source_review_2026-06-20.md` and `stdrive101_r3_2_mcsdk_pwm_output_path_source_closure_2026-06-20.md` | normal generated MCSDK PWM path stays blocked | safety of any future custom waveform candidate |

## Candidate Image Shape

The future waveform candidate must be a separate isolated image. It must not
reuse the normal generated MCSDK application as its execution path.

Required design intent for any later Gate E1 source package:

| Area | Gate E0 requirement |
| --- | --- |
| Image identity | A named isolated waveform image, separate from `stdrive101_gate_lockout_image` and separate from the normal generated MCSDK app. |
| Normal MCSDK start | No `MC_StartMotor1`, no `MCI_START`, no PC13 start / stop, no MCP / ASPEP command ingress, no Motor Pilot, and no Motor Profiler. |
| Candidate pins | The only candidate driver-input pins are `PA8`, `PA9`, `PA10`, `PB13`, `PB14`, and `PB15`. |
| Idle state | Before and after any future candidate window, all six pins must be forced low. |
| Future waveform window | Pattern, frequency, duty, duration, repeat count, and final idle duration must be explicitly specified before source or build. |
| Timer output policy | TIM1 `MOE`, `CCER`, break, AOE, OSSI / OSSR if used, polarity, preload, update timing, and dead-time policy must be explicitly reviewed before source or build. |
| Complementary overlap | High-side / low-side complementary overlap must be blocked by design. This cannot be left to manual timing or later oscilloscope hope. |
| Fault handling | `PB12 / nFAULT` must be monitored or latched in a defined low-priority stop path before any future execution. |
| Rollback | The future execution-entry must begin and end with HSPY output `OFF`; closeout must record `VS / 24V_FUSED < 1 V` before wiring changes. |

## Rejected Shortcuts

The following routes remain blocked:

- modify the normal generated MCSDK app to make it emit PWM;
- call `MC_StartMotor1()` or send `MCI_START`;
- use PC13 as a start button;
- leave MCP / ASPEP command ingress reachable;
- open Motor Pilot or Motor Profiler;
- build or flash a waveform image before the Gate E1 source package and
  Gate E2 build-only record exist;
- jump from this Gate E0 plan to any Gate E4 scope-only no-motor execution;
- connect a motor at any point in the Gate E branch.

## Future Gate E1 Source-Package Requirements

A later Gate E1 record must provide source-level evidence, still without
building or running, that:

- startup forces all six candidate pins low before any timer-output enable
  path can run;
- shutdown forces all six candidate pins low after the candidate window;
- no command path can start or extend the waveform;
- no normal generated MCSDK start, R3_2, Motor Pilot, or Motor Profiler path
  is linked into the candidate;
- TIM1 output-enable behavior is isolated and named;
- `MOE`, `CCER`, break, AOE, dead-time, and complementary-output policy are
  visible in source review;
- the waveform pattern, frequency, duty, duration, repeat count, and idle
  closeout are compile-time constants or otherwise frozen for review;
- `nFAULT` stop handling and rollback are named.

If any of these are missing, the branch must stay at no-power design review.

## Future Gate E2 Build-Only Requirements

A later Gate E2 record must be a build-only record and must include:

- object-only build result;
- linked ELF and MAP result;
- ELF / MAP / optional BIN hashes;
- source grep, ELF symbol, and MAP screens for forbidden ingress:
  `MC_StartMotor1`, `MCI_START`, PC13 start / stop, MCP, ASPEP, Motor Pilot,
  Motor Profiler, normal generated R3_2 output-enable path, Hall closed-loop,
  speed loop, and sensorless paths;
- explicit statement that no flash, Run / Debug, USB runtime execution, 24 V,
  Gate PWM output, Motor Pilot, Motor Profiler, motor connection, or readiness
  claim is opened.

## Decision For Progress

This Gate E0 record opens only the next repository-side checkpoint:

```text
Gate E1 isolated waveform source-package planning/review
or a build-side boundary plan that still has no build, flash, runtime, 24 V,
Gate PWM output, Motor Pilot, Motor Profiler, or motor connection.
```

Still forbidden after this plan:

- flash;
- Run / Debug;
- 24 V;
- Gate PWM output;
- oscilloscope probing on live gate or phase nodes;
- Motor Pilot / Profiler;
- motor connection;
- Hall closed loop;
- sensorless operation;
- power-stage readiness or motor readiness claims.
