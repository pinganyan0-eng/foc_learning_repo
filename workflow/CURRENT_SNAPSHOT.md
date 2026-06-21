# Current Snapshot

Last updated: 2026-06-21

This is the short current-state page for low-token AI handoff. It summarizes
the current project stage and safety boundary. Historical detail remains in
`CURRENT_STATUS.md`.

## Current Stage

- Main project: STM32G474 edge-gateway FOC drive learning and competition
  project.
- Retrieval anchor for current PCB2 Hall route:
  `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`; `PB3=LIN1` and is not current
  PCB2 Hall. This remains software Hall planning evidence only and does not
  open Hall closed-loop readiness.
- Current stage: P2 MCSDK no-power precheck, PCB2 no-power DMM summary
  recorded, software Hall no-power firmware-entry planning, STDRIVE101
  single-input wake clean bounded retest after gate-source pulldown rework,
  post-retest all-inputs-low static recovery recheck, USB-only MCU-facing
  driver input default-state check, USB + 24 V static recheck, PWM/gate
  no-power source review, R3_2 MCSDK PWM output path source closure, manual
  gate-test firmware plan, manual gate-test lockout source package,
  manual gate-test lockout object-only target, manual gate-test lockout
  object-only build pass, manual gate-test USB-only runtime lockout
  preparation, manual gate-test linked-image build-boundary plan, manual
  gate-test linked-image build-only record, manual gate-test USB-only runtime
  lockout phase-gate plan, manual gate-test USB-only runtime lockout
  execution entry, manual gate-test USB-only runtime lockout result,
  manual gate-test 24V static lockout phase-gate plan, manual gate-test
  24V static lockout execution entry, manual gate-test 24V static lockout
  carry-forward result, gate-waveform / PWM-output no-power phase-gate
  plan, Gate E0 gate-waveform image design plan, Gate E1 isolated source
  package review, Gate E2 gate-waveform build-only record, Gate E3
  USB-only neutral-state phase-gate plan, gate-waveform neutral-wrapper
  source review, gate-waveform neutral-wrapper build-only record,
  gate-waveform neutral-wrapper USB-only neutral-state phase-gate plan,
  neutral-wrapper BIN artifact record, neutral-wrapper USB-only download
  execution-entry, neutral-wrapper USB-only download result, neutral-wrapper
  USB-only DMM partial result, neutral-wrapper USB-only DMM completion result,
  neutral-wrapper residual-voltage isolation result, neutral-wrapper
  24V static no-motor result, neutral-wrapper 24V static scope baseline
  result, waveform candidate BIN artifact record, waveform candidate
  USB-only download execution-entry, waveform candidate USB-only download
  result, waveform candidate USB-only DMM result, and waveform candidate
  residual-voltage isolation result.
- Current gate-waveform candidate residual-voltage isolation result:
  `stdrive101_gate_waveform_candidate_residual_voltage_isolation_result_2026-06-21.md`
  records the bounded isolation follow-up after the waveform candidate
  USB-only DMM result reported `VS / 24V_FUSED = 2 V` and `REG12 = 0.3 V`.
  User confirmed USB / ST-LINK disconnected, HSPY / 24 V OFF and physically
  disconnected, motor disconnected, no `10 kohm` wake resistor or LIN1
  stimulus installed, and DMM black probe on GND. User confirmed
  `VS / 24V_FUSED = 0 V` and `REG12 = 0 V`. The earlier candidate USB-only
  `VS / 24V_FUSED = 2 V` cleared after USB disconnect, so persistent VS
  backfeed is not indicated in this candidate isolation check and the
  immediate residual-voltage blocker is cleared only. This opens no 24 V
  command from this record, no Run / Debug, no Gate PWM output, no Motor
  Pilot, no Motor Profiler, no motor connection, and no readiness claim. Next
  checkpoint may only be a separate candidate 24 V static no-motor phase-gate
  or execution entry with fresh preconditions, not motor power-up.
- Current gate-waveform candidate USB-only DMM result:
  `stdrive101_gate_waveform_candidate_usb_only_dmm_result_2026-06-21.md`
  records the user-reported post-download USB-only DMM readings after the
  waveform candidate image copy. The user reported `CN3_1` through `CN3_6`
  all `0 V`, `CN3_13 = 3 V`, `CN3_14 = 3 V`,
  `VS / 24V_FUSED = 2 V`, and `REG12 = 0.3 V`. Board heat / smell / sound /
  reset-loop status was not reported in this latest row. The six driver-input
  stop-rule was not hit, but the voltage-boundary stop condition is active
  because `VS / 24V_FUSED = 2 V` is above the prior `< 1 V` USB-only
  boundary. This is not a pass for upward hardware progression and opens no
  Run / Debug, no 24 V command, no Gate PWM output, no Motor Pilot, no Motor
  Profiler, no motor connection, and no readiness claim. Its live checkpoint
  is superseded by the later waveform candidate residual-voltage isolation
  result, which records `VS / 24V_FUSED = 0 V` and `REG12 = 0 V` after
  USB / ST-LINK disconnect.
- Current gate-waveform candidate USB-only download result:
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
  no motor connection, and no readiness claim. Its live checkpoint is
  superseded by the later waveform candidate residual-voltage isolation
  result, which clears the immediate residual-voltage blocker only and changes
  the next checkpoint to a separate candidate 24 V static no-motor phase-gate
  or execution entry.
- Current gate-waveform candidate USB-only download execution entry:
  `stdrive101_gate_waveform_candidate_usb_only_download_execution_entry_2026-06-21.md`
  records the allowed envelope that opened the one USB-only mass-storage copy.
  It carries forward the candidate BIN hash above, the `D:` / `NOD_G474RE`
  target, pre-copy `FAIL.TXT` absence, and the one-copy limit. It is superseded
  for the live checkpoint by the download result.
- Current gate-waveform candidate BIN artifact record:
  `stdrive101_gate_waveform_candidate_bin_artifact_record_no_power_2026-06-21.md`
  records conversion of the existing Gate E2 waveform candidate ELF to a
  downloadable BIN. Candidate ELF SHA256 is
  `10BA818730E259AEBA8A5C5E5C96CFBA32FCB90AAA4136B775022B9D69ADCE7C`, MAP
  SHA256 is
  `170EA77C566F98CF9EF2AC88F76B154238A5404DC705AAE3917BEAE7C1503D4C`, and
  generated BIN SHA256 is
  `362C510E4F682751F0721B54F306F6E144951F03F9FF875E68E238D92A29BB31`, size
  `1852` bytes. The fallback ELF32 `PT_LOAD` converter was checked against
  the already-recorded neutral-wrapper objcopy BIN and matched SHA256
  `CA2A42F2F83C42EA9E7BEC628BD8656A422DBE767CFFD5A5865BE781603D3D71`.
  The MAP retains `gate_waveform_candidate_run_once` at `0x080005bc`. This
  is a BIN artifact only: no USB copy, no board image change, no Run / Debug,
  no 24 V execution, no Gate PWM output, no Motor Pilot, no Motor Profiler,
  no motor connection, and no readiness claim. Next checkpoint is only a
  separate waveform-candidate USB-only download execution entry after
  explicit user confirmation and authorization.
