# MCSDK No-Power Precheck

This directory is the P2 no-power MCSDK practice area.

It is not the firmware working tree for manual edits. It holds no-power
planning, source-review, and build-only evidence that must be checked before
any Motor Profiler step, power-board connection, motor connection, or PWM Gate
output.

## Current Status

- Created: 2026-05-14.
- Scope: configuration planning only.
- Latest PCB2 DMM evidence:
  `pcb2_no_power_dmm_continuity_short_check_result_2026-06-19.md` records
  the user-reported no-power DMM summary: continuity rows for
  `CN3_10-PA0`, `CN3_11-PA1`, `CN3_12-PB4`, `CN3_2-PB3`,
  `CN3_14-3V3`, `CN3_15-GND`, and `CN3_13-PB12` are reported as `通`,
  while rail, signal-to-rail, and Hall-pair short checks are reported as
  `不通`. Raw ohm values were not provided. This opens only no-power
  software Hall adapter interface / code-entry boundary planning.
- Latest post-DMM software Hall boundary:
  `software_hall_code_entry_boundary_after_dmm_2026-06-19.md` defines the
  next no-power document-side work for a future `PA0 / PA1 / PB4`
  debug-only adapter: exact file list, GPIO pull / EXTI policy review,
  timestamp-source criteria, debug snapshot route, no-power build checklist,
  and rollback checklist. It does not create firmware or authorize MCSDK
  hooks.
- Existing evidence in this directory: draft configuration, tool probe notes,
  a CubeMX Home screenshot, a CubeMX `.ioc` pinout screenshot, pin/config safety
  review, GUI capture result, a current P2 璇佹嵁鍖? source packet intake rules,
  a source packet request pack, a source packet review template, and a user
  action queue, STM32-side signal/build gates, a P2 readiness snapshot, a
  2026-05-16 custom Workbench capture package, 2026-05-17 vendor motor /
  hardware teammate pin-table source clues, a 2026-05-18 Packet A capture
  task package, a 2026-05-19 Workbench capture attempt stopped on the
  self-made STDRIVE101 power-stage context blocker, 2026-05-19 `.epro` and
  Gerber PCB2 board-side source clues, a 2026-05-19 hardware supplement
  handoff, a minimal hardware-teammate request, and a local Workbench
  Board Designer / Board Manager asset probe, plus a 2026-05-19 current PCB2
  mapping / pin-1 / protection source review, a current PCB2 Hall/PWM
  no-power strategy review, a current PCB2 Packet A / firmware feasibility
  review, a software Hall adapter design review, and a Packet A Board
  Designer / Board Manager path review, plus a Packet A Board Designer /
  Manager GUI-only checklist, a `MY_FOC` generated-project source review, a
  `MY_FOC` manual FOC edit rollback record, and a 2026-05-20 Packet C
  STDRIVE101 protection detail review, plus a 2026-05-22 DMM continuity /
  short-check request before software Hall adapter implementation, and a
  2026-05-22 software Hall no-power algorithm prep artifact, plus a
  2026-05-22 software Hall state-machine exercise card, plus a 2026-05-27
  software Hall adapter pseudocode draft, plus a 2026-05-27 software Hall
  adapter processing-order teaching card, plus a 2026-05-27 host-side software
  Hall reference model review, plus 2026-05-27 software Hall golden vectors
  and replay test, plus a 2026-05-27 read-only MCSDK integration probe for
  the software Hall route, plus a 2026-05-27 firmware-entry checklist that
  freezes the missing conditions before any future adapter code, plus a
  2026-05-27 GPIO/EXTI boundary review draft for `PA0/PA1/PB4`, plus a
  2026-05-27 timestamp-source review draft that excludes `TIM1`, keeps current
  `TIM2` as a generated MCSDK Hall clue only, limits `HAL_GetTick()` to coarse
  logs, and leaves an isolated free-running timer as a future review target,
  plus a 2026-05-27 no-power Debug build-only result record for
  `QIANSAI_G474_STDRIVE101_FOC_P2`, plus a 2026-05-27 low-frequency
  debug-output route review draft that defines
  snapshot fields and blocks ISR printing / UART transmit / JSON / ESP32 /
  SWO / every-edge streaming, plus a 2026-05-27 MCSDK firmware-integration boundary review draft that blocks direct writes to `HALL_M1`, speed loop, PID, JEOC / FOC ISR, or TIM1 PWM, plus a 2026-05-28 Chinese-first software Hall firmware-entry plan that defines the future debug-only adapter layers, state-machine order, ISR limits, debug fields, and MCSDK hard stops without opening firmware implementation.
- Current user handoff: 2026-06-01 PCB2 was reported populated / in hand and
  the route is unchanged. The 2026-06-19 no-power DMM summary is now recorded
  as `pcb2_no_power_dmm_continuity_short_check_result_2026-06-19.md`.
- Latest STDRIVE101 fault-isolation evidence:
  `stdrive101_pa7_lin1_wake_nfault_1v3_fault_isolation_result_2026-06-21.md`
  records the PA7 hold-high diagnostic after the open-loop / CN3 no-waveform
  correction. The user reported `PA7 / CN10-15 = 3.3 V`,
  `CN8 P2 / LIN1 = 3.3 V`, `VS / 24V_FUSED = 24 V`, and `REG12 = 12 V`, but
  `nFAULT = 1.3 V` on both `CN8 P13` and `NUCLEO CN10-16`; after disconnecting
  the `nFAULT -> PB12` wire, power-board `CN8 P13` remained `1.3 V`. Corrected
  R3 checks show `R3 = 10 kohm` and endpoint continuity to `3V3` and `nFAULT`,
  so the R3 pull-up value and NUCLEO PB12 are not the primary blockers. Current
  working hypothesis is a power-board-side STDRIVE101 fault state, with the
  `LIN1 / GLS1 / Q2 / OUT1` low-side phase-U VDS or related output path as the
  primary review target. Do not repeat a motor-connected open-loop run from
  this state.
- Latest host-side FOC algorithm evidence:
  `host_side_no_power_foc_algorithm_model_review_2026-06-22.md` records
  `src/foc_core_model.py` and `tests/test_foc_core_model.py` as a host-side
  no-power FOC math reference. Current decision is `Host-side no-power FOC
  algorithm model / no firmware implementation / no MCSDK integration / no PWM
  output / no motor readiness`. MCSDK remains the intended framework
  generation path. This proves only host-side algorithm behavior and is not
  firmware, not MCSDK hook evidence, not Gate PWM validation, not Hall
  closed-loop, not sensorless validation, not power-stage readiness, and not
  motor readiness.
- Latest host-side FOC golden-vector evidence:
  `host_side_no_power_foc_golden_vectors_review_2026-06-22.md` records
  `tests/fixtures/foc_core_golden_vectors.json` and
  `tests/test_foc_core_vectors.py` as host-side no-power FOC math regression
  fixtures. Current decision is `Host-side no-power FOC golden vectors / no
  firmware implementation / no MCSDK integration / no PWM output / no motor
  readiness`. These vectors are not MCSDK convention proof, not compare
  register evidence, not Gate PWM validation, not power-stage readiness, and
  not motor readiness.
