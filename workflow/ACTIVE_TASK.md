# Current Task

This is the current single task page. The newest hardware-adjacent record is
the STDRIVE101 gate-waveform candidate residual-voltage isolation result after
the candidate USB-only DMM result, candidate USB-only download result,
candidate USB-only download execution entry, candidate BIN artifact record,
neutral-wrapper 24V static scope baseline result, 24V static no-motor result,
residual-voltage isolation result, USB-only DMM completion result, partial
result, neutral-wrapper download result, neutral-wrapper download execution
entry, neutral-wrapper BIN artifact record, USB-only neutral-state phase-gate
plan, neutral-wrapper build-only record, neutral-wrapper source review,
Gate E3 USB-only neutral-state phase-gate plan, Gate E2 build-only record,
Gate E1 isolated source package review, Gate E0 gate-waveform image design
plan, and earlier manual gate-test records. It records the user-confirmed
residual-voltage isolation readings after USB / ST-LINK disconnect:
`VS / 24V_FUSED = 0 V` and `REG12 = 0 V`. The earlier candidate USB-only
`VS / 24V_FUSED = 2 V` reading cleared after USB disconnect, so persistent VS
backfeed is not indicated in this candidate isolation check and the immediate
residual-voltage blocker is cleared only. This opens no Run / Debug, no 24 V
command from this record, no Gate PWM output, no Motor Pilot, no Motor
Profiler, no motor connection, power-stage readiness, or motor readiness claim.

## Current 2026-06-21 STDRIVE101 Gate-Waveform Candidate Residual-Voltage Isolation Result

- Task:
  `TASK-2026-06-21-stdrive101-gate-waveform-candidate-residual-voltage-isolation-result`.
- Evidence:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-CANDIDATE-RESIDUAL-VOLTAGE-ISOLATION-RESULT-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_candidate_residual_voltage_isolation_result_2026-06-21.md`.
- Prior candidate USB-only DMM result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_candidate_usb_only_dmm_result_2026-06-21.md`.
- Isolation setup:
  USB / ST-LINK disconnected; HSPY / 24 V OFF and physically disconnected;
  motor disconnected; no `10 kohm` wake resistor or LIN1 stimulus installed;
  DMM black probe on GND.
- User-confirmed isolation readings:
  `VS / 24V_FUSED = 0 V` and `REG12 = 0 V`.
- Decision:
  `STDRIVE101 gate-waveform candidate residual-voltage isolation result /
  USB-STLINK disconnected / HSPY 24 V off and physically disconnected / motor
  disconnected / no 10 kohm wake resistor or LIN1 stimulus installed /
  user-confirmed VS / 24V_FUSED = 0 V / user-confirmed REG12 = 0 V / earlier
  candidate USB-only VS / 24V_FUSED = 2 V cleared after USB disconnect /
  persistent VS backfeed not indicated in this candidate isolation check /
  residual-voltage blocker cleared only / next checkpoint may only be a
  separate candidate 24 V static no-motor phase-gate or execution entry after
  fresh preconditions / no Run Debug / no 24 V command from this record / no
  Gate PWM output / no Motor Pilot / no Motor Profiler / no motor connection /
  no powered-drive readiness`.
- Boundary:
  the immediate candidate residual-voltage blocker is cleared only. This does
  not validate 24 V behavior, Gate PWM output, Motor Pilot, Motor Profiler,
  motor behavior, power-stage readiness, or motor readiness.
- Next checkpoint:
  do not repeat residual-voltage isolation unless the physical state, image,
  wiring, or measured value changes. The next engineering checkpoint may only
  be a separate candidate 24 V static no-motor phase-gate or execution entry
  with fresh preconditions, current limit, measurement points, stop rules, and
  rollback. Do not connect a motor or use Run / Debug, Motor Pilot, Motor
  Profiler, Gate PWM output, or a 24 V command from this result.

## Current 2026-06-21 STDRIVE101 Gate-Waveform Candidate USB-Only DMM Result

- Task:
  `TASK-2026-06-21-stdrive101-gate-waveform-candidate-usbonly-dmm-result`.
- Evidence:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-CANDIDATE-USBONLY-DMM-RESULT-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_candidate_usb_only_dmm_result_2026-06-21.md`.
- Prior download result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_candidate_usb_only_download_result_2026-06-21.md`.
- User-reported readings:
  `CN3_1` through `CN3_6 = 0 V`; `CN3_13 = 3 V`;
  `CN3_14 = 3 V`; `VS / 24V_FUSED = 2 V`; `REG12 = 0.3 V`.
  Board heat / smell / sound / reset-loop status was not reported in this
  latest row.
- Decision:
  `STDRIVE101 gate-waveform candidate USB-only DMM result / user-reported
  CN3_1 through CN3_6 all 0 V / user-reported CN3_13 = 3 V / user-reported
  CN3_14 = 3 V / user-reported VS / 24V_FUSED = 2 V / user-reported
  REG12 = 0.3 V / board heat smell sound reset-loop status not reported in
  this latest row / six driver-input stop-rule not hit / VS residual-voltage
  boundary is active because VS / 24V_FUSED is above the prior <1 V USB-only
  boundary / USB-only DMM result is not a pass for upward hardware progression
  / no Run Debug / no 24 V command / no Gate PWM output / no Motor Pilot / no
  Motor Profiler / no motor connection / no powered-drive readiness`.
- Boundary:
  the six MCU-facing driver inputs stayed low in this USB-only DMM table, so
  the six-input stop-rule was not hit. The result still blocks upward
  progression because `VS / 24V_FUSED = 2 V` is above the prior `< 1 V`
  USB-only residual-voltage boundary. The latest row also does not include
  board abnormal-condition status.
- Next checkpoint:
  superseded by the later waveform candidate residual-voltage isolation result,
  which records `VS / 24V_FUSED = 0 V` and `REG12 = 0 V` after USB / ST-LINK
  disconnect. Do not connect a motor or use Run / Debug, Motor Pilot, Motor
  Profiler, Gate PWM output, or a 24 V command from this result.

## Current 2026-06-21 STDRIVE101 Gate-Waveform Candidate USB-Only Download Result

- Task:
  `TASK-2026-06-21-stdrive101-gate-waveform-candidate-usbonly-download-result`.
- Evidence:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-CANDIDATE-USBONLY-DOWNLOAD-RESULT-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_candidate_usb_only_download_result_2026-06-21.md`.
- Execution entry:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_candidate_usb_only_download_execution_entry_2026-06-21.md`.
- User authorization:
  `允许复制 candidate BIN 到 D:`.
- Candidate BIN:
  `.tmp/manual_gate_waveform_build_only_2026-06-21_clean/stdrive101_gate_waveform_candidate_image.bin`,
  size `1852` bytes, SHA256
  `362C510E4F682751F0721B54F306F6E144951F03F9FF875E68E238D92A29BB31`.
- Copy result:
  `D:` was `NOD_G474RE`; `D:\FAIL.TXT` was absent before copy; the candidate
  BIN was copied once to `D:\stdrive101_gate_waveform_candidate_image.bin`;
  after a short wait `D:` was still `NOD_G474RE`, `D:\FAIL.TXT` was absent,
  and the target BIN was no longer visible, consistent with ST-LINK
  mass-storage consumption. `DETAILS.TXT` reported `Version: V3J17M10` and
  `Build: Oct 17 2025 15:12:06`.
- Decision:
  `STDRIVE101 gate-waveform candidate USB-only download result / candidate BIN
  copied once to D: NOD_G474RE by ST-LINK mass storage / source BIN SHA256
  362C510E4F682751F0721B54F306F6E144951F03F9FF875E68E238D92A29BB31 /
  no FAIL.TXT before copy / no FAIL.TXT after copy / target BIN not retained
  on D: after copy, consistent with ST-LINK mass-storage consumption /
  candidate board image download result only / no CN3 DMM post-download result
  yet / no measured waveform result yet / no Run Debug / no 24 V command / no
  Motor Pilot / no Motor Profiler / no motor connection / no powered-drive
  readiness`.
- Boundary:
  board image is now treated as the waveform candidate image for the next
  bounded checks. Because the candidate image calls
  `gate_waveform_candidate_run_once()` once after reset and then holds idle
  low, this record does not prove absence of a boot-time output transition and
  does not prove waveform correctness. It also opens no 24 V, Run / Debug,
  Motor Pilot, Motor Profiler, motor connection, power-stage readiness, or
  motor readiness.
- Next checkpoint:
  superseded by the later waveform candidate residual-voltage isolation result,
  which clears the immediate residual-voltage blocker only and changes the
  live checkpoint to a separate candidate 24 V static no-motor phase-gate or
  execution entry. Do not connect a motor or use Run / Debug, Motor Pilot, or
  Motor Profiler from this download result.

## Current 2026-06-21 STDRIVE101 Gate-Waveform Candidate BIN Artifact Record No-Power

- Task:
  `TASK-2026-06-21-stdrive101-gate-waveform-candidate-bin-artifact-record-no-power`.
- Evidence:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-CANDIDATE-BIN-ARTIFACT-RECORD-NO-POWER-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_candidate_bin_artifact_record_no_power_2026-06-21.md`.
- Generated BIN:
  `.tmp/manual_gate_waveform_build_only_2026-06-21_clean/stdrive101_gate_waveform_candidate_image.bin`,
  size `1852` bytes, SHA256
  `362C510E4F682751F0721B54F306F6E144951F03F9FF875E68E238D92A29BB31`.
- Decision:
  `STDRIVE101 gate-waveform candidate BIN artifact record no-power / Gate E2
  waveform candidate linked ELF converted to downloadable BIN / converter
  output validated against the prior neutral-wrapper objcopy BIN / candidate
  ELF SHA256 10BA818730E259AEBA8A5C5E5C96CFBA32FCB90AAA4136B775022B9D69ADCE7C
  / candidate MAP SHA256
  170EA77C566F98CF9EF2AC88F76B154238A5404DC705AAE3917BEAE7C1503D4C /
  candidate BIN SHA256
  362C510E4F682751F0721B54F306F6E144951F03F9FF875E68E238D92A29BB31 /
  candidate BIN size 1852 bytes / retained MAP symbol
  gate_waveform_candidate_run_once at 0x080005bc / no forbidden normal-MCSDK
  MAP symbols found in the checked screen / BIN artifact only / no USB copy /
  no flash / no Run Debug / no 24 V execution / no Gate PWM output / no Motor
  Pilot / no Motor Profiler / no motor connection / no powered-drive
  readiness`.
- Boundary:
  downloadable BIN artifact only. It does not copy the BIN to ST-LINK mass
  storage, does not change the current board image, and does not execute a
  waveform window.
- Next checkpoint:
  only a separate waveform-candidate USB-only download execution entry after
  explicit user confirmation and authorization. Keep HSPY / 24 V OFF and the
  motor disconnected until then.

## Current 2026-06-21 STDRIVE101 Gate-Waveform Neutral-Wrapper 24V Static Scope Baseline Result

- Task:
  `TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-24v-static-scope-baseline-result`.
- Evidence:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-24V-STATIC-SCOPE-BASELINE-RESULT-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_neutral_wrapper_24v_static_scope_baseline_result_2026-06-21.md`.
- User-reported readings:
  oscilloscope ground on `CN3_15 / GND`; `CN3_1` / `CN3_2`,
  `CN3_3` / `CN3_4`, and `CN3_5` / `CN3_6` all observed as `0 V` straight
  lines; HSPY `CV` about `0.036 A`; `nFAULT = 3.3 V`; no board heat / smell /
  sound / reset-loop symptom.
- Decision:
  `STDRIVE101 gate-waveform neutral-wrapper 24V static scope baseline result /
  oscilloscope ground on CN3_15 GND / HSPY CV about 0.036 A / CN3_1 and CN3_2
  0 V straight lines / CN3_3 and CN3_4 same 0 V straight lines / CN3_5 and
  CN3_6 same 0 V straight lines / nFAULT remains 3.3 V / no board heat smell
  sound reset-loop reported / all six MCU-facing driver inputs static-low in
  this no-motor no-PWM baseline / no waveform output executed / no Run Debug /
  no Gate PWM output / no Motor Pilot / no Motor Profiler / no motor
  connection / no powered-drive readiness`.
- Boundary:
  static oscilloscope baseline only. It does not validate Gate PWM output,
  waveform correctness, Motor Pilot, Motor Profiler, motor behavior, Hall
  closed loop, sensorless operation, power-stage readiness, or motor readiness.
- Next checkpoint:
  turn HSPY output OFF after this baseline. The next engineering checkpoint
  may only be a separate no-motor, short-window, instrumented waveform
  execution entry with exact probe points, stop rules, and rollback. Do not
  connect the motor or run Motor Pilot / Profiler from this result.

## Current 2026-06-21 STDRIVE101 Gate-Waveform Neutral-Wrapper 24V Static No-Motor Result

- Task:
  `TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-24v-static-no-motor-result`.
- Evidence:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-24V-STATIC-NO-MOTOR-RESULT-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_neutral_wrapper_24v_static_no_motor_result_2026-06-21.md`.
- User-reported readings:
  HSPY `CV`, current `0.036 A`, `VS / 24V_FUSED = 24 V`,
  `CN3_1` through `CN3_6 = 0 V`, `CN3_13 / nFAULT = 3.3 V`,
  `CN3_14 / 3V3 = 3.3 V`, `REG12 = 0.2 V`, and no board heat / smell /
  sound / reset-loop symptom.
- Decision:
  `STDRIVE101 gate-waveform neutral-wrapper 24V static no-motor result /
  HSPY CV 0.036 A / VS 24V_FUSED = 24 V / CN3_1 through CN3_6 all 0 V /
  CN3_13 nFAULT = 3.3 V / CN3_14 3V3 = 3.3 V / REG12 = 0.2 V / no board
  heat smell sound reset-loop reported / six driver-input stop-rule not hit /
  nFAULT high in static no-motor state / bounded 24 V static no-motor check
  clean for this table only / no Run Debug / no Gate PWM output / no Motor
  Pilot / no Motor Profiler / no motor connection / no powered-drive
  readiness`.
- Boundary:
  bounded 24 V static no-motor measurement evidence only. It does not
  validate Gate PWM output, Motor Pilot, Motor Profiler, motor behavior, Hall
  closed loop, sensorless operation, power-stage readiness, or motor
  readiness.
- Next checkpoint:
  superseded for the live checkpoint by the later 24V static scope baseline
  result. Do not connect the motor or start PWM from this result.

## Current 2026-06-21 STDRIVE101 Gate-Waveform Neutral-Wrapper Residual-Voltage Isolation Result

- Task:
  `TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-residual-voltage-isolation-result`.
- Evidence:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-RESIDUAL-VOLTAGE-ISOLATION-RESULT-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_neutral_wrapper_residual_voltage_isolation_result_2026-06-21.md`.
- Prior blocker:
  the USB-only DMM completion result reported `VS / 24V_FUSED = 2 V`,
  `REG12 = 0.5 V`, and no board heat / smell / sound / reset-loop symptom.
- Isolation setup:
  USB / ST-LINK disconnected; HSPY / 24 V OFF and physically disconnected;
  motor disconnected; no `10 kohm` wake resistor or LIN1 stimulus installed;
  DMM black probe on GND.
- User-reported isolation readings:
  `VS / 24V_FUSED = 0 V` and `REG12 = 0 V`.
- Decision:
  `STDRIVE101 gate-waveform neutral-wrapper residual-voltage isolation result /
  USB-STLINK disconnected / HSPY 24 V off and physically disconnected / motor
  disconnected / no 10 kohm wake resistor or LIN1 stimulus installed /
  user-reported VS / 24V_FUSED = 0 V / user-reported REG12 = 0 V / earlier
  USB-only VS / 24V_FUSED = 2 V cleared after USB disconnect / persistent VS
  backfeed not indicated in this isolation check / residual-voltage isolation
  blocker cleared only / no Run Debug / no 24 V execution / no Gate PWM output /
  no Motor Pilot / no Motor Profiler / no motor connection / no powered-drive
  readiness`.
- Boundary:
  residual-voltage isolation result only. It clears the immediate
  residual-voltage blocker raised by the earlier USB-only `VS / 24V_FUSED = 2 V`
  reading, but does not validate 24 V behavior, Gate PWM output, Motor Pilot,
  Motor Profiler, motor behavior, Hall closed loop, sensorless operation,
  power-stage readiness, or motor readiness.
- Next checkpoint:
  superseded for the live checkpoint by the later 24V static no-motor result.
  Do not repeat the residual-voltage isolation check unless the physical state,
  image, wiring, or measured value changes. Do not connect the motor or start
  PWM from this result.

## Current 2026-06-21 STDRIVE101 Gate-Waveform Neutral-Wrapper USB-Only DMM Completion Result

- Task:
  `TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-usbonly-dmm-completion-result`.
