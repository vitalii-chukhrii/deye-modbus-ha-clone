"""Supported Deye inverter models and their bundled register maps.

Each entry maps a model key (stored in the config entry) to the YAML register
map that ships inside ``maps/`` and to device metadata shown in Home Assistant.

Adding a new inverter is a matter of dropping a new ``maps/<file>.yaml`` and
registering it here - no code changes required.
"""
from __future__ import annotations
from typing import Final

# Three-phase low-voltage hybrid protocol (device type 0x0500).
# The SUN-*K-SG04LP3 / SG05LP3 families share the same Modbus register map.
_THREE_PHASE_MAP: Final = "sun_3ph_hybrid.yaml"

MODELS: Final[dict[str, dict[str, str]]] = {
    "sun12k_sg05lp3": {
        "label": "Deye SUN-12K-SG05LP3 (3-phase hybrid)",
        "map": _THREE_PHASE_MAP,
        "manufacturer": "Deye",
        "model": "SUN-12K-SG05LP3",
    },
    "sun_sg05lp3_3ph": {
        "label": "Deye SUN-5/6/8/10/12K-SG05LP3 (3-phase hybrid)",
        "map": _THREE_PHASE_MAP,
        "manufacturer": "Deye",
        "model": "SUN-xxK-SG05LP3",
    },
    "sun_sg04lp3_3ph": {
        "label": "Deye SUN-5/6/8/10/12K-SG04LP3 (3-phase hybrid)",
        "map": _THREE_PHASE_MAP,
        "manufacturer": "Deye",
        "model": "SUN-xxK-SG04LP3",
    },
}

DEFAULT_MODEL: Final = "sun12k_sg05lp3"


def model_options() -> dict[str, str]:
    """Return {key: label} for the config-flow dropdown."""
    return {key: cfg["label"] for key, cfg in MODELS.items()}


def get_model(key: str | None) -> dict[str, str]:
    """Return the model config, falling back to the default model."""
    return MODELS.get(key or DEFAULT_MODEL, MODELS[DEFAULT_MODEL])
