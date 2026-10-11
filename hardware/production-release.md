# Production release — BLOCKED

**Revision status: engineering development, not a released PCB.**

## Inputs required to close electrical design
| Input | Why it matters | Status |
|---|---|---|
| 30 W solar panel datasheet (Voc at cold, Vmp, Isc, Imp) | Charger topology, input ratings, surge protection | Missing |
| Exact 3.2 V 6 Ah LiFePO4 cell datasheet | Charge/discharge limits, cell-holder ratings, protection thresholds | Missing |
| LED emitter/array Vf, If, efficacy, heatsink and driver constraints | Output bus voltage, current, converter sizing, thermal budget | Missing |
| Maximum cable length and connector environmental rating | Pin current, voltage drop, ESD, water ingress | Missing |
| Ambient and battery operating temperature ranges | Charge inhibition and thermal qualification | Missing |

## Release artifacts and required evidence
- [ ] Electrically complete KiCad main schematic, including actual charger and power-path topology
- [ ] Electrically complete KiCad light-unit schematic
- [ ] MCU pin allocation, clock, ADC references and safe reset states
- [ ] Datasheet-linked manufacturer BOM with real values, footprints and sourcing
- [ ] Calculations: battery protection, charger, boost converter, eFuse, wiring, copper and thermal
- [ ] KiCad PCB layout with controlled grounding and tested power copper
- [ ] Clean ERC and DRC reports
- [ ] Gerber and drill outputs matching approved PCB revision
- [ ] Assembly drawings, pick-and-place, production test points
- [ ] Real target firmware compiled and tested on prototype
- [ ] Bench measurements: charging, shorts, dual-port operation, low voltage, hot/cold behavior
- [ ] Environmental and extended-run test results
- [ ] Qualified independent engineering review and sign-off

## Key hazards to resolve
- 1S7P battery holders and removable parallel cells can experience large equalization currents. Do not connect mismatched cells directly.
- An optional second bank must not be directly paralleled with the first without appropriate current limiting and fault isolation.
- A physical master OFF must interrupt charging even when the solar panel remains illuminated.
- Firmware cannot replace hardware overcurrent and overvoltage protection.
- Two lights on the proposed 2h+8h schedule require more energy than a single 134.4 Wh nominal bank stores, even before system losses.

The preliminary BOM and connector netlist are **planning artifacts**, not validated CAD/netlist or procurement outputs. Do not submit this repository's present hardware folder to a PCB manufacturer.