- Latest STDRIVE101 wake-related evidence:
  `stdrive101_gate_waveform_candidate_24v_static_scope_no_waveform_result_2026-06-21.md`
  records the user-reported oscilloscope check on the six STDRIVE101
  MCU-facing driver inputs with the waveform candidate image on the board,
  HSPY at 24 V, and the motor disconnected. User reported no waveform on
  `CN3_1 / CN3_2`, no waveform on `CN3_3 / CN3_4`, and no waveform on
  `CN3_5 / CN3_6`; HSPY stayed `CV` at `0.036 A`; `nFAULT = 3.3 V`; no
  abnormal board symptom was reported. This is bounded no-motor oscilloscope
  evidence only. It opens no Motor Pilot, no Motor Profiler, no motor
  connection, no Hall closed loop, no sensorless operation, no power-stage
  readiness, and no motor readiness. Do not repeat this same check unless the
  image, wiring, board condition, trigger method, measurement setup, or
  observed value changes.
  `stdrive101_gate_waveform_candidate_residual_voltage_isolation_result_2026-06-21.md`
  records the bounded isolation follow-up after the waveform candidate
  USB-only DMM result reported `VS / 24V_FUSED = 2 V` and `REG12 = 0.3 V`.
  With USB / ST-LINK disconnected, HSPY / 24 V OFF and physically
  disconnected, motor disconnected, and no `10 kohm` wake resistor or LIN1
  stimulus installed, the user confirmed `VS / 24V_FUSED = 0 V` and
  `REG12 = 0 V`. The earlier candidate USB-only `VS / 24V_FUSED = 2 V`
  cleared after USB disconnect, so persistent VS backfeed is not indicated in
  this candidate isolation check and the immediate residual-voltage blocker is
  cleared only. This opens no 24 V command from this record, no Run / Debug,
  no Gate PWM output, no Motor Pilot, no Motor Profiler, no motor connection,
  and no hardware readiness. The next checkpoint may only be a separate
  candidate 24 V static no-motor phase-gate or execution entry with fresh
  preconditions, not motor power-up.
  `stdrive101_gate_waveform_candidate_usb_only_dmm_result_2026-06-21.md`
  records the user-reported post-download USB-only DMM table after the
  waveform candidate image copy. The user reported `CN3_1` through `CN3_6`
  all `0 V`, `CN3_13 = 3 V`, `CN3_14 = 3 V`,
  `VS / 24V_FUSED = 2 V`, and `REG12 = 0.3 V`; board heat / smell / sound /
  reset-loop status was not reported in this latest row. The six driver-input
  stop-rule was not hit, but the voltage-boundary stop condition is active
  because `VS / 24V_FUSED = 2 V` is above the prior `< 1 V` USB-only
  boundary. This is not a pass for upward hardware progression and opens no
  Run / Debug, no 24 V command, no Gate PWM output, no Motor Pilot, no Motor
  Profiler, no motor connection, and no hardware readiness. Its live
  checkpoint is superseded by the later waveform candidate residual-voltage
  isolation result, which records `VS / 24V_FUSED = 0 V` and `REG12 = 0 V`
  after USB / ST-LINK disconnect.
  `stdrive101_gate_waveform_candidate_usb_only_download_result_2026-06-21.md`
  records one authorized USB-only ST-LINK mass-storage copy of the waveform
  candidate BIN. User authorization was `允许复制 candidate BIN 到 D:`. The
  copied BIN SHA256 was
  `362C510E4F682751F0721B54F306F6E144951F03F9FF875E68E238D92A29BB31`, size
  `1852` bytes. `D:` was `NOD_G474RE`; `D:\FAIL.TXT` was absent before and
  after copy; the target BIN was not retained after copy, consistent with
  ST-LINK mass-storage consumption; `DETAILS.TXT` reported
  `Version: V3J17M10` and `Build: Oct 17 2025 15:12:06`. The board image is
  now treated as the waveform candidate image for the next bounded checks.
  This download record itself contained no post-download CN3 / REG12 DMM
  result and no measured waveform result. Because the candidate image calls
  `gate_waveform_candidate_run_once()` once after reset and then holds idle
  low, this record does not prove absence of a boot-time output transition.
  It opens no Run / Debug, no 24 V command, no Motor Pilot, no Motor Profiler,
  no motor connection, and no hardware readiness. Its live checkpoint is
  superseded by the later waveform candidate residual-voltage isolation
  result, which clears the immediate residual-voltage blocker only and changes
  the next checkpoint to a separate candidate 24 V static no-motor phase-gate
  or execution entry.
  `stdrive101_gate_waveform_candidate_bin_artifact_record_no_power_2026-06-21.md`
  records conversion of the existing Gate E2 waveform candidate ELF to a
  downloadable BIN. Candidate ELF SHA256 is
  `10BA818730E259AEBA8A5C5E5C96CFBA32FCB90AAA4136B775022B9D69ADCE7C`, MAP
  SHA256 is
  `170EA77C566F98CF9EF2AC88F76B154238A5404DC705AAE3917BEAE7C1503D4C`, and
  generated BIN SHA256 is
  `362C510E4F682751F0721B54F306F6E144951F03F9FF875E68E238D92A29BB31`, size
  `1852` bytes. The fallback ELF32 load-image converter was checked against
  the already-recorded neutral-wrapper objcopy BIN and matched. This is a BIN
  artifact only: no USB copy, no board image change, no Run / Debug, no 24 V
  execution, no Gate PWM output, no Motor Pilot, no Motor Profiler, no motor
  connection, and no hardware readiness.
  `stdrive101_gate_waveform_neutral_wrapper_24v_static_scope_baseline_result_2026-06-21.md`
  records the 24 V static oscilloscope baseline after the static no-motor DMM
  table. With oscilloscope ground on `CN3_15 / GND`, the user probed
  `CN3_1` / `CN3_2`, `CN3_3` / `CN3_4`, and `CN3_5` / `CN3_6`. The user
  reported all six MCU-facing driver inputs as `0 V` straight lines, HSPY
  `CV` about `0.036 A`, `nFAULT = 3.3 V`, and no board heat / smell / sound /
  reset-loop symptom. This is a static no-motor, no-PWM baseline only: no
  waveform output was executed. It opens no Run / Debug, no Gate PWM output,
  no Motor Pilot, no Motor Profiler, no motor connection, and no hardware
  readiness.
  `stdrive101_gate_waveform_neutral_wrapper_24v_static_no_motor_result_2026-06-21.md`
  records the bounded 24 V static no-motor result after residual-voltage
  isolation. User reported HSPY `CV`, current `0.036 A`,
  `VS / 24V_FUSED = 24 V`, `CN3_1` through `CN3_6 = 0 V`,
  `CN3_13 / nFAULT = 3.3 V`, `CN3_14 / 3V3 = 3.3 V`, `REG12 = 0.2 V`, and
  no board heat / smell / sound / reset-loop symptom. The six driver-input
  stop-rule was not hit and `nFAULT` stayed high in the static no-motor state.
  This is clean only for the bounded 24 V static no-motor table. Turn HSPY
  output OFF after the measurement. It opens no Run / Debug, no Gate PWM
  output, no Motor Pilot, no Motor Profiler, no motor connection, and no
  hardware readiness.
  `stdrive101_gate_waveform_neutral_wrapper_residual_voltage_isolation_result_2026-06-21.md`
  records the bounded follow-up after the USB-only DMM completion result
  reported `VS / 24V_FUSED = 2 V` and `REG12 = 0.5 V`. With USB / ST-LINK
  disconnected, HSPY / 24 V OFF and physically disconnected, motor
  disconnected, and no `10 kohm` wake resistor or LIN1 stimulus installed,
  the user reported `VS / 24V_FUSED = 0 V` and `REG12 = 0 V`. The earlier
  USB-only `VS / 24V_FUSED = 2 V` cleared after USB disconnect, so persistent
  VS backfeed is not indicated in this isolation check and the immediate
  residual-voltage blocker is cleared only. This opens no 24 V execution, no
  Run / Debug, no Gate PWM output, no Motor Pilot, no Motor Profiler, no motor
  connection, and no hardware readiness.
  `stdrive101_gate_waveform_neutral_wrapper_usb_only_dmm_completion_result_2026-06-21.md`
  records the completed post-download USB-only DMM table: carried-forward
  `CN3_1` through `CN3_6 = 0 V`, `P13 = 3.3 V`, and `P14 = 3.3 V`, plus
  the user-reported completion rows `VS / 24V_FUSED = 2 V`,
  `REG12 = 0.5 V`, and no board heat / smell / sound / reset-loop symptom.
  The six driver-input stop-rule was not hit, but the voltage-boundary stop
  condition was active in that record because `VS / 24V_FUSED = 2 V` was
  above the prior `< 1 V` USB-only boundary. Its live residual-voltage
  checkpoint is now superseded by the later residual-voltage isolation result,
  which records `VS / 24V_FUSED = 0 V` and `REG12 = 0 V` after USB / ST-LINK
  disconnect.
  `stdrive101_gate_waveform_neutral_wrapper_usb_only_dmm_partial_result_2026-06-21.md`
  records the user-reported post-download USB-only DMM readings:
  `CN3_1` through `CN3_6` all `0 V`, `P13 = 3.3 V`, and `P14 = 3.3 V`.
  `P13` and `P14` are recorded against the requested `CN3_13 / nFAULT` and
  `CN3_14 / 3V3` rows using the same header-label mapping as the prior
  USB-only table. The six driver-input stop-rule was not hit because no
  `CN3_1` through `CN3_6` reading was stably above `0.3 V`. This is partial
  USB-only DMM evidence only: `VS / 24V_FUSED`, `REG12`, and board heat /
  smell / sound / reset-loop status were not reported in that partial record.
  It is superseded by the later DMM completion result and residual-voltage
  isolation result.
  `stdrive101_gate_waveform_neutral_wrapper_usb_only_download_result_2026-06-21.md`
  records one USB-only ST-LINK mass-storage copy of the neutral-wrapper BIN.
  User confirmed `USB-only`, `24V disconnected`, and `motor disconnected`,
  then explicitly allowed copying the neutral-wrapper BIN to `D:`. The source
  ELF SHA256 is
  `C47C02D379DC5312095DF786BF8C99B58D42323AD9227D0903BCB8C98AAD9591`, MAP
  SHA256 is
  `5FB24B2735EFFD402C26BDC3B0D267B26B06DC6522A6B5B5D876491BA9A42A83`, and
  BIN SHA256 is
  `CA2A42F2F83C42EA9E7BEC628BD8656A422DBE767CFFD5A5865BE781603D3D71`.
  Pre-copy checks showed `D:` volume label `NOD_G474RE`, matched source BIN
  hash, no `D:\FAIL.TXT`, and no existing target BIN. The BIN was copied once
  to `D:\stdrive101_gate_waveform_neutral_wrapper_image.bin`; after a short
  wait, `D:` was still `NOD_G474RE`, `D:\FAIL.TXT` was absent, and the target
  BIN was no longer visible, consistent with ST-LINK mass-storage
  consumption. This download record itself contained no DMM neutral-state
  result and opened no 24 V, no Run / Debug, no Gate PWM output, no Motor
  Pilot, no Motor Profiler, no motor connection, and no hardware readiness.
  The later partial DMM, DMM completion, and residual-voltage isolation
  results supersede this download record's live checkpoint; the newest live
  checkpoint is a separate dated next-stage phase-gate decision.
  `stdrive101_gate_waveform_neutral_wrapper_bin_artifact_record_no_power_2026-06-21.md`
  records that the neutral-wrapper ELF was converted with STM32Cube GNU Arm
  `objcopy` into a downloadable BIN,
  `.tmp/gwnw_build_2026-06-21_clean/stdrive101_gate_waveform_neutral_wrapper_image.bin`,
  size `1044` bytes, SHA256
  `CA2A42F2F83C42EA9E7BEC628BD8656A422DBE767CFFD5A5865BE781603D3D71`.
  `stdrive101_gate_waveform_neutral_wrapper_usb_only_neutral_state_phase_gate_plan_2026-06-21.md`
  records planning only for a future USB-only neutral-state check of the
  neutral-wrapper image. It carries forward neutral-wrapper ELF SHA256
  `C47C02D379DC5312095DF786BF8C99B58D42323AD9227D0903BCB8C98AAD9591` and
  MAP SHA256 `5FB24B2735EFFD402C26BDC3B0D267B26B06DC6522A6B5B5D876491BA9A42A83`.
  The build-only image uses `main_neutral_wrapper.c`, excludes old
  `main_waveform_candidate.c`, retains
  `gate_waveform_neutral_wrapper_hold_idle_forever`, and has no retained ELF
  `gate_waveform_candidate_run_once`; the MAP lists
  `.text.gate_waveform_candidate_run_once` only as a discarded zero-address
  input section. This is phase-gate planning only: no flash, no Run / Debug,
  no USB runtime execution, no 24 V, no Gate PWM output, no Motor Pilot, no
  Motor Profiler, no motor connection, and no hardware readiness. The next
  checkpoint is only a separate neutral-wrapper USB-only neutral-state
  execution-entry after explicit user request and freshly confirmed
  preconditions; Gate E4 remains closed.
  `stdrive101_gate_waveform_neutral_wrapper_build_only_record_no_power_2026-06-21.md`
  records no-power object-only and linked-image build-only evidence for the
  neutral-wrapper source review. The separate build-only package is
  `manual_gate_waveform_neutral_wrapper_build_only_2026-06-21/`; the
  source-review packages still have no `CMakeLists.txt`, and only the
  build-only package defines both `GATE_WAVEFORM_CANDIDATE_GATE_E2_BUILD_ACK`
  and `GATE_WAVEFORM_NEUTRAL_WRAPPER_BUILD_ACK`. Clean configure used
  `CMAKE_SYSTEM_NAME=Generic`, `CMAKE_SYSTEM_PROCESSOR=arm`,
  `CMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY`, STM32Cube GNU Arm GCC
  `14.3.1`, and Ninja `1.13.2`; clean build produced
  `stdrive101_gate_waveform_neutral_wrapper_objects` and
  `stdrive101_gate_waveform_neutral_wrapper_image`. Clean ELF SHA256 is
  `C47C02D379DC5312095DF786BF8C99B58D42323AD9227D0903BCB8C98AAD9591`;
  clean MAP SHA256 is
  `5FB24B2735EFFD402C26BDC3B0D267B26B06DC6522A6B5B5D876491BA9A42A83`.
  `arm-none-eabi-size` reports `text=1044`, `data=0`, `bss=1536`,
  `dec=2580`, `hex=a14`; linker memory report is RAM
  `1536 B / 128 KB / 1.17%` and FLASH `1044 B / 512 KB / 0.20%`. The build
  includes `gate_waveform_candidate.c` and `main_neutral_wrapper.c`, excludes
  old `main_waveform_candidate.c`, and defines no HEX or BIN target. The
  retained ELF symbol table has no `gate_waveform_candidate_run_once`; the
  MAP lists it only as a discarded zero-address input section from
  `gate_waveform_candidate.c`, expected with `-ffunction-sections` and
  `--gc-sections`. This is build-only evidence only: no flash, no Run /
  Debug, no USB runtime execution, no 24 V, no Gate PWM output, no Motor
  Pilot, no Motor Profiler, no motor connection, and no hardware readiness.
  The next checkpoint is only a neutral-wrapper USB-only neutral-state
  phase-gate plan or review, not runtime execution.
  `stdrive101_gate_waveform_neutral_wrapper_source_review_no_power_2026-06-21.md`
  records source-review evidence only for the neutral-wrapper package
  `manual_gate_waveform_neutral_wrapper_source_package_2026-06-21/`. The
  package intentionally has no `CMakeLists.txt`; the header requires
  `GATE_WAVEFORM_NEUTRAL_WRAPPER_BUILD_ACK` with a `#error` guard before
  compilation. `main_neutral_wrapper.c` replaces a future candidate entry
  point only: it calls `gate_waveform_candidate_force_idle_low()` before the
  forever loop and inside the forever loop. Wrapper `Inc/` and `Src/` contain
  no `gate_waveform_candidate_run_once()` call and no TIM1 waveform-window or
  output-enable helper. This closes a source-side review after the Gate E3
  limitation: the Gate E2 `run_once()` image remains unsuitable for proving no
  boot transient with DMM-only evidence, while the wrapper itself is still
  source-review only. It opens no build, flash, Run / Debug, USB runtime
  execution, 24 V, Gate PWM output, Motor Pilot, Motor Profiler, motor
  connection, or hardware readiness. The next checkpoint is only a
  neutral-wrapper build-only boundary plan or build-only record, not USB
  runtime.
  `stdrive101_gate_waveform_usb_only_neutral_state_phase_gate_plan_2026-06-21.md`
  records Gate E3 phase-gate planning only for a future USB-only
  neutral-state check of the Gate E2 waveform candidate image. It carries
  forward the Gate E2 ELF SHA256
  `10BA818730E259AEBA8A5C5E5C96CFBA32FCB90AAA4136B775022B9D69ADCE7C` and
  MAP SHA256
  `170EA77C566F98CF9EF2AC88F76B154238A5404DC705AAE3917BEAE7C1503D4C`.
  The current candidate `main()` calls `gate_waveform_candidate_run_once()`
  once and then loops forcing idle low, so a future DMM-only USB check can
  prove only steady post-window idle state and cannot prove absence of a
  reset-time or boot-time transient. This is plan-only evidence: no flash, no
  Run / Debug, no USB runtime execution, no 24 V, no Gate PWM output, no
  Motor Pilot, no Motor Profiler, no motor connection, and no hardware
  readiness. The next checkpoint is only a separate Gate E3 execution-entry
  after explicit user request and fresh preconditions, or a source-side
  neutral-wrapper review; Gate E4 remains closed.
  `stdrive101_gate_waveform_build_only_record_no_power_2026-06-21.md`
  records Gate E2 no-power object-only and linked-image build-only evidence
  for the exact Gate E1 reviewed source package. The separate build-only
  package is `manual_gate_waveform_build_only_2026-06-21/`; the Gate E1
  source package still has no `CMakeLists.txt`, and only the Gate E2 package
  defines `GATE_WAVEFORM_CANDIDATE_GATE_E2_BUILD_ACK`. Clean configure used
  `CMAKE_SYSTEM_NAME=Generic`, `CMAKE_SYSTEM_PROCESSOR=arm`,
  `CMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY`, STM32Cube GNU Arm GCC
  `14.3.1`, and Ninja `1.13.2`; clean build produced
  `stdrive101_gate_waveform_candidate_objects` and
  `stdrive101_gate_waveform_candidate_image`. Clean ELF SHA256 is
  `10BA818730E259AEBA8A5C5E5C96CFBA32FCB90AAA4136B775022B9D69ADCE7C`;
  clean MAP SHA256 is
  `170EA77C566F98CF9EF2AC88F76B154238A5404DC705AAE3917BEAE7C1503D4C`.
  `arm-none-eabi-size` reports `text=1852`, `data=0`, `bss=1544`,
  `dec=3396`, `hex=d44`. Source/build, ELF-symbol, and MAP forbidden screens
  are clean. This is build-only evidence only: no flash, no Run / Debug, no
  USB runtime execution, no 24 V, no Gate PWM output, no Motor Pilot, no Motor
  Profiler, no motor connection, and no hardware readiness. The next
  checkpoint is Gate E3 USB-only neutral-state phase-gate plan or review only,
  not runtime execution.
  `stdrive101_gate_waveform_isolated_source_package_review_no_power_2026-06-21.md`
  records Gate E1 no-power source-package review evidence for
  `manual_gate_waveform_source_package_2026-06-21/`. The package intentionally
  has no `CMakeLists.txt` and the header requires
  `GATE_WAVEFORM_CANDIDATE_GATE_E2_BUILD_ACK` with a `#error` guard before
  compilation. Candidate pins are fixed as `PA8`, `PA9`, `PA10`, `PB13`,
  `PB14`, and `PB15`; startup and shutdown force all six low. The reviewed
  constants are `1 kHz`, `100` permille duty, `16` window periods, `8`
  pre-idle periods, `32` post-idle periods, and `DTG 0x90`. TIM1 `MOE`,
  `CCER`, break, AOE clearing, dead-time, and complementary-output policy are
  visible in source, and `nFAULT` stop handling disables TIM1 outputs and
  forces all six pins low. This is source-review evidence only: no build, no
  flash, no Run / Debug, no USB runtime execution, no 24 V, no Gate PWM
  output, no Motor Pilot, no Motor Profiler, no motor connection, and no
  hardware readiness. The next checkpoint is Gate E2 build-only boundary
  planning or build-only record only.
  `stdrive101_gate_waveform_image_design_plan_no_power_2026-06-20.md`
  records Gate E0 design-boundary planning only for a future isolated
  waveform image. It requires a separate isolated waveform candidate, keeps
  the normal generated MCSDK app and command ingress blocked, fixes the only
  candidate driver-input pins as `PA8`, `PA9`, `PA10`, `PB13`, `PB14`, and
  `PB15`, requires all six low before and after any future candidate window,
  and requires future TIM1 `MOE`, `CCER`, break, AOE, dead-time, polarity,
  and complementary-overlap policy review before source or build. This is
  design-plan evidence only: no source package, no CMake edit, no build, no
  flash, no Run / Debug, no USB runtime execution, no 24 V, no Gate PWM
  output, no Motor Pilot, no Motor Profiler, no motor connection, and no
  hardware readiness. Gate E1 source-package review is now recorded, so the
  next checkpoint is Gate E2 build-only boundary planning or build-only record
  only.
  `stdrive101_gate_waveform_pwm_output_no_power_phase_gate_plan_2026-06-20.md`
  records the next no-power phase-gate plan after the 24V static lockout
  carry-forward result. It accepts the carry-forward static boundary, linked
  lockout image, and USB-only runtime lockout result as planning evidence,
  keeps the normal generated MCSDK PWM path blocked, and names future-only
  Gate E0 through Gate E5 records for waveform-image design, isolated source,
  build-only image, USB-only neutral-state check, future scope-only no-motor
  execution-entry, and result recording. This is plan-only evidence: no flash,
  no Run / Debug, no USB runtime execution, no 24 V, no Gate PWM output, no
  oscilloscope probing on live gate or phase nodes, no Motor Pilot, no Motor
  Profiler, no motor connection, and no hardware readiness.
  `stdrive101_manual_gate_test_24v_static_lockout_carry_forward_result_2026-06-20.md`
  records the no-repeat carry-forward result after the user clarified that the
  equivalent USB + 24 V static all-inputs-low check had already been measured.
  It carries forward the existing USB + 24 V static recheck: HSPY `CV`, about
  `0.045 A`, `CN3_1` through `CN3_6` all close to `0 V`,
  `CN3_13 / nFAULT = 3.3 V`, `CN3_14 / 3V3 = 3.3 V`, and `REG12 = 0.3 V`.
  It also carries forward the USB-only lockout runtime result as reviewed
  lockout-image driver-input-low evidence: `CN3_1` through `CN3_6 = 0 V`,
  `nFAULT = 3.3 V`, `CN3_14 / 3V3 = 3.3 V`, `REG12 = 0 V`, and driver-input
  stop rule not hit. No repeated measurement is requested here, and there is
  no claim of a new 24V lockout measurement under the lockout image. The next
  checkpoint may only be a no-power phase-gate plan for the next higher-risk
  step, such as gate-waveform / PWM-output planning; still no Gate PWM,
  Motor Pilot, Motor Profiler, motor connection, power-stage readiness, or
  motor readiness.
  `stdrive101_manual_gate_test_24v_static_lockout_execution_entry_2026-06-20.md`
  records the user-requested entry after the 24V static lockout phase-gate
  plan. The user confirmed HSPY output `OFF`, HSPY set to `24 V / 0.2 A`,
  `VS / 24V_FUSED` close to `0 V` and below `1 V`, motor disconnected,
  `10 kohm` wake resistor / `LIN1` stimulus removed, Motor Pilot / Profiler
  closed, and no abnormal heat / smell / sound. It opened exactly one bounded
  24 V static lockout measurement pass as a historical execution-entry record.
  The later carry-forward result closes the duplicate-measurement branch using
  the already recorded USB + 24 V static recheck, so this entry must not be
  used to ask for the same static table again unless the image, wiring, board
  condition, or tool state changes. It is not PWM validation, not Motor Pilot,
  not Motor Profiler, not motor connection, and not hardware readiness.
  `stdrive101_manual_gate_test_24v_static_lockout_phase_gate_plan_2026-06-20.md`
  records a phase-gate plan for a later bounded 24 V static lockout check
  after the USB-only lockout result. It accepts the USB-only runtime lockout
  result as driver-input-low evidence and carries forward the earlier USB plus
  24V static baseline. It names candidate later 24V static lockout execution
  preconditions, measurement table, rollback path, and stop rules. This is
  plan-only evidence: no 24V execution in this record, no flash, no Run /
  Debug, no normal generated MCSDK app, no Gate PWM, no Motor Pilot, no Motor
  Profiler, no motor connection, and no hardware readiness.
  `stdrive101_manual_gate_test_usb_only_runtime_lockout_result_2026-06-20.md`
  records one USB / ST-LINK-only lockout flash / run measurement result. The
  reviewed ELF SHA256 was
  `87BF3F7A28949F8DB654927292083609E52AB46C511CB6191D03B280DBFFE9B6`,
  the generated BIN SHA256 was
  `CBF833C8E9289D8B4A952C32C641CAA94928F1F8119C5DC528EBD779915EA6BE`,
  the BIN was copied through ST-LINK mass storage `D:` / `NOD_G474RE`, and no
  `FAIL.TXT` was present after copy. User-reported readings were
  `CN3_1` through `CN3_6 = 0 V`, `CN3_13 / nFAULT = 3.3 V`,
  `CN3_14 / 3V3 = 3.3 V`, and `REG12 = 0 V`; driver-input stop rule was not
  hit. This is USB-only runtime evidence only: no 24 V, no PWM, no Motor
  Pilot, no Motor Profiler, no motor connection, and no hardware readiness.
  `stdrive101_manual_gate_test_usb_only_runtime_lockout_execution_entry_2026-06-20.md`
  records the user request for `USB-only lockout runtime 检查`, user-confirmed
  physical preconditions, and matched candidate ELF hash. It opens exactly one
  USB-only lockout flash / run measurement pass. It is not 24 V, not PWM, not
  Motor Pilot, not Motor Profiler, not motor connection, and not hardware
  validation; the next evidence must be a separate runtime result record after
  direct measurements are reported.
  `stdrive101_manual_gate_test_usb_only_runtime_lockout_phase_gate_plan_2026-06-20.md`
  records a phase-gate plan for a later USB-only runtime lockout check. It
  accepts the linked-image build-only record as image-boundary evidence,
  carries forward the ELF/MAP hashes, and names the later USB-only runtime
  preconditions, measurement table, and stop rules. This is plan-only evidence:
  no flash, no Run / Debug, no USB runtime execution, no 24 V, no PWM, no
  Motor Pilot, no Motor Profiler, no motor connection, and no hardware
  validation.
  `stdrive101_manual_gate_test_linked_image_build_only_record_2026-06-20.md`
  records Gate D build-only evidence for the isolated lockout linked image.
  The repo-local CMake package adds linked target
  `stdrive101_gate_lockout_image`, configured as `Generic` / `arm` with
  STM32Cube GNU Arm GCC `14.3.1` and Ninja. The build produced
  `.tmp/manual_gate_test_lockout_linked_image/stdrive101_gate_lockout_image.elf`
  and
  `.tmp/manual_gate_test_lockout_linked_image/stdrive101_gate_lockout_image.map`,
  with sizes, hashes, memory usage, key symbols, and clean forbidden source /
  ELF / MAP screens recorded. This is build-only evidence only: no flash, no
  Run / Debug, no USB runtime execution, no 24 V, no PWM, no Motor Pilot, no
  Motor Profiler, no motor connection, and no hardware validation.
  `stdrive101_manual_gate_test_linked_image_build_boundary_plan_2026-06-20.md`
  records Gate D boundary planning for a future linkable lockout firmware
  image. It carries forward the lockout source hashes and object-only build
  pass, fixes future link candidate inputs to repo-local
  `nucleo_g474re_baseline` startup, linker script, `system_stm32g4xx.c`,
  `syscalls.c`, and `sysmem.c`, names the future target
  `stdrive101_gate_lockout_image`, and requires ELF plus MAP as minimum future
  build-only artifacts. This is boundary-plan evidence only: no linked image,
  no CMake link target, no build, no flash, no Run / Debug, no USB runtime
  execution, no 24 V, no PWM, and no hardware validation.
  `stdrive101_manual_gate_test_usb_only_runtime_lockout_prep_2026-06-20.md`
  records Gate C preparation for a future USB-only runtime lockout check. It
  carries forward the object-only build pass, source hashes, object hashes,
  future linked-image boundary, USB-only no-24V physical boundary, expected
  future pin readings, stop rules, and a user table for a later approved
  runtime. This is preparation evidence only, not flash, not Run / Debug, not
  USB runtime execution, not 24 V, not PWM, and not hardware validation.
  `stdrive101_manual_gate_test_lockout_object_build_pass_2026-06-20.md`
  records a successful no-power object-only build of
  `stdrive101_gate_lockout_objects` using STM32Cube GNU Arm GCC `14.3.1` and
  Ninja `1.13.2`. The target produced `gate_test_lockout.c.obj` and
  `main_lockout.c.obj` only; no lockout ELF / HEX / BIN / MAP linked firmware
  image was produced. This is object compilation evidence only, not flash,
  runtime, PWM, or hardware validation.
  `stdrive101_manual_gate_test_lockout_object_target_2026-06-20.md` records a
  repo-local CMake object-library target for the isolated lockout package. The
  target compiles only `gate_test_lockout.c` and `main_lockout.c` object files
  and has no ELF / HEX / BIN link target. `REPO_ROOT` was corrected and CMSIS
  headers resolve statically. CMake configure was blocked by sandboxed access
  to external Ninja, and escalation returned 503, so no object build pass is
  claimed. It is build-target setup evidence only, not flash, runtime, PWM, or
  hardware validation.
  `stdrive101_manual_gate_test_lockout_source_package_2026-06-20.md` records
  the repo-local isolated lockout source package under
  `manual_gate_test_lockout_build_only_2026-06-20/`. The package forces
  `PA8`, `PA9`, `PA10`, `PB13`, `PB14`, and `PB15` low as GPIO outputs,
  keeps `PB12 / nFAULT` as input, clears TIM1 `CCER`, clears TIM1 `MOE` and
  automatic output, and leaves TIM1 break enabled. Static grep found no
  forbidden normal MCSDK start / command-ingress / output-enable symbols in
  package `Src` and `Inc`. It is source-package evidence only: no embedded
  build target yet, no flash, no runtime, no 24 V, no Gate PWM output, and no
  motor action.
  `stdrive101_manual_gate_test_firmware_plan_no_power_2026-06-20.md`
  records the no-power-only plan for any future STDRIVE101 manual gate-test
  firmware. Normal generated MCSDK start remains blocked as the first
  gate-test path; any future build must use an isolated lockout route that
  avoids `MC_StartMotor1()`, `MCI_START`, PC13 start/stop, MCP command ingress,
  Motor Pilot, Hall closed-loop paths, speed-loop paths, and motor connection.
  The first lockout image must hold six driver inputs low and keep TIM1 outputs
  locked off. This is plan-only evidence, not firmware implementation, not PWM
  validation, not motor validation, not power-stage readiness, and not motor
  readiness.
  `stdrive101_r3_2_mcsdk_pwm_output_path_source_closure_2026-06-20.md`
  records the exact local Workbench MCSDK `r3_2_g4xx_pwm_curr_fdbk.c` source
  identity and PWM output-path review. The reviewed source confirms normal
  generated MCSDK start remains blocked for powered PWM because the generated
  state path disables BRK before low-side boot-cap, and
  `R3_2_TurnOnLowSides()` enables TIM1 main outputs with 0-tick low-sides-on
  semantics. This is not PWM validation, firmware runtime validation, motor
  validation, power-stage readiness, or motor readiness.
  `stdrive101_pwm_gate_test_no_power_source_review_2026-06-20.md` records the
  no-power source/configuration review for a future explicit PWM/gate-test
  phase gate. The static hardware screen is clean for planning only, but
  generated MCSDK direct PWM remains blocked by command-ingress, external
  R3_2 implementation, BKIN polarity, Hall-route, and generation-log trust
  gaps. This is not PWM validation, firmware runtime validation, motor
  validation, power-stage readiness, or motor readiness.
  `stdrive101_usb24_static_recheck_result_2026-06-20.md` records the bounded
  USB + 24 V static recheck: HSPY `CV`, about `0.045 A`, `CN3_1` through
  `CN3_6` all close to `0 V`, `CN3_14 / 3V3 = 3.3 V`,
  `CN3_13 / nFAULT = 3.3 V`, and `REG12 = 0.3 V`. This closes the immediate
  static pre-PWM screen, but it is not PWM validation, firmware runtime
  validation, gate waveform evidence, motor validation, power-stage readiness,
  or motor readiness.
  `stdrive101_usbonly_mcu_default_input_state_result_2026-06-20.md` records
  the no-24V USB/ST-LINK default-state check: `CN3_1` through `CN3_6` all
  close to `0 V`, with `P13 = 3.3 V` and `P14 = 3.3 V` interpreted from the
  requested table as `CN3_13 / nFAULT = 3.3 V` and `CN3_14 / 3V3 = 3.3 V`.
  This supports only the next bounded static check; it is not PWM validation,
  firmware runtime validation, motor validation, power-stage readiness, or
  motor readiness.
  `stdrive101_all_inputs_low_static_recheck_result_2026-06-20.md` records the
  post-retest all-inputs-low static state after the `10 kohm` wake stimulus was
  removed: HSPY `CV`, current about `0.045 A`, `CN3_1` through `CN3_6` all
  close to `0 V`, `CN3_14 / 3V3 = 3.3 V`, `CN3_13 / nFAULT = 3.3 V`, and
  `REG12 = 0.3 V`. This closes the immediate standby-like recovery check, but
  it is not MCU default GPIO proof, PWM validation, motor validation,
  power-stage readiness, or motor readiness.
  `stdrive101_reg12_single_input_wake_retest_clean_result_2026-06-20.md`
  records the bounded single-input wake retest after gate-source pulldown
  rework: HSPY `CV`, `0.048 A`, `LIN1 = 3.13 V`, `nFAULT = 3.3 V`, and
  `REG12 = 12 V`. Recovery after removing the `10 kohm` stimulus and returning
  all driver inputs low was `CV`, `0.045 A`, `nFAULT = 3.3 V`, and
  `REG12 = 0.33 V`. This is clean wake/recovery evidence for the bounded
  `LIN1` stimulus only, not PWM validation, motor validation, power-stage
  readiness, or motor readiness.
  `stdrive101_gate_source_pulldown_rework_result_2026-06-20.md` records the
  final no-power six-route gate-source pulldown check after rework:
  `VS_OFF_V = 0 V`, `Q1_GS = 10 kohm`, `Q3_GS = 10 kohm`,
  `Q5_GS = 10 kohm`, `Q2_GS = 10 kohm`, `Q4_GS = 10 kohm`, and
  `Q6_GS = 10 kohm`. The previous gate-source pulldown anomaly branch is no
  longer indicated; the later bounded retest records `nFAULT = 3.3 V`, but
  no PWM, motor, or readiness claim is opened.
  `stdrive101_protection_nodes_no_power_dmm_result_2026-06-20.md` records the
  no-power protection-node follow-up: `SCREF-3V3 = 12 kohm`,
  `SCREF-GND = 12 kohm`, `CP-GND = 1.54 Mohm` rising to about `2 Mohm` with
  no resistance-mode beep, `REG12-GND = 0.2 Mohm` rising to `0.28 Mohm`,
  `REG12-VS = 40 kohm`, `OUT1-GND = no beep`, and `OUT1-VS` diode mode `OL`
  both directions. Stable hard short is not indicated on `CP`, `REG12`, or
  `OUT1` in the reported rows; VDS low-side path remains the primary review
  target.
  `stdrive101_fault_review_schematic_marking_2026-06-20.md` records the
  marked source image packet for the post-wake `nFAULT` review. Generated
  images under `hardware/schematic/annotated/` mark the source schematic's
  `CN8` / user's measured `CN3` route, `LIN1`, `nFAULT`, `CP`, `SCREF`,
  `REG12`, `OUT1`, `GHS1`, `GLS1`, Q2 low-side path, and ground domains.
  This is source-map evidence only and is not physical probe permission for
  unknown pads.
  `stdrive101_nfault_no_power_dmm_result_2026-06-20.md` records the follow-up
  no-power DMM results: `LIN1-3V3 = 66 kohm no beep`,
  `LIN1-GND = 60 kohm no beep`, `nFAULT-3V3 = 5 kohm no beep`, and
  `nFAULT-GND = 10 kohm no beep`. It does not show a persistent CN3-side
  rail hard short on `LIN1` or `nFAULT`; the next useful evidence is a marked
  source packet or confidently identified no-power protection-node checks.
  `stdrive101_single_input_wake_nfault_cause_review_2026-06-20.md` records
  the no-power/source review after `REG12 = 12 V` and `nFAULT = 0 V`. It
  ranks VDS monitoring after the `LIN1` low-side command as the primary
  review target, with REG12 sequence / accidental external REG12 tie, CP
  comparator, thermal shutdown, and external nFAULT pull-down as secondary
  targets. It opens only no-power DMM / source-packet collection.
  `stdrive101_reg12_single_input_wake_fault_result_2026-06-19.md` records the
  bounded single-input wake result with `CN3_14 / 3V3 -> 10 kohm ->
  CN3_2 / LIN1`: HSPY `CV`, `0.046 A`, `LIN1 = 3 V`, `nFAULT = 0 V`,
  `REG12 = 12 V`, and post-off `VS / 24V_FUSED = 0 V`. This observed
  `REG12` rising, but it is a stop-rule event because `nFAULT` was low; no
  repeat powered wake diagnostic is allowed before fault-cause review.
  `stdrive101_reg12_single_input_wake_baseline_result_2026-06-19.md` records
  the pre-stimulus baseline as `CV`, `0.036 A`, `VS / 24V_FUSED = 24 V`,
  `CN3_14 / 3V3 = 3.3 V`, `CN3_13 / nFAULT = 3.3 V`, and `REG12 = 0.33 V`.
  The baseline and wake result do not validate PWM, Hall closed-loop behavior,
  sensorless behavior, power-stage readiness, or motor readiness.