- Evidence:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-USBONLY-DMM-COMPLETION-RESULT-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_neutral_wrapper_usb_only_dmm_completion_result_2026-06-21.md`.
- Completed DMM table:
  carried forward `CN3_1` through `CN3_6 = 0 V`, `P13 = 3.3 V`, and
  `P14 = 3.3 V`; newly reported `VS / 24V_FUSED = 2 V`,
  `REG12 = 0.5 V`, and no board heat / smell / sound / reset-loop symptom.
- Decision:
  `STDRIVE101 gate-waveform neutral-wrapper USB-only DMM completion result /
  user-reported CN3_1 through CN3_6 all 0 V / user-reported P13 = 3.3 V and
  P14 = 3.3 V, recorded as the requested CN3_13 / nFAULT and CN3_14 / 3V3
  labels if P13/P14 map to that header / user-reported VS / 24V_FUSED = 2 V /
  user-reported REG12 = 0.5 V / no board heat smell sound reset-loop reported /
  six driver-input stop-rule not hit / VS residual boundary is not clean
  because VS / 24V_FUSED is above the prior <1 V USB-only boundary / USB-only
  DMM table complete but not a pass for upward hardware progression / no Run
  Debug / no 24 V / no Gate PWM output / no Motor Pilot / no Motor Profiler /
  no motor connection / no powered-drive readiness`.
- Boundary:
  completed USB-only DMM measurement evidence only. The completed table is not
  a clean pass for upward hardware progression because `VS / 24V_FUSED = 2 V`
  is above the prior `< 1 V` USB-only boundary. It does not open 24 V, Run /
  Debug, Gate PWM output, Motor Pilot, Motor Profiler, motor connection, Hall
  closed loop, sensorless operation, power-stage readiness, or motor
  readiness.
- Next checkpoint:
  superseded for the live checkpoint by the later residual-voltage isolation
  result, which records `VS / 24V_FUSED = 0 V` and `REG12 = 0 V` after
  USB / ST-LINK disconnect. Do not ask for another residual-voltage repeat
  unless the physical state, image, wiring, or measured value changes.

## Current 2026-06-21 STDRIVE101 Gate-Waveform Neutral-Wrapper USB-Only DMM Partial Result

- Task:
  `TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-usbonly-dmm-partial-result`.
- Evidence:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-USBONLY-DMM-PARTIAL-RESULT-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_neutral_wrapper_usb_only_dmm_partial_result_2026-06-21.md`.
- User-reported readings:
  `CN3_1` through `CN3_6` are all `0 V`; `P13 = 3.3 V`; `P14 = 3.3 V`.
  `P13` and `P14` are recorded against the requested `CN3_13 / nFAULT` and
  `CN3_14 / 3V3` rows using the same header-label mapping as the prior
  USB-only table.
- Decision:
  `STDRIVE101 gate-waveform neutral-wrapper USB-only DMM partial result /
  user-reported CN3_1 through CN3_6 all 0 V / user-reported P13 = 3.3 V and
  P14 = 3.3 V, recorded as the requested CN3_13 / nFAULT and CN3_14 / 3V3
  labels if P13/P14 map to that header / six driver-input stop-rule not hit /
  VS / 24V_FUSED not reported in this partial record / REG12 not reported /
  board heat smell sound reset-loop status not reported / partial USB-only
  DMM evidence only / no full DMM neutral-state pass / no Run Debug / no 24 V /
  no Gate PWM output / no Motor Pilot / no Motor Profiler / no motor
  connection / no powered-drive readiness`.
- Boundary:
  partial USB-only DMM measurement evidence only. This result does not contain
  `VS / 24V_FUSED`, `REG12`, or board abnormal-condition status. It does not
  open 24 V, Run / Debug, Gate PWM output, Motor Pilot, Motor Profiler, motor
  connection, Hall closed loop, sensorless operation, power-stage readiness,
  or motor readiness.
- Next checkpoint:
  superseded for the live checkpoint by the later DMM completion result, which
  reports `VS / 24V_FUSED = 2 V`, `REG12 = 0.5 V`, and no board abnormal
  symptom. The live checkpoint is superseded by the later residual-voltage
  isolation result.

## Current 2026-06-21 STDRIVE101 Gate-Waveform Neutral-Wrapper USB-Only Download Result

- Task:
  `TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-usbonly-download-result`.
- Evidence:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-USBONLY-DOWNLOAD-RESULT-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_neutral_wrapper_usb_only_download_result_2026-06-21.md`.
- Candidate image:
  `.tmp/gwnw_build_2026-06-21_clean/stdrive101_gate_waveform_neutral_wrapper_image.elf`
  SHA256 `C47C02D379DC5312095DF786BF8C99B58D42323AD9227D0903BCB8C98AAD9591`;
  BIN SHA256
  `CA2A42F2F83C42EA9E7BEC628BD8656A422DBE767CFFD5A5865BE781603D3D71`.
- Decision:
  `STDRIVE101 gate-waveform neutral-wrapper USB-only download result /
  neutral-wrapper BIN copied once to D: NOD_G474RE by ST-LINK mass storage /
  source BIN SHA256 CA2A42F2F83C42EA9E7BEC628BD8656A422DBE767CFFD5A5865BE781603D3D71 /
  no FAIL.TXT before copy / no FAIL.TXT after copy / target BIN not retained
  on D: after copy, consistent with ST-LINK mass-storage consumption /
  download result only / no DMM neutral-state measurement result yet / no
  Run Debug / no 24 V / no Gate PWM output / no Motor Pilot / no Motor
  Profiler / no motor connection / no powered-drive readiness`.
- Boundary:
  USB-only mass-storage download result only. This record does not contain
  the CN3 / REG12 DMM neutral-state result. It does not open 24 V, Run /
  Debug, Gate PWM output, Motor Pilot, Motor Profiler, motor connection, Hall
  closed loop, sensorless operation, power-stage readiness, or motor readiness.
- Next checkpoint from this historical download record:
  superseded for the live checkpoint by the later USB-only DMM partial result,
  which records `CN3_1` through `CN3_6`, `P13`, and `P14`. The remaining
  live checkpoint is only `VS / 24V_FUSED`, `REG12`, and board heat / smell /
  sound / reset-loop status. If any later recheck of `CN3_1` through `CN3_6`
  is stably above `0.3 V`, stop, keep 24 V disconnected, and record the raw
  reading.

## Current 2026-06-21 STDRIVE101 Gate-Waveform Neutral-Wrapper USB-Only Download Execution Entry

- Task:
  `TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-usbonly-download-execution-entry`.
- Evidence:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-USBONLY-DOWNLOAD-EXECUTION-ENTRY-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_neutral_wrapper_usb_only_download_execution_entry_2026-06-21.md`.
- User request:
  `现在仍是 USB-only，24V 断开，电机断开，允许复制 neutral-wrapper BIN 到 D:`.
- Boundary:
  opened exactly one USB-only mass-storage BIN copy to `D:\NOD_G474RE`.
  It did not open Run / Debug, 24 V, Gate PWM output, Motor Pilot, Motor
  Profiler, motor connection, power-stage readiness, or motor readiness.

## Current 2026-06-21 STDRIVE101 Gate-Waveform Neutral-Wrapper BIN Artifact Record No-Power

- Task:
  `TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-bin-artifact-record-no-power`.
- Evidence:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-BIN-ARTIFACT-RECORD-NO-POWER-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_neutral_wrapper_bin_artifact_record_no_power_2026-06-21.md`.
- Generated BIN:
  `.tmp/gwnw_build_2026-06-21_clean/stdrive101_gate_waveform_neutral_wrapper_image.bin`,
  size `1044` bytes, SHA256
  `CA2A42F2F83C42EA9E7BEC628BD8656A422DBE767CFFD5A5865BE781603D3D71`.
- Boundary:
  artifact preparation record only; the later USB-only download result records
  the actual ST-LINK mass-storage copy. This artifact record itself opened no
  Run / Debug, 24 V, Gate PWM output, Motor Pilot, Motor Profiler, motor
  connection, power-stage readiness, or motor readiness.

## Current 2026-06-21 STDRIVE101 Gate-Waveform Neutral-Wrapper USB-Only Neutral-State Phase-Gate Plan

- Task:
  `TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-usbonly-neutral-state-phase-gate-plan`.
- Evidence:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-USBONLY-NEUTRAL-STATE-PHASE-GATE-PLAN-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_neutral_wrapper_usb_only_neutral_state_phase_gate_plan_2026-06-21.md`.
- Candidate image boundary:
  `.tmp/gwnw_build_2026-06-21_clean/stdrive101_gate_waveform_neutral_wrapper_image.elf`.
- Carried-forward hashes:
  ELF SHA256 `C47C02D379DC5312095DF786BF8C99B58D42323AD9227D0903BCB8C98AAD9591`;
  MAP SHA256
  `5FB24B2735EFFD402C26BDC3B0D267B26B06DC6522A6B5B5D876491BA9A42A83`.
- Decision:
  `STDRIVE101 gate-waveform neutral-wrapper USB-only neutral-state phase-gate
  plan / plan only / neutral-wrapper build-only record accepted as
  image-boundary evidence / neutral-wrapper ELF and MAP hashes carried forward
  / source-review packages remain source-review only and have no CMakeLists /
  build-only image uses main_neutral_wrapper.c and excludes old
  main_waveform_candidate.c / retained ELF symbol table has
  gate_waveform_neutral_wrapper_hold_idle_forever and has no
  gate_waveform_candidate_run_once / MAP lists gate_waveform_candidate_run_once
  only as a discarded zero-address input section from gate_waveform_candidate.c
  / future USB-only execution-entry must separately name transfer method,
  exact image hash, optional BIN hash if generated, measurement instrument,
  pre/post measurement table, rollback path, and stop rules / phase-gate plan
  only / no flash / no Run Debug / no USB runtime execution / no 24 V / no
  Gate PWM output / no Motor Pilot / no Motor Profiler / no motor connection /
  no powered-drive readiness`.
- Boundary:
  phase-gate planning only. This record performs no firmware flash, no Run /
  Debug, no USB runtime execution, no 24 V, no Gate PWM output, no Motor
  Pilot, no Motor Profiler, no motor connection, no Hall closed loop, no
  sensorless operation, and no power-stage or motor readiness claim.
- Next checkpoint:
  only a separate neutral-wrapper USB-only neutral-state execution-entry after
  explicit user request and freshly confirmed preconditions. Gate E4 remains
  closed.

## Current 2026-06-21 STDRIVE101 Gate-Waveform Neutral-Wrapper Build-Only Record No-Power

- Task:
  `TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-build-only-record-no-power`.
- Evidence:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-BUILD-ONLY-RECORD-NO-POWER-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_neutral_wrapper_build_only_record_no_power_2026-06-21.md`.
- Build-only package:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/manual_gate_waveform_neutral_wrapper_build_only_2026-06-21/`.
- Source packages:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/manual_gate_waveform_source_package_2026-06-21/`
  and
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/manual_gate_waveform_neutral_wrapper_source_package_2026-06-21/`.
- Clean build directory:
  `.tmp/gwnw_build_2026-06-21_clean/`.
- Decision:
  `STDRIVE101 gate-waveform neutral-wrapper build-only record no-power /
  object-only and linked-image build-only evidence for the neutral-wrapper
  source review / separate build-only package defines
  GATE_WAVEFORM_CANDIDATE_GATE_E2_BUILD_ACK and
  GATE_WAVEFORM_NEUTRAL_WRAPPER_BUILD_ACK / source-review packages remain
  source-review only and have no CMakeLists / build inputs include reviewed
  gate_waveform_candidate.c and wrapper main_neutral_wrapper.c / old
  main_waveform_candidate.c excluded from build.ninja and CMake source inputs /
  Generic arm CMake configure and Ninja build passed in short clean build dir /
  object target stdrive101_gate_waveform_neutral_wrapper_objects and linked
  target stdrive101_gate_waveform_neutral_wrapper_image built / ELF and MAP
  artifacts produced and hashed / ELF symbol table retains
  gate_waveform_neutral_wrapper_hold_idle_forever and does not retain
  gate_waveform_candidate_run_once / MAP lists gate_waveform_candidate_run_once
  only as a discarded zero-address input section from gate_waveform_candidate.c
  / no HEX or BIN target / build-only evidence / no flash / no Run Debug / no
  USB runtime execution / no 24 V / no Gate PWM output / no Motor Pilot / no
  Motor Profiler / no motor connection / no powered-drive readiness`.
- Build observations:
  clean build produced `stdrive101_gate_waveform_neutral_wrapper_objects` and
  `stdrive101_gate_waveform_neutral_wrapper_image`. ELF SHA256 is
  `C47C02D379DC5312095DF786BF8C99B58D42323AD9227D0903BCB8C98AAD9591`; MAP
  SHA256 is
  `5FB24B2735EFFD402C26BDC3B0D267B26B06DC6522A6B5B5D876491BA9A42A83`.
  Size is `text=1044`, `data=0`, `bss=1536`, `dec=2580`, `hex=a14`; linker
  memory report is RAM `1536 B / 128 KB / 1.17%` and FLASH
  `1044 B / 512 KB / 0.20%`.
- Boundary:
  build-only evidence only. The source-review packages still have no
  `CMakeLists.txt`; only the separate build-only package defines the two
  build acknowledgement macros. This record produces object, ELF, and MAP
  evidence only. It opens no firmware flash, Run / Debug, USB runtime
  execution, 24 V, Gate PWM output, Motor Pilot, Motor Profiler, motor
  connection, Hall closed loop, sensorless operation, power-stage readiness,
  or motor readiness.
- Next checkpoint:
  neutral-wrapper USB-only neutral-state phase-gate plan or review only. The
  next checkpoint is not flash, not Run / Debug, not USB runtime execution,
  not 24 V, not Gate PWM output, not Motor Pilot, not Motor Profiler, and not
  motor connection.

## Current 2026-06-21 STDRIVE101 Gate-Waveform Neutral-Wrapper Source Review No-Power

- Task:
  `TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-source-review-no-power`.
- Evidence:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-SOURCE-REVIEW-NO-POWER-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_neutral_wrapper_source_review_no_power_2026-06-21.md`.
- Source package:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/manual_gate_waveform_neutral_wrapper_source_package_2026-06-21/`.
- Decision:
  `STDRIVE101 gate-waveform neutral-wrapper source review no-power /
  source-side wrapper package created for review only / package has no
  CMakeLists and has GATE_WAVEFORM_NEUTRAL_WRAPPER_BUILD_ACK #error guard /
  wrapper replaces future candidate entry point only / wrapper calls
  gate_waveform_candidate_force_idle_low before the forever loop and inside
  the forever loop / wrapper source contains no gate_waveform_candidate_run_once
  call / no TIM1 waveform-window or output-enable path in wrapper source /
  current Gate E2 run_once image remains unsuitable for proving no boot
  transient with DMM-only evidence / source review only / no build / no flash /
  no Run Debug / no USB runtime execution / no 24 V / no Gate PWM output / no
  Motor Pilot / no Motor Profiler / no motor connection / no powered-drive
  readiness`.
- Boundary:
  source review only. The package has no `CMakeLists.txt`; the header requires
  `GATE_WAVEFORM_NEUTRAL_WRAPPER_BUILD_ACK` and raises `#error` until a later
  dated build-only boundary is opened. No object, ELF, MAP, HEX, BIN, flash,
  runtime, 24 V, Gate PWM output, Motor Pilot, Motor Profiler, motor
  connection, Hall closed loop, sensorless operation, power-stage readiness,
  or motor readiness is opened.
- Source-review observation:
  `main_neutral_wrapper.c` defines a future replacement entry point. It calls
  `gate_waveform_candidate_force_idle_low()` before the forever loop and
  inside the forever loop. Wrapper `Inc/` and `Src/` contain no
  `gate_waveform_candidate_run_once()` call and no TIM1 waveform-window or
  output-enable helper.
- Next checkpoint:
  neutral-wrapper build-only boundary plan or build-only record only. The next
  checkpoint is not USB runtime execution, not 24 V, not Gate PWM output, not
  Motor Pilot, not Motor Profiler, and not motor connection.

## Current 2026-06-21 STDRIVE101 Gate-Waveform USB-Only Neutral-State Phase-Gate Plan

- Task:
  `TASK-2026-06-21-stdrive101-gate-waveform-usbonly-neutral-state-phase-gate-plan`.
- Evidence:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-USBONLY-NEUTRAL-STATE-PHASE-GATE-PLAN-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_usb_only_neutral_state_phase_gate_plan_2026-06-21.md`.
- Candidate image boundary:
  `.tmp/manual_gate_waveform_build_only_2026-06-21_clean/stdrive101_gate_waveform_candidate_image.elf`
  SHA256 `10BA818730E259AEBA8A5C5E5C96CFBA32FCB90AAA4136B775022B9D69ADCE7C`.
- MAP boundary:
  `.tmp/manual_gate_waveform_build_only_2026-06-21_clean/stdrive101_gate_waveform_candidate_image.map`
  SHA256 `170EA77C566F98CF9EF2AC88F76B154238A5404DC705AAE3917BEAE7C1503D4C`.
- Decision:
  `STDRIVE101 gate-waveform USB-only neutral-state phase-gate plan / Gate E3
  plan only / Gate E2 linked-image build-only record accepted as image-boundary
  evidence / candidate ELF and MAP hashes carried forward / current waveform
  candidate main calls gate_waveform_candidate_run_once once and then loops
  forcing idle low / DMM-only future check can prove only post-window steady
  idle and cannot prove absence of a reset-time or boot-time transient /
  later USB-only execution-entry must separately name flash or transfer
  method, exact image hash, measurement instrument, pre/post measurement
  table, rollback path, and stop rules / phase-gate plan only / no flash / no
  Run Debug / no USB runtime execution / no 24 V / no Gate PWM output / no
  Motor Pilot / no Motor Profiler / no motor connection / no powered-drive
  readiness`.
- Boundary:
  Gate E3 phase-gate plan only. It performs no firmware flash, no Run /
  Debug, no USB runtime execution, no 24 V, no Gate PWM output, no
  oscilloscope probing on live gate or phase nodes, no Motor Pilot, no Motor
  Profiler, and no motor connection. It makes no Hall closed-loop,
  sensorless, power-stage readiness, or motor readiness claim.
- Important DMM limitation:
  the Gate E2 candidate is not a pure all-low lockout image. Its current
  `main()` calls `gate_waveform_candidate_run_once()` once and then loops
  forcing idle low. A future DMM-only USB check can record only steady
  post-window idle state; it cannot prove there was no reset-time or boot-time
  transient.
- Next checkpoint:
  only a separate Gate E3 USB-only neutral-state execution-entry record after
  explicit user request and freshly confirmed preconditions, or a source-side
  neutral-wrapper review if the team rejects the current `run_once()` image
  for a DMM-only neutral-state check. Gate E4 remains closed.

## Current 2026-06-21 STDRIVE101 Gate-Waveform Build-Only Record No-Power

- Task:
  `TASK-2026-06-21-stdrive101-gate-waveform-build-only-record-no-power`.
- Evidence:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-BUILD-ONLY-RECORD-NO-POWER-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_build_only_record_no_power_2026-06-21.md`.
- Source package:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/manual_gate_waveform_source_package_2026-06-21/`.
- Build-only package:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/manual_gate_waveform_build_only_2026-06-21/`.
- Clean build directory:
  `.tmp/manual_gate_waveform_build_only_2026-06-21_clean/`.