- Current gate-waveform neutral-wrapper 24V static scope baseline result:
  `stdrive101_gate_waveform_neutral_wrapper_24v_static_scope_baseline_result_2026-06-21.md`
  records oscilloscope ground on `CN3_15 / GND` and three two-channel probe
  passes: `CN3_1` / `CN3_2`, `CN3_3` / `CN3_4`, and `CN3_5` / `CN3_6`.
  User reported HSPY `CV` at about `0.036 A`, `CN3_1` through `CN3_6` as
  `0 V` straight lines, `nFAULT = 3.3 V`, and no board heat / smell / sound /
  reset-loop symptom. This is a static no-motor, no-PWM oscilloscope baseline
  only: no waveform output was executed. Turn HSPY output OFF after the
  baseline. Next checkpoint may only be a separate no-motor, short-window,
  instrumented waveform execution entry; no Motor Pilot, no Motor Profiler, no
  motor connection, and no readiness claim.
- Current gate-waveform neutral-wrapper 24V static no-motor result:
  `stdrive101_gate_waveform_neutral_wrapper_24v_static_no_motor_result_2026-06-21.md`
  records the bounded static check after residual-voltage isolation. User
  reported HSPY `CV`, current `0.036 A`, `VS / 24V_FUSED = 24 V`,
  `CN3_1` through `CN3_6 = 0 V`, `CN3_13 / nFAULT = 3.3 V`,
  `CN3_14 / 3V3 = 3.3 V`, `REG12 = 0.2 V`, and no board heat / smell /
  sound / reset-loop symptom. The six driver-input stop-rule was not hit and
  `nFAULT` stayed high in the static no-motor state. This is clean only for
  the bounded 24 V static no-motor table. Turn HSPY output OFF after the
  measurement. It opens no Run / Debug, no Gate PWM output, no Motor Pilot, no
  Motor Profiler, no motor connection, and no readiness claim. Next checkpoint
  may only be a separate no-motor instrumented gate-waveform gate, not direct
  motor power-up.
- Current gate-waveform neutral-wrapper residual-voltage isolation result:
  `stdrive101_gate_waveform_neutral_wrapper_residual_voltage_isolation_result_2026-06-21.md`
  records the bounded follow-up after the USB-only DMM completion result
  reported `VS / 24V_FUSED = 2 V` and `REG12 = 0.5 V`. The user disconnected
  USB / ST-LINK while HSPY / 24 V remained OFF and physically disconnected,
  the motor remained disconnected, and no `10 kohm` wake resistor or LIN1
  stimulus was installed. The user then reported `VS / 24V_FUSED = 0 V` and
  `REG12 = 0 V`. The earlier USB-only `VS / 24V_FUSED = 2 V` cleared after
  USB disconnect, so persistent VS backfeed is not indicated in this
  isolation check and the immediate residual-voltage blocker is cleared only.
  This opens no 24 V execution, no Run / Debug, no Gate PWM output, no Motor
  Pilot, no Motor Profiler, no motor connection, and no readiness claim. Next
  checkpoint is a separate dated next-stage phase-gate decision, not another
  repeat of the residual-voltage table and not direct motor power-up.
- Current gate-waveform neutral-wrapper USB-only DMM completion result:
  `stdrive101_gate_waveform_neutral_wrapper_usb_only_dmm_completion_result_2026-06-21.md`
  completes the post-download USB-only DMM table. It carries forward
  `CN3_1` through `CN3_6 = 0 V`, `P13 = 3.3 V`, and `P14 = 3.3 V`, and
  records the new user-reported rows `VS / 24V_FUSED = 2 V`,
  `REG12 = 0.5 V`, and no board heat / smell / sound / reset-loop symptom.
  The six driver-input stop-rule was not hit, but the voltage-boundary stop
  condition for upward progression is active because `VS / 24V_FUSED = 2 V`
  is above the prior `< 1 V` USB-only boundary. This is a completed USB-only
  DMM table but not a pass for 24 V, PWM, or motor progression. Its live
  residual-voltage checkpoint is superseded by the later residual-voltage
  isolation result, which records `VS / 24V_FUSED = 0 V` and `REG12 = 0 V`
  after USB / ST-LINK disconnect.
- Current gate-waveform neutral-wrapper USB-only DMM partial result:
  `stdrive101_gate_waveform_neutral_wrapper_usb_only_dmm_partial_result_2026-06-21.md`
  records the user-reported post-download DMM readings: `CN3_1` through
  `CN3_6` all `0 V`, `P13 = 3.3 V`, and `P14 = 3.3 V`. `P13` and `P14` are
  recorded against the requested `CN3_13 / nFAULT` and `CN3_14 / 3V3` rows
  using the same header-label mapping as the prior USB-only table. The six
  driver-input stop-rule was not hit because no `CN3_1` through `CN3_6`
  reading was stably above `0.3 V`. This is a partial USB-only DMM result
  only: `VS / 24V_FUSED`, `REG12`, and board heat / smell / sound /
  reset-loop status were still not reported in the partial record. It opened
  no 24 V, no Run / Debug, no Gate PWM output, no Motor Pilot, no Motor
  Profiler, no motor connection, and no readiness claim. It is superseded for
  the live checkpoint by the later DMM completion result, which reports
  `VS / 24V_FUSED = 2 V` and changes the next checkpoint to residual-voltage
  isolation.
- Current gate-waveform neutral-wrapper USB-only download result:
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
  Pilot, no Motor Profiler, no motor connection, and no readiness claim. The
  later USB-only DMM partial, DMM completion, and residual-voltage isolation
  results supersede this download record's live checkpoint; the newest live
  checkpoint is a separate dated next-stage phase-gate decision.
- Current gate-waveform neutral-wrapper BIN artifact record:
  `stdrive101_gate_waveform_neutral_wrapper_bin_artifact_record_no_power_2026-06-21.md`
  records `objcopy` conversion of the neutral-wrapper ELF to the downloadable
  BIN `.tmp/gwnw_build_2026-06-21_clean/stdrive101_gate_waveform_neutral_wrapper_image.bin`,
  size `1044` bytes, SHA256
  `CA2A42F2F83C42EA9E7BEC628BD8656A422DBE767CFFD5A5865BE781603D3D71`.
  The retained ELF symbol screen keeps
  `gate_waveform_neutral_wrapper_hold_idle_forever` and has no retained
  `gate_waveform_candidate_run_once`.