- Missing evidence: accepted final Workbench selected-field screenshots,
  Packet A / firmware feasibility proof for the current PCB2
  `HIN/LIN -> PA15/PB3/PB10/PA8/PA9/PA10` route and `PA0/PA1/PB4` software
  Hall route beyond no-power design review, a corrected FOC Workbench
  configuration for `MY_FOC` or a replacement project, software Hall firmware
  implementation, and all powered hardware evidence.

## Safety Boundary

Forbidden in this directory and this P2 stage:

- no 24V;
- no power-board connection;
- no motor connection;
- no PWM Gate output;
- no Motor Profiler run;
- no Hall closed-loop validation;
- no SMO / sensorless claim;
- no claim that `SET_RPM` controls real motor speed.

## Files

- `config_draft.md`: no-power MCSDK configuration draft and conflict policy.
- `pin_config_review_2026-05-14.md`: next-ring pin/config safety review and
  hard-stop checklist before trusting any generated MCSDK configuration.
- `evidence_packet_2026-05-14.md`: 褰撳墠璇佹嵁绛夌骇銆佷粨搴撳簱瀛樺拰淇′换浠讳綍鐢熸垚
  MCSDK 閰嶇疆鍓嶇殑闃诲椤广€?- `source_packet_intake_checklist_2026-05-14.md`: accepted / rejected source
  rules before any missing P2 evidence can be upgraded.