- Decision:
  `STDRIVE101 gate-waveform build-only record no-power / Gate E2 object-only
  and linked-image build-only evidence for the exact Gate E1 reviewed source
  package / separate build-only package defines
  GATE_WAVEFORM_CANDIDATE_GATE_E2_BUILD_ACK / Gate E1 source package remains
  source-review only and has no CMakeLists / Generic arm CMake configure and
  Ninja build passed / object target
  stdrive101_gate_waveform_candidate_objects and linked target
  stdrive101_gate_waveform_candidate_image built / ELF and MAP artifacts
  produced and hashed / -nostdlib minimal runtime keeps newlib malloc free
  paths out of the MAP / forbidden source ELF MAP screens clean / build-only
  evidence / no flash / no Run Debug / no USB runtime / no 24 V / no Gate PWM
  output / no Motor Pilot / no Motor Profiler / no motor connection / no
  powered-drive readiness`.
- Boundary:
  Gate E2 build-only evidence only. The Gate E1 source package still has no
  `CMakeLists.txt`; only the Gate E2 build-only package defines
  `GATE_WAVEFORM_CANDIDATE_GATE_E2_BUILD_ACK`. This record produces object,
  ELF, and MAP evidence only. It opens no firmware flash, Run / Debug, USB
  runtime execution, 24 V, Gate PWM output, Motor Pilot, Motor Profiler, motor
  connection, Hall closed loop, sensorless operation, power-stage readiness,
  or motor readiness.
- Build observations:
  clean configure used `CMAKE_SYSTEM_NAME=Generic`,
  `CMAKE_SYSTEM_PROCESSOR=arm`,
  `CMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY`, STM32Cube GNU Arm GCC
  `14.3.1`, and Ninja `1.13.2`. Clean build produced
  `stdrive101_gate_waveform_candidate_objects` and
  `stdrive101_gate_waveform_candidate_image`. Clean ELF SHA256 is
  `10BA818730E259AEBA8A5C5E5C96CFBA32FCB90AAA4136B775022B9D69ADCE7C`;
  clean MAP SHA256 is
  `170EA77C566F98CF9EF2AC88F76B154238A5404DC705AAE3917BEAE7C1503D4C`.
  `arm-none-eabi-size` reports `text=1852`, `data=0`, `bss=1544`,
  `dec=3396`, `hex=d44`.
- Forbidden screens:
  source/build, ELF symbol, and MAP screens are clean for normal generated
  MCSDK start / command ingress / PWM-output enable / Hall / PID /
  speed-loop / delay / printf / dynamic-allocation terms.
- Next checkpoint:
  Gate E3 only: a separate USB-only neutral-state phase-gate plan or review
  for the Gate E2 image. Gate E3 must still not open flash, Run / Debug, USB
  runtime execution, 24 V, Gate PWM output, Motor Pilot, Motor Profiler, motor
  connection, or readiness claims by default.

## Current 2026-06-21 STDRIVE101 Gate-Waveform Isolated Source Package Review No-Power

- Task:
  `TASK-2026-06-21-stdrive101-gate-waveform-isolated-source-package-review-no-power`.
- Evidence:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-ISOLATED-SOURCE-PACKAGE-REVIEW-NO-POWER-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_isolated_source_package_review_no_power_2026-06-21.md`.
- Source package:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/manual_gate_waveform_source_package_2026-06-21/`.
- Decision:
  `STDRIVE101 gate-waveform isolated source package review no-power / Gate E1
  source package created for review only / package has no CMakeLists and has a
  Gate E2 compile-acknowledgement #error guard / future isolated waveform
  image remains separate from normal generated MCSDK app and lockout image /
  candidate driver inputs fixed as PA8 PA9 PA10 PB13 PB14 PB15 / startup and
  shutdown force all six low / waveform constants frozen at 1 kHz, 100
  permille duty, 16 period window, 8 pre-idle periods, 32 post-idle periods,
  DTG 0x90 / TIM1 MOE CCER break AOE and dead-time policy visible in source /
  nFAULT stop path disables TIM1 outputs and forces all six low / source
  review only / no build / no flash / no Run Debug / no USB runtime / no
  24 V / no Gate PWM output / no Motor Pilot / no Motor Profiler / no motor
  connection / no powered-drive readiness`.
- Boundary:
  Gate E1 source review only. The source package intentionally has no
  `CMakeLists.txt`; the header requires
  `GATE_WAVEFORM_CANDIDATE_GATE_E2_BUILD_ACK` and raises `#error` until a
  later dated Gate E2 build-only boundary is opened. This record produces no
  object, ELF, MAP, HEX, BIN, flash, runtime, 24 V, Gate PWM output, or motor
  evidence.
- Source-review observations:
  candidate driver-input pins are fixed as `PA8`, `PA9`, `PA10`, `PB13`,
  `PB14`, and `PB15`; `gate_waveform_candidate_force_idle_low()` forces all
  six low before and after the candidate window; constants are frozen at
  `1 kHz`, `100` permille duty, `16` window periods, `8` pre-idle periods,
  `32` post-idle periods, and `DTG 0x90`; TIM1 `MOE`, `CCER`, break,
  AOE clearing, dead-time, and complementary-output policy are visible in
  source; `wait_for_pwm_periods_or_fault()` disables TIM1 outputs and forces
  all six pins low if `nFAULT` falls.
- Forbidden source screen:
  no `MC_StartMotor1`, `MCI_START`, PC13 start / stop, MCP, ASPEP,
  `R3_2_TurnOnLowSides`, `PWMC_SwitchOnPWM`, `LL_TIM_EnableAllOutputs`, Hall,
  PID, speed-loop, blocking delay, printf, or dynamic-allocation source path
  was found in the package `Inc/` or `Src/`.
- Next checkpoint:
  Gate E2 only: a separate object-only and linked-image build-only boundary
  plan or build-only record for the exact reviewed source package. Gate E2
  must still open no flash, Run / Debug, USB runtime execution, 24 V, Gate
  PWM output, Motor Pilot, Motor Profiler, motor connection, or readiness
  claims.

## Current 2026-06-20 STDRIVE101 Gate-Waveform Image Design Plan No-Power

- Task:
  `TASK-2026-06-20-stdrive101-gate-waveform-image-design-plan-no-power`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-GATE-WAVEFORM-IMAGE-DESIGN-PLAN-NO-POWER-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_image_design_plan_no_power_2026-06-20.md`.
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
- Boundary:
  Gate E0 design planning only. This record creates no source package, makes
  no CMake edits, runs no object or linked build, flashes no firmware, performs
  no Run / Debug, executes no USB runtime, applies no 24 V, emits no Gate PWM
  output, probes no live gate or phase waveform, starts no normal generated
  MCSDK app, opens no Motor Pilot or Motor Profiler path, connects no motor,
  and claims no Hall closed-loop, sensorless, power-stage, or motor readiness.
- Design requirements carried forward:
  any future waveform candidate must be a separate isolated image. The normal
  generated MCSDK app, `MC_StartMotor1`, `MCI_START`, PC13 start / stop,
  MCP / ASPEP command ingress, Motor Pilot, Motor Profiler, Hall closed-loop
  paths, speed-loop paths, and motor connection remain blocked.
- Candidate pins:
  the only candidate driver-input pins are `PA8`, `PA9`, `PA10`, `PB13`,
  `PB14`, and `PB15`. All six must be forced low before and after any future
  candidate window.
- Future source/build blockers:
  before any Gate E1 source package or Gate E2 build-only image, TIM1 `MOE`,
  `CCER`, break, AOE, OSSI / OSSR if used, polarity, preload, update timing,
  dead-time, and complementary-overlap policy must be explicitly reviewed.
- Next checkpoint:
  Gate E1 only: a separate isolated waveform source-package planning/review
  record, or a build-side boundary plan that still has no build, flash, Run /
  Debug, USB runtime execution, 24 V, Gate PWM output, Motor Pilot, Motor
  Profiler, motor connection, or readiness claim.

## Current 2026-06-20 STDRIVE101 Gate-Waveform / PWM-Output No-Power Phase-Gate Plan

- Task:
  `TASK-2026-06-20-stdrive101-gate-waveform-pwm-output-no-power-phase-gate-plan`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-GATE-WAVEFORM-PWM-OUTPUT-NO-POWER-PHASE-GATE-PLAN-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_pwm_output_no_power_phase_gate_plan_2026-06-20.md`.
- Decision:
  `STDRIVE101 gate-waveform PWM-output no-power phase-gate plan / 24V static
  lockout carry-forward result accepted as static boundary evidence /
  linked lockout image and USB-only runtime lockout result carried forward as
  driver-input-low evidence / normal generated MCSDK PWM path remains blocked /
  future gate-waveform execution gates, instrumentation requirements,
  rollback path, and stop rules named as future-only items / phase-gate plan
  only / no flash / no Run Debug / no 24 V / no Gate PWM output / no Motor
  Pilot / no Motor Profiler / no motor connection / no powered-drive
  readiness`.
- Accepted evidence:
  the 24V static lockout carry-forward result closes the duplicate static
  measurement branch and carries forward HSPY `CV`, about `0.045 A`,
  `CN3_1` through `CN3_6` close to `0 V`, `nFAULT = 3.3 V`,
  `CN3_14 / 3V3 = 3.3 V`, and `REG12 = 0.3 V`. The USB-only lockout result
  carries forward the reviewed lockout image and driver-input stop rule not
  hit.
- Future ladder:
  Gate E0 no-power waveform-image design plan, Gate E1 isolated waveform
  source package, Gate E2 object-only and linked-image build-only record,
  Gate E3 USB-only neutral-state check, Gate E4 future scope-only no-motor
  execution-entry, and Gate E5 result record. This record opens none of those
  execution gates.
- Boundary:
  phase-gate plan only. No flash, no Run / Debug, no USB runtime execution,
  no 24 V, no Gate PWM output, no oscilloscope probing on live gate or phase
  nodes, no normal generated MCSDK app run, no Motor Pilot, no Motor
  Profiler, no motor connection, no Hall closed loop, no sensorless operation,
  no power-stage readiness, and no motor readiness.
- Next checkpoint:
  Gate E0 only: a separate no-power waveform-image design plan, or source /
  build review that keeps all execution actions closed.

## Current 2026-06-20 STDRIVE101 Manual Gate-Test 24V Static Lockout Carry-Forward Result

- Task:
  `TASK-2026-06-20-stdrive101-manual-gate-test-24v-static-lockout-carry-forward-result`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-24V-STATIC-LOCKOUT-CARRY-FORWARD-RESULT-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_24v_static_lockout_carry_forward_result_2026-06-20.md`.
- Decision:
  `STDRIVE101 manual gate-test 24V static lockout carry-forward result /
  no repeated measurement / existing USB plus 24V static recheck carried
  forward with HSPY CV about 0.045 A, CN3_1 through CN3_6 all close to 0 V,
  nFAULT 3.3 V, CN3_14 3.3 V, REG12 0.3 V / USB-only lockout runtime result
  carried forward as reviewed lockout image driver-input-low evidence /
  static baseline accepted for no-repeat gating only / no claim of new 24V
  lockout measurement under lockout image / no Gate PWM output / no Motor
  Pilot / no Motor Profiler / no motor connection / no powered-drive
  readiness`.
- Carried-forward USB + 24 V static evidence:
  HSPY `CV`; current about `0.045 A`; `CN3_1` through `CN3_6` all close to
  `0 V`; `CN3_13 / nFAULT = 3.3 V`; `CN3_14 / 3V3 = 3.3 V`; `REG12 = 0.3 V`.
- Carried-forward USB-only lockout evidence:
  ELF SHA256 `87BF3F7A28949F8DB654927292083609E52AB46C511CB6191D03B280DBFFE9B6`;
  BIN SHA256
  `CBF833C8E9289D8B4A952C32C641CAA94928F1F8119C5DC528EBD779915EA6BE`;
  `CN3_1` through `CN3_6 = 0 V`; `CN3_13 / nFAULT = 3.3 V`;
  `CN3_14 / 3V3 = 3.3 V`; `REG12 = 0 V`; driver-input stop rule not hit.
- Boundary:
  no repeated measurement is requested or performed by this record. It does
  not claim a simultaneous fresh `lockout image + 24 V` direct measurement and
  does not open firmware flash, new Run / Debug, normal generated MCSDK app
  run, Gate PWM output, Motor Pilot, Motor Profiler, motor connection,
  Hall closed loop, sensorless operation, power-stage readiness, or motor
  readiness.
- Next checkpoint:
  a no-power phase-gate plan for the next higher-risk step, such as
  gate-waveform / PWM-output planning. Do not execute PWM, Motor Pilot,
  Motor Profiler, or motor work from this record.

## Current 2026-06-20 STDRIVE101 Manual Gate-Test 24V Static Lockout Execution Entry

- Task:
  `TASK-2026-06-20-stdrive101-manual-gate-test-24v-static-lockout-execution-entry`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-24V-STATIC-LOCKOUT-EXECUTION-ENTRY-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_24v_static_lockout_execution_entry_2026-06-20.md`.
- Decision:
  `STDRIVE101 manual gate-test 24V static lockout execution entry / user
  confirmed HSPY output OFF, HSPY set to 24 V 0.2 A, VS 24V_FUSED close to
  0 V and below 1 V, motor disconnected, wake stimulus removed, Motor Pilot
  and Motor Profiler closed, no abnormal heat smell sound / USB-only lockout
  result accepted as driver-input-low evidence / opens exactly one bounded
  24 V static lockout measurement pass / no Gate PWM output / no Motor Pilot /
  no Motor Profiler / no motor connection / no powered-drive readiness`.
- User-confirmed entry gates:
  HSPY output `OFF`; HSPY set to `24 V / 0.2 A`; `VS / 24V_FUSED` close to
  `0 V` and below `1 V`; motor disconnected; `10 kohm` wake resistor /
  `LIN1` stimulus removed; Motor Pilot / Profiler closed; no abnormal heat /
  smell / sound.
- Boundary:
  opens exactly one bounded 24 V static lockout measurement pass only as a
  historical execution-entry record. The later carry-forward result closes
  that branch without repeating the same static table. No new firmware flash,
  no new Run / Debug, no normal generated MCSDK app run, no Gate PWM output,
  no Motor Pilot, no Motor Profiler, no motor connection, no Hall closed loop,
  no sensorless operation, no power-stage readiness, and no motor readiness.
- Next checkpoint:
  superseded by the carry-forward result; do not repeat the 24 V static table
  unless the image, wiring, board condition, or tool state changes.

## Current 2026-06-20 STDRIVE101 Manual Gate-Test 24V Static Lockout Phase-Gate Plan

- Task:
  `TASK-2026-06-20-stdrive101-manual-gate-test-24v-static-lockout-phase-gate-plan`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-24V-STATIC-LOCKOUT-PHASE-GATE-PLAN-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_24v_static_lockout_phase_gate_plan_2026-06-20.md`.
- Decision:
  `STDRIVE101 manual gate-test 24V static lockout phase-gate plan / USB-only
  runtime lockout result accepted as driver-input-low evidence / earlier USB
  plus 24V static baseline carried forward / candidate 24V static lockout
  execution preconditions, measurement table, rollback path, and stop rules
  named / phase-gate plan only / no 24V execution in this record / no Gate PWM
  output / no Motor Pilot / no Motor Profiler / no motor connection / no
  powered-drive readiness`.
- Accepted evidence:
  USB-only lockout result records `CN3_1` through `CN3_6 = 0 V`,
  `nFAULT = 3.3 V`, `CN3_14 / 3V3 = 3.3 V`, `REG12 = 0 V`, and
  driver-input stop rule not hit. Earlier USB plus 24V static baseline records
  HSPY `CV`, about `0.045 A`, six driver inputs close to `0 V`, `nFAULT =
  3.3 V`, `CN3_14 / 3V3 = 3.3 V`, and `REG12 = 0.3 V`.
- Boundary:
  phase-gate plan only. No 24V execution in this record, no flash, no Run /
  Debug, no normal generated MCSDK app run, no Gate PWM output, no Motor
  Pilot, no Motor Profiler, no motor connection, no Hall closed loop, no
  sensorless operation, no power-stage readiness, and no motor readiness.
- Next checkpoint:
  only a later separate 24 V static lockout execution-entry record may apply
  HSPY, and only after explicit user request plus freshly confirmed
  preconditions.

## Current 2026-06-20 STDRIVE101 Manual Gate-Test USB-Only Runtime Lockout Result

- Task:
  `TASK-2026-06-20-stdrive101-manual-gate-test-usbonly-runtime-lockout-result`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-USBONLY-RUNTIME-LOCKOUT-RESULT-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_usb_only_runtime_lockout_result_2026-06-20.md`.
- Decision:
  `STDRIVE101 manual gate-test USB-only runtime lockout result / reviewed
  lockout ELF converted to BIN and copied through ST-LINK mass storage /
  no FAIL.TXT after copy / user-reported CN3_1 through CN3_6 all 0 V /
  nFAULT 3.3 V / CN3_14 3.3 V / REG12 0 V / driver-input stop rule not hit /
  USB-only runtime evidence only / no 24 V / no PWM-output validation /
  no Motor Pilot / no Motor Profiler / no motor connection / no
  powered-drive readiness`.
- Download evidence:
  ELF SHA256 `87BF3F7A28949F8DB654927292083609E52AB46C511CB6191D03B280DBFFE9B6`;
  generated BIN SHA256
  `CBF833C8E9289D8B4A952C32C641CAA94928F1F8119C5DC528EBD779915EA6BE`;
  copied to ST-LINK mass-storage `D:` / `NOD_G474RE`; no `FAIL.TXT`.
- User-reported readings:
  `CN3_1 = 0 V`, `CN3_2 / LIN1 = 0 V`, `CN3_3 = 0 V`,
  `CN3_4 = 0 V`, `CN3_5 = 0 V`, `CN3_6 = 0 V`,
  `CN3_13 / nFAULT = 3.3 V`, `CN3_14 / 3V3 = 3.3 V`,
  and `REG12 = 0 V`.
- Boundary:
  USB-only runtime evidence only. Still no 24 V, Gate PWM output,
  Motor Pilot, Motor Profiler, motor connection, Hall closed loop,
  sensorless operation, power-stage readiness, or motor readiness.
