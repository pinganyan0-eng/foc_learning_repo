# 2026-05-19 MY_FOC Manual FOC Edit Rollback

Codex backed up and then restored the source Workbench project:
`C:\Users\gregrg\.st_workbench\projects\MY_FOC.stwb6`.

Backup:
`C:\Users\gregrg\.st_workbench\projects\MY_FOC.stwb6.pre_codex_foc_edit_2026-05-19.bak`.

Edit record:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/my_foc_foc_candidate_edit_2026-05-19.md`.

Decision: `Manual FOC source edit failed Workbench reload / rolled back / Packet A still not accepted`.

Accepted exact clues:

- A one-field manual edit from `"algorithm": "sixStep"` to `"algorithm": "FOC"`
  made Workbench unable to load the file.
- The user reported `一般错误 / 无法加载文件:
  C:/Users/gregrg/.st_workbench/projects/MY_FOC.stwb6`.
- Codex restored the external source from backup.
- The current external source again reads `"algorithm": "sixStep"` and matches
  the backup SHA256:
  `062B78AD8E07B5A29A68A007797200FCD4833FE9D3371D2821F3A54D5B9429FD`.

Blocked exact fields:

- The failed manual FOC candidate is negative evidence only.
- Generated `MY_FOC.ioc`, `MY_FOC.wbdef`, `Src/`, and `Inc/` still reflect the
  old generated six-step outputs.
- No Generate, build, flash, 24V, power-board connection, motor connection, No
  Gate PWM output readiness, Motor Profiler readiness, Hall readiness, motor
  readiness, power-stage readiness, or sensorless readiness is upgraded.
- Packet A still not accepted and no generated-project trust is added.

# 2026-05-19 MY_FOC Generated Project Source Review

New user-created Workbench project source:
`C:\Users\gregrg\.st_workbench\projects\MY_FOC`.

Archived selected no-power source files:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-19_my_foc_generated_project/`.

New source review:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-19_005_my_foc_generated_project.md`.

Decision: `Partial clue / generated project quarantined / Packet A not accepted`.

Accepted exact clues:

- MC Workbench 6.4.2 generated a real `MY_FOC` project on this machine.
- MCU/control context is `NUCLEO-G474RE`, `STM32G474RETx`, and
  `STM32G474RE`.
- Power-board naming includes `M1_POWERBOARD_NAME=~MY-STDRIVE101_POWER_BOARD`
  and `M1_PWM_DRIVER_PN=STDRIVE101`.
- Hall sensor selection exists in the generated configuration.
- The user clarified that pins can be changed; therefore the current Hall/PWM
  mismatch is a future editable route, not a permanent rejection.

Blocked exact fields:

- The project is `SIX_STEP`, not FOC.
- Generated sources include `mc_tasks_sixstep.c`, `pwmc_sixstep.c`, and
  `speed_duty_ctrl.c`.
- Current sensing is disabled: `M1_CUR_READING=false`.
- Fault/break is disabled: `TIM1.BreakState=TIM_BREAK_DISABLE`.
- Generated Hall `PA15/PB3/PB10` and generated PWM
  `PA8/PB13/PA9/PB14/PA10/PB15` are not accepted as the current PCB2 route.
- Motor entry `R57BLB50L2` / `MOONS motor for Zest Demo` is not the project
  motor evidence.
- Packet A not accepted. No generated-project trust, build-only clearance,
  No Gate PWM output readiness, Motor Profiler readiness, Hall readiness, motor readiness,
  power-stage readiness, or sensorless readiness is upgraded.

# 2026-05-19 Packet A Board Designer / Board Manager Path Review

New no-power Packet A path review:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_board_designer_manager_path_review_2026-05-19.md`.

Decision: `Board Designer / Board Manager path exists as local documentation
and tool clue / Packet A still blocked`.

Accepted governance updates:

- Workbench `wb2mx.properties` exposes Board Designer and Board Manager as
  external tools.
- Local `STMCBoardDesigner.exe` and `STMCBoardManager.exe` are present.
- Local `STMCBD-UM.pdf` describes creating Power, Control, and Inverter boards,
  importing external boards, custom board clone/modify/delete operations, and
  Board Aggregation from control-board plus power-board choices.
- The path is now documented enough to define a future no-power custom/user
  board capture task for the self-developed STDRIVE101 board.

Blocked exact fields:

- Packet A not accepted.
- Built-in `EVALSTDRIVE101`, `STEVAL-LVLP01`, and `EVLDRIVE101-HPD` remain
  non-substitutes for the project self-developed STDRIVE101 board.
- No custom board source, project-specific `.stwb6`, selected-field
  screenshot, generated project, build-only clearance, firmware, runtime API,
  continuity, Hall readiness, Motor Profiler readiness, motor readiness,
  power-stage readiness, or sensorless readiness is upgraded.
- Generated-project trust remains `Not allowed`; no generated-project trust is
  added by this review.

# 2026-05-19 Software Hall Adapter Design Review

New no-power software Hall adapter design review:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_adapter_design_review_2026-05-19.md`.

Decision: `Software Hall adapter remains no-power design review / Packet A not accepted`.

Accepted governance updates:

- Current PCB2 Hall route stays `J_HALL -> IA/IB/IC -> PA0/PA1/PB4`.
- The review defines future GPIO/EXTI sampling candidates, edge timestamping,
  valid-state filtering, bounce/repeated-state rejection, minimal ISR
  responsibility, and MCSDK integration boundaries.
- The review explicitly avoids function names, buffers, public runtime APIs,
  MCSDK hooks, generated source, and firmware implementation.
- Hard stops are now written: same-timer hardware Hall requirements, invasive
  high-frequency FOC / JEOC edits, time-critical blocking logic, missing
  build-only verification boundary, or unexplainable MCSDK consumption of
  software Hall state all lead to a separate `hardware-rework planning` task.

Blocked exact fields:

- Packet A selected fields are not accepted.
- Generated-project trust remains `Not allowed`.
- Build-only generated-project clearance remains closed.
- No software Hall adapter is implemented or accepted by MCSDK.
- No runtime API, generated source, build, flash, no-power continuity, powered
  readiness, Hall readiness, Motor Profiler readiness, motor readiness, or
  sensorless readiness is upgraded.

# 2026-05-19 Current PCB2 Packet A / Firmware Feasibility Review

New no-power feasibility review:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/current_pcb2_packet_a_firmware_feasibility_2026-05-19.md`.

