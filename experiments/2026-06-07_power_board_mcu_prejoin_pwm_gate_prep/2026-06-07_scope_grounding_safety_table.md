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
| Oscilloscope manufacturer/model | TODO |
| Input grounding architecture | TODO: earth-referenced / isolated / unknown |
| Channel-to-channel isolation | TODO |
| Passive probe model | TODO |
| Probe attenuation | TODO |
| Tip-to-ground rating | TODO |
| Differential probe model | TODO / none |
| Differential voltage rating | TODO |
| Common-mode voltage rating | TODO |
| Bandwidth and CMRR at relevant frequency | TODO |
| Manual URL/page | TODO |

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