- Next checkpoint:
  a separate dated phase-gate review before any later 24 V static lockout
  check, PWM/gate waveform task, or motor task is considered.

## Current 2026-06-20 STDRIVE101 Manual Gate-Test USB-Only Runtime Lockout Execution Entry

- Task:
  `TASK-2026-06-20-stdrive101-manual-gate-test-usbonly-runtime-lockout-execution-entry`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-USBONLY-RUNTIME-LOCKOUT-EXECUTION-ENTRY-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_usb_only_runtime_lockout_execution_entry_2026-06-20.md`.
- Decision:
  `STDRIVE101 manual gate-test USB-only runtime lockout execution entry /
  user confirmed HSPY 24 V OFF and physically disconnected, VS 24V_FUSED
  below 1 V, motor disconnected, wake stimulus removed, Motor Pilot and Motor
  Profiler closed, no abnormal heat smell sound / linked-image ELF hash matched
  / opens exactly one USB-only lockout flash-run measurement pass / no 24 V /
  no PWM-output validation / no Motor Pilot / no Motor Profiler / no motor
  connection / no powered-drive readiness`.
- Candidate image:
  `.tmp/manual_gate_test_lockout_linked_image/stdrive101_gate_lockout_image.elf`
  SHA256 `87BF3F7A28949F8DB654927292083609E52AB46C511CB6191D03B280DBFFE9B6`.
- Boundary:
  one USB-only lockout flash / run measurement pass is opened. Still no
  24 V, Gate PWM output, Motor Pilot, Motor Profiler, motor connection,
  Hall closed loop, sensorless operation, power-stage readiness, or motor
  readiness.
- Next checkpoint:
  fill the direct measurement table and create a separate runtime result
  record.

## Current 2026-06-20 STDRIVE101 Manual Gate-Test USB-Only Runtime Lockout Phase-Gate Plan

- Task:
  `TASK-2026-06-20-stdrive101-manual-gate-test-usbonly-runtime-lockout-phase-gate-plan`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-USBONLY-RUNTIME-LOCKOUT-PHASE-GATE-PLAN-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_usb_only_runtime_lockout_phase_gate_plan_2026-06-20.md`.
- Decision:
  `STDRIVE101 manual gate-test USB-only runtime lockout phase-gate plan
  no-power / linked-image build-only record accepted as image-boundary
  evidence / candidate USB-only runtime preconditions, measurement table, and
  stop rules named / phase-gate plan only / no flash / no Run Debug / no USB
  runtime execution / no 24 V / no PWM-output validation / no powered-drive
  readiness`.
- Candidate image:
  `stdrive101_gate_lockout_image`,
  `.tmp/manual_gate_test_lockout_linked_image/stdrive101_gate_lockout_image.elf`
  SHA256 `87BF3F7A28949F8DB654927292083609E52AB46C511CB6191D03B280DBFFE9B6`.
- Boundary:
  phase-gate plan only. No flash, Run / Debug, USB runtime execution,
  24 V powered runtime, Gate PWM output, Motor Pilot, Motor Profiler,
  motor connection, Hall closed loop, sensorless operation, power-stage
  readiness, or motor readiness is opened.
- Next checkpoint:
  only a later separate USB-only runtime execution record may execute anything,
  and only after explicit user request plus the named preconditions.

## Current 2026-06-20 STDRIVE101 Manual Gate-Test Linked-Image Build-Only Record

- Task:
  `TASK-2026-06-20-stdrive101-manual-gate-test-linked-image-build-only-record-no-power`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-LINKED-IMAGE-BUILD-ONLY-RECORD-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_linked_image_build_only_record_2026-06-20.md`.
- Build target:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/manual_gate_test_lockout_build_only_2026-06-20/CMakeLists.txt`
  adds linked target `stdrive101_gate_lockout_image`.
- Decision:
  `STDRIVE101 manual gate-test linked-image build-only record no-power /
  repo-local CMake linked target stdrive101_gate_lockout_image added /
  Generic bare-metal CMake configure and Ninja build passed / ELF and MAP
  artifacts produced and hashed / forbidden source ELF MAP screens clean /
  build-only evidence / no flash / no Run Debug / no USB runtime / no 24 V /
  no PWM-output validation / no powered-drive readiness`.
- Artifacts:
  `.tmp/manual_gate_test_lockout_linked_image/stdrive101_gate_lockout_image.elf`
  SHA256 `87BF3F7A28949F8DB654927292083609E52AB46C511CB6191D03B280DBFFE9B6`;
  `.tmp/manual_gate_test_lockout_linked_image/stdrive101_gate_lockout_image.map`
  SHA256 `A020546A3D1D56B1C509939161BD80E5A25EC5843C928B9BC13E8D07684FF6C0`.
- Boundary:
  linked-image build-only evidence. No flash, Run / Debug, USB runtime
  execution, 24 V powered runtime, Gate PWM output, Motor Pilot,
  Motor Profiler, motor connection, Hall closed loop, sensorless operation,
  power-stage readiness, or motor readiness is opened.
- Next checkpoint:
  separate USB-only runtime lockout phase-gate plan or review; do not execute
  runtime yet.

## Current 2026-06-20 STDRIVE101 Manual Gate-Test Linked-Image Build-Boundary Plan

- Task:
  `TASK-2026-06-20-stdrive101-manual-gate-test-linked-image-build-boundary-plan-no-power`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-LINKED-IMAGE-BUILD-BOUNDARY-PLAN-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_linked_image_build_boundary_plan_2026-06-20.md`.
- Decision:
  `STDRIVE101 manual gate-test linked-image build-boundary plan no-power /
  object-only lockout build pass and USB-only runtime lockout preparation
  carried forward / future link inputs and minimum image artifacts named /
  boundary plan only / no linked image built / no flash / no runtime / no
  PWM-output validation / no powered-drive readiness`.
- Boundary:
  build-boundary plan evidence only. No linked image, CMake link target,
  firmware flash, Run / Debug, USB runtime execution, 24 V powered runtime,
  Gate PWM output, Motor Pilot, Motor Profiler, motor connection, Hall closed
  loop, sensorless operation, power-stage readiness, or motor readiness is
  opened.
- Next checkpoint:
  create a separate linked-image build-only record for the lockout image; do
  not execute runtime yet.

## Current 2026-06-20 STDRIVE101 Manual Gate-Test USB-Only Runtime Lockout Prep

- Task:
  `TASK-2026-06-20-stdrive101-manual-gate-test-usbonly-runtime-lockout-prep`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-USBONLY-RUNTIME-LOCKOUT-PREP-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_usb_only_runtime_lockout_prep_2026-06-20.md`.
- Decision:
  `STDRIVE101 manual gate-test USB-only runtime lockout preparation no-power /
  object-only lockout build pass carried forward / exact source and object
  provenance recorded / future runtime must be USB-only with no 24 V, motor
  disconnected, power board not powered, and six driver inputs expected low /
  preparation only / no flash / no runtime / no PWM-output validation / no
  powered-drive readiness`.
- Boundary:
  preparation evidence only. No flash, Run / Debug, USB runtime execution,
  24 V powered runtime, Gate PWM output, Motor Pilot, Motor Profiler, motor
  connection, Hall closed loop, sensorless operation, power-stage readiness,
  or motor readiness is opened.
- Next checkpoint:
  linked-image build-boundary plan or build-only record for the lockout image;
  do not execute runtime yet.

## Current 2026-06-20 STDRIVE101 Manual Gate-Test Lockout Object-Only Build Pass

- Task:
  `TASK-2026-06-20-stdrive101-manual-gate-test-lockout-object-build-pass-no-power`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-LOCKOUT-OBJECT-BUILD-PASS-NO-POWER-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_lockout_object_build_pass_2026-06-20.md`.
- Decision:
  `STDRIVE101 manual gate-test lockout object-only build pass no-power /
  repo-local CMake object library configured with STM32Cube GNU Arm GCC
  14.3.1 and Ninja 1.13.2 / stdrive101_gate_lockout_objects built successfully
  / gate_test_lockout.c.obj and main_lockout.c.obj produced / no lockout ELF
  HEX BIN MAP linked image produced / no flash / no runtime / no PWM-output
  validation / no powered-drive readiness`.
- Boundary:
  no-power object-build evidence only. No flash, Run / Debug, 24 V powered
  runtime, Gate PWM output, Motor Pilot, Motor Profiler, motor connection,
  Hall closed loop, sensorless operation, power-stage readiness, or motor
  readiness is opened.
- Next checkpoint:
  write USB-only runtime lockout preparation; do not execute runtime yet.

## Current 2026-06-20 STDRIVE101 Manual Gate-Test Lockout Object-Only Target

- Task:
  `TASK-2026-06-20-stdrive101-manual-gate-test-lockout-object-target-no-power`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-LOCKOUT-OBJECT-TARGET-NO-POWER-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_lockout_object_target_2026-06-20.md`.
- Build target:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/manual_gate_test_lockout_build_only_2026-06-20/CMakeLists.txt`.
- Decision:
  `STDRIVE101 manual gate-test lockout object-only target no-power /
  repo-local CMake object library target added for the isolated lockout source
  package / target compiles only gate_test_lockout.c and main_lockout.c object
  files / no ELF HEX BIN link target / REPO_ROOT path corrected and CMSIS
  headers resolved / sandbox blocked external Ninja during configure and
  auto-review escalation returned 503 / no object build pass claimed / no
  flash / no runtime / no PWM-output validation / no powered-drive readiness`.
- Boundary:
  build-target setup evidence only. No flash, Run / Debug, 24 V powered
  runtime, Gate PWM output, Motor Pilot, Motor Profiler, motor connection,
  Hall closed loop, sensorless operation, power-stage readiness, or motor
  readiness is opened.
- Next checkpoint:
  rerun CMake configure and build the object-only target when external-tool
  approval is available; record object files, compiler diagnostics, sizes, and
  hashes.

## Current 2026-06-20 STDRIVE101 Manual Gate-Test Lockout Source Package

- Task:
  `TASK-2026-06-20-stdrive101-manual-gate-test-lockout-source-package-no-power`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-LOCKOUT-SOURCE-PACKAGE-NO-POWER-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_lockout_source_package_2026-06-20.md`.
- Source package:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/manual_gate_test_lockout_build_only_2026-06-20/`.
- Decision:
  `STDRIVE101 manual gate-test lockout source package no-power / repo-local
  isolated lockout source added / six driver input pins forced GPIO low /
  PB12 nFAULT kept as input / TIM1 CCER cleared / TIM1 MOE and automatic
  output cleared / TIM1 break left enabled / forbidden normal MCSDK start and
  command ingress symbols absent from lockout Src and Inc / source package only
  / no embedded build target yet / no flash / no runtime / no PWM-output
  validation / no powered-drive readiness`.
- Boundary:
  source-package and static-inspection evidence only. No flash, Run / Debug,
  24 V powered runtime, Gate PWM output, Motor Pilot, Motor Profiler, motor
  connection, Hall closed loop, sensorless operation, power-stage readiness, or
  motor readiness is opened.
- Next checkpoint:
  create a separate repo-local embedded build target or an explicitly copied
  external Workbench clone for compile-only checking; still no flash, runtime,
  24 V, PWM output, or motor.

## Current 2026-06-20 STDRIVE101 Manual Gate-Test Firmware Plan

- Task:
  `TASK-2026-06-20-stdrive101-manual-gate-test-firmware-plan-no-power`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-FIRMWARE-PLAN-NO-POWER-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_firmware_plan_no_power_2026-06-20.md`.
- Decision:
  `STDRIVE101 manual gate-test firmware plan no-power / normal MCSDK start path
  remains blocked / future gate-test must use an isolated lockout firmware path
  that avoids MC_StartMotor1, MCI_START, PC13 start-stop, MCP command ingress,
  Motor Pilot, Hall closed-loop paths, speed-loop paths, and motor connection /
  plan only / no PWM-output validation / no powered-drive readiness`.
- Planned lockout shape:
  a later separate firmware task must keep the first lockout image isolated
  from normal MCSDK start, hold `PA8`, `PA9`, `PA10`, `PB13`, `PB14`, and
  `PB15` low, leave `PB12 / nFAULT` as input only, keep TIM1 `MOE = 0`, keep
  all relevant `CCER` outputs disabled, keep automatic output disabled, and
  keep break protection enabled.
- Boundary:
  plan-only / no-power evidence. No firmware edit, build, flash, Run / Debug,
  24 V powered runtime, PWM output, Motor Pilot, Motor Profiler, motor
  connection, Hall closed loop, sensorless operation, power-stage readiness, or
  motor readiness is opened.
- Next checkpoint:
  review the no-power plan. If accepted later, open a separate build-only
  implementation task for an isolated lockout image; do not start from normal
  `MC_StartMotor1()` / `MCI_START`.

## Current 2026-06-20 STDRIVE101 R3_2 MCSDK PWM Output Path Source Closure

- Task:
  `TASK-2026-06-20-stdrive101-r3-2-mcsdk-pwm-output-path-source-closure`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-R3-2-MCSDK-PWM-OUTPUT-PATH-SOURCE-CLOSURE-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_r3_2_mcsdk_pwm_output_path_source_closure_2026-06-20.md`.
- Reviewed source:
  Workbench project-local
  `MCSDK_v6.4.2-Full/MotorControl/MCSDK/MCLib/G4xx/Src/r3_2_g4xx_pwm_curr_fdbk.c`,
  SHA256 `D3787B25374154AB1DC6A2CABD05DE299D5691DA92DDC4DE4BEC93DE81BE2451`.
- Decision:
  `STDRIVE101 R3_2 MCSDK PWM output path source closure / exact local
  Workbench MCSDK r3_2_g4xx_pwm_curr_fdbk.c found and hashed / R3_2 output
  enable behavior reviewed / normal generated MCSDK start remains blocked for
  powered PWM because start path disables BRK before low-side boot-cap and
  R3_2_TurnOnLowSides enables TIM1 main outputs with 0-tick low-sides-on
  semantics / no PWM-output validation / no powered-drive readiness`.
- Boundary:
  no motor, Gate PWM output, Motor Pilot, Motor Profiler, firmware Flash /
  Run / Debug, Hall closed loop, sensorless operation, power-stage readiness,
  or motor readiness.
- Next checkpoint:
  separate no-power-only manual gate-test firmware plan; do not use normal
  `MC_StartMotor1()` / `MCI_START`, PC13 start/stop, MCP command ingress,
  Motor Pilot, Hall closed-loop paths, speed-loop paths, or a motor.

## Current 2026-06-20 STDRIVE101 PWM/Gate-Test No-Power Source Review

- Task:
  `TASK-2026-06-20-stdrive101-pwm-gate-test-no-power-source-review`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-PWM-GATE-TEST-NO-POWER-SOURCE-REVIEW-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_pwm_gate_test_no_power_source_review_2026-06-20.md`.
- Decision:
  `STDRIVE101 PWM gate-test no-power source review / static hardware screen
  passed for planning only / generated MCSDK direct PWM gate remains blocked by
  command-ingress, external R3_2 implementation, BKIN polarity, Hall-route, and
  generation-log trust gaps / no PWM-output validation / no powered-drive
  readiness`.
- Key findings:
  `main.c` has no direct `MC_StartMotor1()` autostart, but runtime start
  ingress exists through PC13 start/stop and MCSDK command paths. A valid
  start command can set `DirectCommand = MCI_START`; the generated state path
  reaches `R3_2_TurnOnLowSides()` and later `PWMC_SwitchOnPWM()`. The actual
  R3_2 PWM implementation is pulled from an external MCSDK file that is not
  packet-local, TIM1 BKIN / `nFAULT` polarity is not closed, and the
  generation log contains PWM / BKIN / MotorControl invalid-parameter messages.
- Boundary:
  no motor, Gate PWM output, Motor Pilot, Motor Profiler, firmware Flash /
  Run / Debug, Hall closed loop, sensorless operation, power-stage readiness,
  or motor readiness.
- Next checkpoint:
  the R3_2 source closure has now been recorded; the remaining next checkpoint
  is a separate no-power-only manual gate-test firmware plan.

## Current 2026-06-20 STDRIVE101 USB + 24V Static Recheck Result

- Task:
  `TASK-2026-06-20-stdrive101-usb24-static-recheck`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-USB24-STATIC-RECHECK-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_usb24_static_recheck_result_2026-06-20.md`.
- User-reported raw readings:
  HSPY `CV`, current about `0.045 A`, `CN3_1` through `CN3_6` all close to
  `0 V`, `CN3_14 / 3V3 = 3.3 V`, `CN3_13 / nFAULT = 3.3 V`, and
  `REG12 = 0.3 V`.
- Decision:
  `STDRIVE101 USB plus 24V static recheck result / USB-STLINK connected /
  HSPY CV about 0.045 A / CN3_1 through CN3_6 all close to 0 V / CN3_14
  3.3 V / nFAULT 3.3 V / REG12 about 0.3 V / no MCU-facing driver input high
  and no REG12 wake observed in USB plus 24V static state / no PWM-output
  validation / no powered-drive readiness`.
- Boundary:
  bounded static diagnostic evidence only. This does not authorize motor
  connection, Gate PWM, Motor Pilot, Motor Profiler, firmware Flash / Run /
  Debug, Hall closed loop, sensorless operation, power-stage readiness, or
  motor readiness.
- Next checkpoint:
  no-power firmware/source planning for a future explicit PWM/gate-test phase
  gate. Do not connect a motor or run PWM.

## Current 2026-06-20 STDRIVE101 USB-Only MCU Default Input State Result

- Task:
  `TASK-2026-06-20-stdrive101-usbonly-mcu-default-input-state`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-USBONLY-MCU-DEFAULT-INPUT-STATE-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_usbonly_mcu_default_input_state_result_2026-06-20.md`.
- User-reported raw readings:
  `CN3_1` through `CN3_6` all close to `0 V`; `P13 = 3.3 V` and
  `P14 = 3.3 V`, interpreted from the requested table as
  `CN3_13 / nFAULT = 3.3 V` and `CN3_14 / 3V3 = 3.3 V`.
