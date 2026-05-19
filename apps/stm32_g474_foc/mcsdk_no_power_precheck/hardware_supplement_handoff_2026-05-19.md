# Hardware Supplement Handoff - 2026-05-19

This handoff turns the current P2 hardware blockers into exact materials that
the hardware teammate can provide without touching powered hardware.

It is not a wiring instruction, not a continuity record, not generated
firmware, not a Workbench project, and not hardware validation.

## Gate

| Field | Decision |
| --- | --- |
| Project goal | Advance the STM32G474 + self-developed STDRIVE101 driver-board P2 no-power precheck. |
| Learning goal | Make clear which hardware materials can unlock Packet B/C and which items still do not allow power or motor work. |
| Change scope | Documentation, status, evidence-entry, and hardware handoff records only. |
| Forbidden scope | No 24V, no power-board connection, no motor connection, no Gate PWM output, no Motor Profiler, no source generation, no build, no flash. |

## Current Evidence Baseline

Current accepted clues:

- `ProDoc_P1_2026-05-19.epro` gives current schematic-source clues for the
  self-developed STDRIVE101 driver board, including `CN3`, `U1=STDRIVE101`,
  `J_HALL`, `J_MOTOR`, shunts, `NFAULT`, `REG12`, `SCREF`, bootstrap, and
  output nets.
- `Gerber_PCB2_2026-05-19.zip` gives board-side Gerber plus
  `FlyingProbeTesting.json` pad/net clues for `CN3`, STDRIVE101 pads, PWM
  input paths, shunt/current-sense nets, Hall/motor connectors, and protection
  related nets.

Short outbound request:

- Use `hardware_teammate_min_request_2026-05-19.md` first when sending the
  next message to the hardware teammate. It asks only for exact Gerber PCB2
  revision confirmation, complete `CN3 -> NUCLEO/CN8 -> STM32 pin` mapping,
  and marked `CN3` / `J_HALL` pin-1 evidence.

Current blockers unchanged:

- NUCLEO `CN8` and STM32 endpoint mapping are not proven.
- Physical connector/cable continuity is not proven.
- Exact fabrication / assembly / tested-board revision match is not confirmed.
- `PB3` / SWO release and Hall B readiness are not proven.
- `J_HALL` physical pin-1 and Hall A/B/C numbering are not accepted.
- Packet A Workbench selected fields remain `Partial clue / stopped`.
- Generated-project trust remains `Not allowed`.
- Power-stage readiness, Motor Profiler readiness, Hall readiness, motor
  readiness, and sensorless readiness remain not allowed.

## Hardware Teammate Request Matrix

| Priority | Request | Accepted source forms | Why it matters | Current status after review |
| --- | --- | --- | --- | --- |
| P0 | Confirm whether `Gerber_PCB2_2026-05-19.zip` is the exact PCB revision being fabricated, assembled, or tested. | Board revision note, order screenshot, assembly note, marked board photo, or EDA export metadata. | Prevents using same-day but non-final files as final board truth. | Blocked until confirmation is provided. |
| P0 | Provide `CN3 -> NUCLEO/CN8 -> STM32 pin` mapping for every control signal. | Table, schematic page, harness drawing, connector diagram, or readable EDA screenshot. | Converts board-side `CN3` clues into endpoint proof. | Board-side `CN3` is visible; NUCLEO and STM32 endpoints are blocked. |
| P0 | Mark `CN3` pin 1 and `J_HALL` pin 1 orientation. | Marked board photo, assembly drawing, silkscreen screenshot, or EDA placement screenshot. | Prevents mirrored connector and Hall order mistakes. | `J_HALL` numbering is blocked. |
| P0 | State Hall A/B/C relationship to `IA/IB/IC` and the physical Hall connector. | Connector table, harness drawing, EDA screenshot, or no-power inspection note. | Needed before Hall fallback can be treated as a real route. | Candidate clue only. |
| P1 | If Hall B still uses `PB3/TIM2_CH2`, provide SWO release or isolation evidence; otherwise provide the alternate Hall B endpoint. | NUCLEO solder-bridge/manual evidence, CubeMX/Workbench screenshot, or board route evidence. | `PB3` is still owned by SWO in the accepted NUCLEO draft. | Blocked. |
| P1 | Finish STDRIVE101 protection path details for `DT/MODE`, `STBY`, `CP`, `SCREF`, and `NFAULT`. | Schematic source, PCB source, netlist, readable crop, threshold calculation, or reviewer note tied to the current board revision. | Needed before protection-path proof can be accepted. | Partial clue; `CP`, `STBY`, threshold math, and STM32 endpoint handling remain unresolved. |
| P1 | Provide the EasyEDA Pro PCB source if available, not only Gerber. | EDA Pro project with PCB layout, PCB source export, or object-level layout source. | Allows object-level layout review and cross-check against Gerber pad nets. | Current `.epro` has schematic only; PCB source is absent. |
| P2 | Prepare a no-power continuity / short-check record for the actual wiring stage. | Later DMM table with probe points, expected net, measured continuity/resistance, and board revision. | Required before any future powered phase gate. | Not started; this handoff does not perform continuity checks. |

