## 2026-06-22 Host-Side No-Power FOC Golden Vectors Added

- Added host-side no-power FOC golden vectors:
  `tests/fixtures/foc_core_golden_vectors.json`.
- Added replay tests:
  `tests/test_foc_core_vectors.py`.
- Added the review artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/host_side_no_power_foc_golden_vectors_review_2026-06-22.md`.
- Evidence:
  `EV-2026-06-22-P2-HOST-SIDE-NO-POWER-FOC-GOLDEN-VECTORS-001`.
- Task:
  `TASK-2026-06-22-p2-host-side-no-power-foc-golden-vectors`.
- Decision:
  `Host-side no-power FOC golden vectors / no firmware implementation / no MCSDK integration / no PWM output / no motor readiness`.
- Scope:
  the vectors replay Clarke, Park, inverse Park, host-side SVPWM-style duty
  math, PI anti-windup / clamping, and current-loop state behavior against the
  current Python reference model.
- MCSDK boundary:
  these vectors freeze only the current host-side Python convention. They are
  not proof that MCSDK generated code uses the same sign convention, scaling
  convention, duty representation, timing, or saturation behavior.
- Boundary:
  this is host-side no-power regression fixture evidence only. It does not
  configure TIM1, write compare registers, provide compare-register evidence,
  drive gates, validate PWM safety, integrate with MCSDK, validate Hall
  closed-loop, validate sensorless / SMO, prove power-stage readiness, or
  prove motor readiness. It is not compare-register evidence, not Gate PWM
  validation, not power-stage readiness, and not motor readiness.
- Verification:
  `python -m unittest tests.test_foc_core_vectors` passed: 6 tests OK;
  `python -m unittest tests.test_workflow_contracts.FocCoreHostModelWorkflowTests`
  passed: 4 tests OK; `python -m unittest tests.test_foc_core_model` passed:
  14 tests OK; `python -m unittest discover -s tests` passed: 218 tests OK;
  `python -m compileall src tests` passed;
  `python tools\check_ai_contracts.py` reported no AI contract errors and the
  existing `ACTIVE_TASK.md is done and still requires review` warning;
  `git diff --check` passed with only CRLF conversion warnings.

## 2026-06-22 Host-Side No-Power FOC Algorithm Model Added

- Added a host-side no-power FOC algorithm model:
  `src/foc_core_model.py`.
- Added unit tests:
  `tests/test_foc_core_model.py`.
- Added the review artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/host_side_no_power_foc_algorithm_model_review_2026-06-22.md`.
- Evidence:
  `EV-2026-06-22-P2-HOST-SIDE-NO-POWER-FOC-ALGORITHM-MODEL-001`.
- Task:
  `TASK-2026-06-22-p2-host-side-no-power-foc-algorithm-model`.
- Decision:
  `Host-side no-power FOC algorithm model / no firmware implementation / no MCSDK integration / no PWM output / no motor readiness`.
- Scope:
  the model covers Clarke, inverse Clarke, Park, inverse Park, host-side
  zero-sequence SVPWM-style duty calculation, PI current control with
  anti-windup, and one host-side current-loop step. It is a Python learning
  and regression artifact only.
- MCSDK boundary:
  ST MCSDK remains the intended motor-control framework generation path. This
  model does not replace Workbench/CubeMX generation, does not hook into MCSDK,
  and does not edit generated firmware.
- Boundary:
  this is host-side no-power algorithm evidence only. It is not firmware
  implementation, not MCSDK integration, not a timer driver, not GPIO/ADC/TIM1
  runtime behavior, not Gate PWM output validation, not Hall closed-loop,
  not sensorless / SMO validation, not power-stage readiness, and not motor
  readiness.
- Verification:
  `python -m unittest tests.test_foc_core_model` passed: 14 tests OK;
  `python -m unittest tests.test_workflow_contracts.FocCoreHostModelWorkflowTests`
  passed: 2 tests OK; `python -m unittest discover -s tests` passed:
  210 tests OK; `python -m compileall src tests` passed;
  `python tools\check_ai_contracts.py` reported no AI contract errors and the
  existing `ACTIVE_TASK.md is done and still requires review` warning;
  `git diff --check` passed with only CRLF conversion warnings.

## 2026-06-21 STDRIVE101 PA7 LIN1 Wake nFAULT 1.3V Fault Isolation Result Recorded

- Added the PA7 / LIN1 wake fault-isolation result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_pa7_lin1_wake_nfault_1v3_fault_isolation_result_2026-06-21.md`.
- Evidence:
  `EV-2026-06-21-STDRIVE101-PA7-LIN1-WAKE-NFAULT-1V3-FAULT-ISOLATION-001`.
- Task:
  `TASK-2026-06-21-stdrive101-pa7-lin1-wake-nfault-1v3-fault-isolation`.
- User-reported isolation results:
  `PA7 / CN10-15 = 3.3 V`, `CN8 P2 / LIN1 = 3.3 V`,
  `VS / 24V_FUSED = 24 V`, `REG12 = 12 V`, and `nFAULT = 1.3 V`.
  Both `CN8 P13 / nFAULT` and `NUCLEO CN10-16 / PB12` measured `1.3 V`;
  after disconnecting the `nFAULT -> PB12` wire, power-board `CN8 P13`
  still measured `1.3 V`.
- Corrected no-power checks:
  `R3 body = 10 kohm`,
  `R3 3V3 side -> CN8 P14 / 3V3 = 0 ohm`, and
  `R3 nFAULT side -> CN8 P13 / nFAULT = 0 ohm`. SCREF-related checks
  recorded `SCREF -> GND = 33 kohm`, `SCREF -> 3V3 = 33 kohm`,
  `R1 / R2 body = 33 kohm / 20 kohm`, and both checked R2 endpoint
  continuities as `0 ohm`.
- Decision:
  `STDRIVE101 PA7 LIN1 wake nFAULT 1.3V fault isolation result / PA7
  hold-high image copied by ST-LINK mass storage / PA7 CN10-15 = 3.3 V /
  CN8 P2 LIN1 = 3.3 V / VS 24V_FUSED = 24 V / REG12 = 12 V / nFAULT =
  1.3 V on both CN8 P13 and NUCLEO CN10-16 / nFAULT remains 1.3 V after
  PB12 wire disconnected / R3 pull-up body and endpoint continuity corrected
  as 10 kohm and 0 ohm / R3 pull-up value and NUCLEO PB12 not primary
  blocker / STDRIVE101 wakes but reports or holds a power-board-side fault
  state / current primary hypothesis is low-side phase-U VDS or related
  driver-output path after LIN1 stimulus / no repeated motor run / no Motor
  Pilot / no Motor Profiler / no Hall closed-loop validation / no sensorless
  claim / no power-stage readiness / no motor-readiness claim`.
- Boundary:
  this is fault-isolation evidence only. It does not validate PWM output,
  phase-output behavior, power-stage readiness, motor readiness, Hall closed
  loop, sensorless operation, or safe drive operation.
- Next checkpoint:
  do not repeat the motor-connected open-loop run. The next teacher-reviewed
  diagnostic should distinguish a `LIN1 / GLS1 / Q2 / OUT1` low-side path
  issue from a common STDRIVE101 protection / CP / SCREF / soldering / chip
  issue. A bounded motor-disconnected comparison using
  `3.3 V -> 10 kohm -> CN8 P1 / HIN1` may be considered only after review.

## 2026-06-21 STDRIVE101 Gate-Waveform Candidate 24V Static Scope No-Waveform Result Recorded

- Added the waveform candidate 24V static scope no-waveform result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_candidate_24v_static_scope_no_waveform_result_2026-06-21.md`.
- Evidence:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-CANDIDATE-24V-STATIC-SCOPE-NO-WAVEFORM-RESULT-001`.
- Task:
  `TASK-2026-06-21-stdrive101-gate-waveform-candidate-24v-static-scope-no-waveform-result`.
- User-reported result:
  `CN3_1 / CN3_2`, `CN3_3 / CN3_4`, and `CN3_5 / CN3_6` all showed no
  waveform; HSPY stayed `CV` at `0.036 A`; `nFAULT = 3.3 V`; no abnormal
  board symptom was reported.
- Decision:
  `STDRIVE101 gate-waveform candidate 24V static scope no-waveform result /
  waveform candidate image / HSPY CV 0.036 A / CN3_1 and CN3_2 no waveform /
  CN3_3 and CN3_4 no waveform / CN3_5 and CN3_6 no waveform / nFAULT remains
  3.3 V / no board heat smell sound reset-loop symptom / no observed
  MCU-facing driver-input waveform in this no-motor bounded check / no Run
  Debug / no Motor Pilot / no Motor Profiler / no motor connection / no
  powered-drive readiness`.
- Boundary:
  this records only the bounded no-motor oscilloscope observation for the
  waveform candidate image. It does not authorize Motor Pilot, Motor Profiler,
  motor connection, Hall closed loop, sensorless operation, power-stage
  readiness, or motor readiness.
- Next checkpoint:
  do not repeat the same candidate 24 V static scope check unless the image,
  wiring, board condition, trigger method, measurement setup, or observed value
  changes. The next engineering step should be source/build/runtime-entry
  review for why the candidate waveform was not observed, or a deliberate
  return to a lower-risk neutral-wrapper / lockout path.

## 2026-06-21 STDRIVE101 Gate-Waveform Candidate Residual-Voltage Isolation Result Recorded

- Added the waveform candidate residual-voltage isolation result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_candidate_residual_voltage_isolation_result_2026-06-21.md`.
- Evidence:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-CANDIDATE-RESIDUAL-VOLTAGE-ISOLATION-RESULT-001`.
- Task:
  `TASK-2026-06-21-stdrive101-gate-waveform-candidate-residual-voltage-isolation-result`.
- Prior blocker:
  the waveform candidate USB-only DMM result reported
  `VS / 24V_FUSED = 2 V` and `REG12 = 0.3 V` after the candidate image copy.
- User-confirmed isolation setup:
  USB / ST-LINK disconnected; HSPY / 24 V OFF and physically disconnected;
  motor disconnected; no `10 kohm` wake resistor or LIN1 stimulus installed;
  DMM black probe on GND.
- User-confirmed readings:
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
  this clears only the immediate candidate residual-voltage blocker. It does
  not validate 24 V behavior, Gate PWM output, Motor Pilot, Motor Profiler,
  motor behavior, power-stage readiness, or motor readiness.
- Next checkpoint:
  do not repeat the residual-voltage isolation check unless the physical state,
  image, wiring, or measured value changes. The next engineering checkpoint
  may only be a separate candidate 24 V static no-motor phase-gate or
  execution entry, still with the motor disconnected and with no Run / Debug,
  no Gate PWM output, no Motor Pilot, no Motor Profiler, and no motor-readiness
  claim.

## 2026-06-21 STDRIVE101 Gate-Waveform Candidate USB-Only DMM Result Recorded

- Added the waveform candidate USB-only DMM result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_candidate_usb_only_dmm_result_2026-06-21.md`.
- Evidence:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-CANDIDATE-USBONLY-DMM-RESULT-001`.
- Task:
  `TASK-2026-06-21-stdrive101-gate-waveform-candidate-usbonly-dmm-result`.
- User-reported DMM readings after the candidate USB-only download:
  `CN3_1` through `CN3_6 = 0 V`, `CN3_13 = 3 V`,
  `CN3_14 = 3 V`, `VS / 24V_FUSED = 2 V`, and `REG12 = 0.3 V`.
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
  the six MCU-facing driver inputs stayed low in the reported USB-only DMM
  table, so the six-input stop-rule was not hit. However,
  `VS / 24V_FUSED = 2 V` keeps the residual-voltage boundary active and
  blocks upward hardware progression. This is not a pass for 24 V, Gate PWM,
  or motor work.
- Next checkpoint:
  superseded by the later waveform candidate residual-voltage isolation result,
  which records `VS / 24V_FUSED = 0 V` and `REG12 = 0 V` after USB / ST-LINK
  disconnect. Do not repeat the full CN3 table or the residual-voltage
  isolation check unless the physical state, image, wiring, or measured value
  changes.

## 2026-06-21 STDRIVE101 Gate-Waveform Candidate USB-Only Download Result Recorded

- Added the waveform candidate USB-only download result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_candidate_usb_only_download_result_2026-06-21.md`.
- Added the waveform candidate USB-only download execution entry:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_candidate_usb_only_download_execution_entry_2026-06-21.md`.
- Evidence:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-CANDIDATE-USBONLY-DOWNLOAD-RESULT-001`
  and
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-CANDIDATE-USBONLY-DOWNLOAD-EXECUTION-ENTRY-001`.
- Task:
  `TASK-2026-06-21-stdrive101-gate-waveform-candidate-usbonly-download-result`
  and
  `TASK-2026-06-21-stdrive101-gate-waveform-candidate-usbonly-download-execution-entry`.
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
  the board image is now treated as the waveform candidate image for the next
  bounded checks. This record is a USB-only download result only. Because the
  candidate image calls `gate_waveform_candidate_run_once()` once after reset
  and then holds idle low, this record does not prove absence of a boot-time
  output transition. It also does not prove CN3 state, waveform correctness,
  24 V behavior, power-stage readiness, or motor readiness.
- Next checkpoint:
  superseded by the later waveform candidate residual-voltage isolation result,
  which clears the immediate residual-voltage blocker only and changes the
  live checkpoint to a separate candidate 24 V static no-motor phase-gate or
  execution entry. Do not connect a motor or use Run / Debug, Motor Pilot, or
  Motor Profiler from this download result.

## 2026-06-21 STDRIVE101 Gate-Waveform Candidate BIN Artifact Record No-Power

- Added the waveform candidate BIN artifact record:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_candidate_bin_artifact_record_no_power_2026-06-21.md`.
- Evidence:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-CANDIDATE-BIN-ARTIFACT-RECORD-NO-POWER-001`.
- Task:
  `TASK-2026-06-21-stdrive101-gate-waveform-candidate-bin-artifact-record-no-power`.
- Candidate image:
  `.tmp/manual_gate_waveform_build_only_2026-06-21_clean/stdrive101_gate_waveform_candidate_image.elf`
  with ELF SHA256
  `10BA818730E259AEBA8A5C5E5C96CFBA32FCB90AAA4136B775022B9D69ADCE7C` and
  MAP SHA256
  `170EA77C566F98CF9EF2AC88F76B154238A5404DC705AAE3917BEAE7C1503D4C`.
- Generated BIN:
  `.tmp/manual_gate_waveform_build_only_2026-06-21_clean/stdrive101_gate_waveform_candidate_image.bin`,
  size `1852` bytes, SHA256
  `362C510E4F682751F0721B54F306F6E144951F03F9FF875E68E238D92A29BB31`.
- Conversion evidence:
  the local fallback ELF32 `PT_LOAD` converter was checked against the
  already-recorded neutral-wrapper objcopy BIN; both hashes matched
  `CA2A42F2F83C42EA9E7BEC628BD8656A422DBE767CFFD5A5865BE781603D3D71`.
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
  this is downloadable BIN artifact evidence only. It does not change the
  image currently on the board, does not copy to ST-LINK mass storage, does
  not execute Gate PWM output, and does not authorize Motor Pilot, Motor
  Profiler, motor connection, power-stage readiness, or motor readiness.
- Next checkpoint:
  only a separate waveform-candidate USB-only download execution entry after
  explicit user confirmation and authorization. Keep HSPY / 24 V OFF and the
  motor disconnected until then.

## 2026-06-21 STDRIVE101 Gate-Waveform Neutral-Wrapper 24V Static Scope Baseline Result Recorded

- Added the neutral-wrapper 24V static scope baseline result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_neutral_wrapper_24v_static_scope_baseline_result_2026-06-21.md`.
- Evidence:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-24V-STATIC-SCOPE-BASELINE-RESULT-001`.
- Task:
  `TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-24v-static-scope-baseline-result`.
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
  this is static oscilloscope baseline evidence only. It does not authorize or
  validate Gate PWM output, waveform correctness, Motor Pilot, Motor Profiler,
  motor connection, Hall closed loop, sensorless operation, power-stage
  readiness, or motor readiness.
- Next checkpoint:
  turn HSPY output OFF after this baseline. The next engineering checkpoint
  may only be a separate no-motor, short-window, instrumented waveform
  execution entry with exact probe points, stop rules, and rollback.

## 2026-06-21 STDRIVE101 Gate-Waveform Neutral-Wrapper 24V Static No-Motor Result Recorded

- Added the neutral-wrapper 24V static no-motor result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_neutral_wrapper_24v_static_no_motor_result_2026-06-21.md`.
- Evidence:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-24V-STATIC-NO-MOTOR-RESULT-001`.
- Task:
  `TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-24v-static-no-motor-result`.
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
  this is bounded 24 V static no-motor measurement evidence only. It does not
  authorize Gate PWM output, Motor Pilot, Motor Profiler, motor connection,
  Hall closed loop, sensorless operation, power-stage readiness, or motor
  readiness.
- Next checkpoint:
  turn HSPY output OFF after this static measurement. The next engineering
  checkpoint may only be a separate no-motor instrumented gate-waveform gate,
  not motor power-up.

## 2026-06-21 STDRIVE101 Gate-Waveform Neutral-Wrapper Residual-Voltage Isolation Result Recorded

- Added the neutral-wrapper residual-voltage isolation result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_neutral_wrapper_residual_voltage_isolation_result_2026-06-21.md`.
- Evidence:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-RESIDUAL-VOLTAGE-ISOLATION-RESULT-001`.
- Task:
  `TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-residual-voltage-isolation-result`.
- Prior blocker:
  the neutral-wrapper USB-only DMM completion result reported
  `VS / 24V_FUSED = 2 V`, `REG12 = 0.5 V`, and no board heat / smell /
  sound / reset-loop symptom.
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
  this clears only the immediate residual-voltage blocker raised by the earlier
  USB-only `VS / 24V_FUSED = 2 V` reading. It does not authorize 24 V, Run /
  Debug, Gate PWM output, Motor Pilot, Motor Profiler, motor connection, Hall
  closed loop, sensorless operation, power-stage readiness, or motor readiness.
- Next checkpoint:
  do not repeat the residual-voltage isolation check unless the physical state,
  image, wiring, or measured value changes. The next engineering checkpoint is
  a separate dated next-stage phase-gate decision, not direct motor power-up.

## 2026-06-21 STDRIVE101 Gate-Waveform Neutral-Wrapper USB-Only DMM Completion Result Recorded

- Added the neutral-wrapper USB-only DMM completion result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_neutral_wrapper_usb_only_dmm_completion_result_2026-06-21.md`.
- Evidence:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-USBONLY-DMM-COMPLETION-RESULT-001`.
- Task:
  `TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-usbonly-dmm-completion-result`.
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
  this is completed USB-only DMM measurement evidence only. It does not
  authorize 24 V, Run / Debug, Gate PWM output, Motor Pilot, Motor Profiler,
  motor connection, Hall closed loop, sensorless operation, power-stage
  readiness, or motor readiness. The table is not treated as a clean pass
  because `VS / 24V_FUSED = 2 V` is above the prior `< 1 V` boundary.
- Next checkpoint:
  superseded for the live checkpoint by the later residual-voltage isolation
  result, which records `VS / 24V_FUSED = 0 V` and `REG12 = 0 V` after
  USB / ST-LINK disconnect.


## 2026-06-21 STDRIVE101 Gate-Waveform Neutral-Wrapper USB-Only DMM Partial Result Recorded

- Added the neutral-wrapper USB-only DMM partial result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_neutral_wrapper_usb_only_dmm_partial_result_2026-06-21.md`.
- Evidence:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-USBONLY-DMM-PARTIAL-RESULT-001`.
- Task:
  `TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-usbonly-dmm-partial-result`.
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
  this is partial USB-only DMM measurement evidence after the neutral-wrapper
  USB-only ST-LINK mass-storage download. It does not authorize 24 V, Run /
  Debug, Gate PWM output, Motor Pilot, Motor Profiler, motor connection, Hall
  closed loop, sensorless operation, power-stage readiness, or motor
  readiness.
- Next checkpoint:
  do not repeat the already reported `CN3_1` through `CN3_6` rows unless the
  physical state changes. With black probe on GND, USB-only still active,
  24 V still disconnected, and motor still disconnected, report only
  `VS / 24V_FUSED`, `REG12`, and board heat / smell / sound / reset-loop
  status. If any later recheck of `CN3_1` through `CN3_6` is stably above
  `0.3 V`, stop, keep 24 V disconnected, and record the raw reading.

## 2026-06-21 STDRIVE101 Gate-Waveform Neutral-Wrapper USB-Only Download Result Recorded

- Added the neutral-wrapper USB-only download result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_neutral_wrapper_usb_only_download_result_2026-06-21.md`.
- Added the neutral-wrapper USB-only download execution entry:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_neutral_wrapper_usb_only_download_execution_entry_2026-06-21.md`.
- Added the neutral-wrapper BIN artifact record:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_neutral_wrapper_bin_artifact_record_no_power_2026-06-21.md`.
- Evidence:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-USBONLY-DOWNLOAD-RESULT-001`,
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-USBONLY-DOWNLOAD-EXECUTION-ENTRY-001`, and
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-BIN-ARTIFACT-RECORD-NO-POWER-001`.
- Tasks:
  `TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-usbonly-download-result`,
  `TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-usbonly-download-execution-entry`, and
  `TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-bin-artifact-record-no-power`.
- Candidate image identity:
  `.tmp/gwnw_build_2026-06-21_clean/stdrive101_gate_waveform_neutral_wrapper_image.elf`
  SHA256 `C47C02D379DC5312095DF786BF8C99B58D42323AD9227D0903BCB8C98AAD9591`;
  MAP SHA256
  `5FB24B2735EFFD402C26BDC3B0D267B26B06DC6522A6B5B5D876491BA9A42A83`;
  generated BIN
  `.tmp/gwnw_build_2026-06-21_clean/stdrive101_gate_waveform_neutral_wrapper_image.bin`
  size `1044` bytes, SHA256
  `CA2A42F2F83C42EA9E7BEC628BD8656A422DBE767CFFD5A5865BE781603D3D71`.
- Download result:
  the user confirmed `USB-only`, `24V disconnected`, and `motor disconnected`,
  and explicitly allowed copying the neutral-wrapper BIN to `D:`. Pre-copy
  checks showed `D:` volume label `NOD_G474RE`, source BIN hash
  `CA2A42F2F83C42EA9E7BEC628BD8656A422DBE767CFFD5A5865BE781603D3D71`,
  and no `D:\FAIL.TXT`. The BIN was copied once to
  `D:\stdrive101_gate_waveform_neutral_wrapper_image.bin`. After a short
  wait, `D:` was still `NOD_G474RE`, `D:\FAIL.TXT` was absent, and the target
  BIN was no longer visible, consistent with ST-LINK mass-storage consumption.
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
  this is a USB-only ST-LINK mass-storage download result for the neutral-
  wrapper image only. It does not record the CN3 / REG12 DMM neutral-state
  result yet. It does not authorize 24 V, Run / Debug, Gate PWM output,
  Motor Pilot, Motor Profiler, motor connection, Hall closed loop, sensorless
  operation, power-stage readiness, or motor readiness.
- Next checkpoint:
  direct USB-only DMM table with 24 V still disconnected and motor still
  disconnected: `VS / 24V_FUSED`, `CN3_1` through `CN3_6`,
  `CN3_13 / nFAULT`, `CN3_14 / 3V3`, `REG12`, and board heat / smell /
  sound / reset-loop status. If any `CN3_1` through `CN3_6` is stably above
  `0.3 V`, stop, disconnect USB if needed, keep 24 V disconnected, and
  record the raw reading.

## 2026-06-21 STDRIVE101 Gate-Waveform Neutral-Wrapper USB-Only Neutral-State Phase-Gate Plan Recorded

- Added the neutral-wrapper USB-only neutral-state phase-gate plan:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_neutral_wrapper_usb_only_neutral_state_phase_gate_plan_2026-06-21.md`.
- Evidence:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-USBONLY-NEUTRAL-STATE-PHASE-GATE-PLAN-001`.
- Task:
  `TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-usbonly-neutral-state-phase-gate-plan`.
- Candidate image boundary carried forward:
  `.tmp/gwnw_build_2026-06-21_clean/stdrive101_gate_waveform_neutral_wrapper_image.elf`
  SHA256 `C47C02D379DC5312095DF786BF8C99B58D42323AD9227D0903BCB8C98AAD9591`;
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
  this is phase-gate planning only. It performs no flash, no Run / Debug, no
  USB runtime execution, no 24 V, no Gate PWM output, no oscilloscope probing
  on live gate or phase nodes, no Motor Pilot, no Motor Profiler, and no motor
  connection. It also makes no power-stage readiness or motor readiness claim.
- Important DMM limitation:
  the neutral-wrapper retained ELF no longer contains
  `gate_waveform_candidate_run_once`, so it is better suited than the earlier
  Gate E2 `run_once()` image for a future DMM-only neutral-state check. DMM
  can still show only steady firmware-controlled neutral state after firmware
  reaches the wrapper loop; it cannot prove reset-time pin state or absence of
  a very short transient on real hardware.
- Next checkpoint:
  only a separate neutral-wrapper USB-only neutral-state execution-entry record
  after explicit user request and freshly confirmed preconditions. It is not
  flash, not Run / Debug, not USB runtime execution in this record, not 24 V,
  not Gate PWM output, not Motor Pilot, not Motor Profiler, and not motor
  connection. Gate E4 remains closed.

## 2026-06-21 STDRIVE101 Gate-Waveform Neutral-Wrapper Build-Only Record No-Power Recorded

- Added the neutral-wrapper no-power build-only record:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_neutral_wrapper_build_only_record_no_power_2026-06-21.md`.
- Added the separate neutral-wrapper build-only package:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/manual_gate_waveform_neutral_wrapper_build_only_2026-06-21/`.
- Source packages carried forward:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/manual_gate_waveform_source_package_2026-06-21/`
  and
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/manual_gate_waveform_neutral_wrapper_source_package_2026-06-21/`.
- Clean build directory:
  `.tmp/gwnw_build_2026-06-21_clean/`.
- Evidence:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-BUILD-ONLY-RECORD-NO-POWER-001`.
- Task:
  `TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-build-only-record-no-power`.
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
  clean configure used `CMAKE_SYSTEM_NAME=Generic`,
  `CMAKE_SYSTEM_PROCESSOR=arm`,
  `CMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY`, STM32Cube GNU Arm GCC
  `14.3.1`, and Ninja `1.13.2`. Clean build produced
  `stdrive101_gate_waveform_neutral_wrapper_objects` and
  `stdrive101_gate_waveform_neutral_wrapper_image`. Clean ELF SHA256 is
  `C47C02D379DC5312095DF786BF8C99B58D42323AD9227D0903BCB8C98AAD9591`;
  clean MAP SHA256 is
  `5FB24B2735EFFD402C26BDC3B0D267B26B06DC6522A6B5B5D876491BA9A42A83`.
  `arm-none-eabi-size` reports `text=1044`, `data=0`, `bss=1536`,
  `dec=2580`, `hex=a14`. Linker memory report is RAM
  `1536 B / 128 KB / 1.17%` and FLASH `1044 B / 512 KB / 0.20%`.
- Key symbol boundary:
  retained ELF symbols include `gate_waveform_candidate_force_idle_low`,
  `gate_waveform_neutral_wrapper_hold_idle_forever`, `main`,
  `Reset_Handler`, `SystemInit`, and `_estack`. The retained ELF symbol table
  has no `gate_waveform_candidate_run_once` and no
  `main_waveform_candidate` symbol. The MAP shows
  `.text.gate_waveform_candidate_run_once` only in the discarded input-section
  area at `0x00000000`, which is expected with `-ffunction-sections` and
  `--gc-sections`.
- Boundary:
  this is build-only evidence only. It does not authorize firmware flash,
  Run / Debug, USB runtime execution, 24 V, Gate PWM output, oscilloscope
  probing on live gate or phase nodes, normal generated MCSDK app execution,
  Motor Pilot, Motor Profiler, motor connection, Hall closed loop, sensorless
  operation, power-stage readiness, or motor readiness.
- Next checkpoint:
  neutral-wrapper USB-only neutral-state phase-gate plan or review only. It is
  not flash, not Run / Debug, not USB runtime execution, not 24 V, not Gate
  PWM output, not Motor Pilot, not Motor Profiler, and not motor connection.

## 2026-06-21 STDRIVE101 Gate-Waveform Neutral-Wrapper Source Review No-Power Recorded

- Added the neutral-wrapper no-power source review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_neutral_wrapper_source_review_no_power_2026-06-21.md`.
- Added the neutral-wrapper source-review package:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/manual_gate_waveform_neutral_wrapper_source_package_2026-06-21/`.
- Evidence:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-NEUTRAL-WRAPPER-SOURCE-REVIEW-NO-POWER-001`.
- Task:
  `TASK-2026-06-21-stdrive101-gate-waveform-neutral-wrapper-source-review-no-power`.
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
- Source package boundary:
  the package intentionally has no `CMakeLists.txt`; the header requires
  `GATE_WAVEFORM_NEUTRAL_WRAPPER_BUILD_ACK` and raises `#error` until a later
  dated neutral-wrapper build-only boundary is opened. No object, ELF, MAP,
  HEX, or BIN artifact is produced or claimed here.
- Static source review:
  `main_neutral_wrapper.c` defines `main()` and calls
  `gate_waveform_neutral_wrapper_hold_idle_forever()`, which calls
  `gate_waveform_candidate_force_idle_low()` once before the forever loop and
  then forever inside the loop. Wrapper `Inc/` and `Src/` contain no
  `gate_waveform_candidate_run_once()` call and no TIM1 waveform-window or
  TIM1 output-enable helper.
- Future build-only requirement:
  any later neutral-wrapper build-only package must include the reviewed
  `gate_waveform_candidate.c`, exclude the old `main_waveform_candidate.c`,
  use `main_neutral_wrapper.c` as the only entry point, and record forbidden
  source / ELF / MAP screens.
- Boundary:
  this is source-review evidence only. It does not authorize object-only
  build, linked-image build, firmware flash, Run / Debug, USB runtime
  execution, 24 V, Gate PWM output, oscilloscope probing on live gate or phase
  nodes, normal generated MCSDK app execution, Motor Pilot, Motor Profiler,
  motor connection, Hall closed loop, sensorless operation, power-stage
  readiness, or motor readiness.
- Next checkpoint:
  neutral-wrapper build-only boundary plan or build-only record only. It is
  not USB runtime execution, not 24 V, not Gate PWM output, not Motor Pilot,
  not Motor Profiler, and not motor connection.

## 2026-06-21 STDRIVE101 Gate-Waveform USB-Only Neutral-State Phase-Gate Plan Recorded

- Added the Gate E3 USB-only neutral-state phase-gate plan:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_usb_only_neutral_state_phase_gate_plan_2026-06-21.md`.
- Evidence:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-USBONLY-NEUTRAL-STATE-PHASE-GATE-PLAN-001`.
- Task:
  `TASK-2026-06-21-stdrive101-gate-waveform-usbonly-neutral-state-phase-gate-plan`.
- Candidate image boundary carried forward:
  `.tmp/manual_gate_waveform_build_only_2026-06-21_clean/stdrive101_gate_waveform_candidate_image.elf`
  SHA256 `10BA818730E259AEBA8A5C5E5C96CFBA32FCB90AAA4136B775022B9D69ADCE7C`;
  MAP SHA256
  `170EA77C566F98CF9EF2AC88F76B154238A5404DC705AAE3917BEAE7C1503D4C`.
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
  this is phase-gate planning only. It performs no flash, no Run / Debug, no
  USB runtime execution, no 24 V, no Gate PWM output, no oscilloscope probing
  on live gate or phase nodes, no Motor Pilot, no Motor Profiler, and no motor
  connection. It also makes no power-stage readiness or motor readiness claim.
- Important DMM limitation:
  the Gate E2 candidate is not a pure lockout image. Its current `main()` calls
  `gate_waveform_candidate_run_once()` once and then loops forcing idle low.
  Therefore a future DMM-only USB check can record only steady post-window
  idle state; it cannot prove there was no reset-time or boot-time transient.
- Next checkpoint:
  only a separate Gate E3 USB-only neutral-state execution-entry record after
  explicit user request and freshly confirmed preconditions, or a source-side
  neutral-wrapper review if the team rejects the current `run_once()` image
  for a DMM-only neutral-state check. Gate E4 remains closed.

## 2026-06-21 STDRIVE101 Gate-Waveform Build-Only Record No-Power Recorded

- Added the Gate E2 no-power build-only record:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_build_only_record_no_power_2026-06-21.md`.
- Added the separate Gate E2 build-only package:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/manual_gate_waveform_build_only_2026-06-21/`.
- Source package carried forward:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/manual_gate_waveform_source_package_2026-06-21/`.
- Clean build directory:
  `.tmp/manual_gate_waveform_build_only_2026-06-21_clean/`.
- Evidence:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-BUILD-ONLY-RECORD-NO-POWER-001`.
- Task:
  `TASK-2026-06-21-stdrive101-gate-waveform-build-only-record-no-power`.
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
- Build boundary:
  the Gate E1 source package still has no `CMakeLists.txt`; only the Gate E2
  build-only package defines `GATE_WAVEFORM_CANDIDATE_GATE_E2_BUILD_ACK`.
  CMake configured as `Generic` / `arm` with
  `CMAKE_TRY_COMPILE_TARGET_TYPE=STATIC_LIBRARY`, STM32Cube GNU Arm GCC
  `14.3.1`, and Ninja `1.13.2`.
- Built targets and artifacts:
  `stdrive101_gate_waveform_candidate_objects` and
  `stdrive101_gate_waveform_candidate_image` built successfully. The clean ELF
  is
  `.tmp/manual_gate_waveform_build_only_2026-06-21_clean/stdrive101_gate_waveform_candidate_image.elf`
  SHA256 `10BA818730E259AEBA8A5C5E5C96CFBA32FCB90AAA4136B775022B9D69ADCE7C`;
  the clean MAP is
  `.tmp/manual_gate_waveform_build_only_2026-06-21_clean/stdrive101_gate_waveform_candidate_image.map`
  SHA256 `170EA77C566F98CF9EF2AC88F76B154238A5404DC705AAE3917BEAE7C1503D4C`.
  `arm-none-eabi-size` reports `text=1852`, `data=0`, `bss=1544`,
  `dec=3396`, `hex=d44`; linker memory use is RAM `1544 B / 128 KB /
  1.18%` and FLASH `1852 B / 512 KB / 0.35%`.