- `software_hall_firmware_entry_plan_2026-05-28.md`: Chinese-first no-power
  firmware-entry plan for the future `PA0/PA1/PB4` debug-only software Hall
  adapter. Decision:
  `Software Hall firmware-entry plan / debug-only no-power boundary / no firmware implementation / no MCSDK hook / no Hall readiness`.
- `pcb2_waiting_hardware_handoff_2026-05-31.md`: current waiting-hardware
  handoff. It records PCB2 as not populated / waiting for hardware, keeps DMM
  deferred, requests a hardware teammate status line and any updated source
  package, and points the no-power algorithm track to the mixed Hall sequence
  check under WP-030.
- `pcb2_populated_route_unchanged_dmm_pending_2026-06-01.md`: current
  populated-board handoff. It records PCB2 as soldered / in hand with unchanged
  `PA0/PA1/PB4 + PB3=LIN1 + P14/P15=3V3/GND` route, opens the DMM table as
  no-power pending, and keeps all powered / firmware readiness claims blocked.
- `stdrive101_reg12_single_input_wake_baseline_result_2026-06-19.md`:
  user-reported pre-stimulus baseline for the bounded STDRIVE101 single-input
  wake diagnostic. It records `CV`, `0.036 A`, `VS / 24V_FUSED = 24 V`,
  `CN3_14 / 3V3 = 3.3 V`, `CN3_13 / nFAULT = 3.3 V`, and `REG12 = 0.33 V`
  before any `10 kohm` stimulus. Current decision is `pre-stimulus baseline
  satisfied only`; it is not a wake result or powered-drive readiness.
