# Identical light-unit connector — provisional 8-pin allocation

**NOT a finalized connector footprint or wiring harness.** Both sockets must be identical.

| Pin | Signal | Direction | Purpose |
|---|---|---|---|
| 1 | VOUT_PROTECTED | PCB -> light | Regulated power; voltage TBD |
| 2 | GND | common | Power and signal return |
| 3 | LED_DIM | PCB -> light | PWM/analog driver command |
| 4 | LOCAL_SWITCH | light -> PCB | Debounced local switch state/event |
| 5 | DIAG_DATA | PCB -> light | Shift-register serial data |
| 6 | DIAG_CLOCK | PCB -> light | Shift-register clock |
| 7 | DIAG_LATCH | PCB -> light | Shift-register latch |
| 8 | TEMP_SENSE | light -> PCB | Remote LED-board NTC measurement |

Each light unit can use a low-cost **non-programmable** shift register (for example a suitable 8-bit serial-in/parallel-out IC) to drive its five diagnostic indicators through resistors. All encoding and sequencing happen on the main MCU. Confirm logic-voltage compatibility, reset state, and indicator current budget.

A maintained local switch can be interpreted as ON/OFF; a momentary button can be interpreted as toggle. Select and document **one** mechanical behavior before firmware release. In AUTO, local control must be able to override both ON and OFF schedule commands; define explicit resynchronization at the next schedule transition.

LED driver enable/dimming must be separated from protected port supply, so local requests can be sensed when LEDs are OFF. Each port requires independent hardware current limiting and fault feedback.

If connector insertion/removal under power is allowed, specify pin sequencing, inrush limiting, ESD protection and connector ratings.