Decision: `No-PCB-change route remains feasibility only / Packet A not accepted`.

Accepted governance updates:

- Current PCB2 PWM / driver-input route was reviewed against local
  `STM32G474RETx` pin-function clues.
- The route is not cleared as standard MCSDK `TIM1` complementary PWM
  selected-field evidence.
- Current PCB2 Hall route `PA0/PA1/PB4` is not cleared as same-timer hardware
  Hall.
- The no-PCB-change path remains open only as later firmware feasibility
  review for software Hall sampling, timestamping, valid-state filtering, and
  MCSDK integration boundaries.

Blocked exact fields:

- Packet A selected fields are not accepted.
- Generated-project trust remains `Not allowed`.
- Build-only generated-project clearance remains closed.
- No concrete software Hall adapter is implemented or accepted.
- No hardware rework is executed or authorized.
- No continuity, power-stage readiness, Hall readiness, Motor Profiler
  readiness, motor readiness, or sensorless readiness is upgraded.

# 2026-05-19 Current PCB2 Hall/PWM No-Power Strategy Review

New no-power strategy review:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/current_pcb2_hall_pwm_strategy_2026-05-19.md`.

Decision: `No-power strategy review opened / no PCB change first`.

Accepted governance updates:

- Current PCB2 PWM / driver-input route under review is
  `HIN1/LIN1/HIN2/LIN2/HIN3/LIN3 -> PA15/PB3/PB10/PA8/PA9/PA10`.
- Current PCB2 Hall route remains `J_HALL -> IA/IB/IC -> PA0/PA1/PB4`.
- The old standard `TIM1` complementary PWM draft and old
  `PA15/PB3/PB10` hardware Hall draft are historical or alternate candidates
  only. They are not accepted current PCB2 configuration evidence.
- `PA0/PA1/PB4` is not a same-timer hardware Hall set. Software Hall remains
  a future no-power Packet A / firmware design review topic, not Hall
  readiness.
- `PB3` is current PCB2 `LIN1`, not current PCB2 `HALL_B`; any alternate
  Hall use of `PB3` still needs SWO release/isolation and a new accepted route.

Blocked exact fields:

- No accepted Workbench selected-field screenshot or project-specific `.stwb6`
  proves the current PCB2 PWM/Hall choices.
- No generated-project trust, build-only clearance, no-power continuity,
  power-stage readiness, Hall readiness, Motor Profiler readiness, motor
  readiness, or sensorless readiness is upgraded by this strategy review.
- No hardware rework is executed or authorized in this task.

# 2026-05-19 PCB2 Mapping / Pin-1 / Protection Intake

New current PCB2 mapping source packet:
`hardware/schematic/2026-05-19_pcb2_mapping_pin1_protection/`.

New Packet B/C plus PB3/SWO/Hall no-power review:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-19_004_pcb2_mapping_pin1_protection.md`.

Decision: `Partial clue / accepted current PCB2 mapping source; Hall/PWM
conflicts clarified`.

Accepted exact clues:

- The user states the answer corresponds to current PCB2.
- The source provides a P1-P15 mapping from board-side functions to NUCLEO
  positions and STM32 pins, including `HIN1/LIN1/HIN2/LIN2/HIN3/LIN3`,
  `ADC_U/ADC_V/ADC_W`, `IA/IB/IC`, `nFAULT`, `3V3`, and `GND`.
- Two pin-1 / connector-orientation images are archived.
- Hall relationship is stated as `HALL_A -> U/IA`, `HALL_B -> V/IB`,
  `HALL_C -> W/IC`.
- A later clarification image states `PC7/PB3/PB10` was an alternate suggestion,
  not current PCB2 physical routing. Current PCB2 physical Hall route is
  `J_HALL -> IA/IB/IC -> PA0/PA1/PB4`.
- `IA/IB/IC` are Hall signal nets after pull-up/filtering; `ADC_U/ADC_V/ADC_W`
  are current-sense nets.
- STDRIVE101 protection-chain intent is stated as `DT/MODE -> GND`,
  `CP -> 100 nF -> GND`, `SCREF` divider `33 k / 20 k`, `nFAULT` 10 k pull-up
  to 3.3 V, and no separate `STBY` pin.

Blocked exact fields:

- `PB3` / `PB10` apparent conflicts are clarified: `PB3` is current PCB2
  `LIN1`, `PB10` is current PCB2 `HIN2`, and the Hall rows using
  `PC7/PB3/PB10` are alternate suggestions.
- Current PCB2 Hall route `PA0/PA1/PB4` still needs a software Hall or firmware
  design decision because it is not a normal same-timer three-channel Hall
  input set.
- SWO release is described but not captured as an accepted final CubeMX /
  Workbench project state. The older 2026-05-17 pin table still does not
  release SWO by itself.
- Packet A selected fields, timer alternate-function compatibility,
  generated-project trust, no-power continuity, powered readiness, Motor
  Profiler readiness, Hall readiness, motor readiness, and sensorless readiness
  remain unchanged and not allowed.

# 2026-05-19 Minimal Hardware Request And Workbench Asset Probe