- Key symbols:
  `g_pfnVectors`, `disable_tim1_outputs_keep_counter`,
  `wait_for_pwm_periods_or_fault`,
  `gate_waveform_candidate_force_idle_low`,
  `gate_waveform_candidate_run_once`, `main`, `__libc_init_array`, `_init`,
  `_fini`, `Reset_Handler`, `SystemInit`, and `_estack` are recorded from the
  clean ELF.
- Forbidden screens:
  source/build, ELF symbol, and MAP screens are clean for normal generated
  MCSDK start / command ingress / PWM-output enable / Hall / PID /
  speed-loop / delay / printf / dynamic-allocation terms. README-only
  boundary text hits are not source or symbol paths.
- Boundary:
  this is build-only evidence. It does not authorize firmware flash, Run /
  Debug, USB runtime execution, 24 V, Gate PWM output, oscilloscope probing on
  live gate or phase nodes, normal generated MCSDK app execution, Motor Pilot,
  Motor Profiler, motor connection, Hall closed loop, sensorless operation,
  power-stage readiness, or motor readiness.
- Next checkpoint:
  Gate E3 only: a separate USB-only neutral-state phase-gate plan or review
  for the Gate E2 image. Gate E3 must still not open flash, Run / Debug, USB
  runtime execution, 24 V, Gate PWM output, Motor Pilot, Motor Profiler, motor
  connection, or readiness claims by default.

## 2026-06-21 STDRIVE101 Gate-Waveform Isolated Source Package Review No-Power Recorded

- Added the Gate E1 no-power source-package review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_isolated_source_package_review_no_power_2026-06-21.md`.
- Added the reviewed source package:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/manual_gate_waveform_source_package_2026-06-21/`.
- Evidence:
  `EV-2026-06-21-STDRIVE101-GATE-WAVEFORM-ISOLATED-SOURCE-PACKAGE-REVIEW-NO-POWER-001`.
- Task:
  `TASK-2026-06-21-stdrive101-gate-waveform-isolated-source-package-review-no-power`.
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
- Source package boundary:
  the package intentionally has no `CMakeLists.txt`; the header requires
  `GATE_WAVEFORM_CANDIDATE_GATE_E2_BUILD_ACK` and raises `#error` until a
  later dated Gate E2 build-only boundary is opened. No object, ELF, MAP, HEX,
  or BIN artifact is produced or claimed here.
- Static source review:
  the package fixes candidate driver-input pins as `PA8`, `PA9`, `PA10`,
  `PB13`, `PB14`, and `PB15`; uses `gate_waveform_candidate_force_idle_low()`
  before and after the candidate window; freezes the candidate constants at
  `1 kHz`, `100` permille duty, `16` window periods, `8` pre-idle periods,
  `32` post-idle periods, and `DTG 0x90`; makes TIM1 `MOE`, `CCER`, break,
  AOE clearing, dead-time, and complementary-output policy visible in source;
  and polls `nFAULT` through `wait_for_pwm_periods_or_fault()`, which disables
  TIM1 outputs and forces all six pins low on a fault.
- Forbidden-source screen:
  source-path review found no `MC_StartMotor1`, `MCI_START`, PC13 start /
  stop, MCP, ASPEP, `R3_2_TurnOnLowSides`, `PWMC_SwitchOnPWM`,
  `LL_TIM_EnableAllOutputs`, Hall, PID, speed-loop, blocking delay, printf, or
  dynamic-allocation source path in `Inc/` or `Src/`. The only text hits for
  Motor Pilot / Motor Profiler are boundary language in the package README.
- Boundary:
  this is source-review evidence only. It does not authorize object-only
  build, linked-image build, firmware flash, Run / Debug, USB runtime
  execution, 24 V, Gate PWM output, oscilloscope probing on live gate or phase
  nodes, normal generated MCSDK app execution, Motor Pilot, Motor Profiler,
  motor connection, Hall closed loop, sensorless operation, power-stage
  readiness, or motor readiness.
- Next checkpoint:
  Gate E2 only: a separate object-only and linked-image build-only boundary
  plan or build-only record for this exact reviewed source package. Gate E2
  still must not open flash, Run / Debug, USB runtime execution, 24 V, Gate
  PWM output, Motor Pilot, Motor Profiler, motor connection, or readiness
  claims.

## 2026-06-20 STDRIVE101 Gate-Waveform Image Design Plan No-Power Recorded

- Added the Gate E0 no-power design-boundary plan:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_image_design_plan_no_power_2026-06-20.md`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-GATE-WAVEFORM-IMAGE-DESIGN-PLAN-NO-POWER-001`.
- Task:
  `TASK-2026-06-20-stdrive101-gate-waveform-image-design-plan-no-power`.
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
  this is Gate E0 design planning only. It creates no source package, makes no
  CMake edits, runs no build, flashes no firmware, performs no Run / Debug,
  executes no USB runtime, applies no 24 V, emits no Gate PWM output, probes no
  live gate or phase waveform, starts no normal generated MCSDK application,
  opens no Motor Pilot or Motor Profiler path, connects no motor, and makes no
  Hall closed-loop, sensorless, power-stage readiness, or motor readiness
  claim.
- Required future image shape:
  any later waveform candidate must be a separate isolated image, not the
  normal generated MCSDK app and not the existing lockout image. The only
  candidate driver-input pins are `PA8`, `PA9`, `PA10`, `PB13`, `PB14`, and
  `PB15`; all six must be forced low before and after any future candidate
  window. TIM1 `MOE`, `CCER`, break, AOE, dead-time, polarity, and
  complementary-overlap policy must be reviewed before any source or build.
- Next checkpoint:
  Gate E1 only: a separate isolated waveform source-package planning/review
  record, or a build-side boundary plan that still has no build, flash, Run /
  Debug, USB runtime execution, 24 V, Gate PWM output, Motor Pilot, Motor
  Profiler, motor connection, or readiness claim.

## 2026-06-20 STDRIVE101 Gate-Waveform / PWM-Output No-Power Phase-Gate Plan Recorded

- Added the no-power phase-gate plan:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_waveform_pwm_output_no_power_phase_gate_plan_2026-06-20.md`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-GATE-WAVEFORM-PWM-OUTPUT-NO-POWER-PHASE-GATE-PLAN-001`.
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
- Carried-forward evidence:
  the 24V static lockout carry-forward result closes the duplicate static
  measurement branch and carries forward HSPY `CV`, about `0.045 A`,
  `CN3_1` through `CN3_6` close to `0 V`, `nFAULT = 3.3 V`,
  `CN3_14 / 3V3 = 3.3 V`, `REG12 = 0.3 V`, plus the USB-only lockout
  runtime result with the reviewed lockout image and driver-input stop rule
  not hit.
- Future ladder named only:
  Gate E0 no-power waveform-image design plan, Gate E1 isolated source
  package, Gate E2 build-only linked image, Gate E3 USB-only neutral-state
  runtime check, Gate E4 future scope-only no-motor execution-entry, and
  Gate E5 result record. None of these execution gates are opened by this
  record.
- Boundary:
  this is plan-only evidence. It does not authorize firmware flash,
  Run / Debug, USB runtime execution, 24 V, Gate PWM output, oscilloscope
  probing on live gate or phase nodes, normal generated MCSDK app execution,
  Motor Pilot, Motor Profiler, motor connection, Hall closed loop, sensorless
  operation, power-stage readiness, or motor readiness.
- Next checkpoint:
  Gate E0 only: a separate no-power waveform-image design plan, or source /
  build review that keeps all execution actions closed.

## 2026-06-20 STDRIVE101 Manual Gate-Test 24V Static Lockout Carry-Forward Result Recorded

- Added the no-repeat carry-forward result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_24v_static_lockout_carry_forward_result_2026-06-20.md`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-24V-STATIC-LOCKOUT-CARRY-FORWARD-RESULT-001`.
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
  HSPY `CV`; current about `0.045 A`; motor disconnected; wake stimulus
  removed; `CN3_1` through `CN3_6` all close to `0 V`;
  `CN3_13 / nFAULT = 3.3 V`; `CN3_14 / 3V3 = 3.3 V`; and `REG12 = 0.3 V`.
- Carried-forward USB-only lockout runtime evidence:
  ELF SHA256 `87BF3F7A28949F8DB654927292083609E52AB46C511CB6191D03B280DBFFE9B6`;
  BIN SHA256
  `CBF833C8E9289D8B4A952C32C641CAA94928F1F8119C5DC528EBD779915EA6BE`;
  `CN3_1` through `CN3_6 = 0 V`; `CN3_13 / nFAULT = 3.3 V`;
  `CN3_14 / 3V3 = 3.3 V`; `REG12 = 0 V`; driver-input stop rule not hit.
- Boundary:
  this is a consolidation record, not a new hardware measurement. It closes
  the duplicate-measurement branch opened by the 24V static lockout
  execution-entry record after the user clarified that the equivalent
  USB + 24 V all-inputs-low static check was already measured and recorded.
  It does not claim a fresh simultaneous `lockout image + 24 V` direct
  measurement and does not authorize firmware flash, new Run / Debug, normal
  generated MCSDK app run, Gate PWM output, Motor Pilot, Motor Profiler,
  motor connection, Hall closed loop, sensorless operation, power-stage
  readiness, or motor readiness.
- Next checkpoint:
  create only a no-power phase-gate plan for the next higher-risk step, such
  as gate-waveform / PWM-output planning. Do not execute PWM, Motor Pilot,
  Motor Profiler, or motor work from this record.

## 2026-06-20 STDRIVE101 Manual Gate-Test 24V Static Lockout Execution Entry Recorded

- Added the 24V static lockout execution-entry record:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_24v_static_lockout_execution_entry_2026-06-20.md`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-24V-STATIC-LOCKOUT-EXECUTION-ENTRY-001`.
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
  this opened exactly one bounded 24 V static lockout measurement pass as a
  historical execution-entry record. The later carry-forward result closes
  the duplicate-measurement branch without repeating the same static table. It
  does not flash, does not Run / Debug, does not run a normal generated MCSDK
  app, does not open Gate PWM output, Motor Pilot, Motor Profiler, motor
  connection, Hall closed loop, sensorless operation, power-stage readiness,
  or motor readiness.
- Next checkpoint:
  superseded by the carry-forward result; do not repeat the 24 V static table
  unless the image, wiring, board condition, or tool state changes.

## 2026-06-20 STDRIVE101 Manual Gate-Test 24V Static Lockout Phase-Gate Plan Recorded

- Added the 24V static lockout phase-gate plan:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_24v_static_lockout_phase_gate_plan_2026-06-20.md`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-24V-STATIC-LOCKOUT-PHASE-GATE-PLAN-001`.
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
  `CN3_13 / nFAULT = 3.3 V`, `CN3_14 / 3V3 = 3.3 V`, `REG12 = 0 V`,
  and driver-input stop rule not hit. The earlier USB plus 24V static
  baseline records HSPY `CV`, about `0.045 A`, six driver inputs close to
  `0 V`, `CN3_13 / nFAULT = 3.3 V`, `CN3_14 / 3V3 = 3.3 V`, and
  `REG12 = 0.3 V`.
- Boundary:
  this is a phase-gate plan only. It does not apply 24V, does not flash, does
  not Run / Debug, does not run a normal generated MCSDK app, does not open
  Gate PWM output, Motor Pilot, Motor Profiler, motor connection, Hall closed
  loop, sensorless operation, power-stage readiness, or motor readiness.
- Next checkpoint:
  only a later separate 24 V static lockout execution-entry record may apply
  HSPY, and only after explicit user request plus freshly confirmed
  preconditions.

## 2026-06-20 STDRIVE101 Manual Gate-Test USB-Only Runtime Lockout Result Recorded

- Added the USB-only runtime lockout result record:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_usb_only_runtime_lockout_result_2026-06-20.md`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-USBONLY-RUNTIME-LOCKOUT-RESULT-001`.
- Decision:
  `STDRIVE101 manual gate-test USB-only runtime lockout result / reviewed
  lockout ELF converted to BIN and copied through ST-LINK mass storage /
  no FAIL.TXT after copy / user-reported CN3_1 through CN3_6 all 0 V /
  nFAULT 3.3 V / CN3_14 3.3 V / REG12 0 V / driver-input stop rule not hit /
  USB-only runtime evidence only / no 24 V / no PWM-output validation /
  no Motor Pilot / no Motor Profiler / no motor connection / no
  powered-drive readiness`.
- Download evidence:
  `.tmp/manual_gate_test_lockout_linked_image/stdrive101_gate_lockout_image.elf`,
  SHA256 `87BF3F7A28949F8DB654927292083609E52AB46C511CB6191D03B280DBFFE9B6`;
  generated `.bin`, SHA256
  `CBF833C8E9289D8B4A952C32C641CAA94928F1F8119C5DC528EBD779915EA6BE`;
  copied to ST-LINK mass-storage `D:` / `NOD_G474RE`; no `FAIL.TXT` after
  copy.
- User-reported USB-only readings:
  `CN3_1 = 0 V`, `CN3_2 / LIN1 = 0 V`, `CN3_3 = 0 V`,
  `CN3_4 = 0 V`, `CN3_5 = 0 V`, `CN3_6 = 0 V`,
  `CN3_13 / nFAULT = 3.3 V`, `CN3_14 / 3V3 = 3.3 V`,
  and `REG12 = 0 V`.
- Boundary:
  this proves only the USB-only lockout runtime measurement state. It does not
  authorize 24 V, Gate PWM output, Motor Pilot, Motor Profiler, motor
  connection, Hall closed loop, sensorless operation, power-stage readiness, or
  motor readiness.
- Next checkpoint:
  a separate dated phase-gate review before any later 24 V static lockout
  check, PWM/gate waveform task, or motor task is considered.

## 2026-06-20 STDRIVE101 Manual Gate-Test USB-Only Runtime Lockout Execution Entry Recorded

- Added the USB-only runtime lockout execution-entry record:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_usb_only_runtime_lockout_execution_entry_2026-06-20.md`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-USBONLY-RUNTIME-LOCKOUT-EXECUTION-ENTRY-001`.
- Decision:
  `STDRIVE101 manual gate-test USB-only runtime lockout execution entry /
  user confirmed HSPY 24 V OFF and physically disconnected, VS 24V_FUSED
  below 1 V, motor disconnected, wake stimulus removed, Motor Pilot and Motor
  Profiler closed, no abnormal heat smell sound / linked-image ELF hash matched
  / opens exactly one USB-only lockout flash-run measurement pass / no 24 V /
  no PWM-output validation / no Motor Pilot / no Motor Profiler / no motor
  connection / no powered-drive readiness`.
- Candidate image:
  `.tmp/manual_gate_test_lockout_linked_image/stdrive101_gate_lockout_image.elf`,
  SHA256 `87BF3F7A28949F8DB654927292083609E52AB46C511CB6191D03B280DBFFE9B6`.
- User-confirmed physical boundary:
  HSPY / 24 V `OFF` and physically disconnected; `VS / 24V_FUSED < 1 V`;
  motor disconnected; `10 kohm` wake resistor / `LIN1` stimulus removed;
  Motor Pilot / Profiler closed; no abnormal heat / smell / sound.
- Boundary:
  opens only one USB-only lockout flash / run measurement pass using the exact
  candidate ELF. Still no 24 V, no Gate PWM output, no Motor Pilot, no Motor
  Profiler, no motor connection, no Hall closed loop, no sensorless operation,
  no power-stage readiness, and no motor readiness.
- Next checkpoint:
  after the user measures `CN3_1` through `CN3_6`, `CN3_13 / nFAULT`,
  `CN3_14 / 3V3`, and `REG12`, create a separate runtime result record.

## 2026-06-20 STDRIVE101 Manual Gate-Test USB-Only Runtime Lockout Phase-Gate Plan Recorded

- Added the USB-only runtime lockout phase-gate plan:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_usb_only_runtime_lockout_phase_gate_plan_2026-06-20.md`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-USBONLY-RUNTIME-LOCKOUT-PHASE-GATE-PLAN-001`.
- Decision:
  `STDRIVE101 manual gate-test USB-only runtime lockout phase-gate plan
  no-power / linked-image build-only record accepted as image-boundary
  evidence / candidate USB-only runtime preconditions, measurement table, and
  stop rules named / phase-gate plan only / no flash / no Run Debug / no USB
  runtime execution / no 24 V / no PWM-output validation / no powered-drive
  readiness`.
- Candidate image carried forward:
  `stdrive101_gate_lockout_image`,
  `.tmp/manual_gate_test_lockout_linked_image/stdrive101_gate_lockout_image.elf`,
  SHA256 `87BF3F7A28949F8DB654927292083609E52AB46C511CB6191D03B280DBFFE9B6`;
  `.tmp/manual_gate_test_lockout_linked_image/stdrive101_gate_lockout_image.map`,
  SHA256 `A020546A3D1D56B1C509939161BD80E5A25EC5843C928B9BC13E8D07684FF6C0`.
- Later execution gates named:
  explicit user request to execute USB-only lockout runtime, matching ELF hash
  or replacement build-only record, HSPY / 24 V OFF and disconnected,
  `VS / 24V_FUSED < 1 V`, motor disconnected, wake resistor removed,
  Motor Pilot / Profiler closed, and no normal MCSDK ingress.
- Boundary:
  this is a phase-gate plan only. It does not authorize flash, Run / Debug,
  USB runtime execution, 24 V, Gate PWM output, Motor Pilot, Motor Profiler,
  motor connection, Hall closed loop, sensorless operation, power-stage
  readiness, or motor readiness.
- Next checkpoint:
  only a later separate USB-only runtime execution record may execute anything,
  and only after explicit user request plus the named preconditions.

## 2026-06-20 STDRIVE101 Manual Gate-Test Linked-Image Build-Only Record Recorded

- Added the linked-image build-only record:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_linked_image_build_only_record_2026-06-20.md`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-LINKED-IMAGE-BUILD-ONLY-RECORD-001`.
- Decision:
  `STDRIVE101 manual gate-test linked-image build-only record no-power /
  repo-local CMake linked target stdrive101_gate_lockout_image added /
  Generic bare-metal CMake configure and Ninja build passed / ELF and MAP
  artifacts produced and hashed / forbidden source ELF MAP screens clean /
  build-only evidence / no flash / no Run Debug / no USB runtime / no 24 V /
  no PWM-output validation / no powered-drive readiness`.
- Build target:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/manual_gate_test_lockout_build_only_2026-06-20/CMakeLists.txt`
  now keeps `stdrive101_gate_lockout_objects` and adds linked target
  `stdrive101_gate_lockout_image`.
- Build result:
  CMake configured with `CMAKE_SYSTEM_NAME=Generic`,
  `CMAKE_SYSTEM_PROCESSOR=arm`, STM32Cube GNU Arm GCC `14.3.1`, and Ninja;
  `cmake --build .tmp\manual_gate_test_lockout_linked_image --target
  stdrive101_gate_lockout_image --verbose` exited `0`.
- Produced artifacts:
  `.tmp/manual_gate_test_lockout_linked_image/stdrive101_gate_lockout_image.elf`,
  `24788` bytes, SHA256
  `87BF3F7A28949F8DB654927292083609E52AB46C511CB6191D03B280DBFFE9B6`;
  `.tmp/manual_gate_test_lockout_linked_image/stdrive101_gate_lockout_image.map`,
  `123825` bytes, SHA256
  `A020546A3D1D56B1C509939161BD80E5A25EC5843C928B9BC13E8D07684FF6C0`.
- Size / memory:
  `text=1356`, `data=0`, `bss=1568`, RAM `1568 B / 128 KB`, FLASH
  `1356 B / 512 KB`.
- Boundary:
  this is linked-image build-only evidence. It does not authorize flash,
  Run / Debug, USB runtime execution, 24 V, Gate PWM output, Motor Pilot,
  Motor Profiler, motor connection, Hall closed loop, sensorless operation,
  power-stage readiness, or motor readiness.
- Next checkpoint:
  write a separate USB-only runtime lockout phase-gate plan or review before
  any runtime is discussed; do not execute runtime yet.

## 2026-06-20 STDRIVE101 Manual Gate-Test Linked-Image Build-Boundary Plan Recorded

- Added the linked-image build-boundary plan:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_linked_image_build_boundary_plan_2026-06-20.md`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-LINKED-IMAGE-BUILD-BOUNDARY-PLAN-001`.
- Decision:
  `STDRIVE101 manual gate-test linked-image build-boundary plan no-power /
  object-only lockout build pass and USB-only runtime lockout preparation
  carried forward / future link inputs and minimum image artifacts named /
  boundary plan only / no linked image built / no flash / no runtime / no
  PWM-output validation / no powered-drive readiness`.
- Candidate future link inputs are fixed to repo-local
  `apps/stm32_g474_foc/nucleo_g474re_baseline/` startup, linker script,
  `system_stm32g4xx.c`, `syscalls.c`, and `sysmem.c`, with SHA256 hashes
  recorded in the plan.
- Future target name, if a later build-only task creates it:
  `stdrive101_gate_lockout_image`; minimum future artifacts are ELF and MAP.
- Boundary:
  this is a boundary-plan record only. It does not create a linked image,
  does not edit CMake, and does not authorize flash, Run / Debug, USB runtime
  execution, 24 V, Gate PWM output, Motor Pilot, Motor Profiler, motor
  connection, Hall closed loop, sensorless operation, power-stage readiness,
  or motor readiness.
- Next checkpoint:
  create a separate linked-image build-only record for the lockout image; do
  not execute runtime yet.

## 2026-06-20 STDRIVE101 Manual Gate-Test USB-Only Runtime Lockout Prep Recorded

- Added the USB-only runtime lockout preparation record:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_usb_only_runtime_lockout_prep_2026-06-20.md`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-USBONLY-RUNTIME-LOCKOUT-PREP-001`.
- Decision:
  `STDRIVE101 manual gate-test USB-only runtime lockout preparation no-power /
  object-only lockout build pass carried forward / exact source and object
  provenance recorded / future runtime must be USB-only with no 24 V, motor
  disconnected, power board not powered, and six driver inputs expected low /
  preparation only / no flash / no runtime / no PWM-output validation / no
  powered-drive readiness`.
- Carried-forward source hashes:
  `gate_test_lockout.h`
  SHA256 `E1E69943BFEBC50C12C8FAAEE12203BD4FE5D9A6474E318C9EC10AA8111A9862`,
  `gate_test_lockout.c`
  SHA256 `C5277630BC99E4BA1966799699F6660CA6ABB361EE17FF0AC89D8369135B264B`,
  `main_lockout.c`
  SHA256 `D6BD1CB9BA4C54774E06C4B9381EA94C86903F7FB08426CAC904AEFB1DFB3EE3`,
  and `CMakeLists.txt`
  SHA256 `B3887E85544EF5BB89309200689276312CF2D6BA0287CCAA89684B1F23190CE1`.
- Boundary:
  this is preparation evidence only. It does not authorize flash, Run /
  Debug, USB runtime execution, 24 V, Gate PWM output, Motor Pilot, Motor
  Profiler, motor connection, Hall closed loop, sensorless operation,
  power-stage readiness, or motor readiness.
- Next checkpoint:
  create a linked-image build-boundary plan or build-only record for the
  lockout image; do not execute runtime yet.

## 2026-06-20 STDRIVE101 Manual Gate-Test Lockout Object-Only Build Pass Recorded

- Added the object-only build pass record:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_lockout_object_build_pass_2026-06-20.md`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-LOCKOUT-OBJECT-BUILD-PASS-NO-POWER-001`.
- Decision:
  `STDRIVE101 manual gate-test lockout object-only build pass no-power /
  repo-local CMake object library configured with STM32Cube GNU Arm GCC
  14.3.1 and Ninja 1.13.2 / stdrive101_gate_lockout_objects built successfully
  / gate_test_lockout.c.obj and main_lockout.c.obj produced / no lockout ELF
  HEX BIN MAP linked image produced / no flash / no runtime / no PWM-output
  validation / no powered-drive readiness`.
- Produced lockout object files:
  `gate_test_lockout.c.obj`, `2084` bytes,
  SHA256 `C395D049FDCFC3213B65DF2813E07A663B5BF09D7C983BD2FBEC7025F0B79FE8`;
  `main_lockout.c.obj`, `924` bytes,
  SHA256 `B2C77D50306258F7A7FFAE745119B17F9E18E703DC39A98CDC0810ACC4C66D98`.
- Boundary:
  this proves only no-power object compilation of the isolated lockout source.
  It does not authorize flash, Run / Debug, 24 V, Gate PWM output, Motor Pilot,
  Motor Profiler, motor connection, Hall closed loop, sensorless operation,
  power-stage readiness, or motor readiness.
- Next checkpoint:
  write USB-only runtime lockout preparation; do not execute runtime yet.

## 2026-06-20 STDRIVE101 Manual Gate-Test Lockout Object-Only Target Recorded

- Added a repo-local object-only CMake target for the isolated lockout package:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/manual_gate_test_lockout_build_only_2026-06-20/CMakeLists.txt`.
- Added the target setup record:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_lockout_object_target_2026-06-20.md`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-LOCKOUT-OBJECT-TARGET-NO-POWER-001`.
- Decision:
  `STDRIVE101 manual gate-test lockout object-only target no-power /
  repo-local CMake object library target added for the isolated lockout source
  package / target compiles only gate_test_lockout.c and main_lockout.c object
  files / no ELF HEX BIN link target / REPO_ROOT path corrected and CMSIS
  headers resolved / sandbox blocked external Ninja during configure and
  auto-review escalation returned 503 / no object build pass claimed / no
  flash / no runtime / no PWM-output validation / no powered-drive readiness`.
- Boundary:
  this is build-target setup evidence only. It does not authorize flash,
  Run / Debug, 24 V, Gate PWM output, Motor Pilot, Motor Profiler, motor
  connection, Hall closed loop, sensorless operation, power-stage readiness, or
  motor readiness.
- Next checkpoint:
  rerun CMake configure and build the object-only target when external-tool
  approval is available; record object files, compiler diagnostics, sizes, and
  hashes.

## 2026-06-20 STDRIVE101 Manual Gate-Test Lockout Source Package Recorded

- Added the repo-local isolated lockout source package:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/manual_gate_test_lockout_build_only_2026-06-20/`.
- Added the Gate B no-power source-package record:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_lockout_source_package_2026-06-20.md`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-LOCKOUT-SOURCE-PACKAGE-NO-POWER-001`.
- Decision:
  `STDRIVE101 manual gate-test lockout source package no-power / repo-local
  isolated lockout source added / six driver input pins forced GPIO low /
  PB12 nFAULT kept as input / TIM1 CCER cleared / TIM1 MOE and automatic
  output cleared / TIM1 break left enabled / forbidden normal MCSDK start and
  command ingress symbols absent from lockout Src and Inc / source package only
  / no embedded build target yet / no flash / no runtime / no PWM-output
  validation / no powered-drive readiness`.
- Boundary:
  this is source-package and static-inspection evidence only. It does not
  authorize flash, Run / Debug, 24 V, Gate PWM output, Motor Pilot, Motor
  Profiler, motor connection, Hall closed loop, sensorless operation,
  power-stage readiness, or motor readiness.
- Next checkpoint:
  create a separate repo-local embedded build target or an explicitly copied
  external Workbench clone for compile-only checking; still no flash, runtime,
  24 V, PWM output, or motor.

## 2026-06-20 STDRIVE101 Manual Gate-Test Firmware Plan Recorded

- Added the no-power-only manual gate-test firmware plan:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_manual_gate_test_firmware_plan_no_power_2026-06-20.md`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-MANUAL-GATE-TEST-FIRMWARE-PLAN-NO-POWER-001`.
- Decision:
  `STDRIVE101 manual gate-test firmware plan no-power / normal MCSDK start path
  remains blocked / future gate-test must use an isolated lockout firmware path
  that avoids MC_StartMotor1, MCI_START, PC13 start-stop, MCP command ingress,
  Motor Pilot, Hall closed-loop paths, speed-loop paths, and motor connection /
  plan only / no PWM-output validation / no powered-drive readiness`.
- Planned future lockout shape:
  the first manual image, if a later phase gate opens implementation, must keep
  `PA8`, `PA9`, `PA10`, `PB13`, `PB14`, and `PB15` as GPIO outputs low, monitor
  `PB12 / nFAULT` as input, keep TIM1 `MOE = 0`, `CCER = 0`, automatic output
  disabled, and break enabled. It must not call normal MCSDK start or output
  enable APIs.
- Boundary:
  this plan does not authorize firmware edits, build, flash, Run / Debug,
  24 V, Gate PWM output, Motor Pilot, Motor Profiler, motor connection, Hall
  closed loop, sensorless operation, power-stage readiness, or motor readiness.
- Next checkpoint:
  review this plan; if accepted later, create a separate no-power build-only
  implementation task package for the isolated lockout firmware.

## 2026-06-20 STDRIVE101 R3_2 MCSDK PWM Output Path Source Closure Recorded

- Added the no-power source closure for the exact local MCSDK `R3_2` PWM path:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_r3_2_mcsdk_pwm_output_path_source_closure_2026-06-20.md`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-R3-2-MCSDK-PWM-OUTPUT-PATH-SOURCE-CLOSURE-001`.
- Exact reviewed source:
  `C:\Users\gregrg\.st_workbench\projects\QIANSAI_G474_STDRIVE101_FOC_P2\MCSDK_v6.4.2-Full\MotorControl\MCSDK\MCLib\G4xx\Src\r3_2_g4xx_pwm_curr_fdbk.c`,
  SHA256 `D3787B25374154AB1DC6A2CABD05DE299D5691DA92DDC4DE4BEC93DE81BE2451`.
- Decision:
  `STDRIVE101 R3_2 MCSDK PWM output path source closure / exact local
  Workbench MCSDK r3_2_g4xx_pwm_curr_fdbk.c found and hashed / R3_2 output
  enable behavior reviewed / normal generated MCSDK start remains blocked for
  powered PWM because start path disables BRK before low-side boot-cap and
  R3_2_TurnOnLowSides enables TIM1 main outputs with 0-tick low-sides-on
  semantics / no PWM-output validation / no powered-drive readiness`.
- Key finding:
  the normal generated `MCI_START` path can call `LL_TIM_DisableBRK(TIM1)`
  before `R3_2_TurnOnLowSides()`. In the reviewed MCSDK source,
  `R3_2_TurnOnLowSides()` treats `0` ticks as low-sides ON and calls
  `LL_TIM_EnableAllOutputs(TIMx)`. Later `PWMC_SwitchOnPWM()` also enables
  TIM1 main outputs.
- Boundary:
  this is source evidence only. It does not authorize motor connection, Gate
  PWM output, Motor Pilot, Motor Profiler, firmware Flash / Run / Debug, Hall
  closed loop, sensorless operation, power-stage readiness, or motor readiness.
- Next checkpoint:
  write a separate no-power-only manual gate-test firmware plan that avoids the
  normal MCSDK start path, PC13 start/stop, MCP / Motor Pilot ingress, Hall
  closed loop, speed loop, and motor connection.

## 2026-06-20 STDRIVE101 PWM Gate-Test No-Power Source Review Recorded

- Added the no-power source/configuration review for a future explicit
  PWM/gate-test phase gate:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_pwm_gate_test_no_power_source_review_2026-06-20.md`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-PWM-GATE-TEST-NO-POWER-SOURCE-REVIEW-001`.
- Decision:
  `STDRIVE101 PWM gate-test no-power source review / static hardware screen
  passed for planning only / generated MCSDK direct PWM gate remains blocked by
  command-ingress, external R3_2 implementation, BKIN polarity, Hall-route, and
  generation-log trust gaps / no PWM-output validation / no powered-drive
  readiness`.
- Key findings:
  `main.c` has no direct `MC_StartMotor1()` autostart, but PC13
  start/stop and MCSDK command paths can set `DirectCommand = MCI_START`.
  The generated state path then reaches `R3_2_TurnOnLowSides()` and later
  `PWMC_SwitchOnPWM()`. The exact R3_2 PWM implementation is pulled from an
  external MCSDK source path that is not packet-local, and the generation log
  contains PWM / BKIN / MotorControl invalid-parameter messages.
- Boundary:
  this is a no-power planning gate only. It does not authorize motor
  connection, Gate PWM output, Motor Pilot, Motor Profiler, firmware Flash /
  Run / Debug, Hall closed loop, sensorless operation, power-stage readiness,
  or motor readiness.
- Next checkpoint:
  close the source packet by reviewing the exact local MCSDK
  `r3_2_g4xx_pwm_curr_fdbk.c` plus TIM1 BKIN / `nFAULT` polarity and
  command-ingress behavior, or write a separate no-power-only manual
  gate-test firmware plan.

## 2026-06-20 STDRIVE101 USB + 24V Static Recheck Recorded

- Added the bounded USB + 24 V static recheck result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_usb24_static_recheck_result_2026-06-20.md`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-USB24-STATIC-RECHECK-001`.
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
- Interpretation:
  with USB/ST-LINK connected and 24 V current-limited input applied, the six
  driver inputs were still reported low, `nFAULT` remained high, and `REG12`
  stayed low. This closes the immediate pre-PWM static safety screen, but it
  does not prove firmware PWM behavior, gate waveforms, motor behavior,
  Hall feedback, power-stage readiness, or motor readiness.
- Boundary:
  turn HSPY output OFF before any later wiring change and reconfirm
  `VS / 24V_FUSED < 1 V`. The next project step should be no-power firmware /
  source planning for a future explicit PWM/gate-test phase gate, not motor,
  PWM output, Motor Pilot, or Motor Profiler.

## 2026-06-20 STDRIVE101 USB-Only MCU Default Input State Recorded

- Added the no-24V USB/ST-LINK default-state result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_usbonly_mcu_default_input_state_result_2026-06-20.md`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-USBONLY-MCU-DEFAULT-INPUT-STATE-001`.
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
- Interpretation:
  no driver input was reported accidentally high with USB/ST-LINK connected
  and no 24 V applied. `P13/P14` naming should be corrected later if the user
  meant a connector name different from `CN3_13/CN3_14`.
- Boundary:
  this does not authorize PWM, motor, Motor Pilot, Motor Profiler, firmware
  Flash / Run / Debug, Hall closed loop, sensorless operation, power-stage
  readiness, or motor readiness. The next bounded step may be a static 24 V
  check with USB/ST-LINK connected and no firmware command.

## 2026-06-20 STDRIVE101 All-Inputs-Low Static Recheck Recorded

- Added the post-retest static recheck result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_all_inputs_low_static_recheck_result_2026-06-20.md`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-ALL-INPUTS-LOW-STATIC-RECHECK-001`.
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
- Interpretation:
  the immediate recovery-static branch is closed: after the clean `LIN1` wake
  retest and stimulus removal, the six driver inputs were reported low and
  `REG12` returned to the low voltage region. This does not prove MCU reset
  default GPIO behavior, PWM safety, gate waveforms, motor behavior,
  power-stage readiness, or motor readiness.
- Boundary:
  before any later wiring change, set HSPY output OFF and reconfirm
  `VS / 24V_FUSED < 1 V`. The next bounded hardware-adjacent step should be
  no-24V USB/ST-LINK default-state checking, not motor, PWM, Motor Pilot, or
  Motor Profiler.

## 2026-06-20 STDRIVE101 Single-Input Wake Retest Clean Result Recorded

- Added the bounded retest result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_reg12_single_input_wake_retest_clean_result_2026-06-20.md`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-SINGLE-INPUT-WAKE-RETEST-CLEAN-001`.
- User-reported retest readings:
  `retest_supply_state = CV`, `retest_supply_current_A = 0.048 A`,
  `retest_CN3_2_LIN1_V = 3.13 V`, `retest_CN3_13_nFAULT_V = 3.3 V`,
  and `retest_REG12_V = 12 V`.
- User-reported recovery readings after removing the `10 kohm` stimulus and
  restoring all-inputs-low:
  `recovery_supply_state = CV`, `recovery_supply_current_A = 0.045 A`,
  `recovery_CN3_13_nFAULT_V = 3.3 V`, and `recovery_REG12_V = 0.33 V`.
- Decision:
  `STDRIVE101 REG12 single-input wake retest clean result / CN3_14 3V3 through
  10 kohm to CN3_2 LIN1 / LIN1 3.13 V / HSPY CV 0.048 A / REG12 rose to
  12 V / nFAULT stayed 3.3 V / recovery all-inputs-low REG12 0.33 V and
  nFAULT 3.3 V / previous nFAULT-low wake blocker not reproduced after
  gate-source pulldown rework / no PWM-output validation / no powered-drive
  readiness`.
- Interpretation:
  the bounded retest now shows clean STDRIVE101 standby exit and recovery for
  the single `LIN1` stimulus after the gate-source pulldown rework. It does
  not validate PWM, gate waveforms, Hall closed-loop behavior, sensorless
  behavior, motor operation, power-stage readiness, or motor readiness.
- Boundary:
  before any later wiring change, set HSPY output OFF and reconfirm
  `VS / 24V_FUSED < 1 V`; keep the `10 kohm` stimulus removed unless a
  separate bounded diagnostic explicitly reinstalls it. No motor, Gate PWM,
  Motor Pilot, Motor Profiler, firmware Run / Debug, or readiness claim is
  opened.

## 2026-06-20 STDRIVE101 Gate-Source Pulldown Rework Result Recorded

- Added the no-power gate-source pulldown rework result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_gate_source_pulldown_rework_result_2026-06-20.md`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-GATE-SOURCE-PULLDOWN-REWORK-RESULT-001`.
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
  `VS_OFF_V = 0 V` closes the missing power-off-voltage field for this
  no-power record. Reconfirm `VS / 24V_FUSED < 1 V` before any later wiring
  change or powered retest. This result does not authorize repeat powered
  wake, alternate input stimulus, firmware implementation, flash, Run / Debug,
  motor connection, Gate PWM, Motor Pilot, Motor Profiler, Hall closed loop,
  sensorless operation, power-stage readiness, or motor readiness.

## 2026-06-20 STDRIVE101 Protection Nodes No-Power DMM Result Recorded

- Added the no-power protection-node DMM result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_protection_nodes_no_power_dmm_result_2026-06-20.md`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-PROTECTION-NODES-NO-POWER-DMM-RESULT-001`.
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
- Interpretation:
  the corrected resistance / diode-mode readings supersede the earlier generic
  `蜂鸣` reports for interpretation. They reduce concern about simple hard
  shorts on `CP`, `REG12`, and `OUT1`, but they do not prove the cause of
  `nFAULT = 0 V`.
- Boundary:
  the latest corrected table did not restate `VS_OFF_V`; confirm
  `VS / 24V_FUSED < 1 V` before any further measurement. Continue no-power
  only, with no unknown-node probing, no repeat powered wake, no motor, no
  PWM, and no powered-drive readiness claim.

## 2026-06-20 STDRIVE101 Fault Review Schematic Marking Added

- Added the no-power source-marking artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_fault_review_schematic_marking_2026-06-20.md`.
- Added marked schematic images:
  `hardware/schematic/annotated/stdrive101_fault_review_full_marked_2026-06-20.png`,
  `hardware/schematic/annotated/stdrive101_driver_control_nodes_marked_2026-06-20.png`,
  and
  `hardware/schematic/annotated/stdrive101_phase_u_out1_gls1_q2_marked_2026-06-20.png`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-FAULT-REVIEW-SCHEMATIC-MARKING-001`.
- Decision:
  `STDRIVE101 fault review schematic marking / source image marked for CN8-CN3,
  LIN1, nFAULT, CP, SCREF, REG12, OUT1, GHS1, GLS1, Q2 low-side path, and
  GND domains / supports VDS-monitoring source review after LIN1 low-side
  command / no unknown-node probing / no repeat powered wake / no PWM-output
  validation / no powered-drive readiness`.
- Boundary:
  this is source-image marking only. It is not physical probe permission for
  unknown pads and does not authorize repeat powered wake, alternate input
  stimulus, firmware implementation, flash, Run / Debug, motor connection,
  Gate PWM, Motor Pilot, Motor Profiler, Hall closed loop, sensorless
  operation, power-stage readiness, or motor readiness.
- Next checkpoint:
  no power. Use the marked images to identify board areas only; if `SCREF`,
  `CP`, `REG12`, `OUT1`, `GLS1`, or Q2 terminals cannot be physically
  identified with certainty, request a clear board photo or EDA/netlist crop
  rather than probing by guesswork.

## 2026-06-20 STDRIVE101 nFAULT No-Power DMM Result Recorded

- Added the no-power DMM result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_nfault_no_power_dmm_result_2026-06-20.md`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-NFAULT-NO-POWER-DMM-RESULT-001`.
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
- Interpretation:
  the four CN3-side readings do not show a persistent rail hard short on
  `LIN1` or `nFAULT`. This reduces concern that the powered `nFAULT = 0 V`
  event was caused by a simple CN3-side short, but it does not prove the
  STDRIVE101 internal fault cause.
- Next boundary:
  remain no-power. Do not probe `SCREF`, `CP`, `REG12`, `OUT1`, `GLS1`, or
  MOSFET pins by guesswork. Next useful evidence is a marked source packet or
  confidently identified no-power protection-node checks.

## 2026-06-20 STDRIVE101 Single-Input Wake nFAULT Cause Review Added

- Added the no-power / source-review artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_single_input_wake_nfault_cause_review_2026-06-20.md`.
- Evidence:
  `EV-2026-06-20-STDRIVE101-SINGLE-INPUT-WAKE-NFAULT-CAUSE-REVIEW-001`.
