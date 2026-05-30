# P2 Source Packet Review - 2026-05-15-002 - My_First_FOC.stwb6

Review template source:
`source_packet_review_template_2026-05-14.md`.

This review covers a local Packet A MCSDK / MotorControl source candidate found
after the 2026-05-15 checkpoint. On 2026-05-16 the user clarified that this
file is a previous Workbench learning artifact and that the `EVALSTDRIVE101`
power-board choice was arbitrary, so it stays legacy `Partial clue` only.

## Packet Metadata

| Field | Value |
| --- | --- |
| Review ID | `P2-SOURCE-REVIEW-2026-05-15-002` |
| Packet type | Packet A - MCSDK / MotorControl configuration |
| Source file | `packet_a_sources/2026-05-15_my_first_foc/My_First_FOC.stwb6` |
| Original path | `F:\STMCSDK\My_First_FOC.stwb6` |
| Source timestamp | 2026-04-27 16:37:42 |
| Source owner | Local machine file; user clarified it is a previous learning artifact, not the custom-board Packet A source. |
| Tool path | `F:\STMCSDK\MC_SDK_6.4.2\Utilities\PC_Software\STMCWB\STMCWB.exe` |
| Tool version | ST MC Workbench 6.4.2 |
| Source format note | MCSDK 6 stores Workbench projects as `.stwb6`; legacy `.stmcx` is not the only valid format. |

## Extracted Source Facts

The `.stwb6` file is JSON-readable and records:

| Field | Extracted value | Decision |
| --- | --- | --- |
| Workbench project file | `My_First_FOC.stwb6` | Accepted as a real MCSDK 6 Workbench project file. |
| Algorithm | `FOC` | Accepted for source intent only. |
| Workbench version | `6.4.2` | Accepted. |
| Control board | `NUCLEO-G474RE` | Accepted for NUCLEO context. |
| MCU | `STM32G474RETx` | Accepted for MCU context. |
| Power board | `EVALSTDRIVE101` | Partial clue only; this is not the custom current physical power board. |
| Motor | `R57BLB50L2` / MOONS Zest demo motor | Partial clue only; not the competition motor proof. |
| PWM / timer clues | File contains `TIM1_CH1`, `TIM1_CH2`, `TIM1_CH3`, `TIM1_CH1N`, `TIM1_CH2N`, and `TIM1_CH3N` hardware variants. | Partial clue only until the Workbench GUI shows the selected topology. |
| Fault input clues | File contains `TIM1_BKIN` and `TIM1_BKIN2` hardware variants; `PB12` appears as NUCLEO connector `CN10.16`. | Partial clue only; it does not prove the custom-board `NFAULT` route to `PB12/TIM1_BKIN`. |
| Current sensing clues | File contains `ThreeShunt_AmplifiedCurrents` under `EVALSTDRIVE101`. | Partial clue only; not proof of the custom three-shunt/OPAMP/ADC implementation. |
| Hall clues | File contains `HallEffectSensor` variants and `PB3` connector clues. | Partial clue only; `PB3` Hall readiness remains blocked by SWO release and board-route evidence. |
| `PA2/PA3` clues | File contains `PA2` / `PA3` as NUCLEO connector UART candidates. | Partial clue only; it does not prove final FOC communication policy. |

## Packet A Decision

Overall decision: `Partial clue`.

Accepted:

- the repo now has a real MCSDK 6 Workbench project-file candidate;
- the exact Workbench launcher path is known;
- tool version `6.4.2`, algorithm `FOC`, control board `NUCLEO-G474RE`, and MCU
  `STM32G474RETx` are recorded in a source file.

Still blocked:

- final custom-board context;
- TIM1 complementary PWM selected topology in the GUI;
- final `NFAULT` / `PB12/TIM1_BKIN` selection;
- current-sense selection for the custom board;
- Hall/sensorless final selection;
- `PA2/PA3` exclusion or reuse decision;
- `PB3` SWO release or Hall B ownership;
- any generated-project trust.

## Forbidden Conclusions

Do not claim from this source that:

- MCSDK MotorControl configuration is complete for the competition board;
- a generated motor-control project may be trusted, built, flashed, or run;
- CN8 routing is proven;
- STDRIVE101 protection paths are proven;
- no Gate PWM behavior, Motor Profiler, Hall, motor, power-stage, or sensorless behavior is validated.

## Next Required Capture

Open the file in ST MC Workbench 6.4.2 and capture no-power screenshots showing:

1. project/global view with NUCLEO-G474RE, `STM32G474RETx`, Workbench version,
   and `EVALSTDRIVE101` or any replaced custom-board context;
2. PWM generation / fault / current-sensing pages showing the actually selected
   topology and protection input;
3. Hall/sensorless and communication pages showing `PA2/PA3` policy and `PB3`
   ownership.

If these screenshots remain incomplete, Packet A stays `Partial clue` and
generated-project trust stays `Not allowed`.