New minimal hardware-teammate request:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/hardware_teammate_min_request_2026-05-19.md`.

New Packet A local asset probe:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_workbench_asset_probe_2026-05-19.md`.

Decision: `Workflow/evidence governance only`.

Accepted exact governance updates:

- Hardware teammate should first provide three P0 items: exact Gerber PCB2
  revision confirmation, complete `CN3 -> NUCLEO/CN8 -> STM32 pin` mapping,
  and marked `CN3` / `J_HALL` pin-1 orientation evidence.
- The full handoff remains in
  `hardware_supplement_handoff_2026-05-19.md` for Hall A/B/C mapping, PB3/SWO,
  STDRIVE101 protection details, optional PCB source, and later no-power DMM
  continuity / short-check records.
- Workbench local config references installed Board Designer and Board Manager
  tools, and the installed hardware assets contain built-in STDRIVE101 board
  definitions such as `EVALSTDRIVE101`, `STEVAL-LVLP01`, and
  `EVLDRIVE101-HPD`.

Blocked exact fields:

- No custom self-developed STDRIVE101 board definition is accepted.
- No project-specific `.stwb6`, legacy `.stmcx`, selected-field screenshot,
  generated source, build, flash, or hardware action exists.
- Built-in ST board definitions remain non-substitutes for the project driver
  board.
- Packet A/B/C, PB3/SWO, `J_HALL`, generated-project trust, continuity,
  powered readiness, motor readiness, Hall readiness, Motor Profiler readiness,
  and sensorless readiness remain unchanged.

# 2026-05-19 Gerber PCB2 Manufacturing Package Intake

New Gerber package:
`hardware/schematic/2026-05-19_gerber_pcb2_stdrive101/Gerber_PCB2_2026-05-19.zip`.

New Packet B/C no-power review:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-19_003_gerber_pcb2.md`.

Decision: `Partial clue / accepted board-side Gerber + flying-probe net clue`.

The ZIP is a same-day Gerber manufacturing package supplied after the
self-developed STDRIVE101 driver-board `.epro` source. It contains top/bottom
copper, two inner copper layers, solder mask, paste mask, silkscreen, board
outline, drill files, and `FlyingProbeTesting.json`. Gerber headers record
`EasyEDA Pro v3.2.91`, generated `2026-05-19 11:16:57`. The archived ZIP hash
is SHA256 `F61C073C5A9E71CD608460976430D3F927E7AD48EC05A42661E77662AF04CE56`.

Accepted exact board-side clues:

- `CN3` flying-probe pad/net table:
  `1 HIN1`, `2 LIN1`, `3 HIN2`, `4 LIN2`, `5 HIN3`, `6 LIN3`,
  `7 ADC_U`, `8 ADC_V`, `9 ADC_W`, `10 IA`, `11 IB`, `12 IC`,
  `13 NFAULT`, `14 3V3`, `15 GND_SIGNAL`.
- `U1=STDRIVE101` pad nets include `$2N118` for the `CP` pin position,
  `GND_POWER` for the `DT/MODE` pin position, plus `SCREF`, `24V_FUSED`,
  `REG12`, `NFAULT`, `INx`, `ENx`, `BOOTx`, `GHSx`, `GLSx`, and `OUTx`.
- PWM input paths are visible at pad-net level:
  `R4 HIN1-IN1`, `R8 LIN1-EN1`, `R5 HIN2-IN2`, `R6 LIN2-EN2`,
  `R7 HIN3-IN3`, `R9 LIN3-EN3`.
- Protection/current-sense pad-net clues are visible:
  `R3 NFAULT-3V3`, `R1 SCREF-3V3`, `R2 GND_SIGNAL-SCREF`,
  `C4/C5 REG12-GND_SIGNAL`, `D1/D2/D3 REG12-to-BOOTx`,
  and `R12/R14/R17 ADC_U/V/W-GND_POWER`.
- Connector clues are visible:
  `U2=J_HALL` has `+5V`, `GND_SIGNAL`, and three signal paths through
  `R22/R23/R24` to `IA/IB/IC`; `CN2=J_MOTOR` has `OUT1/OUT2/OUT3`.

Blocked exact fields:

- No NUCLEO `CN8` endpoint, STM32 pin mapping, or harness/adapter mapping is
  present in this package.
- Exact fabrication/revision match still needs user or hardware teammate
  confirmation before it can be treated as final build evidence.
- `CP` is present only as unnamed net `$2N118`; `STBY` was not observed.
- `J_HALL` physical pin-1 orientation and Hall A/B/C numbering are not
  accepted.
- PB3/SWO release, Packet A/Workbench selected fields, generated-project
  trust, continuity checks, power-stage readiness, Motor Profiler readiness,
  motor readiness, and sensorless readiness remain unchanged.

# 2026-05-19 ProDoc P1 EDA Pro Source Intake

New self-developed STDRIVE101 driver-board source:
`hardware/schematic/2026-05-19_prodoc_p1_stdrive101_epro/ProDoc_P1_2026-05-19.epro`.

New Packet B/C no-power review:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-19_002_prodoc_p1_epro.md`.

Decision: `Partial clue / accepted schematic-source clue`.

The `.epro` is a readable EDA Pro schematic source for the user-confirmed
self-developed STDRIVE101 driver board. Parsed metadata shows
`STDRIVE101_3Phase_Inverter`, board `Schematic1`, sheet `P1`, create/update
date `2026-05-19`, and create/update time `10:26:36`. The archived file hash
is SHA256 `B9D67B9E5D6DD08D5229928636DFA8048C081DED7EE230ADDB79F20D83D718A1`.

Accepted exact schematic clues:

- `U1=STDRIVE101`.
- `Q1-Q6=NCEP40T11G`.
- `R12/R14/R17=20mOhm` shunt resistors.
- `CN3=2.54mm-15P ZZ` board-side control connector.
- `U2=J_HALL`, `CN2=J_MOTOR`.
- `CN3` board-side pinout:
  `1 HIN1`, `2 LIN1`, `3 HIN2`, `4 LIN2`, `5 HIN3`, `6 LIN3`,
  `7 ADC_U`, `8 ADC_V`, `9 ADC_W`, `10 IA`, `11 IB`, `12 IC`,
  `13 NFAULT`, `14 3V3`, `15 GND_SIGNAL`.
- `J_HALL` schematic clue: `+5V`, `GND_SIGNAL`, and three signal paths
  through `R22/R23/R24=100 ohm` into `IA/IB/IC`.
- STDRIVE101 schematic clues: `NFAULT`, `REG12`, `SCREF`, `BOOTx`, `OUTx`,
  `GHSx`, and `GLSx` are visible. `DT/MODE` appears tied to `GND_POWER` at
  the STDRIVE101 pin, but this remains a clue pending dedicated review.

Blocked exact fields:

- The archive contains no PCB layout data: `project.json` has `pcbs: {}`, the
  board entry has an empty `pcb` field, and `PCB/` is only an empty directory
  entry.
- No NUCLEO `CN8` endpoint or STM32 pin mapping is proven.
- `CP` has no explicit parsed net label, `STBY` was not observed, and the
  protection thresholds/fault-release path still need review.
- PB3/SWO release, `J_HALL` numbering, Hall readiness, power-stage readiness,
  Packet A/Workbench selected fields, generated-project trust, Motor Profiler
  readiness, motor readiness, and sensorless readiness remain unchanged.

# 2026-05-19 Packet A Workbench Capture Attempt

New Packet A no-power capture-attempt review:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-19_001_packet_a_workbench_capture_attempt.md`.

New Workbench screenshots:

- `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/screenshots/2026-05-19_workbench_launch_fullscreen.png`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/screenshots/2026-05-19_workbench_after_new_project.png`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/screenshots/2026-05-19_workbench_motor_control_kit_selected.png`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/screenshots/2026-05-19_workbench_board_path_probe.png`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/screenshots/2026-05-19_workbench_power_slot_search_stdrive101_exact.png`

Decision: `Partial clue / stopped`.

Accepted exact clue: Workbench 6.4.2 Desktop launches, and the component path
can show `NUCLEO-G474RE` / `STM32G474RETx` as the control-board context.

Blocked exact fields: no project-specific `.stwb6`, no accepted Custom /
Generic self-made STDRIVE101 power-stage context, and no selected-field
screenshots for PWM, current sensing, Hall/sensorless, driver protection, or
pin usage. User clarified on 2026-05-19 that the project uses a self-developed
motor driver board based on the STDRIVE101 chip, so built-in ST board entries
such as `EVALSTDRIVE101` or `STEVAL-LVLP01` cannot be used as board-match
substitutes.

Packet A remains `Partial clue / Preparation only`. Generated-project trust
remains `Not allowed`. Packet B/C, CN8 routing, STDRIVE101 protection-path
proof, PB3/SWO release, `J_HALL`, Hall readiness, power-stage readiness, Motor
Profiler readiness, motor readiness, and sensorless readiness remain unchanged.

# 2026-05-18 PB3 / SWO CubeMX Probe

New PB3/SWO no-power review:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-18_002_pb3_swo_probe.md`.

New evidence files:

- `apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/2026-05-18_cubemx_pb3_current_swo_fullscreen.png`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_no_power_nucleo_g474re_draft/pb3_tim2_ch2_probe_2026-05-18.ioc`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/2026-05-18_cubemx_pb3_tim2_ch2_probe_fullscreen.png`

Decision: `Partial clue`.

The existing NUCLEO-G474RE no-power draft still records
`PB3.GPIO_Label=T_SWO` and `PB3.Signal=SYS_JTDO-SWO`; the new CubeMX screenshot
preserves that current state. A separate dated probe `.ioc` changes only the
copy to `PB3.GPIO_Label=HALL_B_PROBE` and `PB3.Signal=TIM2_CH2`, and CubeMX can
open that probe. This is a configuration-layer clue only. It does not prove
NUCLEO SWO release / isolation, Workbench Hall B selection, CN8 / `J_HALL`
endpoint mapping, Hall readiness, or any powered behavior.

`PB3` remains blocked for Hall B until separate SWO release / isolation evidence
and board-route endpoint evidence arrive. Packet A/B/C, generated-project
trust, CN8 routing, STDRIVE101 protection-path proof, Hall closed-loop,
power-stage readiness, Motor Profiler readiness, motor readiness, and sensorless
readiness are unchanged.

# 2026-05-17 Vendor Motor And G431 Pin Table Update

New motor source:
`hardware/motor/2026-05-17_vendor_57blf01_motor_parameters.md`.

New hardware teammate pin-table source:
`hardware/schematic/2026-05-17_stm32g431rb_pin_assignment_hw_teammate.md`.

New MCU pin compatibility check:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/mcu_pin_compatibility_check_2026-05-17.md`.

Review record:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-17_001_vendor_motor_g431_pin_table.md`.

Decision: `Partial clue`.

The supplier motor table supports a better no-power Workbench label,
`57BLF01_VENDOR_CANDIDATE`, but it does not provide project-measured motor
parameters or Motor Profiler data. The hardware teammate pin table is titled
for `STM32G431RB`; the teammate states the relevant G431/G474 pins are the
same, and local MCSDK `STM32G431RBTx` / `STM32G474RETx` asset comparison
supports the compared key rows. This still does not accept CN8 routing,
`J_HALL` connector numbering, `PB3` / SWO release, or OPAMP/VCP policy.

Generated-project trust remains `Not allowed`.

# 2026-05-16 Packet A Custom Capture Package Update

