"""Shared DeviceInfo builder so all platforms attach to one device."""
from __future__ import annotations

from homeassistant.const import CONF_HOST
from homeassistant.helpers.entity import DeviceInfo

from .const import DOMAIN, CONF_MODEL
from .models import get_model


def build_device_info(entry) -> DeviceInfo:
    host = entry.data.get(CONF_HOST)
    model = get_model(entry.data.get(CONF_MODEL))
    return DeviceInfo(
        identifiers={(DOMAIN, entry.entry_id)},
        name=f"Deye {model['model']}",
        manufacturer=model["manufacturer"],
        model=model["model"],
        configuration_url=(f"http://{host}" if host else None),
    )