- Current gate-waveform neutral-wrapper USB-only neutral-state phase-gate plan:
  `stdrive101_gate_waveform_neutral_wrapper_usb_only_neutral_state_phase_gate_plan_2026-06-21.md`
  records planning only for a future USB-only neutral-state check of the
  neutral-wrapper image. It carries forward neutral-wrapper ELF SHA256
  `C47C02D379DC5312095DF786BF8C99B58D42323AD9227D0903BCB8C98AAD9591` and MAP
  SHA256 `5FB24B2735EFFD402C26BDC3B0D267B26B06DC6522A6B5B5D876491BA9A42A83`.
  The build-only image uses `main_neutral_wrapper.c`, excludes old
  `main_waveform_candidate.c`, retains
  `gate_waveform_neutral_wrapper_hold_idle_forever`, and has no retained ELF
  `gate_waveform_candidate_run_once`; the MAP lists
  `.text.gate_waveform_candidate_run_once` only as a discarded zero-address
  input section. This is phase-gate planning only: no flash, no Run / Debug,
  no USB runtime execution, no 24 V, no Gate PWM output, no Motor Pilot, no
  Motor Profiler, no motor connection, and no readiness claim. The next
  checkpoint is only a separate neutral-wrapper USB-only neutral-state
  execution-entry after explicit user request and freshly confirmed
  preconditions; Gate E4 remains closed.
- Current gate-waveform neutral-wrapper build-only record:
  `stdrive101_gate_waveform_neutral_wrapper_build_only_record_no_power_2026-06-21.md`
  records no-power object-only and linked-image build-only evidence for the
  neutral-wrapper source review. The separate build-only package is
  `manual_gate_waveform_neutral_wrapper_build_only_2026-06-21/`. The
  source-review packages still have no `CMakeLists.txt`; only the build-only
  package defines both `GATE_WAVEFORM_CANDIDATE_GATE_E2_BUILD_ACK` and
  `GATE_WAVEFORM_NEUTRAL_WRAPPER_BUILD_ACK`. Clean configure used
  `CMAKE_SYSTEM_NAME=Generic`, `CMAKE_SYSTEM_PROCESSOR=arm`,
  `CMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY`, STM32Cube GNU Arm GCC
  `14.3.1`, and Ninja `1.13.2`; clean build produced
  `stdrive101_gate_waveform_neutral_wrapper_objects` and
  `stdrive101_gate_waveform_neutral_wrapper_image`. Clean ELF SHA256 is
  `C47C02D379DC5312095DF786BF8C99B58D42323AD9227D0903BCB8C98AAD9591`;
  clean MAP SHA256 is
  `5FB24B2735EFFD402C26BDC3B0D267B26B06DC6522A6B5B5D876491BA9A42A83`.
  Size is `text=1044`, `data=0`, `bss=1536`, `dec=2580`, `hex=a14`; RAM use
  is `1536 B / 128 KB / 1.17%` and FLASH use is `1044 B / 512 KB / 0.20%`.
  The build includes reviewed `gate_waveform_candidate.c` and wrapper
  `main_neutral_wrapper.c`, excludes old `main_waveform_candidate.c`, and
  defines no HEX or BIN target. The retained ELF symbol table has no
  `gate_waveform_candidate_run_once`; the MAP lists it only as a discarded
  zero-address input section from `gate_waveform_candidate.c`, expected with
  `-ffunction-sections` and `--gc-sections`. This is build-only evidence only:
  no flash, no Run / Debug, no USB runtime execution, no 24 V, no Gate PWM
  output, no Motor Pilot, no Motor Profiler, no motor connection, and no
  readiness claim. The next checkpoint is a neutral-wrapper USB-only
  neutral-state phase-gate plan or review only, not runtime execution.
- Current gate-waveform neutral-wrapper source review:
  `stdrive101_gate_waveform_neutral_wrapper_source_review_no_power_2026-06-21.md`
  records no-power source-review evidence only for
  `manual_gate_waveform_neutral_wrapper_source_package_2026-06-21/`. The
  package intentionally has no `CMakeLists.txt`; the header requires
  `GATE_WAVEFORM_NEUTRAL_WRAPPER_BUILD_ACK` with a `#error` guard before
  compilation. The wrapper replaces a future candidate entry point only:
  `main_neutral_wrapper.c` calls
  `gate_waveform_candidate_force_idle_low()` before the forever loop and
  inside the forever loop. Wrapper `Inc/` and `Src/` contain no
  `gate_waveform_candidate_run_once()` call and no TIM1 waveform-window or
  output-enable helper. This keeps the current Gate E2 `run_once()` image
  classified as unsuitable for proving no boot transient with DMM-only
  evidence, while the wrapper itself remains source review only. This opens no
  build, flash, Run / Debug, USB runtime execution, 24 V, Gate PWM output,
  Motor Pilot, Motor Profiler, motor connection, or readiness claim. The next
  checkpoint is neutral-wrapper build-only boundary plan or build-only record
  only, not USB runtime.
- Current Gate E3 gate-waveform USB-only neutral-state phase-gate plan:
  `stdrive101_gate_waveform_usb_only_neutral_state_phase_gate_plan_2026-06-21.md`
  records phase-gate planning only for a future USB-only neutral-state check
  of the Gate E2 waveform candidate image. It carries forward the Gate E2 ELF
  SHA256
  `10BA818730E259AEBA8A5C5E5C96CFBA32FCB90AAA4136B775022B9D69ADCE7C`
  and MAP SHA256
  `170EA77C566F98CF9EF2AC88F76B154238A5404DC705AAE3917BEAE7C1503D4C`.
  The current waveform candidate `main()` calls
  `gate_waveform_candidate_run_once()` once and then loops forcing idle low,
  so a future DMM-only USB check can prove only steady post-window idle state
  and cannot prove absence of a reset-time or boot-time transient. This plan
  opens no flash, no Run / Debug, no USB runtime execution, no 24 V, no Gate
  PWM output, no Motor Pilot, no Motor Profiler, no motor connection, and no
  readiness claim. The next checkpoint is only a separate Gate E3
  execution-entry after explicit user request and fresh preconditions, or a
  source-side neutral-wrapper review; Gate E4 remains closed.
- Current Gate E2 gate-waveform build-only record:
  `stdrive101_gate_waveform_build_only_record_no_power_2026-06-21.md`
  records no-power object-only and linked-image build-only evidence for the
  exact Gate E1 reviewed source package. The separate build-only package is
  `manual_gate_waveform_build_only_2026-06-21/`; the Gate E1 source package
  still has no `CMakeLists.txt`, and only the Gate E2 package defines
  `GATE_WAVEFORM_CANDIDATE_GATE_E2_BUILD_ACK`. Clean configure used
  `CMAKE_SYSTEM_NAME=Generic`, `CMAKE_SYSTEM_PROCESSOR=arm`,
  `CMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY`, STM32Cube GNU Arm GCC
  `14.3.1`, and Ninja `1.13.2`; clean build produced
  `stdrive101_gate_waveform_candidate_objects` and
  `stdrive101_gate_waveform_candidate_image`. Clean ELF SHA256 is
  `10BA818730E259AEBA8A5C5E5C96CFBA32FCB90AAA4136B775022B9D69ADCE7C`;
  clean MAP SHA256 is
  `170EA77C566F98CF9EF2AC88F76B154238A5404DC705AAE3917BEAE7C1503D4C`.
  Size is `text=1852`, `data=0`, `bss=1544`, `dec=3396`, `hex=d44`; RAM use
  is `1544 B / 128 KB / 1.18%` and FLASH use is `1852 B / 512 KB / 0.35%`.
  Source/build, ELF-symbol, and MAP forbidden screens are clean. This is
  build-only evidence only: no flash, no Run / Debug, no USB runtime, no
  24 V, no Gate PWM output, no Motor Pilot, no Motor Profiler, no motor
  connection, and no readiness claim. The next checkpoint is Gate E3 only: a
  separate USB-only neutral-state phase-gate plan or review, not runtime
  execution.