The old `My_First_FOC.stwb6` file is now explicitly treated as a legacy
toolchain-learning leftover, not the intended project-specific Packet A source.
Its arbitrary `EVALSTDRIVE101` power-board choice remains a reason it cannot be
accepted for the custom board.

New package:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/`.

New preparation review:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-16_001_custom_nucleo_stdrive101_capture_package.md`.

Decision: `Partial clue / Preparation only`.

The package defines the next no-power Workbench capture path for
`NUCLEO-G474RE` / `STM32G474RETx`, a Custom / Generic STDRIVE101 power stage,
FOC, Hall fallback, 3-shunt current sensing, `57BLF01_VENDOR_CANDIDATE`
supplier-clue motor label, a
no-power motor measurement log, and a pin assignment table. It still does not
contain a real new `.stwb6` or selected-field Workbench screenshot.

Generated-project trust remains `Not allowed`.

# 2026-05-15 Packet A STWB6 Candidate Update

Codex found the real ST MC Workbench 6.4.2 launcher at
`F:\STMCSDK\MC_SDK_6.4.2\Utilities\PC_Software\STMCWB\STMCWB.exe` and preserved
`F:\STMCSDK\My_First_FOC.stwb6` under
`apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-15_my_first_foc/My_First_FOC.stwb6`.

