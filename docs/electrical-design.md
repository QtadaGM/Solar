# Electrical implementation plan (unvalidated)

This file is an engineering checklist, **not a completed schematic**.

1. Solar front end: characterize Voc/Vmp/Isc/Imp at temperature extremes; select reverse-blocking and surge protection; choose a switching charger supporting 1S LiFePO4 voltage/current/thermal profile.
2. Bank A and B: per-bank dedicated LiFePO4-rated protection, fusing, thermal sensors, insertion protection and controlled current-limited coupling. Review individual parallel-cell insertion/equalization and holder/contact ratings.
3. Master switch SW0: design and verify isolation of solar-fed charger and battery-fed system, including reverse leakage; charging OFF as explicitly requested.
4. DC/DC: calculate worst-case two-port load, peak current, thermal loss and inrush. Regulated 12 V is only a proposal until LED drivers and connectors are chosen.
5. Per-port eFuse/current limit: independent fast hardware fault cutoff, current sensing, MCU fault status, controlled retry/latch policy.
6. Main MCU: choose STM32C0-class or equivalent only after GPIO/ADC/timer budget is complete; add watchdog, brownout handling, programming pads and safe pin defaults.
7. Per-port connector: use identical provisional 8-pin map in connector.md, ESD, ground return, cable/connector ratings.
8. Light-unit driver: constant-current LED stage, MCU-controlled dim/enable, local switch, NTC, five status LEDs with simple nonprogrammable shift register.
9. PCB: ERC, DRC, trace current calculations, copper and heat sinking, separation of noisy switch nodes and analog sense, thermal test.
10. Safety: validate battery overcharge/undervoltage, temperature inhibit, hard shorts, reverse connection, contact failure, and simultaneous overload.

Do not reuse a 4.2 V Li-ion protector for 3.65 V-class LiFePO4 charging without checking actual thresholds. Avoid claiming that a component name alone makes a safe charging or protection design.

## Required outputs for next stage
- KiCad schematic with fully specified component values and actual net connections.
- Datasheet-linked BOM and worst-case power/thermal calculations.
- Firmware target, pin assignment, state-machine tests and fault mapping.
- PCB and Gerbers only after independent schematic review and bench validation.