- Decision:
  `STDRIVE101 USB-only MCU default input state result / HSPY OFF no 24 V /
  USB-STLINK connected / CN3_1 through CN3_6 all close to 0 V / interpreted
  CN3_13 nFAULT 3.3 V / interpreted CN3_14 3V3 3.3 V / no MCU-facing driver
  input high observed in USB-only state / no PWM-output validation / no
  powered-drive readiness`.
- Boundary:
  USB-only / no-24V evidence only. This does not authorize motor connection,
  Gate PWM, Motor Pilot, Motor Profiler, firmware Flash / Run / Debug, Hall
  closed loop, sensorless operation, power-stage readiness, or motor
  readiness.
- Next checkpoint:
  separate bounded static 24 V check with USB/ST-LINK connected and no
  firmware command. Do not connect a motor or run PWM.

## Current 2026-06-20 STDRIVE101 All-Inputs-Low Static Recheck Result

- Task:
  `TASK-2026-06-20-stdrive101-all-inputs-low-static-recheck`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-ALL-INPUTS-LOW-STATIC-RECHECK-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_all_inputs_low_static_recheck_result_2026-06-20.md`.
- User-reported raw readings:
  HSPY `CV`, current about `0.045 A`, `CN3_1` through `CN3_6` all close to
  `0 V`, `CN3_14 / 3V3 = 3.3 V`, `CN3_13 / nFAULT = 3.3 V`, and
  `REG12 = 0.3 V`.
- Decision:
  `STDRIVE101 all-inputs-low static recheck result / 10 kohm wake stimulus
  removed / HSPY CV about 0.045 A / CN3_1 through CN3_6 all close to 0 V /
  CN3_14 3.3 V / nFAULT 3.3 V / REG12 about 0.3 V / standby-like recovery
  confirmed after clean LIN1 wake retest / no PWM-output validation / no
  powered-drive readiness`.
- Boundary:
  bounded static diagnostic evidence only. Before any later wiring change,
  HSPY output must be OFF and `VS / 24V_FUSED < 1 V` must be rechecked. This
  does not authorize motor connection, Gate PWM, Motor Pilot, Motor Profiler,
  firmware Run / Debug, Hall closed loop, sensorless operation, power-stage
  readiness, or motor readiness.
- Next checkpoint:
  no-24V USB/ST-LINK default-state check of MCU-facing driver inputs. Do not
  connect a motor or run PWM.

## Current 2026-06-20 STDRIVE101 Single-Input Wake Retest Clean Result

- Task:
  `TASK-2026-06-20-stdrive101-single-input-wake-retest-clean-result`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-SINGLE-INPUT-WAKE-RETEST-CLEAN-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_reg12_single_input_wake_retest_clean_result_2026-06-20.md`.
- User-reported retest readings:
  `retest_supply_state = CV`, `retest_supply_current_A = 0.048 A`,
  `retest_CN3_2_LIN1_V = 3.13 V`, `retest_CN3_13_nFAULT_V = 3.3 V`,
  and `retest_REG12_V = 12 V`.
- User-reported recovery readings:
  `recovery_supply_state = CV`, `recovery_supply_current_A = 0.045 A`,
  `recovery_CN3_13_nFAULT_V = 3.3 V`, and
  `recovery_REG12_V = 0.33 V`.
- Decision:
  `STDRIVE101 REG12 single-input wake retest clean result / CN3_14 3V3 through
  10 kohm to CN3_2 LIN1 / LIN1 3.13 V / HSPY CV 0.048 A / REG12 rose to
  12 V / nFAULT stayed 3.3 V / recovery all-inputs-low REG12 0.33 V and
  nFAULT 3.3 V / previous nFAULT-low wake blocker not reproduced after
  gate-source pulldown rework / no PWM-output validation / no powered-drive
  readiness`.
- Boundary:
  bounded diagnostic evidence only. Before any later wiring change, HSPY
  output must be OFF and `VS / 24V_FUSED < 1 V` must be rechecked. This does
  not authorize motor connection, Gate PWM, Motor Pilot, Motor Profiler,
  firmware Run / Debug, Hall closed loop, sensorless operation, power-stage
  readiness, or motor readiness.
- Next checkpoint:
  return to no-power planning / source review unless a separate bounded phase
  gate is opened. Do not connect a motor or run PWM.

## Current 2026-06-20 STDRIVE101 Gate-Source Pulldown Rework Result

- Task:
  `TASK-2026-06-20-stdrive101-gate-source-pulldown-rework-result`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-GATE-SOURCE-PULLDOWN-REWORK-RESULT-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_source_pulldown_rework_result_2026-06-20.md`.
- User-reported final six-route readings after rework:
  `VS_OFF_V = 0 V`, `Q1_GS = 10 kohm`, `Q3_GS = 10 kohm`,
  `Q5_GS = 10 kohm`, `Q2_GS = 10 kohm`, `Q4_GS = 10 kohm`, and
  `Q6_GS = 10 kohm`, with `10k_removed = yes`.
- Decision:
  `STDRIVE101 gate-source pulldown rework result / Q1-GS 10 kohm / Q3-GS
  10 kohm / Q5-GS 10 kohm / Q2-GS 10 kohm / Q4-GS 10 kohm / Q6-GS 10 kohm /
  previous gate-source pulldown anomaly branch no longer indicated / original
  nFAULT cause not proven / no repeat powered wake yet / no PWM-output
  validation / no powered-drive readiness`.
- Boundary:
  no power and no unknown-node probing. `VS_OFF_V = 0 V` closes the missing
  power-off-voltage field for this record, but `VS / 24V_FUSED < 1 V` must be
  rechecked before any later wiring change or powered retest. This does not
  authorize repeat powered wake, alternate input stimulus, firmware
  implementation, generated-code edits, CubeMX / Workbench edits, flash,
  Run / Debug, motor connection, Gate PWM, Motor Pilot, Motor Profiler,
  Hall closed loop, sensorless operation, power-stage readiness, or motor
  readiness.
- Next checkpoint:
  decide whether to continue no-power evidence or prepare a separate bounded
  single-input wake retest plan. Do not connect a motor or run PWM.

## Current 2026-06-20 STDRIVE101 Protection Nodes No-Power DMM Result

- Task:
  `TASK-2026-06-20-stdrive101-protection-nodes-no-power-dmm-result`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-PROTECTION-NODES-NO-POWER-DMM-RESULT-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_protection_nodes_no_power_dmm_result_2026-06-20.md`.
- User-reported raw readings:
  `SCREF-3V3 = 12 kohm`, `SCREF-GND = 12 kohm`,
  `CP-GND = 1.54 Mohm` rising to about `2 Mohm` with no resistance-mode beep,
  `REG12-GND = 0.2 Mohm` rising to `0.28 Mohm`,
  `REG12-VS = 40 kohm` steady, `OUT1-GND = no beep`, and
  `OUT1-VS` diode mode `OL` in both directions.
- Decision:
  `STDRIVE101 protection-node no-power DMM result / SCREF to 3V3 12 kohm /
  SCREF to GND 12 kohm / CP to GND 1.54 Mohm rising to about 2 Mohm no beep /
  REG12 to GND 0.2 Mohm rising to 0.28 Mohm / REG12 to VS 40 kohm steady /
  OUT1 to GND no beep / OUT1 to VS diode OL both directions / stable hard
  short not indicated on CP, REG12, or OUT1 in the reported rows / VDS
  low-side path remains the primary review target / next no-power Q2 low-side
  path checks only / no repeat powered wake / no PWM-output validation / no
  powered-drive readiness`.
- Boundary:
  no power and no unknown-node probing. The corrected table did not restate
  `VS_OFF_V`; confirm `VS / 24V_FUSED < 1 V` before any later measurement.
  This does not authorize repeat powered wake, alternate input stimulus,
  firmware implementation, generated-code edits, CubeMX / Workbench edits,
  flash, Run / Debug, motor connection, Gate PWM, Motor Pilot, Motor Profiler,
  Hall closed loop, sensorless operation, power-stage readiness, or motor
  readiness.
- Next checkpoint:
  no-power Q2 low-side path checks only, using confidently identified component
  pads. If Q2 source, Q2 drain / `OUT1`, Q2 gate / `GLS1`, `ADC_U`, or `R25`
  pads are uncertain, request a clear board photo or EDA/netlist crop instead
  of probing by guesswork.

## Current 2026-06-20 STDRIVE101 Fault Review Schematic Marking

- Task:
  `TASK-2026-06-20-stdrive101-fault-review-schematic-marking`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-FAULT-REVIEW-SCHEMATIC-MARKING-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_fault_review_schematic_marking_2026-06-20.md`.
- Marked images:
  `hardware/schematic/annotated/stdrive101_fault_review_full_marked_2026-06-20.png`,
  `hardware/schematic/annotated/stdrive101_driver_control_nodes_marked_2026-06-20.png`,
  and
  `hardware/schematic/annotated/stdrive101_phase_u_out1_gls1_q2_marked_2026-06-20.png`.
- Decision:
  `STDRIVE101 fault review schematic marking / source image marked for CN8-CN3,
  LIN1, nFAULT, CP, SCREF, REG12, OUT1, GHS1, GLS1, Q2 low-side path, and
  GND domains / supports VDS-monitoring source review after LIN1 low-side
  command / no unknown-node probing / no repeat powered wake / no PWM-output
  validation / no powered-drive readiness`.
- Boundary:
  source-image marking only. It does not authorize repeat powered wake,
  alternate input stimulus, firmware implementation, generated-code edits,
  CubeMX / Workbench edits, flash, Run / Debug, motor connection, Gate PWM,
  Motor Pilot, Motor Profiler, Hall closed loop, sensorless operation,
  power-stage readiness, or motor readiness.
- Next checkpoint:
  no power. Use the marked images only to identify physical board areas. If
  `SCREF`, `CP`, `REG12`, `OUT1`, `GLS1`, or Q2 terminals cannot be identified
  with certainty, request a clear board photo or EDA/netlist crop instead of
  probing by guesswork.

## Current 2026-06-20 STDRIVE101 nFAULT No-Power DMM Result

- Task:
  `TASK-2026-06-20-stdrive101-nfault-no-power-dmm-result`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-NFAULT-NO-POWER-DMM-RESULT-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_nfault_no_power_dmm_result_2026-06-20.md`.
- User-reported raw readings:
  `CN3_2 / LIN1` to `CN3_14 / 3V3` = no beep / `66 kohm`;
  `CN3_2 / LIN1` to `CN3_15 / GND` = no beep / `60 kohm`;
  `CN3_13 / nFAULT` to `CN3_14 / 3V3` = no beep / `5 kohm`;
  `CN3_13 / nFAULT` to `CN3_15 / GND` = no beep / `10 kohm`.
- Decision:
  `STDRIVE101 nFAULT no-power DMM result / LIN1 to 3V3 66 kohm no beep /
  LIN1 to GND 60 kohm no beep / nFAULT to 3V3 5 kohm no beep / nFAULT to GND
  10 kohm no beep / LIN1 persistent rail short not indicated / nFAULT
  persistent rail short not indicated / VDS monitoring after LIN1 low-side
  command remains the primary review target / source packet or identified
  no-power protection-node checks needed before any repeat powered wake / no
  PWM-output validation / no powered-drive readiness`.
- Boundary:
  no power and no unknown-node probing. This does not authorize repeat powered
  wake, alternate input stimulus, firmware implementation, generated-code
  edits, CubeMX / Workbench edits, flash, Run / Debug, motor connection,
  Gate PWM, Motor Pilot, Motor Profiler, Hall closed loop, sensorless
  operation, power-stage readiness, or motor readiness.
- Next checkpoint:
  no power. Provide a marked source packet or confidently identified no-power
  protection-node checks for `SCREF`, `CP`, `REG12`, `OUT1`, and the related
  low-side-1 gate / MOSFET nodes. Do not probe unknown points by guesswork.

## Current 2026-06-20 STDRIVE101 Single-Input Wake nFAULT Cause Review

- Task:
  `TASK-2026-06-20-stdrive101-single-input-wake-nfault-cause-review`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-SINGLE-INPUT-WAKE-NFAULT-CAUSE-REVIEW-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_single_input_wake_nfault_cause_review_2026-06-20.md`.
- Decision:
  `STDRIVE101 single-input wake nFAULT cause review / REG12 wake observed but
  clean wake failed / primary review target VDS monitoring after LIN1 low-side
  command / secondary targets REG12 sequence or accidental external REG12 tie,
  CP comparator, thermal shutdown, external nFAULT pull-down / next step
  no-power DMM and source packet only / no repeat powered wake / no PWM-output
  validation / no powered-drive readiness`.
- Scope:
  ranks plausible `nFAULT` causes using the STDRIVE101 datasheet, project
  protection notes, and the user-reported wake result.
- Boundary:
  this is no-power / source review only. It does not authorize repeat powered
  wake, alternate input stimulus, firmware implementation, generated-code
  edits, CubeMX / Workbench edits, flash, Run / Debug, motor connection,
  Gate PWM, Motor Pilot, Motor Profiler, Hall closed loop, sensorless
  operation, power-stage readiness, or motor readiness.
- Next checkpoint:
  with HSPY output OFF, `VS / 24V_FUSED < 1 V`, motor disconnected, and the
  `10 kohm` stimulus removed, collect raw no-power DMM results for
  `CN3_2-LIN1` to `3V3` / `GND` and `CN3_13-nFAULT` to `3V3` / `GND`, or
  provide a source packet identifying `SCREF`, `CP`, `REG12`, and `OUT1`.

## Current 2026-06-19 STDRIVE101 Single-Input Wake Fault Result

- Task:
  `TASK-2026-06-19-stdrive101-single-input-wake-fault-result`.
- Evidence:
  `EV-2026-06-19-STDRIVE101-SINGLE-INPUT-WAKE-FAULT-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_reg12_single_input_wake_fault_result_2026-06-19.md`.
- User-reported raw readings:
  `wake_supply_state = CV`, `wake_supply_current_A = 0.046 A`,
  `wake_CN3_2_LIN1_V = 3 V`, `wake_CN3_13_nFAULT_V = 0 V`,
  `wake_REG12_V = 12 V`, and post-off `VS / 24V_FUSED = 0 V`.
- Decision:
  `STDRIVE101 REG12 single-input wake result / CN3_14 3V3 through 10 kohm to
  CN3_2 LIN1 / LIN1 3 V / HSPY CV 0.046 A / REG12 rose to 12 V / nFAULT 0 V
  stop-rule event / post-off VS reported 0 V / no retry before fault-cause
  review / no PWM-output validation / no powered-drive readiness`.
- Scope:
  records the bounded diagnostic result only. It separates the observed
  `REG12` rise from the failing `nFAULT` state.
- Boundary:
  this does not authorize a repeat powered wake diagnostic, a different input
  stimulus, firmware implementation, generated-code edits, CubeMX / Workbench
  edits, flash, Run / Debug, motor connection, Gate PWM, Motor Pilot,
  Motor Profiler, Hall closed loop, sensorless operation, power-stage
  readiness, or motor readiness.
- Next checkpoint:
  keep HSPY output OFF, remove the `10 kohm` stimulus resistor if not already
  removed after confirming `VS / 24V_FUSED < 1 V`, then proceed only with
  no-power or source review of `nFAULT` causes and board conditions.

## Current 2026-06-19 Software Hall Code-Entry Boundary After DMM

- Task:
  `TASK-2026-06-19-software-hall-code-entry-boundary-post-dmm`.
- Evidence:
  `EV-2026-06-19-SOFTWARE-HALL-CODE-ENTRY-BOUNDARY-POST-DMM-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_code_entry_boundary_after_dmm_2026-06-19.md`.
- Decision:
  `Software Hall code-entry boundary after DMM summary /
  PA0-PA1-PB4 debug-only adapter planning allowed / no firmware
  implementation / no MCSDK hook / no Hall readiness`.
- Scope:
  defines the next no-power document-side work after the DMM summary: exact
  future file list, GPIO pull / EXTI trigger policy review, timestamp-source
  criteria, low-frequency debug snapshot route, no-power build checklist, and
  rollback checklist.
- Boundary:
  this does not create STM32 firmware, edit generated MCSDK files, edit
  CubeMX / Workbench, flash, Run / Debug, apply 24 V, connect a motor, output
  Gate PWM, run Motor Pilot, run Motor Profiler, claim GPIO runtime proof,
  claim MCSDK hook readiness, claim Hall closed-loop behavior, claim
  power-stage readiness, claim motor readiness, or claim sensorless
  validation.

## Current 2026-06-19 PCB2 No-Power DMM Summary Result

- Task:
  `TASK-2026-06-19-pcb2-no-power-dmm-summary`.
- Evidence:
  `EV-2026-06-19-PCB2-NO-POWER-DMM-SUMMARY-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/pcb2_no_power_dmm_continuity_short_check_result_2026-06-19.md`.
- User-reported continuity rows:
  `CN3_10 / IA -> CN4-A0 / PA0`, `CN3_11 / IB -> CN4-A1 / PA1`,
  `CN3_12 / IC -> CN5-D5 / PB4`, `CN3_2 / LIN1 -> CN10-D12 / PB3`,
  `CN3_14 / 3V3 -> CN4-3V3`, `CN3_15 / GND -> CN4-GND`, and
  `CN3_13 / nFAULT -> CN10-D14 / PB12` are reported as `通`.
- User-reported short-check rows:
  all requested rail, signal-to-rail, and Hall-pair rows are reported as
  `不通`.
- Decision:
  `PCB2 no-power DMM continuity / short-check summary / expected continuity
  reported for CN3_10-PA0, CN3_11-PA1, CN3_12-PB4, CN3_2-PB3, CN3_14-3V3,
  CN3_15-GND, and CN3_13-PB12 / no rail, signal-to-rail, or Hall-line hard
  short reported / raw ohm values not provided / no powered readiness`.
- Boundary:
  this is a no-power DMM summary only. It opens only no-power software Hall
  adapter interface / code-entry boundary planning. It does not authorize
  firmware implementation, generated-code edits, CubeMX / Workbench edits,
  flash, Run / Debug, 24 V, power-board connection, motor connection, Gate
  PWM, Motor Pilot, Motor Profiler, Hall closed loop, sensorless operation,
  power-stage readiness, or motor readiness.

## Current 2026-06-19 STDRIVE101 Single-Input Wake Baseline

- Task:
  `TASK-2026-06-19-stdrive101-single-input-wake-baseline`.
- Evidence:
  `EV-2026-06-19-STDRIVE101-SINGLE-INPUT-WAKE-BASELINE-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_reg12_single_input_wake_baseline_result_2026-06-19.md`.
- User-reported raw readings:
  `CV`, `0.036 A`, `VS / 24V_FUSED = 24 V`,
  `CN3_14 / 3V3 = 3.3 V`, `CN3_13 / nFAULT = 3.3 V`, and
  `REG12 = 0.33 V`.
- Decision:
  `STDRIVE101 REG12 single-input wake baseline / HSPY 24 V 0.2 A CV /
  0.036 A static current / VS 24 V / CN3_14 3.3 V present with USB-STLINK
  unplugged / nFAULT 3.3 V / REG12 0.33 V / pre-stimulus baseline satisfied
  only / no wake stimulus installed / no PWM-output validation / no powered-drive
  readiness`.
- Boundary:
  this is a static baseline record only. It does not install the `10 kohm`
  stimulus, drive `CN3_2 / LIN1` high, execute the wake diagnostic, validate
  Gate PWM, validate Hall closed-loop behavior, validate sensorless behavior,
  or prove power-stage / motor readiness.
- Next allowed hardware step, if the user chooses to continue:
  `CN3_14 / 3V3 -> 10 kohm series resistor -> CN3_2 / LIN1`, motor
  disconnected, HSPY `24 V / 0.2 A`, no firmware PWM, no Motor Pilot, no
  Motor Profiler, strict CV/CC stop rules, and no direct wire.

## Current 2026-06-19 STDRIVE101 Single-Input Wake Handoff

- Task:
  `TASK-2026-06-19-stdrive101-single-input-wake-handoff`.
- Evidence:
  `EV-2026-06-19-STDRIVE101-SINGLE-INPUT-WAKE-HANDOFF-001`.
- Trigger phrase:
  if the user says `开始单输入唤醒诊断`, `单输入唤醒`, `STDRIVE101 唤醒`, or
  `REG12 唤醒`, route to this hardware handoff, not Codex mobile wakeup,
  CodexMobileWeb, service wakeup, or automation wakeup.
- Required files to read before giving the checklist:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_reg12_single_input_wake_plan_2026-06-19.md`,
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_reg12_wake_official_web_review_2026-06-19.md`,
  and
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/out1_output_node_no_power_short_check_result_2026-06-19.md`.
- Candidate diagnostic:
  `CN3_14 / 3V3 -> 10 kohm series resistor -> CN3_2 / LIN1`.