Review record:
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-15_002_my_first_foc_stwb6.md`.

Decision: `Partial clue`.

Accepted from the file: MCSDK 6 `.stwb6` project format, Workbench version
`6.4.2`, algorithm `FOC`, control board `NUCLEO-G474RE`, and MCU
`STM32G474RETx`.

Still not accepted: final custom-board context, selected TIM1 complementary PWM
topology, final `NFAULT` / `PB12/TIM1_BKIN` selection, custom-board current
sensing, Hall/sensorless final selection, `PA2/PA3` policy, `PB3` ownership,
and generated-project trust.

Current decision: Packet A has a source candidate, but generated-project trust
remains `Not allowed`.

# P2 证据包 - 2026-05-14

这个文件记录当前仓库里“真的有证据”的内容。它的作用不是教你接线，
也不是生成固件，而是帮你判断：哪些东西现在可以相信，哪些还只是草案，
哪些会卡住后续 MCSDK 工程。

## 安全边界

这个证据包不授权任何上电或电机动作：

- 不接 24V；
- 不接功率板；
- 不接电机；
- 不输出 Gate PWM；
- 不运行 Motor Profiler；
- 不声称 Hall 闭环已经验证；
- 不声称 SMO / 无感控制已经验证。

## 当前仓库里有什么

| 检查项 | 当前结果 | 这说明什么 |
| --- | --- | --- |
| `.stmcx` 文件 | `rg --files -g "*.stmcx"` 在 GUI 尝试前后都没有找到任何文件。 | 还没有 Motor Control Workbench 工程文件。 |
| CubeMX `.ioc` 草案 | `apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_no_power_nucleo_g474re_draft/mcsdk_no_power_nucleo_g474re_draft.ioc`。 | 证明 NUCLEO-G474RE 板卡入口、`PB12/TIM1_BKIN`、`PB14/TIM1_CH2N`、`PA2/PA3` VCP、`PB3` SWO 已保存到 CubeMX 配置层；仍不是 `.stmcx` 或 MCSDK MotorControl 工程。 |
| GUI 截图 | `apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/2026-05-14_cubemx_home.png`，`screenshots/2026-05-14_cubemx_ioc_launch_attempt.png`、`screenshots/2026-05-14_cubemx_ioc_pinout_active_window.png`，以及 2026-05-18 `screenshots/2026-05-18_cubemx_pb3_current_swo_fullscreen.png` 和 `screenshots/2026-05-18_cubemx_pb3_tim2_ch2_probe_fullscreen.png`。 | 首页截图证明 CubeMX 打开；2026-05-14 截图证明保存的 NUCLEO `.ioc` 可在 CubeMX `Pinout & Configuration` 页面打开；2026-05-18 截图证明当前草案仍显示 `PB3` 为 SWO，另一个 probe 副本可显示 `PB3` 为 `HALL_B_PROBE`。它们仍不证明 MotorControl/Workbench 配置、SWO 物理释放或 Hall endpoint。 |
| PB3/SWO probe | `apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_no_power_nucleo_g474re_draft/pb3_tim2_ch2_probe_2026-05-18.ioc`。 | 这是从原 `.ioc` 复制出的配置层 probe，只把 `PB3` 改为 `TIM2_CH2` / `HALL_B_PROBE` 并由 CubeMX 打开截图；它不替代原草案，也不证明 NUCLEO SWO 释放、CN8 / `J_HALL` endpoint 或 Hall readiness。 |
| GUI 捕获结果 | `apps/stm32_g474_foc/mcsdk_no_power_precheck/gui_capture_result_2026-05-14.md`。 | 记录本轮 GUI fallback 证据、`.ioc` 读回、截图路径和 `.stmcx` / MotorControl 仍阻塞。 |
| Workbench 入口探测 | `apps/stm32_g474_foc/mcsdk_no_power_precheck/workbench_entry_probe_2026-05-14.md`。 | 记录 repo、CubeMX 安装目录、MCSDK package、VS Code STM32 extension、`.stm32cubemx` 和常见 ST 安装目录的目标探测；确认 MotorControl package 数据存在，但仍没有 `.stmcx` 或独立 Workbench launcher 证据。 |
| 板级走线证据 | 仓库里有 `hardware/schematic/2026-05-09_power_board_schematic_screenshot.jpg`、对应说明，以及 2026-05-15 新导入的 `hardware/schematic/2026-05-15_power_board_cn8_stdrive101_schematic_candidate.png` / `.md`。 | 2026-05-15 截图可读性更好，用户已确认它对应当前物理功率板且由硬件同学自绘，能作为 Packet B/C 候选和 `Partial clue`；但缺正式 source revision/date、STM32 端点映射、`DT/MODE` 端点证明和 `STBY` 证明，所以仍不是 accepted CN8 / EDA / netlist 走线证明。 |
| STDRIVE101 资料 | 本地已有 STDRIVE101 PDF、提取文本和 digest。 | 可以用来做保护路径审查，但还不能证明你的功率板实际怎么连。 |
| STDRIVE101 保护路径审查 | `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_protection_path_review_2026-05-14.md`。 | 已把 `DT/MODE`、`nFAULT`、`REG12`、`CP`、`SCREF`、`VS/VM`、bootstrap、standby 和 VDS monitoring 固化成缺证矩阵；这仍只是审查规则，不是板级通过证据。 |

## 证据等级

| 等级 | 需要什么证据 | 当前状态 | 当前决定 |
| --- | --- | --- | --- |
| A | Workbench/CubeMX 的 `.stwb6` / `.stmcx`、配置截图或可读 `.ioc`，能看到 `STM32G474RETx`、current PCB2 PWM/Hall route、`PB12/TIM1_BKIN`、`PA2/PA3` policy、`PB3` ownership。 | 部分具备：已有 NUCLEO-G474RE `.ioc` 草案和 CubeMX `Pinout & Configuration` 截图，仍没有 accepted `.stwb6` / `.stmcx` 或 MCSDK/Workbench MotorControl selected-field 截图。 | 可相信 CubeMX 引脚配置草案已保存并可由 GUI 打开；不能信任“MCSDK MotorControl 配置已经完成”，也不能信任 current PCB2 PWM/Hall route 已被 Packet A 接受。 |
| B | NUCLEO 连接器和焊桥证据，说明 VCP/SWO 到底占不占对应引脚。 | `.ioc` 已保存 `PA2/PA3` 为 VCP、`PB3` 为 SWO；2026-05-19 当前 PCB2 映射说明 `PB3` 是 `LIN1`，不是当前 PCB2 Hall B。 | `PB3` 不能作为当前 PCB2 Hall；作为 `LIN1` 仍需要 Packet A timer/pin-function proof。任何 alternate Hall use 仍需 SWO 释放/隔离证据。 |
| C | CN8 / EDA / netlist 走线证据，证明 `NFAULT`、PWM 输入、电流采样、Hall、`3V3`、`GND_SIGNAL` 实际连到哪里。 | 缺失。现在只有原理图截图，没有 EDA、PDF、PCB、Gerber 或 netlist。 | 不能信任 STM32 引脚真的连到了目标 STDRIVE101 网络。 |
| D | 无功率连续性 / 短路检查记录。 | 缺失。 | P2 书面审查阶段不做这一步；后续硬件阶段前必须补。 |
| E | 限流上电日志、波形和测量记录。 | 缺失，而且 P2 禁止做。 | 不能有功率、电机、PWM Gate、Profiler、Hall、SMO 结论。 |

## 关键点逐项结论

| 项目 | 当前草案怎么选 | 现在有什么证据 | 信任前还缺什么 |
| --- | --- | --- | --- |
| `PB12/TIM1_BKIN` 作为 `nFAULT` | 当前首选候选。 | pin/config review 和 config draft 已记录这个选择；`mcsdk_no_power_nucleo_g474re_draft.ioc` 已保存 `PB12.Signal=TIM1_BKIN`。 | CN8/EDA/netlist 必须证明 STDRIVE101 `nFAULT` 真的到这个 STM32 输入；还要确认上拉电压和低有效含义。 |
| `PC5` 作为 `nFAULT` | 当前草案拒绝。 | `config_draft.md` 和 `pin_config_review_2026-05-14.md` 已记录拒绝理由。 | 只有写清楚 OPAMP/VCP/定时器 break/走线冲突怎么解决，才允许重新打开。 |
| Current PCB2 PWM / driver-input route | `HIN1/LIN1/HIN2/LIN2/HIN3/LIN3 -> PA15/PB3/PB10/PA8/PA9/PA10` is now the route under review. | `source_packet_review_2026-05-19_004_pcb2_mapping_pin1_protection.md`, `current_pcb2_hall_pwm_strategy_2026-05-19.md`, and `current_pcb2_packet_a_firmware_feasibility_2026-05-19.md` record it as a source clue and feasibility topic. | Accepted Packet A / Workbench selected fields must still prove how this route can be represented; no Gate PWM output in P2. |
| Historical standard TIM1 complementary PWM draft | `PA8/PB13`, `PA9/PB14`, `PA10/PB15`. | `config_draft.md` now marks this as historical candidate only. | It cannot be treated as current PCB2 route unless a future hardware-rework packet changes the board. |
| `PA2/PA3` 作为 FOC 通信口 | 默认排除。 | `.ioc` 已保存 `PA2.Signal=LPUART1_TX`、`PA3.Signal=LPUART1_RX`，证明这是 NUCLEO VCP 路径。 | 如果以后要复用，必须由 CubeMX/Workbench 证明不会和 OPAMP/PGA 冲突。 |
| Current PCB2 Hall route | `J_HALL -> IA/IB/IC -> PA0/PA1/PB4`. | 2026-05-19 mapping packet, strategy review, Packet A / firmware feasibility review, and software Hall adapter design review record this as current board source clue. | It is not accepted as a same-timer hardware Hall set; software Hall remains no-power design review only and cannot upgrade Hall readiness. |
| Alternate `PB3` Hall B route | Only a future alternate route after SWO release/isolation. | Original `.ioc` and 2026-05-18 screenshot still show `PB3` as SWO; probe copy can show `PB3` as `TIM2_CH2` / `HALL_B_PROBE`; 2026-05-19 clarification says current PCB2 uses `PB3` as `LIN1`. | Any alternate Hall use still needs NUCLEO SWO release/isolation evidence, Packet A assignment, and accepted board-route endpoint. |
| `DT/MODE` 与 PWM 模式 | 仍是硬件审查依赖项。 | STDRIVE101 digest 已解释为什么它重要。 | 需要 EDA/netlist 证明 `DT/MODE` 是电阻设置还是接地，并让 MCSDK/TIM1 输出模式匹配它。 |
| STDRIVE101 保护路径 | 仍是硬件审查依赖项。 | 本地 STDRIVE101 PDF、文本和 digest 都在。 | 还要证明板子上的 `nFAULT`、`REG12`、`CP`、`SCREF`、`VS/VM`、bootstrap、电源唤醒、VDS 监测网络。 |
| STDRIVE101 保护路径审查文件 | 已建立缺证矩阵。 | `stdrive101_protection_path_review_2026-05-14.md` 按同一格式记录官方要求、截图线索、可信等级、缺失证据和 P2 决策。 | 还要用当前版 EDA/PDF/netlist/高清图把每一项从 blocked 升级为 proven。 |

## 生成 MCSDK 前的硬阻塞

1. 没有 `.stmcx`，也没有 Workbench/CubeMX MotorControl 配置页截图；当前只有 NUCLEO-G474RE CubeMX `.ioc` 草案、CubeMX `Pinout & Configuration` GUI fallback 截图，以及 MotorControl package 数据存在的探测记录。
2. 当前 PCB2 `HIN/LIN` route 和 `PA0/PA1/PB4` software Hall strategy 还没有 Packet A / firmware feasibility review；不能把 source clue 当作 accepted Workbench selected fields。
3. 没有 CN8 / EDA / netlist 走线证明。
4. 没有板级 `DT/MODE`、`nFAULT`、`REG12`、`CP`、`SCREF`、`VS/VM`、bootstrap、standby 和 VDS monitoring 源证据；当前只有保护路径审查缺证矩阵。
5. 没有证据证明 alternate `PB3` Hall B use 之前，SWO 已经释放或隔离；2026-05-18 probe 只证明配置层可显示 `TIM2_CH2` / `HALL_B_PROBE`，不清除该阻塞。
6. 没有连续性 / 短路检查记录；而上电证据在 P2 阶段仍然禁止。

## 下一步证据入口

新增入口规则：
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_intake_checklist_2026-05-14.md`。

