# 2026-05-13 P2 MCSDK No-Power Precheck Card

## Purpose

P2 prepares MCSDK configuration knowledge and low-risk artifacts without energizing motor hardware.

This card does not prove motor-control behavior. It only proves that the learner and repo are ready to plan MCSDK work safely.

## Current Entry Condition

- P1 NUCLEO UART command and DMA + IDLE concept checks are recorded as passed.
- COM5 command validation exists for the NUCLEO baseline.
- No MCSDK motor-control project, Motor Profiler result, Hall run, power-board waveform, or real motor log exists yet.

## Allowed In P2

| Area | Allowed Work | Evidence |
| --- | --- | --- |
| Tooling | Record STM32CubeMX, MCSDK / Motor Control Workbench, VS Code STM32 extension, CMake/Ninja/GCC status | Tool version table, screenshots, command output |
| Configuration planning | Review Workbench screens, draft configuration notes, identify required project files | `.stmcx` placeholder, screenshots, notes |
| Pin planning | Draft NUCLEO and future power-board pin map without wiring power hardware | Pin map table, conflict notes |
| Motor Profiler planning | Write what must be known before a future Profiler run | Plan only, no live profiler result |
| Risk control | Write no-go list and required evidence before P3 | Risk checklist |

## Forbidden In P2

- No 24V.
- No power board connection.
- No motor connection.
- No PWM Gate output to a power stage.
- No real Motor Profiler run.
- No Hall closed-loop validation.
- No SMO / sensorless claim.
- No claim that `SET_RPM` controls real motor speed.

## Tool Role Map

| Tool / Artifact | Role | What It Can Prove In P2 | What It Cannot Prove In P2 |
| --- | --- | --- | --- |
| STM32CubeMX | Select MCU, configure pins/peripherals, generate project structure | Configuration intent and pin/peripheral draft | Motor behavior or safe power operation |
| MCSDK / Motor Control Workbench | Prepare motor-control project configuration | Understanding of MCSDK workflow and planned parameters | Correct motor parameters or stable FOC |
| Generated STM32 project | Buildable firmware source tree when generated and built | Toolchain/configuration path can build | Real motor-control behavior without hardware evidence |
| Motor Profiler | Future tool to measure motor parameters with hardware | A written test plan only | Any real Rs/Ls/Ke or motor validation |

## Required P2 Artifacts

1. Tool version/status table.
2. MCSDK / Workbench configuration screenshot or placeholder.
3. NUCLEO / future board pin map draft.
4. Motor Profiler plan listing required hardware, power limits, motor information, and stop conditions.
5. Risk/no-go checklist.

## 2026-05-14 No-Power Practice Result

Codex executed the P2 no-power practice line without touching the existing NUCLEO baseline and without any hardware action.

| Result | Evidence | P2 Meaning |
| --- | --- | --- |
| Independent draft directory created | `apps/stm32_g474_foc/mcsdk_no_power_precheck/` | There is now a safe place for MCSDK planning artifacts. This is not a generated MCSDK project. |
| Config draft written | `apps/stm32_g474_foc/mcsdk_no_power_precheck/config_draft.md` | The current draft keeps `PB12/TIM1_BKIN`, rejects `PC5` for nFAULT, excludes `PA2/PA3` as default FOC UART, and keeps `PB3` Hall B tied to a SWO release/isolation decision. |
| Pin/config safety review added | `apps/stm32_g474_foc/mcsdk_no_power_precheck/pin_config_review_2026-05-14.md` | The next-ring review now defines evidence classes, acceptance rules, failure conditions, and hard stops for `PB12/TIM1_BKIN`, `PB14/TIM1_CH2N`, `PA2/PA3`, `PB3`, `DT/MODE`, and STDRIVE101 protection paths. |
| Tool probe written | `apps/stm32_g474_foc/mcsdk_no_power_precheck/tool_probe_2026-05-14.md` | The probe records local tool truth for this turn. |
| CubeMX launch path proven | `F:\STMCubeMX\STM32CubeMX.exe`; launched process `F:\STMCubeMX\jre\bin\javaw.exe` | CubeMX can be opened for user-visible GUI work. A screenshot or saved config is still required. |
| Workbench / `.stmcx` still missing | Repo search still found no `.stmcx`; no standalone Workbench executable was found under `MCSDK_v6.4.2-Full`. | Do not claim an MCSDK Workbench project or generated motor-control project exists. |
| NUCLEO CubeMX draft saved | `apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_no_power_nucleo_g474re_draft/mcsdk_no_power_nucleo_g474re_draft.ioc` | User completed the hands-on Board Selector flow. The `.ioc` saves `PA13/PA14` as SWD, `PA2/PA3` as VCP, `PB3` as SWO, `PB12` as `TIM1_BKIN`, and `PB14` as `TIM1_CH2N`. This is CubeMX config evidence only, not MCSDK MotorControl or hardware validation. |
| CubeMX `.ioc` GUI capture added | `apps/stm32_g474_foc/mcsdk_no_power_precheck/gui_capture_result_2026-05-14.md`, `apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/2026-05-14_cubemx_ioc_launch_attempt.png`, `apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/2026-05-14_cubemx_ioc_pinout_active_window.png` | CubeMX reopened the saved `.ioc` to `Pinout & Configuration` and the window title showed `STM32G474RETx - NUCLEO-G474RE`. This is fallback GUI evidence for the `.ioc`; repo search still found no `.stmcx`, and no MotorControl configuration page was captured. |
| Workbench entry probe added | `apps/stm32_g474_foc/mcsdk_no_power_precheck/workbench_entry_probe_2026-05-14.md` | Targeted checks found installed MotorControl package XML/templates/libraries, but no repo `.stmcx`, no standalone Workbench launcher under the checked paths, and no MotorControl configuration page evidence. |
| CN8 / STDRIVE101 route review added | `apps/stm32_g474_foc/mcsdk_no_power_precheck/cn8_stdrive101_route_review_2026-05-14.md` | Current repo evidence is still only screenshot-level clue plus datasheet review requirements. No accepted current EDA, schematic PDF, netlist, or high-resolution route crop is in the repo; the excluded WeChat-side `netlist_PADS.net` candidate is not used as current board evidence. |

