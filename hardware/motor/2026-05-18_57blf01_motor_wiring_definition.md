# 57BLF01 Motor Wiring Definition Source - 2026-05-18

This note records a user-provided motor wiring definition image. It is a
no-power source clue only.

Source image:
`hardware/motor/2026-05-18_57blf01_motor_wiring_definition.jpg`

Original provided file:
`C:\Users\gregrg\Documents\xwechat_files\wxid_5gjwrl5pj20022_32b0\temp\RWTemp\2026-05\a12055270de7bbee9d00360836dabbaa.jpg`

SHA256:
`62C2668751705A647C2178DF784E3AD038B5AAB615B37FE53CB39141479DED9A`

## Source Metadata

| Field | Value |
| --- | --- |
| Source type | User-provided wiring definition image |
| Source confidence | Candidate / wiring clue |
| Physical harness photo by project | No |
| Project continuity measurement | No |
| Hall powered validation | No |
| Motor Profiler result | No |

## Extracted Phase Wiring

The image labels the three thick phase wires as:

| Motor phase | Wire color | Review status |
| --- | --- | --- |
| U | Yellow | Candidate image clue |
| V | Red | Candidate image clue |
| W | Black | Candidate image clue |

## Extracted Hall Wiring

The image labels the five thin Hall wires as:

| Hall signal | Wire color | Meaning | Review status |
| --- | --- | --- | --- |
| `HU` | Yellow | Hall U / Hall A-family signal clue | Candidate image clue |
| `HV` | White | Hall V / Hall B-family signal clue | Candidate image clue |
| `HW` | Blue | Hall W / Hall C-family signal clue | Candidate image clue |
| `H+` | Red | `+5V` Hall supply clue | Candidate image clue; do not power in P2 |
| `H-` | Black | `GND` Hall supply return clue | Candidate image clue; do not power in P2 |

The image also shows Hall switch labels `S1`, `S2`, and `S3`, but this does not
accept Hall angle, electrical sequence, connector pin numbering, or phase/Hall
alignment.

## Interpretation Rules

- Treat the three thick wires and five thin Hall wires as different harness
  groups. Yellow appears in both groups: phase U and Hall `HU`.
- Do not use this image as proof that the actual motor harness has been
  inspected, measured, or powered.
- Do not derive pole pairs, Hall angle, phase sequence, PI gains, current
  limits, or Motor Profiler values from this image.
- Do not connect Hall `H+` to 5 V during P2. This source only records a color
  clue for a later gated check.

## Workbench Use Policy

This source may help fill no-power Workbench notes and motor wiring labels
when creating the future project-specific `.stwb6`, but only as a candidate
source. It does not upgrade Packet A selected fields by itself.

## Required Follow-Up

1. Photograph the actual motor harness and verify the thick/fine wire groups.
2. Confirm U/V/W phase wire colors on the physical motor.
3. Confirm Hall `HU/HV/HW/H+/H-` colors on the physical connector.
4. Confirm `J_HALL` connector pin numbering from board source or continuity
   evidence before mapping these wires to the power board.
5. Keep phase/Hall alignment and Hall angle for a later gated hardware stage.