- Required powered setup if the user explicitly opens the execution gate:
  motor disconnected, HSPY `24 V / 0.2 A`, CN3 connected as in the static
  check, no firmware PWM, no Motor Pilot, no Motor Profiler.
- Boundary:
  this is not motor validation, not PWM validation, not Hall closed-loop, not
  sensorless operation, not power-stage readiness, and not motor readiness.

## Current 2026-06-17 Three-Hour Optimization Sprint Addendum

- Task:
  `TASK-2026-06-17-three-hour-optimization-sprint`.
- Evidence:
  `EV-2026-06-17-THREE-HOUR-OPTIMIZATION-SPRINT-001`.
- Decision:
  `Three-hour optimization sprint / subagent protocol / Obsidian Chinese learning notes / retrieval maintainability / no hardware or firmware action`.
- Scope:
  implemented the requested structured optimization sprint across AI
  architecture, Obsidian Chinese learning notes, and low-risk retrieval
  maintainability. `workflow/three_hour_optimization_report_2026-06-17.md`
  records the timebox, role split, timestamped progress, mid-project review,
  completed components, retrieval checks, verification plan, and efficiency
  recommendations.
- Integration:
  subagent exploration and implementation outputs were filtered before
  main-agent integration. Failed subagent slices were inspected and recovered
  by the main agent rather than accepted blindly.
- Boundary:
  repo-maintenance documentation, notes, retrieval, and tests only. No firmware
  implementation, no generated-code edit, no CubeMX/MCSDK edit, no flash, no
  24V, no power-board connection, no motor connection, no Gate PWM, no Motor
  Profiler, no Hall closed-loop, and no sensorless / SMO claim.
- Review lifecycle:
  this addendum does not mark the earlier `done + Review Required` software
  Hall task as `reviewed`; user review still clears strict warnings.

## Current 2026-06-17 AI Architecture Subagent Protocol Addendum

- Task:
  `TASK-2026-06-17-ai-architecture-subagent-protocol`.
- Evidence:
  `EV-2026-06-17-AI-ARCHITECTURE-SUBAGENT-PROTOCOL-001`.
- Decision:
  `AI architecture subagent protocol / hierarchical task decomposition / context filtering / summarized handoff / no hardware or firmware action`.
- Scope:
  updated `docs/00_project_truth/ai_architecture.md` with a structured
  subagent communication protocol, hierarchical task decomposition, context
  filtering rules, a summary gate, and an old-flat-vs-new-filtered comparison.
  The status files now point at the updated architecture contract so the
  low-token handoff path keeps the new protocol visible.
- Boundary:
  repo-maintenance documentation only. No firmware implementation, no
  generated-code edit, no CubeMX/MCSDK edit, no flash, no 24V, no power-board
  connection, no motor connection, no Gate PWM, no Motor Profiler, no Hall
  closed-loop, and no sensorless / SMO claim.
- Review lifecycle:
  this addendum does not mark the earlier `done + Review Required` software
  Hall task as `reviewed`; user review still clears strict warnings.

## Current 2026-06-17 AI Maintenance Audit Readability Status Addendum

- Task:
  `TASK-2026-06-17-ai-maintenance-audit-readability-status`.
- Evidence:
  `EV-2026-06-17-AI-MAINTENANCE-AUDIT-READABILITY-STATUS-001`.
- Decision:
  `AI maintenance audit readability status / entry-header versus legacy-debt handoff / no hardware or firmware action`.
- Scope:
  extended `tools/run_ai_maintenance_audit.py` with
  `readability_status_from_repo()`, `readability_header_status_from_repo()`,
  and `readability_legacy_debt_status_from_repo()`. The audit now exposes
  top-level `readability_status` with `entry_headers_ok`,
  `guarded_entry_files`, `legacy_debt_present`, `legacy_debt_count`,
  `legacy_debt_paths`, `full_legacy_cleanup_claimed`, and
  `hardware_validation: false`. Updated contract checks, tests, retrieval
  expansion/eval, low-token docs, file index, tools README, and project Skill
  workflow-maintenance reference.
- Verification:
  passed with
  `python -m py_compile tools\run_ai_maintenance_audit.py tools\check_ai_contracts.py tools\search_local_v2.py tests\test_ai_architecture_contracts.py`,
  `python -m unittest tests.test_ai_architecture_contracts`,
  `python tools\check_ai_contracts.py` with 0 errors and the two known
  review-lifecycle warnings,
  `python tools\build_vector_store.py`,
  `python tools\search_local_v2.py --eval`,
  `python -m unittest discover -s tests`,
  `python -m compileall src tests`,
  `git diff --check` with only existing CRLF conversion warnings,
  `python -X utf8 C:\Users\gregrg\.codex\skills\.system\skill-creator\scripts\quick_validate.py codex_skills\stm32g474-foc-assistant`,
  `python tools\check_project_skill_install.py --repo-only --json`,
  `powershell -ExecutionPolicy Bypass -File .\tools\install_project_skill.ps1`,
  `python tools\check_project_skill_install.py`,
  `python tools\build_context_pack.py --mode workflow_maintenance --max-chars 350`,
  and `python tools\run_ai_maintenance_audit.py --json --max-output-chars 700`.
  The full audit returned `ok: true`, `repo_maintenance_closeout_ok: true`,
  `readability_status.entry_headers_ok: true`,
  `readability_status.legacy_debt_present: true`, and
  `hardware_validation: false`.
- Boundary:
  `readability_status` is repo-text handoff evidence only. It separates the
  guarded entry headers from broader legacy mojibake debt and does not claim
  full historical cleanup, inspect hardware, run firmware, clean the worktree,
  or validate readiness. No DMM table fill, no firmware implementation, no
  generated-code edit, no CubeMX/MCSDK edit, no flash, no 24V, no power-board
  connection, no motor connection, no Gate PWM, no Motor Profiler, no Hall
  closed-loop, and no sensorless / SMO claim.
- Review lifecycle:
  this addendum does not mark the earlier `done + Review Required` software
  Hall task as `reviewed`; user review still clears strict warnings.

## Current 2026-06-10 Entry Readability Contract Addendum

- Task:
  `TASK-2026-06-10-entry-readability-contract`.
- Evidence:
  `EV-2026-06-10-ENTRY-READABILITY-CONTRACT-001`.
- Decision:
  `High-value entry readability repair / UTF-8 header contract / no hardware or firmware action`.
- Scope:
  restored the readable entry header and weekly/phase template fields in
  `deliverables/submission_checklist.md`, restored the title and evidence
  boundary in `workflow/evidence_register.md`, and extended
  `tools/check_ai_contracts.py` with `READABILITY_HEADER_REQUIREMENTS`,
  `READABILITY_MOJIBAKE_MARKERS`, and `check_readability_headers()`. Added
  unit coverage, retrieval expansion/eval, architecture/index/tool docs, and
  project Skill workflow-maintenance guidance.
- Verification:
  passed with
  `python -m py_compile tools\check_ai_contracts.py tools\search_local_v2.py`,
  `python -m unittest tests.test_ai_architecture_contracts`,
  `python tools/check_ai_contracts.py` with 0 errors and the two known
  review-lifecycle warnings,
  `python -X utf8 C:\Users\gregrg\.codex\skills\.system\skill-creator\scripts\quick_validate.py codex_skills\stm32g474-foc-assistant`,
  `python tools/check_project_skill_install.py --repo-only --json`,
  `powershell -ExecutionPolicy Bypass -File .\tools\install_project_skill.ps1`,
  `python tools/check_project_skill_install.py`,
  `python tools/build_vector_store.py`,
  `python tools/search_local_v2.py --eval`,
  `python -m unittest tests.test_search_local_v2 tests.test_ai_architecture_contracts tests.test_workflow_contracts`,
  and `python tools/run_ai_maintenance_audit.py --json --max-output-chars 700`.
  The full audit passed with 143 discovered tests, retrieval eval, compileall,
  Skill install drift check, `closeout_summary.repo_maintenance_closeout_ok:
  true`, and `git diff --check`; diff check output only contained existing
  CRLF conversion warnings.
- Boundary:
  this repairs and guards the high-value entry headers only. It does not claim
  that every legacy historical mojibake row is repaired, change task state,
  inspect hardware, run firmware, or validate readiness. No DMM table fill, no
  firmware implementation, no generated-code edit, no CubeMX/MCSDK edit, no
  flash, no 24V, no power-board connection, no motor connection, no Gate PWM,
  no Motor Profiler, no Hall closed-loop, and no sensorless / SMO claim.
- Review lifecycle:
  this addendum does not mark the earlier `done + Review Required` software
  Hall task as `reviewed`; user review still clears strict warnings.

## Current 2026-06-10 AI Maintenance Audit Closeout Summary Addendum

- Task:
  `TASK-2026-06-10-ai-maintenance-audit-closeout-summary`.
- Evidence:
  `EV-2026-06-10-AI-MAINTENANCE-AUDIT-CLOSEOUT-SUMMARY-001`.
- Decision:
  `AI maintenance audit closeout summary / top-level repo-maintenance handoff / no hardware or firmware action`.
- Scope:
  extended `tools/run_ai_maintenance_audit.py` with
  `closeout_summary_from_statuses()` and top-level `closeout_summary`. The
  summary reports `repo_maintenance_closeout_ok`, `strict_ready`,
  `needs_user_review`, dirty-worktree state, dirty entry count, next review
  group/focus, `no_power_boundary_active`, and `hardware_validation: false`.
  Updated tests, contract checks, retrieval eval, low-token docs, file index,
  tools README, and project Skill workflow-maintenance reference.
- Verification:
  passed with
  `python -m py_compile tools\run_ai_maintenance_audit.py tools\check_ai_contracts.py tools\search_local_v2.py`,
  `python -m unittest tests.test_ai_architecture_contracts`,
  `python tools/check_ai_contracts.py` with 0 errors and the two known
  review-lifecycle warnings,
  `python -X utf8 C:\Users\gregrg\.codex\skills\.system\skill-creator\scripts\quick_validate.py codex_skills\stm32g474-foc-assistant`,
  `python tools/check_project_skill_install.py --repo-only --json`,
  `powershell -ExecutionPolicy Bypass -File .\tools\install_project_skill.ps1`,
  `python tools/check_project_skill_install.py`,
  `python tools/build_context_pack.py --mode workflow_maintenance --max-chars 350`,
  `python tools/build_vector_store.py`,
  `python tools/search_local_v2.py --eval`,
  `python -m unittest tests.test_search_local_v2 tests.test_ai_architecture_contracts`,
  and `python tools/run_ai_maintenance_audit.py --json --max-output-chars 700`.
  The full audit passed with `closeout_summary.repo_maintenance_closeout_ok:
  true`, `strict_ready: false`, `needs_user_review: true`, 0 contract errors,
  0 unexpected warnings, 2 known review-lifecycle warnings, 142 discovered unit
  tests, compileall, Skill install drift check, retrieval eval, and
  `git diff --check`; diff check output only contained existing CRLF
  conversion warnings.
- Boundary:
  `closeout_summary` is derived from audit outputs only. It does not
  self-clear required review, change task state, inspect hardware, run
  firmware, clean the worktree, or validate readiness. No external GitHub Skill
  install, no DMM table fill, no firmware implementation, no generated-code
  edit, no CubeMX/MCSDK edit, no flash, no 24V, no power-board connection, no
  motor connection, no Gate PWM, no Motor Profiler, no Hall closed-loop, and no
  sensorless / SMO claim.
- Review lifecycle:
  this addendum does not mark the earlier `done + Review Required` software
  Hall task as `reviewed`; user review still clears strict warnings.

## Current 2026-06-10 AI Maintenance Audit Contract Status Addendum

- Task:
  `TASK-2026-06-10-ai-maintenance-audit-contract-status`.
- Evidence:
  `EV-2026-06-10-AI-MAINTENANCE-AUDIT-CONTRACT-STATUS-001`.
- Decision:
  `AI maintenance audit contract status / review-lifecycle warning classification / no hardware or firmware action`.
- Scope:
  extended `tools/run_ai_maintenance_audit.py` with
  `REVIEW_LIFECYCLE_WARNING_MARKERS`, `parse_contract_output()`, and
  `contract_status_from_results()`. The audit now exposes top-level
  `contract_status` with error and warning counts, review-lifecycle warning
  count, unexpected warning count, `strict_ready`, and
  `implementation_closeout_ok`. Markdown reports now include a `Contract
  Status` section. Updated tests, retrieval eval, low-token docs, file index,
  tools README, and project Skill workflow-maintenance reference. Added
  `MAINTENANCE_SOURCE_FILES` in `tools/build_vector_store.py` so maintenance
  tool scripts, tests, and eval JSON stay indexed for local retrieval. Updated
  `tools/search_local_v2.py` with path-aware topic-entry scoring so workflow
  entry files and the `tools/check_ai_contracts.py` dangerous-claim
  implementation remain discoverable after status/evidence docs grow.
- Verification:
  passed with
  `python tools/build_context_pack.py --mode workflow_maintenance --max-chars 350`,
  `python tools/check_ai_contracts.py` with 0 errors and the two known
  review-lifecycle warnings, `python tools/check_project_skill_install.py`,
  `python tools/build_vector_store.py`, `python tools/search_local_v2.py --eval`,
  `python -m unittest tests.test_search_local_v2 tests.test_ai_architecture_contracts`
  with 18 tests OK, and
  `python tools/run_ai_maintenance_audit.py --json --max-output-chars 700`.
  The full audit passed with retrieval eval, 142 discovered unit tests,
  compileall, Skill install drift check, and `git diff --check`; diff check
  output only contained existing CRLF conversion warnings.
- Boundary:
  `contract_status` is a parsed contract-output handoff summary only. It does
  not self-clear required review, change task state, inspect hardware, run
  firmware, clean the worktree, or validate readiness. No external GitHub Skill
  install, no DMM table fill, no firmware implementation, no generated-code
  edit, no CubeMX/MCSDK edit, no flash, no 24V, no power-board connection, no
  motor connection, no Gate PWM, no Motor Profiler, no Hall closed-loop, and no
  sensorless / SMO claim.
- Review lifecycle:
  this addendum does not mark the earlier `done + Review Required` software
  Hall task as `reviewed`; user review still clears strict warnings.

## Current 2026-06-09 Dangerous Claim Scan Surface Addendum

- Task:
  `TASK-2026-06-09-ai-contract-dangerous-claim-scan-surface`.
- Evidence:
  `EV-2026-06-09-AI-CONTRACT-DANGEROUS-CLAIM-SCAN-SURFACE-001`.
- Decision:
  `AI contract dangerous claim scan surface / broader no-power static text scan / no hardware or firmware action`.
- Scope:
  extended `tools/check_ai_contracts.py` with `DANGEROUS_CLAIM_SCAN_PATHS`,
  `DANGEROUS_CLAIM_SCAN_SUFFIXES`, `is_dangerous_claim_scan_candidate()`, and
  `iter_dangerous_claim_scan_files()`, so dangerous positive hardware claims
  are scanned across project truth, workflow, project Skill, no-power
  precheck, deliverable, interface, and learning text rather than only a few
  entry files. Updated tests, retrieval eval, docs, and project Skill
  workflow-maintenance reference.
