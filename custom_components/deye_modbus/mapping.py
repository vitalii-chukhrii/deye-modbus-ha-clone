"""Load a Deye register map (YAML) for a given inverter model."""
from __future__ import annotations
import os
import logging
from typing import Any

import yaml

from .models import get_model

_LOGGER = logging.getLogger(__name__)


def maps_dir() -> str:
    return os.path.join(os.path.dirname(__file__), "maps")


def resolve_map_path(model_key: str | None) -> str:
    """Return the absolute path to the bundled YAML map for a model."""
    model = get_model(model_key)
    return os.path.join(maps_dir(), model["map"])


def load_register_mapping(model_key: str | None) -> dict[str, Any]:
    """Load and parse the register map for the selected inverter model."""
    path = resolve_map_path(model_key)
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        sensors = data.get("sensors", []) or []
        controls = data.get("controls", []) or []
        _LOGGER.info(
            "Deye map loaded from %s: %s sensors, %s controls",
            path, len(sensors), len(controls),
        )
        return {"sensors": sensors, "controls": controls, "path": path}
    except Exception as err:  # noqa: BLE001 - never break setup on a bad map
        _LOGGER.error("Failed to read Deye map from %s: %s", path, err)
        return {"sensors": [], "controls": [], "path": path}