- Decision:
  `STDRIVE101 single-input wake nFAULT cause review / REG12 wake observed but
  clean wake failed / primary review target VDS monitoring after LIN1 low-side
  command / secondary targets REG12 sequence or accidental external REG12 tie,
  CP comparator, thermal shutdown, external nFAULT pull-down / next step
  no-power DMM and source packet only / no repeat powered wake / no PWM-output
  validation / no powered-drive readiness`.
- Review result:
  VDS monitoring is the primary source-review target because `LIN1` high can
  command phase-1 low-side on after `REG12` rises, and a failure to pull
  `OUT1` near ground while low-side is commanded can fit the latched
  `nFAULT` pattern. This is an inference, not proof.
- Next user checkpoint:
  no power. Confirm `10k removed = yes`, `VS / 24V_FUSED < 1 V`, then record
  raw DMM results for `CN3_2-LIN1` to `3V3` / `GND` and
  `CN3_13-nFAULT` to `3V3` / `GND`, or provide a marked source packet for
  `SCREF`, `CP`, `REG12`, and `OUT1`.
- Boundary:
  this does not authorize a repeat powered wake diagnostic, alternate input
  stimulus, firmware implementation, flash, Run / Debug, motor connection,
  Gate PWM, Motor Pilot, Motor Profiler, Hall closed loop, sensorless
  operation, power-stage readiness, or motor readiness.

## 2026-06-19 STDRIVE101 Single-Input Wake Fault Result Recorded

- Added the bounded wake result record:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_reg12_single_input_wake_fault_result_2026-06-19.md`.
- Evidence:
  `EV-2026-06-19-STDRIVE101-SINGLE-INPUT-WAKE-FAULT-001`.
- User-reported raw readings:
  `wake_supply_state = CV`, `wake_supply_current_A = 0.046 A`,
  `wake_CN3_2_LIN1_V = 3 V`, `wake_CN3_13_nFAULT_V = 0 V`, and
  `wake_REG12_V = 12 V`.
- User-reported power-down follow-up:
  `post_off_VS_or_24V_FUSED_V = 0 V`.
- Decision:
  `STDRIVE101 REG12 single-input wake result / CN3_14 3V3 through 10 kohm to
  CN3_2 LIN1 / LIN1 3 V / HSPY CV 0.046 A / REG12 rose to 12 V / nFAULT 0 V
  stop-rule event / post-off VS reported 0 V / no retry before fault-cause
  review / no PWM-output validation / no powered-drive readiness`.
- Interpretation:
  the `10 kohm` stimulus reached `LIN1`, and `REG12` rose into the expected
  regulator range, but the diagnostic did not pass as a clean wake condition
  because `nFAULT` was low.
- Boundary:
  this result does not authorize another powered wake attempt, a different
  input stimulus, firmware implementation, flash, Run / Debug, motor
  connection, Gate PWM, Motor Pilot, Motor Profiler, Hall closed loop,
  sensorless operation, power-stage readiness, or motor readiness.
- Next boundary:
  keep HSPY output OFF, remove the `10 kohm` stimulus resistor if not already
  removed after confirming `VS / 24V_FUSED < 1 V`, and review STDRIVE101
  `nFAULT` causes and board conditions before any repeat diagnostic is
  proposed.

## 2026-06-19 Software Hall Code-Entry Boundary After DMM Added

- Added the no-power post-DMM code-entry boundary:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_code_entry_boundary_after_dmm_2026-06-19.md`.
- Evidence:
  `EV-2026-06-19-SOFTWARE-HALL-CODE-ENTRY-BOUNDARY-POST-DMM-001`.
- Decision:
  `Software Hall code-entry boundary after DMM summary /
  PA0-PA1-PB4 debug-only adapter planning allowed / no firmware
  implementation / no MCSDK hook / no Hall readiness`.
- Scope:
  records that the 2026-06-19 DMM summary stops the no-power DMM table from
  being the immediate planning blocker, then defines the next allowed
  document-side work: exact future file list, GPIO pull / EXTI trigger review,
  timestamp-source selection criteria, low-frequency debug snapshot route,
  no-power build checklist, and rollback checklist.
- Boundary:
  this is a no-power document-side boundary only. It does not create STM32
  firmware, edit generated MCSDK files, edit CubeMX / Workbench, flash, run
  hardware, apply 24 V, connect a motor, output Gate PWM, run Motor Pilot,
  run Motor Profiler, claim GPIO runtime proof, claim MCSDK hook readiness,
  claim Hall closed-loop behavior, claim power-stage readiness, claim motor
  readiness, or claim sensorless validation.

## 2026-06-19 PCB2 No-Power DMM Summary Result Recorded

- Added the user-reported no-power DMM continuity / short-check summary:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/pcb2_no_power_dmm_continuity_short_check_result_2026-06-19.md`.
- Evidence:
  `EV-2026-06-19-PCB2-NO-POWER-DMM-SUMMARY-001`.
- User-reported continuity rows:
  `CN3_10 / IA -> CN4-A0 / PA0`, `CN3_11 / IB -> CN4-A1 / PA1`,
  `CN3_12 / IC -> CN5-D5 / PB4`, `CN3_2 / LIN1 -> CN10-D12 / PB3`,
  `CN3_14 / 3V3 -> CN4-3V3`, `CN3_15 / GND -> CN4-GND`, and
  `CN3_13 / nFAULT -> CN10-D14 / PB12` are reported as `通`.
- User-reported short-check rows:
  `CN3_14 / 3V3` to `CN3_15 / GND`, `CN3_10 / IA`, `CN3_11 / IB`,
  `CN3_12 / IC`, `CN3_2 / LIN1`, and `CN3_13 / nFAULT` to the relevant
  `3V3` / `GND` rails, plus `IA-IB`, `IA-IC`, and `IB-IC`, are reported as
  `不通`.
- Decision:
  `PCB2 no-power DMM continuity / short-check summary / expected continuity
  reported for CN3_10-PA0, CN3_11-PA1, CN3_12-PB4, CN3_2-PB3, CN3_14-3V3,
  CN3_15-GND, and CN3_13-PB12 / no rail, signal-to-rail, or Hall-line hard
  short reported / raw ohm values not provided / no powered readiness`.
- Boundary:
  this is a no-power DMM summary only. It does not authorize firmware
  implementation, generated-code edits, CubeMX / Workbench edits, flash,
  Run / Debug, 24 V, power-board connection, motor connection, Gate PWM,
  Motor Pilot, Motor Profiler, Hall closed loop, sensorless operation,
  power-stage readiness, or motor readiness.
- Next boundary:
  the immediate DMM-table blocker is no longer the next step for no-power
  planning. The next allowed project step is a no-power software Hall adapter
  interface / code-entry boundary review for `PA0 / PA1 / PB4`.

## 2026-06-19 STDRIVE101 Single-Input Wake Baseline Recorded

- Added the bounded pre-stimulus baseline result:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_reg12_single_input_wake_baseline_result_2026-06-19.md`.
- Evidence:
  `EV-2026-06-19-STDRIVE101-SINGLE-INPUT-WAKE-BASELINE-001`.
- Decision:
  `STDRIVE101 REG12 single-input wake baseline / HSPY 24 V 0.2 A CV /
  0.036 A static current / VS 24 V / CN3_14 3.3 V present with USB-STLINK
  unplugged / nFAULT 3.3 V / REG12 0.33 V / pre-stimulus baseline satisfied
  only / no wake stimulus installed / no PWM-output validation / no powered-drive
  readiness`.
- User-reported raw readings:
  `CV`, `0.036 A`, `VS / 24V_FUSED = 24 V`,
  `CN3_14 / 3V3 = 3.3 V`, `CN3_13 / nFAULT = 3.3 V`, and
  `REG12 = 0.33 V`.
- Boundary:
  this is a static baseline only. It does not install the `10 kohm` stimulus,
  drive `CN3_2 / LIN1` high, execute the wake diagnostic, validate Gate PWM,
  validate Hall closed-loop behavior, validate sensorless behavior, or prove
  power-stage / motor readiness.
- Next boundary:
  if the user wants to keep progressing without installing the `10 kohm`
  resistor, stop at this recorded evidence and continue non-hardware planning
  or review. If the user later chooses to execute the wake diagnostic, the
  next step remains `CN3_14 / 3V3 -> 10 kohm -> CN3_2 / LIN1` with motor
  disconnected, HSPY `24 V / 0.2 A`, strict CV/CC stop rules, and no direct
  wire.

## 2026-06-19 STDRIVE101 Single-Input Wake Handoff Route Added

- Added the hardware phrase handoff task:
  `TASK-2026-06-19-stdrive101-single-input-wake-handoff`.
- Evidence:
  `EV-2026-06-19-STDRIVE101-SINGLE-INPUT-WAKE-HANDOFF-001`.
- Decision:
  `STDRIVE101 single-input wake phrase route / qiansai root AGENTS bridge /
  project Skill no-power route / no hardware execution`.
- Scope:
  added a root-level `AGENTS.md` in the outer `qiansai` workspace so a new
  Codex session starting outside the Git repo routes STM32G474 FOC work to
  `foc_learning_repo/`. Updated `AI_CONTEXT.md`,
  `workflow/CURRENT_SNAPSHOT.md`, `workflow/ACTIVE_TASK.md`, repo
  `AGENTS.md`, and the project Skill no-power boundary so the phrase
  `开始单输入唤醒诊断` means the STDRIVE101 `CN3_2 / LIN1` single-input wake
  diagnostic, not Codex mobile wakeup, CodexMobileWeb, service wakeup, or
  automation wakeup.
