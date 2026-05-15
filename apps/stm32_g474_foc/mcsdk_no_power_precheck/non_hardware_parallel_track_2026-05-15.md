# P2 Non-Hardware Parallel Track - 2026-05-15

这个文件记录一条明确策略：硬件源包支线可以暂时跳过，但不能视为已解决。
P2 仍然只推进 no-power、no-motor、no-Gate-PWM 的软件和接口准备工作。

## Safety Boundary

- No 24V.
- No power-board connection.
- No motor connection.
- No Gate PWM output.
- No Motor Profiler run.
- No Hall closed-loop claim.
- No sensorless / SMO claim.

## 功能句

在 Packet B/C 硬件源证据没有完全闭环前，项目可以先推进 MCSDK
配置证据、STM32 侧接口契约、未来 build-only gate 和提交材料，但不能把这些
工作写成硬件通过。

## Skipped, Not Cleared

| Blocker | Current handling | Why it stays blocked |
| --- | --- | --- |
| Packet B - CN8 / board route | Temporarily skipped for scheduling. | The 2026-05-15 schematic screenshot is only `Partial clue`; accepted STM32 endpoint mapping is still missing. |
| Packet C - STDRIVE101 protection path | Temporarily skipped for scheduling. | `DT/MODE`, `STBY`, and protection-threshold proof remain unresolved. |
| PB3 / SWO release | Temporarily skipped for scheduling. | Current `.ioc` still records `PB3.Signal=SYS_JTDO-SWO`; Hall B readiness is not proven. |
| Powered checks | Not part of P2. | They require later gated hardware stage evidence. |

## Allowed Parallel Work

| Track | Allowed work now | Output artifact | Still forbidden |
| --- | --- | --- | --- |
| Packet A - MCSDK / MotorControl evidence | Capture or import `.stmcx`, MotorControl screenshot, or exact GUI path/version/config screen. | Update `evidence_packet_2026-05-14.md` only for proven config fields. | No Motor Profiler, no Gate PWM output, no hardware behavior claim. |
| STM32-side signal contract | Write the desired STM32-side meaning of CN8-facing nets as a planning contract. | A no-power interface contract that says which signals are candidates, blocked, or unknown. | No claim that connector routing is proven. |
| Future generated-project gate | Define the checks that must exist before any generated project is trusted or built. | A build-only gate for later use after Packet A exists. | No generated project trust without `.stmcx` / MotorControl evidence. |
| Delivery / report readiness | Keep submission checklist and evidence register honest. | Clear status language for答辩: planning proof vs hardware proof. | No measured performance, Hall, SMO, or motor claim. |

## STM32-Side Signal Contract Draft

This is a planning contract, not a wiring proof.

| CN8-facing net from candidate screenshot | Intended STM32-side meaning | Current candidate or policy | Evidence status |
| --- | --- | --- | --- |
| `HIN1/LIN1/HIN2/LIN2/HIN3/LIN3` | STDRIVE101 input commands for three phases. | Must be matched to MCSDK/TIM1 output mode after `DT/MODE` is proven. | Blocked: no accepted STM32 endpoint mapping and no Packet A. |
| `NFAULT` | Fault input to STM32 break/fault path. | Draft candidate remains `PB12/TIM1_BKIN`. | Blocked: power-board side clue exists; STM32-side connector mapping still missing. |
| `ADC_U/ADC_V/ADC_W` | Phase or shunt-related analog feedback into ADC / OPAMP plan. | Must avoid `PA2/PA3` VCP conflict and match MCSDK current-sense mode. | Blocked: no accepted ADC/OPAMP endpoint mapping. |
| `IA/IB/IC` | Hall or interface signals as labelled by the schematic. | `PB3` cannot be claimed for Hall B while SWO owns it. | Blocked: no accepted Hall endpoint mapping and no SWO release proof. |
| `3V3` | Logic supply reference between STM32 side and power board. | Must remain a no-power planning item until source and continuity checks exist. | Partial clue only. |
| `GND_SIGNAL` | Signal return reference. | Must be reviewed with `GND_POWER` / `R_GND_ISO` before any hardware interpretation. | Partial clue only. |

## Future Generated-Project Gate

Do not generate or trust an MCSDK motor-control project until all of these are
true:

1. Packet A exists: `.stmcx` or MotorControl / Workbench configuration screenshot.
2. The config explicitly records MCU / board context, PWM / timer choices,
   fault input, current-sense mode, Hall / sensorless selection or absence,
   `PA2/PA3` policy, and `PB3` ownership.
3. The project is treated as build-only and no-power.
4. The evidence register says it proves configuration familiarity only.
5. The no-go list remains visible: no 24V, no power-board connection, no motor
   connection, no Gate PWM output, no Motor Profiler run, no Hall closed-loop
   claim, no sensorless / SMO claim.

## Next Codex Work That Does Not Need Hardware Source

1. Search again for `.stmcx` only when new files are expected or the user gives a path.
2. Prepare a Packet A capture checklist for the next GUI session.
3. Keep the STM32-side signal contract current as new `.ioc` or MotorControl
   config evidence arrives.
4. Update status and tests after every evidence change.

## Current Decision

The hardware-source branch is skipped for scheduling only. It is not cleared.
This scheduling decision does not close Packet B or Packet C.
P2 can continue Packet A / interface-contract / build-gate preparation, but
cannot claim CN8 routing proof, STDRIVE101 protection-path proof, power-stage
readiness, Hall readiness, Motor Profiler readiness, motor readiness, or
sensorless readiness.

## 2026-05-15 Standalone Track Artifacts

The inline drafts above now have standalone repo artifacts:

- `stm32_side_signal_contract_2026-05-15.md`
- `future_build_only_gate_2026-05-15.md`

These files make the STM32-side signal contract and future build-only gate
reviewable without upgrading Packet A/B/C or any hardware evidence.
