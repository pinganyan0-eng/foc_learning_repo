# ST Official Manuals Index

Generated at: 2026-04-30T04:22:39
Last updated: 2026-05-13

These are local text extractions of official ST PDF manuals/application notes. Use the `.txt` files for fast local retrieval, but use the repo-local PDFs for figures, tables, exact page citations, and safety-critical electrical values.

The 2026-05-13 update mirrors frequently used PDFs into `materials/raw/st_manuals/` and records hashes plus official URLs in `materials/raw/st_manuals/manifest.json`. Direct shell download from `st.com` failed in this session, so the current repo PDFs were copied from the user's existing local cache under `F:\嵌赛\1手册`; the official ST URLs were checked online and are preserved for the next refresh.

## Repo-Local PDF Mirror

| ID | Repo-local PDF | Extracted text | Official URL / Refresh Note |
| --- | --- | --- | --- |
| `st_rm0440_stm32g4_reference_manual` | `materials/raw/st_manuals/st_rm0440_stm32g4_reference_manual.pdf` | `materials/extracted/st_manuals/st_rm0440_stm32g4_reference_manual.txt` | <https://www.st.com/resource/en/reference_manual/rm0440-stm32g4-series-advanced-armbased-32bit-mcus-stmicroelectronics.pdf> |
| `st_stm32g474re_datasheet` | `materials/raw/st_manuals/st_stm32g474re_datasheet.pdf` | `materials/extracted/st_manuals/st_stm32g474re_datasheet.txt` | <https://www.st.com/resource/en/datasheet/stm32g474rb.pdf> |
| `st_um2505_nucleo64_mb1367` | `materials/raw/st_manuals/st_um2505_nucleo64_mb1367.pdf` | `materials/extracted/st_manuals/st_um2505_nucleo64_mb1367.txt` | <https://www.st.com/resource/en/user_manual/um2505-stm32g4-nucleo64-boards-mb1367-stmicroelectronics.pdf> |
| `st_an5306_opamp_stm32g4` | `materials/raw/st_manuals/st_an5306_opamp_stm32g4.pdf` | `materials/extracted/st_manuals/st_an5306_opamp_stm32g4.txt` | <https://www.st.com/resource/en/application_note/dm00605707-operational-amplifier-opamp-usage-in-stm32g4-series-stmicroelectronics.pdf> |
| `st_um3027_motor_control_sdk` | `materials/raw/st_manuals/st_um3027_motor_control_sdk.pdf` | `materials/extracted/st_manuals/st_um3027_motor_control_sdk.txt` | <https://www.st.com/resource/en/user_manual/um3027-how-to-use-stm32-motor-control-sdk-v60-workbench-stmicroelectronics.pdf> |
| `st_an5397_sensorless_pmsm_foc` | `materials/raw/st_manuals/st_an5397_sensorless_pmsm_foc.pdf` | `materials/extracted/st_manuals/st_an5397_sensorless_pmsm_foc.txt` | <https://www.st.com/resource/en/application_note/an5397-sensorless-pmsm-foc-controller-stmicroelectronics.pdf> |
| `st_an4144_stm32f0_foc_mcsdk` | `materials/raw/st_manuals/st_an4144_stm32f0_foc_mcsdk.pdf` | `materials/extracted/st_manuals/st_an4144_stm32f0_foc_mcsdk.txt` | <https://www.st.com/resource/en/application_note/an4144-fieldoriented-control-using-the-stm32f0-and-the-stmicroelectronics-motor-control-sdk-stmicroelectronics.pdf> |
| `st_nucleo_g474re_brief` | `materials/raw/st_manuals/st_nucleo_g474re_brief.pdf` | `materials/extracted/st_manuals/st_nucleo_g474re_brief.txt` | <https://www.st.com/resource/en/data_brief/nucleo-g474re.pdf> |
| `st_stdrive101_datasheet` | `materials/raw/st_manuals/st_stdrive101_datasheet.pdf` | `materials/extracted/st_manuals/st_stdrive101_datasheet.txt`; digest: `materials/extracted/st_manuals/st_stdrive101_datasheet_digest.md` | <https://www.st.com/resource/en/datasheet/stdrive101.pdf>; DS13472 Rev 2, June 2022. |

