# Vendor Motor Parameter Source - 57BLF01 - 2026-05-17

This note records a vendor-provided motor-parameter image. It is a source
packet for no-power review only.

Source image:
`hardware/motor/2026-05-17_vendor_57blf01_motor_parameters.jpg`

## Source Metadata

| Field | Value |
| --- | --- |
| Source type | Vendor-provided parameter image |
| Provided by | User, from seller information |
| Source confidence | Candidate / supplier clue |
| Physical measurement by project | No |
| Motor Profiler result | No |
| Powered Hall validation | No |

## Extracted Parameters

| Parameter | Vendor value | Review status |
| --- | --- | --- |
| Model | `57BLF01` | Candidate |
| Magnetic pole count | `4` | Candidate; if this means total poles, MCSDK pole pairs would be `2`, but this must be confirmed. |
| Phase count | `3` | Candidate |
| Rated DC voltage | `24 VDC` | Candidate |
| Rated speed | `3000 rpm` | Candidate |
| Holding torque | `0.2 N-m` | Candidate |
| Output power | `63 W` | Candidate |
| Peak torque | `0.6 N-m` | Candidate |
| Peak current | `9.6 A` | Candidate |
| Line resistance | `0.6 ohm` | Candidate; not a project DMM measurement. |
| Line inductance | `0.75 mH` | Candidate; not a project LCR measurement. |
| Torque constant | `0.065 N-m/A` | Candidate |
| Back EMF | `6.23 V/kRPM` | Candidate |
| Rotor inertia | `120 g*cm2` | Candidate |
| Body length | `48 mm` | Candidate |
| Weight | `0.65 kg` | Candidate |

## Workbench Use Policy

If Workbench requires a motor entry before the project can be saved, use a
vendor-candidate name such as:

`57BLF01_VENDOR_CANDIDATE`

This name is intentionally short because Workbench notes that firmware uses
only the first 24 characters of a motor name.

Do not treat these values as measured project data. They may support a
no-power configuration draft, but they do not authorize Motor Profiler, PI
tuning, current-limit selection for powered work, Hall closed-loop, or any
motor run.

## Required Follow-Up

Before using these values beyond no-power configuration planning:

1. photograph the actual motor nameplate and harness;
2. record U/V/W and Hall wire colors visually;
3. measure U-V, V-W, and W-U resistance with probe-short residual recorded;
4. confirm whether "magnetic pole count 4" means total poles or pole pairs;
5. defer inductance, Ke, and Hall-angle validation to a later gated hardware
   stage.