- Current Gate E1 gate-waveform isolated source package review:
  `stdrive101_gate_waveform_isolated_source_package_review_no_power_2026-06-21.md`
  records no-power source-review evidence only. The reviewed package is
  `manual_gate_waveform_source_package_2026-06-21/`; it intentionally has no
  `CMakeLists.txt` and the header requires
  `GATE_WAVEFORM_CANDIDATE_GATE_E2_BUILD_ACK` with a `#error` guard before
  any compilation. Candidate driver inputs are fixed as `PA8`, `PA9`, `PA10`,
  `PB13`, `PB14`, and `PB15`; startup and shutdown force all six low. The
  frozen candidate constants are `1 kHz`, `100` permille duty, `16` window
  periods, `8` pre-idle periods, `32` post-idle periods, and `DTG 0x90`. TIM1
  `MOE`, `CCER`, break, AOE clear, dead-time, and complementary-output policy
  are visible in source. The `nFAULT` stop path disables TIM1 outputs and
  forces all six pins low. This opens no build, flash, Run / Debug, USB
  runtime, 24 V, Gate PWM output, Motor Pilot, Motor Profiler, motor
  connection, or readiness claim. The next checkpoint is Gate E2 only: a
  separate object-only and linked-image build-only boundary plan or build-only
  record for the exact reviewed source package, still without runtime or
  hardware action.
- Current Gate E0 gate-waveform image design plan:
  `stdrive101_gate_waveform_image_design_plan_no_power_2026-06-20.md`
  records design-boundary planning only for a future isolated waveform image.
  It requires a separate isolated waveform candidate, keeps the normal
  generated MCSDK app and command ingress blocked, fixes candidate driver
  inputs to `PA8`, `PA9`, `PA10`, `PB13`, `PB14`, and `PB15`, requires all
  six to be forced low before and after any future candidate window, and
  requires future TIM1 `MOE`, `CCER`, break, AOE, dead-time, polarity, and
  complementary-overlap policy review before source or build. This record
  creates no source package, makes no CMake edit, runs no build, flashes no
  firmware, performs no Run / Debug, executes no USB runtime, applies no
  24 V, emits no Gate PWM output, opens no Motor Pilot or Motor Profiler
  path, connects no motor, and makes no readiness claim. Gate E1 has now been
  recorded separately, so the next checkpoint is Gate E2 build-only boundary
  planning or build-only record only, still without runtime or hardware action.
- Current gate-waveform / PWM-output no-power phase-gate plan:
  `stdrive101_gate_waveform_pwm_output_no_power_phase_gate_plan_2026-06-20.md`
  records planning only after the 24V static lockout carry-forward result. It
  accepts the carry-forward static boundary, linked lockout image, and
  USB-only runtime lockout result as planning evidence, keeps the normal
  generated MCSDK PWM path blocked, and names future-only Gate E0 through
  Gate E5 records for waveform-image design, isolated source, build-only
  image, USB-only neutral-state check, future scope-only no-motor
  execution-entry, and result recording. This plan opens no flash, no
  Run / Debug, no USB runtime execution, no 24 V, no Gate PWM output, no
  oscilloscope probing on live gate or phase nodes, no Motor Pilot, no Motor
  Profiler, no motor connection, and no readiness claims. The next checkpoint
  is Gate E0 only: a separate no-power waveform-image design plan or source /
  build review with execution actions still closed. Gate E0 has now been
  recorded separately, and Gate E1 source-package review is now recorded too.
  The next checkpoint is Gate E2 build-only boundary planning or build-only
  record only.
- Current manual gate-test 24V static lockout carry-forward result:
  `stdrive101_manual_gate_test_24v_static_lockout_carry_forward_result_2026-06-20.md`
  records the no-repeat decision after the user clarified that the equivalent
  USB + 24 V static all-inputs-low check had already been measured. It carries
  forward the existing USB + 24 V static recheck: HSPY `CV`, about `0.045 A`,
  `CN3_1` through `CN3_6` all close to `0 V`,
  `CN3_13 / nFAULT = 3.3 V`, `CN3_14 / 3V3 = 3.3 V`, and
  `REG12 = 0.3 V`. It also carries forward the USB-only lockout runtime
  result as reviewed lockout-image driver-input-low evidence:
  `CN3_1` through `CN3_6 = 0 V`, `nFAULT = 3.3 V`,
  `CN3_14 / 3V3 = 3.3 V`, `REG12 = 0 V`, and driver-input stop rule not hit.
  No repeated measurement is requested here, and there is no claim of a new
  24 V lockout measurement under the lockout image. The next checkpoint may
  only be a no-power phase-gate plan for the next higher-risk step, such as
  gate-waveform / PWM-output planning; that separate plan is now recorded.
  Still no Gate PWM, Motor Pilot, Motor Profiler, motor connection,
  power-stage readiness, or motor readiness.
- Current manual gate-test 24V static lockout execution entry:
  `stdrive101_manual_gate_test_24v_static_lockout_execution_entry_2026-06-20.md`
  records the user request to continue after the phase-gate plan and the
  freshly confirmed entry gates: HSPY output `OFF`, HSPY set to
  `24 V / 0.2 A`, `VS / 24V_FUSED` close to `0 V` and below `1 V`, motor
  disconnected, wake stimulus removed, Motor Pilot / Profiler closed, and no
  abnormal heat / smell / sound. It opens exactly one bounded 24 V static
  lockout measurement pass as a historical entry. The later carry-forward
  result closes the duplicate-measurement branch using the already recorded
  USB + 24 V static recheck, so this entry must not be used to ask for the
  same static table again unless the image, wiring, board condition, or tool
  state changes. It does not open Gate PWM, Motor Pilot, Motor Profiler,
  motor connection, Hall closed loop, sensorless operation, power-stage
  readiness, or motor readiness.
- Current manual gate-test 24V static lockout phase-gate plan:
  `stdrive101_manual_gate_test_24v_static_lockout_phase_gate_plan_2026-06-20.md`
  records a phase-gate plan only after the USB-only lockout result. It accepts
  the USB-only runtime lockout result as driver-input-low evidence and carries
  forward the earlier USB plus 24V static baseline. It names candidate later
  24V static lockout execution preconditions, measurement table, rollback path,
  and stop rules. It opens no 24V execution in this record, no flash, no Run /
  Debug, no normal generated MCSDK app run, no Gate PWM, no Motor Pilot, no
  Motor Profiler, no motor connection, and no readiness claims. The next
  possible checkpoint is only a later separate 24 V static lockout
  execution-entry record if explicitly requested and if preconditions are
  freshly true.
