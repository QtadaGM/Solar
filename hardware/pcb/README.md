# PCB design package — electrical architecture freeze pending

**Status: preliminary placement / NOT fabrication-ready.**

The production target is a custom FR-4 main board with solar charging, two independently protected 1S7P LiFePO4 bank interfaces, master shutdown, power conversion, central STM32-class MCU and two completely identical eight-pin female light connectors.

## Quality objectives
- Identical connector footprints, pinouts, ratings and protection circuitry for JACK1 and JACK2.
- No hot paralleling of independently charged battery banks.
- Dedicated fast hardware fault protection for each output, separate from firmware.
- Correct cell-chemistry thresholds and temperature inhibit.
- Hardware master isolation of all active power paths including solar charging.
- Trace/plane width and via count justified by worst-case RMS and fault currents.
- Kelvin sensing for shunts, low-noise ADC routing, and separation of switching and logic grounds.
- Connector ESD/transient protection, inrush handling, and adequate creepage/clearance.
- Appropriate copper weight and heat spreading after loss and thermal analysis.
- SWD/debug access, labeled test points and production-test access.
- ERC/DRC and independent design review before release.

## Why the routed PCB is not included yet
An actual manufacturable PCB must be generated from a complete netlisted electrical schematic. The 30 W panel Voc/Vmp, cell model and allowable discharge rate, LED forward voltage/current, connector/cable requirements and output voltage are unresolved. Guessing these values would create a plausible-looking but potentially unsafe lithium-battery PCB.

The [BOM](../bom/bom.csv) is a **structured engineering BOM**, not a procurement BOM: every unverified part is marked TBD. It intentionally does not invent manufacturer part numbers or component values.

## Next design gates
1. Lock the panel, cell and LED electrical specifications.
2. Select charger/protection/DC-DC ICs against datasheets and compute passives.
3. Capture complete KiCad schematic and export netlist.
4. Complete layout from schematic; run ERC, DRC, thermal and power integrity checks.
5. Prototype and validate before issuing Gerbers or assembly BOM.
