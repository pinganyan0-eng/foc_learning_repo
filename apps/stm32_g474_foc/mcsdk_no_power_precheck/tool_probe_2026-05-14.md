# Tool Probe - 2026-05-14

This probe records local tool evidence for the P2 MCSDK no-power practice turn.
It does not prove MCSDK project generation, Motor Profiler readiness, or
hardware behavior.

## Commands / Checks

| Check | Result | P2 Meaning |
| --- | --- | --- |
| Repo `.stmcx` search | `rg --files -g "*.stmcx"` returned no `.stmcx`. | No Workbench project file exists in the repo. |
| MCSDK package executable search | No `.exe`, `.bat`, `.cmd`, `.jar`, or `.stmcx` was found under `C:\Users\gregrg\STM32Cube\Repository\MCSDK_v6.4.2-Full`. | The installed MCSDK package data is present, but a standalone Workbench executable path was not found there. |
| MCSDK package data | `C:\Users\gregrg\STM32Cube\Repository\MCSDK_v6.4.2-Full\MotorControl` contains `MotorControl_Configs.xml`, `MotorControl_Modes.xml`, `MCSDK`, `templates`, `libMP`, and `libHSO`. | Package data exists; it is not a saved project configuration. |
| Workbench entry follow-up | `workbench_entry_probe_2026-05-14.md` records targeted checks of the repo, `F:\STMCubeMX`, the MCSDK package, VS Code STM32 extension folders, `.stm32cubemx`, and common ST program roots. | MotorControl package data is installed, but no `.stmcx` or standalone Workbench launcher was identified. |
| CubeMX launch path | `F:\STMCubeMX\STM32CubeMX.exe` exists. | CubeMX GUI path is now proven. |
| CubeMX launch attempt | `Start-Process -FilePath 'F:\STMCubeMX\STM32CubeMX.exe'` started `F:\STMCubeMX\jre\bin\javaw.exe`. | CubeMX was launched for user-visible GUI work. Power hardware remains out of scope. |
| CubeMX Home screenshot | `screenshots/2026-05-14_cubemx_home.png` captures the CubeMX Home page with the MCU / board / example selector buttons and recent projects. | This proves GUI launch visibility only. It is not an MCSDK configuration, `.stmcx`, generated firmware, or hardware behavior record. |
| CubeMX saved `.ioc` launch | `STM32CubeMX.exe` was launched with `mcsdk_no_power_nucleo_g474re_draft.ioc`. | The saved NUCLEO draft can be reopened in CubeMX. |
| CubeMX pinout screenshots | `screenshots/2026-05-14_cubemx_ioc_launch_attempt.png` and `screenshots/2026-05-14_cubemx_ioc_pinout_active_window.png`. | These show `Pinout & Configuration` for `STM32G474RETx - NUCLEO-G474RE`. This is fallback GUI evidence for the `.ioc`, not Workbench `.stmcx` evidence. |
| Repo `.stmcx` search after GUI attempt | `rg --files -g "*.stmcx"` returned no `.stmcx`. | No real Workbench project file was produced by this GUI attempt. |
| VS Code STM32 extension CLI tools | `cube.exe` and `cube-cmake.exe` exist under the STM32 VS Code extension folders. | Extension-side tools are present; this does not replace Workbench `.stmcx` evidence. |

## Current Decision

- Keep `apps/stm32_g474_foc/mcsdk_no_power_precheck/` as a planning area.
- Do not claim an MCSDK generated project exists.
- Do not claim a Workbench `.stmcx` exists.
- Use `gui_capture_checklist_2026-05-14.md` for the next GUI-only capture.
- This turn captured the saved `.ioc` in CubeMX `Pinout & Configuration`, but
  did not capture a MotorControl page or produce `.stmcx`.
- If the user can later save a Workbench/CubeMX MotorControl screenshot or
  `.stmcx` from the GUI, store or link it from this directory and update the P2
  card.

## Hardware Boundary

No 24V, no power board, no motor, no PWM Gate output, and no Motor Profiler run
were performed or authorized by this probe.