- Required context before giving the future checklist:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_reg12_single_input_wake_plan_2026-06-19.md`,
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_reg12_wake_official_web_review_2026-06-19.md`,
  and
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/out1_output_node_no_power_short_check_result_2026-06-19.md`.
- Candidate diagnostic remains:
  `CN3_14 / 3V3 -> 10 kohm series resistor -> CN3_2 / LIN1`, motor
  disconnected, HSPY `24 V / 0.2 A`, no firmware PWM, no Motor Pilot, and no
  Motor Profiler.
- Installed the updated project Skill to
  `C:\Users\gregrg\.codex\skills\stm32g474-foc-assistant`.
- Boundary:
  this is handoff and routing evidence only. It does not execute the wake
  diagnostic, inspect hardware, change firmware, connect a motor, start PWM,
  run Motor Pilot, run Motor Profiler, claim Hall closed-loop, claim
  sensorless operation, or claim power-stage / motor readiness.

## 2026-06-17 AI Maintenance Audit Readability Status Added

- Added the no-power repository maintenance task:
  `TASK-2026-06-17-ai-maintenance-audit-readability-status`.
- Evidence:
  `EV-2026-06-17-AI-MAINTENANCE-AUDIT-READABILITY-STATUS-001`.
- Decision:
  `AI maintenance audit readability status / entry-header versus legacy-debt handoff / no hardware or firmware action`.
- Extended `tools/run_ai_maintenance_audit.py` with
  `readability_status_from_repo()`, `readability_header_status_from_repo()`,
  and `readability_legacy_debt_status_from_repo()`.
- The no-power audit now exposes top-level `readability_status`, including
  `entry_headers_ok`, `guarded_entry_files`, `legacy_debt_present`,
  `legacy_debt_count`, `legacy_debt_paths`, `full_legacy_cleanup_claimed`, and
  `hardware_validation: false`.
- Updated `tools/check_ai_contracts.py`, `tools/search_local_v2.py`,
  `retrieval_eval/queries.json`, `tests/test_ai_architecture_contracts.py`,
  `AI_CONTEXT.md`, `workflow/CURRENT_SNAPSHOT.md`,
  `docs/00_project_truth/ai_architecture.md`, `docs/file_map.md`,
  `tools/README.md`, the project Skill workflow-maintenance reference,
  `workflow/ACTIVE_TASK.md`, and `workflow/evidence_register.md`.
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
- This adds audit visibility only. It does not claim full historical mojibake
  cleanup, clean worktree, DMM continuity, firmware readiness, powered
  readiness, motor readiness, Hall readiness, power-stage readiness, or
  sensorless validation.
- Safety boundary unchanged: no DMM table fill, no firmware implementation, no
  generated-code edit, no CubeMX/MCSDK edit, no flash, no 24V, no power-board
  connection, no motor connection, no Gate PWM, no Motor Profiler, no Hall
  closed-loop, and no sensorless / SMO claim.

## 2026-06-17 Three-Hour Optimization Sprint Implemented

- Added the no-power repository maintenance task:
  `TASK-2026-06-17-three-hour-optimization-sprint`.
- Evidence:
  `EV-2026-06-17-THREE-HOUR-OPTIMIZATION-SPRINT-001`.
- Decision:
  `Three-hour optimization sprint / subagent protocol / Obsidian Chinese learning notes / retrieval maintainability / no hardware or firmware action`.
- Implemented a structured optimization sprint using subagent discovery and
  bounded implementation slices. All subagent outputs were filtered into
  summaries before main-agent integration.
- Architecture:
  added the subagent communication protocol, hierarchical task decomposition,
  context filtering, summary gate, and before/after comparison in
  `docs/00_project_truth/ai_architecture.md`.
- Obsidian:
  added Chinese-first learning tags, concept/glossary/review templates, sample
  learning cards, cross-linking strategy, Dataview queries, and retrieval
  checks under `notes/10_learning/` and `notes/99_templates/`.
- Project optimization:
  finished a focused maintainability refactor in `tools/search_local_v2.py`
  by moving path-specific phrase boosts into configured rules, with regression
  coverage in `tests/test_search_local_v2.py`.
- Report:
  `workflow/three_hour_optimization_report_2026-06-17.md` records the timebox,
  subagent roles, timestamped progress log, mid-project review, completed
  components, retrieval checks, verification plan, and efficiency
  recommendations.
- Boundary:
  repo-maintenance documentation, notes, retrieval, and tests only. This does
  not change firmware, generated code, CubeMX/MCSDK config, hardware
  parameters, DMM results, or powered-test evidence.
- Safety boundary unchanged: no DMM table fill, no firmware implementation, no
  generated-code edit, no CubeMX/MCSDK edit, no flash, no 24V, no power-board
  connection, no motor connection, no Gate PWM, no Motor Profiler, no Hall
  closed-loop, and no sensorless / SMO claim.

## 2026-06-17 AI Architecture Subagent Protocol Added

- Added the no-power repository maintenance task:
  `TASK-2026-06-17-ai-architecture-subagent-protocol`.
- Evidence:
  `EV-2026-06-17-AI-ARCHITECTURE-SUBAGENT-PROTOCOL-001`.
- Decision:
  `AI architecture subagent protocol / hierarchical task decomposition / context filtering / summarized handoff / no hardware or firmware action`.
- Updated `docs/00_project_truth/ai_architecture.md` with a structured
  subagent communication protocol, hierarchical task decomposition, context
  filtering rules, a summary gate, and a before/after comparison of old flat
  handoff versus the new filtered hierarchy.
- Mirrored the architecture update in `workflow/CURRENT_SNAPSHOT.md` and
  `workflow/ACTIVE_TASK.md` so low-token handoff keeps the new protocol visible.
- Boundary:
  this is repo-maintenance documentation only. It does not change firmware,
  generated code, CubeMX/MCSDK config, hardware parameters, DMM results, or
  powered-test evidence.
- Safety boundary unchanged: no DMM table fill, no firmware implementation, no
  generated-code edit, no CubeMX/MCSDK edit, no flash, no 24V, no power-board
  connection, no motor connection, no Gate PWM, no Motor Profiler, no Hall
  closed-loop, and no sensorless / SMO claim.

## 2026-06-10 Entry Readability Contract Added

- Added the no-power repository maintenance task:
  `TASK-2026-06-10-entry-readability-contract`.
- Evidence:
  `EV-2026-06-10-ENTRY-READABILITY-CONTRACT-001`.
- Decision:
  `High-value entry readability repair / UTF-8 header contract / no hardware or firmware action`.
- Restored the readable entry header and weekly/phase template fields in
  `deliverables/submission_checklist.md`.
- Restored the title and evidence boundary in
  `workflow/evidence_register.md`.
- Extended `tools/check_ai_contracts.py` with
  `READABILITY_HEADER_REQUIREMENTS`, `READABILITY_MOJIBAKE_MARKERS`, and
  `check_readability_headers()`.
- Added unit coverage, retrieval expansion/eval, low-token handoff updates,
  architecture/index/tool docs, project Skill workflow-maintenance guidance,
  active task, and evidence record.
- Verification passed:
  `python -m py_compile tools\check_ai_contracts.py tools\search_local_v2.py`;
  `python -m unittest tests.test_ai_architecture_contracts`;
  `python tools/check_ai_contracts.py` with 0 errors and the two known
  review-lifecycle warnings;
  `python -X utf8 C:\Users\gregrg\.codex\skills\.system\skill-creator\scripts\quick_validate.py codex_skills/stm32g474-foc-assistant`;
  `python tools/check_project_skill_install.py --repo-only --json`;
  `powershell -ExecutionPolicy Bypass -File .\tools\install_project_skill.ps1`;
  `python tools/check_project_skill_install.py`;
  `python tools/build_vector_store.py`;
  `python tools/search_local_v2.py --eval`;
  `python -m unittest tests.test_search_local_v2 tests.test_ai_architecture_contracts tests.test_workflow_contracts`;
  and `python tools/run_ai_maintenance_audit.py --json --max-output-chars 700`.
  The full audit passed with 143 discovered tests, retrieval eval, compileall,
  Skill install drift check, `closeout_summary.repo_maintenance_closeout_ok:
  true`, and `git diff --check`; diff check output only contained existing
  CRLF conversion warnings.
- This repairs and guards the high-value entry headers only. It does not claim
  that every legacy historical mojibake row is repaired.
- Safety boundary unchanged: no DMM table fill, no firmware implementation, no
  generated-code edit, no CubeMX/MCSDK edit, no flash, no 24V, no power-board
  connection, no motor connection, no Gate PWM, no Motor Profiler, no Hall
  closed-loop, and no sensorless / SMO claim.

## 2026-06-10 AI Maintenance Audit Closeout Summary Added

- Added the no-power repository maintenance task:
  `TASK-2026-06-10-ai-maintenance-audit-closeout-summary`.
- Evidence:
  `EV-2026-06-10-AI-MAINTENANCE-AUDIT-CLOSEOUT-SUMMARY-001`.
- Decision:
  `AI maintenance audit closeout summary / top-level repo-maintenance handoff / no hardware or firmware action`.
- Extended `tools/run_ai_maintenance_audit.py` with
  `closeout_summary_from_statuses()` and top-level `closeout_summary`.
- The summary reports `repo_maintenance_closeout_ok`, `strict_ready`,
  `needs_user_review`, dirty-worktree state, dirty entry count, next review
  group/focus, `no_power_boundary_active`, and `hardware_validation: false`.
- Markdown audit reports now include a `Closeout Summary` section.
- Updated tests, contract checks, retrieval expansion, retrieval eval,
  low-token handoff docs, file index, tools README, project Skill
  workflow-maintenance reference, active task, and evidence register.
- Verification passed:
  `python -m py_compile tools\run_ai_maintenance_audit.py tools\check_ai_contracts.py tools\search_local_v2.py`;
  `python -m unittest tests.test_ai_architecture_contracts`;
  `python tools/check_ai_contracts.py` with 0 errors and the two known
  review-lifecycle warnings;
  `python -X utf8 C:\Users\gregrg\.codex\skills\.system\skill-creator\scripts\quick_validate.py codex_skills\stm32g474-foc-assistant`;
  `python tools/check_project_skill_install.py --repo-only --json`;
  `powershell -ExecutionPolicy Bypass -File .\tools\install_project_skill.ps1`;
  `python tools/check_project_skill_install.py`;
  `python tools/build_context_pack.py --mode workflow_maintenance --max-chars 350`;
  `python tools/build_vector_store.py`;
  `python tools/search_local_v2.py --eval`;
  `python -m unittest tests.test_search_local_v2 tests.test_ai_architecture_contracts`;
  and `python tools/run_ai_maintenance_audit.py --json --max-output-chars 700`.
  The full audit passed with `closeout_summary.repo_maintenance_closeout_ok:
  true`, `strict_ready: false`, `needs_user_review: true`, 0 contract errors,
  0 unexpected warnings, 2 known review-lifecycle warnings, 142 discovered unit
  tests, compileall, Skill install drift check, retrieval eval, and
  `git diff --check`; diff check output only contained existing CRLF
  conversion warnings.
- This does not install external GitHub Skills and does not mark the earlier
  `done + Review Required` task as `reviewed`.
- Safety boundary unchanged: no DMM table fill, no firmware implementation, no
  generated-code edit, no CubeMX/MCSDK edit, no flash, no 24V, no power-board
  connection, no motor connection, no Gate PWM, no Motor Profiler, no Hall
  closed-loop, and no sensorless / SMO claim.

## 2026-06-10 AI Maintenance Audit Contract Status Added

- Added the no-power repository maintenance task:
  `TASK-2026-06-10-ai-maintenance-audit-contract-status`.
- Evidence:
  `EV-2026-06-10-AI-MAINTENANCE-AUDIT-CONTRACT-STATUS-001`.
- Decision:
  `AI maintenance audit contract status / review-lifecycle warning classification / no hardware or firmware action`.
- Extended `tools/run_ai_maintenance_audit.py` with
  `REVIEW_LIFECYCLE_WARNING_MARKERS`, `parse_contract_output()`, and
  `contract_status_from_results()`.
- The no-power audit now exposes top-level `contract_status`, including
  contract error count, warning count, review-lifecycle warning count,
  unexpected warning count, `strict_ready`, `implementation_closeout_ok`, and
  the parsed warning lists.
- The current expected result is no contract errors, two review-lifecycle
  warnings, no unexpected warnings, implementation closeout allowed, and strict
  readiness still false until user review clears the old `done + Review
  Required` lifecycle state.
- Markdown audit reports now include a `Contract Status` section and a
  `Review Lifecycle Warnings` subsection.
- Added `MAINTENANCE_SOURCE_FILES` in `tools/build_vector_store.py` so
  maintenance tool scripts, tests, and eval JSON stay indexed for local
  retrieval.
- Updated `tools/search_local_v2.py` with path-aware topic-entry scoring so
  workflow entry files and the `tools/check_ai_contracts.py`
  dangerous-claim implementation remain discoverable after status/evidence
  docs grow.
- Updated tests, retrieval expansion, retrieval eval, low-token handoff docs,
  file index, tools README, project Skill workflow-maintenance reference,
  active task, and evidence register.
- Verification passed:
  `python tools/build_context_pack.py --mode workflow_maintenance --max-chars 350`;
  `python tools/check_ai_contracts.py` with 0 errors and the two known
  review-lifecycle warnings;
  `python tools/check_project_skill_install.py`;
  `python tools/build_vector_store.py`;
  `python tools/search_local_v2.py --eval`;
  `python -m unittest tests.test_search_local_v2 tests.test_ai_architecture_contracts`
  with 18 tests OK;
  and `python tools/run_ai_maintenance_audit.py --json --max-output-chars 700`,
  which passed retrieval eval, 142 discovered unit tests, compileall, Skill
  install drift check, and `git diff --check`. Diff check output only contained
  existing CRLF conversion warnings.
- This does not install external GitHub Skills and does not mark the earlier
  `done + Review Required` task as `reviewed`.
- Safety boundary unchanged: no DMM table fill, no firmware implementation, no
  generated-code edit, no CubeMX/MCSDK edit, no flash, no 24V, no power-board
  connection, no motor connection, no Gate PWM, no Motor Profiler, no Hall
  closed-loop, and no sensorless / SMO claim.

## 2026-06-09 Dangerous Claim Scan Surface Added

- Added the no-power repository maintenance task:
  `TASK-2026-06-09-ai-contract-dangerous-claim-scan-surface`.
- Evidence:
  `EV-2026-06-09-AI-CONTRACT-DANGEROUS-CLAIM-SCAN-SURFACE-001`.
- Decision:
  `AI contract dangerous claim scan surface / broader no-power static text scan / no hardware or firmware action`.
- Extended `tools/check_ai_contracts.py` with
  `DANGEROUS_CLAIM_SCAN_PATHS`, `DANGEROUS_CLAIM_SCAN_SUFFIXES`,
  `is_dangerous_claim_scan_candidate()`, and
  `iter_dangerous_claim_scan_files()`.
- The dangerous positive hardware claim scan now covers project truth,
  workflow, project Skill, no-power precheck, deliverable, interface, and
  learning text. It intentionally does not scan tool constants in
  `tools/check_ai_contracts.py` itself.
- Added unit coverage that confirms `CURRENT_STATUS.md`,
  `workflow/ACTIVE_TASK.md`, `docs/00_project_truth/ai_architecture.md`, and
  the project Skill workflow-maintenance reference are in the scan surface,
  while `tools/check_ai_contracts.py` is excluded from the claim-text surface.
- Added the `dangerous_claim_scan_surface` retrieval eval case and search
  expansion for dangerous positive hardware claim questions.
- Updated low-token handoff docs, file index, tools README, project Skill
  workflow-maintenance reference, active task, and evidence register.
- Verification passed:
  `python tools/check_ai_contracts.py` with no errors and only the known
  `ACTIVE_TASK.md` review-lifecycle warnings;
  targeted dangerous-claim-scan tests in
  `tests/test_ai_architecture_contracts.py`;
  `python tools/build_vector_store.py`;
  `python -m json.tool retrieval_eval\queries.json`;
  targeted `rg` dangerous-phrase sweep returned no matches in the scanned
  project-truth/workflow/Skill/precheck surface;
  `python tools/search_local_v2.py --eval`;
  `python -X utf8 C:\Users\gregrg\.codex\skills\.system\skill-creator\scripts\quick_validate.py codex_skills\stm32g474-foc-assistant`;
  `python tools/check_project_skill_install.py --repo-only --json`;
  `powershell -ExecutionPolicy Bypass -File .\tools\install_project_skill.ps1`;
  `python tools/check_project_skill_install.py`;
  `python tools/build_context_pack.py --mode workflow_maintenance --max-chars 350`;
  and `python tools/run_ai_maintenance_audit.py --json --max-output-chars 700`.
- This does not install external GitHub Skills and does not mark the earlier
  `done + Review Required` task as `reviewed`.
- Safety boundary unchanged: no DMM table fill, no firmware implementation, no
  generated-code edit, no CubeMX/MCSDK edit, no flash, no 24V, no power-board
  connection, no motor connection, no Gate PWM, no Motor Profiler, no Hall
  closed-loop, and no sensorless / SMO claim.

## 2026-06-09 AI Maintenance Audit Handoff Review Queue Added

- Added the no-power repository maintenance task:
  `TASK-2026-06-09-ai-maintenance-audit-handoff-review-queue`.
- Evidence:
  `EV-2026-06-09-AI-MAINTENANCE-AUDIT-HANDOFF-REVIEW-QUEUE-001`.
- Decision:
  `AI maintenance audit handoff review queue / group-specific dirty-worktree review focus / no hardware or firmware action`.
- Extended `tools/run_ai_maintenance_audit.py` with `GROUP_REVIEW_FOCUS` and
  `build_handoff_review_queue()`, deriving
  `workspace_status.handoff_review_queue` from existing `path_groups` and
  ordered `focus_groups`.
- The handoff review queue gives each dirty-worktree group a stable review
  focus, for example AI maintenance scripts/tests/contracts, workflow status
  and evidence, project Skill source/install drift, no-power precheck files,
  project truth docs, learning memory, interfaces, and personal notes.
- Updated Markdown report output with a `Handoff Review Queue` subsection under
  `Workspace Status`.
- Added unit assertions for `handoff_review_queue`,
  `build_handoff_review_queue`, `GROUP_REVIEW_FOCUS`, and Markdown
  `Handoff Review Queue` output.
- Updated AI/workflow maintenance contracts, retrieval expansion, retrieval
  eval, low-token handoff docs, file index, tools README, project Skill
  workflow-maintenance reference, current snapshot, active task, and evidence
  register so handoff review guidance remains discoverable.
- Verification passed:
  `python tools/run_ai_maintenance_audit.py --check git_status --json --max-output-chars 1`;
  targeted audit tests in `tests/test_ai_architecture_contracts.py`;
  `python tools/check_ai_contracts.py` with no errors and only the known
  `ACTIVE_TASK.md` review-lifecycle warnings;
  `python -X utf8 C:\Users\gregrg\.codex\skills\.system\skill-creator\scripts\quick_validate.py codex_skills\stm32g474-foc-assistant`;
  `python tools/check_project_skill_install.py --repo-only --json`;
  `powershell -ExecutionPolicy Bypass -File .\tools\install_project_skill.ps1`;
  `python tools/check_project_skill_install.py`;
  `python tools/build_context_pack.py --mode workflow_maintenance --max-chars 350`;
  and `python tools/run_ai_maintenance_audit.py --json --max-output-chars 700`.
- This does not install external GitHub Skills and does not mark the earlier
  `done + Review Required` task as `reviewed`.
- Safety boundary unchanged: no DMM table fill, no firmware implementation, no
  generated-code edit, no CubeMX/MCSDK edit, no flash, no 24V, no power-board
  connection, no motor connection, no Gate PWM, no Motor Profiler, no Hall
  closed-loop, and no sensorless / SMO claim.

## 2026-06-09 AI Maintenance Audit Focus Groups Added

- Added the no-power repository maintenance task:
  `TASK-2026-06-09-ai-maintenance-audit-focus-groups`.
- Evidence:
  `EV-2026-06-09-AI-MAINTENANCE-AUDIT-FOCUS-GROUPS-001`.
- Decision:
  `AI maintenance audit focus groups / ordered dirty-worktree handoff / no hardware or firmware action`.
- Extended `tools/run_ai_maintenance_audit.py` with `GROUP_FOCUS_ORDER` and
  `summarize_focus_groups()`, deriving an ordered `workspace_status.focus_groups`
  list from existing `path_groups`.
- The ordered focus list prioritizes AI maintenance, workflow/status, project
  Skill, no-power precheck, project truth docs, learning memory, interfaces,
  personal notes/Obsidian, then `other`. This helps future Codex inspect dirty
  scope in a stable order.
- Updated Markdown report output with a `Focus Groups` subsection under
  `Workspace Status`, showing per-focus-group counts.
- Added unit assertions for `focus_groups`, `summarize_focus_groups`, and
  Markdown `Focus Groups` output.
- Updated AI/workflow maintenance contracts, retrieval expansion, retrieval
  eval, low-token handoff docs, file index, tools README, project Skill
  workflow-maintenance reference, current snapshot, active task, and evidence
  register so ordered focus groups remain discoverable.
- Reinstalled the validated repo-local project Skill after updating
  `references/workflow-maintenance.md`; final installed Skill drift check is
  OK.
- Verification passed:
  `python tools/run_ai_maintenance_audit.py --quick --repo-only-skill --json --max-output-chars 1`;
  `python tools/check_project_skill_install.py`;
  `python tools/run_ai_maintenance_audit.py --json --max-output-chars 700`;
  `python tools/check_ai_contracts.py` with no errors and only the known
  `ACTIVE_TASK.md` review-lifecycle warnings;
  `python tools/build_vector_store.py`;
  `python tools/search_local_v2.py --eval`;
  `python -m unittest discover -s tests`;
  `python -m compileall src tests`;
  `git status --short`;
  `git diff --check` reported CRLF conversion warnings only.
- This does not install external GitHub Skills and does not mark the earlier
  `done + Review Required` task as `reviewed`.
- Safety boundary unchanged: no DMM table fill, no firmware implementation, no
  generated-code edit, no CubeMX/MCSDK edit, no flash, no 24V, no power-board
  connection, no motor connection, no Gate PWM, no Motor Profiler, no Hall
  closed-loop, and no sensorless / SMO claim.

## 2026-06-09 AI Maintenance Audit Status Paths Added

- Added the no-power repository maintenance task:
  `TASK-2026-06-09-ai-maintenance-audit-status-paths`.
- Evidence:
  `EV-2026-06-09-AI-MAINTENANCE-AUDIT-STATUS-PATHS-001`.
- Decision:
  `AI maintenance audit status paths / status-code dirty-worktree handoff / no hardware or firmware action`.
- Extended `tools/run_ai_maintenance_audit.py` with `summarize_status_paths()`
  and `workspace_status.status_paths`, mapping each `git status --short`
  status code to the matching path list.
- This makes modified and untracked files directly accessible through the
  audit JSON, for example `workspace_status.status_paths[" M"]` and
  `workspace_status.status_paths["??"]`, without reparsing `items` or raw text.
- Updated Markdown report output with a `Status Paths` subsection under
  `Workspace Status`, showing per-status counts for handoff.
- Added unit assertions for `status_paths`, `summarize_status_paths`, and
  Markdown `Status Paths` output.
- Updated AI/workflow maintenance contracts, retrieval expansion, retrieval
  eval, low-token handoff docs, file index, tools README, project Skill
  workflow-maintenance reference, current snapshot, active task, and evidence
  register so status-code path lists remain discoverable.
- Reinstalled the validated repo-local project Skill after updating
  `references/workflow-maintenance.md`; final installed Skill drift check is
  OK.
- Verification passed:
  `python tools/run_ai_maintenance_audit.py --quick --repo-only-skill --json --max-output-chars 1`;
  `python tools/check_project_skill_install.py`;
  `python tools/run_ai_maintenance_audit.py --json --max-output-chars 700`;
  `python tools/check_ai_contracts.py` with no errors and only the known
  `ACTIVE_TASK.md` review-lifecycle warnings;
  `python tools/build_vector_store.py`;
  `python tools/search_local_v2.py --eval`;
  `python -m unittest discover -s tests`;
  `python -m compileall src tests`;
  `git status --short`;
  `git diff --check` reported CRLF conversion warnings only.
- This does not install external GitHub Skills and does not mark the earlier
  `done + Review Required` task as `reviewed`.
- Safety boundary unchanged: no DMM table fill, no firmware implementation, no
  generated-code edit, no CubeMX/MCSDK edit, no flash, no 24V, no power-board
  connection, no motor connection, no Gate PWM, no Motor Profiler, no Hall
  closed-loop, and no sensorless / SMO claim.

## 2026-06-09 AI Maintenance Audit Workspace Path Groups Added

- Added the no-power repository maintenance task:
  `TASK-2026-06-09-ai-maintenance-audit-workspace-path-groups`.
- Evidence:
  `EV-2026-06-09-AI-MAINTENANCE-AUDIT-WORKSPACE-PATH-GROUPS-001`.
- Decision:
  `AI maintenance audit workspace path groups / repository-area dirty-worktree handoff / no hardware or firmware action`.
- Extended `tools/run_ai_maintenance_audit.py` with
  `classify_path_group()` and `path_groups` inside the top-level
  `workspace_status` object.
- Path groups currently classify dirty paths into stable repository areas such
  as `ai_maintenance`, `project_skill`, `workflow_status`,
  `project_truth_docs`, `learning_memory`, `no_power_precheck`,
  `personal_notes_or_obsidian`, `interfaces`, and `other`.
- Updated Markdown report output with a `Path Groups` subsection under
  `Workspace Status`, showing per-group counts for handoff.
- Added unit assertions for `path_groups`, `classify_path_group`, and Markdown
  `Path Groups` output.
- Updated AI/workflow maintenance contracts, retrieval expansion, retrieval
  eval, low-token handoff docs, file index, tools README, project Skill
  workflow-maintenance reference, current snapshot, active task, and evidence
  register so path grouping remains discoverable.
- Reinstalled the validated repo-local project Skill after updating
  `references/workflow-maintenance.md`; final installed Skill drift check is
  OK.
- Verification passed:
  `python tools/run_ai_maintenance_audit.py --quick --repo-only-skill --json --max-output-chars 1`;
  `python tools/check_project_skill_install.py`;
  `python tools/run_ai_maintenance_audit.py --json --max-output-chars 700`;
  `python tools/check_ai_contracts.py` with no errors and only the known
  `ACTIVE_TASK.md` review-lifecycle warnings;
  `python tools/build_vector_store.py`;
  `python tools/search_local_v2.py --eval`;
  `python -m unittest discover -s tests`;
  `python -m compileall src tests`;
  `git status --short`;
  `git diff --check` reported CRLF conversion warnings only.
- This does not install external GitHub Skills and does not mark the earlier
  `done + Review Required` task as `reviewed`.
- Safety boundary unchanged: no DMM table fill, no firmware implementation, no
  generated-code edit, no CubeMX/MCSDK edit, no flash, no 24V, no power-board
  connection, no motor connection, no Gate PWM, no Motor Profiler, no Hall
  closed-loop, and no sensorless / SMO claim.

## 2026-06-09 AI Maintenance Audit Workspace Status Summary Added

- Added the no-power repository maintenance task:
  `TASK-2026-06-09-ai-maintenance-audit-workspace-status-summary`.
- Evidence:
  `EV-2026-06-09-AI-MAINTENANCE-AUDIT-WORKSPACE-STATUS-SUMMARY-001`.
- Decision:
  `AI maintenance audit workspace-status summary / machine-readable dirty-worktree handoff / no hardware or firmware action`.
- Extended `tools/run_ai_maintenance_audit.py` with
  `parse_git_status_short()` and a top-level `workspace_status` object derived
  from the existing full `git_status` output.
- The summary records whether the worktree is dirty, total `git status
  --short` entries, status-code counts, paths, and per-entry
  `{status, path}` items. It does not run extra git commands and does not
  change audit pass/fail semantics.
- Updated Markdown report output with a `Workspace Status` section that
  displays dirty state, total entries, and status counts.
- Added unit assertions for `workspace_status`, `status_counts`, paths/items,
  and the Markdown `Workspace Status` section.
- Updated AI/workflow maintenance contracts, retrieval expansion, retrieval
  eval, low-token handoff docs, file index, tools README, project Skill
  workflow-maintenance reference, current snapshot, active task, and evidence
  register so the parsed summary remains discoverable.
- Reinstalled the validated repo-local project Skill after updating
  `references/workflow-maintenance.md`; final installed Skill drift check is
  OK.
- Verification passed:
  `python tools/run_ai_maintenance_audit.py --quick --repo-only-skill --json --max-output-chars 1`;
  `python tools/check_project_skill_install.py`;
  `python tools/run_ai_maintenance_audit.py --json --max-output-chars 700`;
  `python tools/check_ai_contracts.py` with no errors and only the known
  `ACTIVE_TASK.md` review-lifecycle warnings;
  `python tools/build_vector_store.py`;
  `python tools/search_local_v2.py --eval`;
  `python -m unittest discover -s tests`;
  `python -m compileall src tests`;
  `git status --short`;
  `git diff --check` reported CRLF conversion warnings only.
- This does not install external GitHub Skills and does not mark the earlier
  `done + Review Required` task as `reviewed`.
- Safety boundary unchanged: no DMM table fill, no firmware implementation, no
  generated-code edit, no CubeMX/MCSDK edit, no flash, no 24V, no power-board
  connection, no motor connection, no Gate PWM, no Motor Profiler, no Hall
  closed-loop, and no sensorless / SMO claim.

## 2026-06-09 AI Maintenance Audit Preserves Full Git Status Output

- Added the no-power repository maintenance task:
  `TASK-2026-06-09-ai-maintenance-audit-preserve-git-status-output`.
- Evidence:
  `EV-2026-06-09-AI-MAINTENANCE-AUDIT-PRESERVE-GIT-STATUS-OUTPUT-001`.
- Decision:
  `AI maintenance audit full git-status output / dirty-worktree handoff evidence not truncated / no hardware or firmware action`.
- Extended `tools/run_ai_maintenance_audit.py` so each audit step has an
  output policy. Normal steps remain `tail` and obey `--max-output-chars`;
  `git_status` is marked `preserve_output=True` and reports
  `output_policy: full`.
- Added a regression test that runs
  `python tools/run_ai_maintenance_audit.py --check git_status --json --max-output-chars 1`
  and compares the audit JSON output with raw `git status --short`, proving
  the dirty-worktree handoff evidence is not truncated by the one-character
  limit.
- Updated AI/workflow maintenance contracts, unit tests, retrieval expansion,
  retrieval eval, low-token handoff docs, file index, tools README, project
  Skill workflow-maintenance reference, current snapshot, active task, and
  evidence register so the full-output policy remains discoverable.
- Reinstalled the validated repo-local project Skill after updating
  `references/workflow-maintenance.md`; final installed Skill drift check is
  OK.
- Verification passed:
  `python tools/run_ai_maintenance_audit.py --quick --repo-only-skill --json --max-output-chars 1`;
  `python tools/check_project_skill_install.py`;
  `python tools/run_ai_maintenance_audit.py --json --max-output-chars 700`;
  `python tools/check_ai_contracts.py` with no errors and only the known
  `ACTIVE_TASK.md` review-lifecycle warnings;
  `python tools/build_vector_store.py`;
  `python tools/search_local_v2.py --eval`;
  `python -m unittest discover -s tests`;
  `python -m compileall src tests`;
  `git status --short`;
  `git diff --check` reported CRLF conversion warnings only.
- This does not install external GitHub Skills and does not mark the earlier
  `done + Review Required` task as `reviewed`.
- Safety boundary unchanged: no DMM table fill, no firmware implementation, no
  generated-code edit, no CubeMX/MCSDK edit, no flash, no 24V, no power-board
  connection, no motor connection, no Gate PWM, no Motor Profiler, no Hall
  closed-loop, and no sensorless / SMO claim.

## 2026-06-08 AI Maintenance Audit Git Status Step Added

- Added the no-power repository maintenance task:
  `TASK-2026-06-08-ai-maintenance-audit-git-status-step`.
- Evidence:
  `EV-2026-06-08-AI-MAINTENANCE-AUDIT-GIT-STATUS-001`.
- Decision:
  `AI maintenance audit git-status step / dirty-worktree handoff evidence / no hardware or firmware action`.
- Extended `tools/run_ai_maintenance_audit.py` with a read-only `git_status`
  step that runs `git status --short`.
- The full audit now records `git_status` after compileall and before
  `git diff --check`. The quick repo-only audit now records
  `git_status` after project Skill, context-pack, and AI-contract checks.
- The audit records current dirty-worktree scope for Codex handoff only. It
  does not clean, reorder, revert, stage, commit, or validate the worktree.
- Updated AI/workflow maintenance contracts, unit tests, retrieval expansion,
  retrieval eval, low-token handoff docs, file index, tools README, project
  Skill workflow-maintenance reference, current snapshot, active task, and
  evidence register so the git-status audit step remains discoverable.
- Reinstalled the validated repo-local project Skill after updating
  `references/workflow-maintenance.md`; final installed Skill drift check is
  OK.
- Verification passed:
  `python tools/run_ai_maintenance_audit.py --quick --repo-only-skill --json --max-output-chars 300`;
  `python tools/check_project_skill_install.py`;
  `python tools/run_ai_maintenance_audit.py --json --max-output-chars 700`;
  `python tools/check_ai_contracts.py` with no errors and only the known
  `ACTIVE_TASK.md` review-lifecycle warnings;
  `python tools/build_vector_store.py`;
  `python tools/search_local_v2.py --eval`;
  `python -m unittest discover -s tests`;
  `python -m compileall src tests`;
  `git status --short`;
  `git diff --check` reported CRLF conversion warnings only.
- This does not install external GitHub Skills and does not mark the earlier
  `done + Review Required` task as `reviewed`.
- Safety boundary unchanged: no DMM table fill, no firmware implementation, no
  generated-code edit, no CubeMX/MCSDK edit, no flash, no 24V, no power-board
  connection, no motor connection, no Gate PWM, no Motor Profiler, no Hall
  closed-loop, and no sensorless / SMO claim.

## 2026-06-08 AI Maintenance Audit Markdown Report Output Added

- Added the no-power repository maintenance task:
  `TASK-2026-06-08-ai-maintenance-audit-markdown-report`.
- Evidence:
  `EV-2026-06-08-AI-MAINTENANCE-AUDIT-MARKDOWN-REPORT-001`.
- Decision:
  `AI maintenance audit Markdown report output / explicit write-report mode / no hardware or firmware action`.
- Extended `tools/run_ai_maintenance_audit.py` with `--write-report <path>`.
  Default audit behavior remains no-write; Markdown output is created only when
  the caller explicitly passes a report path.
- The generated report includes audit result, generated UTC timestamp, project
  Skill mode, no-power boundary, step table, command list, errors, and output
  tails. It explicitly states that the report is repository maintenance
  evidence only and not hardware validation.
- Added a unit test that writes a quick repo-only audit report to a temporary
  directory and checks the Markdown content and JSON `report_path`.
- Updated AI/workflow maintenance docs, the project Skill workflow-maintenance
  reference, retrieval expansion, retrieval eval, and contract checks so
  `--write-report` remains discoverable.
- Reinstalled the validated repo-local project Skill after updating
  `references/workflow-maintenance.md`; final installed Skill drift check is
  OK.
- Verification passed:
  `python tools/run_ai_maintenance_audit.py --json --max-output-chars 700`
  returned `ok: true`; it ran `Skill is valid!`;
  `python tools/check_project_skill_install.py` OK;
  `python tools/build_context_pack.py --mode workflow_maintenance --max-chars 350`;
  `python tools/check_ai_contracts.py` with no errors and only the known
  `ACTIVE_TASK.md` review-lifecycle warnings;
  `python tools/build_vector_store.py` built `8845` chunks;
  `python tools/search_local_v2.py --eval` passed;
  `python -m unittest discover -s tests` ran `139` tests OK;
  `python -m compileall src tests` passed;
  `git diff --check` reported CRLF conversion warnings only.
- This does not install external GitHub Skills and does not mark the earlier
  `done + Review Required` task as `reviewed`.
- Safety boundary unchanged: no DMM table fill, no firmware implementation, no
  generated-code edit, no CubeMX/MCSDK edit, no flash, no 24V, no power-board
  connection, no motor connection, no Gate PWM, no Motor Profiler, no Hall
  closed-loop, and no sensorless / SMO claim.

## 2026-06-08 AI Maintenance Audit Runner Added

- Added the no-power repository maintenance task:
  `TASK-2026-06-08-ai-maintenance-audit-runner`.
- Evidence:
  `EV-2026-06-08-AI-MAINTENANCE-AUDIT-RUNNER-001`.
- Decision:
  `AI maintenance audit runner / consolidated no-power closeout checks / no hardware or firmware action`.
- Added `tools/run_ai_maintenance_audit.py`, a consolidated no-power audit
  runner for AI/workflow maintenance closeout.
- The full audit runs Skill validation, project Skill install drift check,
  `workflow_maintenance` context pack rendering, AI contract checks,
  vector-store rebuild, retrieval eval, unit tests, compileall, and
  `git diff --check`.
- The quick audit mode
  `python tools/run_ai_maintenance_audit.py --quick --repo-only-skill --json`
  runs an environment-independent project Skill, context-pack, and AI contract
  handoff check.
- Wired the audit runner into `tools/build_context_pack.py`,
  `tools/check_ai_contracts.py`, `tests/test_ai_architecture_contracts.py`,
  `retrieval_eval/queries.json`, `tools/search_local_v2.py`, `AI_CONTEXT.md`,
  `docs/00_project_truth/ai_architecture.md`, `docs/file_map.md`,
  `tools/README.md`, `workflow/CURRENT_SNAPSHOT.md`, `workflow/ACTIVE_TASK.md`,
  and `workflow/evidence_register.md`.
- Reinstalled the validated repo-local project Skill after updating
  `references/workflow-maintenance.md`; final installed Skill drift check is
  OK.
- Verification passed:
  `python tools/run_ai_maintenance_audit.py --json --max-output-chars 800`
  returned `ok: true`; it ran `Skill is valid!`;
  `python tools/check_project_skill_install.py` OK;
  `python tools/build_context_pack.py --mode workflow_maintenance --max-chars 350`;
  `python tools/check_ai_contracts.py` with no errors and only the known
  `ACTIVE_TASK.md` review-lifecycle warnings;
  `python tools/build_vector_store.py` built `8837` chunks;
  `python tools/search_local_v2.py --eval` passed;
  `python -m unittest discover -s tests` ran `138` tests OK;
  `python -m compileall src tests` passed;
  `git diff --check` reported CRLF conversion warnings only.
- This does not install external GitHub Skills and does not mark the earlier
  `done + Review Required` task as `reviewed`.
- Safety boundary unchanged: no DMM table fill, no firmware implementation, no
  generated-code edit, no CubeMX/MCSDK edit, no flash, no 24V, no power-board
  connection, no motor connection, no Gate PWM, no Motor Profiler, no Hall
  closed-loop, and no sensorless / SMO claim.

## 2026-06-08 Project Skill Install Drift Checker Added

- Added the no-power repository maintenance task:
  `TASK-2026-06-08-project-skill-install-drift-checker`.
- Evidence:
  `EV-2026-06-08-PROJECT-SKILL-INSTALL-DRIFT-CHECK-001`.
- Decision:
  `Project Skill install drift checker / repo-local versus installed Skill comparison / no hardware or firmware action`.
- Added `tools/check_project_skill_install.py`, a read-only checker that
  validates the repo-local project Skill source and optionally compares it with
  the installed user Skill under `.codex/skills`.
- The checker reports `missing_installed_files`, `extra_installed_files`, and
  `changed_installed_files`, and supports `--repo-only --json` for tests or CI.
- Wired the checker into `tools/build_context_pack.py --mode ai_maintenance`
  and `--mode workflow_maintenance`, `tools/check_ai_contracts.py`,
  `tests/test_ai_architecture_contracts.py`, `retrieval_eval/queries.json`,
  `tools/search_local_v2.py`, `AI_CONTEXT.md`,
  `docs/00_project_truth/ai_architecture.md`, `docs/file_map.md`,
  `tools/README.md`, `workflow/CURRENT_SNAPSHOT.md`, `workflow/ACTIVE_TASK.md`,
  and `workflow/evidence_register.md`.
- Reinstalled the validated repo-local project Skill to
  `C:\Users\gregrg\.codex\skills\stm32g474-foc-assistant` after the new
  checker detected an expected drift in `references/workflow-maintenance.md`.
- Verification passed:
  `python tools/check_project_skill_install.py --repo-only --json`;
  `python tools/check_project_skill_install.py`;
  `python tools/build_context_pack.py --mode workflow_maintenance --max-chars 350`;
  `python tools/check_ai_contracts.py` with no errors and only the known
  `ACTIVE_TASK.md` review-lifecycle warnings;
  `python tools/build_vector_store.py` built `8827` chunks;
  `python tools/search_local_v2.py --eval` passed;
  `python -m unittest discover -s tests` ran `137` tests OK;
  `python -m compileall src tests` passed;
  `git diff --check` reported CRLF conversion warnings only.
- This does not install external GitHub Skills and does not mark the earlier
  `done + Review Required` task as `reviewed`.
- Safety boundary unchanged: no DMM table fill, no firmware implementation, no
  generated-code edit, no CubeMX/MCSDK edit, no flash, no 24V, no power-board
  connection, no motor connection, no Gate PWM, no Motor Profiler, no Hall
  closed-loop, and no sensorless / SMO claim.

## 2026-06-08 Project Skill v2 Optimization Implemented

- Added the no-power repository maintenance task:
  `TASK-2026-06-08-project-skill-v2-optimization`.
- Evidence:
  `EV-2026-06-08-PROJECT-SKILL-V2-OPT-001`.
- Decision:
  `Project Skill v2 router / no-power references / contract-checked workflow maintenance / no hardware or firmware action`.
- Refactored the project Skill source
  `codex_skills/stm32g474-foc-assistant/SKILL.md` into a concise v2 router.
- Added one-level Skill references:
  `project-navigation.md`, `no-power-boundary.md`,
  `learning-feedback.md`, and `workflow-maintenance.md`.
- Updated `agents/openai.yaml` so the visible Skill metadata points to
  no-power boundaries, weak points, and evidence records.
- Extended `tools/build_context_pack.py --mode workflow_maintenance` and
  `--mode ai_maintenance` to include the project Skill router and references.
- Extended `tools/check_ai_contracts.py` and
  `tests/test_ai_architecture_contracts.py` with project Skill v2 contracts,
  including required references, UTF-8 readability, no mojibake markers in the
  Skill source, install-flow documentation, and the four-line execution gate.
- Extended local retrieval by indexing `codex_skills/`, adding source priority
  for the project Skill, and adding the `project_skill_v2_router` eval case.
- Updated `AI_CONTEXT.md`, `workflow/CURRENT_SNAPSHOT.md`,
  `docs/00_project_truth/ai_architecture.md`, `docs/file_map.md`,
  `tools/README.md`, `workflow/ACTIVE_TASK.md`, and
  `workflow/evidence_register.md` so the Skill v2 maintenance surface is
  discoverable from low-token handoff.
- Installed the validated repo-local project Skill to
  `C:\Users\gregrg\.codex\skills\stm32g474-foc-assistant`; restart Codex if
  the updated Skill does not appear immediately.
- Verification passed:
  `python -X utf8 C:\Users\gregrg\.codex\skills\.system\skill-creator\scripts\quick_validate.py codex_skills\stm32g474-foc-assistant`;
  `python tools/build_context_pack.py --mode workflow_maintenance --max-chars 350`;
  `python tools/check_ai_contracts.py` with no errors and only the known
  `ACTIVE_TASK.md` review-lifecycle warnings;
  `python tools/build_vector_store.py` built `8819` chunks;
  `python tools/search_local_v2.py --eval` passed;
  `python -m unittest discover -s tests` ran `136` tests OK;
  `python -m compileall src tests` passed;
  `git diff --check` reported CRLF conversion warnings only.
- This does not install unreviewed external GitHub Skills and does not mark the
  earlier `done + Review Required` task as `reviewed`.
- Safety boundary unchanged: no DMM table fill, no firmware implementation, no
  generated-code edit, no CubeMX/MCSDK edit, no flash, no 24V, no power-board
  connection, no motor connection, no Gate PWM, no Motor Profiler, no Hall
  closed-loop, and no sensorless / SMO claim.

## 2026-06-08 Project Workflow / AI Architecture Maintenance Implemented

- Added the no-power repository maintenance task:
  `TASK-2026-06-08-project-workflow-ai-architecture-optimization`.
- Evidence:
  `EV-2026-06-08-PROJECT-WORKFLOW-AI-ARCHITECTURE-OPT-001`.
- Decision:
  `Project workflow and AI architecture maintenance / workflow_maintenance context / project workflow contract checks / no hardware or firmware action`.
- Added `tools/build_context_pack.py --mode workflow_maintenance` for
  automation, learning feedback, closeout checklist, definition-of-done,
  submission checklist, index, tool, retrieval, and test maintenance handoffs.
- Extended `tools/check_ai_contracts.py` so project workflow contracts are now
  checked along with AI entry files, safety phrases, review lifecycle, UTF-8
  readability, index coverage, retrieval-eval coverage, and dangerous positive
  claims.
- Extended local retrieval regression with workflow cases for closeout,
  automation `No repo writes`, learning feedback loop, and repo-maintenance
  definition of done. `tools/search_local_v2.py --eval` remains source-finding
  evidence only and does not validate hardware.
- Updated `AI_CONTEXT.md`, `workflow/CURRENT_SNAPSHOT.md`,
  `docs/00_project_truth/ai_architecture.md`, `docs/file_map.md`,
  `tools/README.md`, `workflow/ACTIVE_TASK.md`, and
  `workflow/evidence_register.md` so the new workflow-maintenance contract is
  discoverable from low-token handoff.
- Verification passed:
  `python tools/build_context_pack.py --mode workflow_maintenance --max-chars 350`;
  `python tools/check_ai_contracts.py` with no errors and only the known
  `ACTIVE_TASK.md` review-lifecycle warnings;
  `python tools/build_vector_store.py` built `8786` chunks;
  `python tools/search_local_v2.py --eval` passed;
  `python -m unittest discover -s tests` ran `135` tests OK;
  `python -m compileall src tests` passed;
  `git diff --check` reported CRLF conversion warnings only.
- This does not mark the earlier `done + Review Required` task as `reviewed`.
  User review still clears strict warnings.
- Safety boundary unchanged: no DMM table fill, no firmware implementation, no
  generated-code edit, no CubeMX/MCSDK edit, no flash, no 24V, no power-board
  connection, no motor connection, no Gate PWM, no Motor Profiler, no Hall
  closed-loop, and no sensorless / SMO claim.

## 2026-06-01 PCB2 Populated / Route Unchanged / DMM Pending

- User reported: PCB2 soldered / in hand, and current route still
  `PA0/PA1/PB4 + PB3=LIN1 + P14/P15=3V3/GND`.
- Added the no-power populated-board handoff:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/pcb2_populated_route_unchanged_dmm_pending_2026-06-01.md`.
- Decision:
  `PCB2 populated / current route unchanged / DMM continuity and short-check opened as no-power pending / no powered action`.
- The DMM gate is now open as a no-power user action, but it is not passed.
  The user must fill the continuity / short-check table before any software
  Hall adapter implementation, flash, Gate PWM, motor, Motor Profiler, or
  Hall closed-loop claim.
- Current route for DMM remains:
  `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`, `PB3=LIN1`, and
  `P14/P15=3V3/GND`.
- Safety boundary unchanged: board unpowered only; no 24V, no powered
  power-board connection, no motor connection, no Gate PWM, no flash, no
  generated-project run, no Motor Profiler / Motor Pilot, and no Hall
  closed-loop or hardware readiness claim.

## 2026-06-01 PR #5 Learning Notes Merged And WP-030 Mixed Trace Passed

- Reviewed PR #5, `learning notes`, from branch
  `learning/mcsdk-hall-feedback-2026-06-01`.
- The two added files stayed inside the teaching contract: L2 MCSDK Hall
  speed / position feedback concept evidence only, no MCSDK Hall closed-loop
  completion claim, no Motor Profiler / power-board / motor / PWM / serial /
  build validation claim, and no-power / debug-only boundary preserved.
- Merged PR #5 into `master` with merge commit
  `2b614b4aae4eb40a5b2a882c5f2252dadbe06079`.
- User reported on 2026-06-01 that the hardware teammate is close to finishing
  PCB2 soldering. This is a scheduling clue only; until populated-board
  evidence and a filled DMM continuity / short-check table exist, the DMM gate
  remains deferred, not passed.
- User passed the WP-030 no-power mixed-sequence review:
  `(1000,100)` baseline, `(1600,100)` repeat, `(2200,110)` accepted adjacent
  forward candidate, `(2210,010)` bounce candidate rejected because
  `dt=10 < 50`, `(3000,111)` illegal state, and `(3800,011)` abnormal jump
  from last trusted `110`.
- Decision:
  `PR #5 concept-learning evidence accepted / WP-030 mixed trace passed / no firmware implementation / no MCSDK hook / no Hall readiness`.
- Safety boundary unchanged: no DMM until populated board exists, no 24V, no
  power-board connection, no motor connection, no Gate PWM, no flash, no
  generated-project run, no Motor Profiler / Motor Pilot, and no Hall
  closed-loop or hardware readiness claim.

## 2026-05-31 PCB2 Waiting-Hardware Handoff Added

- Added the no-power waiting-hardware handoff:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/pcb2_waiting_hardware_handoff_2026-05-31.md`.
- Decision:
  `PCB2 waiting for population / DMM gate deferred / no powered action / no firmware implementation`.
- User-selected current PCB2 state: not populated / waiting for hardware.
- The DMM continuity / short-check request remains pending and must not be filled from memory or old evidence. Deferred does not mean passed.
- Current route stays as recorded unless a new hardware source packet says otherwise:
  `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`, `PB3=LIN1`, and `P14/P15=3V3/GND`.
- At that time the user action was to return the hardware teammate status line and any updated schematic / EDA / netlist / Gerber / BOM / pin-table evidence, plus answer the no-power Hall mixed-sequence check under WP-030. The mixed-sequence check was answered and accepted on 2026-06-01; hardware evidence is still pending.
- Safety boundary unchanged: no DMM until populated board exists, no 24V, no power-board connection, no motor connection, no Gate PWM, no flash, no generated-project run, no Motor Profiler / Motor Pilot, and no Hall closed-loop or hardware readiness claim.

## 2026-05-28 Dual-Teacher Concept-Only Guard Added

- Added an explicit dual-teacher concept-only role guard after the user reported
  repeated drift in the teaching boundary.
- Decision:
  `Dual-teacher concept-only role guard / ChatGPT teaches theory / Codex reviews records and executes repo work`.
- Rule now recorded in `workflow/codex_dual_teacher_execution_gate.md`,
  `workflow/teaching_contract.md`, `AI_CONTEXT.md`,
  `docs/00_project_truth/ai_architecture.md`, and the project Skill source
  `codex_skills/stm32g474-foc-assistant/SKILL.md`.
- New behavior: for theory, concept, "I do not understand", "teach me", or
  "what should I learn" turns that do not require repo files, commands, build
  output, tests, logs, screenshots, learning-record writes, GitHub, or
  hardware-safety state, Codex must hand the user a concrete ChatGPT prompt/task
  packet instead of teaching the full lesson.
- Added GitHub learning-evidence handoff: if ChatGPT has GitHub write access,
  it may open a branch / PR for its own concept-lesson evidence. Codex then
  syncs, reviews, verifies, records, and either accepts or asks for changes.
  The PR is not accepted project truth until Codex review.
- Codex remains responsible for reviewing returned answers, updating learning
  evidence, running checks, recording project status, and executing any
  repo-side engineering work.
- Safety boundary unchanged: this is workflow-control only. It does not
  authorize firmware edits, Workbench regeneration, flash, 24V, power-board
  connection, motor connection, Gate PWM, Motor Profiler, Hall closed-loop, or
  powered readiness.

## 2026-05-28 Software Hall Firmware-Entry Plan Added

- Added the Chinese-first no-power firmware-entry plan:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_firmware_entry_plan_2026-05-28.md`.
- Decision:
  `Software Hall firmware-entry plan / debug-only no-power boundary / no firmware implementation / no MCSDK hook / no Hall readiness`.
