"""Constants for the Deye Modbus integration."""
from __future__ import annotations
from typing import Final

DOMAIN: Final = "deye_modbus"

# --- Config / options keys ---
CONF_HOST: Final = "host"
CONF_PORT: Final = "port"
CONF_UNIT_ID: Final = "unit_id"
CONF_SCAN_INTERVAL: Final = "scan_interval"
CONF_MODEL: Final = "model"
CONF_TRANSPORT: Final = "transport"
CONF_BAUDRATE: Final = "baudrate"
CONF_BYTESIZE: Final = "bytesize"
CONF_PARITY: Final = "parity"
CONF_STOPBITS: Final = "stopbits"
CONF_ADDR_OFFSET: Final = "address_offset"

# --- Defaults ---
# Deye WiFi/LAN loggers expose Modbus TCP on 8899 by default. Third-party
# RS485<->TCP gateways (Elfin EW11, USR, ...) usually use 502.
DEFAULT_PORT: Final = 8899
DEFAULT_UNIT_ID: Final = 1
DEFAULT_SCAN_SECONDS: Final = 15
MIN_SCAN_SECONDS: Final = 5
MAX_SCAN_SECONDS: Final = 300
DEFAULT_TRANSPORT: Final = "tcp"
DEFAULT_ADDR_OFFSET: Final = 0

# Serial params (only used when transport == "rtutcp")
DEFAULT_BAUDRATE: Final = 9600
DEFAULT_BYTESIZE: Final = 8
DEFAULT_PARITY: Final = "N"
DEFAULT_STOPBITS: Final = 1