- Current manual gate-test USB-only runtime lockout result:
  `stdrive101_manual_gate_test_usb_only_runtime_lockout_result_2026-06-20.md`
  records one USB / ST-LINK-only lockout flash / run measurement pass using
  the reviewed lockout image. The ELF SHA256 was
  `87BF3F7A28949F8DB654927292083609E52AB46C511CB6191D03B280DBFFE9B6`,
  the generated BIN SHA256 was
  `CBF833C8E9289D8B4A952C32C641CAA94928F1F8119C5DC528EBD779915EA6BE`,
  the BIN was copied through ST-LINK mass storage `D:` / `NOD_G474RE`, and
  no `FAIL.TXT` was present after copy. User-reported readings were
  `CN3_1` through `CN3_6 = 0 V`, `CN3_13 / nFAULT = 3.3 V`,
  `CN3_14 / 3V3 = 3.3 V`, and `REG12 = 0 V`; driver-input stop rule was not
  hit. This is USB-only runtime evidence only and does not open 24 V,
  Gate PWM, Motor Pilot, Motor Profiler, motor connection, Hall closed loop,
  sensorless operation, power-stage readiness, or motor readiness.
- Current manual gate-test USB-only runtime lockout execution entry:
  `stdrive101_manual_gate_test_usb_only_runtime_lockout_execution_entry_2026-06-20.md`
  records the user request `USB-only lockout runtime 检查`, the user-confirmed
  physical boundary (`HSPY / 24 V OFF`, physically disconnected,
  `VS / 24V_FUSED < 1 V`, motor disconnected, wake stimulus removed,
  Motor Pilot / Profiler closed, no abnormal heat / smell / sound), and the
  matched candidate ELF hash
  `87BF3F7A28949F8DB654927292083609E52AB46C511CB6191D03B280DBFFE9B6`.
  It opens exactly one USB-only lockout flash / run measurement pass. It does
  not open 24 V, Gate PWM, Motor Pilot, Motor Profiler, motor connection,
  Hall closed loop, sensorless operation, power-stage readiness, or motor
  readiness. The next checkpoint is a separate runtime result record after
  direct measurements are reported.
- Current manual gate-test USB-only runtime lockout phase-gate plan:
  `stdrive101_manual_gate_test_usb_only_runtime_lockout_phase_gate_plan_2026-06-20.md`
  records a phase-gate plan only. It accepts the linked-image build-only
  record as image-boundary evidence and names later USB-only runtime
  preconditions: explicit user execution request, matching ELF hash or a
  replacement build-only record, HSPY / 24 V OFF and disconnected,
  `VS / 24V_FUSED < 1 V`, motor disconnected, wake resistor removed,
  Motor Pilot / Profiler closed, and no normal MCSDK ingress. It also defines
  a measurement table and stop rules. It opens no flash, no Run / Debug, no
  USB runtime execution, no 24 V, no Gate PWM, no Motor Pilot, no Motor
  Profiler, no motor connection, and no readiness claims. The next possible
  checkpoint is a later separate USB-only runtime execution record only if the
  user explicitly asks to execute it and the preconditions are still true.
- Current manual gate-test linked-image build-only record:
  `stdrive101_manual_gate_test_linked_image_build_only_record_2026-06-20.md`
  records Gate D build-only evidence for the isolated lockout image. The
  repo-local CMake package now adds linked target
  `stdrive101_gate_lockout_image`, configured as `Generic` / `arm` with
  STM32Cube GNU Arm GCC `14.3.1` and Ninja. The build produced ELF and MAP
  artifacts under `.tmp/manual_gate_test_lockout_linked_image/` and recorded
  sizes, hashes, memory usage, key symbols, and clean forbidden source / ELF /
  MAP screens. This is build-only evidence only: it opens no flash, no Run /
  Debug, no USB runtime execution, no 24 V, no Gate PWM, no Motor Pilot, no
  Motor Profiler, no motor connection, and no readiness claims. The next
  allowed checkpoint is a separate USB-only runtime lockout phase-gate plan or
  review, not runtime execution.
- Current manual gate-test linked-image build-boundary plan:
  `stdrive101_manual_gate_test_linked_image_build_boundary_plan_2026-06-20.md`
  records Gate D boundary planning only. It carries forward the lockout source
  hashes and object-only build pass, fixes future link candidate inputs to the
  repo-local `nucleo_g474re_baseline` startup, linker script,
  `system_stm32g4xx.c`, `syscalls.c`, and `sysmem.c`, names the future target
  `stdrive101_gate_lockout_image`, and requires ELF plus MAP as minimum future
  build-only artifacts. It does not create a linked image, edit CMake, run a
  build, flash, Run / Debug, execute USB runtime, authorize 24 V, Gate PWM,
  Motor Pilot, Motor Profiler, motor connection, or readiness claims. The next
  allowed checkpoint is a separate linked-image build-only record for the
  lockout image, still without runtime execution.
- Current manual gate-test USB-only runtime lockout preparation:
  `stdrive101_manual_gate_test_usb_only_runtime_lockout_prep_2026-06-20.md`
  records Gate C preparation only. It carries forward the object-only build
  pass, source hashes, object hashes, future linked-image boundary, USB-only
  no-24V physical boundary, expected future pin readings, stop rules, and a
  user table for a later approved runtime. It does not open flash, Run /
  Debug, USB runtime execution, 24 V, Gate PWM, Motor Pilot, Motor Profiler,
  motor connection, or readiness claims. The next allowed checkpoint is a
  linked-image build-boundary plan or build-only record for the lockout image,
  still without runtime execution.
- Current manual gate-test lockout object-only build pass:
  `stdrive101_manual_gate_test_lockout_object_build_pass_2026-06-20.md`
  records a successful no-power object-only build of
  `stdrive101_gate_lockout_objects` using STM32Cube GNU Arm GCC `14.3.1` and
  Ninja `1.13.2`. The target produced only `gate_test_lockout.c.obj` and
  `main_lockout.c.obj`; no lockout ELF / HEX / BIN / MAP linked firmware image
  was produced. This does not open flash, Run / Debug, 24 V, Gate PWM, Motor
  Pilot, Motor Profiler, motor connection, or readiness claims.
- Current manual gate-test lockout object-only target:
  `stdrive101_manual_gate_test_lockout_object_target_2026-06-20.md` records a
  repo-local CMake object-library target for the isolated lockout package. It
  compiles only `gate_test_lockout.c` and `main_lockout.c` object files and
  has no ELF / HEX / BIN link target. `REPO_ROOT` was corrected and CMSIS
  headers resolve statically. CMake configure could not complete in the
  sandbox because external Ninja was blocked; the escalation path returned
  503, so no object build pass is claimed. No flash, Run / Debug, 24 V,
  Gate PWM, or motor action is authorized.
- Current manual gate-test lockout source package:
  `stdrive101_manual_gate_test_lockout_source_package_2026-06-20.md` records
  the repo-local isolated lockout source under
  `manual_gate_test_lockout_build_only_2026-06-20/`. It forces the six
  STDRIVE101 MCU-facing driver inputs low as GPIO outputs, keeps
  `PB12 / nFAULT` as input, clears TIM1 `CCER`, clears TIM1 `MOE` and
  automatic output, and leaves TIM1 break enabled. Static source grep found no
  forbidden normal MCSDK start / command-ingress / output-enable symbols in
  `Src` and `Inc`. This is source-package evidence only: no embedded build
  target yet, no flash, no Run / Debug, no 24 V, no Gate PWM, and no motor.
