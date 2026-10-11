# Prototype verification checklist

**Bench work must be performed by a qualified engineer with current-limited supplies and appropriate battery precautions.**

- [ ] Panel Vmp/Voc/Isc/Imp measured or datasheet confirmed.
- [ ] Cell datasheet, holder, fuse and BMS thresholds verified for LiFePO4.
- [ ] Both bank inputs separately protected; hot insertion/equalization tested.
- [ ] Master OFF blocks solar charging and all active power paths.
- [ ] Both light jacks verified identical pinout, supply rating and controls.
- [ ] Port short hardware trip verified independently on each jack.
- [ ] One shorted jack does not disable safe operation of the other.
- [ ] Manual local control works with AUTO disabled.
- [ ] AUTO override works in both directions.
- [ ] Sunset detection resists cloud/shadow transients.
- [ ] 2h + 8h schedule validated against real-time clock/timer.
- [ ] Five remote diagnostic LEDs verified on both light units.
- [ ] All E01–E14 triggers linked to actual measurable signals.
- [ ] Battery low warning and hard cutoff tested.
- [ ] Dual-output equal load shedding tested.
- [ ] Worst-case DC/DC, connector and battery temperatures measured.
- [ ] ERC and DRC clean; independent schematic safety review complete.
- [ ] Manufacturing package reviewed and versioned.