- Verification:
  `python tools/check_ai_contracts.py`,
  targeted dangerous-claim-scan tests in
  `tests/test_ai_architecture_contracts.py`,
  `python tools/build_vector_store.py`,
  `python -m json.tool retrieval_eval\queries.json`,
  targeted `rg` dangerous-phrase sweep across the scanned maintenance surface,
  `python tools/search_local_v2.py --eval`,
  `python -X utf8 C:\Users\gregrg\.codex\skills\.system\skill-creator\scripts\quick_validate.py codex_skills\stm32g474-foc-assistant`,
  `python tools/check_project_skill_install.py --repo-only --json`,
  `powershell -ExecutionPolicy Bypass -File .\tools\install_project_skill.ps1`,
  `python tools/check_project_skill_install.py`,
  `python tools/build_context_pack.py --mode workflow_maintenance --max-chars 350`,
  and `python tools/run_ai_maintenance_audit.py --json --max-output-chars 700`.
- Boundary:
  this is a static text scan only; it does not inspect hardware, run firmware,
  clean the worktree, or validate readiness. No external GitHub Skill install,
  no DMM table fill, no firmware implementation, no generated-code edit, no
  CubeMX/MCSDK edit, no flash, no 24V, no power-board connection, no motor
  connection, no Gate PWM, no Motor Profiler, no Hall closed-loop, and no
  sensorless / SMO claim.
- Review lifecycle:
  this addendum does not mark the earlier `done + Review Required` software
  Hall task as `reviewed`; user review still clears strict warnings.

## Current 2026-06-09 AI Maintenance Audit Handoff Review Queue Addendum

- Task:
  `TASK-2026-06-09-ai-maintenance-audit-handoff-review-queue`.
- Evidence:
  `EV-2026-06-09-AI-MAINTENANCE-AUDIT-HANDOFF-REVIEW-QUEUE-001`.
- Decision:
  `AI maintenance audit handoff review queue / group-specific dirty-worktree review focus / no hardware or firmware action`.
- Scope:
  extended `tools/run_ai_maintenance_audit.py` with `GROUP_REVIEW_FOCUS` and
  `build_handoff_review_queue()`, added
  `workspace_status.handoff_review_queue`, added Markdown
  `Handoff Review Queue` output, and updated tests, contracts, retrieval,
  docs, and project Skill workflow-maintenance reference.
- Verification:
  `python tools/run_ai_maintenance_audit.py --check git_status --json --max-output-chars 1`,
  targeted audit tests in `tests/test_ai_architecture_contracts.py`,
  `python tools/check_ai_contracts.py`,
  `python -X utf8 C:\Users\gregrg\.codex\skills\.system\skill-creator\scripts\quick_validate.py codex_skills\stm32g474-foc-assistant`,
  `python tools/check_project_skill_install.py --repo-only --json`,
  `powershell -ExecutionPolicy Bypass -File .\tools\install_project_skill.ps1`,
  `python tools/check_project_skill_install.py`,
  `python tools/build_context_pack.py --mode workflow_maintenance --max-chars 350`,
  and `python tools/run_ai_maintenance_audit.py --json --max-output-chars 700`.
- Boundary:
  `handoff_review_queue` is parsed handoff guidance only; it does not hide,
  clean, reorder, revert, stage, commit, or validate the dirty worktree. No
  external GitHub Skill install, no DMM table fill, no firmware
  implementation, no generated-code edit, no CubeMX/MCSDK edit, no flash, no
  24V, no power-board connection, no motor connection, no Gate PWM, no Motor
  Profiler, no Hall closed-loop, and no sensorless / SMO claim.
- Review lifecycle:
  this addendum does not mark the earlier `done + Review Required` software
  Hall task as `reviewed`; user review still clears strict warnings.

## Current 2026-06-09 AI Maintenance Audit Focus Groups Addendum

- Task:
  `TASK-2026-06-09-ai-maintenance-audit-focus-groups`.
- Evidence:
  `EV-2026-06-09-AI-MAINTENANCE-AUDIT-FOCUS-GROUPS-001`.
- Decision:
  `AI maintenance audit focus groups / ordered dirty-worktree handoff / no hardware or firmware action`.
- Scope:
  extended `tools/run_ai_maintenance_audit.py` with `GROUP_FOCUS_ORDER` and
  `summarize_focus_groups()`, added `workspace_status.focus_groups`, added
  Markdown `Focus Groups` output, and updated tests, contracts, retrieval,
  docs, and project Skill workflow-maintenance reference.
- Verification:
  `python tools/run_ai_maintenance_audit.py --quick --repo-only-skill --json --max-output-chars 1`,
  `python tools/check_project_skill_install.py`,
  `python tools/run_ai_maintenance_audit.py --json --max-output-chars 700`,
  `python tools/check_ai_contracts.py`,
  `python tools/build_vector_store.py`,
  `python tools/search_local_v2.py --eval`,
  `python -m unittest discover -s tests`,
  `python -m compileall src tests`,
  `git status --short`, and `git diff --check`.
- Boundary:
  `focus_groups` are parsed handoff evidence only; they do not hide, clean,
  reorder, revert, stage, commit, or validate the dirty worktree. No external
  GitHub Skill install, no DMM table fill, no firmware implementation, no
  generated-code edit, no CubeMX/MCSDK edit, no flash, no 24V, no power-board
  connection, no motor connection, no Gate PWM, no Motor Profiler, no Hall
  closed-loop, and no sensorless / SMO claim.
- Review lifecycle:
  this addendum does not mark the earlier `done + Review Required` software
  Hall task as `reviewed`; user review still clears strict warnings.

## Current 2026-06-09 AI Maintenance Audit Status Paths Addendum

- Task:
  `TASK-2026-06-09-ai-maintenance-audit-status-paths`.
- Evidence:
  `EV-2026-06-09-AI-MAINTENANCE-AUDIT-STATUS-PATHS-001`.
- Decision:
  `AI maintenance audit status paths / status-code dirty-worktree handoff / no hardware or firmware action`.
- Scope:
  extended `tools/run_ai_maintenance_audit.py` with
  `summarize_status_paths()` and `workspace_status.status_paths`, added
  Markdown `Status Paths` output, and updated tests, contracts, retrieval,
  docs, and project Skill workflow-maintenance reference.
- Verification:
  `python tools/run_ai_maintenance_audit.py --quick --repo-only-skill --json --max-output-chars 1`,
  `python tools/check_project_skill_install.py`,
  `python tools/run_ai_maintenance_audit.py --json --max-output-chars 700`,
  `python tools/check_ai_contracts.py`,
  `python tools/build_vector_store.py`,
  `python tools/search_local_v2.py --eval`,
  `python -m unittest discover -s tests`,
  `python -m compileall src tests`,
  `git status --short`, and `git diff --check`.
- Boundary:
  `status_paths` are parsed handoff evidence only; they do not hide, clean,
  reorder, revert, stage, commit, or validate the dirty worktree. No external
  GitHub Skill install, no DMM table fill, no firmware implementation, no
  generated-code edit, no CubeMX/MCSDK edit, no flash, no 24V, no power-board
  connection, no motor connection, no Gate PWM, no Motor Profiler, no Hall
  closed-loop, and no sensorless / SMO claim.
- Review lifecycle:
  this addendum does not mark the earlier `done + Review Required` software
  Hall task as `reviewed`; user review still clears strict warnings.

## Current 2026-06-09 AI Maintenance Audit Workspace Path Groups Addendum

- Task:
  `TASK-2026-06-09-ai-maintenance-audit-workspace-path-groups`.
- Evidence:
  `EV-2026-06-09-AI-MAINTENANCE-AUDIT-WORKSPACE-PATH-GROUPS-001`.
- Decision:
  `AI maintenance audit workspace path groups / repository-area dirty-worktree handoff / no hardware or firmware action`.
- Scope:
  extended `tools/run_ai_maintenance_audit.py` with
  `classify_path_group()` and `workspace_status.path_groups`, added Markdown
  `Path Groups` output, and updated tests, contracts, retrieval, docs, and
  project Skill workflow-maintenance reference.
- Verification:
  `python tools/run_ai_maintenance_audit.py --quick --repo-only-skill --json --max-output-chars 1`,
  `python tools/check_project_skill_install.py`,
  `python tools/run_ai_maintenance_audit.py --json --max-output-chars 700`,
  `python tools/check_ai_contracts.py`,
  `python tools/build_vector_store.py`,
  `python tools/search_local_v2.py --eval`,
  `python -m unittest discover -s tests`,
  `python -m compileall src tests`,
  `git status --short`, and `git diff --check`.
- Boundary:
  `path_groups` are parsed handoff evidence only; they do not hide, clean,
  reorder, revert, stage, commit, or validate the dirty worktree. No external
  GitHub Skill install, no DMM table fill, no firmware implementation, no
  generated-code edit, no CubeMX/MCSDK edit, no flash, no 24V, no power-board
  connection, no motor connection, no Gate PWM, no Motor Profiler, no Hall
  closed-loop, and no sensorless / SMO claim.
- Review lifecycle:
  this addendum does not mark the earlier `done + Review Required` software
  Hall task as `reviewed`; user review still clears strict warnings.

## Current 2026-06-09 AI Maintenance Audit Workspace Status Addendum

- Task:
  `TASK-2026-06-09-ai-maintenance-audit-workspace-status-summary`.
- Evidence:
  `EV-2026-06-09-AI-MAINTENANCE-AUDIT-WORKSPACE-STATUS-SUMMARY-001`.
- Decision:
  `AI maintenance audit workspace-status summary / machine-readable dirty-worktree handoff / no hardware or firmware action`.
- Scope:
  extended `tools/run_ai_maintenance_audit.py` with
  `parse_git_status_short()` and a top-level `workspace_status` object derived
  from the existing full `git_status` output. Updated Markdown report output,
  tests, contracts, retrieval, docs, and project Skill workflow-maintenance
  reference.
- Verification:
  `python tools/run_ai_maintenance_audit.py --quick --repo-only-skill --json --max-output-chars 1`,
  `python tools/check_project_skill_install.py`,
  `python tools/run_ai_maintenance_audit.py --json --max-output-chars 700`,
  `python tools/check_ai_contracts.py`,
  `python tools/build_vector_store.py`,
  `python tools/search_local_v2.py --eval`,
  `python -m unittest discover -s tests`,
  `python -m compileall src tests`,
  `git status --short`, and `git diff --check`.
- Boundary:
  `workspace_status` is parsed handoff evidence only; it does not run extra git
  commands, clean, reorder, revert, stage, commit, or validate the dirty
  worktree. No external GitHub Skill install, no DMM table fill, no firmware
  implementation, no generated-code edit, no CubeMX/MCSDK edit, no flash, no
  24V, no power-board connection, no motor connection, no Gate PWM, no Motor
  Profiler, no Hall closed-loop, and no sensorless / SMO claim.
- Review lifecycle:
  this addendum does not mark the earlier `done + Review Required` software
  Hall task as `reviewed`; user review still clears strict warnings.

## Current 2026-06-09 AI Maintenance Audit Full Git Status Addendum

- Task:
  `TASK-2026-06-09-ai-maintenance-audit-preserve-git-status-output`.
- Evidence:
  `EV-2026-06-09-AI-MAINTENANCE-AUDIT-PRESERVE-GIT-STATUS-OUTPUT-001`.
- Decision:
  `AI maintenance audit full git-status output / dirty-worktree handoff evidence not truncated / no hardware or firmware action`.
- Scope:
  extended `tools/run_ai_maintenance_audit.py` with per-step output policy;
  normal steps remain tail-limited, while `git_status` uses
  `preserve_output=True` and reports `output_policy: full`. Updated tests,
  contracts, retrieval, docs, and project Skill workflow-maintenance reference.
- Verification:
  `python tools/run_ai_maintenance_audit.py --quick --repo-only-skill --json --max-output-chars 1`,
  `python tools/check_project_skill_install.py`,
  `python tools/run_ai_maintenance_audit.py --json --max-output-chars 700`,
  `python tools/check_ai_contracts.py`,
  `python tools/build_vector_store.py`,
  `python tools/search_local_v2.py --eval`,
  `python -m unittest discover -s tests`,
  `python -m compileall src tests`,
  `git status --short`, and `git diff --check`.
- Boundary:
  full `git_status` output is handoff evidence only; it does not clean,
  reorder, revert, stage, commit, or validate the dirty worktree. No external
  GitHub Skill install, no DMM table fill, no firmware implementation, no
  generated-code edit, no CubeMX/MCSDK edit, no flash, no 24V, no power-board
  connection, no motor connection, no Gate PWM, no Motor Profiler, no Hall
  closed-loop, and no sensorless / SMO claim.
- Review lifecycle:
  this addendum does not mark the earlier `done + Review Required` software
  Hall task as `reviewed`; user review still clears strict warnings.

## Current 2026-06-08 AI Maintenance Audit Git Status Addendum

- Task:
  `TASK-2026-06-08-ai-maintenance-audit-git-status-step`.
- Evidence:
  `EV-2026-06-08-AI-MAINTENANCE-AUDIT-GIT-STATUS-001`.
- Decision:
  `AI maintenance audit git-status step / dirty-worktree handoff evidence / no hardware or firmware action`.
- Scope:
  extended `tools/run_ai_maintenance_audit.py` with a read-only
  `git_status` step that runs `git status --short`, included it in full and
  quick audits, and updated tests, contracts, retrieval, docs, and project
  Skill workflow-maintenance reference.
- Verification:
  `python tools/run_ai_maintenance_audit.py --quick --repo-only-skill --json --max-output-chars 300`,
  `python tools/check_project_skill_install.py`,
  `python tools/run_ai_maintenance_audit.py --json --max-output-chars 700`,
  `python tools/check_ai_contracts.py`,
  `python tools/build_vector_store.py`,
  `python tools/search_local_v2.py --eval`,
  `python -m unittest discover -s tests`,
  `python -m compileall src tests`,
  `git status --short`, and `git diff --check`.
- Boundary:
  git-status capture is handoff evidence only; it does not clean, reorder,
  revert, stage, commit, or validate the dirty worktree. No external GitHub
  Skill install, no DMM table fill, no firmware implementation, no
  generated-code edit, no CubeMX/MCSDK edit, no flash, no 24V, no power-board
  connection, no motor connection, no Gate PWM, no Motor Profiler, no Hall
  closed-loop, and no sensorless / SMO claim.
- Review lifecycle:
  this addendum does not mark the earlier `done + Review Required` software
  Hall task as `reviewed`; user review still clears strict warnings.

## Current 2026-06-08 AI Maintenance Audit Markdown Report Addendum

- Task:
  `TASK-2026-06-08-ai-maintenance-audit-markdown-report`.
- Evidence:
  `EV-2026-06-08-AI-MAINTENANCE-AUDIT-MARKDOWN-REPORT-001`.
- Decision:
  `AI maintenance audit Markdown report output / explicit write-report mode / no hardware or firmware action`.
- Scope:
  extended `tools/run_ai_maintenance_audit.py` with explicit
  `--write-report <path>` output, added temp-file test coverage, and updated
  contracts, retrieval, docs, and project Skill workflow-maintenance reference.
- Verification:
  `python tools/run_ai_maintenance_audit.py --json --max-output-chars 500`,
  `python tools/check_project_skill_install.py`,
  `python tools/build_vector_store.py`,
  `python tools/search_local_v2.py --eval`,
  `python -m unittest discover -s tests`,
  `python -m compileall src tests`, and `git diff --check`.
- Boundary:
  explicit Markdown report output only, repo-local project Skill reinstall only,
  no external GitHub Skill install, no DMM table fill, no firmware
  implementation, no generated-code edit, no CubeMX/MCSDK edit, no flash, no
  24V, no power-board connection, no motor connection, no Gate PWM, no Motor
  Profiler, no Hall closed-loop, and no sensorless / SMO claim.
- Review lifecycle:
  this addendum does not mark the earlier `done + Review Required` software
  Hall task as `reviewed`; user review still clears strict warnings.

## Current 2026-06-08 AI Maintenance Audit Runner Addendum

- Task:
  `TASK-2026-06-08-ai-maintenance-audit-runner`.
- Evidence:
  `EV-2026-06-08-AI-MAINTENANCE-AUDIT-RUNNER-001`.
- Decision:
  `AI maintenance audit runner / consolidated no-power closeout checks / no hardware or firmware action`.
- Scope:
  added `tools/run_ai_maintenance_audit.py`, wired it into context packs,
  contract checks, retrieval eval, docs, and tests, then used it to run the
  full no-power AI maintenance closeout set.
- Verification:
  `python tools/run_ai_maintenance_audit.py --json --max-output-chars 800`
  returned `ok: true`, including Skill validation, installed Skill drift
  check, `workflow_maintenance` context pack, AI contracts, vector-store
  rebuild, retrieval eval, unit tests, compileall, and `git diff --check`.
- Boundary:
  repo-local project Skill reinstall only, no external GitHub Skill install,
  no DMM table fill, no firmware implementation, no generated-code edit, no
  CubeMX/MCSDK edit, no flash, no 24V, no power-board connection, no motor
  connection, no Gate PWM, no Motor Profiler, no Hall closed-loop, and no
  sensorless / SMO claim.
- Review lifecycle:
  this addendum does not mark the earlier `done + Review Required` software
  Hall task as `reviewed`; user review still clears strict warnings.

## Current 2026-06-08 Project Skill Install Drift Checker Addendum

- Task:
  `TASK-2026-06-08-project-skill-install-drift-checker`.
- Evidence:
  `EV-2026-06-08-PROJECT-SKILL-INSTALL-DRIFT-CHECK-001`.
- Decision:
  `Project Skill install drift checker / repo-local versus installed Skill comparison / no hardware or firmware action`.
- Scope:
  added `tools/check_project_skill_install.py`, wired it into context packs,
  contract checks, retrieval eval, docs, and tests, and reinstalled the
  validated repo-local project Skill after the checker detected expected drift
  from the new workflow-maintenance reference update.
- Verification:
  `python tools/check_project_skill_install.py --repo-only --json`,
  `python tools/check_project_skill_install.py`,
  `python tools/build_context_pack.py --mode workflow_maintenance --max-chars 350`,
  `python tools/check_ai_contracts.py`,
  `python tools/build_vector_store.py`,
  `python tools/search_local_v2.py --eval`,
  `python -m unittest discover -s tests`,
  `python -m compileall src tests`, and `git diff --check`.
