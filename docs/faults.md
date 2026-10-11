# Fault taxonomy

All codes are generated on the main PCB. Each connected light displays system-wide faults and its own port-specific faults using five LEDs. Proposed binary 5-bit display encoding (0–31) must be validated for user readability; alternate blink sequences may be used. Multiple simultaneous faults require priority/rotation rules.

| Code | Meaning |
|---|---|
| E01 | Battery overcharge |
| E02 | Low battery warning |
| E03 | Battery overdischarge |
| E04 | Charging overcurrent |
| E05 | Battery discharge overcurrent |
| E06 | General short circuit outside per-port branches |
| E07 | Battery overheating |
| E08 | Battery too cold for charging |
| E09 | Light-unit overheating |
| E10 | Solar input overvoltage |
| E11 | Reverse-current protection fault |
| E12 | Charging circuit malfunction |
| E13 | Moisture/electrical ingress fault (requires actual sensor) |
| E14 | Light-output short, overcurrent, or combined power overload |

## E14 details
- E14.1: JACK 1 short.
- E14.2: JACK 2 short.
- E14.3: combined output over rated capacity.
- E14.4: requested load exceeds battery's safe discharge capability.
- E14.5: JACK 1 overcurrent.
- E14.6: JACK 2 overcurrent.
- E14.7: output regulation failure.

A single installed bank or an unplugged light is **not** an error. Battery energy depletion is E02/E03, not E14.

Do not claim to detect E11, E12, E13, etc. without the necessary instrumentation and a defined detection algorithm. Fast faults require hardware cutoff independent of MCU.