- The plan locks the current route as `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`
  and keeps `PB3=LIN1` out of Hall. MCSDK standard TIM2 Hall
  `PA15/PB3/PB10` remains generated-source evidence only, not current PCB2
  Hall.
- The first future adapter shape is debug-only: GPIO/EXTI capture on
  `PA0/PA1/PB4`, ISR stores only `raw_state + timestamp + event counter`,
  low-priority state machine rejects `000/111`, repeat, bounce candidates, and
  abnormal jumps, and low-frequency debug snapshot exposes counters plus
  `direction_candidate` / `speed_candidate`.
- Hard stops remain: no writes to `HALL_M1`, no `hall_speed_pos_fdbk.c/.h`
  modification, no speed loop / PID injection, no `mc_tasks_foc.c` / JEOC /
  FOC ISR edits, no TIM1 PWM edits, no generated-code edits, no Motor
  Profiler / Motor Pilot, and no Hall closed-loop claim.
- PCB2 is still unpopulated. DMM continuity / short-check evidence is hardware-side deferred, not passed. The 2026-05-27 build-only pass remains
  local compile evidence only and does not replace hardware or runtime proof.
- User checkpoint: no measurement, no power, and no toolchain work is needed
  now. Keep
  `C:\Users\gregrg\.st_workbench\projects\QIANSAI_G474_STDRIVE101_FOC_P2`
  stable and report any hardware route change or PCB2 solder-complete signal.

## 2026-05-27 No-Power Build-Only Debug Pass Recorded

- Ran no-power build-only command for the external Workbench project:
  `cmake --build "C:\Users\gregrg\.st_workbench\projects\QIANSAI_G474_STDRIVE101_FOC_P2\build\Debug" --config Debug`.
- Result: exit code `0`; Ninja reported `ninja: no work to do`, meaning the
  Debug target was already up to date.
- Confirmed build artifacts:
  `QIANSAI_G474_STDRIVE101_FOC_P2.elf` (`2161388` bytes,
  SHA256 `8EF20B93DC069F085AEBD670A77C5C4C4266FE59532A91DF784241CCB062BB23`)
  and `QIANSAI_G474_STDRIVE101_FOC_P2.map` (`1484465` bytes,
  SHA256 `B571B7C9CF5F262BF49E35BE63B05C128CC59480E546FA36929BD8704CBD132D`).
- Added build-only result record:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/build_only_result_2026-05-27_qiansai_g474_stdrive101_foc_p2_debug.md`.
- Decision:
  `No-power build-only Debug pass / local toolchain compiles generated project / no firmware runtime or hardware readiness`.
- This upgrades only the local no-power compile evidence for the generated
  Workbench project. It does not upgrade firmware runtime behavior, current
  PCB2 routing, DMM continuity, STDRIVE101 protection, current sensing, GPIO /
  EXTI runtime behavior, MCSDK Hall integration, Gate PWM safety, Hall
  closed-loop, Motor Profiler readiness, motor readiness, power-stage
  readiness, or sensorless readiness.
- Safety boundary unchanged: no flash, no Run / Debug, no 24V, no power-board
  connection, no motor connection, no Gate PWM output, no Motor Profiler, no
  Motor Pilot.

## 2026-05-27 Software Hall MCSDK Speed/Position Feedback Interface Review Added

- Added the no-power MCSDK speed / position feedback interface review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_mcsdk_speed_position_feedback_interface_review_2026-05-27.md`.
- Decision:
  `Software Hall MCSDK speed/position feedback interface review / no firmware implementation / no MCSDK hook / no Hall readiness`.
- The archived generated `Src/Inc` snapshot shows MCSDK standard Hall is a full feedback chain, not only a three-bit Hall state reader: TIM2 Hall IRQ updates `HALL_M1`, medium-frequency tasks calculate speed/reliability, the speed loop reads `SPD_GetAvrgMecSpeedUnit(...)`, and the FOC current loop consumes electrical angle through `SPD_GetElAngle(...)`.
- Current PCB2 remains `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`, with `PB3=LIN1`; this still does not match Workbench TIM2 Hall `PA15/PB3/PB10`.
- `speed_pos_fdbk.h` is not present in the archived project `Src/Inc` snapshot, so the base MCSDK feedback interface remains only partially visible and no custom `SpeednPosFdbk` component is accepted.
- Current decision: future software Hall remains debug-only unless a separate reviewed `SpeednPosFdbk`-compatible component proposal is created with full interface evidence, DMM evidence, no-power build record, exact hook list, and rollback plan.
- Verification passed: `python -m unittest discover -s tests` (`126` tests OK), `python -m compileall src tests`, `git diff --check` with CRLF warnings only, `python tools\build_vector_store.py` (`8678` chunks), `python tools\search_local_v2.py --eval`, and `python tools\check_ai_contracts.py` with warning only that `ACTIVE_TASK.md` is done and still requires review.
- No STM32 firmware, generated-code edit, MCSDK hook, no-power build record, DMM proof, flash, 24V, power-board connection, motor connection, Gate PWM output, Hall closed-loop, motor readiness, power-stage readiness, or sensorless readiness is upgraded.
## 2026-05-27 Full Workbench Src/Inc Snapshot Archived

- Confirmed the external generated Workbench project exists at
  `C:\Users\gregrg\.st_workbench\projects\QIANSAI_G474_STDRIVE101_FOC_P2`.
- Archived a no-power read-only snapshot at
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-27_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot/`.
- Added source review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-27_001_qiansai_g474_stdrive101_foc_p2_full_src_inc_snapshot.md`.
- Decision:
  `Full generated Src/Inc snapshot archived / source interface evidence available for read-only review / no firmware implementation / no MCSDK hook / no Hall readiness`.
- The snapshot includes generated `Src/`, `Inc/`, `cmake/`, top-level project/build metadata, `SOURCE_MANIFEST_2026-05-27.md`, and `SHA256SUMS.txt`.
- Key requested files are now present for read-only review: `hall_speed_pos_fdbk.c/.h`, `speed_torq_ctrl.c/.h`, `mc_tasks.c/.h`, `mc_tasks_foc.c`, `mc_interface.c/.h`, `mc_api.c/.h`, `mc_app_hooks.c/.h`, `mc_parameters.c/.h`, `motorcontrol.c/.h`, `mc_type.h`, interrupt sources, current-feedback backend files, register-interface files, `usart_aspep_driver.c`, and `aspep.c/.h`.
- `Inc/usart_aspep_driver.h` is not present in the generated `Inc/` folder and must not be silently treated as an accepted interface header.
- Static review confirms generated MCSDK Hall still uses standard TIM2 Hall `PA15/PB3/PB10`, while current PCB2 remains `PA0/PA1/PB4` software Hall with `PB3=LIN1`; therefore this snapshot does not prove current PCB2 Hall integration.
- No STM32 firmware, generated-code edit, MCSDK hook, no-power build record, DMM proof, flash, 24V, power-board connection, motor connection, Gate PWM output, Hall closed-loop, motor readiness, power-stage readiness, or sensorless readiness is upgraded.

## 2026-05-27 Software Hall MCSDK Hook Evidence Request Checklist Added

- Added the no-power MCSDK hook evidence request checklist:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_mcsdk_hook_evidence_request_checklist_2026-05-27.md`.
- Decision:
  `Software Hall MCSDK hook evidence request checklist / no firmware implementation / no MCSDK hook / no Hall readiness`.
- The checklist turns log-only MCSDK generated file names into a concrete source-evidence request before any future software Hall hook.
- Required evidence now includes exact generated or MCSDK interface sources such as `hall_speed_pos_fdbk.c/.h`, speed / position feedback interface evidence, `speed_torq_ctrl.c/.h`, `mc_tasks.c/.h`, `mc_tasks_foc.c`, `mc_interface.c/.h`, `mc_api.c/.h`, `mc_app_hooks.c/.h`, `mc_parameters.c/.h`, `motorcontrol.c/.h`, `mc_type.h`, interrupt sources, current-feedback backend files, and ASPEP / register-interface files.
- Rejected evidence types include log-only file names, screenshots, files from a different project/version, AI summaries, host tests, build-only success by itself, and memory-based claims.
- No STM32 firmware, MCSDK hook, generated-code edit, build record, DMM proof, flash, 24V, power-board connection, motor connection, Gate PWM output, Hall closed-loop, motor readiness, power-stage readiness, or sensorless readiness is upgraded.
## 2026-05-27 Software Hall MCSDK Firmware-Integration Boundary Review Draft Added

- Added the no-power MCSDK firmware-integration boundary review draft:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_mcsdk_firmware_integration_boundary_review_2026-05-27.md`.
- Decision:
  `Software Hall MCSDK firmware-integration boundary review draft / no firmware implementation / no MCSDK hook / no Hall readiness`.
- The draft records that future software Hall output is only
  `direction_candidate` and `speed_candidate` until accepted MCSDK interface
  evidence exists.
- Generated clues such as `HALL_M1`, `SpeednTorqCtrlM1`, `PIDSpeedHandle_M1`,
  `pSTC`, `MCI_Handle_t`, `FOCVars`, `SPD_HALL_TIM_M1_IRQHandler`,
  `M1_SPEED_SENSOR=HALL_SENSOR`, and `M1_HALL_TIMER_SELECTION=HALL_TIM2` are
  treated as read-only clues, not MCSDK hooks.
- Generated log file names `hall_speed_pos_fdbk.c/.h`, `speed_torq_ctrl.c/.h`,
  and `mc_app_hooks.c/.h` remain file-name clues only until archived source and
  interface contracts are reviewed.
- Hard stops remain: no write to `HALL_M1`, no speed-loop / PID injection, no
  JEOC / FOC ISR edits, no TIM1 PWM edits, no generated-code edits, no Motor
  Profiler / Motor Pilot, and no Hall closed-loop claim.
- No STM32 firmware, MCSDK hook, build record, DMM proof, flash, 24V,
  power-board connection, motor connection, Gate PWM output, Hall closed-loop,
  motor readiness, power-stage readiness, or sensorless readiness is upgraded.
## 2026-05-27 Software Hall Debug-Output Route Review Draft Added

- Added the no-power low-frequency debug-output route review draft:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_debug_output_route_review_2026-05-27.md`.
- Decision:
  `Software Hall low-frequency debug-output route review draft / no firmware implementation / no UART implementation / no Hall readiness`.
- The draft defines future debug snapshot fields:
  `current_raw_state`, `last_accepted_state`, `last_decision`, `edge_count`,
  `illegal_state_count`, `repeat_count`, `bounce_candidate_count`,
  `abnormal_jump_count`, `lost_event_count`, `last_edge_dt_ticks`,
  `timestamp_source_id`, `direction_candidate`, and `speed_candidate`.
- Output boundary:
  first firmware shape, if later authorized, must be a low-frequency snapshot
  path. It is not every-edge streaming, not ISR printing, not JEOC / FOC ISR
  work, and not MCSDK speed feedback.
- Route constraints:
  UART text / CSV / JSON, ESP32 / WebSocket display, MCSDK USART2 / ASPEP /
  MCP reuse, `PA2/PA3` reuse, and SWO / ITM are not authorized by this draft.
- No STM32 firmware, UART implementation, JSON protocol, ESP32 gateway,
  MCSDK hook, build record, DMM proof, flash, 24V, power-board connection,
  motor connection, Gate PWM output, Motor Profiler, Hall closed-loop, motor
  readiness, power-stage readiness, or sensorless readiness is upgraded.

## 2026-05-27 Software Hall Timestamp Source Review Draft Added

- Added the no-power timestamp-source review draft:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_timestamp_source_review_2026-05-27.md`.
- Decision:
  `Software Hall timestamp-source review draft / no firmware implementation / no timer configuration / no Hall readiness`.
- The draft records why `TIM1` is a hard no for software Hall timestamping:
  generated clues tie it to PWM, ADC injected triggering, and FOC timing through
  `MX_TIM1_Init()`, `TIM1_UP_TIM16_IRQn`, and `ADC_EXTERNALTRIGINJEC_T1_TRGO`.
- The draft records why `TIM2` is not current `PA0/PA1/PB4` software Hall
  timestamp clearance: generated clues use `HAL_TIMEx_HallSensor_Init` and
  `M1_HALL_TIMER_SELECTION=HALL_TIM2` for the standard MCSDK Hall route.
- `HAL_GetTick()` / SysTick is limited to coarse logs or timeouts because the
  local HAL clue is `uwTickFreq = HAL_TICK_FREQ_DEFAULT; /* 1KHz */`.
- Future preferred class is an isolated `dedicated free-running timer`, with
  `1 us tick` only as a review target and `unsigned delta` required for
  overflow handling.
- No exact timer instance, prescaler, CubeMX setting, firmware source,
  MCSDK hook, build record, DMM proof, flash, 24V, power-board connection,
  motor connection, Gate PWM output, Motor Profiler, Hall closed-loop, motor
  readiness, power-stage readiness, or sensorless readiness is upgraded.

## 2026-05-27 Local Retrieval V2 Added

- Added the second AI architecture foundation batch:
  `tools/search_local_v2.py`,
  `retrieval_eval/queries.json`, and `tests/test_search_local_v2.py`.
- Decision:
  `Local retrieval v2 / source-priority search / retrieval regression checks /
  no RAG hardware claims / no powered readiness`.
- Evidence ID:
  `EV-2026-05-27-AI-RETRIEVAL-V2-001`.
- The new search tool reads the existing `vector_store/` index but adds:
  query expansion, source-priority weighting, phrase bonuses, a minimum
  reliable-score threshold, and a built-in retrieval evaluation mode.
- The first retrieval evaluation cases cover:
  `JEOC 娑擃厽鏌囬柌宀冨厴娑撳秷鍏?printf`,
  `ESP32 閼虫垝绗夐懗鍊熺箻閸?FOC 鐎圭偞妞傞幒褍鍩楅悳鐥? and
  `瑜版挸澧?PCB2 Hall 鐠侯垳鍤?PA0 PA1 PB4 PB3 閺勵垯绮堟稊鍧?
- Verification:
  `python tools/search_local_v2.py "JEOC 娑擃厽鏌囬柌宀冨厴娑撳秷鍏?printf"` now ranks
  `docs/protocol.md` first and also returns the JEOC review template and
  STM32 app rules. `python tools/search_local_v2.py --eval` passed.
  `python -m unittest discover -s tests` passed with 115 tests.
  `python tools/build_vector_store.py` rebuilt the local retrieval index with
  8548 chunks.
- This remains local evidence retrieval only. It does not generate hardware
  conclusions, does not replace phase gates or evidence records, and does not
  upgrade firmware implementation, generated-code trust, build trust,
  GPIO/EXTI runtime proof, MCSDK Hall integration, DMM continuity, flash, 24V,
  power-board connection, motor connection, Gate PWM output, Motor Profiler,
  Hall closed-loop, motor readiness, power-stage readiness, or sensorless
  readiness.

## 2026-05-27 AI Architecture Foundation Added

- Added the first AI architecture foundation batch:
  `docs/00_project_truth/ai_architecture.md`,
  `workflow/CURRENT_SNAPSHOT.md`,
  `tools/build_context_pack.py`, and `tools/check_ai_contracts.py`.
- Decision:
  `AI architecture foundation / low-token handoff / read-only workflow checks /
  no firmware, no hardware, no powered readiness`.
- Evidence ID:
  `EV-2026-05-27-AI-ARCHITECTURE-FOUNDATION-001`.
- The architecture contract keeps the current evidence-first model:
  short context -> grounded retrieval -> task packet -> safe execution ->
  evidence record -> learning update -> verification.
- `CURRENT_SNAPSHOT.md` is now the default low-token current-state page. It
  summarizes P2 no-power state, current PCB2 Hall route, software Hall planning
  status, AI architecture work, and the active safety boundary.
- `build_context_pack.py` can generate mode-specific context packs for
  `codex_task`, `teaching`, `hardware_review`, `mcsdk_packet`,
  `experiment_analysis`, and `report_defense`.
- `check_ai_contracts.py` performs a read-only static check of required AI
  architecture files, `ACTIVE_TASK` status and evidence ID, safety phrases,
  indexes, review-queue size, and dangerous positive readiness claims.
- Verification:
  `python tools/check_ai_contracts.py` passed with no errors,
  `python tools/build_context_pack.py --mode codex_task --max-chars 400`
  emitted a context pack, `python tools/build_context_pack.py --list-modes`
  listed the supported modes, and `python -m unittest discover -s tests`
  passed with 111 tests. `python tools/build_vector_store.py` rebuilt the
  local retrieval index with 8529 chunks.
- This is repository workflow infrastructure only. It does not upgrade
  firmware implementation, generated-code trust, build trust, GPIO/EXTI
  runtime proof, MCSDK Hall integration, DMM continuity, flash, 24V,
  power-board connection, motor connection, Gate PWM output, Motor Profiler,
  Hall closed-loop, motor readiness, power-stage readiness, or sensorless
  readiness.

## 2026-05-27 Software Hall GPIO/EXTI Boundary Review Draft Added

- Added the no-power GPIO/EXTI boundary draft:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_gpio_exti_boundary_review_2026-05-27.md`.
- Decision:
  `Software Hall GPIO/EXTI boundary review draft / no firmware implementation / no GPIO runtime proof / no Hall readiness`.
- The draft records the current static boundary for the future software Hall
  route: `PA0=GPIO_EXTI0`, `PA1=GPIO_EXTI1`, `PB4=GPIO_EXTI4`, with
  `PB3=LIN1` kept out of Hall.
- Local CMSIS/HAL clues identify `EXTI0_IRQn`, `EXTI1_IRQn`, `EXTI4_IRQn`,
  `GPIO_MODE_IT_RISING_FALLING`, and pull-mode options, but this is only a
  no-power review draft.
- Open blockers remain: populated PCB2, DMM continuity / short-check table,
  pull-up / pull-down decision, timestamp-source decision, debug-output route,
  and separate MCSDK firmware-integration review. The build-only record now
  exists but does not open firmware implementation or hardware readiness.
- No STM32 firmware, CubeMX/Workbench setting, generated code, build, flash,
  Gate PWM, Motor Profiler, Motor Pilot, motor, power-stage, Hall closed-loop,
  or sensorless readiness is upgraded.

## 2026-05-27 Software Hall Firmware-Entry Checklist Added

- Added the no-power firmware-entry checklist:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_firmware_entry_checklist_2026-05-27.md`.
- Decision:
  `Software Hall firmware-entry checklist / no firmware implementation / no MCSDK Hall integration / no Hall readiness`.
- The checklist converts the existing software Hall prep, pseudocode, host
  model, golden vectors, and MCSDK probe into explicit entry conditions before
  any future STM32 adapter code.
- Current required but missing entry evidence remains: populated PCB2,
  DMM continuity / short-check table, GPIO/EXTI boundary review, timestamp
  source decision, low-frequency debug-output route, no-power build-only
  record, and a separate MCSDK firmware-integration review before any hook.
- First future code, if later authorized, must stay as an independent adapter.
  It must not modify TIM1 PWM, JEOC / FOC ISR, `HALL_M1`, MCSDK speed loop,
  Gate PWM, flash, Motor Profiler, Motor Pilot, or powered hardware.
- No user hardware action is needed while PCB2 is unpopulated. The next
  learner checkpoint remains the one-sentence processing-order teach-back.

## 2026-05-27 Software Hall MCSDK Integration Probe Added

- Added a read-only MCSDK integration clue review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_mcsdk_integration_probe_2026-05-27.md`.
- Decision:
  `MCSDK Hall integration points identified as read-only clues / no firmware implementation / no MCSDK Hall integration / no Hall readiness`.
- Read-only checks in the 2026-05-21 generated-project clue folder found the
  standard MCSDK Hall path: `MX_TIM2_Init()`, `HAL_TIMEx_HallSensor_Init`,
  `HALL_Handle_t HALL_M1`, `SpeednTorqCtrlM1`, `PIDSpeedHandle_M1`,
  `M1_SPEED_SENSOR=HALL_SENSOR`, `SPEED_SENSOR_SELECTION=HALL_SENSORS`,
  `M1_HALL_TIMER_SELECTION=HALL_TIM2`, and generated log references to
  `hall_speed_pos_fdbk.c/.h` and `speed_torq_ctrl.c/.h`.
- Conclusion: those are only read-only clues for the standard TIM2 hardware
  Hall route. They do not match current PCB2 `PA0/PA1/PB4` software Hall and
  do not create MCSDK Hall integration.
- Any future MCSDK hook requires a separate firmware-integration review. Hard
  stops remain: do not edit JEOC / FOC ISR, TIM1 PWM timing, generated speed
  loop, or `HALL_M1` path without a new review.

## 2026-05-27 Software Hall Golden Vectors Added

- Added host-side no-power golden vectors for the future software Hall adapter:
  `tests/fixtures/software_hall_golden_vectors.json`.
- Added replay test:
  `tests/test_software_hall_vectors.py`.
- Added no-power review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_golden_vectors_review_2026-05-27.md`.
- Decision:
  `Host-side software Hall golden vectors / no firmware implementation / no MCSDK Hall integration / no Hall readiness`.
- The vectors turn the state-machine rules into replayable input/output
  examples for later firmware-adapter review: forward candidate cycle,
  illegal-state rejection, repeated-state rejection, configurable
  bounce-candidate rejection, abnormal non-adjacent jump, and reverse adjacent
  step.
- This is host-side no-power algorithm-contract evidence only. It does not read
  GPIO, configure EXTI, edit MCSDK generated code, build firmware, flash
  hardware, pass DMM, output Gate PWM, connect a motor, or prove Hall
  readiness.

## 2026-05-27 Software Hall Host Model Added

- Added a host-side executable reference model for the future software Hall
  adapter:
  `src/software_hall_model.py`.
- Added tests:
  `tests/test_software_hall_model.py`.
- Added no-power review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_host_model_review_2026-05-27.md`.
- Decision:
  `Host-side software Hall reference model / no firmware implementation / no MCSDK Hall integration / no Hall readiness`.
- The model implements the no-power algorithm sequence:
  illegal-state check -> first-valid baseline -> repeated-state rejection ->
  configurable bounce/timing check -> forward/reverse adjacent step ->
  abnormal-jump count.
- Test coverage includes valid states, `000/111`, `100 -> 110`,
  `100 -> 101`, `100 -> 011`, repeated state, configurable bounce candidate,
  and a full candidate forward cycle.
- This is executable host-side algorithm evidence only. It does not read GPIO,
  configure EXTI, edit MCSDK generated code, build firmware, flash hardware,
  pass DMM, output Gate PWM, connect a motor, or prove Hall readiness.

## 2026-05-27 Software Hall Processing-Order Teaching Card Added

- User could correctly classify individual Hall transition rows, but then
  answered `閹存垳绗夐惌銉╀壕閸熷グ when asked to restate the adapter processing order.
- Added a Chinese-first no-power repair artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_adapter_processing_order_card_2026-05-27.md`.
- Decision:
  `Software Hall adapter processing-order teaching card / no firmware implementation / no MCSDK Hall integration / no Hall readiness`.
- Evidence level:
  L1 repair artifact for the processing-order weak point. This is not a new
  mastery upgrade.
- Evidence limit: not a new mastery upgrade.
- The card explains:
  raw read -> illegal-state check -> first-valid check -> repeated-state check
  -> bounce/timing check -> forward/reverse adjacent check -> abnormal-jump
  count.
- Current route remains `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`;
  `PB3=LIN1` and is not Hall.
- This does not upgrade firmware implementation, GPIO/EXTI runtime behavior,
  MCSDK Hall integration, DMM continuity proof, build record, flash, 24V,
  power-board connection, motor connection, Gate PWM output, Motor Profiler,
  Hall closed-loop, motor readiness, power-stage readiness, or sensorless
  readiness.
- Next user checkpoint:
  say the one-sentence Chinese rule from the card, without filling another
  table.

## 2026-05-27 Hall State-Machine Follow-Up Review Passed

- User completed the follow-up Hall transition table:
  `100 -> 110`, `100 -> 101`, `100 -> 011`, `000`, and `111`.
- Codex review result:
  all five rows are correct.
- Evidence level:
  `L4 for table-level no-power Hall state-machine classification`.
- Recorded learning evidence:
  `learning/session_notes/2026-05-27_hall_state_machine_review_followup.md`
  and
  `learning/review_items/2026-05-27_hall_state_machine_review_completed.md`.
- This upgrades only algorithm-table mastery. It does not upgrade firmware
  implementation, GPIO/EXTI runtime behavior, MCSDK Hall integration, DMM
  continuity proof, build record, flash, 24V, power-board connection, motor
  connection, Gate PWM output, Motor Profiler, Hall closed-loop, motor
  readiness, power-stage readiness, or sensorless readiness.
- Next algorithm-side review before code:
  restate the adapter processing order:
  raw read -> illegal-state check -> first-valid check -> repeated-state check
  -> bounce/timing check -> forward/reverse adjacent check -> abnormal-jump
  count.

## 2026-05-27 Software Hall Adapter Pseudocode Draft Added

- Added the next no-power software Hall design artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_adapter_pseudocode_draft_2026-05-27.md`.
- Decision:
  `Software Hall adapter pseudocode draft / no firmware implementation / no MCSDK Hall integration / no Hall readiness`.
- This uses the 2026-05-27 Hall state-machine L2 learning evidence only as
  algorithm understanding, not as hardware or firmware evidence.
- The draft defines future responsibilities for `Hall_ReadRaw3()`,
  `Hall_IsValidState()`, `Hall_IsForwardAdjacent()`,
  `Hall_IsReverseAdjacent()`, `Hall_CaptureEdge_ISR()`,
  `Hall_ProcessEvent()`, and `Hall_GetDebugSnapshot()` as pseudocode only.
- Current route remains `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`;
  `PB3=LIN1` and is not Hall.
- The draft locks the decision order:
  illegal `000/111` -> repeated state -> forward/reverse adjacent transition
  -> abnormal jump.
- ISR boundary remains minimal: timestamp, raw Hall state, pending/event flag
  or small counter only. No `printf`, JSON, `HAL_Delay`, blocking wait,
  dynamic allocation, complex MCSDK call, speed-loop decision, or FOC-loop
  edit is allowed in ISR.
- PCB2 is still unpopulated, so DMM remains hardware-side deferred, not
  passed. No firmware file, runtime API, generated-code hook, MCSDK Hall
  integration, build record, flash, 24V, power-board connection, motor
  connection, Gate PWM output, Motor Profiler, Motor Pilot, Hall closed-loop,
  motor readiness, power-stage readiness, or sensorless readiness is
  authorized.

## 2026-05-22 Software Hall State-Machine Exercise Card Added

- Added the next algorithm-side no-power exercise card:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_state_machine_exercise_card_2026-05-22.md`.
- Decision:
  `User Hall state-machine exercise requested / no firmware implementation / no Hall readiness`.
- The card is Chinese-first and asks the algorithm role to answer five checks:
  why three Hall lines have six valid states, why `000/111` are illegal, why
  the candidate sequence `001 -> 101 -> 100 -> 110 -> 010 -> 011 -> 001`
  can define one direction candidate, why `PA0/PA1/PB4` must be treated as
  software GPIO/EXTI Hall, and why `PB3=LIN1` cannot be Hall.
- The required user response table is:
  `Input sequence | User judgment | Count edge? | Abnormal? | Note` for
  `001 -> 101`, `001 -> 001`, `001 -> 010`, and `000`.
- PCB2 is still unpopulated, so the DMM gate remains hardware-side deferred,
  not passed. This exercise does not need DMM, board power, Workbench, CubeMX,
  Motor Profiler, oscilloscope, or hardware measurement.
- No firmware logic, runtime API, generated-code hook, MCSDK Hall integration,
  build record, flash, 24V, power-board connection, motor connection, Gate PWM
  output, Motor Profiler, Hall closed-loop, motor readiness, power-stage
  readiness, or sensorless readiness is authorized.

## 2026-05-22 Software Hall No-Power Algorithm Prep Added

- Added the algorithm-side no-power preparation artifact:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_no_power_algorithm_prep_2026-05-22.md`.
- Decision:
  `Algorithm-side no-power preparation / no firmware implementation / no Hall readiness`.
- This lets the algorithm role progress while the unpopulated PCB2 DMM gate is
  hardware-side deferred. Deferred does not mean passed.
- The artifact locks the no-power state-machine contract for
  `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`, while keeping `PB3=LIN1` outside
  the current Hall path.
- Valid Hall candidates are `001`, `010`, `011`, `100`, `101`, and `110`;
  `000` and `111` are illegal. Repeated states do not count as new edges,
  non-adjacent jumps are abnormal, and bounce filtering remains a future
  measured-threshold topic.
- Future debug observables are only low-frequency candidates:
  raw/accepted Hall state, edge count, illegal-state count, abnormal-jump
  count, repeat count, bounce-candidate count, edge delta, direction candidate,
  and speed candidate.
- ISR boundary remains minimal: capture timestamp/state and defer decoding,
  logging, JSON, UART formatting, WebSocket work, dynamic allocation, blocking
  delays, and control decisions to lower-priority context.
- No firmware logic, runtime API, generated-code hook, MCSDK Hall integration,
  build record, flash, 24V, power-board connection, motor connection, Gate PWM
  output, Motor Profiler, Hall closed-loop, motor readiness, power-stage
  readiness, or sensorless readiness is authorized.

## 2026-05-22 No-Power DMM Evidence Request Opened

- Added the next real-world no-power evidence request:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/dmm_continuity_short_check_request_2026-05-22.md`.
- Current route remains locked as `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`,
  `PB3=LIN1`, and `P14/P15=3V3/GND`.
- Next user action is a filled DMM continuity / short-check table for
  `IA->PA0`, `IB->PA1`, `IC->PB4`, `PB3->LIN1`, `P14->3V3`, `P15->GND`,
  `nFAULT->PB12`, `3V3-GND`, STM32 signal pins to `3V3/GND`, and Hall-line
  pair shorts.
- CLI toolchain setup is not the main real-world progress blocker in this
  step. A later 2026-05-27 no-power build-only record now exists, but it does
  not replace the hardware-side DMM gate.
- No software Hall adapter implementation starts until the DMM table is
  returned and reviewed.
- No firmware logic, runtime API, generated-code hook, flash,
  24V, power-board connection, motor connection, Gate PWM output, Motor
  Profiler, Hall closed-loop, motor readiness, power-stage readiness, or
  sensorless readiness is authorized.

## 2026-05-21 Current PCB2 Software Hall Route Confirmed

- User confirmed the current PCB2 `CN3/CN8 -> STM32` mapping has no known
  error for this route decision.
- Existing archived PCB2 mapping already records `P14=3V3` and `P15=GND`;
  they are no longer a missing-evidence blocker for software Hall route
  selection. They still do not replace no-power continuity or short checks.
- Current PCB2 Hall route is locked for no-PCB-change planning as
  `HALL_A/B/C -> IA/IB/IC -> PA0/PA1/PB4`.
- Current PCB2 `PB3` is locked as `LIN1` / low-side PWM driver input. It is no
  longer a current Hall candidate in Packet A or firmware-design discussion.
- The active route is now `software Hall adapter first`; hardware rework is a
  fallback only if later MCSDK integration proves the software route unsafe or
  unrepresentable.
- The future software Hall adapter boundary is GPIO/EXTI input sampling on
  `PA0/PA1/PB4`, three-bit Hall state readout, illegal-state filtering for
  `000/111`, edge timestamp capture, and minimal ISR work only.
- The Workbench generated TIM2 Hall route `PA15/PB3/PB10` remains accepted only
  as no-power generated configuration evidence. It does not match the current
  PCB2 Hall route and cannot be used directly as current-board Hall proof.
- No firmware logic, runtime API, generated-code hook, build record, flash,
  24V, power-board connection, motor connection, Gate PWM output, Motor
  Profiler, Hall closed-loop, motor readiness, power-stage readiness, or
  sensorless readiness is authorized.

## 2026-05-21 Packet A Generated-Source Review And Build-Only Gate

- Added generated-source side-effect review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-21_001_qiansai_g474_stdrive101_foc_p2_generated_project.md`.
- Decision:
  `Packet A selected fields accepted for no-power configuration evidence /
  build-only source prerequisite satisfied / build execution deferred at the
  time / hardware trust still blocked`.
- Accepted Packet A configuration fields from the 2026-05-21 Workbench
  generated-project clues: `FOC`, `NUCLEO-G474RE`, `STM32G474RETx`,
  `MY-STDRIVE101_POWER_BOARD`, `STDRIVE101`, TIM1 complementary PWM
  `PA8/PA9/PA10 + PB13/PB14/PB15`, `PB12/TIM1_BKIN`, three-shunt current
  sensing, TIM2 Hall `PA15/PB3/PB10`, and USART2 `PA2/PA3` ASPEP/MCP.
- Read-only static checks found no `SIX_STEP`, `sixstep`,
  `mc_tasks_sixstep`, `pwmc_sixstep`, or `speed_duty_ctrl` matches in the
  archived generated-project clue folder.
- At the time of this 2026-05-21 review, the build-only gate source
  prerequisite was satisfied but no no-power build record existed yet. This
  older CLI path blocker is superseded by the 2026-05-27 no-power Debug
  build-only pass recorded at
  `build_only_result_2026-05-27_qiansai_g474_stdrive101_foc_p2_debug.md`.
- The generated Workbench Hall route `PA15/PB3/PB10` still does not match the
  current PCB2 Hall clue `PA0/PA1/PB4`; current PCB2 also records `PB3=LIN1`.
  Hall readiness and current-board route trust remain blocked.
- `R57BLB50L2` remains a temporary Workbench motor placeholder, not measured
  motor evidence.
- No trusted build output, flash, 24V, power-board connection, motor
  connection, Gate PWM output, Motor Profiler, Motor Pilot, Hall closed-loop,
  sensorless / SMO, powered readiness, motor readiness, or power-stage
  readiness is authorized.

