# P2 Workbench Entry Probe - 2026-05-14

This record turns the remaining Workbench / `.stmcx` question into a
repo-visible no-power evidence item. It does not generate firmware and does not
validate hardware.

## Probe Goal

Find whether the current machine exposes a usable Motor Control Workbench entry
or an existing `.stmcx` project file that can move P2 beyond CubeMX `.ioc`
fallback evidence.

## Locations Checked

| Location | Result |
| --- | --- |
| Repo root | `rg --files -g "*.stmcx"` found no `.stmcx`. |
| `F:\STMCubeMX` | CubeMX executable exists. Targeted search found CubeMX files and helper utilities, but no obvious Motor Control Workbench launcher or `.stmcx`. |
| `C:\Users\gregrg\STM32Cube\Repository\MCSDK_v6.4.2-Full` | MotorControl package data exists. Targeted search found MotorControl XML, templates, libraries, and profiler source/library files, but no `.stmcx` and no standalone Workbench executable. |
| `C:\Users\gregrg\.vscode\extensions` | STM32 VS Code extension tools exist, including `cube.exe` and `cube-cmake.exe`; targeted search did not identify a Workbench launcher or `.stmcx`. |
| Common ST program roots | `C:\Program Files\STMicroelectronics`, `C:\Program Files (x86)\STMicroelectronics`, and `C:\ST` were not present in this shell. |

## MCSDK Package Evidence

The MCSDK package includes:

- `MotorControl/MotorControl_Configs.xml`;
- `MotorControl/MotorControl_Modes.xml`;
- `MotorControl/MCSDK/`;
- `MotorControl/templates/`;
- `MotorControl/libMP/`;
- `MotorControl/libHSO/`.

The first lines of `MotorControl_Configs.xml` identify the package as:

- `Name="MotorControl"`;
- `Version="MCSDK_v6.4.2-Full"`;
- `RootFolder="MCSDK_v6.4.2-Full/MotorControl/"`.

The first lines of `MotorControl_Modes.xml` identify it as a middleware IP:

- `Name="MotorControl"`;
- `IPType="middleware"`;
- `IpGroup="Middleware"`;
- `Version="MCSDK_v6.4.2-Full"`.

This proves MotorControl package data is installed. It does not prove a saved
project configuration exists.

## P2 Decision

Current P2 evidence can claim:

- CubeMX can open the saved NUCLEO-G474RE `.ioc`;
- MotorControl package data is installed locally;
- package XML/templates/libraries are present.

Current P2 evidence cannot claim:

- a real Workbench `.stmcx` exists;
- a MotorControl configuration page has been captured;
- a generated MCSDK motor-control project exists;
- Motor Profiler is ready to run;
- any power-board, motor, Hall, Gate PWM, or sensorless behavior is validated.

## Next Evidence Required

The next valid Workbench-side evidence must be supplied by one of:

1. a real `.stmcx` saved under `apps/stm32_g474_foc/mcsdk_no_power_precheck/`;
2. a screenshot of a MotorControl / Workbench configuration page showing the
   selected MCU and motor-control settings;
3. an exact new launcher path for Motor Control Workbench if it exists outside
   the locations checked above.

This remains P2 no-power work only.

## 2026-05-14 Follow-up Recheck

This follow-up rechecked the `.stmcx` / MotorControl side while the route-review
work ran in parallel.

| Location | Follow-up result | P2 decision |
| --- | --- | --- |
| Repo root | `rg --files -g "*.stmcx"` returned no files. | No saved Workbench project is present in the repo. |
| `F:\STMCubeMX` | Narrow searches found Eclipse workbench plugin files and no `.stmcx`; they did not identify a Motor Control Workbench project or launcher. | CubeMX remains available, but this is not MotorControl configuration evidence. |
| `C:\Users\gregrg\STM32Cube\Repository\MCSDK_v6.4.2-Full` | Narrow searches found no `.stmcx` and no standalone Workbench/MotorControl executable. | Installed package data still does not prove a saved project configuration. |
| `C:\Users\gregrg\.vscode\extensions` | Narrow searches found no `.stmcx`; extension tools such as `cube.exe` / `cube-cmake.exe` are present. | VS Code extension tooling exists, but no Workbench project evidence was found. |

No MotorControl configuration page was captured in this follow-up. The next
valid upgrade remains a real `.stmcx`, a MotorControl / Workbench configuration
screenshot, or a reproducible launcher path plus captured configuration page.