- Current manual gate-test firmware plan:
  `stdrive101_manual_gate_test_firmware_plan_no_power_2026-06-20.md` records
  the no-power-only plan for a future isolated lockout firmware path. Normal
  MCSDK start remains blocked. Future gate-test work must avoid
  `MC_StartMotor1`, `MCI_START`, PC13 start/stop, MCP command ingress,
  Motor Pilot, Hall closed-loop paths, speed-loop paths, and motor connection.
  This plan opens no firmware edit, build, flash, Run / Debug, 24 V, Gate PWM,
  Motor Pilot, Motor Profiler, or motor action.
- Current R3_2 source closure:
  `stdrive101_r3_2_mcsdk_pwm_output_path_source_closure_2026-06-20.md`
  records the exact local Workbench MCSDK source file and hash for
  `r3_2_g4xx_pwm_curr_fdbk.c`. The review confirms `R3_2_TurnOnLowSides()`
  treats `0` ticks as low-sides ON and calls `LL_TIM_EnableAllOutputs(TIMx)`;
  the generated state machine calls `LL_TIM_DisableBRK(TIM1)` before that
  low-side boot-cap action. Normal generated MCSDK start remains blocked for
  powered PWM. The next allowed checkpoint is a no-power-only manual gate-test
  firmware plan.
- Current PWM/gate-test source review:
  `stdrive101_pwm_gate_test_no_power_source_review_2026-06-20.md` records the
  no-power source/configuration decision that the static hardware screen is
  clean for planning only. Generated MCSDK direct PWM remains blocked because
  runtime start-command ingress exists, the start-command path reaches
  low-side / PWM routines, the exact external `r3_2_g4xx_pwm_curr_fdbk.c`
  implementation is not packet-local, TIM1 BKIN / `nFAULT` polarity is not
  closed, generated Hall pins do not match the accepted PCB2 Hall route, and
  the generation log has PWM / BKIN / MotorControl invalid-parameter messages.
  No motor, PWM output, Motor Pilot, Motor Profiler, firmware Flash / Run /
  Debug, power-stage readiness, or motor readiness is authorized.
- Current PCB2 no-power DMM result:
  `pcb2_no_power_dmm_continuity_short_check_result_2026-06-19.md` records the
  user-reported table as `通` for `CN3_10-PA0`, `CN3_11-PA1`,
  `CN3_12-PB4`, `CN3_2-PB3`, `CN3_14-3V3`, `CN3_15-GND`, and
  `CN3_13-PB12`, with all requested rail, signal-to-rail, and Hall-pair
  short checks reported as `不通`. Raw ohm values were not provided. This
  closes the immediate no-power DMM-table blocker for planning only; it does
  not authorize firmware implementation, flash, 24 V, motor connection,
  Gate PWM, Motor Pilot, Motor Profiler, Hall closed loop, sensorless
  operation, power-stage readiness, or motor readiness.
- Current post-DMM software Hall boundary:
  `software_hall_code_entry_boundary_after_dmm_2026-06-19.md` defines the
  next allowed no-power document-side work for `PA0 / PA1 / PB4`: exact future
  debug-only file list, GPIO pull / EXTI trigger policy review,
  timestamp-source criteria, low-frequency debug snapshot route, no-power
  build checklist, and rollback checklist. It does not create firmware or open
  MCSDK hooks.
- Current hardware handoff: the 2026-06-19 no-power and static checks have
  reached the execution-gate decision for a bounded STDRIVE101 single-input
  wake diagnostic. If the user says `开始单输入唤醒诊断` or `单输入唤醒`, this means
  `CN3_14 / 3V3 -> 10 kohm series resistor -> CN3_2 / LIN1` with motor
  disconnected and HSPY `24 V / 0.2 A`. It does not mean Codex mobile wakeup,
  service wakeup, or automation wakeup. Before giving steps, read
  `stdrive101_reg12_single_input_wake_plan_2026-06-19.md`,
  `stdrive101_reg12_wake_official_web_review_2026-06-19.md`, and
  `out1_output_node_no_power_short_check_result_2026-06-19.md`.
- Current single-input wake baseline result:
  `stdrive101_reg12_single_input_wake_baseline_result_2026-06-19.md` records
  the user-reported pre-stimulus baseline as `CV`, `0.036 A`,
  `VS / 24V_FUSED = 24 V`, `CN3_14 / 3V3 = 3.3 V`,
  `CN3_13 / nFAULT = 3.3 V`, and `REG12 = 0.33 V`. This closes only the
  baseline condition.
- Current single-input wake result:
  `stdrive101_reg12_single_input_wake_fault_result_2026-06-19.md` records the
  user-reported bounded diagnostic with `CN3_14 / 3V3 -> 10 kohm ->
  CN3_2 / LIN1`: HSPY `CV`, `0.046 A`, `LIN1 = 3 V`, `nFAULT = 0 V`,
  `REG12 = 12 V`, and post-off `VS / 24V_FUSED = 0 V`. The diagnostic
  observed `REG12` rising, but did not pass as a clean wake condition because
  `nFAULT` was low. No retry or alternate input stimulus is allowed before
  fault-cause review.
- Current single-input wake retest result:
  `stdrive101_reg12_single_input_wake_retest_clean_result_2026-06-20.md`
  records the user-reported bounded retest after gate-source pulldown rework:
  HSPY `CV`, `0.048 A`, `LIN1 = 3.13 V`, `nFAULT = 3.3 V`, and
  `REG12 = 12 V`. Recovery after removing the `10 kohm` stimulus and returning
  all inputs low was `CV`, `0.045 A`, `nFAULT = 3.3 V`, and
  `REG12 = 0.33 V`. The previous `nFAULT = 0 V` wake blocker was not
  reproduced in this bounded retest. This is not PWM validation, motor
  validation, power-stage readiness, or motor readiness.
- Current all-inputs-low static recheck result:
  `stdrive101_all_inputs_low_static_recheck_result_2026-06-20.md` records the
  user-reported post-retest static state after the `10 kohm` wake stimulus was
  removed: HSPY `CV`, current about `0.045 A`, `CN3_1` through `CN3_6` all
  close to `0 V`, `CN3_14 / 3V3 = 3.3 V`, `CN3_13 / nFAULT = 3.3 V`, and
  `REG12 = 0.3 V`. This confirms standby-like recovery after the clean wake
  retest, but it does not prove MCU reset/default GPIO behavior, PWM safety,
  gate waveforms, motor behavior, power-stage readiness, or motor readiness.