No 24V, power-board connection, motor connection, PWM Gate output, Motor Profiler run, Hall closed-loop validation, or SMO validation was performed.

## 2026-05-14 P2 证据包

当前 P2 证据包是
`apps/stm32_g474_foc/mcsdk_no_power_precheck/evidence_packet_2026-05-14.md`.
它记录仓库里现在真正可见的证据，以及信任任何生成 MCSDK 配置前的硬阻塞。

| 证据区域 | 当前结果 | 当前决定 |
| --- | --- | --- |
| Workbench/CubeMX 配置 | 仓库里没有 `.stmcx`；已有 NUCLEO-G474RE CubeMX `.ioc` 草案，保存了 `PB12/TIM1_BKIN`、`PB14/TIM1_CH2N`、`PA2/PA3` VCP 和 `PB3` SWO；CubeMX `Pinout & Configuration` 截图证明该 `.ioc` 可由 GUI 打开；Workbench entry probe 证明 MotorControl package 数据存在但没有发现 Workbench launcher 或 `.stmcx`。 | 可以信任“CubeMX 引脚草案已保存并可 GUI 查看、MCSDK MotorControl package 数据已安装”，继续阻塞“MCSDK MotorControl 项目配置可信”的结论。 |
| CN8 / EDA / netlist 走线 | 仓库可见的只有功率板原理图截图和元数据；没有 EDA 源文件、原理图 PDF、PCB、Gerber 或 netlist。 | 暂时不能信任 STM32 引脚真的连到目标 STDRIVE101 网络。 |
| STDRIVE101 保护路径 | 本地已有官方 PDF、提取文本和 digest，但缺少板级 `DT/MODE`、`nFAULT`、`REG12`、`CP`、`SCREF`、`VS/VM`、bootstrap、standby、VDS 监测证据。 | digest 只能当审查清单，不能当板级验证。 |
| Hall/SWO 冲突 | `PB3` 只有在 SWO 已释放或隔离后才是 Hall B 候选；当前没有板子设置证据。 | 不声称 Hall 输入已经可用。 |

## 2026-05-13 Tool Version / Status Table

Scope: this is a local no-power inspection. It records what the current Windows shell and repo can prove today; it does not prove that MCSDK Workbench can generate a motor-control project yet.