## 2026-05-21 Workbench FOC Source Captured For Packet A

- User completed a no-power ST Motor Control Workbench 6.4.2 GUI route for
  `QIANSAI_G474_STDRIVE101_FOC_P2`.
- Archived primary Workbench source:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/QIANSAI_G474_STDRIVE101_FOC_P2_2026-05-21.stwb6`.
- SHA256:
  `05CD6F0DF86276DE10C96CCCFE5AA32E04C9EDE7D8B27E4242D3532D2A126643`.
- Archived user power-board source:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/MY-STDRIVE101_POWER_BOARD.foc_no_power_2026-05-21.json`.
- SHA256:
  `80B655D52D082F89E6CE73804E9A15511D24A9FF3C965494F6A0D98527311B7A`.
- Added source review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/workbench_foc_capture_success_2026-05-21.md`.
- Read-only verification confirms `algorithm: FOC`, `NUCLEO-G474RE`,
  `STM32G474RETx`, `MY-STDRIVE101_POWER_BOARD`, `HallEffectSensor`,
  `speedSensorMode: hall`, `CURRENT_AMPL_U/V/W`, and `DP_TRIGGER` on
  `PB12/TIM1_BKIN`.
- Key GUI unblock: `CURRENT_AMPL_V` had to move from `MR15` to `MR24`; the
  earlier `MR15` route made hardware checks green but kept FOC disabled.
- Driver protection warning was cleared by adding active-low `DP_TRIGGER ->
  MR16`, which Workbench resolves to `PB12/TIM1_BKIN`.
- Workbench also created a local generated-project directory as a GUI side
  effect. Selected source clues were archived under
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-21_qiansai_g474_stdrive101_foc_p2_generated_project/`.
- Decision: `Workbench FOC source captured / no-power Packet A source evidence
  upgraded / hardware and build trust still blocked`.
- No build-only clearance, trusted generated source, powered readiness, Hall
  readiness, Motor Profiler readiness, motor readiness, power-stage readiness,
  or sensorless readiness is upgraded.
- No build, flash, 24V, power-board connection, motor connection, Gate PWM
  output, Motor Profiler, Motor Pilot, Hall closed-loop, or sensorless / SMO
  claim is authorized.

## 2026-05-20 Workbench Short-Name Power Board Alias Added

- User reported that searching `OPAMP` in the Workbench GUI still did not show
  `QIANSAI_STDRIVE101_TIM1_OPAMP_ADAPTER_POWER`.
- Read-only Workbench API check confirmed the long-name candidate was already
  present in `http://localhost:8009/api/hardware/usr/power`; the problem is
  therefore treated as a Workbench GUI search/filter visibility issue, not a
  missing JSON install.
- Added and installed a short-name no-power alias:
  `QS_TIM1_OPAMP_PWR`.
- Repo source:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/QS_TIM1_OPAMP_PWR.no_power_candidate_2026-05-20.json`.
- Workbench user-board install:
  `C:\Users\gregrg\.st_workbench\hardware\board\power\QS_TIM1_OPAMP_PWR.json`.
- SHA256:
  `79BABB221D6F488FB63B79E73B62B9500CEC19BDE96D9FCCB7308A2882B00141`.
- Workbench log confirms:
  `loading Json User Hardware: QS_TIM1_OPAMP_PWR.json` and
  `successfully parsed User Hardware: QS_TIM1_OPAMP_PWR.json`.
- Because the GUI still did not surface the user-library board, the same
  no-power alias was also installed as a local Workbench app asset:
  `F:\STMCSDK\MC_SDK_6.4.2\Utilities\PC_Software\STMCWB\assets\hardware\board\power\QS_TIM1_OPAMP_PWR.json`.
- Workbench was restarted. Read-only verification now shows
  `QS_TIM1_OPAMP_PWR` in `http://localhost:8009/api/hardware/app/power`, and
  the log confirms `successfully parsed assets Hardware:
  QS_TIM1_OPAMP_PWR.json`.
- Next GUI action: from a fresh Workbench `New Project` path, search `QS` in
  the Power Board selector, select `QS_TIM1_OPAMP_PWR`, and stop at the
  summary before `Create`.
- Packet A remains blocked. No `.stwb6`, generated-project trust, build-only
  clearance, trusted generated source, powered readiness, Hall readiness, Motor
  Profiler readiness, motor readiness, power-stage readiness, or sensorless
  readiness is upgraded.
- No Generate, build, flash, 24V, power-board connection, motor connection,
  Gate PWM output, Motor Profiler, Motor Pilot, Hall closed-loop, or
  sensorless / SMO claim is authorized.

## 2026-05-20 Workbench TIM1 Adapter Follow-up Still Blocked

- Added no-power TIM1 adapter follow-up:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/workbench_tim1_adapter_followup_2026-05-20.md`.
- Added no-power candidate board sources:
  `QIANSAI_STDRIVE101_TIM1_ADAPTER_POWER.no_power_candidate_2026-05-20.json`
  and
  `QIANSAI_STDRIVE101_TIM1_OPAMP_ADAPTER_POWER.no_power_candidate_2026-05-20.json`.
- Installed local Workbench user-board candidate:
  `C:\Users\gregrg\.st_workbench\hardware\board\power\QIANSAI_STDRIVE101_TIM1_OPAMP_ADAPTER_POWER.json`.
- GUI evidence shows the `TIM1_ADAPTER` candidate resolves the previous
  `PWM Generation` red X: `PWM Generation`, `Driver Protection`, and UART are
  green in Workbench, while `Current Sensing` remains red and `Create` remains
  disabled.
- Archived follow-up log:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/logs/2026-05-20_connectAlgo_tim1_adapter_pwm_pass_current_sensing_blocked.log`.
- Follow-up log SHA256:
  `3A6109B82EAB2FDF21C97C989640EC8A7F2B99B7B00B312EA6E33A287A583D3C`.
- Current-sense blocker narrowed: current PCB2 clue
  `ADC_U/ADC_V/ADC_W -> PA4/PB0/PA5` is still not accepted by Workbench as the
  G4 internal OPAMP/PGA FOC current-sense route.
- The OPAMP adapter candidate maps current sense to `PA1/PA7/PB0` and PWM to
  `PA8/PA9/PA10 + PB13/PB14/PB15`, but it is only an adapter/rework candidate.
  Its power-board-side current-sense type was corrected to
  `ThreeShunt_RawCurrents_SingleEnded`; Workbench should perform the G474
  OPAMP/PGA mapping during connection. It is not current PCB2 proof and it
  conflicts with the current PCB2 `PA0/PA1/PB4` software-Hall clue.
- GUI reselection of `QIANSAI_STDRIVE101_TIM1_OPAMP_ADAPTER_POWER` remains
  pending. Next no-power GUI action: restart Workbench, select the OPAMP
  adapter candidate, and stop at the summary before `Create`.
- Packet A remains blocked. No `.stwb6`, generated-project trust, build-only
  clearance, trusted generated source, powered readiness, Hall readiness, Motor
  Profiler readiness, motor readiness, power-stage readiness, or sensorless
  readiness is upgraded.
- No Generate, build, flash, 24V, power-board connection, motor connection,
  Gate PWM output, Motor Profiler, Motor Pilot, Hall closed-loop, or
  sensorless / SMO claim is authorized.

## 2026-05-20 Workbench FOC Custom Board Capture Blocked

- Added no-power Workbench FOC capture blocker:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/workbench_foc_capture_blocker_2026-05-20.md`.
- Archived Workbench connection log:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/logs/2026-05-20_connectAlgo_qiansai_pwm_blocker.log`.
- Captured GUI evidence under:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/screenshots/`.
- Decision: `Partial clue / Workbench FOC GUI path reached / Packet A still
  blocked`. Workbench accepted the custom
  `QIANSAI_STDRIVE101_PCB2_POWER` board into the summary and did not use
  `EVALSTDRIVE101`, but `PWM Generation` remained blocked.
- Primary Workbench log error:
  `DrivingHighAndLowSides No timer matches all signals requirement`.
- The saved custom board maps STDRIVE101 PWM to
  `PA15/PB10/PA9/PB3/PA8/PA10`, which cannot form one consistent `TIM1`
  complementary `CH1/CH2/CH3 + CH1N/CH2N/CH3N` set. `PB3` also remains tied to
  the existing SWO/Hall blocker context.
- `R57BLB50L2` was selected only as a user-approved temporary Workbench motor
  placeholder. It is not accepted as measured project motor data.
- No `.stwb6` was saved from this attempt because Workbench left `Create`
  disabled and no valid pre-generate save path was exposed.
- Packet A remains blocked. No generated-project trust, build-only clearance,
  trusted generated source, powered readiness, Hall readiness, Motor Profiler
  readiness, motor readiness, power-stage readiness, or sensorless readiness is
  upgraded.
- No Generate, build, flash, 24V, power-board connection, motor connection,
  Gate PWM output, Motor Profiler, Motor Pilot, Hall closed-loop, or
  sensorless / SMO claim is authorized.

## 2026-05-20 Packet C STDRIVE101 Protection Detail Review

- Added no-power Packet C detail review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_c_stdrive101_protection_detail_review_2026-05-20.md`.
- Updated current task to
  `TASK-2026-05-20-p2-packet-c-stdrive101-protection-detail-review`.
- Evidence ID:
  `EV-2026-05-20-P2-PACKET-C-STDRIVE101-PROTECTION-DETAIL-001`.
- Decision: `Packet C detail narrowed / protection proof still partial clue /
  P3 still blocked`.
- The review narrows `DT/MODE`, `nFAULT`, `REG12`, `CP`, `SCREF`, `VS/VM`,
  bootstrap, `STBY`, and VDS monitoring using the current `.epro`, Gerber,
  current PCB2 mapping note, and repo-local STDRIVE101 extracted text.
- The old `V_DSth = 0.249V` / `I_trip ~= 55A` note is now explicitly not
  accepted as a project threshold. The current local official extraction
  supports `VDSth = VSCREF`; the `33k / 20k` divider gives about `1.245V`, so
  this remains a VDS-monitoring source clue, not a safe current-limit value.
- Packet C remains partial clue. No Packet A acceptance, generated-project
  trust, build-only clearance, continuity proof, powered readiness, Hall
  readiness, Motor Profiler readiness, motor readiness, or sensorless readiness
  is upgraded.
- No Generate, build, flash, 24V, power-board connection, motor connection,
  Gate PWM output, Motor Profiler, Motor Pilot, Hall closed-loop, or
  sensorless / SMO claim is authorized.

## 2026-05-19 Packet A FOC Route Decision After MY_FOC Rollback

- Added no-power Packet A route decision:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_foc_route_decision_2026-05-19.md`.
- Updated current task to
  `TASK-2026-05-19-p2-packet-a-foc-route-decision-after-my-foc-rollback`.
- Evidence ID:
  `EV-2026-05-19-P2-PACKET-A-FOC-ROUTE-DECISION-001`.
- Decision: `Route narrowed / GUI-created FOC source required / Packet A still
  blocked`. The failed `MY_FOC` manual edit now becomes negative evidence:
  do not retry partial `.stwb6` text edits. A valid next Packet A attempt must
  come from Workbench GUI creation/conversion or another complete reviewable
  FOC source.
- Route comparison recorded: legacy `My_First_FOC.stwb6` proves local FOC
  source structure exists but uses built-in `EVALSTDRIVE101`; restored
  `MY_FOC.original_2026-05-19.stwb6` has custom STDRIVE101 board clues but is
  still `"algorithm": "sixStep"`; failed
  `MY_FOC.codex_foc_candidate_2026-05-19.stwb6` must not be reused.
- Next acceptable Packet A capture must show FOC, `NUCLEO-G474RE`, a
  self-developed/custom STDRIVE101 board path, enabled current sensing,
  enabled fault/break handling, and reviewable Hall/PWM choices before any
  generation or build.
- Packet A still blocked. No generated-project trust, no build-only clearance,
  no trusted generated source, no powered readiness, no Hall readiness, no
  Motor Profiler readiness, no motor readiness, no power-stage readiness, and
  no sensorless readiness is upgraded.
- No Generate, build, flash, 24V, power-board connection, motor connection,
  Gate PWM output, Motor Profiler, Motor Pilot, Hall closed-loop, or
  sensorless / SMO claim is authorized.
- Verification: `python -m unittest discover -s tests` passed with 64 tests;
  `git diff --check` passed with LF/CRLF warnings only; `python
  tools/build_vector_store.py` completed with 8291 chunks.

## 2026-05-19 MY_FOC Manual FOC Edit Rollback

- Backed up the Workbench source project:
  `C:\Users\gregrg\.st_workbench\projects\MY_FOC.stwb6`.
- Backup:
  `C:\Users\gregrg\.st_workbench\projects\MY_FOC.stwb6.pre_codex_foc_edit_2026-05-19.bak`.
- Attempted one minimal source-file edit: changed top-level
  `"algorithm": "sixStep"` to `"algorithm": "FOC"`.
- User opened Workbench and reported `娑撯偓閼割剟鏁婄拠?/ 閺冪姵纭堕崝鐘烘祰閺傚洣娆?
  C:/Users/gregrg/.st_workbench/projects/MY_FOC.stwb6`.
- Decision:
  `Manual FOC source edit failed Workbench reload / rolled back / Packet A still not accepted`.
- Rollback completed: external `MY_FOC.stwb6` was restored from the backup and
  now again reads `"algorithm": "sixStep"`.
- Current external `.stwb6` SHA256 matches the backup:
  `062B78AD8E07B5A29A68A007797200FCD4833FE9D3371D2821F3A54D5B9429FD`.
- Archived original/restored and failed FOC-candidate `.stwb6` copies under
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-19_my_foc_generated_project/`.
- Engineering result: do not hand-edit only the top-level `.stwb6` `algorithm`
  field to convert six-step to FOC. Use Workbench GUI flow or create a full
  reviewable FOC `.stwb6` instead.
- Packet A still blocked. No generated-project trust, no build-only clearance,
  no trusted generated source, no powered readiness, no Hall readiness, no
  Motor Profiler readiness, no motor readiness, no power-stage readiness, and
  no sensorless readiness is upgraded.
- No Generate, build, flash, 24V, power-board connection, motor connection,
  Gate PWM output, Motor Profiler, Motor Pilot, Hall closed-loop, or
  sensorless / SMO claim is authorized.
- Verification: `python -m unittest discover -s tests` passed with 61 tests;
  `git diff --check` passed with LF/CRLF warnings only; `python
  tools/build_vector_store.py` completed with 8276 chunks. Read-back confirmed
  external `MY_FOC.stwb6` has `"algorithm": "sixStep"` and matches the backup
  SHA256.

## 2026-05-19 MY_FOC Generated Project Source Review

- Archived selected no-power source files from
  `C:\Users\gregrg\.st_workbench\projects\MY_FOC` under
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-19_my_foc_generated_project/`.
- Added source review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-19_005_my_foc_generated_project.md`.
- Updated current task to
  `TASK-2026-05-19-p2-my-foc-generated-project-source-review`.
- Evidence ID:
  `EV-2026-05-19-P2-MY-FOC-GENERATED-PROJECT-001`.
- Decision: `Partial clue / generated project quarantined / Packet A not
  accepted`. `MY_FOC` proves Workbench 6.4.2 generated a real project on this
  machine, but it is configured as `SIX_STEP`, not FOC.
- Key blockers remain: `M1_CUR_READING=false`,
  `TIM1.BreakState=TIM_BREAK_DISABLE`, generated Hall on `PA15/PB3/PB10`,
  generated PWM on `PA8/PB13/PA9/PB14/PA10/PB15`, and motor placeholder
  `R57BLB50L2` / `MOONS motor for Zest Demo`.
- User clarification recorded: pins can be changed. The Hall/PWM mismatch is
  now treated as a future editable hardware/adapter or Workbench route, not a
  permanent rejection. It still needs a new reviewable FOC configuration and a
  matching physical route before Packet A can be accepted.
- Packet A still blocked. No generated-project trust, no build-only clearance,
  no FOC configuration completion, no firmware trust, no continuity evidence,
  no powered readiness, no Hall readiness, no Motor Profiler readiness, no
  motor readiness, no power-stage readiness, and no sensorless readiness is
  upgraded.
- No build, flash, 24V, power-board connection, motor connection, Gate PWM
  output, Motor Profiler, Motor Pilot, Hall closed-loop, or sensorless / SMO
  claim is authorized.
- Verification: `python -m unittest discover -s tests` passed with 59 tests;
  `git diff --check` passed with LF/CRLF warnings only; `python
  tools/build_vector_store.py` completed with 8265 chunks.

## 2026-05-19 Packet A Board Designer / Manager GUI-Only Checklist

- Added no-power GUI-only checklist:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_board_designer_manager_gui_checklist_2026-05-19.md`.
- Updated current task to
  `TASK-2026-05-19-p2-packet-a-board-designer-manager-gui-checklist`.
- Evidence ID:
  `EV-2026-05-19-P2-PACKET-A-BOARD-DESIGNER-MANAGER-GUI-CHECKLIST-001`.
- Decision: `GUI-only checklist prepared / Packet A still blocked`. The
  checklist tells the user how to capture Board Designer / Board Manager entry,
  custom/import/create board screens, Power/Control/Inverter board flows,
  Board Aggregation, Finalize/save prompt, Board Manager import/list path, and
  blocked states.
- Later screenshots should go under
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-19_board_designer_manager_path/screenshots/`.
- Built-in `EVALSTDRIVE101`, `STEVAL-LVLP01`, and `EVLDRIVE101-HPD` remain
  non-substitutes for the project self-developed STDRIVE101 board. If the GUI
  only exposes those built-in boards or requires source generation / hardware
  actions, the user should capture the blocked screen and stop.
- Packet A still blocked. No generated-project trust, no build-only clearance,
  no custom board source, no `.stwb6`, no firmware, no runtime API, no
  continuity evidence, no powered readiness, no Hall readiness, no Motor
  Profiler readiness, no motor readiness, no power-stage readiness, or no
  sensorless readiness is upgraded.
- No GUI launch occurred in this task. No Generate click, source generation,
  build, flash, 24V, power-board connection, motor connection, Gate PWM output,
  Motor Profiler, Motor Pilot, Hall closed-loop, or sensorless / SMO claim is
  authorized.
- Verification: `python -m unittest discover -s tests` passed with 56 tests;
  `git diff --check` passed with LF/CRLF warnings only; `python
  tools/build_vector_store.py` completed with 8243 chunks.

## 2026-05-19 Packet A Board Designer / Board Manager Path Review

- Added no-power Packet A path review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_board_designer_manager_path_review_2026-05-19.md`.
- Updated current task to
  `TASK-2026-05-19-p2-packet-a-board-designer-manager-path-review`.
- Evidence ID:
  `EV-2026-05-19-P2-PACKET-A-BOARD-DESIGNER-MANAGER-PATH-001`.
- Decision: `Board Designer / Board Manager path exists as local documentation
  and tool clue / Packet A still blocked`. Workbench config references Board
  Designer and Board Manager, the executables exist locally, and the local
  Board Designer manual describes custom board creation/import and board
  aggregation workflows.
- Built-in `EVALSTDRIVE101`, `STEVAL-LVLP01`, and `EVLDRIVE101-HPD` remain
  examples only. They cannot replace evidence for the project self-developed
  STDRIVE101 board.
- Packet A is not accepted. Generated-project trust and build-only
  generated-project clearance remain `Not allowed`. No self-developed board
  definition, `.stwb6`, selected-field screenshot, generated project, build,
  flash, continuity, powered readiness, Hall readiness, Motor Profiler
  readiness, motor readiness, or sensorless readiness is upgraded.
- Next valid Packet A task, if used later, is GUI-only path confirmation and
  screenshot/source capture for a custom/user board; if that cannot be made
  reviewable, the fallback is surrogate build-only planning without
  generated-project trust or separate hardware-rework planning.
- No GUI launch occurred in this review. No source generation, build, flash,
  24V, power-board connection, motor connection, Gate PWM output, Motor
  Profiler, Motor Pilot, Hall closed-loop, or sensorless / SMO claim is
  authorized.
- Verification: `python -m unittest discover -s tests` passed with 53 tests;
  `git diff --check` passed with LF/CRLF warnings only; `python
  tools/build_vector_store.py` completed with 8231 chunks.

## 2026-05-19 Software Hall Adapter Design Review

- Added no-power software Hall adapter design review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/software_hall_adapter_design_review_2026-05-19.md`.
- Updated current task to
  `TASK-2026-05-19-p2-software-hall-adapter-design-review`.
- Evidence ID:
  `EV-2026-05-19-P2-SOFTWARE-HALL-ADAPTER-DESIGN-001`.
- Decision: `Software Hall adapter remains no-power design review / Packet A
  not accepted`. Current PCB2 Hall route remains
  `J_HALL -> IA/IB/IC -> PA0/PA1/PB4`; the review defines only future GPIO/EXTI
  sampling, edge timestamping, valid-state filtering, minimal ISR responsibility,
  and MCSDK integration boundaries.
- Hard stops are explicit: if Workbench / MCSDK requires same-timer hardware
  Hall, if the adapter would invade the high-frequency FOC / JEOC path, or if
  no build-only verification boundary can be defined after accepted Packet A,
  the next step becomes a separate hardware-rework planning task.
- Packet A selected fields remain not accepted. Generated-project trust and
  build-only generated-project clearance remain `Not allowed`. No software Hall
  adapter, runtime API, firmware implementation, generated project, build, flash,
  continuity, powered readiness, Hall readiness, Motor Profiler readiness, motor
  readiness, or sensorless readiness is upgraded.
- No GUI launch, source generation, build, flash, 24V, power-board connection,
  motor connection, Gate PWM output, Motor Profiler, Hall closed-loop, or
  sensorless / SMO claim is authorized.
- Verification: `python -m unittest discover -s tests` passed with 50 tests;
  `git diff --check` passed with LF/CRLF warnings only; `python
  tools/build_vector_store.py` completed with 8209 chunks.

## 2026-05-19 Current PCB2 Packet A / Firmware Feasibility Review

- Added no-power feasibility review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/current_pcb2_packet_a_firmware_feasibility_2026-05-19.md`.
- Updated current task to
  `TASK-2026-05-19-p2-current-pcb2-packet-a-firmware-feasibility`.
- Evidence ID:
  `EV-2026-05-19-P2-CURRENT-PCB2-PACKET-A-FIRMWARE-FEASIBILITY-001`.
- Decision: `No-PCB-change route remains feasibility only / Packet A not
  accepted`. Current PCB2 `HIN/LIN` route is not cleared as a standard MCSDK
  `TIM1` complementary PWM selected-field claim, and `PA0/PA1/PB4` is not
  cleared as a same-timer hardware Hall interface.
- The no-PCB-change path remains open only as a later no-power firmware design
  review for software Hall sampling, edge timestamping, valid-state filtering,
  and MCSDK integration boundaries.
- Packet A remains not accepted. Generated-project trust and build-only
  generated-project clearance remain `Not allowed`.
- Hardware rework is not executed or decided in this task; it remains a
  fallback if Workbench/firmware feasibility fails.
- No GUI launch, source generation, build, flash, 24V, power-board connection,
  motor connection, Gate PWM output, Motor Profiler, Hall closed-loop, or
  sensorless / SMO claim is authorized.
- Verification: `python -m unittest discover -s tests` passed with 47 tests;
  `git diff --check` passed with LF/CRLF warnings only; `python
  tools/build_vector_store.py` completed.

## 2026-05-19 Current PCB2 Hall/PWM No-Power Strategy Review

- Added no-power strategy review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/current_pcb2_hall_pwm_strategy_2026-05-19.md`.
- Updated current task to
  `TASK-2026-05-19-p2-current-pcb2-hall-pwm-strategy`.
- Evidence ID:
  `EV-2026-05-19-P2-CURRENT-PCB2-HALL-PWM-STRATEGY-001`.
- Decision: `No-power strategy review opened / no PCB change first`. The
  current PCB2 PWM / driver-input route under review is
  `HIN1/LIN1/HIN2/LIN2/HIN3/LIN3 -> PA15/PB3/PB10/PA8/PA9/PA10`, and the
  current PCB2 Hall route remains `J_HALL -> IA/IB/IC -> PA0/PA1/PB4`.
- The old standard `TIM1` complementary PWM draft and the old
  `PA15/PB3/PB10` hardware Hall draft are now historical or alternate
  candidates only. They are not accepted current PCB2 configuration evidence.
- `PA0/PA1/PB4` is not accepted as a same-timer hardware Hall set. This task
  records only software Hall feasibility review as a future no-power Packet A /
  firmware design topic; it does not upgrade Hall readiness.
- `PB3` is current PCB2 `LIN1`, not current PCB2 `HALL_B`. Any alternate use
  of `PB3` as Hall still needs SWO release/isolation and a new accepted route.
- Packet A remains `Partial clue / Preparation only / stopped`;
  generated-project trust remains `Not allowed`; build-only generated-project
  work remains closed.
- No GUI launch, source generation, build, flash, 24V, power-board connection,
  motor connection, Gate PWM output, Motor Profiler, Hall closed-loop, or
  sensorless / SMO claim is authorized.
- Verification: `python -m unittest discover -s tests` passed with 44 tests;
  `git diff --check` passed with LF/CRLF warnings only; `python
  tools/build_vector_store.py` built 8175 chunks. The project dry-run no-power
  safety scan was not completed because the tool platform rejected the call
  with a usage-limit message; it was not bypassed.

## 2026-05-19 PCB2 Mapping / Pin-1 / Protection Intake

- Archived user-provided current PCB2 mapping and pin-1 source packet under:
  `hardware/schematic/2026-05-19_pcb2_mapping_pin1_protection/`.
- Added no-power Packet B/C plus PB3/SWO/Hall source review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-19_004_pcb2_mapping_pin1_protection.md`.
- Updated current task to
  `TASK-2026-05-19-p2-pcb2-mapping-pin1-protection-intake`.
- Evidence ID:
  `EV-2026-05-19-P2-PCB2-MAPPING-PIN1-PROTECTION-001`.
- Decision: `Partial clue / accepted current PCB2 mapping source; Hall/PWM
  conflicts clarified`. The user states the answer corresponds to current
  PCB2. The packet provides P1-P15 mapping, connector-orientation images, Hall
  relationship, PB3/SWO handling, and STDRIVE101 `DT/MODE` / `CP` / `SCREF` /
  `nFAULT` / `STBY` statements.
- Latest clarification: `PC7/PB3/PB10` was an alternate suggestion, not current
  PCB2 physical routing. Current PCB2 Hall routing is
  `J_HALL -> IA/IB/IC -> PA0/PA1/PB4`; `IA/IB/IC` are Hall signal nets after
  pull-up/filtering, and `ADC_U/ADC_V/ADC_W` are current-sense nets.
- `PB3` is `LIN1`, not current PCB2 `HALL_B`; `PB10` is `HIN2`, not current
  PCB2 `HALL_C`. The remaining blocker is now software/Workbench strategy:
  current Hall inputs `PA0/PA1/PB4` are not a normal three-channel hardware
  Hall timer set and need a no-power Packet A / firmware design decision.
- Generated-project trust remains `Not allowed`. Packet A selected fields,
  no-power continuity, powered readiness, motor readiness, Hall readiness,
  Motor Profiler readiness, and sensorless readiness remain unchanged.
- No 24V, power-board connection, motor connection, Gate PWM output, Motor
  Profiler, source generation, build, flash, Hall closed-loop, or sensorless /
  SMO claim is authorized.
- Verification passed: `python -m unittest discover -s tests` ran 41 tests OK
  after restoring the required `does not release SWO` boundary phrase;
  `git diff --check` passed with line-ending warnings only; the project dry-run
  no-power safety scan reported no unsafe added claims; `python
  tools/build_vector_store.py` rebuilt the local index with 8160 chunks.

## 2026-05-19 P2 Minimal Hardware Request And Workbench Asset Probe

- Added the short hardware-teammate request:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/hardware_teammate_min_request_2026-05-19.md`.
- Added the read-only Packet A Workbench asset probe:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_workbench_asset_probe_2026-05-19.md`.
- Updated current task to
  `TASK-2026-05-19-p2-min-hw-request-workbench-asset-probe`.
- Evidence ID:
  `EV-2026-05-19-P2-MIN-HW-REQ-WB-ASSET-PROBE-001`.
- Decision: workflow/evidence-governance only. The minimal request narrows the
  next hardware-teammate packet to three P0 items first: exact Gerber PCB2
  revision confirmation, complete `CN3 -> NUCLEO/CN8 -> STM32 pin` mapping,
  and marked `CN3` / `J_HALL` pin-1 evidence.
- Packet A local asset probe found installed Board Designer and Board Manager
  executables referenced by Workbench config, plus built-in STDRIVE101 board
  JSON definitions. This is only a local path clue; no accepted custom
  self-developed STDRIVE101 board definition, project-specific `.stwb6`, or
  selected-field screenshot exists.
- Generated-project trust remains `Not allowed`. Packet A/B/C, PB3/SWO,
  `J_HALL`, continuity, powered readiness, motor readiness, Hall readiness,
  Motor Profiler readiness, and sensorless readiness remain unchanged.
- No 24V, power-board connection, motor connection, Gate PWM output, Motor
  Profiler, source generation, build, flash, Hall closed-loop, or sensorless /
  SMO claim is authorized.
- Verification passed: `python -m unittest discover -s tests` ran 41 tests OK;
  `git diff --check` passed with line-ending warnings only; the project dry-run
  no-power safety scan reported no unsafe added claims; `python
  tools/build_vector_store.py` rebuilt the local index with 8133 chunks.

## 2026-05-19 P2 Hardware Supplement Handoff

- Added hardware-teammate handoff:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/hardware_supplement_handoff_2026-05-19.md`.
- Updated current task to
  `TASK-2026-05-19-p2-hardware-supplement-handoff`.
- Evidence ID:
  `EV-2026-05-19-P2-HARDWARE-SUPPLEMENT-HANDOFF-001`.
- Decision: workflow/evidence-governance only. The handoff converts the
  latest `.epro` and Gerber follow-up blockers into exact hardware teammate
  requests: Gerber exact revision confirmation,
  `CN3 -> NUCLEO/CN8 -> STM32 pin` mapping, `CN3` / `J_HALL` pin-1
  orientation, Hall A/B/C mapping, PB3/SWO release or alternate Hall B route,
  STDRIVE101 `DT/MODE` / `STBY` / `CP` / `SCREF` / `NFAULT` protection-chain
  details, optional EasyEDA Pro PCB source, and later no-power continuity /
  short-check records.
- Packet A remains `Partial clue / Preparation only / stopped`;
  generated-project trust remains `Not allowed`.
- Packet B/C still has accepted board-side schematic + Gerber/flying-probe
  clues only; NUCLEO `CN8`, STM32 endpoint mapping, connector orientation,
  continuity, powered readiness, motor readiness, Hall readiness, and
  sensorless readiness remain not allowed.
- No 24V, power-board connection, motor connection, Gate PWM output, Motor
  Profiler, source generation, build, flash, Hall closed-loop, or sensorless /
  SMO claim is authorized.
- Verification passed: `python -m unittest discover -s tests` ran 41 tests OK;
  `python tools/build_vector_store.py` rebuilt the local index with 8110
  chunks.

## 2026-05-19 Gerber PCB2 Manufacturing Package Intake

- Archived hardware-teammate supplied Gerber package:
  `hardware/schematic/2026-05-19_gerber_pcb2_stdrive101/Gerber_PCB2_2026-05-19.zip`.
- Added no-power Packet B/C Gerber review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-19_003_gerber_pcb2.md`.
- Decision: `Partial clue / accepted board-side Gerber + flying-probe net
  clue`. The ZIP contains a four-layer EasyEDA Pro Gerber manufacturing
  package plus drill files and `FlyingProbeTesting.json`; Gerber headers record
  `EasyEDA Pro v3.2.91`, generated `2026-05-19 11:16:57`, and the archived
  ZIP hash is
  `F61C073C5A9E71CD608460976430D3F927E7AD48EC05A42661E77662AF04CE56`.
- Accepted exact board-side clues: `CN3` 15-pin pad/net mapping, `U1`
  STDRIVE101 pad nets, PWM input paths through `R4-R9`, `R12/R14/R17`
  shunt/current-sense pad nets, `U2=J_HALL` pad-net clue, `CN2=J_MOTOR`,
  `NFAULT -> R3 -> 3V3 / CN3_13`, `SCREF` divider, `REG12`, bootstrap, and
  `OUT1/2/3` motor output pad nets.
- Still blocked: exact fabrication/revision match confirmation, NUCLEO `CN8`
  endpoint mapping, STM32 pin mapping, PB3/SWO release, `J_HALL` physical
  pin-1 / Hall A/B/C numbering, Packet A/Workbench selected fields,
  generated-project trust, continuity checks, power-stage readiness, Motor
  Profiler readiness, motor readiness, and sensorless readiness.

## 2026-05-19 ProDoc P1 EDA Pro Source Intake

- Archived user-confirmed self-developed STDRIVE101 driver-board source:
  `hardware/schematic/2026-05-19_prodoc_p1_stdrive101_epro/ProDoc_P1_2026-05-19.epro`.
- Added no-power Packet B/C source review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-19_002_prodoc_p1_epro.md`.
- Decision: `Partial clue / accepted schematic-source clue`. The `.epro`
  is a readable EDA Pro schematic source with one sheet, project/title-block
  metadata `STDRIVE101_3Phase_Inverter`, create/update time
  `2026-05-19 10:26:36`, and source hash
  `B9D67B9E5D6DD08D5229928636DFA8048C081DED7EE230ADDB79F20D83D718A1`.
- Accepted exact clues: `U1=STDRIVE101`, `Q1-Q6=NCEP40T11G`, three
  `20mOhm` shunts, `CN3` 15-pin board-side control connector, `U2=J_HALL`,
  `CN2=J_MOTOR`, `CN3` pinout, and visible `NFAULT`, `REG12`, `SCREF`,
  `BOOTx`, `OUTx`, `GHSx`, and `GLSx` schematic nets.