- `stdrive101_reg12_single_input_wake_fault_result_2026-06-19.md`:
  user-reported bounded STDRIVE101 single-input wake result with
  `CN3_14 / 3V3 -> 10 kohm -> CN3_2 / LIN1`. It records HSPY `CV`,
  `0.046 A`, `LIN1 = 3 V`, `nFAULT = 0 V`, `REG12 = 12 V`, and post-off
  `VS / 24V_FUSED = 0 V`. Current decision is `REG12` rose under stimulus,
  but `nFAULT = 0 V` is a stop-rule event; no retry before fault-cause
  review and no powered-drive readiness.
- `stdrive101_single_input_wake_nfault_cause_review_2026-06-20.md`:
  no-power / source review of why `nFAULT` went low after the single-input
  wake result. Current decision is `primary review target VDS monitoring after
  LIN1 low-side command`; next checkpoint is no-power DMM on `LIN1` and
  `nFAULT`, or a marked source packet for `SCREF`, `CP`, `REG12`, and `OUT1`.
- `stdrive101_nfault_no_power_dmm_result_2026-06-20.md`:
  user-reported no-power DMM follow-up on `LIN1` and `nFAULT`. It records
  no hard short indication on `LIN1` or `nFAULT`; `nFAULT -> GND` is
  `10 kohm` with no beep. The next useful evidence is a marked source packet
  or confidently identified no-power checks for `SCREF`, `CP`, `REG12`,
  `OUT1`, and related low-side-1 gate / MOSFET nodes before any repeat
  powered wake.