| Tool / Package | Current Local Evidence | Status | P2 Decision / Next Evidence |
| --- | --- | --- | --- |
| VS Code app / `code` CLI | `code` is not in PATH. Standard `Code.exe` / `code.cmd` locations under `AppData\\Local\\Programs\\Microsoft VS Code` and `C:\\Program Files\\Microsoft VS Code` were not found from this shell. | Editor launch path not verified in this turn. | Do not depend on `code` CLI for P2 evidence. If GUI is used later, capture the actual editor path or screenshot. |
| STM32 VS Code extension set | Extension folders exist under `C:\\Users\\gregrg\\.vscode\\extensions`, including `stmicroelectronics.stm32-vscode-extension-3.9.0`, `stm32cube-ide-core-1.3.0-win32-x64`, `stm32cube-ide-build-cmake-1.45.0-win32-x64`, `stm32cube-ide-debug-stlink-gdbserver-1.3.0`, `ms-vscode.cmake-tools-1.23.52`, and `marus25.cortex-debug-1.12.1`. | Extension files are installed locally. | Treat as installed, but still capture a VS Code extension screenshot before using it as final P2 evidence. |
| STM32CubeMX | `C:\\Users\\gregrg\\.stm32cubemx\\mxinstallversion.txt` reports `STM32CubeMX Without Administration rights 6.17.0-RC5`. `STM32CubeMX.log` shows the NUCLEO baseline was generated on 2026-05-09 with STM32Cube FW_G4 V1.6.2 and CMake/GCC output. `F:\\STMCubeMX\\STM32CubeMX.exe` exists and was launched on 2026-05-14, starting `F:\\STMCubeMX\\jre\\bin\\javaw.exe`. | Install metadata, generation log, executable path, and launch process are now verified. | Add a CubeMX GUI screenshot or saved configuration evidence before final P2 closeout. |
| STM32Cube FW_G4 | `C:\\Users\\gregrg\\STM32Cube\\Repository\\STM32Cube_FW_G4_V1.6.2` exists. CubeMX log also records FW_G4 V1.6.2 during baseline generation. | Available locally. | OK as the current firmware package for no-power config review. |
| MCSDK / MotorControl package | `C:\\Users\\gregrg\\STM32Cube\\Repository\\MCSDK_v6.4.2-Full\\MotorControl` exists and contains `MotorControl_Configs.xml`, `MotorControl_Modes.xml`, `MCSDK`, `templates`, `libMP`, and `libHSO`. 2026-05-13 and 2026-05-14 shell probes found no `.exe`, `.bat`, `.cmd`, `.jar`, or `.stmcx` under `MCSDK_v6.4.2-Full`, and no `.stmcx` in the repo. | MCSDK package files are present, but Workbench GUI / `.stmcx` generation is still not verified. | Use the repo draft only until a Workbench screenshot or real `.stmcx` is captured. Do not claim Workbench project readiness from package files alone. |
| Motor Profiler | MCSDK package contains profiler-related files, but no live profiler run exists in this repo. UM3027 shows Workbench can launch Motor Profiler from the GUI home area, but that is a future hardware-stage action. | Planning only. | Do not run Profiler in P2. Keep it as a future P3 plan requiring motor, power chain, current limit, stop conditions, and rollback evidence. |
| System CMake | `C:\\Program Files\\CMake\\bin\\cmake.exe`; `cmake --version` returned `4.3.2`. | Available in PATH. | OK for shell-side build orchestration when a generated no-power project exists. |
| Ninja | `ninja` is not in PATH in this shell. Prior `workflow/windows_toolchain_status.md` records a VS Code bundle Ninja `1.13.2`, but this turn did not locate the executable. | Current shell cannot run it directly. | Re-verify the VS Code bundle path before claiming P2 build readiness. |
| GNU Arm GCC | `arm-none-eabi-gcc` is not in PATH in this shell. Prior `workflow/windows_toolchain_status.md` records a VS Code bundle GNU Tools for STM32 `14.3.1`, but this turn did not locate the executable. | Current shell cannot run it directly. | Re-verify bundle path or configure the build preset before generated MCSDK project build evidence. |
| STM32CubeProgrammer / ST-LINK CLI | `STM32_Programmer_CLI` is not in PATH and was not found in the quick AppData search. | Download/debug backend not verified in this turn. | Not needed for P2 no-power artifact. Required before any future flash/debug evidence. |
| Serial tool | COM5 evidence exists from P1 logs, but the serial tool name/screenshot is still not recorded. | P1 serial behavior is evidenced; tool identity remains incomplete. | Add serial tool name/screenshot later if it is used as submission evidence. |

## 2026-05-13 Workbench / `.stmcx` Evidence Probe

This probe tried to turn the missing GUI evidence into a concrete next action without inventing a completed Workbench step.

| Probe | Result | P2 Meaning |
| --- | --- | --- |
| Repo `.stmcx` search | `rg --files -g "*.stmcx"` found no `.stmcx` in the repo. | No Workbench project file exists yet. |
| MCSDK package `.stmcx` search | MCSDK package search found `MotorControl_Configs.xml` and `MotorControl_Modes.xml`, but no `.stmcx`. | Installed package data is not the same as a project configuration. |
| MCSDK executable search | No `.exe`, `.bat`, `.cmd`, or `.jar` was found under `C:\\Users\\gregrg\\STM32Cube\\Repository\\MCSDK_v6.4.2-Full`. | Shell cannot launch Workbench from this package path. |
| Common ST program roots | `C:\\Program Files\\STMicroelectronics`, `C:\\Program Files (x86)\\STMicroelectronics`, and `C:\\ST\\STM32CubeIDE` did not exist in this shell. | No separate ST GUI install path was proven in this turn. |
| VS Code extension roots | STM32 VS Code extension folders exist, but shell search did not locate `ninja.exe`, `arm-none-eabi-gcc.exe`, `cmake.exe`, `STM32CubeMX.exe`, or `STM32_Programmer_CLI.exe` under `.vscode\\extensions`. | Prior bundle evidence remains useful, but this turn did not re-prove exact executable paths. |

Decision: keep Workbench/CubeMX evidence open. The next valid evidence must be one of:

- a screenshot of Motor Control Workbench / CubeMX showing the draft configuration;
- a real `.stmcx` saved by Workbench into a planned no-power project folder;
- an exact, reproducible launch path plus captured version/config screen.

