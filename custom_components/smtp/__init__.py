from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
import homeassistant.helpers.config_validation as cv

from .const import DOMAIN, PLATFORMS

from .qqmail import QQMail
unique_id = DOMAIN + '-qqmail'

CONFIG_SCHEMA = cv.deprecated(DOMAIN)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    cfg = entry.data
    hass.data[unique_id] = QQMail(hass, cfg['qq'], cfg['code'])
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    cfg = entry.data
    hass.data[unique_id] = QQMail(hass, cfg['qq'], cfg['code'])
    return True