这个清单只规定什么来源可以进入证据审查，不升级任何当前缺证项。

用户动作队列：
`apps/stm32_g474_foc/mcsdk_no_power_precheck/user_action_queue_2026-05-14.md`。

这个队列现在把下一步交付顺序固定为：先做 Packet A / firmware strategy
review，评估 current PCB2 `HIN/LIN` route 和 `PA0/PA1/PB4` software Hall
feasibility；再继续补 Packet B/C source proof；如果未来走 alternate
`PB3` Hall B，再补 SWO 释放或隔离证据。它仍不升级任何当前缺证项。

审查模板：
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_template_2026-05-14.md`。

这个模板规定收到源包后先做 Accept / Partial clue / Reject 判断，再决定
是否更新本证据包。未被模板接受的字段继续保持 `Blocked`。

| 缺证项 | 需要走的入口 | 当前状态 |
| --- | --- | --- |
| `.stwb6` / `.stmcx` / MotorControl 配置截图 | MCSDK / MotorControl Configuration Packet | Partial clue. `My_First_FOC.stwb6` is preserved and reviewed, but final selected fields and custom-board context remain unaccepted. |
| Current PCB2 `HIN/LIN` route plus `PA0/PA1/PB4` software Hall feasibility | Packet A / firmware strategy review and software Hall adapter design review | No-power design review only. `current_pcb2_packet_a_firmware_feasibility_2026-05-19.md` and `software_hall_adapter_design_review_2026-05-19.md` define the boundary, but do not accept selected fields, generated-project trust, build-only clearance, or Hall readiness. |
| CN8 / EDA / netlist 走线证明 | CN8 / Board Route Packet | Blocked. 仍没有 current-version EDA、schematic PDF、netlist 或高清走线图。 |
| STDRIVE101 `DT/MODE`、`nFAULT`、`REG12`、`CP`、`SCREF`、`VS/VM`、bootstrap、standby 和 VDS monitoring | STDRIVE101 Protection Path Packet | Blocked. 仍只有官方器件要求和缺证矩阵，没有板级通过证据。 |
| `PB3` Hall B 前的 SWO 释放或隔离 | CN8 / Board Route Packet plus NUCLEO bridge/source evidence | `Partial clue / still Blocked`. 原 `.ioc` 仍显示 `PB3.Signal=SYS_JTDO-SWO`；2026-05-18 probe 副本可显示 `PB3.Signal=TIM2_CH2`，但缺 SWO release/isolation 和 Hall endpoint 证明。 |

2026-05-15 新增源包审查：
`apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-15_001_cn8_stdrive101_schematic_candidate.md`。

当前判定为 `Partial clue`。用户已确认该截图对应当前物理功率板，来源/版本
口径为硬件同学自绘。该截图可见 CN8、STDRIVE101、输入电阻、
`nFAULT` 上拉/LED、`REG12`、`CP`、`SCREF`、bootstrap、MOSFET、采样电阻和
Hall 接口线索；但仍没有正式 source revision/date、STM32 端点映射、
accepted `DT/MODE` 端点证明或 `STBY` 证明。因此本证据包不升级 CN8
routing proof 或 STDRIVE101 protection-path proof。

Rejected source types stay rejected: low-resolution screenshots, oral
descriptions, old or unknown-version files, incomplete crops, generated source
without matching configuration evidence, and the excluded WeChat-side
`netlist_PADS.net` candidate.

## 2026-05-14 Parallel Evidence Push

| Evidence chain | Follow-up result | Current trust level |
| --- | --- | --- |
| `.stmcx` / MotorControl | Repo search still found no `.stmcx`. Narrow checks of `F:\STMCubeMX`, `MCSDK_v6.4.2-Full`, and VS Code extension folders did not identify a saved Workbench project, standalone Workbench launcher, or MotorControl configuration page. | Blocked. MotorControl package presence is not project configuration evidence. |
| CN8 / STDRIVE101 route | `cn8_stdrive101_route_review_2026-05-14.md` now defines the accepted source packet. Current repo evidence is still only screenshot-level clue plus STDRIVE101 datasheet review requirements. | Blocked. No accepted current EDA, schematic PDF, netlist, or high-resolution route crop is in the repo. |
| Excluded source | The WeChat-side `netlist_PADS.net` candidate is intentionally not imported and not used as current board evidence. | Not evidence. |

## 2026-05-14 STDRIVE101 Protection Path Review

| Evidence chain | Follow-up result | Current trust level |
| --- | --- | --- |
| ST official source | ST official product page and datasheet were rechecked. They confirm two input strategies selected by `DT/MODE`, `REG12` gate-driver supply, overcurrent comparator, VDS monitoring, UVLO, thermal shutdown, and standby behavior. | High for official device requirements. |
| Board screenshot clue | Existing screenshot notes mention possible `R3`/`nFAULT`, `C4`/`C5` for `REG12`, `C1` for `CP`, `R1`/`R2` for `SCREF`, and bootstrap components, but resolution/source type is not accepted board proof. | Low-grade clue only. |
| Protection-path review | `stdrive101_protection_path_review_2026-05-14.md` now records a missing-evidence matrix for `DT/MODE`, `nFAULT`, `REG12`, `CP`, `SCREF`, `VS/VM`, bootstrap, `STBY`, and VDS monitoring. | High for review structure and blockers; blocked for board-level proof. |

Current decision: P2 can continue written review and GUI/config capture work,
but it still cannot claim saved MCSDK MotorControl configuration, CN8 routing
proof, STDRIVE101 protection-path proof, power-stage readiness, Hall readiness,
or sensorless readiness.

## 2026-05-15 Packet A Local Probe

New Packet A records:

- `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_local_probe_2026-05-15.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_capture_checklist_2026-05-15.md`

The local probe checked the repo, existing screenshots, the
`apps/stm32_g474_foc/MotorControl` placeholder, `F:\STMCubeMX`,
`C:\Users\gregrg\STM32Cube\Repository`, `C:\Users\gregrg\.stm32cubemx`, and
common user locations (`Documents`, `Downloads`, `Desktop`). It still found no
real `.stmcx` and no MotorControl / Workbench configuration screenshot. Direct
search of `C:\Users\gregrg` returned access denied, so this is a bounded local
probe, not proof that every private user directory was searched.

Packet A was later upgraded to `Partial clue` by
`source_packet_review_2026-05-15_002_my_first_foc_stwb6.md`. The new checklist
defines the next accepted capture: Workbench screenshots or an accepted final
`.stwb6` / legacy `.stmcx` proving the selected fields.
It does not upgrade MCSDK MotorControl configuration, generated-project trust,
Gate PWM, Motor Profiler, Hall, motor, power-stage, CN8 routing, STDRIVE101
protection-path, or sensorless evidence.

## 2026-05-15 STM32 Signal Contract And Build-Only Gate

New non-hardware track artifacts:

- `apps/stm32_g474_foc/mcsdk_no_power_precheck/stm32_side_signal_contract_2026-05-15.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/future_build_only_gate_2026-05-15.md`

The STM32-side signal contract records future responsibilities for TIM1 PWM
commands, `NFAULT`, `STBY`, `DT/MODE`, current sensing, Hall fallback,
`PA2/PA3`, `PB3`, `3V3`, `GND_SIGNAL`, and the ESP32 gateway boundary. Every
hardware-dependent field remains `Blocked`, `Candidate`, or `Partial clue`
unless Packet A/B/C or PB3/SWO evidence proves it.

The future build-only gate records that generated-project trust is currently
`Not allowed` because Packet A is only `Partial clue`. If Packet A selected
fields are later accepted, a generated MCSDK project can be treated only as no-power build evidence. Build
success will not upgrade CN8 routing, STDRIVE101 protection-path proof, Gate
PWM behavior, Motor Profiler readiness, Hall readiness, motor readiness, or
sensorless readiness.

## 2026-05-15 P2 Readiness Snapshot

New readiness control artifact:

- `apps/stm32_g474_foc/mcsdk_no_power_precheck/p2_readiness_snapshot_2026-05-15.md`

The snapshot consolidates Packet A/B/C, PB3/SWO, STM32-side signal-contract,
and future build-only gate status into one current gate decision. Current
decision remains: P2 is in progress, Packet A is `Partial clue`, generated-project
trust is `Not allowed`, Packet B/C and PB3/SWO remain blocked or partial clue
only, and P3 powered or motor work is not allowed.

This snapshot does not upgrade MCSDK MotorControl configuration, generated
project trust, CN8 routing proof, STDRIVE101 protection-path proof, Gate PWM,
Motor Profiler, Hall, motor, power-stage, or sensorless evidence.

## 当前 P2 判断

P2 可以继续做书面审查、GUI / 配置证据收集和非硬件并行准备。2026-05-15
新增 `non_hardware_parallel_track_2026-05-15.md`，把“暂时跳过硬件源包支线”
记录为 scheduling decision, not clearance。当前仓库还不能信任生成的 MCSDK
电机控制配置，也不能进入功率板、电机、PWM Gate、Motor Profiler、Hall 闭环
或无感控制阶段。