This is a P2 blocker for claiming the MCSDK configuration is generated. It does not block continuing the written no-power risk plan.

## 2026-05-14 Workbench / CubeMX Follow-up Probe

| Probe | Result | P2 Meaning |
| --- | --- | --- |
| CubeMX executable path | `F:\STMCubeMX\STM32CubeMX.exe` exists. | CubeMX can be launched from a reproducible local path. |
| CubeMX launch | `Start-Process -FilePath 'F:\STMCubeMX\STM32CubeMX.exe'` started `F:\STMCubeMX\jre\bin\javaw.exe`. | GUI opened to a visible Home page; a later NUCLEO-G474RE CubeMX `.ioc` draft was saved. |
| CubeMX Home screenshot | `apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/2026-05-14_cubemx_home.png` | Captures CubeMX Home and recent projects. This is GUI launch evidence only, not a saved MCSDK configuration. |
| CubeMX `.ioc` Pinout screenshots | `apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/2026-05-14_cubemx_ioc_launch_attempt.png`, `apps/stm32_g474_foc/mcsdk_no_power_precheck/screenshots/2026-05-14_cubemx_ioc_pinout_active_window.png` | Captures the saved NUCLEO `.ioc` opened at `Pinout & Configuration`. This confirms GUI visibility of the saved `.ioc`, not MotorControl/Workbench configuration. |
| GUI capture result | `apps/stm32_g474_foc/mcsdk_no_power_precheck/gui_capture_result_2026-05-14.md` | Records the fallback evidence and the remaining `.stmcx` / MotorControl blocker. |
| Workbench entry probe | `apps/stm32_g474_foc/mcsdk_no_power_precheck/workbench_entry_probe_2026-05-14.md` | Records targeted search for Workbench launcher and `.stmcx`. MotorControl package XML/templates/libraries exist, but no saved Workbench project or launcher was identified. |
| MCSDK no-power directory | `apps/stm32_g474_foc/mcsdk_no_power_precheck/` created. | This is a planning directory, not generated firmware. |
| Config draft | `apps/stm32_g474_foc/mcsdk_no_power_precheck/config_draft.md` created. | Draft decisions are now explicit and reviewable. |
| Tool probe note | `apps/stm32_g474_foc/mcsdk_no_power_precheck/tool_probe_2026-05-14.md` created. | Local GUI/tool evidence for this turn is preserved. |
| Repo `.stmcx` status | Still absent. | P2 cannot claim Workbench configuration generation. |

## 2026-05-14 NUCLEO Board Selector Hands-on Draft

The learner used the NUCLEO-G474RE Board Selector path and saved a no-power
CubeMX draft at:

`apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_no_power_nucleo_g474re_draft/mcsdk_no_power_nucleo_g474re_draft.ioc`.

Key readback:

| Item | `.ioc` readback | P2 meaning |
| --- | --- | --- |
| Board entry | `Mcu.IP0=NUCLEO-G474RE` | This draft starts from the real development board, not a bare-MCU guess. |
| MCU / package | `Mcu.UserName=STM32G474RETx`; `Mcu.CPN=STM32G474RET6`; `Mcu.Package=LQFP64` | Correct NUCLEO-G474RE MCU/package context. |
| Debug pins | `PA13.Signal=SYS_JTMS-SWDIO`; `PA14.Signal=SYS_JTCK-SWCLK` | SWD must remain reserved. |
| VCP pins | `PA2.Signal=LPUART1_TX`; `PA3.Signal=LPUART1_RX` | P1/Nucleo VCP path is visible and should not be blindly reused for FOC communication. |
| SWO conflict | `PB3.Signal=SYS_JTDO-SWO` | `PB3` remains blocked for Hall B until SWO is released or isolated. |
| nFAULT candidate | `PB12.Signal=TIM1_BKIN` | CubeMX accepts the preferred break-input candidate. Board routing to STDRIVE101 `nFAULT` is still unproven. |
| V low-side candidate | `PB14.Signal=TIM1_CH2N` | CubeMX accepts the preferred V low-side PWM candidate. Board routing to the STDRIVE101 input is still unproven. |

No `.stmcx`, Motor Profiler result, Hall run, power-board connection, motor
connection, Gate PWM output, or SMO validation was produced.

## Baseline `.ioc` Readback

Source: `apps/stm32_g474_foc/nucleo_g474re_baseline/nucleo_g474re_baseline.ioc`.