- Current USB-only MCU default input state result:
  `stdrive101_usbonly_mcu_default_input_state_result_2026-06-20.md` records
  the user-reported no-24V USB/ST-LINK check: `CN3_1` through `CN3_6` all
  close to `0 V`, with `P13 = 3.3 V` and `P14 = 3.3 V` interpreted from the
  requested table as `CN3_13 / nFAULT = 3.3 V` and `CN3_14 / 3V3 = 3.3 V`.
  No MCU-facing STDRIVE101 input was reported high in the USB-only state. This
  is not PWM validation, firmware runtime validation, motor validation,
  power-stage readiness, or motor readiness.
- Current USB + 24 V static recheck result:
  `stdrive101_usb24_static_recheck_result_2026-06-20.md` records the
  user-reported static check with USB/ST-LINK connected and 24 V applied:
  HSPY `CV`, current about `0.045 A`, `CN3_1` through `CN3_6` all close to
  `0 V`, `CN3_14 / 3V3 = 3.3 V`, `CN3_13 / nFAULT = 3.3 V`, and
  `REG12 = 0.3 V`. This closes the immediate static pre-PWM screen, but it is
  not PWM validation, firmware runtime validation, gate waveform evidence,
  motor validation, power-stage readiness, or motor readiness.
- Current nFAULT cause review:
  `stdrive101_single_input_wake_nfault_cause_review_2026-06-20.md` records
  the no-power/source review. It ranks VDS monitoring after the `LIN1`
  low-side command as the primary review target, with REG12 sequence /
  accidental external REG12 tie, CP comparator, thermal shutdown, and
  external nFAULT pull-down as secondary targets. Next checkpoint is no-power
  DMM on `LIN1` and `nFAULT`, or a marked source packet for `SCREF`, `CP`,
  `REG12`, and `OUT1`.
- Current nFAULT no-power DMM result:
  `stdrive101_nfault_no_power_dmm_result_2026-06-20.md` records
  `LIN1-3V3 = 66 kohm no beep`, `LIN1-GND = 60 kohm no beep`,
  `nFAULT-3V3 = 5 kohm no beep`, and `nFAULT-GND = 10 kohm no beep`.
  This does not show a persistent CN3-side rail hard short on `LIN1` or
  `nFAULT`. VDS monitoring after the `LIN1` low-side command remains the
  primary review target; the next useful evidence is a marked source packet or
  confidently identified no-power protection-node checks.
- Current STDRIVE101 schematic marking:
  `stdrive101_fault_review_schematic_marking_2026-06-20.md` and the generated
  images under `hardware/schematic/annotated/` mark the source schematic's
  `CN8` / user's measured `CN3` route, `LIN1`, `nFAULT`, `CP`, `SCREF`,
  `REG12`, `OUT1`, `GHS1`, `GLS1`, Q2 low-side path, and ground domains.
  This is source-map evidence for the VDS-monitoring review only; it is not
  physical probe permission for unknown pads and does not open repeat powered
  wake, PWM, motor, or readiness.
- Current STDRIVE101 protection-node DMM result:
  `stdrive101_protection_nodes_no_power_dmm_result_2026-06-20.md` records
  `SCREF-3V3 = 12 kohm`, `SCREF-GND = 12 kohm`,
  `CP-GND = 1.54 Mohm` rising to about `2 Mohm` with no resistance-mode beep,
  `REG12-GND = 0.2 Mohm` rising to `0.28 Mohm`,
  `REG12-VS = 40 kohm`, `OUT1-GND = no beep`, and `OUT1-VS` diode mode `OL`
  both directions. Stable hard short is not indicated on `CP`, `REG12`, or
  `OUT1` in the reported rows, but the result does not prove the `nFAULT`
  cause. VDS low-side path remains the primary review target.
- Current STDRIVE101 gate-source pulldown rework result:
  `stdrive101_gate_source_pulldown_rework_result_2026-06-20.md` records
  final user-reported six-route readings after rework:
  `VS_OFF_V = 0 V`, `Q1_GS = 10 kohm`, `Q3_GS = 10 kohm`,
  `Q5_GS = 10 kohm`, `Q2_GS = 10 kohm`, `Q4_GS = 10 kohm`, and
  `Q6_GS = 10 kohm`, with `10k_removed = yes`. The previous gate-source
  pulldown anomaly branch is no longer indicated. The later bounded wake
  retest now records `nFAULT = 3.3 V`, but this still does not prove PWM,
  waveform, motor, Hall closed-loop, sensorless, power-stage, or motor
  readiness.
- The single-input wake branch now has a clean bounded retest result, but the
  project remains behind the no-motor / no-PWM boundary: no firmware PWM, no
  Motor Pilot, no Motor Profiler, no Hall closed-loop claim, no sensorless
  claim, and no power-stage or motor readiness claim.
- Current real-world blocker update: PCB2 is reported populated / in hand, the
  route is unchanged, and the 2026-06-19 no-power DMM summary is now recorded.
  After the STDRIVE101 clean wake, static recovery, USB-only default-state,
  and USB + 24 V static checks, the next work should be no-power firmware /
  source planning for a future explicit PWM/gate-test phase gate, not motor,
  PWM output, or Motor Pilot / Profiler.
- No-power build-only status: Debug build command completed with exit code `0`
  on 2026-05-27 for
  `QIANSAI_G474_STDRIVE101_FOC_P2`; this is local compile evidence only.
- Strategy: use ST MCSDK for the motor-control framework, keep Hall
  closed-loop as the safe fallback path, and treat SMO/PLL sensorless as a
  later stretch goal.
- Real-time boundary: STM32 owns FOC. ESP32-C3 displays, forwards, and alerts
  only.

## Current PCB2 Route

- Current Hall planning route: `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`.
- `PB3=LIN1` and is not current PCB2 Hall.
- `P14/P15=3V3/GND`.
- PCB2 populated status is now reported, and the 2026-06-19 no-power DMM
  summary records continuity for `IA/IB/IC -> PA0/PA1/PB4`, `PB3=LIN1`,
  `P14/P15=3V3/GND`, and `nFAULT->PB12`, plus no reported rail / signal /
  Hall-line hard shorts. The WP-030 no-power Hall mixed-sequence check is
  passed at L4.

## Current Software Hall State

- Host-side and document-side no-power software Hall preparation exists:
  state-machine rules, pseudocode, host model, golden vectors, MCSDK integration
  clues, firmware-entry checklist, GPIO/EXTI boundary review,
  timestamp-source review, debug-output route review, MCSDK firmware-integration boundary review, and MCSDK hook evidence request checklist.
- A Chinese-first no-power firmware-entry plan now exists at
  `software_hall_firmware_entry_plan_2026-05-28.md`. It locks
  `PA0/PA1/PB4` as the future software GPIO/EXTI Hall route, keeps
  `PB3=LIN1` out of Hall, defines the debug-only adapter layers, state-machine
  order, ISR limits, debug fields, MCSDK hard stops, and user checkpoint.
  Decision:
  `Software Hall firmware-entry plan / debug-only no-power boundary / no firmware implementation / no MCSDK hook / no Hall readiness`.
- A post-DMM code-entry boundary now exists at
  `software_hall_code_entry_boundary_after_dmm_2026-06-19.md`. It updates the
  entry path after the DMM summary and keeps the next work as document-side
  no-power planning only.