- `stdrive101_fault_review_schematic_marking_2026-06-20.md`:
  no-power source-marking packet for the post-wake `nFAULT` review. It links
  the generated marked images under `hardware/schematic/annotated/` and records
  the marked `CN8` / `CN3`, `LIN1`, `nFAULT`, `CP`, `SCREF`, `REG12`, `OUT1`,
  `GHS1`, `GLS1`, Q2 low-side path, and ground-domain clues. It supports
  no-power source review only and does not authorize unknown-node probing,
  repeat powered wake, PWM, motor, or readiness.
- `stdrive101_protection_nodes_no_power_dmm_result_2026-06-20.md`:
  no-power protection-node DMM result after the marked source packet. It
  records no stable hard short indication on `CP`, `REG12`, or `OUT1` in the
  user-reported rows, keeps VDS low-side path as the primary review target,
  and limits the next step to no-power Q2 source / body-diode / gate-source
  path checks if the pads are confidently identified.
- `stdrive101_gate_source_pulldown_rework_result_2026-06-20.md`:
  no-power six-route gate-source pulldown rework result. It records final
  user-reported readings of `10 kohm` on `Q1/Q3/Q5/Q2/Q4/Q6` gate-source
  paths, closes the previous gate-source pulldown anomaly branch, and keeps
  repeat powered wake, PWM, motor, and readiness blocked pending a separate
  bounded decision.
- `stdrive101_reg12_single_input_wake_retest_clean_result_2026-06-20.md`:
  bounded single-input wake retest result after gate-source pulldown rework.
  It records `LIN1 = 3.13 V`, HSPY `CV`, `0.048 A`, `nFAULT = 3.3 V`, and
  `REG12 = 12 V`, plus recovery to `REG12 = 0.33 V` and `nFAULT = 3.3 V`
  after removing the `10 kohm` stimulus. It is not PWM validation, motor
  validation, power-stage readiness, or motor readiness.
- `stdrive101_all_inputs_low_static_recheck_result_2026-06-20.md`:
  bounded static recheck after the clean single-input wake retest. It records
  HSPY `CV`, about `0.045 A`, `CN3_1` through `CN3_6` close to `0 V`,
  `3V3 = 3.3 V`, `nFAULT = 3.3 V`, and `REG12 = 0.3 V` after the `10 kohm`
  wake stimulus was removed. It is not MCU default GPIO proof, PWM
  validation, motor validation, power-stage readiness, or motor readiness.
- `stdrive101_usbonly_mcu_default_input_state_result_2026-06-20.md`:
  no-24V USB/ST-LINK default-state check. It records `CN3_1` through `CN3_6`
  close to `0 V`, with `P13/P14` interpreted as `CN3_13 / nFAULT = 3.3 V` and
  `CN3_14 / 3V3 = 3.3 V`. It is not PWM validation, firmware runtime
  validation, motor validation, power-stage readiness, or motor readiness.
- `stdrive101_usb24_static_recheck_result_2026-06-20.md`:
  bounded USB + 24 V static recheck. It records HSPY `CV`, about `0.045 A`,
  `CN3_1` through `CN3_6` close to `0 V`, `3V3 = 3.3 V`, `nFAULT = 3.3 V`,
  and `REG12 = 0.3 V` with USB/ST-LINK connected and 24 V applied. It is not
  PWM validation, firmware runtime validation, gate waveform evidence, motor
  validation, power-stage readiness, or motor readiness.
- `pcb2_no_power_dmm_continuity_short_check_result_2026-06-19.md`:
  user-reported no-power DMM continuity / short-check summary for the current
  PCB2 route. It records expected continuity for the `CN3_10-PA0`,
  `CN3_11-PA1`, `CN3_12-PB4`, `CN3_2-PB3`, `CN3_14-3V3`,
  `CN3_15-GND`, and `CN3_13-PB12` rows, plus no reported rail,
  signal-to-rail, or Hall-line hard shorts. Raw ohm values were not provided.
  It is not powered validation or readiness.
- `software_hall_code_entry_boundary_after_dmm_2026-06-19.md`:
  no-power post-DMM code-entry boundary for the future software Hall adapter.
  Current decision is `Software Hall code-entry boundary after DMM summary /
  PA0-PA1-PB4 debug-only adapter planning allowed / no firmware
  implementation / no MCSDK hook / no Hall readiness`. It updates the entry
  path after the DMM summary and keeps all future code work behind a separate
  no-power authorization.
- `source_packet_request_pack_2026-05-14.md`: concrete request pack for the
  next `.stmcx`, MotorControl screenshot, CN8/EDA/netlist, and STDRIVE101
  protection-path handoff.
- `source_packet_review_template_2026-05-14.md`: repeatable review form for
  accepting, downgrading to clue-only, or rejecting Packet A/B/C and PB3/SWO
  evidence before updating the evidence packet.
- `source_packet_review_2026-05-15_001_cn8_stdrive101_schematic_candidate.md`:
  review of the user-provided CN8 / STDRIVE101 schematic screenshot candidate;
  current decision is `Partial clue`.
- `packet_a_sources/2026-05-15_my_first_foc/My_First_FOC.stwb6`: preserved
  local MCSDK 6 Workbench project candidate.
- `source_packet_review_2026-05-15_002_my_first_foc_stwb6.md`: Packet A review
  of the local `.stwb6`; current decision is `Partial clue`, not build-only
  clearance.
- `packet_a_sources/2026-05-16_custom_nucleo_stdrive101/`: prepared capture
  package for a new project-specific Workbench configuration targeting
  `NUCLEO-G474RE` plus a Custom / Generic STDRIVE101 power stage. It contains a
  GUI guide, no-power motor measurement template, pin assignment table, and
  screenshot inbox. It does not yet contain an accepted `.stwb6`.
- `source_packet_review_2026-05-16_001_custom_nucleo_stdrive101_capture_package.md`:
  review of the 2026-05-16 capture package. Current decision is
  `Partial clue / Preparation only`; generated-project trust remains
  `Not allowed`.
- `mcu_pin_compatibility_check_2026-05-17.md`: local MCSDK asset comparison for
  `STM32G431RBTx` versus `STM32G474RETx`. It supports the hardware teammate's
  statement that the compared key rows are pin-function compatible, but it does
  not prove CN8 routing, `J_HALL` numbering, or `PB3` / SWO release.
- `source_packet_review_2026-05-17_001_vendor_motor_g431_pin_table.md`:
  review of the vendor `57BLF01` motor source and hardware teammate
  `STM32G431RB` pin table. Current decision is `Partial clue`; motor values are
  supplier clues, and board-route / Hall connector blockers remain.
- `source_packet_review_2026-05-18_001_motor_wiring_definition.md`: review of
  the user-provided 57BLF01 phase/Hall wire-color definition image. Current
  decision is `Partial clue`; wire colors are candidate clues only and do not
  prove physical harness inspection, Hall powering, phase/Hall alignment, or
  `J_HALL` numbering.
- `packet_a_capture_task_2026-05-18.md`: workflow-only task package for the
  future project-specific Workbench capture. It fixes the `.stwb6` path,
  required screenshots, stop conditions, and field acceptance matrix. It does
  not add a real `.stwb6`, screenshots, generated source, build evidence, or
  hardware validation.
- `source_packet_review_2026-05-19_001_packet_a_workbench_capture_attempt.md`:
  review of the no-power Workbench capture attempt. Current decision is
  `Partial clue / stopped`; Workbench 6.4.2 launches and
  `NUCLEO-G474RE` / `STM32G474RETx` control-board context is visible, but no
  accepted self-made STDRIVE101 power-stage context or selected-field
  screenshots were captured.
- `source_packet_review_2026-05-19_002_prodoc_p1_epro.md`: review of the
  user-confirmed EasyEDA Pro schematic source for the self-developed
  STDRIVE101 driver board. Current decision is `Partial clue / accepted
  schematic-source clue`; it improves board-side source visibility but does
  not prove PCB layout, NUCLEO `CN8`, STM32 endpoints, or readiness.
- `source_packet_review_2026-05-19_003_gerber_pcb2.md`: review of the
  hardware-teammate supplied Gerber PCB2 package. Current decision is
  `Partial clue / accepted board-side Gerber + flying-probe net clue`; it
  supports board-side pad/net clues but not NUCLEO endpoint mapping,
  continuity, or readiness.
- `source_packet_review_2026-05-19_004_pcb2_mapping_pin1_protection.md`:
  review of the user-provided current PCB2 mapping, pin-1 images, Hall
  relationship, PB3/SWO guidance, and STDRIVE101 protection-chain statement.
  Current decision is `Partial clue / accepted current PCB2 mapping source;
  Hall/PWM conflicts clarified`; `PC7/PB3/PB10` is an alternate suggestion,
  while current PCB2 Hall routing is `IA/IB/IC -> PA0/PA1/PB4`.
- `current_pcb2_hall_pwm_strategy_2026-05-19.md`: no-power strategy review
  for the current PCB2 PWM/Hall mismatch. Current decision is
  `No-power strategy review opened / no PCB change first`; old standard
  `TIM1` PWM and `PA15/PB3/PB10` Hall drafts are historical or alternate
  candidates only, and software Hall on `PA0/PA1/PB4` remains feasibility
  review only.