| Item | Current Baseline Value | P2 Meaning |
| --- | --- | --- |
| Board | `NUCLEO-G474RE` | The P1 project is a NUCLEO baseline, not a motor-control project. |
| MCU | `STM32G474RETx` / `STM32G474R(B-C-E)Tx` | Correct MCU family for the future MCSDK work. |
| Debug | `PA13` = SWDIO, `PA14` = SWCLK, `PB3` = SWO | Keep SWD. Treat `PB3` as a possible conflict if Hall B later uses `TIM2_CH2` on `PB3`. |
| ST-LINK VCP in P1 baseline | `PA2` = `LPUART1_TX`, `PA3` = `LPUART1_RX` | This is a P1 communication convenience. It must not be blindly reused in the MCSDK FOC config because OPAMP/PGA planning also touches `PA2/PA3`. |
| LED / button support | Board BSP common plus `PA5` LD2 and `PC13` B1 behavior in generated/BSP code | OK for NUCLEO learning evidence. Do not treat as a motor enable or fault-reset design without a later safety review. |
| Clock | PLL system clock target recorded as `170000000` Hz | Useful for MCSDK planning, but timing must be regenerated by CubeMX/Workbench in the real MCSDK project. |
| Motor-control peripherals | No TIM1 PWM, ADC injected, OPAMP, Hall, nFAULT, or MCSDK middleware assigned in this baseline `.ioc`. | P2 must create a separate MCSDK config draft; P1 `.ioc` is not a motor-control starting point. |

## 2026-05-13 Official Source Cross-Check

This pass uses local extracted ST text for line-level search, then checks the current ST online pages/PDFs before turning the result into a P2 decision. Local text alone is not enough for a durable P2 artifact because ST board manuals, schematics, and board resources can be revised.

Durable local use: frequently used ST PDFs are now mirrored under `materials/raw/st_manuals/`, with hashes and official URLs recorded in `materials/raw/st_manuals/manifest.json`. The local extracted text remains the fast search layer; the mirrored PDFs are the page/table/figure layer.

| Source | Online Verification | P2 Use |
| --- | --- | --- |
| STM32G474xB/xC/xE datasheet DS12288 | ST datasheet PDF: <https://www.st.com/resource/en/datasheet/stm32g474rb.pdf>. Online search/open confirmed DS12288 Rev 6 pin tables. | Pin alternate-function decisions for `PA2/PA3`, `PC5`, `PB12`, `PB14`, `PB3`, `PA12`, `PC10/PC11`. |
| NUCLEO-G474RE / UM2505 | ST product page lists `UM2505 STM32G4 Nucleo-64 boards (MB1367)` version 6.0, latest update 2025-12-09, and the PDF opens as UM2505 Rev 6 December 2025: <https://www.st.com/resource/en/user_manual/um2505-stm32g4-nucleo64-boards-mb1367-stmicroelectronics.pdf>. | NUCLEO header, VCP, solder bridge, and ST morpho connector checks. |
| NUCLEO board design resources | ST product page lists 2026-01-02 MB1367 D01 schematic, board design, manufacturing, and BOM resources. | Board routing remains a required follow-up; current repo has no downloaded D01 schematic/netlist evidence yet. |
| AN5306 OPAMP application note | ST application-note PDF: <https://www.st.com/resource/en/application_note/dm00605707-operational-amplifier-opamp-usage-in-stm32g4-series-stmicroelectronics.pdf>. | Confirms PGA/internal feedback concepts and that an OPAMP VOUT pin can be reused only when the internal ADC output route is configured. |
| RM0440 reference manual | Current ST RM0440 PDF URL located at <https://www.st.com/resource/en/reference_manual/rm0440-stm32g4-series-advanced-armbased-32bit-mcus-stmicroelectronics.pdf>. The browser fetch failed for this PDF in this turn, so local extracted RM0440 text remains the line-level evidence for `TIMx_BKIN` enable/polarity behavior. | Break input planning: `TIM1_BKIN` is the correct class of safety input to verify for nFAULT; it still needs CubeMX/Workbench confirmation. |
| STDRIVE101 datasheet | Repo-local PDF: `materials/raw/st_manuals/st_stdrive101_datasheet.pdf`; extracted text: `materials/extracted/st_manuals/st_stdrive101_datasheet.txt`; digest: `materials/extracted/st_manuals/st_stdrive101_datasheet_digest.md`. Official source: <https://www.st.com/resource/en/datasheet/stdrive101.pdf>, DS13472 Rev 2. | Gate-driver protection review: `nFAULT`, `DT/MODE`, `CP`, `SCREF`, `REG12`, `VS`/`VM`, VDS monitoring, overcurrent, UVLO, and thermal shutdown. |

### Pin Conflict Resolution Pass

