# Future Build-Only Gate - 2026-05-15

This gate defines how a later MCSDK-generated project may be handled while the
project remains no-power. It is a future control rule, not a generated project,
not a build record, and not hardware validation.

## Safety Boundary

- No 24V.
- No power-board connection.
- No motor connection.
- No Gate PWM output.
- No Motor Profiler run.
- No Hall closed-loop claim.
- No sensorless / SMO claim.
- No flash or board run from a generated motor-control project unless a later
  phase gate explicitly allows it.

## Feature Sentence

If a future MCSDK project is generated before hardware evidence is complete,
Codex may treat it only as a no-power build artifact, and only after Packet A
configuration evidence exists.

## Gate States

| State | Meaning | Current project decision |
| --- | --- | --- |
| `Not allowed` | Required config evidence is missing or only partial. | Superseded for Packet A on 2026-05-21 by `source_packet_review_2026-05-21_001_qiansai_g474_stdrive101_foc_p2_generated_project.md`. |
| `Build-only allowed` | Packet A selected fields are accepted and the project is explicitly marked no-power. | Source prerequisite satisfied on 2026-05-21; local Debug build-only pass recorded on 2026-05-27. |
| `Hardware allowed` | Later phase gates provide no-power checks, current limits, measurement points, rollback path, and safety evidence. | Not a P2 state. |

## Prerequisites For Build-Only

Do not generate, trust, or build an MCSDK motor-control project until all of
these are true:

1. Packet A exists: real `.stwb6` / legacy `.stmcx`, MotorControl / Workbench
   configuration screenshot, or exact GUI path plus captured version/config
   screen.
2. Packet A records MCU / board context, TIM1/PWM mode, fault input,
   current-sense mode, Hall/sensorless selection or absence, `PA2/PA3` policy,
   and `PB3` ownership.
3. The generated project path is separate from the P1 NUCLEO baseline unless
   the user explicitly asks for a scoped replacement.
4. The build output is recorded as configuration/build evidence only.
5. Packet B/C blockers are copied forward if endpoint mapping, `DT/MODE`,
   `STBY`, or STDRIVE101 protection proof is still missing.

2026-05-21 route clarification: current PCB2 `PB3` is fixed as `LIN1`, not
current Hall. Software Hall planning uses `PA0/PA1/PB4`, and `P14/P15` are
confirmed `3V3/GND`. Any `PB3` Hall use is alternate/hardware-rework only.

## Allowed Build-Only Actions

After the prerequisites are met, Codex may:

- inspect generated source layout;
- run a no-power build;
- record compiler output, warnings, and binary size;
- review whether generated code selected expected modules;
- update evidence files to say "build-only configuration evidence".

## Forbidden Actions In This Gate

Codex must not:

- flash the generated motor-control project;
- connect the power board;
- connect the motor;
- apply 24V;
- enable or observe Gate PWM output;
- run Motor Profiler;
- claim Hall closed-loop behavior;
- claim sensorless / SMO behavior;
- treat compile success as proof of CN8 routing, driver readiness, current
  sensing, protection behavior, or motor behavior.

## Build Record Template

When the gate is used later, record:

| Field | Required content |
| --- | --- |
| Source config | `.stwb6` / legacy `.stmcx` / screenshot / GUI path that authorized build-only work. |
| Generated path | Repo path of the generated project. |
| Build command | Exact command and working directory. |
| Result | Pass/fail, warnings, binary path, and size if available. |
| Evidence limit | State that it proves build-only configuration familiarity. |
| Carry-forward blockers | Packet B/C, `DT/MODE`, `STBY`, alternate-use PB3/SWO, endpoint mapping where still needed, continuity checks, and powered checks. |

## Exit Rule

Build success remains build-only evidence.

A build-only pass can upgrade only this statement:

`The generated project compiles in the local toolchain under no-power scope.`

It cannot upgrade any of these statements:

- CN8 routing is correct.
- STDRIVE101 protection paths are correct.
- cannot claim Gate PWM behavior is safe.
- Motor Profiler can run.
- Hall closed-loop works.
- Sensorless / SMO works.
- The motor is ready to connect or spin.

## Current Decision

Current state is `Build-only source prerequisite satisfied / no-power Debug build-only pass recorded`.

`source_packet_review_2026-05-21_001_qiansai_g474_stdrive101_foc_p2_generated_project.md`
accepts the Packet A selected fields as no-power configuration evidence. The
generated Workbench project was then checked by a no-power Debug build-only
command on 2026-05-27.

Build record:

- Result file:
  `build_only_result_2026-05-27_qiansai_g474_stdrive101_foc_p2_debug.md`.
- Command:
  `cmake --build "C:\Users\gregrg\.st_workbench\projects\QIANSAI_G474_STDRIVE101_FOC_P2\build\Debug" --config Debug`.
- Result: exit code `0`; Ninja output `ninja: no work to do`.
- Artifacts confirmed: `.elf` and `.map`.
- Tool paths came from STM32Cube bundled Ninja and GNU Arm GCC, not from
  global `PATH`.

Build success proves only:

`The generated project compiles in the local toolchain under no-power scope.`

It will not prove current PCB2 routing, STDRIVE101 protection, current sensing,
Hall behavior, Gate PWM safety, Motor Profiler readiness, motor readiness,
power-stage readiness, or sensorless / SMO behavior.

It also will not prove the software Hall adapter on `PA0/PA1/PB4` is integrated
with MCSDK or safe for Hall closed-loop use.
