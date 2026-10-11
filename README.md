# Solar — Dual-Port Solar LED Controller

Engineering workspace for a solar-powered, dual-port LED lighting controller.

> **STATUS: DESIGN / NOT MANUFACTURING READY.** No schematic, PCB layout, firmware build, or lithium-battery protection circuit in this repository has been validated for production. Do not assemble or energize an unreviewed power stage.

## Product requirements
- 30 W nominal solar panel; actual Voc/Vmp/Isc/Imp must be confirmed.
- Main battery: seven removable 3.2 V, 6 Ah LiFePO4 cells, 1S7P (42 Ah, 134.4 Wh nominal).
- Optional second independent 1S7P bank; controlled connection only, no uncontrolled hot paralleling.
- Two **identical**, fully functional, independently protected multi-pin light sockets.
- Three main-board switches: SW0 master isolation, SW1 auto for jack 1, SW2 auto for jack 2.
- Central MCU owns scheduling, light-unit switch interpretation, fault processing, and status indicators. No MCU in light units.
- Each light unit has a local switch, LED power stage, and five diagnostic LEDs.
- Auto schedule: 2 hours at target 2000 lm, then 8 hours at 1000 lm, then OFF.
- Manual mode: AUTO disabled -> local light-unit switch commands the main MCU; hardware safety always overrides.
- E14 denotes socket short/overcurrent and combined output overload, not mere absence of the optional bank.
- Under combined overload, apply equal power reduction when feasible, then safely disconnect loads.

## Repository layout
- [System architecture](docs/architecture.md)
- [Electrical design and unresolved requirements](docs/electrical-design.md)
- [Connector interface](docs/connector.md)
- [Control state machine](docs/control.md)
- [Fault catalog](docs/faults.md)
- [Energy budget](docs/energy-budget.md)
- [Prototype validation checklist](docs/validation.md)

## Engineering gates
1. Obtain panel, cell, LED, connector, and thermal specifications.
2. Select and verify charger, battery protector, power converter, and per-port hardware protection.
3. Capture and ERC-check KiCad schematics.
4. Implement/test target-specific firmware against a finalized MCU pin map.
5. Test power and fault behavior on a current-limited bench supply.
6. Layout PCB, run DRC, review thermal/current paths, then release manufacturing files.

No Gerbers or fabrication claims should be made before these gates are complete.
