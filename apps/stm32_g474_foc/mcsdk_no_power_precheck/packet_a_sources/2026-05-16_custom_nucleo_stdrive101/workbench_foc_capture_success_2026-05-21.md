# Workbench FOC Capture Success - No-Power Packet A Source

Date: 2026-05-21

Decision: `Workbench FOC source captured / no-power Packet A source evidence upgraded / hardware and build trust still blocked`.

This record archives the first reviewable ST Motor Control Workbench 6.4.2 FOC configuration source for the custom NUCLEO-G474RE + user STDRIVE101 power-board route. It is configuration evidence only. It does not authorize generated-source trust, build-only clearance, flashing, 24V, motor connection, Gate PWM output, Motor Profiler, Motor Pilot, Hall closed-loop readiness, or sensorless readiness.

## Archived Sources

| File | SHA256 | Role |
| --- | --- | --- |
| `QIANSAI_G474_STDRIVE101_FOC_P2_2026-05-21.stwb6` | `05CD6F0DF86276DE10C96CCCFE5AA32E04C9EDE7D8B27E4242D3532D2A126643` | Primary Workbench FOC configuration source |
| `MY-STDRIVE101_POWER_BOARD.foc_no_power_2026-05-21.json` | `80B655D52D082F89E6CE73804E9A15511D24A9FF3C965494F6A0D98527311B7A` | User power-board definition used by Workbench |
| `screenshots/2026-05-21_workbench_foc_hall_driver_protection_overview.png` | `C6A1B455B4B870BBE0FE1A965777885E1BFB8F6BF671F73772D8EF1A7A7F0EB6` | Auxiliary desktop screenshot; not the only evidence because it includes the wider desktop |

The external live Workbench source was:

`C:\Users\gregrg\.st_workbench\projects\QIANSAI_G474_STDRIVE101_FOC_P2.stwb6`

## Read-Only Verification

Read-back of the archived `.stwb6` confirms:

- `algorithm`: `FOC`
- Workbench version: `6.4.2`
- Control board: `NUCLEO-G474RE`
- MCU: `STM32G474RETx`
- Power board: `MY-STDRIVE101_POWER_BOARD`
- Motor placeholder: `R57BLB50L2`
- Hall is selected in the Workbench source:
  - `HallEffectSensor`
  - `hasHallSensor: true`
  - `speedSensingSel_0.mainSensorParams.speedSensorMode: hall`

## Key No-Power Board Routes In The Source

Power-board definition routes:

- Current sensing:
  - `CURRENT_AMPL_U -> ML30`
  - `CURRENT_AMPL_V -> MR24`
  - `CURRENT_AMPL_W -> ML34`
- TIM1 complementary PWM:
  - `PWM_CHU_H -> MR23`
  - `PWM_CHV_H -> MR21`
  - `PWM_CHW_H -> MR33`
  - `PWM_CHU_L -> MR30`
  - `PWM_CHV_L -> MR28`
  - `PWM_CHW_L -> MR26`
- Hall source route:
  - `HALLSENSOR_H1 -> ML17`
  - `HALLSENSOR_H2 -> MR31`
  - `HALLSENSOR_H3 -> MR25`
- Driver protection:
  - `DP_TRIGGER -> MR16`
  - `DPSignalPolarity: Active low`
  - `DPTriggerFilterDuration: 0`

Workbench connection output inside `.stwb6` includes:

- PWM solved as `PA8/TIM1_CH1`, `PA9/TIM1_CH2`, `PA10/TIM1_CH3`, `PB13/TIM1_CH1N`, `PB14/TIM1_CH2N`, `PB15/TIM1_CH3N`.
- Hall solved as `PA15/TIM2_CH1`, `PB3/TIM2_CH2`, `PB10/TIM2_CH3`.
- Driver protection solved as `PB12/TIM1_BKIN`.

The `MR24` change was the key GUI unblock for FOC. The earlier `CURRENT_AMPL_V -> MR15` model made hardware checks look green but kept FOC disabled.

## Generated Project Side Effect

After the GUI `Create` flow, Workbench also created a local generated-project directory:

`C:\Users\gregrg\.st_workbench\projects\QIANSAI_G474_STDRIVE101_FOC_P2`

Selected files were archived as source clues under:

`../2026-05-21_qiansai_g474_stdrive101_foc_p2_generated_project/`

Hashes:

- `main.c`: `4B51A0A9ED5B988379D35DB97BB8EF922DCC97D415CFB08477607ADC4BDFE1A0`
- `mc_config.c`: `3E066A1ED75EB599E33C5615DF1AAEFDC753C83BC2B5C7D574F40285BBA1EA42`
- `parameters_conversion.h`: `3029E881005A36752C238F746D9894333E7886CFAFC0CE173D81A0AEE30026FB`
- `QIANSAI_G474_STDRIVE101_FOC_P2.ioc`: `6DFADF888374C8B2E63E89621E4448B58C042728A6A5AD019B28CECB91B58274`
- `QIANSAI_G474_STDRIVE101_FOC_P2.ioc.wb`: `E3ABC3BE3C1EF1B0FF8CF5BD0EAF54F60CC99B75C7514E4DA155F9E1E8B23D56`
- `QIANSAI_G474_STDRIVE101_FOC_P2.log`: `0C4341C46FF9E004B020C7526B645A5689852F7E92FD679A38255466DA85A86F`
- `QIANSAI_G474_STDRIVE101_FOC_P2.wbdef`: `D7F004653B4CC3A7CC0D1AED20F83A91932F5B8ADFD10B89D60255BFA397B687`

These files are not accepted as trusted generated firmware yet. They require a separate no-power source review before any build-only work.

## Remaining Blockers

- The Workbench route is a compatibility/model route. It is not physical proof of the current PCB2 as-built route.
- Existing project clues still record a current PCB2 Hall route of `PA0/PA1/PB4`; the Workbench FOC route uses `PA15/PB3/PB10`.
- Current-sense and Hall routes need schematic/netlist/continuity review before any hardware claim.
- `R57BLB50L2` remains a temporary Workbench motor placeholder, not measured motor data.
- No build-only clearance exists until the generated source is reviewed.
- No powered readiness exists.

## Safety Boundary

- No Generate action is authorized from this record.
- No build.
- No flash.
- No 24V.
- No power-board connection.
- No motor connection.
- No Gate PWM output.
- No Motor Profiler.
- No Motor Pilot.
- No Hall closed-loop claim.
- No sensorless / SMO claim.