- `current_pcb2_packet_a_firmware_feasibility_2026-05-19.md`: no-power Packet
  A / firmware feasibility review for the current no-PCB-change route. Current
  decision is `No-PCB-change route remains feasibility only / Packet A not
  accepted`; current PWM is not cleared as standard MCSDK `TIM1`
  complementary PWM selected-field evidence, and `PA0/PA1/PB4` is not cleared
  as same-timer hardware Hall.
- `software_hall_adapter_design_review_2026-05-19.md`: no-power design review
  for the current PCB2 software Hall path on `PA0/PA1/PB4`. Current decision is
  `Software Hall adapter remains no-power design review / Packet A not
  accepted`; it defines future GPIO/EXTI sampling, edge timestamping,
  valid-state filtering, minimal ISR responsibility, MCSDK integration
  boundaries, and `hardware-rework planning` fallback conditions without
  adding firmware, runtime APIs, generated source, build-only clearance, or
  Hall readiness.
- `dmm_continuity_short_check_request_2026-05-22.md`: no-power table template
  for the next real-world evidence before software Hall adapter implementation.
  It requests continuity for `IA->PA0`, `IB->PA1`, `IC->PB4`, `PB3->LIN1`,
  `P14->3V3`, `P15->GND`, `nFAULT->PB12`, plus rail, signal-to-rail, and
  Hall-line short checks. It is not a measurement result.
- `software_hall_no_power_algorithm_prep_2026-05-22.md`: algorithm-side
  no-power preparation for the current software Hall route. Current decision is
  `Algorithm-side no-power preparation / no firmware implementation / no Hall
  readiness`; it defines valid/illegal Hall states, transition rules, candidate
  sequences, debug observables, ISR limits, and MCSDK hard stops while the
  unpopulated-board DMM gate is deferred, not passed.
- `software_hall_state_machine_exercise_card_2026-05-22.md`: Chinese-first
  no-power exercise card for the algorithm role. Current decision is
  `User Hall state-machine exercise requested / no firmware implementation /
  no Hall readiness`; it asks five concept checks and a four-row Hall
  transition table before any pseudocode or firmware work.
- `software_hall_adapter_pseudocode_draft_2026-05-27.md`: Chinese-first
  no-power pseudocode draft for the future `PA0/PA1/PB4` software Hall
  adapter. Current decision is `Software Hall adapter pseudocode draft / no
  firmware implementation / no MCSDK Hall integration / no Hall readiness`;
  it defines function responsibilities, state fields, decision order, ISR
  limits, debug observables, MCSDK hard stops, and future code-entry
  conditions without adding firmware or hardware evidence.
- `software_hall_adapter_processing_order_card_2026-05-27.md`: Chinese-first
  no-power repair card for the future software Hall adapter processing order.
  Current decision is `Software Hall adapter processing-order teaching card /
  no firmware implementation / no MCSDK Hall integration / no Hall readiness`;
  it explains raw read, illegal-state check, first-valid handling, repeated
  state handling, bounce/timing check, adjacent direction check, and
  abnormal-jump count after the user could not restate the sequence.
- `software_hall_host_model_review_2026-05-27.md`: review of the host-side
  executable software Hall reference model in `src/software_hall_model.py` and
  `tests/test_software_hall_model.py`. Current decision is `Host-side software
  Hall reference model / no firmware implementation / no MCSDK Hall integration
  / no Hall readiness`; it proves only host-side algorithm behavior.
- `software_hall_golden_vectors_review_2026-05-27.md`: review of the
  host-side software Hall golden vectors in
  `tests/fixtures/software_hall_golden_vectors.json` and replay test
  `tests/test_software_hall_vectors.py`. Current decision is `Host-side
  software Hall golden vectors / no firmware implementation / no MCSDK Hall
  integration / no Hall readiness`; it proves only host-side no-power
  algorithm replay behavior.
- `host_side_no_power_foc_algorithm_model_review_2026-06-22.md`: review of
  the host-side FOC math reference model in `src/foc_core_model.py` and
  `tests/test_foc_core_model.py`. Current decision is `Host-side no-power FOC
  algorithm model / no firmware implementation / no MCSDK integration / no PWM
  output / no motor readiness`; it proves only host-side algorithm behavior
  while MCSDK remains the intended framework generation path.
- `host_side_no_power_foc_golden_vectors_review_2026-06-22.md`: review of
  the host-side FOC golden vectors in
  `tests/fixtures/foc_core_golden_vectors.json` and replay test
  `tests/test_foc_core_vectors.py`. Current decision is `Host-side no-power
  FOC golden vectors / no firmware implementation / no MCSDK integration / no
  PWM output / no motor readiness`; it proves only host-side no-power math
  replay behavior and is not MCSDK convention proof.
- `software_hall_mcsdk_integration_probe_2026-05-27.md`: read-only probe of
  the 2026-05-21 generated-project clue files for speed/position feedback
  integration points. Current decision is `MCSDK Hall integration points
  identified as read-only clues / no firmware implementation / no MCSDK Hall
  integration / no Hall readiness`; it identifies standard TIM2 hardware Hall
  clues and keeps the current `PA0/PA1/PB4` software Hall route outside MCSDK
  Hall integration.
- `software_hall_firmware_entry_checklist_2026-05-27.md`: no-power entry
  checklist for any future `PA0/PA1/PB4` software Hall adapter firmware work.
  Current decision is `Software Hall firmware-entry checklist / no firmware
  implementation / no MCSDK Hall integration / no Hall readiness`; it requires
  populated-board DMM evidence, GPIO/EXTI boundary review, timestamp-source
  decision, debug route, and separate MCSDK firmware-integration review before
  any adapter code or powered claim. The build-only record now exists but does
  not open firmware implementation.
- `software_hall_gpio_exti_boundary_review_2026-05-27.md`: no-power
  GPIO/EXTI boundary draft for the future software Hall adapter. Current
  decision is `Software Hall GPIO/EXTI boundary review draft / no firmware
  implementation / no GPIO runtime proof / no Hall readiness`; it records
  `PA0/PA1/PB4` as software input candidates, `EXTI0/EXTI1/EXTI4` as
  event-capture candidates, minimal ISR duties, and the remaining pull-mode,
  timestamp, debug, build-only, DMM, and MCSDK integration blockers.
- `software_hall_timestamp_source_review_2026-05-27.md`: no-power timestamp
  source review for the future `PA0/PA1/PB4` software Hall adapter. Current
  decision is `Software Hall timestamp-source review draft / no firmware
  implementation / no timer configuration / no Hall readiness`; it records
  `TIM1` as unavailable, current `TIM2` as the generated MCSDK Hall clue path,
  `HAL_GetTick()` as coarse-only, and a future isolated free-running timer plus
  `unsigned delta` as review targets only.
- `software_hall_debug_output_route_review_2026-05-27.md`: no-power
  low-frequency debug-output route review for the future software Hall adapter.
  Current decision is `Software Hall low-frequency debug-output route review
  draft / no firmware implementation / no UART implementation / no Hall
  readiness`; it defines future snapshot fields and blocks ISR printing,
  JSON formatting, UART transmit, ESP32 / WebSocket, SWO, every-edge streaming,
  and direct MCSDK speed feedback.
- `software_hall_mcsdk_firmware_integration_boundary_review_2026-05-27.md`:
  no-power MCSDK firmware-integration boundary review for the future software
  Hall adapter. Current decision is `Software Hall MCSDK firmware-integration
  boundary review draft / no firmware implementation / no MCSDK hook / no Hall
  readiness`; it records generated MCSDK clues such as `HALL_M1`,
  `SpeednTorqCtrlM1`, `PIDSpeedHandle_M1`, `pSTC`, `MCI_Handle_t`, `FOCVars`,
  `SPD_HALL_TIM_M1_IRQHandler`, `M1_SPEED_SENSOR=HALL_SENSOR`, and
  `M1_HALL_TIMER_SELECTION=HALL_TIM2` as clues or hard stops, not hooks.
- `software_hall_mcsdk_hook_evidence_request_checklist_2026-05-27.md`:
  no-power MCSDK hook evidence request checklist for the future software Hall
  adapter. Current decision is `Software Hall MCSDK hook evidence request
  checklist / no firmware implementation / no MCSDK hook / no Hall readiness`;
  it requests exact generated or interface sources such as
  `hall_speed_pos_fdbk.c/.h`, `speed_torq_ctrl.c/.h`, `mc_tasks.c/.h`,
  `mc_tasks_foc.c`, `mc_interface.c/.h`, `mc_api.c/.h`, `mc_app_hooks.c/.h`,
  `mc_parameters.c/.h`, `motorcontrol.c/.h`, interrupt sources,
  current-feedback backend files, and ASPEP / register-interface files before
  any hook proposal.
- `source_packet_review_2026-05-27_001_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot.md`:
  no-power review of the full generated Workbench `Src/Inc` snapshot copied
  from `C:\Users\gregrg\.st_workbench\projects\QIANSAI_G474_STDRIVE101_FOC_P2`.
  Current decision is `Full generated Src/Inc snapshot archived / source
  interface evidence available for read-only review / no firmware
  implementation / no MCSDK hook / no Hall readiness`; the snapshot lives at
  `packet_a_sources/2026-05-27_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot/`
  and includes manifest/hash evidence for read-only interface review only.
- `software_hall_mcsdk_speed_position_feedback_interface_review_2026-05-27.md`:
  no-power MCSDK speed / position feedback interface review for the future
  software Hall route. Current decision is `Software Hall MCSDK speed/position
  feedback interface review / no firmware implementation / no MCSDK hook / no
  Hall readiness`; it traces `HALL_M1`, `HALL_CalcAvrgMecSpeedUnit`,
  `STC_GetSpeedSensor`, `SPD_GetAvrgMecSpeedUnit`, and `SPD_GetElAngle`, and
  records that a future hook needs a reviewed `SpeednPosFdbk`-compatible
  component rather than direct writes of `direction_candidate` or
  `speed_candidate`.
