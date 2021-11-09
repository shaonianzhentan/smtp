from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
import homeassistant.helpers.config_validation as cv

from .const import DOMAIN, PLATFORMS

CONFIG_SCHEMA = cv.deprecated(DOMAIN)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    print('安装', entry)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    print('更新', entry)
    return True