| Conflict ID | Official-Source Finding | Conservative P2 Decision | Still Required |
| --- | --- | --- | --- |
| P2-CFG-001 | UM2505 Rev 6 shows the NUCLEO VCP path on `PA2/PA3` for `LPUART1`; the datasheet also maps `PA2` to `OPAMP1_VOUT` and `PA3` to OPAMP-related inputs. AN5306 allows VOUT pin reuse only when the internal output-to-ADC path is configured. | Do not use `PA2/PA3` as the MCSDK FOC debug/control UART in the draft. Prefer a separate future UART candidate such as `USART3 PC10/PC11`. | CubeMX/Workbench must show OPAMP and UART choices with no conflict. |
| P2-CFG-002 | The datasheet maps `PC5` to `TIM15_BKIN`, `TIM1_CH4N`, `USART1_RX`, and OPAMP1/OPAMP2 VINM additional functions; it is not the clean `TIM1_BKIN` candidate. `PB12` maps to `TIM1_BKIN`. UM2505 also shows `PC5` tied into USART1/VCP solder-bridge options. | Reject `PC5` as the nFAULT/TIM1 break draft pin. Use `PB12 / TIM1_BKIN` as the current nFAULT candidate. | Confirm `PB12` reaches the future power-board nFAULT net in CN8/EDA/netlist and is accepted by CubeMX/Workbench. |
| P2-CFG-003 | The datasheet maps `PB3` to `JTDO-TRACESWO` and `TIM2_CH2`; UM2505 SB15 controls whether T_SWO is connected to PB3. | Keep SWD on `PA13/PA14`. If Hall B uses `PB3/TIM2_CH2`, release SWO / isolate PB3 rather than claiming both uses. | CubeMX/Workbench Hall selection and physical board bridge state must be recorded before hardware. |
| P2-CFG-004 | The datasheet maps `PB14` to `TIM1_CH2N`; it also maps `PA12` to `TIM1_CH2N` but `PA12` has USB_DP and older-material conflicts. | Keep `PB14 / TIM1_CH2N` as the preferred V low-side PWM candidate. Treat `PA12` as an alternate only if the board routing forces it. | Verify MCSDK pin assignment against CN8/power-board routing before any generated project is trusted. |
| P2-CFG-005 | ST's current NUCLEO page has newer 2026-01 board resources, but this repo has not captured the matching schematic/netlist for the future power board or NUCLEO revision. | Keep the entire pin map as a planning artifact, not a wiring instruction. | Capture schematic/EDA/netlist or exact Workbench/CubeMX evidence before moving beyond P2. |

## MCSDK Pin / Config Draft - Not Applied

This draft is a planning artifact only. It is not a wiring instruction and must be reconciled in CubeMX/MCSDK against NUCLEO headers, the future power-board CN8 connector, and official pin alternate functions before any hardware action.

### Configuration Draft

| Config Area | Draft Choice | Evidence / Rationale | P2 Status |
| --- | --- | --- | --- |
| Project style | New MCSDK no-power project, kept separate from `nucleo_g474re_baseline` | P1 baseline has no motor-control peripherals and should remain stable. | Draft only. |
| Suggested future path | `apps/stm32_g474_foc/mcsdk_no_power_precheck/` | Keeps generated structure intact and avoids mixing P1 UART demo with MCSDK. | Directory created for planning only. It is not a generated MCSDK project. |
| Board mode | Start as NUCLEO-G474RE for learning, then custom-board pin review for STDRIVE101 power stage | Current repo has NUCLEO evidence and only a screenshot/line-item record for the power board. | Draft only. |
| Current sensing | 3-shunt low-side, internal OPAMP/PGA candidate | Project facts and V9 route use G474 OPAMP/PGA and 20 mOhm shunts. | Values are placeholders until Datasheet/Workbench review. |
| Speed feedback | Hall sensors as first closed-loop fallback; SMO/PLL only later | Project strategy is Hall first, sensorless later. | P2 may configure/plan; no Hall run. |
| PWM timer | TIM1 center-aligned complementary PWM candidate | Project facts use TIM1 -> ADC injected -> JEOC -> FOC timing. | No PWM output in P2. |
| Protection input | nFAULT should use `PB12 / TIM1_BKIN` as the current draft candidate | STDRIVE101 nFAULT is safety-critical. Online/local ST source checks make `PC5` a bad draft choice and make `PB12` the cleaner TIM1 break candidate. | Draft resolved at pin-function level; still blocked on CubeMX/Workbench and CN8/EDA/netlist confirmation. |
| Communication | Do not reuse P1 `PA2/PA3` VCP by default in FOC config; prefer a separate future ESP32/debug plan such as `USART3 PC10/PC11` from V9 | `PA2/PA3` are tied to P1 LPUART and also appear in OPAMP/PGA constraints. Online UM2505 and datasheet checks confirm the conflict risk. | Draft only; must be checked in CubeMX. |
| Motor parameters | Keep a template only: motor model, voltage/current, pole pairs, Rs/Ls/Ke, Hall placement, limits | Real Rs/Ls/Ke require Motor Profiler or measured data. | No measured motor parameters in P2. |

### Candidate Pin Map

