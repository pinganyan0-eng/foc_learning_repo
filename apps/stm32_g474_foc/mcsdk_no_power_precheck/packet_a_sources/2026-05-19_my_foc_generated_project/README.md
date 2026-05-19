# MY_FOC Generated Project Source Packet - 2026-05-19

This directory stores selected no-power source evidence copied from:

`C:\Users\gregrg\.st_workbench\projects\MY_FOC`

It intentionally does not include the generated `Src/`, `Inc/`, `Drivers/`, or
`MCSDK_v6.4.2-Full/` trees.

Review result:

`Partial clue / generated project quarantined / Packet A not accepted`.

The project shows MC Workbench 6.4.2 generated a `MY_FOC` project, but it is
configured as `SIX_STEP`, not FOC. It also does not yet provide accepted
current-sense, fault, Hall/PWM, physical route, or build-only evidence for the
self-developed STDRIVE101 board.

No generated-project trust is added. No 24V, No Gate PWM output, and No Motor
Profiler run are authorized.

Later Codex manual edit and rollback:

- Original `.stwb6` archived as `MY_FOC.original_2026-05-19.stwb6`.
- External source project:
  `C:\Users\gregrg\.st_workbench\projects\MY_FOC.stwb6`.
- Backup created:
  `C:\Users\gregrg\.st_workbench\projects\MY_FOC.stwb6.pre_codex_foc_edit_2026-05-19.bak`.
- Failed manual FOC candidate archived as
  `MY_FOC.codex_foc_candidate_2026-05-19.stwb6`.
- The one-field edit from `"algorithm": "sixStep"` to `"algorithm": "FOC"`
  made Workbench unable to load the file.
- The external `MY_FOC.stwb6` was restored from the backup and again reads
  `"algorithm": "sixStep"`.

The failed FOC candidate is negative evidence only. No Generate, no build, no
flash, No 24V, No Gate PWM output, and No Motor Profiler run are authorized.
