# System architecture

```text
30W solar panel
   | surge/reverse protection + solar sensing
   v
LiFePO4 switching solar charger ---- charge safety/temperature inhibit
   |
   +---- Bank A: 1S7P removable LiFePO4, independent protection
   |
   +---- Bank B: optional 1S7P, independent protection
            (controlled power-path coupling; never hard hot-parallel)
   |
SW0 complete-system power isolation (both battery and solar-derived paths)
   |
Protected DC/DC supply + energy/power monitor
   |
   +---- hardware eFuse/current limit #1 ---- JACK 1 (power + signals)
   |
   +---- hardware eFuse/current limit #2 ---- JACK 2 (power + signals)
   |
Central low-power MCU
   +-- SW1 AUTO 1 / SW2 AUTO 2
   +-- solar sensing / sunset detection
   +-- independent light-unit switch inputs
   +-- independent light enable/dimming outputs
   +-- port-current/voltage/temp inputs
   +-- status encoding for each port
```

Both ports have identical circuit topology, pinout, current ratings, control functions, and protection. Neither is designated primary. Missing accessories are normal status, not faults.

The LED module may include analog driver/shift-register electronics but **no processor or independent firmware**. A protected always-available auxiliary rail (when SW0 ON) must allow local override requests and status display even if the main LED is scheduled OFF.

Safety-critical overcurrent, overvoltage, and battery protection must function without MCU execution.

**SW0 OFF:** intended to disable charging, controller, indicators and both outputs; power-path isolation implementation must be verified for both solar and battery feeds. Passive cell-protection elements may remain physically connected to cells.

## Engineering questions
- Actual panel Vmp/Voc and operating temperature.
- Cell manufacturer, current rating, dimensions, holder contact resistance, and individual-cell fuse strategy.
- Output bus voltage and constant-current LED driver design (12 V is provisional).
- Physical connector, cable length, ingress/ESD requirements.
- Reliable thermal sensor and optional moisture-sensor placement.
- Bank B controlled coupling and independent fault isolation topology.
