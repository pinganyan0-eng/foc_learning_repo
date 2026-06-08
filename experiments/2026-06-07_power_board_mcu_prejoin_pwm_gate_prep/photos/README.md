# Photo evidence naming

This directory stores field photos for the MCU pre-join and future dynamic
PWM/Gate tasks. A photo is evidence for preparation review only; it is not a
test pass by itself.

## Required Preparation Photos

| Filename | Content |
| --- | --- |
| `2026-06-07_01_power_board_overview_unpowered.jpg` | Power-board overview showing no motor and no phase load. |
| `2026-06-07_02_cn8_pin1_and_silkscreen.jpg` | CN8 close-up showing pin 1, silkscreen, and orientation. |
| `2026-06-07_03_stdrive101_dt_mode_area.jpg` | High-resolution U1 / DT-MODE local area. |
| `2026-06-07_04_nucleo_connector_overview.jpg` | NUCLEO connector and intended cable. |
| `2026-06-07_05_scope_and_probe_labels.jpg` | Oscilloscope and probe model / rating labels. |
| `2026-06-07_06_unpowered_wiring_plan.jpg` | Wiring-plan photo only while equipment is unpowered. |

## Photo Rules

- Preserve original images; do not replace them with compressed chat previews.
- Each photo should carry one main evidence goal.
- Annotate measurement points with non-conductive markers or post-processing
  arrows. Do not place metal objects near a powered board.
- If a matching `.md` file is added, record source, capture time, board
  revision, what the photo proves, and what it cannot prove.

## Archived Photos - 2026-06-07

Source: user-provided WeChat photos reviewed by Codex on 2026-06-07.
These photos are evidence for preparation review only. They do not prove any
PWM output, Gate waveform, motor behavior, or dynamic safety.

| Filename | What it can support | Limit |
| --- | --- | --- |
| `2026-06-07_power_board_top_overview.jpg` | Power-board top-side overview; OUT1/OUT2/OUT3 connector, CN3/CN8 area, STDRIVE101 area, MOSFET area and bulk capacitors are visible. | Does not prove DT/MODE net, MCU wiring, or powered state. |
| `2026-06-07_power_board_bottom_overview.jpg` | Bottom-side routing overview and solder side are visible. | Photo is not a netlist, EDA source, or continuity proof. |
| `2026-06-07_cn3_cn8_closeup.jpg` | CN3/CN8 connector region and adjacent resistor arrays are visible enough for orientation review. | Does not provide a NUCLEO-to-CN8 six-channel mapping. |
| `2026-06-07_power_board_with_dc_modules.jpg` | Power board with external DC modules and no motor connected in the photo. | Not a reviewed wiring plan; power ownership and current-limit setup still need a separate table. |
| `2026-06-07_stdrive101_dt_mode_area_closeup.jpg` | STDRIVE101 surrounding components and local copper are visible for review. | Does not conclusively prove DT/MODE direct-GND or RDT mode; EDA/netlist or DMM evidence is still needed. |
| `2026-06-07_rigol_back_label.jpg` | Scope rear label shows a line-powered RIGOL instrument and "maintain ground" warning. Treat as earth-referenced. | Does not prove channel isolation; assume channel grounds are common unless a manual proves otherwise. |
| `2026-06-07_rigol_front_model.jpg` | Scope front label shows RIGOL DS1102E Plus, 2 channels, 120 MHz, 1 GSa/s. | Does not authorize floating or high-side measurements. |
| `2026-06-07_rigol_rp2200_passive_probe.jpg` | Passive probe appears to be RIGOL RP2200-class, marked for 1x/10x use and CAT II ratings. | It is not a differential probe; do not use its ground clip on OUTx, BOOTx, or high-side source/switch nodes. |
