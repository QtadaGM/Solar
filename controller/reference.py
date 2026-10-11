"""Hardware-independent behavioral reference, NOT deployable MCU firmware."""
from dataclasses import dataclass
from enum import Enum

class Mode(Enum):
    AUTO = "auto"
    MANUAL = "manual"

@dataclass(frozen=True)
class PortInput:
    mode: Mode
    local_on: bool
    override_active: bool = False
    requested_watts: float = 15.0
    shorted: bool = False
    overcurrent: bool = False

@dataclass(frozen=True)
class PortOutput:
    enabled: bool
    allocated_watts: float
    fault: str | None

def schedule_fraction(hours_since_sunset: float) -> float:
    if hours_since_sunset < 0:
        return 0.0
    if hours_since_sunset < 2:
        return 1.0
    if hours_since_sunset < 10:
        return 0.5
    return 0.0

def distribute(master_on: bool, hours_since_sunset: float,
               ports: tuple[PortInput, PortInput],
               safe_budget_watts: float,
               battery_safe: bool = True) -> tuple[PortOutput, PortOutput]:
    """Equal proportional shedding; local port shorts trip independently.

    This is an abstract functional model, not a protection mechanism.
    """
    if safe_budget_watts < 0:
        raise ValueError("negative power budget")
    requests = []
    faults = []
    for port in ports:
        fault = "E14" if port.shorted or port.overcurrent else None
        faults.append(fault)
        if not master_on or not battery_safe or fault:
            requests.append(0.0)
            continue
        if port.mode is Mode.MANUAL or port.override_active:
            fraction = 1.0 if port.local_on else 0.0
        else:
            fraction = schedule_fraction(hours_since_sunset)
        requests.append(max(0.0, port.requested_watts) * fraction)
    total = sum(requests)
    scale = min(1.0, safe_budget_watts / total) if total else 1.0
    return tuple(
        PortOutput(enabled=(req * scale > 0), allocated_watts=req * scale,
                   fault=faults[i] if faults[i] else
                   ("E14" if req > 0 and scale < 1 else None))
        for i, req in enumerate(requests)
    )
