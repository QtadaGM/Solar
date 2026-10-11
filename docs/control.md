# Control behavior and scheduling

SW0 is a hardware master shutdown/isolation request, not a substitute for battery protection.

SW1 and SW2 independently select **AUTO** or **MANUAL** for their respective sockets.

| Master | Port mode | Local request | Expected behavior |
|---|---|---|---|
| OFF | any | any | Both ports, charging, MCU, diagnostics OFF |
| ON | MANUAL | OFF | Port's main LEDs OFF, auxiliary/status available |
| ON | MANUAL | ON | Port's LEDs ON subject to safe power budget |
| ON | AUTO | no override | Sunset schedule applies |
| ON | AUTO | local override | Local ON/OFF overrides schedule until defined reset |
| ON | any | fault/unsafe | Hardware safety and power limits take precedence |

## Schedule per port
- Detect sunset from panel input with filtering/hysteresis; avoid cloud-induced false sunset.
- First 2 hours: 100% target (~2000 lm).
- Following 8 hours: 50% target (~1000 lm).
- Thereafter: OFF.
- Light outputs have identical default schedules, but control/overrides and protection are independent.

## Power allocation
If simultaneous requests exceed safe source or converter capacity, reduce both requested light levels proportionally when possible. A local short must disconnect **only** the affected port; never attempt to dim through a hard short. If safe operation cannot be restored, disable outputs with a defined recovery policy.

## Firmware acceptance tests
- Both sockets identical under role reversal.
- AUTO off allows local ON and OFF.
- AUTO on allows override of scheduled ON and OFF.
- Light status remains powered while LED output is scheduled OFF.
- SW0 OFF cannot be bypassed by solar power.
- A short on JACK 2 does not kill safe JACK 1 operation.
- Battery undervoltage is E02/E03; port overload is E14.
- No floating switch inputs; debounce and startup state deterministic.
