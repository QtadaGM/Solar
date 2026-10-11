"""Diagnostic encoding and fault prioritization reference.

A five-LED display has 32 instantaneous patterns. Display the base E01-E14
number as a 5-bit binary value, LSB at LED1. E14 subcodes are shown as a
separate alternating frame; the indicator requires a legend on the enclosure.
No claim is made that this constitutes a finished human-factors interface.
"""
from enum import IntEnum

class Fault(IntEnum):
    BATTERY_OVERCHARGE = 1
    BATTERY_LOW = 2
    BATTERY_OVERDISCHARGE = 3
    CHARGE_OVERCURRENT = 4
    DISCHARGE_OVERCURRENT = 5
    GENERAL_SHORT = 6
    BATTERY_HOT = 7
    CHARGE_TOO_COLD = 8
    LIGHT_HOT = 9
    SOLAR_OVERVOLTAGE = 10
    REVERSE_CURRENT = 11
    CHARGER_MALFUNCTION = 12
    MOISTURE = 13
    PORT_OVERLOAD = 14

E14_SUBCODES = {
    1: "JACK1_SHORT",
    2: "JACK2_SHORT",
    3: "COMBINED_OVERLOAD",
    4: "INSUFFICIENT_BATTERY_DISCHARGE",
    5: "JACK1_OVERCURRENT",
    6: "JACK2_OVERCURRENT",
    7: "OUTPUT_REGULATION_FAILURE",
}

def led_bits(code: int) -> tuple[bool, bool, bool, bool, bool]:
    if not 0 <= code <= 31:
        raise ValueError("five-LED code must be in 0..31")
    return tuple(bool(code & (1 << bit)) for bit in range(5))

def diagnostic_frames(fault: Fault, subcode: int | None = None):
    if subcode is not None and (fault != Fault.PORT_OVERLOAD or subcode not in E14_SUBCODES):
        raise ValueError("only E14 subcodes 1..7 are defined")
    base = led_bits(int(fault))
    return (base,) if subcode is None else (base, led_bits(subcode))

def visible_faults(global_faults, port_faults):
    """Return all distinct fault codes, most severe first.

    Priority is provisional; production firmware needs explicit safety states,
    latched-event policy, timestamping, and per-port display arbitration.
    """
    order = [Fault.BATTERY_OVERCHARGE, Fault.BATTERY_OVERDISCHARGE,
             Fault.GENERAL_SHORT, Fault.DISCHARGE_OVERCURRENT,
             Fault.CHARGE_OVERCURRENT, Fault.BATTERY_HOT,
             Fault.CHARGE_TOO_COLD, Fault.SOLAR_OVERVOLTAGE,
             Fault.REVERSE_CURRENT, Fault.CHARGER_MALFUNCTION,
             Fault.LIGHT_HOT, Fault.PORT_OVERLOAD,
             Fault.MOISTURE, Fault.BATTERY_LOW]
    present = set(global_faults) | set(port_faults)
    return tuple(f for f in order if f in present)