- Boundary:
  repo-local project Skill reinstall only, no external GitHub Skill install,
  no DMM table fill, no firmware implementation, no generated-code edit, no
  CubeMX/MCSDK edit, no flash, no 24V, no power-board connection, no motor
  connection, no Gate PWM, no Motor Profiler, no Hall closed-loop, and no
  sensorless / SMO claim.
- Review lifecycle:
  this addendum does not mark the earlier `done + Review Required` software
  Hall task as `reviewed`; user review still clears strict warnings.

## Current 2026-06-08 Project Skill v2 Optimization Addendum

- Task:
  `TASK-2026-06-08-project-skill-v2-optimization`.
- Evidence:
  `EV-2026-06-08-PROJECT-SKILL-V2-OPT-001`.
- Decision:
  `Project Skill v2 router / no-power references / contract-checked workflow maintenance / no hardware or firmware action`.
- Scope:
  refactored `codex_skills/stm32g474-foc-assistant/SKILL.md` into a concise
  router, added `references/project-navigation.md`,
  `references/no-power-boundary.md`, `references/learning-feedback.md`, and
  `references/workflow-maintenance.md`, then wired the Skill source into
  context packs, contract checks, retrieval eval, docs, and tests.
- Verification:
  `python -X utf8 C:\Users\gregrg\.codex\skills\.system\skill-creator\scripts\quick_validate.py codex_skills\stm32g474-foc-assistant`,
  `python tools/build_context_pack.py --mode workflow_maintenance --max-chars 350`,
  `python tools/check_ai_contracts.py`,
  `python tools/build_vector_store.py`,
  `python tools/search_local_v2.py --eval`,
  `python -m unittest discover -s tests`,
  `python -m compileall src tests`, and `git diff --check`.
- Boundary:
  repo-local project Skill install only, no external GitHub Skill install, no
  DMM table fill, no firmware implementation, no generated-code edit, no
  CubeMX/MCSDK edit, no flash, no 24V, no power-board connection, no motor
  connection, no Gate PWM, no Motor Profiler, no Hall closed-loop, and no
  sensorless / SMO claim.
- Review lifecycle:
  this addendum does not mark the earlier `done + Review Required` software
  Hall task as `reviewed`; user review still clears strict warnings.

## Current 2026-06-08 Project Workflow / AI Architecture Maintenance Addendum

- Task:
  `TASK-2026-06-08-project-workflow-ai-architecture-optimization`.
- Evidence:
  `EV-2026-06-08-PROJECT-WORKFLOW-AI-ARCHITECTURE-OPT-001`.
- Decision:
  `Project workflow and AI architecture maintenance / workflow_maintenance context / project workflow contract checks / no hardware or firmware action`.
- Scope:
  added `workflow_maintenance` context, project workflow contract checks,
  workflow retrieval regression cases, and updated AI/workflow entry indexes.
- Verification:
  `python tools/build_context_pack.py --mode workflow_maintenance --max-chars 350`,
  `python tools/check_ai_contracts.py`,
  `python tools/build_vector_store.py`,
  `python tools/search_local_v2.py --eval`,
  `python -m unittest discover -s tests`,
  `python -m compileall src tests`, and `git diff --check`.
- Boundary:
  no DMM table fill, no firmware implementation, no generated-code edit, no
  CubeMX/MCSDK edit, no flash, no 24V, no power-board connection, no motor
  connection, no Gate PWM, no Motor Profiler, no Hall closed-loop, and no
  sensorless / SMO claim.
- Review lifecycle:
  this addendum does not mark the earlier `done + Review Required` software
  Hall task as `reviewed`; user review still clears strict warnings.

## Current Waiting-Hardware Addendum

- New handoff:
  `TASK-2026-05-31-p2-pcb2-waiting-hardware-handoff`.
- Evidence:
  `EV-2026-05-31-P2-PCB2-WAITING-HARDWARE-HANDOFF-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/pcb2_waiting_hardware_handoff_2026-05-31.md`.
- Decision:
  `PCB2 waiting for population / DMM gate deferred / no powered action / no firmware implementation`.
- Boundary: PCB2 has not yet been accepted as populated for measurement. Do
  not fill the DMM table until populated hardware exists; ask for the hardware
  teammate status and any updated source packet. The no-power Hall
  mixed-sequence check is now completed and parked at L4.

## Current 2026-06-01 Learning Evidence Addendum

- PR #5, `learning notes`, was reviewed and merged into `master` with merge
  commit `2b614b4aae4eb40a5b2a882c5f2252dadbe06079`.
- PR scope accepted: L2 MCSDK Hall speed / position feedback concept evidence
  only; no MCSDK Hall closed-loop, Motor Profiler, power-board, motor, PWM,
  serial, build, or powered validation claim.
- WP-030 mixed-sequence trace is now passed at L4 and recorded in
  `learning/review_items/2026-06-01_software_hall_mixed_sequence_review.md`.
- Hardware note: the user reported that the hardware teammate is close to
  finishing soldering on 2026-06-01. This does not open DMM until populated-board
  evidence exists.

## Current 2026-06-01 PCB2 Populated Addendum

- User reported: PCB2 soldered / in hand, and current route still
  `PA0/PA1/PB4 + PB3=LIN1 + P14/P15=3V3/GND`.
- Evidence:
  `EV-2026-06-01-P2-PCB2-POPULATED-ROUTE-UNCHANGED-DMM-PENDING-001`.
- Artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/pcb2_populated_route_unchanged_dmm_pending_2026-06-01.md`.
- Decision:
  `PCB2 populated / current route unchanged / DMM continuity and short-check opened as no-power pending / no powered action`.
- Boundary: DMM may now be filled only with the board unpowered. This is not a
  DMM pass and does not authorize firmware implementation, flash, 24V, motor,
  Gate PWM, Motor Profiler, or Hall closed-loop claims.

## Current Workflow Guard Addendum

- User-reported issue: Codex kept drifting into concept teaching even though the
  dual-teacher workflow says ChatGPT should teach pure theory.
- Hotfix task:
  `TASK-2026-05-28-workflow-dual-teacher-concept-guard`.
- Evidence:
  `EV-2026-05-28-WORKFLOW-DUAL-TEACHER-CONCEPT-GUARD-001`.
- Decision:
  `Dual-teacher concept-only role guard / ChatGPT teaches theory / Codex reviews records and executes repo work`.
- Boundary: workflow-control only; no firmware, no Workbench regeneration, no
  flash, no 24V, no power-board connection, no motor connection, no Gate PWM,
  no Motor Profiler, no Hall closed-loop, and no powered readiness.

## Task ID

- ID: `TASK-2026-05-28-p2-software-hall-firmware-entry-plan`
- Topic: software Hall firmware-entry plan for future debug-only
  `PA0/PA1/PB4` adapter
- Status: `done`
- Risk Level: `L1 no-power design boundary / no firmware / no hardware`
- Definition of Done: `workflow/definition_of_done.md`
- Evidence ID:
  `EV-2026-05-28-P2-SOFTWARE-HALL-FIRMWARE-ENTRY-PLAN-001`
- Related build-only task:
  `TASK-2026-05-27-p2-qiansai-g474-stdrive101-foc-p2-debug-build-only`
- Related MCSDK interface task:
  `TASK-2026-05-27-p2-software-hall-mcsdk-speed-position-feedback-interface-review`
- Related hardware gate:
  `TASK-2026-05-22-p2-dmm-continuity-short-check-request`
- Review Required: yes

## Background

PCB2 is still unpopulated. DMM continuity / short-check evidence is deferred,
not passed. Deferred does not mean passed.

The external Workbench project must remain stable at:

`C:\Users\gregrg\.st_workbench\projects\QIANSAI_G474_STDRIVE101_FOC_P2`

The no-power Debug build-only task already recorded local compile evidence.
That build-only pass does not prove current PCB2 physical routing, GPIO/EXTI
runtime behavior, MCSDK Hall integration, Gate PWM safety, Hall closed-loop
behavior, motor readiness, power-stage readiness, or sensorless validation.

## Feature Sentence

The project now has a Chinese-first no-power firmware-entry plan:

```text
accepted current route PA0/PA1/PB4
-> future GPIO/EXTI debug-only capture
-> ISR stores raw_state + timestamp + event count only
-> low-priority state machine rejects 000/111, repeats, bounce candidates, and abnormal jumps
-> low-frequency debug snapshot exposes direction_candidate and speed_candidate
-> no MCSDK hook, no firmware implementation, no Hall readiness
```

## Evidence Decision

- Decision:
  `Software Hall firmware-entry plan / debug-only no-power boundary / no firmware implementation / no MCSDK hook / no Hall readiness`.
- Evidence level: L1 no-power design-boundary evidence.
- New artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_firmware_entry_plan_2026-05-28.md`.
- Current route:
  `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`.
- Fixed constraint: `PB3=LIN1`; it is not current Hall.
- Generated-route reminder: MCSDK standard TIM2 Hall `PA15/PB3/PB10` is
  generated-source evidence only, not current PCB2 Hall proof.
- This artifact is not usable to claim firmware implementation, MCSDK Hall
  integration, MCSDK hook readiness, DMM continuity, Gate PWM safety, Hall
  closed-loop, motor readiness, power-stage readiness, or sensorless
  validation.

## Input Files

- `workflow/CURRENT_SNAPSHOT.md`
- `CURRENT_STATUS.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_firmware_entry_checklist_2026-05-27.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_gpio_exti_boundary_review_2026-05-27.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_timestamp_source_review_2026-05-27.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_debug_output_route_review_2026-05-27.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_mcsdk_speed_position_feedback_interface_review_2026-05-27.md`

## Output Files

- `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_firmware_entry_plan_2026-05-28.md`
- `CURRENT_STATUS.md`
- `AI_CONTEXT.md`
- `workflow/ACTIVE_TASK.md`
- `workflow/CURRENT_SNAPSHOT.md`
- `workflow/evidence_register.md`
- `workflow/current_learning_sprint.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/p2_readiness_snapshot_2026-05-15.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/evidence_packet_2026-05-14.md`
- `apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md`
- `deliverables/submission_checklist.md`
- `tests/test_workflow_contracts.py`

## Carry-Forward Build-Only Contract

The earlier build-only evidence remains active context, but it is not the
current task.

- `TASK-2026-05-27-p2-qiansai-g474-stdrive101-foc-p2-debug-build-only` /
  `EV-2026-05-27-P2-QIANSAI-G474-STDRIVE101-FOC-P2-BUILD-ONLY-001`:
  `No-power build-only Debug pass / local toolchain compiles generated project / no firmware runtime or hardware readiness`.
- Build command:
  `cmake --build "C:\Users\gregrg\.st_workbench\projects\QIANSAI_G474_STDRIVE101_FOC_P2\build\Debug" --config Debug`.
- Result: exit code `0`; Ninja output `ninja: no work to do`.
- Confirmed artifacts:
  `QIANSAI_G474_STDRIVE101_FOC_P2.elf` and
  `QIANSAI_G474_STDRIVE101_FOC_P2.map`.
- The record is `not a clean rebuild record`; it is local no-power compile
  evidence only.

## Carry-Forward Software Hall Contracts

These prior no-power software Hall records remain active context for safety and
review. They are not usable to claim firmware implementation, MCSDK Hall
integration, Hall closed-loop behavior, Gate PWM safety, motor readiness,
power-stage readiness, or sensorless validation.

Stable carry-forward phrases:

- not usable to claim firmware implementation
- Not usable to claim firmware implementation
- not firmware or hardware readiness

- `TASK-2026-05-22-p2-software-hall-no-power-algorithm-prep` /
  `EV-2026-05-22-P2-SOFTWARE-HALL-ALGORITHM-PREP-001`:
  `Algorithm-side no-power preparation only`; `Deferred does not mean passed`.
- `TASK-2026-05-22-p2-software-hall-state-machine-exercise` /
  `EV-2026-05-22-P2-SOFTWARE-HALL-STATE-MACHINE-EXERCISE-001`:
  `Software Hall state-machine exercise`; `Waiting for user answer`; learning
  check only.
- `TASK-2026-05-27-p2-software-hall-adapter-pseudocode-draft` /
  `EV-2026-05-27-P2-SOFTWARE-HALL-PSEUDOCODE-DRAFT-001`:
  `Pseudocode draft added / no firmware implementation / no MCSDK Hall integration / no Hall readiness`;
  DMM remains deferred, not passed.
- `TASK-2026-05-27-p2-software-hall-followup-review` /
  `EV-2026-05-27-P2-SOFTWARE-HALL-FOLLOWUP-REVIEW-001`:
  `L4 table-level no-power Hall state-machine classification / no firmware implementation / no hardware validation`.
- `TASK-2026-05-27-p2-software-hall-processing-order-card` /
  `EV-2026-05-27-P2-SOFTWARE-HALL-PROCESSING-ORDER-CARD-001`:
  `Software Hall Adapter Processing-Order Card`; L1 repair artifact, not a new
  mastery upgrade.
- `TASK-2026-05-27-p2-software-hall-host-model` /
  `EV-2026-05-27-P2-SOFTWARE-HALL-HOST-MODEL-001`:
  `Host-side software Hall reference model / no firmware implementation / no MCSDK Hall integration / no Hall readiness`.
- `TASK-2026-05-27-p2-software-hall-golden-vectors` /
  `EV-2026-05-27-P2-SOFTWARE-HALL-GOLDEN-VECTORS-001`:
  `Host-side software Hall golden vectors / no firmware implementation / no MCSDK Hall integration / no Hall readiness`.
- `TASK-2026-05-27-p2-software-hall-mcsdk-integration-probe` /
  `EV-2026-05-27-P2-SOFTWARE-HALL-MCSDK-INTEGRATION-PROBE-001`:
  `MCSDK Hall integration points identified as read-only clues / no firmware implementation / no MCSDK Hall integration / no Hall readiness`.
- `TASK-2026-05-27-p2-software-hall-firmware-entry-checklist` /
  `EV-2026-05-27-P2-SOFTWARE-HALL-FIRMWARE-ENTRY-CHECKLIST-001`:
  `Software Hall firmware-entry checklist / no firmware implementation / no MCSDK Hall integration / no Hall readiness`.
- `TASK-2026-05-27-p2-software-hall-gpio-exti-boundary` /
  `EV-2026-05-27-P2-SOFTWARE-HALL-GPIO-EXTI-BOUNDARY-001`:
  `Software Hall GPIO/EXTI boundary review draft / no firmware implementation / no GPIO runtime proof / no Hall readiness`.
- `TASK-2026-05-27-p2-software-hall-timestamp-source-review` /
  `EV-2026-05-27-P2-SOFTWARE-HALL-TIMESTAMP-SOURCE-001`:
  `Software Hall timestamp-source review draft / no firmware implementation / no timer configuration / no Hall readiness`.
- `TASK-2026-05-27-p2-software-hall-debug-output-route-review` /
  `EV-2026-05-27-P2-SOFTWARE-HALL-DEBUG-OUTPUT-ROUTE-001`:
  `Software Hall low-frequency debug-output route review draft / no firmware implementation / no UART implementation / no Hall readiness`.
- `TASK-2026-05-27-p2-software-hall-mcsdk-firmware-integration-boundary` /
  `EV-2026-05-27-P2-SOFTWARE-HALL-MCSDK-FIRMWARE-INTEGRATION-BOUNDARY-001`:
  `Software Hall MCSDK firmware-integration boundary review draft / no firmware implementation / no MCSDK hook / no Hall readiness`.
- `TASK-2026-05-27-p2-software-hall-mcsdk-hook-evidence-request-checklist` /
  `EV-2026-05-27-P2-SOFTWARE-HALL-MCSDK-HOOK-EVIDENCE-REQUEST-001`:
  `Software Hall MCSDK hook evidence request checklist / no firmware implementation / no MCSDK hook / no Hall readiness`.
- `TASK-2026-05-27-p2-software-hall-mcsdk-speed-position-feedback-interface-review` /
  `EV-2026-05-27-P2-SOFTWARE-HALL-MCSDK-SPEED-POSITION-INTERFACE-001`:
  `Software Hall MCSDK speed/position feedback interface review / no firmware implementation / no MCSDK hook / no Hall readiness`.

## Next User Checkpoint

The current repo-side checkpoint is complete through the waveform candidate
residual-voltage isolation result:

`apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_candidate_residual_voltage_isolation_result_2026-06-21.md`

The immediate user checkpoint is no longer another residual-voltage repeat.
The residual-voltage blocker is cleared only. The next engineering checkpoint
may only be a separate candidate 24 V static no-motor phase-gate or execution
entry.

Candidate next-stage preconditions to confirm before that separate record:

- current board image remains the waveform candidate image;
- HSPY / 24 V is OFF before setup and starts from a current-limited state;
- no `10 kohm` wake resistor or LIN1 stimulus;
- motor disconnected;
- oscilloscope or DMM measurement points are named before applying 24 V;
- stop rules and rollback are stated before applying 24 V.

That next checkpoint is still static no-motor only. It is not motor power-up
and does not open Run / Debug, Motor Pilot, Motor Profiler, Gate PWM output,
motor connection, power-stage readiness, or motor readiness.

Do not repeat the residual-voltage isolation check unless the physical state,
image, wiring, or measured value changes.

## Verification

Latest repo-side verification run for the waveform candidate residual-voltage
isolation result registration after this update:

- `python -m unittest tests.test_workflow_contracts.Stdrive101ManualGateTestLinkedImageBoundaryTests`
  passed: 41 tests OK.
- `python -m unittest discover -s tests`
  passed: 194 tests OK.
- `python tools\check_ai_contracts.py` passed with no AI contract errors; known
  warning remains: `ACTIVE_TASK.md is done and still requires review.`
- `git diff --check` passed with no whitespace errors; output contained only
  CRLF conversion warnings for touched Markdown files.

## Safety Boundary

This task does not authorize firmware logic edits, generated-code edits,
CubeMX/Workbench edits, flash, Run / Debug, 24V, power-board connection, motor
connection, Gate PWM output, Motor Profiler, Motor Pilot, Hall closed-loop, or
sensorless / SMO claims.