| Function | Draft STM32 Pin | Peripheral / Mode | Source | Status |
| --- | --- | --- | --- | --- |
| U high PWM | `PA8` | `TIM1_CH1` | V9 pin map | Candidate, not applied. |
| U low PWM | `PB13` | `TIM1_CH1N` | V9 pin map | Candidate, not applied. |
| V high PWM | `PA9` | `TIM1_CH2` | V9 pin map | Candidate, not applied. |
| V low PWM | `PB14` | `TIM1_CH2N` | V9 pin map | Candidate, not applied; older notes mention `PA12`, so keep conflict visible. |
| W high PWM | `PA10` | `TIM1_CH3` | V9 pin map | Candidate, not applied. |
| W low PWM | `PB15` | `TIM1_CH3N` | V9 pin map | Candidate, not applied. |
| U current sense | `PA1` | `OPAMP1_VINP` / internal ADC route | V9 and tech report | Candidate, not applied. |
| V current sense | `PA7` | `OPAMP2_VINP` / internal ADC route | V9 and tech report | Candidate, not applied. |
| W current sense | `PB0` | `OPAMP3_VINP` / internal ADC route | V9 and tech report | Candidate, not applied. |
| OPAMP1 feedback/output pins | `PA3` / `PA2` | PGA internal feedback / output route | V9 OPAMP table plus ST datasheet/AN5306 cross-check | Must not be casually reused for UART in FOC config. `PA2` external VOUT can be treated as reusable only if CubeMX/MCSDK explicitly configures internal OPAMP output to ADC. |
| OPAMP2 feedback/output pins | `PC5` / `PA6` | PGA internal feedback / output route | V9 OPAMP table plus ST datasheet cross-check | `PC5` is rejected as nFAULT for the P2 draft; keep it unavailable until OPAMP mode and board routing are checked. |
| OPAMP3 feedback/output pins | `PB2` / `PB1` | PGA internal feedback / output route | V9 OPAMP table | Keep external feedback pins floating if PGA mode requires it. |
| Bus voltage | `PC4` | `ADC2_IN5` candidate | V9 pin map | Candidate, not applied. |
| nFAULT | `PB12` preferred; `PC5` rejected for this draft | `TIM1_BKIN` safety input candidate | ST datasheet online/local check plus older report/proposals | Draft decision only. Requires CubeMX/Workbench and CN8/EDA/netlist proof before use. |
| Hall A | `PA15` | `TIM2_CH1` | V9 pin map | Candidate, not applied. |
| Hall B | `PB3` | `TIM2_CH2` | V9 pin map plus ST datasheet/UM2505 cross-check | Candidate conflict with current SWO. Release/isolate SWO if Hall B remains on PB3. |
| Hall C | `PB10` | `TIM2_CH3` | V9 pin map | Candidate, not applied. |
| ESP32 UART TX/RX | `PC10` / `PC11` | `USART3_TX` / `USART3_RX` | V9 pin map and power-board screenshot metadata | Candidate for later gateway stage, not P2 validation. |
| OLED I2C | `PB8` / `PB9` | `I2C1_SCL` / `I2C1_SDA` | V9 pin map | Later gateway/display work, not P2 validation. |

### Pin / Config Conflict List

| Conflict ID | Conflict | Why It Matters | Conservative P2 Action |
| --- | --- | --- | --- |
| P2-CFG-001 | P1 uses `PA2/PA3` for `LPUART1`, while OPAMP/PGA planning touches `PA2/PA3`. | Reusing the P1 serial path may break the FOC analog configuration or hide an OPAMP output/input constraint. | Treat P1 COM5 UART as learning evidence only. Exclude `PA2/PA3` from the MCSDK FOC communication draft unless CubeMX/MCSDK proves the OPAMP route is safe. |
| P2-CFG-002 | V9 lists `PC5` for nFAULT, but ST pin tables show `PC5` is not a clean `TIM1_BKIN` pin and also has OPAMP1/OPAMP2 VINM roles. | nFAULT is safety-critical; a break input should not be assigned to an ambiguous OPAMP/VCP-related pin. | Reject `PC5` for nFAULT in P2. Use `PB12/TIM1_BKIN` as the draft candidate, pending CubeMX/Workbench and board-routing proof. |
| P2-CFG-003 | V9 lists Hall B on `PB3`, while current baseline keeps `PB3` as SWO. | Hall input and SWO trace cannot both own the same pin. | Keep SWD `PA13/PA14`; release/isolate SWO if Hall B remains on `PB3/TIM2_CH2`. |
| P2-CFG-004 | V phase low-side PWM differs across materials: V9 says `PB14`; older notes mention `PA12`. | Wrong complementary PWM pin can drive the wrong STDRIVE101 input. | Prefer `PB14/TIM1_CH2N`; keep `PA12/TIM1_CH2N` only as a board-routing alternate. |
| P2-CFG-005 | Power-board source is still screenshot/user-confirmed line items, not EDA/netlist/PDF. | CN8 names prove intent, not final electrical correctness or physical routing. | Keep this as a planning draft only. Require EDA source/PDF/BOM/netlist before wiring or power checks. |

## Motor Profiler Future Plan

Motor Profiler remains forbidden in P2. This section is only the future P3 plan skeleton and the stop-condition list that must exist before any profiler attempt.

