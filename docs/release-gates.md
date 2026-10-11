# Release gates and evidence

Status: **NOT PRODUCTION READY**. No manufacturing or battery safety claims are authorized by this repository.

## G0: Requirements
- [x] Dual-port behavior documented
- [x] Fault taxonomy documented
- [x] Energy feasibility documented
- [ ] Panel, cells, connectors and LED component datasheets collected

## G1: Electrical design
- [ ] Complete KiCad schematic with validated symbols, footprints and ERC
- [ ] LiFePO4 charging profile and independent hardware battery protection reviewed
- [ ] Battery bank insertion, individual-cell fusing and equalization risks addressed
- [ ] SW0 isolation under solar and battery feed tested
- [ ] Independent hardware port current limiting and fault feedback demonstrated
- [ ] Component BOM with sourcing, lifecycle and datasheet links
- [ ] Worst-case power and thermal calculations reviewed

## G2: Embedded
- [x] Hardware-independent reference behavior and unit tests
- [ ] MCU pin map, firmware target, startup and watchdog validated
- [ ] Real ADC calibration and hardware protection feedback implemented
- [ ] Sunset, local override, diagnostics and fault recovery tested on hardware

## G3: PCB and manufacturing
- [ ] PCB placement/routing, DRC, thermal/current and EMC review
- [ ] Gerber, drill, pick-and-place, assembly drawing and BOM generated
- [ ] Prototype assembled and inspected

## G4: Physical verification
- [ ] Battery and charger safety tests, including fault injection
- [ ] Single and dual port load tests and thermal soak
- [ ] Short-circuit isolation and repeated protection recovery tests
- [ ] Solar and battery cycling under expected environmental conditions
- [ ] Engineering sign-off, production test jig and traceability

**Reference tests do not validate the electronics.** A qualified engineer must review and test physical hardware before manufacturing approval.