## Added Sources

| ID | Document | Role | Pages | Extracted text | Original PDF |
| --- | --- | --- | ---: | ---: | --- |
| `st_an4144_stm32f0_foc_mcsdk` | AN4144 - Field-oriented control using STM32F0 and ST Motor Control SDK | FOC and MCSDK background reference | 28 | 42485 chars | `F:\嵌赛\1手册\an4144-fieldoriented-control-using-the-stm32f0-and-the-stmicroelectronics-motor-control-sdk-stmicroelectronics.pdf` |
| `st_an5306_opamp_stm32g4` | AN5306 - Operational Amplifier (OPAMP) usage in STM32G4 Series | STM32G4 OPAMP/current-sense reference | 43 | 59288 chars | `F:\嵌赛\1手册\an5306-dual-motor-control-using-the-stm32g4-stmicroelectronics.pdf` |
| `st_an5397_sensorless_pmsm_foc` | AN5397 - Sensorless PMSM FOC controller | Sensorless FOC algorithm reference | 17 | 23125 chars | `F:\嵌赛\1手册\an5397-sensorless-pmsm-foc-controller-stmicroelectronics.pdf` |
| `st_nucleo_g474re_brief` | NUCLEO-G474RE board brief | Board quick reference | 13 | 19492 chars | `F:\嵌赛\1手册\nucleo-g474re.pdf` |
| `st_rm0440_stm32g4_reference_manual` | RM0440 - STM32G4 Series reference manual | Authoritative STM32G4 peripheral reference | 2140 | 4264829 chars | `F:\嵌赛\1手册\rm0440-stm32g4-series-advanced-armbased-32bit-mcus-stmicroelectronics.pdf` |
| `st_stm32g474re_datasheet` | STM32G474RE datasheet | Authoritative MCU electrical and feature reference | 236 | 363571 chars | `F:\嵌赛\1手册\stm32g474re.pdf` |
| `st_um2505_nucleo64_mb1367` | UM2505 - STM32 Nucleo-64 boards MB1367 user manual | NUCLEO-G474RE board user manual | 48 | 67400 chars | `F:\嵌赛\1手册\um2505-stm32-nucleo64-boards-mb1367-stmicroelectronics.pdf` |
| `st_um3027_motor_control_sdk` | UM3027 - STM32 Motor Control SDK user manual | MCSDK workflow reference | 42 | 34570 chars | `F:\嵌赛\1手册\um3027-stm32-motor-control-sdk-stmicroelectronics.pdf` |

## Retrieval Guidance

- For STM32G474 peripheral behavior, prefer `st_rm0440_stm32g4_reference_manual`.
- For STM32G474RE pinout, package, alternate functions, and electrical limits, prefer `st_stm32g474re_datasheet`.
- For MCSDK workflow, generated project structure, Motor Profiler, and tuning flow, prefer `st_um3027_motor_control_sdk`.
- For NUCLEO-G474RE board connectors, power, jumpers, and ST-LINK details, prefer `st_um2505_nucleo64_mb1367` plus `st_nucleo_g474re_brief`.
- For STM32G4 OPAMP/PGA/current-sense analog front-end concepts, prefer `st_an5306_opamp_stm32g4`.
- For sensorless FOC concepts, observer/startup flow, and algorithm background, prefer `st_an5397_sensorless_pmsm_foc`.
- Treat `st_an4144_stm32f0_foc_mcsdk` as background only when it conflicts with STM32G4-specific documents.
- For STDRIVE101 gate-driver protection, `nFAULT`, `DT/MODE`, `CP`, `SCREF`, `REG12`, and `VS`/`VM` checks, use `st_stdrive101_datasheet`; re-check exact PDF tables before hardware work.

## Safety Note

Do not change PWM, dead-time, over-current, ADC current-sense, OPAMP, comparator, or startup parameters from extracted text alone. Confirm against the original PDF and then validate with current-limited, instrumented tests.