- The archive has no PCB layout evidence: `project.json` has `pcbs: {}`, the
  board entry has an empty `pcb` field, and `PCB/` is only an empty directory
  entry. PCB routing, NUCLEO `CN8` endpoint mapping, STM32 pin mapping,
  PB3/SWO release, `J_HALL` numbering, Hall readiness, power-stage readiness,
  Packet A/Workbench selected fields, generated-project trust, Motor Profiler
  readiness, motor readiness, and sensorless readiness remain unchanged and
  not allowed.

## 2026-05-19 Packet A Workbench Capture Attempt

- Added no-power Packet A Workbench capture-attempt review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-19_001_packet_a_workbench_capture_attempt.md`.
- Captured Workbench 6.4.2 launch and board-selection screenshots under:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/screenshots/`.
- Decision: `Partial clue / stopped`. Workbench launches and the component path
  can show `NUCLEO-G474RE` / `STM32G474RETx` as the control-board context, but
  no accepted Custom / Generic self-made STDRIVE101 power-stage context was
  captured.
- User clarified on 2026-05-19 that the project uses a self-developed motor
  driver board based on the STDRIVE101 chip. Therefore built-in ST power-board
  entries such as `EVALSTDRIVE101` or `STEVAL-LVLP01` cannot be treated as
  board-match substitutes for Packet A.
- No project-specific `.stwb6`, no selected-field PWM/current-sense/Hall/driver
  protection/pin-usage screenshots, and no generated motor-control project were
  created. Generated-project trust remains `Not allowed`.
- Packet A remains `Partial clue / Preparation only`; Packet B/C, CN8 routing,
  STDRIVE101 protection-path proof, PB3/SWO release, `J_HALL`, Hall readiness,
  power-stage readiness, Motor Profiler readiness, motor readiness, and
  sensorless readiness remain unchanged. No 24V, power-board connection, motor
  connection, Gate PWM, Motor Profiler, build, flash, or generated
  motor-control project is authorized.

## 2026-05-18 PB3 / SWO CubeMX Probe

- Added no-power PB3/SWO source-packet review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-18_002_pb3_swo_probe.md`.
- Captured current CubeMX state screenshot:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/2026-05-18_cubemx_pb3_current_swo_fullscreen.png`.
- Added dated configuration-layer probe:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_no_power_nucleo_g474re_draft/pb3_tim2_ch2_probe_2026-05-18.ioc`.
- Captured probe screenshot:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/2026-05-18_cubemx_pb3_tim2_ch2_probe_fullscreen.png`.
- Decision: `Partial clue` only. The accepted NUCLEO draft still records
  `PB3.GPIO_Label=T_SWO` and `PB3.Signal=SYS_JTDO-SWO`; the probe copy can show
  `PB3` as `TIM2_CH2` / `HALL_B_PROBE` in CubeMX, but it does not prove SWO
  release / isolation, Workbench Hall B selection, CN8 / `J_HALL` endpoint
  mapping, or Hall readiness.
- Packet A/B/C, generated-project trust, CN8 routing, STDRIVE101
  protection-path proof, Hall closed-loop, power-stage readiness, Motor
  Profiler readiness, motor readiness, and sensorless readiness remain
  unchanged. No 24V, power-board connection, motor connection, Gate PWM,
  Motor Profiler, build, flash, or generated motor-control project is
  authorized.

## 2026-05-18 Motor Wiring Definition Intake

- Added user-provided motor wiring definition source:
  `hardware/motor/2026-05-18_57blf01_motor_wiring_definition.jpg`.
- Added extracted wiring note:
  `hardware/motor/2026-05-18_57blf01_motor_wiring_definition.md`.
- Added P2 source-packet review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-18_001_motor_wiring_definition.md`.
- Updated no-power motor log:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/motor_no_power_measurement_log_2026-05-16.md`.
- Extracted candidate wire colors: phase `U` = yellow thick wire, `V` = red
  thick wire, `W` = black thick wire; Hall `HU` = yellow thin wire, `HV` =
  white thin wire, `HW` = blue thin wire, `H+` / `+5V` = red thin wire, and
  `H-` / `GND` = black thin wire.
- Decision: `Partial clue` only. This source helps future Workbench notes and
  no-power wiring labels, but it does not prove physical harness inspection,
  continuity, Hall powered behavior, phase/Hall alignment, `J_HALL` numbering,
  Motor Profiler data, or motor readiness.
- No 24V, power-board connection, motor connection, Gate PWM, Motor Profiler,
  Hall closed-loop, or sensorless / SMO claim is authorized.

## 2026-05-18 Packet A Capture Task Package Refresh

- Added workflow-only Packet A capture task package:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_capture_task_2026-05-18.md`.
- Updated `workflow/ACTIVE_TASK.md` to point at the P2 Packet A capture
  preparation task with `open/ready` status and a no-GUI, no-generation,
  no-build, no-flash, no-hardware boundary.
- Refreshed P2 entry points:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/p2_readiness_snapshot_2026-05-15.md`
  and `apps/stm32_g474_foc/mcsdk_no_power_precheck/README.md`.
- Registered workflow-only evidence:
  `EV-2026-05-18-P2-PACKET-A-TASK-PACKAGE-001`.
- Verification passed: `python -m unittest discover -s tests` ran 41 tests OK;
  `python tools\build_vector_store.py` rebuilt the local index successfully.
- Decision unchanged: Packet A remains `Partial clue / Preparation only`;
  generated-project trust remains `Not allowed`; Packet B/C, `PB3` / SWO,
  `J_HALL`, CN8 routing, and STDRIVE101 protection-path blockers remain open.
- This update does not create a new `.stwb6`, does not add Workbench
  screenshots, does not launch Workbench, does not generate or build source,
  and does not authorize 24V, power-board connection, motor connection, Gate
  PWM, Motor Profiler, Hall closed-loop, or sensorless / SMO claims.

## 2026-05-17 Vendor Motor And Hardware Pin Table Intake

- Added supplier motor-parameter source:
  `hardware/motor/2026-05-17_vendor_57blf01_motor_parameters.jpg`.
- Added extracted motor review note:
  `hardware/motor/2026-05-17_vendor_57blf01_motor_parameters.md`.
- Added hardware teammate pin-assignment PDF:
  `hardware/schematic/2026-05-17_stm32g431rb_pin_assignment_hw_teammate.pdf`.
- Added extracted pin-table review note:
  `hardware/schematic/2026-05-17_stm32g431rb_pin_assignment_hw_teammate.md`.
- Added source-packet review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-17_001_vendor_motor_g431_pin_table.md`.
- Added MCU pin compatibility cross-check:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/mcu_pin_compatibility_check_2026-05-17.md`.
- Decision: `Partial clue` only. The motor values are supplier clues, not
  project measurements or Motor Profiler results. The pin table is titled for
  `STM32G431RB`, but the hardware teammate says the relevant G431/G474 pins are
  the same; local MCSDK `STM32G431RBTx` / `STM32G474RETx` asset comparison
  supports the compared key TIM1, TIM2, USART, and OPAMP-capable rows.
- `J_HALL` pin numbering is explicitly uncertain. Hall A/B/C rows remain
  candidate or blocked until board source or continuity evidence confirms the
  connector. CN8 endpoint proof and `PB3` / SWO release remain separate
  blockers.
- If Workbench requires a motor entry, the preferred no-power label is now
  `57BLF01_VENDOR_CANDIDATE`, replacing the generic placeholder name only as a
  label. It does not upgrade motor parameters to accepted measurements.
- Generated-project trust remains `Not allowed`; no 24V, power-board
  connection, motor connection, Gate PWM, Motor Profiler, Hall closed-loop, or
  sensorless / SMO claim is authorized.

## 2026-05-16 Packet A Custom Workbench Capture Package

- Added the new project-specific Packet A capture package:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-16_custom_nucleo_stdrive101/`.
- Added hand-run Workbench guide:
  `workbench_no_power_configuration_guide_2026-05-16.md`.
- Added no-power motor measurement template:
  `motor_no_power_measurement_log_2026-05-16.md`.
- Added pin assignment table:
  `pin_assignment_table_2026-05-16.md`.
- Added preparation review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-16_001_custom_nucleo_stdrive101_capture_package.md`.
- User clarified that `My_First_FOC.stwb6` is a previous toolchain-learning
  leftover and that its `EVALSTDRIVE101` power-board choice is arbitrary. It
  remains preserved as a legacy `Partial clue` only and is not the source for
  the new project-specific Packet A path.
- New intended capture target: `NUCLEO-G474RE` / `STM32G474RETx`, Custom /
  Generic STDRIVE101 power stage, FOC, Hall fallback, 3-shunt current sensing,
  motor label `57BLF01_VENDOR_CANDIDATE` if Workbench requires a motor entry,
  and no generated source. The older `PLACEHOLDER_not_profiled_2026-05-16`
  name is superseded as the preferred label, not upgraded into measured motor
  proof.
- Generated-project trust remains `Not allowed`. The 2026-05-16 package
  prepares GUI capture and review, but no new `.stwb6` or selected-field
  Workbench screenshot has been accepted yet.
- Motor information collection is limited to no-power records: nameplate photo,
  wire colors, and multimeter phase-to-phase resistance clues. These are not
  Motor Profiler data and do not authorize motor connection, Hall powering, or
  closed-loop use.

## 2026-05-15 Packet A STWB6 Candidate Intake

- Found the real ST MC Workbench 6.4.2 launcher:
  `F:\STMCSDK\MC_SDK_6.4.2\Utilities\PC_Software\STMCWB\STMCWB.exe`.
- Found and preserved a local MCSDK 6 Workbench project candidate:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_sources/2026-05-15_my_first_foc/My_First_FOC.stwb6`.
- Added Packet A review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-15_002_my_first_foc_stwb6.md`.
- Review decision: `Partial clue`. The file records Workbench 6.4.2, FOC,
  `NUCLEO-G474RE`, `STM32G474RETx`, `EVALSTDRIVE101`, and `R57BLB50L2`, but it
  is not accepted final evidence for the custom power board, selected TIM1 PWM,
  final fault input, current-sense mode, Hall/sensorless mode, `PA2/PA3`
  policy, or `PB3` ownership.
- Updated Packet A wording to accept MCSDK 6 `.stwb6` project files as the
  current Workbench format; legacy `.stmcx` remains valid only for older
  Workbench sources.
- Generated-project trust remains `Not allowed`. This update does not prove
  CN8 routing, STDRIVE101 protection paths, power-stage readiness, Hall
  readiness, Gate PWM, Motor Profiler, motor behavior, or sensorless behavior,
  and it does not authorize 24V, power-board connection, motor connection,
  flashing, Gate PWM, Motor Profiler, Hall closed-loop, or sensorless FOC
  claims.

## 2026-05-15 Phase Gate P2 Insert

- Updated phase gate checklist:
  `workflow/phase_gate_checklist.md`.
- The phase gate now explicitly blocks jumping from NUCLEO basics directly to
  Motor Profiler or generated-project trust. It adds `P2-S1 - MCSDK No-Power
  Precheck`, `P2-S2 - Build-Only Generated Project Gate`, and a `P2 To P3
  Blocker List`.
- Current decision is unchanged: Packet A must be accepted before build-only
  generated-project work; Packet B/C, PB3/SWO, no-power continuity checks,
  current-limited bring-up settings, measurement points, stop conditions, and a
  rollback image are required before P3 powered work can open.
- This update is workflow gating only. It does not prove MCSDK MotorControl
  configuration, generated-project trust, CN8 routing, STDRIVE101
  protection-path proof, power-stage readiness, Hall readiness, Gate PWM, Motor
  Profiler, motor behavior, or sensorless behavior, and it does not authorize
  24V, power-board connection, motor connection, Gate PWM, Motor Profiler, Hall
  closed-loop, or sensorless FOC claims.

## 2026-05-15 P2 Readiness Snapshot

- Added P2 readiness snapshot:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/p2_readiness_snapshot_2026-05-15.md`.
- At that snapshot time, P2 no-power planning remained in progress, Packet A
  had no accepted selected-field source, generated-project trust was
  `Not allowed`, Packet B/C and PB3/SWO remained blocked or partial clue only,
  and P3 powered or motor work was not allowed. This has since been refined by
  the 2026-05-15 legacy `.stwb6` partial clue review and the 2026-05-16 custom
  capture package preparation, while generated-project trust remains
  `Not allowed`.
- The snapshot does not prove MCSDK MotorControl configuration,
  generated-project trust, CN8 routing, STDRIVE101 protection-path proof,
  power-stage readiness, Hall readiness, Gate PWM, Motor Profiler, motor
  behavior, or sensorless behavior, and it does not authorize 24V, power-board
  connection, motor connection, Gate PWM, Motor Profiler, Hall closed-loop, or
  sensorless FOC claims.

## 2026-05-15 STM32 Signal Contract And Build-Only Gate

- Added STM32-side signal contract:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stm32_side_signal_contract_2026-05-15.md`.
- Added future build-only gate:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/future_build_only_gate_2026-05-15.md`.
- The signal contract records future STM32 responsibilities for TIM1 PWM
  commands, `NFAULT`, `STBY`, `DT/MODE`, current sensing, Hall fallback,
  `PA2/PA3`, `PB3`, `3V3`, `GND_SIGNAL`, and ESP32 gateway boundaries. All
  hardware-dependent items remain blocked or candidate-only until Packet A/B/C
  or PB3/SWO evidence proves them.
- The build-only gate records that generated-project trust is currently
  `Not allowed` because Packet A is only `Partial clue`. Even after Packet A selected fields are accepted,
  a generated MCSDK project may only be treated as no-power build evidence
  until later hardware phase gates exist.
- This update does not prove MCSDK MotorControl configuration,
  generated-project trust, CN8 routing, STDRIVE101 protection-path proof,
  power-stage readiness, Hall readiness, Gate PWM, Motor Profiler, motor
  behavior, or sensorless behavior, and it does not authorize 24V, power-board
  connection, motor connection, Gate PWM, Motor Profiler, Hall closed-loop, or
  sensorless FOC claims.

## 2026-05-15 Packet A Local Probe

- Added Packet A local probe:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_local_probe_2026-05-15.md`.
- Added Packet A capture checklist:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_capture_checklist_2026-05-15.md`.
- Current result: checked repo `.stmcx`, existing screenshots,
  `apps/stm32_g474_foc/MotorControl`, `F:\STMCubeMX`,
  `C:\Users\gregrg\STM32Cube\Repository`, `C:\Users\gregrg\.stm32cubemx`, and
  common user locations (`Documents`, `Downloads`, `Desktop`). No real
  `.stmcx` and no MotorControl / Workbench configuration screenshot were found.
  Direct search of `C:\Users\gregrg` returned access denied, so this is a
  bounded local probe, not an all-disk proof.
- Packet A was not accepted by this local probe alone. It later gained only a
  legacy `.stwb6` `Partial clue` and a 2026-05-16 custom capture package
  preparation. This still does not prove MCSDK MotorControl configuration,
  generated-project trust, CN8 routing, STDRIVE101 protection-path proof,
  power-stage readiness, Hall readiness, Gate PWM, Motor Profiler, motor
  behavior, or sensorless behavior, and it does not authorize 24V, power-board
  connection, motor connection, Gate PWM, Motor Profiler, Hall closed-loop, or
  sensorless FOC claims.

## 2026-05-15 P2 Non-Hardware Parallel Track

- Added non-hardware parallel track:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/non_hardware_parallel_track_2026-05-15.md`.
- User asked to skip the hardware source package branch for now. The repo now
  records this as "skipped for scheduling, not cleared": Packet B/C, `DT/MODE`,
  `STBY`, STM32 endpoint mapping, and `PB3` / SWO release remain blocked.
- Allowed parallel work is now explicit: Packet A MCSDK / MotorControl evidence,
  STM32-side signal contract, future build-only gate, and submission/evidence
  cleanup.
- This update does not prove `.stmcx`, MotorControl configuration, CN8 routing,
  STDRIVE101 protection paths, power-stage readiness, Hall readiness, Gate PWM,
  Motor Profiler, motor behavior, or sensorless behavior, and it does not
  authorize 24V, power-board connection, motor connection, Gate PWM, Motor
  Profiler, Hall closed-loop, or sensorless FOC claims.

## 2026-05-15 P2 Schematic Candidate Intake

- Imported the user-provided schematic screenshot as a preserved P2 hardware
  source candidate:
  `hardware/schematic/2026-05-15_power_board_cn8_stdrive101_schematic_candidate.png`.
- Added source note:
  `hardware/schematic/2026-05-15_power_board_cn8_stdrive101_schematic_candidate.md`.
- Added review record:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_2026-05-15_001_cn8_stdrive101_schematic_candidate.md`.
- Current decision: `Partial clue`. The screenshot can guide Packet B/C review
  because it shows CN8 labels, STDRIVE101, input resistors, `nFAULT`, `REG12`,
  `CP`, `SCREF`, bootstrap clues, MOSFETs, shunts, and Hall interface clues.
  User confirmed on 2026-05-15 that it is the current physical power board and
  was drawn by the hardware teammate. It still lacks a formal title-block
  source revision/date, STM32-side CN8-to-MCU pin mapping, accepted `DT/MODE`
  endpoint proof, and `STBY` proof.
- This update does not prove CN8 routing, STDRIVE101 protection paths, MCSDK
  MotorControl configuration, power-stage readiness, Hall readiness, Gate PWM,
  Motor Profiler, motor behavior, or sensorless behavior, and it does not
  authorize 24V, power-board connection, motor connection, Gate PWM, Motor
  Profiler, Hall closed-loop, or sensorless FOC claims.

## 2026-05-14 P2 Source Packet Review Template

- Added repeatable source packet review template:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_review_template_2026-05-14.md`.
- The template defines the Codex-side review path after Packet A, Packet B,
  Packet C, or `PB3` / SWO evidence arrives: Accept, Partial clue, or Reject;
  then update only the exact proven fields.
- This is a no-power review-control artifact only. It does not add `.stmcx`,
  MotorControl screenshot, CN8 / EDA / netlist evidence, STDRIVE101
  protection-path proof, or any hardware validation, and it does not authorize
  24V, power-board connection, motor connection, Gate PWM, Motor Profiler, Hall
  closed-loop, or sensorless FOC claims.

## 2026-05-14 P2 User Action Queue

- Added direct user action queue:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/user_action_queue_2026-05-14.md`.
- The queue tells the user exactly what to provide next: first Packet B
  current-version CN8 / board-route / STDRIVE101 source evidence, then Packet A
  MCSDK / MotorControl `.stmcx` or screenshot evidence, plus `PB3` / SWO release
  evidence if Hall B remains planned.
- This is a handoff and intake artifact only. It does not prove MCSDK
  MotorControl configuration, does not prove CN8 routing, does not prove
  STDRIVE101 protection paths, and does not authorize 24V, power-board
  connection, motor connection, Gate PWM, Motor Profiler, Hall closed-loop, or
  sensorless FOC claims.

## 2026-05-14 P2 Source Packet Request Pack

- Added concrete source packet request pack:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_request_pack_2026-05-14.md`.
- The request pack turns the intake checklist into three handoff packets:
  MCSDK / MotorControl configuration evidence, CN8 / board-route evidence, and
  board-level STDRIVE101 protection-path evidence.
- It records required fields, rejected sources, Codex review steps, and the
  current blocked state for `.stmcx`, MotorControl screenshots, CN8 / EDA /
  netlist evidence, STDRIVE101 protection paths, and `PB3` Hall/SWO ownership.
- This is a handoff artifact only. It does not add board evidence, does not
  prove MCSDK MotorControl configuration, does not prove CN8 routing or
  STDRIVE101 protection paths, and does not authorize 24V, power-board
  connection, motor connection, Gate PWM, Motor Profiler, Hall closed-loop, or
  sensorless FOC claims.

## 2026-05-14 P2 Source Packet Intake 闂傤厾骞?
- Added P2 source packet intake checklist:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/source_packet_intake_checklist_2026-05-14.md`.
- The checklist defines accepted evidence packets for MCSDK `.stmcx` /
  MotorControl screenshots, CN8 / EDA / netlist / high-resolution route
  evidence, and board-level STDRIVE101 protection-path source evidence.
- It also rejects low-resolution screenshots, oral descriptions, old or
  unknown-version files, incomplete crops, generated source without matching
  configuration evidence, and the excluded WeChat-side `netlist_PADS.net`
  candidate.
- This is an evidence-entry rule only. It does not prove MCSDK MotorControl
  configuration completion, CN8 routing, STDRIVE101 protection paths,
  power-stage readiness, Hall readiness, or sensorless readiness, and it still
  does not authorize 24V, power-board connection, motor connection, Gate PWM,
  Motor Profiler, Hall closed-loop, or sensorless FOC claims.

## 2026-05-14 P2 STDRIVE101 娣囨繃濮㈢捄顖氱窞鐎光剝鐓?
- Added STDRIVE101 protection-path review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_protection_path_review_2026-05-14.md`.
- The review fixes the required P2 checklist for `DT/MODE`, `nFAULT`,
  `REG12`, `CP`, `SCREF`, `VS/VM`, bootstrap, standby, and VDS monitoring.
- ST official product page and datasheet (`DS13472 Rev 2`, June 2022) were
  rechecked on 2026-05-14. The official source still describes STDRIVE101 as a
  triple half-bridge gate driver with two input strategies selected by
  `DT/MODE`, 12 V `REG12` gate supply, overcurrent comparator, VDS monitoring,
  UVLO, thermal shutdown, and standby behavior.
- The existing schematic screenshot remains only a low-grade clue. It does not
  prove CN8 routing, PCB routing, connector pinout, STDRIVE101 protection-path
  correctness, or power-stage readiness.
- This update still does not authorize 24V, power-board connection, motor
  connection, Gate PWM, Motor Profiler, Hall closed-loop, or sensorless FOC
  claims.

## 2026-05-14 P2 Parallel Evidence Push

- Added CN8 / STDRIVE101 route review:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/cn8_stdrive101_route_review_2026-05-14.md`.
- Rechecked the `.stmcx` / MotorControl side: repo search still found no
  `.stmcx`; narrow checks of `F:\STMCubeMX`,
  `C:\Users\gregrg\STM32Cube\Repository\MCSDK_v6.4.2-Full`, and VS Code
  extension folders still did not prove a saved Workbench project, standalone
  Workbench launcher, or MotorControl configuration page.
- Route review now explicitly accepts only current-version EDA, schematic PDF,
  netlist, or high-resolution route crop as board-route evidence. The existing
  schematic screenshot remains a low-grade clue only.
- The WeChat-side `netlist_PADS.net` candidate was not imported and is not used
  as current board evidence.
- Current blockers remain: real `.stmcx` or MotorControl configuration
  screenshot; accepted CN8 / route evidence; accepted STDRIVE101 `nFAULT`,
  `DT/MODE`, `REG12`, `CP`, `SCREF`, `VS/VM`, bootstrap, standby, and VDS
  monitoring source evidence.
- This update still does not authorize 24V, power-board connection, motor
  connection, Gate PWM, Motor Profiler, Hall closed-loop, or sensorless FOC
  claims.

## 2026-05-14 P2 GUI 闁板秶鐤嗙拠浣瑰祦閹恒劏绻?
- Codex 娴ｈ法鏁?`F:\STMCubeMX\STM32CubeMX.exe` 閹垫挸绱戝韫箽鐎涙娈?NUCLEO-G474RE
  `.ioc` 閼藉顢嶉敍灞借嫙閺傛澘顤?GUI 閹规洝骞忕拋鏉跨秿閿?  `apps/stm32_g474_foc/mcsdk_no_power_precheck/gui_capture_result_2026-05-14.md`.
- 閺傛澘顤冮幋顏勬禈閿?  `apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/2026-05-14_cubemx_ioc_launch_attempt.png`
  閸?  `apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/2026-05-14_cubemx_ioc_pinout_active_window.png`.
- 閹搭亜娴樼拠浣规 CubeMX 閸欘垯浜掗幎濠佺箽鐎涙娈?`.ioc` 閹垫挸绱戦崚?`Pinout & Configuration`
  妞ょ敻娼伴敍宀€鐛ラ崣锝嗙垼妫版ɑ妯夌粈?`STM32G474RETx - NUCLEO-G474RE`閿涙矖.ioc` 鐠囪娲栨禒宥団€樼拋?  `PB12/TIM1_BKIN`閵嗕梗PB14/TIM1_CH2N`閵嗕梗PA2/PA3` VCP 閸?`PB3` SWO閵?- `rg --files -g "*.stmcx"` 閸?GUI 鐏忔繆鐦崥搴濈矝濞屸剝婀侀幍鎯у煂 `.stmcx`閿涙稒婀版潪顔荤瘍濞屸剝婀?  閹规洝骞?MCSDK MotorControl 闁板秶鐤嗘い鐐光偓鍌氱秼閸撳秵鏌婃晶鐐垫畱閺?CubeMX `.ioc` GUI fallback
  鐠囦焦宓侀敍灞肩瑝閺?Workbench / MotorControl 闁板秶鐤嗙拠浣瑰祦閵?- 鏉╂瑤绮涢悞鏈电瑝閹哄牊娼?24V閵嗕礁濮涢悳鍥ㄦ緲閵嗕胶鏁搁張鎭掆偓涓焌te PWM閵嗕府otor Profiler閵嗕胶鍎宠ぐ?鐠嬪啳鐦妴?  Hall 闂傤厾骞嗛幋鏍ㄦ￥閹?FOC 缂佹捁顔戦妴?
## 2026-05-14 P2 Workbench 閸忋儱褰涢幒銏＄ゴ

- Codex 閺傛澘顤?Workbench 閸忋儱褰涢幒銏＄ゴ鐠佹澘缍嶉敍?  `apps/stm32_g474_foc/mcsdk_no_power_precheck/workbench_entry_probe_2026-05-14.md`.
- 閻╊喗鐖ｅΛ鈧弻銉洬閻?repo閵嗕梗F:\STMCubeMX`閵嗕梗C:\Users\gregrg\STM32Cube\Repository\MCSDK_v6.4.2-Full`閵?  VS Code STM32 extension閵嗕梗.stm32cubemx` 閸滃苯鐖剁憴?ST 缁嬪绨惄顔肩秿閵?- 缂佹捁顔戦敍姘拱閺堝搫鍑＄€瑰顥?MCSDK `MotorControl` package 閺佺増宓侀敍宀冨厴閻鍩?  `MotorControl_Configs.xml`閵嗕梗MotorControl_Modes.xml`閵嗕梗MCSDK/`閵嗕梗templates/`閵?  `libMP/` 閸?`libHSO/`閿涙稐绲炬禒宥嗙梾閺?repo `.stmcx`閵嗕胶瀚粩?Workbench launcher 閹?  MotorControl 闁板秶鐤嗘い鍨焻閸ヤ勘鈧?- 閸ョ姵顒?P2 瑜版挸澧犻懗鍊熺槈閺勫簶鈧发CSDK MotorControl package 閺佺増宓佺€涙ê婀垾婵撶礉娑撳秷鍏樼拠浣规
  閳ユ凡orkbench 妞ゅ湱娲伴柊宥囩枂瀹歌弓绻氱€涙ǚ鈧縿鈧?
## 2026-05-14 P2 鐠囦焦宓侀崠鍛纯閺?
- 瀹稿弶鏌婃晶鐐茬秼閸?P2 鐠囦焦宓侀崠鍜冪窗
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/evidence_packet_2026-05-14.md`.
- 鐠囦焦宓侀崠鍛邦唶瑜版洖缍嬮崜宥勭波鎼存挾婀＄€圭偛绨辩€涙﹫绱板▽鈩冩箒 `.stmcx`閿涘苯鍑￠張?CubeMX 妫ｆ牠銆夐幋顏勬禈閸?  NUCLEO-G474RE CubeMX `.ioc` 閼藉顢嶉敍娑楃矝濞屸剝婀?Workbench/CubeMX MotorControl
  闁板秶鐤嗘い鍨焻閸ヤ勘鈧竼N8/EDA/netlist 鐠ф壆鍤庣拠浣规閿涘奔绡冨▽鈩冩箒閺夎法楠?STDRIVE101 娣囨繃濮㈢捄顖氱窞鐠囦焦妲戦妴?- 鐠囦焦宓侀崠鍛Ω `PB12/TIM1_BKIN`閵嗕梗PB14/TIM1_CH2N`閵嗕梗PA2/PA3`閵嗕梗PB3`閵?  `DT/MODE` 閸?STDRIVE101 娣囨繃濮㈡い瑙勬杹鏉╂盯妯嗘繅鐐躲€冮敍宀勪缉閸忓秵濡搁懡澶嬵攳瀵洝鍓艰ぐ鎾村灇
  閸欘垯淇婇幒銉у殠閵?- 鏉╂瑤绮涢悞璺哄涧閺?P2 閺冪姴濮涢悳鍥槈閹诡喗涓嶉悶鍡礉娑撳秵宸块弶鍐т繆娴犺崵鏁撻幋鎰畱 MCSDK 瀹搞儳鈻奸敍灞肩瘍娑撳秵宸块弶?  24V閵嗕礁濮涢悳鍥ㄦ緲閵嗕胶鏁搁張鎭掆偓涓焌te PWM閵嗕府otor Profiler閵嗕笭all 闂傤厾骞嗛幋鏍ㄦ￥閹?FOC 缂佹捁顔戦妴?
## 2026-05-14 P2 NUCLEO CubeMX 鐎圭偞鎼烽懡澶嬵攳

- 閻劍鍩涢幐?NUCLEO-G474RE Board Selector 鐠侯垰绶炵€瑰本鍨氶幍瀣Ω閹靛妫ら崝鐔哄芳鐎圭偞鎼烽敍灞借嫙娣囨繂鐡?  CubeMX `.ioc` 閼藉顢嶉敍?  `apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_no_power_nucleo_g474re_draft/mcsdk_no_power_nucleo_g474re_draft.ioc`.
- `.ioc` 鐠囪娲栫涵顔款吇閿涙瓪PA13/PA14` 娑?SWD閿涘畭PA2/PA3` 娑?NUCLEO VCP閿?  `PB3` 娑?SWO閿涘畭PB12` 娑?`TIM1_BKIN`閿涘畭PB14` 娑?`TIM1_CH2N`閵?- 鏉╂瑨鐦夐弰?CubeMX 闁板秶鐤嗙仦鍌涘复閸欐缍嬮崜?NUCLEO 閼藉顢嶉崪灞艰⒈娑擃亜鍙ч柨顔尖偓娆撯偓澶庡壖閿涙稐绮涙稉宥堢槈閺?  `.stmcx`閵嗕府CSDK MotorControl 瀹搞儳鈻奸妴涓哊8/EDA/netlist 鐠ф壆鍤庨妴涓糡DRIVE101
  娣囨繃濮㈢捄顖氱窞閵嗕笩ate PWM閵嗕府otor Profiler閵嗕笭all 闂傤厾骞嗛幋鏍ㄦ￥閹?FOC閵?
## 2026-05-14 Codex Dual-Teacher Gate Update

- Codex continuation is now hardened in
  `workflow/codex_dual_teacher_execution_gate.md`.
- `AGENTS.md`, `workflow/teaching_contract.md`, `workflow/prompt_recipes.md`,
  `workflow/session_close_checklist.md`, and the project Skill source now point
  to the same four-line gate:
  `妞ゅ湱娲伴惄顔界垼` / `鐎涳缚绡勯惄顔界垼` / `娣囶喗鏁奸懠鍐ㄦ纯` / `缁備焦顒涢懠鍐ㄦ纯`.
- New regression tests in `tests/test_workflow_contracts.py` check that the gate
  stays linked from the main entry points and keeps the no-power boundary.
- This is a workflow-control update only. It does not authorize 24V, power
  board connection, motor connection, Gate PWM, Motor Profiler, Hall closed-loop,
  or sensorless FOC claims.

## 2026-05-14 P2 No-Power GUI Evidence Update

- CubeMX Home screenshot captured:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/2026-05-14_cubemx_home.png`.
- Next GUI-only checklist added:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/gui_capture_checklist_2026-05-14.md`.
- This proves CubeMX GUI launch visibility. The later NUCLEO `.ioc` draft proves
  a CubeMX board/pin configuration was saved, but still does not prove a saved
  MCSDK MotorControl configuration, generated firmware, hardware wiring, Gate
  PWM output, Motor Profiler result, Hall closed-loop behavior, or motor behavior.
- Current blockers remain: real `.stmcx` or Workbench/CubeMX MotorControl
  configuration screenshot; `PB12/TIM1_BKIN` confirmation against
  CubeMX/Workbench plus CN8/EDA/netlist evidence.

## 2026-05-14 NUCLEO Firmware Update

- The NUCLEO baseline now uses LPUART1 RX DMA + IDLE for command reception.
- The interrupt callback only copies received bytes into a ring buffer and
  restarts DMA; command parsing and `printf()` stay in the main loop.
- Debug build passed:
  `apps/stm32_g474_foc/nucleo_g474re_baseline/build/Debug/nucleo_g474re_baseline.elf`.
- Build size after the change: RAM 2552 B, FLASH 23652 B.
- Detailed log:
  `experiments/2026-05-09_nucleo_baseline/logs/2026-05-14_uart_dma_idle_build.md`.
- This is firmware/build progress only. It does not authorize 24V, power board,
  motor, Gate PWM, Motor Profiler, Hall closed-loop, or SMO work.

## 2026-05-14 UART Protocol Model Update

- `src/protocol_model.py` now includes `LineFramer` for DMA/IDLE-like byte
  chunks and newline-delimited JSON frames.
- `tests/test_protocol_model.py` now covers chunk-split frames, multiple frames
  in one chunk, empty lines, oversize drop, discard-until-line-end behavior,
  and recovery.
- `python -m unittest discover -s tests` passes with 24 tests.
- This advances the ESP32/STM32 command path without touching power hardware.

## 2026-05-14 P2 Pin / Config Safety Review

- User clarified they are already familiar with the toolchain; future teaching
  should skip basic CubeMX/CubeIDE navigation unless explicitly requested.
- Next-ring review artifact added:
  `apps/stm32_g474_foc/mcsdk_no_power_precheck/pin_config_review_2026-05-14.md`.
- This review defines evidence classes, hard stops, and the minimum packet
  required before trusting any generated MCSDK configuration:
  Workbench/CubeMX `.stmcx` or screenshot, CN8/EDA/netlist routing evidence,
  and STDRIVE101 `nFAULT` / `DT/MODE` / protection-path evidence.
- This is still P2 no-power evidence only. It does not authorize generated
  PWM behavior, Motor Profiler, power-board connection, motor connection, Hall
  closed-loop, or sensorless FOC claims.

