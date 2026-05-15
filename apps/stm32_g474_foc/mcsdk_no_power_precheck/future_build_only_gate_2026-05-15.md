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
| `Not allowed` | Required config evidence is missing. | Current state because Packet A is still blocked. |
| `Build-only allowed` | Packet A exists and the project is explicitly marked no-power. | Future state only. |
| `Hardware allowed` | Later phase gates provide no-power checks, current limits, measurement points, rollback path, and safety evidence. | Not a P2 state. |

## Prerequisites For Build-Only

Do not generate, trust, or build an MCSDK motor-control project until all of
these are true:

1. Packet A exists: real `.stmcx`, MotorControl / Workbench configuration
   screenshot, or exact GUI path plus captured version/config screen.
2. Packet A records MCU / board context, TIM1/PWM mode, fault input,
   current-sense mode, Hall/sensorless selection or absence, `PA2/PA3` policy,
   and `PB3` ownership.
3. The generated project path is separate from the P1 NUCLEO baseline unless
   the user explicitly asks for a scoped replacement.
4. The build output is recorded as configuration/build evidence only.
5. Packet B/C blockers are copied forward if endpoint mapping, `DT/MODE`,
   `STBY`, or STDRIVE101 protection proof is still missing.

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
| Source config | `.stmcx` / screenshot / GUI path that authorized build-only work. |
| Generated path | Repo path of the generated project. |
| Build command | Exact command and working directory. |
| Result | Pass/fail, warnings, binary path, and size if available. |
| Evidence limit | State that it proves build-only configuration familiarity. |
| Carry-forward blockers | Packet B/C, `DT/MODE`, `STBY`, PB3/SWO, endpoint mapping, continuity checks, and powered checks. |

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

Current state is `Not allowed` for generated-project trust because Packet A
remains blocked. This file only creates the future gate so that a later
generated project, if created, stays build-only until stronger evidence exists.