- `packet_a_board_designer_manager_path_review_2026-05-19.md`: no-power Packet
  A path review for the Workbench Board Designer / Board Manager path. Current
  decision is `Board Designer / Board Manager path exists as local
  documentation and tool clue / Packet A still blocked`; it records the local
  Workbench external-tool entries, local Board Designer / Board Manager
  executables, Board Designer manual custom-board workflow clues, and the
  boundary that built-in `EVALSTDRIVE101`, `STEVAL-LVLP01`, and
  `EVLDRIVE101-HPD` cannot replace evidence for the self-developed STDRIVE101
  board. It adds no generated-project trust, no build-only clearance, no
  custom board source, no `.stwb6`, and no powered readiness.
- `packet_a_board_designer_manager_gui_checklist_2026-05-19.md`: GUI-only
  checklist for the later user screenshot capture around Board Designer /
  Board Manager. Current decision is `GUI-only checklist prepared / Packet A
  still blocked`; it defines the screenshot save directory, required screenshots
  for custom/import/create board paths, Power/Control/Inverter board flows,
  Board Aggregation, Finalize/save prompt, Board Manager import/list path, and
  blocked states. It adds no generated-project trust, no custom board source,
  no `.stwb6`, and no powered readiness.
- `source_packet_review_2026-05-19_005_my_foc_generated_project.md`: review of
  the user-created `MY_FOC` Workbench generated project. Current decision is
  `Partial clue / generated project quarantined / Packet A not accepted`; it
  proves a real generated project exists, but the project is `SIX_STEP`, not
  FOC, and current sensing, fault/break, Hall/PWM route, and motor evidence are
  not accepted. User clarification that pins can be changed is recorded as a
  future editable route, not Packet A acceptance.
- `packet_a_sources/2026-05-19_my_foc_generated_project/`: selected no-power
  source/config/log files copied from the user-created `MY_FOC` Workbench
  project. The generated `Src/`, `Inc/`, `Drivers/`, and
  `MCSDK_v6.4.2-Full/` trees are intentionally not copied or trusted.
- `my_foc_foc_candidate_edit_2026-05-19.md`: records the Codex manual FOC edit
  attempt and rollback for
  `C:\Users\gregrg\.st_workbench\projects\MY_FOC.stwb6`. Current decision is
  `Manual FOC source edit failed Workbench reload / rolled back / Packet A still not accepted`;
  the one-field edit from `"algorithm": "sixStep"` to `"algorithm": "FOC"`
  made Workbench unable to load the file, so Codex restored the external source
  from backup. The current external source is again six-step; the failed FOC
  candidate is negative evidence only.
- `packet_c_stdrive101_protection_detail_review_2026-05-20.md`: no-power
  Packet C detail review for `DT/MODE`, `nFAULT`, `REG12`, `CP`, `SCREF`,
  `VS/VM`, bootstrap, `STBY`, and VDS monitoring. Current decision is
  `Packet C detail narrowed / protection proof still partial clue / P3 still blocked`;
  it marks the old `V_DSth = 0.249V` / `I_trip ~= 55A` note as not accepted and
  keeps Packet C, generated-project trust, continuity, and powered readiness
  blocked.
- `hardware_supplement_handoff_2026-05-19.md`: current hardware-teammate
  handoff for the next accepted evidence. It asks for exact board revision,
  `CN3 -> NUCLEO/CN8 -> STM32 pin` mapping, `CN3` / `J_HALL` pin-1
  orientation, Hall A/B/C mapping, PB3/SWO evidence, STDRIVE101 protection
  chain details, optional PCB source, and later no-power continuity records.
- `hardware_teammate_min_request_2026-05-19.md`: short first packet to send to
  the hardware teammate. It asks first for Gerber PCB2 revision confirmation,
  complete `CN3 -> NUCLEO/CN8 -> STM32 pin` mapping, and marked `CN3` /
  `J_HALL` pin-1 evidence.
- `packet_a_workbench_asset_probe_2026-05-19.md`: read-only local Workbench
  asset probe. It records built-in STDRIVE101 board JSONs and the installed
  Board Designer / Board Manager executables as path clues only; Packet A
  remains blocked until a project-specific custom board definition, `.stwb6`,
  and selected-field screenshots are accepted.
- `non_hardware_parallel_track_2026-05-15.md`: no-power plan for temporarily
  skipping Packet B/C scheduling while keeping blockers visible and progressing
  Packet A, STM32-side signal contract, future build-only gate, and delivery
  cleanup.
- `packet_a_local_probe_2026-05-15.md`: local Packet A recheck covering repo
  `.stmcx`, `.stwb6`, screenshots, common user locations, `.stm32cubemx`,
  CubeMX, STM32Cube Repository, Start Menu, and `F:\STMCSDK`. Current result:
  Packet A has a `Partial clue` source candidate.
- `packet_a_capture_checklist_2026-05-15.md`: next acceptable no-power capture
  checklist for `.stmcx`, MotorControl screenshots, or exact GUI path plus
  captured version/config screen.
- `stm32_side_signal_contract_2026-05-15.md`: no-power planning contract for
  future STM32 responsibilities on CN8-facing signals. It separates candidate
  firmware intent from connector routing and hardware proof.
- `future_build_only_gate_2026-05-15.md`: future gate that allows only
  no-power build evidence after Packet A selected fields are accepted; current
  state is still `Not allowed` because Packet A is only `Partial clue`.
- `p2_readiness_snapshot_2026-05-15.md`: current P2 gate decision. It
  consolidates Packet A/B/C, PB3/SWO, signal-contract, and build-only status
  and records that generated-project trust is still `Not allowed`.
- `user_action_queue_2026-05-14.md`: direct user-facing queue for the next
  Packet B board-route source, Packet A MCSDK/MotorControl source, and PB3/SWO
  release evidence.
- `tool_probe_2026-05-14.md`: local tool and GUI evidence gathered for this
  practice turn.
- `workbench_entry_probe_2026-05-14.md`: targeted probe for Workbench launcher,
  `.stmcx`, and installed MCSDK MotorControl package data.
- `gui_capture_result_2026-05-14.md`: records the GUI follow-up attempt,
  screenshots, `.ioc` readback, and the remaining `.stmcx` / MotorControl
  blocker.
- `gui_capture_checklist_2026-05-14.md`: next GUI-only capture checklist.
- `screenshots/2026-05-14_cubemx_home.png`: CubeMX Home launch evidence. This
  is not a saved MCSDK configuration.
- `screenshots/2026-05-14_cubemx_ioc_launch_attempt.png` and
  `screenshots/2026-05-14_cubemx_ioc_pinout_active_window.png`: CubeMX opened
  the saved NUCLEO `.ioc` to `Pinout & Configuration`. These are fallback GUI
  evidence, not Workbench `.stmcx` evidence.

## Next Valid Evidence

Use `user_action_queue_2026-05-14.md` and
`source_packet_request_pack_2026-05-14.md` to collect the next valid P2
evidence. For the current hardware-teammate follow-up after the 2026-05-19
`.epro` and Gerber intakes, start with
`hardware_teammate_min_request_2026-05-19.md`, then use
`hardware_supplement_handoff_2026-05-19.md` for the full matrix. Use
`source_packet_review_template_2026-05-14.md` to review any new material before
upgrading any blocker. After the 2026-05-19 clarification image, current PCB2
Hall/PWM strategy review, and Packet A / firmware feasibility review, the next
question is no longer generic hardware mapping and is no longer whether the
current route is immediately clearable. The current no-PCB-change route remains
feasibility only. After the software Hall adapter design review, Packet A Board
Designer / Board Manager path review, and GUI-only checklist, the next valid
Packet A packet is a GUI-only custom/user board capture for the self-developed
STDRIVE101 board if Workbench can create a reviewable artifact; otherwise
Packet A remains blocked and the fallback is surrogate build-only planning
without generated-project trust or separate hardware-rework planning. The next
valid packet must be one of:

- a real `.stwb6` saved by MCSDK 6 Workbench, or legacy `.stmcx`;
- a screenshot showing the Workbench/CubeMX draft configuration;
- an exact reproducible GUI path plus a captured version/config screen;
- the 2026-05-16 custom capture package after a Workbench-supported
  custom/user board entry path is found and its real `.stwb6` plus screenshots
  are added and reviewed;
- current-version CN8 / EDA / netlist / high-resolution route evidence;
- board-level STDRIVE101 protection-path source evidence.
- exact board-revision confirmation, connector orientation proof, PB3/SWO
  release evidence, or later no-power continuity records as defined in
  `hardware_supplement_handoff_2026-05-19.md`.

Even after that evidence exists, P2 still does not authorize powered hardware
actions.

If the hardware-source branch is skipped for scheduling, use
`non_hardware_parallel_track_2026-05-15.md`. Skipping is not clearance: Packet
B/C blockers stay blocked.

Before claiming readiness for generated-project trust or build-only work, read
`p2_readiness_snapshot_2026-05-15.md`. Before running the next Packet A GUI
capture, read `packet_a_capture_task_2026-05-18.md`. Before asking the hardware
teammate for the next board-side packet, read
`hardware_teammate_min_request_2026-05-19.md` and
`hardware_supplement_handoff_2026-05-19.md`. Before treating any Workbench
Board Designer / Board Manager result as Packet A evidence, read
`packet_a_workbench_asset_probe_2026-05-19.md` and
`packet_a_board_designer_manager_path_review_2026-05-19.md`. Before capturing
later Board Designer / Board Manager screenshots, read
`packet_a_board_designer_manager_gui_checklist_2026-05-19.md`.
Before using any STDRIVE101 protection threshold or `nFAULT` behavior in a
phase decision, read
`packet_c_stdrive101_protection_detail_review_2026-05-20.md` and treat the old
`55A` VDS claim as not accepted.