# CURRENT_STATUS

閺堚偓閸氬孩娲块弬甯窗2026-05-14

鏉╂瑤閲滈弬鍥︽閺勵垶銆嶉惄顔解偓缁樺付妞ょ偣鈧倹鐦″▎锛勬埛缂?FOC 妞ゅ湱娲伴弮璁圭礉閸忓牐顕版潻娆撳櫡閿涘苯鍟€鐠?`AGENTS.md`閵嗕梗materials/START_HERE.md` 閸?`docs/00_project_truth/project_context.md`閵?

## 瑜版挸澧犻梼鑸殿唽

妞ゅ湱娲版径鍕艾 NUCLEO 閸╄櫣顢呭銉р柤闂冭埖顔岄敍灞借嫙瀹告彃鐣幋鎰秼閸?P1 濮掑倸搴风仦鍌炵崣閺€韬测偓?026-05-09 瀹歌尙鏁撻幋鎰嫙缂傛牞鐦ч柅姘崇箖 NUCLEO-G474RE baseline CubeMX/CMake 瀹搞儳鈻奸敍?026-05-11 閻劍鍩涢幓鎰返 VOFA+ 閹搭亜娴橀敍宀冪槈閺勫骸缍嬮崜宥呮祼娴犺泛鍑℃稉瀣祰鏉╂劘顢戦獮鍫曗偓姘崇箖 COM5 / ST-LINK VCP 鏉堟挸鍤悩鑸碘偓浣规簚閺冦儱绻旈敍瀹峬ode` 娑?`mode_name` 閼宠棄鎮撳銉︽▔缁€?`IDLE`閵嗕梗ARMED`閵嗕梗RUN_SIM`閵?026-05-12 Codex 闁俺绻?COM5 妤犲矁鐦夋禍?`PING`閵嗕梗MODE?`閵嗕梗ARM`閵嗕梗STOP` 閸滃苯顒熸稊鐘垫暏 `SET_RPM <rpm>` 閸涙垝鎶ら敍姘承掗弸鎰版晩鐠囶垬鈧浇瀵栭崶鎾晩鐠囶垬鈧胶濮搁幀浣瑰珕缂佹縿鈧竸RM 閸氬海娲伴弽鍥р偓鍏兼纯閺傝埇鈧讣TOP 濞撳懘娴傞崸鍥╊儊閸氬牐顫夐崚娆掋€冮妴鍌氭倱閺冦儻绱漃1 catch-up 娴溿倓绮崠鍛嚒鐞涖儵缍堥敍姝嶢RT 閸涙垝鎶ら崜顖欑稊閻劏銆冮妴涓廙A + IDLE 閹恒儲鏁瑰ù浣衡柤閸滃矂妯佸▓闈涱槻閻╂ê娼庡鎻掑弳娴犳挶鈧?026-05-13 鐎涳缚绡勯懓鍛缁斿鈧俺绻?STOP/DMA P0 鏉╀胶些濡偓閺屻儯鈧礁鎳℃禒銈呭娴ｆ粎鏁ら梼鍛邦嚢閸?DMA + IDLE 閸ョ偠鐨熸禍鏃€顒炲ù浣衡柤閿涘畭normalize_learning_loop.py` 娑撳骸宕熼崗鍐╃ゴ鐠囨洟鈧俺绻冮敍娑樻倱閺?P2 MCSDK 閺冪姴濮涢悳鍥暕濡偓閸椻€冲嚒瀵偓婵锝為崘娆欑礉瑜版挸澧犲鍙夋箒閺堫剚婧€瀹搞儱鍙块悧鍫熸拱/status 鐞涖劊鈧攻aseline `.ioc` 鐠囪娲栭妴涔竔n/config 閼藉顢嶉妴浣哥埗閻?ST PDF 閺堫剙婀撮梹婊冨剼閵嗕讣T 鐎规缍夋禍銈呭级閺嶆悂鐛欓崪?pin-function 閸愯尙鐛婃径鍕倞閿涙瓪PC5` 鐞氼偅甯撻梽銈勮礋 nFAULT 閼藉顢嶉懘姘剧礉`PB12/TIM1_BKIN` 閹存劒璐熻ぐ鎾冲 nFAULT 閸婃瑩鈧绱漙PA2/PA3` 娑撳秴鍟€娴ｆ粈璐?FOC UART 姒涙顓婚柅澶嬪閿涘畭PB3` Hall B 闂団偓鐟曚線鍣撮弨?闂呮梻顬?SWO閵?026-05-14 Codex 閸掓稑缂撴禍鍡欏缁斿娈?P2 閺冪姴濮涢悳鍥帳缂冾喛宕忓鍫㈡窗瑜?`apps/stm32_g474_foc/mcsdk_no_power_precheck/`閿涘矁顔囪ぐ鏇氱啊 MCSDK draft閵嗕礁鍟跨粣浣稿枀缁涙牕鎷板銉ュ徔閹恒垺绁撮敍娑欐拱閺?CubeMX 閸欘垱澧界悰宀冪熅瀵板嫮鈥樼拋銈勮礋 `F:\STMCubeMX\STM32CubeMX.exe` 楠炶泛鍑￠崥顖氬З閸?`javaw.exe` 鏉╂稓鈻奸妴鍌炴閸氬海鏁ら幋宄扮暚閹?NUCLEO-G474RE Board Selector 閹靛濡搁幍瀣杽閹垮秴鑻熸穱婵嗙摠 CubeMX `.ioc` 閼藉顢?`apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_no_power_nucleo_g474re_draft/mcsdk_no_power_nucleo_g474re_draft.ioc`閿涘矁顕伴崶鐐碘€樼拋?`PA13/PA14` 娑?SWD閵嗕梗PA2/PA3` 娑?VCP閵嗕梗PB3` 娑?SWO閵嗕梗PB12` 娑?`TIM1_BKIN`閵嗕梗PB14` 娑?`TIM1_CH2N`閵嗗倷绮ㄦ惔鎾冲敶娴犲秵鐥呴張澶屾埂鐎?`.stmcx`閿涘奔绡冨▽鈩冩箒閻欘剛鐝?Motor Control Workbench 閸欘垱澧界悰宀冪熅瀵板嫨鈧倽绻栨禍娑楃矝娑撳秳鍞悰?MCSDK MotorControl 瀹搞儳鈻煎鑼晸閹存劖鍨ㄦ禒璁崇秿绾兛娆?閻㈠灚婧€鐞涘奔璐熷鏌ョ崣鐠囦降鈧倻鏁ら幋椋庘€樼拋銈囧閸旂喓宸奸弶鍨彠闁款喖娅掓禒韬测偓浣烘暩濠ф劘寤洪妴浣风箽閹躲倕顦婚崶鏉戞嫲闂冨牆鈧偐鍤庣槐銏犲嚒鐠佹澘缍嶉敍姹P32 瀹搞儳鈻奸妴涓矯B/Gerber閵嗕焦顒滃?BOM 閺傚洣娆㈤崪灞藉閻?閻㈠灚婧€鐎圭偞绁撮弮銉ョ箶鏉╂ɑ鐥呴張澶婄磻婵鐭囧ǎ鈧妴?
瑜版挸澧犳禒鎾崇氨閻ㄥ嫪瀵岀憰浣风稊閻劍妲搁敍姘祼鐎规岸銆嶉惄顔荤皑鐎圭偞绨妴浣割劅娑旂姾鐭剧痪瑁も偓浣哥暔閸忋劎瀛╃痪瑁も偓浣界カ閺傛瑧鍌ㄥ鏇樷偓浣瑰复閸欙絽顨栫痪锕€鎷伴崥搴ｇ敾娴溿倓绮悧鈺冩窗瑜版洏鈧?

## 瑜版挸澧犳い鍦窗鐎规矮缍?

- 妞ゅ湱娲伴崥宥囆為敍姘唨娴?STM32G474 閻ㄥ嫯绔熺紓妯肩秹閸忓啿鐎烽弮鐘冲妳 FOC 妞瑰崬濮╃化鑽ょ埠閵?
- 娑撹崵鍤庨弸鑸电€敍姝婽M32G474 + STDRIVE101 + 娑撳娴?BLDC + Hall 娣囨繂绨?+ SMO 閺冪姵鍔呴崘鎻掑煛 + ESP32-C3 鏉堝湱绱純鎴濆彠閵?
- 瑜版挸澧犲銉ュ徔闁炬儳褰涘鍕剁窗VS Code + STM32CubeIDE 閹绘帊娆?+ STM32CubeMX + MCSDK閿涙稐绗夋担璺ㄦ暏閻欘剛鐝?STM32CubeIDE 娴ｆ粈璐熸稉?IDE閵?
- 姒涙顓婚張宥呭鐎电钖勯敍娆?閸氬苯顒熼敍宀€鐣诲▔?娑撶粯甯堕弬鐟版倻閵?
- 瀹搞儳鈻奸崢鐔峰灟閿涙艾鍘涚€瑰鍙忔潪顒冩崳閺夈儻绱濋崘宥呬粵閺冪姵鍔呴妴浣风喘閸栨牕鎷扮粵鏃囦含娴滎喚鍋ｉ妴?
- ChatGPT + Codex 閸欏苯绗€閸掕泛浼愭担婊勭ウ瀹告彃娴愰崠鏍电窗ChatGPT 鐠愮喕鐭楅弫娆忣劅閵嗕椒鎹㈤崝鈥冲瘶閸滃苯顦查惄姗堢幢Codex 鐠愮喕鐭楀銉р柤閹笛嗩攽閵嗕浇鐦夐幑顔款唶瑜版洖鎷版禒鎾崇氨閺囧瓨鏌婇妴?

## 瀹告彃鐣幋鎰板帳缂?

- 閸斺晜澧滈煬顐″敜娑撳酣銆嶉惄顔款潐閸掓瑱绱癭AGENTS.md`閵嗕梗materials/assistant_profile.md`閵?
- Codex 娑撴挸鐫?Skill閿涙瓪stm32g474-foc-assistant`閿涘苯鍑＄€瑰顥婇崚鐗堟拱閺?Codex skills 閻╊喖缍嶉敍灞借嫙闁俺绻?`quick_validate.py` 鐎规ɑ鏌熼弽锟犵崣閵?
- 鏉堝懎濮?Skills閿涙瓪jupyter-notebook`閵嗕梗screenshot`閿涘苯鍑＄€瑰顥婇崚鐗堟拱閺?Codex skills 閻╊喖缍嶉敍灞借嫙闁俺绻?`quick_validate.py` 鐎规ɑ鏌熼弽锟犵崣閵?
- 閺堚偓妤傛ü绱崗鍫㈤獓娴滃鐤勫┃鎰剁窗`docs/00_project_truth/project_context.md`閵?
- 閼辨梻缍夐弽鍛婄叀娑撳孩娼靛┃鎰喘閸忓牏楠囬敍姝歞ocs/00_project_truth/internet_verification_rules.md`閵?
- 閺堫剙婀寸挧鍕灐缁便垹绱╅敍姝歮aterials/source_manifest.json`閵嗕梗docs/file_map.md`閵?
- ST 鐎规ɑ鏌熺挧鍕灐缁便垹绱╅敍姝歳eferences/st_manuals_index.md`閿涙稑鐖堕悽?ST PDF 瀹告煡鏆呴崓蹇撳煂 `materials/raw/st_manuals/`閿涘苯瀵橀幏?STDRIVE101 datasheet閿涙波ash 娑撳骸鐣奸弬?URL 鐠佹澘缍嶉崷?`materials/raw/st_manuals/manifest.json`閵?
- 閺堫剙婀村Λ鈧槐銏㈠偍瀵洩绱癭vector_store/`閵?
- Windows 瀹搞儱鍙块柧鎾呯窗CubeMX 閻㈢喐鍨氬銉р柤瀹告彃鐣幋鎰剁幢STM32CubeIDE for VS Code 閹碘晛鐫嶉張顑跨秼瀹告彃鐣ㄧ憗鍜冪幢閹碘晛鐫嶉幍妯碱吀閻?CMake/Ninja/GNU Arm GCC bundle 瀹告彃褰查悽銊ょ艾閺嬪嫬缂撻妴鍌氱秼閸撳秴鍑℃宀冪槈缁崵绮?PATH 娑?`cmake` 閸欘垳鏁ら敍瀹峮inja`閵嗕梗arm-none-eabi-gcc` 閺堫亜濮為崗?PATH閿涙稖绻栭弰?bundle 閹垫顓稿銉ュ徔闁惧彞绗呴惃鍕劀鐢摜濮搁幀浣碘偓鍌滃Ц閹浇顔囪ぐ鏇☆潌 `workflow/windows_toolchain_status.md`閵?
- 閻劍鍩涚涵顔款吇閻楀牏鈥栨禒璺烘珤娴犳湹绗岄梼鍫濃偓鑲╁殠缁鳖澁绱癭hardware/bom/2026-05-09_user_provided_power_stage_parts.md`閿涘牏鏁ら幋鐤嚛閺勫簼绗夐懗鎴掔箽鐠囦礁鍙忛柈銊︻劀绾噯绱濈亸姘弓閸?Datasheet/鎼存挸鐡?PCB/鐎圭偞绁存径宥嗙壋閿涘鈧?
- 閸樼喓鎮婇崶鐐焻閸ユ拝绱癭hardware/schematic/2026-05-09_power_board_schematic_screenshot.jpg`閿涘本鍩呴崶鎯у帗閺佺増宓侀敍姝歨ardware/schematic/2026-05-09_power_board_schematic_screenshot.md`閵?
- 闂冭埖顔岄幒銊ㄧ箻闂傛悂妫敍姝歸orkflow/phase_gate_checklist.md`閵?
- 妫ｆ牗顐肩挧鍕灐鐎电厧鍙嗙憴鍕灟閿涙瓪workflow/intake_checklist.md`閵?
- MacBook Codex 閸欏本婧€闁板秶鐤嗛崗銉ュ經閿涙瓪workflow/macbook_codex_replica.md`閵嗕梗tools/create_mac_codex_setup_bundle.ps1`閵嗕梗tools/bootstrap_mac_codex.sh`閵?
- GitHub 閸欏本婧€閸氬本顒炴潻婊咁伂閿涙瓪origin` -> `https://github.com/pinganyan0-eng/foc_learning_repo`閿涘牏顫嗛張澶夌波鎼存搫绱氶妴?
- STM32 baseline 瀹搞儳鈻奸敍姝歛pps/stm32_g474_foc/nucleo_g474re_baseline/`閿涘瓔ubeMX/CMake 閻㈢喐鍨氶幋鎰閿涘瓕ebug 閺嬪嫬缂撻柅姘崇箖楠炲墎鏁撻幋?`build/Debug/nucleo_g474re_baseline.elf`閵嗗倸缍嬮崜宥呮祼娴犺泛鍑￠崷?NUCLEO-G474RE 娑撳﹪鈧俺绻?COM5 / ST-LINK VCP 鏉堟挸鍤悩鑸碘偓浣规簚閺冦儱绻旈敍娑滅槈閹诡喛顫?`experiments/2026-05-09_nucleo_baseline/logs/2026-05-11_vofa_mode_name_log.md`閵?026-05-12 瀹歌尪鎷烽崝鐘辫閸欙絽鎳℃禒銈夌崣鐠囦礁鎷扮€涳缚绡勯悽?`SET_RPM` 妤犲矁鐦夐敍娑滅槈閹诡喛顫?`experiments/2026-05-09_nucleo_baseline/logs/2026-05-12_com5_set_rpm_validation.md`閵?
- ESP32 瀹搞儳鈻奸崡鐘辩秴閻╊喖缍嶉敍姝歛pps/esp32_c3_gateway/`閵?
- STM32 娑?ESP32 閸楀繗顔呮總鎴犲閿涙瓪interfaces/`閵?
- 鐎圭偤鐛欑拋鏉跨秿娑撳海鐡熸潏鈺€姘︽禒妯煎⒖閻╊喖缍嶉敍姝歟xperiments/`閵嗕梗deliverables/`閵?
- NUCLEO 閸╄櫣顢呭銉р柤鐎圭偤鐛欑拋鏉跨秿閿涙瓪experiments/2026-05-09_nucleo_baseline/`閵?
- 鐎涳缚绡勯梻顓犲箚缂佸瓨濮㈤懘姘拱閿涙瓪tools/normalize_learning_loop.py`閵嗕梗tools/start_learning_session.*`閵嗕梗tools/end_learning_session.*`閵?
- 妞ゅ湱娲伴懛顏勫З閸栨牕顨栫痪锔肩窗`workflow/automation_playbook.md`閿涙稑缍嬮崜?Codex 閼奉亜濮╅崠鏍у瘶閹奉剚鐦￠弮銉ヮ劅娑旂姾顫嬫０鎴﹀仏娴犺翰鈧焦鐦￠弮銉┿€嶉惄顔跨箻閸栨牕璐板Λ鈧柇顔绘閸滃本鐦￠崨銊┿€嶉惄顔碱槻閻╂﹢鍋栨禒璁圭礉閸у洨绮︾€规岸銆嶉惄顔界壌閻╊喖缍嶆潻鎰攽閵?
- 閸欏苯绗€閸掓湹鎹㈤崝鈥冲弳閸欙綇绱癭workflow/ACTIVE_TASK.md`閵嗕梗workflow/task_packet_template.md`閵嗕梗workflow/session_close_checklist.md`閵?
- 閸欏苯绗€閸掕泛顓哥拋鈥茬瑢閹垹顦查弬鍥︽閿涙瓪workflow/task_state_machine.md`閵嗕梗workflow/definition_of_done.md`閵嗕梗workflow/evidence_register.md`閵嗕梗workflow/risk_gate_matrix.md`閵嗕梗workflow/prompt_recipes.md`閵?
- 閸欏苯绗€閸掕埖鏆€鐎涳箑顨栫痪锔肩窗`workflow/teaching_contract.md`閿涘矁顫夌€?ChatGPT/Codex 閺佹瑥顒熼弮鍓佹畱閺傛澘鎮曠拠宥埿掗柌濞库偓浣峰敩閻浇顔夌憴锝夈€庢惔蹇嬧偓浣筋嚦閸氬骸顒熸稊鐘侯唶瑜版洖鎷?GitHub PR 閸愭瑥鍙嗙憴鍕灟閵?
- B 缁犳纭堕崥灞筋劅閺佹瑥顒熸稉搴濇唉娴犳ɑ鈧槒顓搁崚鎺炵窗`workflow/algo_b_teaching_delivery_plan.md`閿涘本濡告稉銈勫敜 8 閸?56 婢?HTML 鐎涳缚绡勭拋鈥冲灊鏉烆剚鍨氳ぐ鎾冲閻喎鐤勯梼鑸殿唽閸欘垱澧界悰宀€娈戦弫娆忣劅閼哄倸顨旈妴浣剿夋潻娑樺閺堝搫鍩楅妴浣圭槨鐠?濮ｅ繐鎳嗘稉濠佹唉閻椻晛鎷扮€瑰鍙忛梻鎼佹，鐟欏嫬鍨妴?
- 瑜版挸澧犵€涳缚绡勯幍褑顢戠仦鍌︾窗`learning/NEXT_LESSON.md`閵嗕梗learning/MASTERY_MAP.md`閵嗕梗workflow/current_learning_sprint.md`閿涘本濡?P1 娑撳绔寸拠淇扁偓浣瑰笁閹宦ょ槈閹诡喓鈧礁顦叉稊鐘辩喘閸忓牏楠囬崪?sprint 娴溿倓绮悧鈺€绮犻梹鑳吀閸掓帡鍣烽幎鑺ュ灇閻厼鍙嗛崣锝冣偓?
- P1 catch-up 娴溿倓绮崠鍜冪窗`deliverables/2026-05-12_p1_catchup_pack.md`閿涘苯鑻熷鍙夊Ω UART 閸涙垝鎶ら崜顖欑稊閻劏銆冮崘娆忓弳 `docs/05_test_and_logs/week1_nucleo_baseline.md`閵嗕笍MA + IDLE 閹恒儲鏁瑰ù浣衡柤閸愭瑥鍙?`docs/04_iot_gateway/uart_dma_idle.md`閵?
- P2 MCSDK 閺冪姴濮涢悳鍥暕濡偓閸椔ゅ磸濡楀牞绱癭deliverables/2026-05-13_p2_mcsdk_no_power_precheck.md`閿涘苯缍嬮崜宥堫唶瑜版洘婀伴張鍝勪紣閸忛澧楅張?status閵嗕攻aseline `.ioc` 鐠囪娲栭妴涓瓹SDK pin/config 閼藉顢嶉妴涓糡 鐎规ɑ鏌熼弶銉︾爱娴溿倕寮堕弽鎼佺崣閵嗕垢in-function 閸愯尙鐛婃径鍕倞閵嗕够hell GUI 鐠囦焦宓侀幒銏＄ゴ閸滃本婀弶?Motor Profiler 閸嬫粍顒?閸ョ偤鈧偓鐠佲€冲灊閿?026-05-14 瀹歌尪鎷烽崝鐘靛缁斿妫ら崝鐔哄芳閼藉顢嶉惄顔肩秿 `apps/stm32_g474_foc/mcsdk_no_power_precheck/`閵嗕竼ubeMX 閸氼垰濮╃捄顖氱窞閵嗕笩UI 闂冭顢ｇ拋鏉跨秿閵嗕腐UCLEO-G474RE CubeMX `.ioc` 閼藉顢?`apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_no_power_nucleo_g474re_draft/mcsdk_no_power_nucleo_g474re_draft.ioc`閿涘奔浜掗崣?STDRIVE101 娣囨繃濮㈢捄顖氱窞鐎光剝鐓?`apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_protection_path_review_2026-05-14.md`閿?026-05-18 瀹稿弶鏌婃晶?Packet A 閹规洝骞忔禒璇插閸?`apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_capture_task_2026-05-18.md`閿涘苯褰ч崶鍝勭暰閺堫亝娼?`.stwb6`閵嗕焦鍩呴崶淇扁偓浣哥摟濞堢敻鐛欓弨璺烘嫲閸嬫粍顒涢弶鈥叉閵嗗倽绻栨禍娑樺涧閺勵垱妫ら崝鐔哄芳闁板秶鐤嗛妴浣割吀閺屻儱鎷版禒璇插濞岃崵鎮婄拠浣瑰祦閿涘奔绗夐弰?`.stmcx`閵嗕府CSDK MotorControl 瀹搞儳鈻奸妴涓畂tor Profiler閵嗕笭all 閹存牕濮涢悳鍥╅獓妤犲矁鐦夐妴?- Obsidian 缁楁棁顔囧銉ょ稊閸栫尨绱版禒鎾崇氨閺嶅湱娲拌ぐ鏇炲嚒闁板秶鐤?`.obsidian/`閿涘奔閲滄禍铏圭應鐠佹澘鎷伴惇瀣緲閺€鎯ф躬 `notes/`閿涘苯鍙嗛崣锝勮礋 `notes/00_home/foc_dashboard.md`閵?

## 瑜版挸澧犻張顏勭磻婵?

- NUCLEO-G474RE baseline CubeMX/CMake 瀹搞儳鈻煎鍙夋杹閸忋儻绱盤2 瀹稿弶鏌婃晶?NUCLEO-G474RE CubeMX `.ioc` 閼藉顢嶉獮鏈电箽鐎?`PB12/TIM1_BKIN`閵嗕梗PB14/TIM1_CH2N`閵嗕梗PA2/PA3` VCP 閸?`PB3` SWO閵嗕净CSDK 閻㈠灚婧€閹貉冨煑瀹搞儳鈻肩亸姘弓閺€鎯у弳閿涙稖绻栨禍娑樷偓娆撯偓澶婄毣閺堫亞绮℃潻?MCSDK/Workbench `.stmcx` 閸?CN8/EDA/netlist 閸忓崬鎮撶涵顔款吇閿涘苯鐨婚張顏嗘晸閹存劗婀＄€?`.stmcx` 閹?MotorControl 闁板秶鐤嗛幋顏勬禈鐠囦焦宓侀妴?- 閻喎鐤?ESP32-C3 缂冩垵鍙у銉р柤鐏忔碍婀弨鎯у弳閵?
- 閸樼喓鎮婇崶鐐焻閸ユ儳鍑￠弨鎯у弳閿涙宝DA 濠ф劖鏋冩禒韬测偓浣割嚤閸?PDF閵嗕赋CB閵嗕笩erber/閸ф劖鐖ｉ弬鍥︽閵嗕礁娅掓禒?Datasheet 閸栧懎鎷板锝呯础 BOM 鐞涖劌鐨婚張顏呮杹閸忋儯鈧?
- 瀹稿弶婀侀惃鍕暏閹撮鈥樼拋銈囧绾兛娆㈠〒鍛礋娴犲秵妲稿鍛槻閺嶅摜鍤庣槐顫礉娑撳秳鍞悰銊р€栨禒鎯邦啎鐠佲€冲嚒鐎光剝鐓￠柅姘崇箖閵?
- NUCLEO baseline 娑撴彃褰涢弮銉ョ箶閸滃苯顒熸稊鐘垫暏 `SET_RPM` 閸涙垝鎶ゆ宀冪槈瀹歌弓楠囬悽鐕傜幢缁€鐑樺皾閸ｃ劍灏濊ぐ顫偓涓畂tor Profiler 缂佹挻鐏夐妴涓燼ll 闂傤厾骞嗙拋鏉跨秿鐏忔碍婀禍褏鏁撻妴?

鏉╂瑤绨烘稉宥嗘Ц闁板秶鐤嗙紓鍝勩亼閿涘矁鈧本妲告い鍦窗鐏忔碍婀潻娑樺弳鐎电懓绨查梼鑸殿唽閵?

## 娑撳绔村銉︽付鐏忓繐濮╂担?

1. 婵″倹鐏夌憰浣哥磻婵顒熸稊?鐎圭偞鎼烽敍姘崇箻閸?NUCLEO-G474RE 閸╄櫣顢呭銉р柤閿涘苯鍘涢崑姘卞仯閻忣垬鈧椒瑕嗛崣锝嗗ⅵ閸楄埇鈧礁鐣鹃弮璺烘珤閸?UART DMA + IDLE閿涙稐绗夐幒?24V閵嗕椒绗夐幒銉ュ閻滃洦婢橀妴浣风瑝閹恒儳鏁搁張鎭掆偓?
2. 婵″倹鐏夌憰浣瑰腹鏉╂盯妯佸▓纰夌窗閸忓牆顕悡?`workflow/phase_gate_checklist.md`閿涘瞼鈥樼拋銈堢箻閸忋儲娼禒韬测偓浣烽獓閸戦缚鐦夐幑顔兼嫲缁備焦顒涢崝銊ょ稊閵?
3. 婵″倹鐏夌憰浣割嚤閸忋儲鏌婄挧鍕灐閿涙艾鍘涢幐?`workflow/intake_checklist.md` 閸掑棛琚崨钘夋倳閿涘苯鍟€閺囧瓨鏌婄€电懓绨茬槐銏犵穿閵?
4. 婵″倹鐏夌憰浣烘埛缂?P2 MCSDK 閺冪姴濮涢悳鍥暕濡偓閿涙艾鍘涚拠?`deliverables/2026-05-13_p2_mcsdk_no_power_precheck.md`閵嗕梗apps/stm32_g474_foc/mcsdk_no_power_precheck/packet_a_capture_task_2026-05-18.md`閵嗕梗apps/stm32_g474_foc/mcsdk_no_power_precheck/config_draft.md`閵嗕梗apps/stm32_g474_foc/mcsdk_no_power_precheck/hands_on_evidence_2026-05-14.md` 閸?`apps/stm32_g474_foc/mcsdk_no_power_precheck/stdrive101_protection_path_review_2026-05-14.md`閿涙稑缍嬮崜宥呭嚒閺?NUCLEO-G474RE CubeMX `.ioc` 閼藉顢嶉妴涓砤cket A 閹规洝骞忔禒璇插閸栧懎鎷?STDRIVE101 娣囨繃濮㈢捄顖氱窞缂傞缚鐦夐惌鈺呮█閿涘奔绲炬禒宥堫洣鐞涖儳婀＄€?MCSDK/Workbench `.stwb6` 閹?MotorControl 闁板秶鐤嗛幋顏勬禈閵嗕竼N8/EDA/netlist 鐠ф壆鍤庣拠浣瑰祦閸滃苯缍嬮崜宥囧 STDRIVE101 娣囨繃濮㈢捄顖氱窞濠ф劘鐦夐幑顕嗙幢娴犲秳绗夐幒?24V閵嗕椒绗夐幒銉ュ閻滃洦婢橀妴浣风瑝閹恒儳鏁搁張鎭掆偓浣风瑝鏉╂劘顢?Motor Profiler閵?5. 婵″倹鐏夌憰浣烘埛缂?STM32 baseline閿涙艾婀鏌ョ崣鐠?COM5 娑撴彃褰涢崨鎴掓姢鐠侯垰绶為惃鍕唨绾偓娑撳绱濈悰銉ㄥ€濋惇?LD2 闂傤亞鍎婄拠浣瑰祦閿涘本鍨ㄩ悽?Codex 鏉╂稖顢戦惇鐔风杽 UART DMA + IDLE callback 閻ㄥ嫭妫ら崝鐔哄芳鐎圭偟骞?閺嬪嫬缂撴宀冪槈閵?
6. 婵″倹鐏夌憰浣哥磻婵鈥栨禒璺侯吀閺屻儻绱版禒?`hardware/bom/2026-05-09_user_provided_power_stage_parts.md` 娑撳搫娅掓禒鍓佸殠缁鳖澁绱濈紒褏鐢荤悰銉ュ斧閻炲棗娴?PDF閵嗕赋CB 閹搭亜娴橀妴浣诡劀瀵?BOM閵嗕笍atasheet 閸滃苯鍙ч柨顔荤箽閹躲倝妲囬崐鑹邦吀缁犳ぜ鈧?

## 鐎瑰鍙忕痪銏㈠殠

- 娑撳秶娲块幒?24V 婢堆呮暩濞翠椒绗傞悽鐐光偓?
- 妫ｆ牗顐兼稉濠勬暩娴ｈ法鏁ら梽鎰ウ閻㈠灚绨敍宀勭帛鐠併倓绮?0.2A 缁狙冨焼瀵偓婵鈧?
- 閹恒儳鏁搁張鍝勫閸忓牆浠涚粚楦挎祰 PWM閵嗕笩ate 濞夈垹鑸伴妴涔禙AULT閵嗕箓S/REG12/VREG 閸滃矂鍣伴弽鐑芥懠鐠侯垱顥呴弻銉ｂ偓?
- JEOC/FOC ISR 閸愬懍绗夐弨?`printf`閵嗕梗HAL_Delay`閵嗕福SON 鐟欙絾鐎介妴涔別bSocket閵嗕礁濮╅幀浣稿敶鐎涙ɑ鍨ㄩ梹鑳偓妤佹闁槒绶妴?
- V9 娑撳骸鐣奸弬?Datasheet 閸愯尙鐛婇弮璁圭礉閸忓牏娴夋穱鈥崇暭閺傜绁弬娆忚嫙閹绘劗銇氭搴ㄦ珦閿涙矂9 娑撳骸鐤勫ù瀣暱缁愪焦妞傞敍灞藉帥濡偓閺屻儲绁寸拠鏇熸蒋娴犺翰鈧?

## 鐢摜鏁ら崗銉ュ經

- 妞ゅ湱娲扮憴鍕灟閿涙瓪AGENTS.md`
- Obsidian 閹粯甯堕崣甯窗`notes/00_home/foc_dashboard.md`
- 鐎涳缚绡勯崗銉ュ經閿涙瓪materials/START_HERE.md`
- 妞ゅ湱娲版禍瀣杽閿涙瓪docs/00_project_truth/project_context.md`
- 闂冭埖顔岄梻鎼佹，閿涙瓪workflow/phase_gate_checklist.md`
- 鐠у嫭鏋＄€电厧鍙嗛敍姝歸orkflow/intake_checklist.md`
- 瑜版挸澧犳禒璇插閸栧拑绱癭workflow/ACTIVE_TASK.md`
- 娴犺濮熼崠鍛侀弶鍖＄窗`workflow/task_packet_template.md`
- 閺€璺轰紣濡偓閺屻儻绱癭workflow/session_close_checklist.md`
- 娴犺濮熼悩鑸碘偓浣规簚閿涙瓪workflow/task_state_machine.md`
- 鐎瑰本鍨氱€规矮绠熼敍姝歸orkflow/definition_of_done.md`
- 鐠囦焦宓侀惂鏄忣唶閿涙瓪workflow/evidence_register.md`
- 妞嬪酣娅撻惌鈺呮█閿涙瓪workflow/risk_gate_matrix.md`
- 閺佹瑥顒熸稉搴濇唉娴犳ɑ鈧槒顓搁崚鎺炵窗`workflow/algo_b_teaching_delivery_plan.md`
- 娑撳绔寸拠鐐⒔鐞涘苯宕遍敍姝歭earning/NEXT_LESSON.md`
- 閹哄本褰欑拠浣瑰祦閸︽澘娴橀敍姝歭earning/MASTERY_MAP.md`
- 瑜版挸澧犵€涳缚绡?sprint閿涙瓪workflow/current_learning_sprint.md`
- 閺佹瑥顒熸總鎴犲閿涙瓪workflow/teaching_contract.md`
- 閹绘劗銇氱拠宥喣侀弶鍖＄窗`workflow/prompt_recipes.md`
- 閺堫剙婀村Λ鈧槐顫窗`python tools/ask_local.py "娴ｇ姷娈戦梻顕€顣?`
- 瀵偓瀹搞儱鍙嗛崣锝忕窗`powershell -ExecutionPolicy Bypass -File .\tools\start_learning_session.ps1`
- 閺€璺轰紣閸忋儱褰涢敍姝歱owershell -ExecutionPolicy Bypass -File .\tools\end_learning_session.ps1 -Topic "娑撳顣? -Summary "娴犲﹤銇夐崑姘啊娴犫偓娑?`
- 鐎涳缚绡勯梼鐔峰灙閺佸鎮婇敍姝歱ython tools/normalize_learning_loop.py`
- 闁插秴缂撳Λ鈧槐銏㈠偍瀵洩绱癭python tools/build_vector_store.py`
- 閸ョ偛缍婂ù瀣槸閿涙瓪python -m unittest discover -s tests`