Required `CN3` mapping rows:

| CN3 pin | Board-side net | Hardware teammate must add |
| --- | --- | --- |
| 1 | `HIN1` | NUCLEO connector pin and STM32 pin |
| 2 | `LIN1` | NUCLEO connector pin and STM32 pin |
| 3 | `HIN2` | NUCLEO connector pin and STM32 pin |
| 4 | `LIN2` | NUCLEO connector pin and STM32 pin |
| 5 | `HIN3` | NUCLEO connector pin and STM32 pin |
| 6 | `LIN3` | NUCLEO connector pin and STM32 pin |
| 7 | `ADC_U` | NUCLEO connector pin and STM32 ADC/OPAMP endpoint |
| 8 | `ADC_V` | NUCLEO connector pin and STM32 ADC/OPAMP endpoint |
| 9 | `ADC_W` | NUCLEO connector pin and STM32 ADC/OPAMP endpoint |
| 10 | `IA` | NUCLEO connector pin and STM32 Hall endpoint |
| 11 | `IB` | NUCLEO connector pin and STM32 Hall endpoint |
| 12 | `IC` | NUCLEO connector pin and STM32 Hall endpoint |
| 13 | `NFAULT` | NUCLEO connector pin and STM32 break/fault endpoint |
| 14 | `3V3` | Source of `3V3` and connector endpoint |
| 15 | `GND_SIGNAL` | Ground endpoint and return path |

## Acceptance Rules

- A source can upgrade only the exact field it proves.
- Oral descriptions remain clues unless paired with a repo-stored source,
  screenshot, table, or marked photo.
- Same-day source files still need a current-board revision statement before
  being treated as final fabrication evidence.
- Packet B/C evidence does not upgrade Packet A, generated-project trust,
  Workbench selected fields, continuity, powered readiness, or motor readiness.
- No-power continuity records are allowed only as future DMM records; they do
  not authorize power without a later phase-gate decision.

## Packet A Parallel Track

In parallel, continue searching for a Workbench-supported Custom / Generic
entry or import path for the self-developed STDRIVE101 driver board.

Packet A remains blocked until a project-specific `.stwb6` or accepted
configuration screenshots prove the selected PWM, fault input, current-sense,
Hall/sensorless, UART, and `PB3` choices. Built-in ST power-board entries such
as `EVALSTDRIVE101` or `STEVAL-LVLP01` are not board-match substitutes for the
self-developed driver board.

## Review Procedure After New Hardware Material Arrives

1. Archive the source under `hardware/` or a clearly named P2 source directory.
2. Record source owner, source date/version, board revision, and whether it
   matches the current physical board.
3. Review the packet with `source_packet_review_template_2026-05-14.md`.
4. Update only the proven fields in `evidence_packet_2026-05-14.md`.
5. Refresh `p2_readiness_snapshot_2026-05-15.md` and
   `workflow/evidence_register.md`.
6. Run `python -m unittest discover -s tests`.
7. Rebuild `vector_store/` after status, workflow, docs, or evidence changes.

## Hardware Teammate Short Template

```text
我提供 P2 硬件补证。
文件路径：
来源日期/版本：
是否匹配当前打样/焊接/测试板：
补的是：版本确认 / CN3-CN8-STM32 映射 / CN3 pin-1 / J_HALL pin-1 / PB3-SWO / STDRIVE101 保护链 / PCB 源文件 / 断电连续性记录
我没有接 24V、没有接功率板、没有接电机、没有运行 Motor Profiler、没有输出 Gate PWM。
```

## Current Decision

This handoff makes the next hardware-teammate request executable and
reviewable. It does not upgrade Packet A/B/C, PB3/SWO, `J_HALL`, generated
project trust, continuity, powered readiness, motor readiness, Hall readiness,
or sensorless readiness.