| Required Before Future Profiler Run | P2 Status |
| --- | --- |
| Exact motor model, rated voltage/current, pole pairs, phase resistance/inductance expectation if known, Hall sensor wiring, and safe speed/current limits | Missing; template only. P2 must not invent measured Rs/Ls/Ke. |
| Power chain identified, inspected with no-power checks, and current-limited supply procedure written | Missing; no 24V or power board action allowed. First future bring-up should start from a conservative current limit, defaulting around 0.2 A unless later project evidence justifies another value. |
| STDRIVE101 mode and protection reviewed | Partially drafted. Before P3, verify `DT/MODE`, `REG12`, `VS`/`VM`, `SCREF`, `CP`, `nFAULT`, standby/wake behavior, and whether VDS monitoring is enabled or intentionally disabled. |
| nFAULT, PWM enable/gate, current-sense, bus-voltage, and Hall pins verified against CubeMX/Workbench plus board netlist | Missing; pin draft only. `PB12/TIM1_BKIN` remains a draft candidate until board route and Workbench evidence agree. |
| Pre-run no-power evidence | Missing. Required later: visual inspection, continuity/no-short checks, power-rail resistance checks, gate-driver passive checks, pull-up/pull-down review, and known-good firmware rollback image. |
| Instruments and logs | Missing. Required later: current-limited supply, multimeter, oscilloscope for Gate/nFAULT/rail checks, serial log capture, and a written operator stop procedure. |
| Abort conditions | Written here for future P3: stop immediately on unexpected current draw, supply collapse, `nFAULT` low, REG12/VS abnormality, gate waveform mismatch, wrong Hall transitions, abnormal heating/smell, profiler detection failure, communication loss, or any ambiguous fault source. |
| Rollback path | P1 known-good NUCLEO baseline exists. Before P3, also retain a profiler-specific firmware image, exact config file, power-off sequence, and restore steps back to the safe baseline. |

Future profiler run rule: a profiler attempt is allowed only after the hardware phase gate explicitly opens. It must start from no-load, current-limited, instrumented checks and must be logged under `experiments/YYYY-MM-DD_motor_profiler/`. If any stop condition appears, power off first and record evidence before changing firmware or wiring.

## Learner Check

Passed on 2026-05-13:

- Motor Profiler cannot run in P2 because it needs a real motor and power chain.
- A generated MCSDK project without hardware can show toolchain/configuration familiarity, but cannot prove real motor parameters or power-chain behavior.
- P2 no-power artifacts include pin map, motor-parameter template, no-power configuration file or placeholder, risk/no-go checklist, and Motor Profiler plan.
- Real measured motor parameters must wait for a later hardware stage with real motor and power chain.

## 2026-05-15 Readiness Snapshot

Current readiness control file:

`apps/stm32_g474_foc/mcsdk_no_power_precheck/p2_readiness_snapshot_2026-05-15.md`

The snapshot consolidates Packet A/B/C, PB3/SWO, STM32-side signal-contract,
and build-only gate status into one gate decision. Current decision: P2
remains in progress; Packet A remains `Blocked`; generated-project trust is
`Not allowed`; Packet B/C and PB3/SWO remain blocked or partial clue only; P3
powered or motor work is not allowed.

This is readiness governance only. It does not prove MCSDK MotorControl
configuration, generated-project trust, CN8 routing, STDRIVE101
protection-path proof, Gate PWM, Motor Profiler, Hall, motor, power-stage, or
sensorless behavior.

## 2026-05-15 Phase Gate Insert

The formal phase gate checklist now includes a P2 no-power insert:

`workflow/phase_gate_checklist.md`

It blocks direct NUCLEO-to-Motor-Profiler jumps, separates P2-S1 no-power
precheck from P2-S2 build-only generated-project work, and lists the P2-to-P3
blockers: accepted Packet A/B/C, PB3/SWO evidence where used, no-power
continuity checks, current-limited bring-up settings, measurement points, stop
conditions, rollback image, and a new dated decision that explicitly opens the
powered action.

## Next Step

Continue P2 by adding the evidence that the saved NUCLEO `.ioc` and CubeMX pinout screenshots still cannot provide: a Workbench/MCSDK `.stmcx` or MotorControl configuration screenshot, plus CN8/EDA/netlist routing evidence. The next GUI/config check must verify `PB12/TIM1_BKIN` for nFAULT, `PB14/TIM1_CH2N` versus any `PA12` alternate, `PA2/PA3` exclusion from the FOC UART plan, and any `PB3` Hall/SWO choice. Keep hardware actions blocked until the phase gate explicitly allows them.

CubeMX now has a proven launch path: `F:\STMCubeMX\STM32CubeMX.exe`, and the repository contains a saved NUCLEO `.ioc` draft at `apps/stm32_g474_foc/mcsdk_no_power_precheck/mcsdk_no_power_nucleo_g474re_draft/mcsdk_no_power_nucleo_g474re_draft.ioc`. Do not mark P2 ready for generated MCSDK work until a real Workbench/MCSDK configuration artifact and board-routing evidence exist.

The user has stated they are already familiar with toolchain navigation. Future teaching should skip CubeMX basics and use `apps/stm32_g474_foc/mcsdk_no_power_precheck/pin_config_review_2026-05-14.md` as the next engineering checkpoint.
