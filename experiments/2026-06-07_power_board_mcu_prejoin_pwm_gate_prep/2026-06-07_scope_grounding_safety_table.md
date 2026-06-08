# Oscilloscope grounding safety table

## Core Rule

Most line-powered bench oscilloscopes connect all channel ground shells and probe ground leads to protective earth. Connecting a ground clip to a switching node can create a direct short through the oscilloscope.

Never disconnect or defeat the oscilloscope protective-earth conductor. Floating measurements require a correctly rated differential probe or an isolated-input instrument used according to its manual.

## Measurement Table

| Target | Passive probe ground clip | Decision | Reason |
| --- | --- | --- | --- |
| MCU logic input relative to GND_SIGNAL | Confirmed GND_SIGNAL only | Potentially allowed after equipment review | Ground-referenced logic signal |
| nFAULT relative to GND_SIGNAL | Confirmed GND_SIGNAL only | Potentially allowed after equipment review | Ground-referenced open-drain signal |
| GLSx relative to board GND | Confirmed board GND only | Potentially allowed after equipment review | Low-side gate is ground-referenced |
| REG12 relative to board GND | Confirmed board GND only | DMM preferred during preparation | Ground-referenced supply node |
| GHSx relative to OUTx | Do not use passive-probe ground clip on OUTx | Differential probe required | Both points move relative to earth |
| OUT1/OUT2/OUT3 | Never attach ordinary ground clip | Prohibited in this task | Phase nodes are switching nodes |
| BOOT1/BOOT2/BOOT3 | Never attach ordinary ground clip | Prohibited in this task | Floating bootstrap nodes |
| Two channel ground clips on different nodes | Never | Prohibited | Channel grounds are commonly bonded in typical bench scopes |

## Equipment Record

Do not approve a measurement until every field is filled:

| Item | Record |
| --- | --- |
| Oscilloscope manufacturer/model | RIGOL DS1102E Plus, 2-channel, 120 MHz, 1 GSa/s; photo `photos/2026-06-07_rigol_front_model.jpg`. |
| Input grounding architecture | Treat as earth-referenced. Rear label says line powered and "maintain ground"; photo `photos/2026-06-07_rigol_back_label.jpg`. |
| Channel-to-channel isolation | Not proven. Treat channel grounds as common unless the instrument manual proves isolated inputs. |
| Passive probe model | RIGOL RP2200-class passive probe from photo `photos/2026-06-07_rigol_rp2200_passive_probe.jpg`. |
| Probe attenuation | 1x/10x marking visible; use 10x for any approved board measurement. |
| Tip-to-ground rating | Photo marking appears to show 1x/150 V CAT II and 10x/300 V CAT II; verify on the physical probe before use. |
| Differential probe model | None shown. |
| Differential voltage rating | Not available. |
| Common-mode voltage rating | Not available. |
| Bandwidth and CMRR at relevant frequency | Not available without a differential probe. |
| Manual URL/page | TODO: add RIGOL DS1102E Plus and RP2200 manual references before a dynamic task. |

## Equipment Decision - 2026-06-07 Photo Review

- The RIGOL scope and passive probe can be considered only for ground-referenced
  logic input, nFAULT, REG12, or low-side Gate measurements after a separate
  dynamic task is approved.
- Ordinary passive-probe ground clips must be connected only to reviewed
  GND_SIGNAL / board GND.
- High-side `GHSx - OUTx`, `OUTx`, and `BOOTx` measurements remain prohibited
  with the shown equipment because no differential probe or isolated-input
  instrument was provided.

## Pre-Measurement Review

- [ ] Instrument manual confirms grounding architecture.
- [ ] Probe voltage and category ratings exceed the planned measurement.
- [ ] Differential probe common-mode range is sufficient.
- [ ] Channel grounds are treated as common unless the manual explicitly proves isolation.
- [ ] Ground location is verified by schematic and DMM continuity while unpowered.
- [ ] Probe compensation and attenuation settings are recorded.
- [ ] Only one reviewed ground point is used for ordinary passive probes.
- [ ] No measurement relies on removing the oscilloscope earth connection.

## Official Safety Basis

- Tektronix states that differential probes or isolated-input oscilloscopes are appropriate for signals not referenced to ground, including motor drives.
- Tektronix warns that defeating a bench oscilloscope protective ground creates shock, fire, equipment-damage and measurement-integrity risks.
- Tektronix also notes that ordinary multi-channel scope grounds are commonly connected internally; placing channel grounds on different nodes can short those nodes together.

Sources:

- [Floating Measurements Selection Guide](https://www.tek.com/en/datasheet/floating-measurements-selection-guide)
- [The Three Facets of Floating Measurement Solutions](https://www.tek.com/en/documents/application-note/three-facets-floating-measurement-solutions)

