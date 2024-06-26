from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers import discovery
from homeassistant.const import Platform

from .manifest import manifest

DOMAIN = manifest.domain

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    await discovery.async_load_platform(
        hass,
        Platform.NOTIFY,
        DOMAIN,
        {'name': entry.title, 'entry_id': entry.entry_id, **entry.data},
        {},
    )
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    return True