- The external Workbench project
  `C:\Users\gregrg\.st_workbench\projects\QIANSAI_G474_STDRIVE101_FOC_P2`
  exists and its generated `Src/`, `Inc/`, `cmake/`, and top-level build
  metadata are now archived as
  `packet_a_sources/2026-05-27_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot/`
  with a manifest, hash list, and source review.
- A read-only MCSDK speed / position feedback interface review now exists at
  `software_hall_mcsdk_speed_position_feedback_interface_review_2026-05-27.md`.
  It traces `HALL_M1`, `HALL_CalcAvrgMecSpeedUnit`, `STC_GetSpeedSensor`,
  `SPD_GetAvrgMecSpeedUnit`, and `SPD_GetElAngle`, and records that future
  software Hall must remain debug-only unless a separate reviewed
  `SpeednPosFdbk`-compatible component proposal is created.
- No-power build-only result now exists at
  `build_only_result_2026-05-27_qiansai_g474_stdrive101_foc_p2_debug.md`.
  It records `cmake --build ... --config Debug`, exit code `0`, `ninja: no
  work to do`, and `.elf` / `.map` artifacts from the external Workbench build
  directory.
- PR #5, `learning notes`, was reviewed and merged into `master` on
  2026-06-01 with merge commit
  `2b614b4aae4eb40a5b2a882c5f2252dadbe06079`. Its two added learning files
  record only L2 MCSDK Hall speed / position feedback concept evidence and do
  not claim MCSDK Hall closed-loop, Motor Profiler, power-board, motor, PWM,
  serial, or build validation.
- WP-030 software Hall processing-order transfer is now L4 at no-power
  mixed-sequence level. The next software-Hall learning risk is firmware-entry
  pseudocode discipline, not more sequence recall.
- These are no-power planning and host-model evidence only.
- They do not prove GPIO runtime behavior, MCSDK Hall integration, MCSDK hook
  readiness, DMM continuity, Hall closed-loop behavior, flash readiness, or
  powered readiness.
- The DMM table summary is now recorded for no-power planning only. It is not
  powered validation, firmware runtime proof, MCSDK hook readiness, Hall
  closed-loop behavior, or motor readiness.

## Current AI Architecture Work

- This repository now treats AI assistance as an evidence-first workflow:
  short context, grounded retrieval, one active task, explicit safety boundary,
  contract checks, and evidence records.
- `docs/00_project_truth/ai_architecture.md` is the architecture contract.
- AI Architecture v2 adds `tools/build_context_pack.py --mode ai_maintenance`
  for AI workflow maintenance handoffs.
- Project workflow maintenance now uses
  `tools/build_context_pack.py --mode workflow_maintenance` for automation,
  learning feedback, closeout checklist, definition-of-done, submission
  checklist, index, and tool-contract maintenance.
- Project Skill v2 is now a concise router at
  `codex_skills/stm32g474-foc-assistant/SKILL.md`, with one-level references
  for project navigation, no-power boundaries, learning feedback, and workflow
  maintenance.
- `tools/check_project_skill_install.py` now checks whether the installed user
  Skill matches the repo-local project Skill source.
- `tools/run_ai_maintenance_audit.py` now provides a consolidated no-power AI
  maintenance audit runner, with full and quick repo-only modes plus optional
  Markdown report output via `--write-report`. It records
  `git status --short` as dirty-worktree handoff evidence before
  `git diff --check`; the `git_status` step preserves full output even when
  other step output is tail-limited by `--max-output-chars`, and exposes a
  parsed `workspace_status` summary with `status_paths`, `path_groups`, and
  ordered `focus_groups`, plus a `handoff_review_queue` that names the review
  focus for each dirty-worktree group. It also exposes `contract_status` to
  distinguish contract errors from known review-lifecycle warnings and strict
  readiness, `readability_status` to separate guarded entry headers from
  broader legacy mojibake debt, plus `closeout_summary` for the top-level
  repo-maintenance closeout decision, dirty-worktree state, review-needed
  flag, and next review focus. This does not clean the worktree or validate
  hardware.
- `tools/check_ai_contracts.py` is the no-power workflow consistency checker.
  It checks entry files, safety phrases, task review lifecycle, UTF-8
  readability, index coverage, retrieval-eval coverage, project workflow
  contracts, and dangerous positive claims across project truth, workflow,
  Skill, no-power precheck, deliverable, interface, and learning text.
- The readable entry headers of `workflow/evidence_register.md` and
  `deliverables/submission_checklist.md` are now contract-checked. Broader
  legacy historical mojibake remains separate review work rather than a
  silent full-repair claim.
- Review lifecycle policy: Codex may leave `done + Review Required` warnings
  during implementation closeout. User review clears strict warnings; Codex
  must not silently mark the task `reviewed` just to make strict mode pass.
- `retrieval_eval/queries.json` covers dual-teacher guard, current PCB2 Hall
  route, DMM pending/no-power boundary, ACTIVE_TASK review lifecycle, and ESP32
  real-time boundary, plus workflow closeout, automation no-write, learning
  feedback, repo-maintenance DoD, project Skill v2 router, and project Skill
  install drift cases, plus the AI maintenance audit runner case.
- `tools/search_local_v2.py --eval` is source-finding regression evidence only,
  not hardware validation.
- Dual-teacher concept-only role guard is now explicit: ChatGPT teaches pure
  theory/concept turns, while Codex provides the ChatGPT prompt, reviews and
  records returned learning evidence, and keeps repo-side engineering work.
- The AI architecture doc now also defines a structured subagent communication
  protocol with hierarchical task decomposition, context filtering, a summary gate,
  and an old-flat-vs-new-filtered comparison. Subagent output is
  summarized before it reaches the main-agent decision loop.
- A three-hour optimization sprint report now exists at
  `workflow/three_hour_optimization_report_2026-06-17.md`. It records
  subagent roles, timestamped progress, mid-project review, Obsidian Chinese
  learning note enhancements, retrieval-maintainability changes, verification
  commands, and efficiency recommendations.

## Current Safety Boundary

Unless a later dated phase-gate decision explicitly opens the action:

- No flash.
- No 24V.
- No power-board connection.
- No motor connection.
- No Gate PWM output.
- No Motor Profiler run.
- No Motor Pilot run.
- No Hall closed-loop claim.
- No sensorless / SMO claim.
- No powered readiness, motor readiness, or power-stage readiness claim.

Current Packet A and software Hall artifacts may be accepted only as no-power
configuration, planning, host-model, or generated-source clues. They do not
prove PCB2 physical routing, continuity, protection behavior, firmware runtime
behavior, or powered behavior.

## Default Read Order

1. `AI_CONTEXT.md`
2. `workflow/CURRENT_SNAPSHOT.md`
3. `workflow/ACTIVE_TASK.md`
4. `docs/00_project_truth/project_context.md`
5. Mode-specific files named by `tools/build_context_pack.py`

Open `CURRENT_STATUS.md`, `workflow/evidence_register.md`, historical Packet
records, manuals, and generated directories only for concrete evidence,
hardware-safety, phase-gate, or implementation tasks.
