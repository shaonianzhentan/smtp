"""Notify.Events platform for notify component."""
from __future__ import annotations

import logging

from homeassistant.components.notify import (
    ATTR_DATA,
    ATTR_TITLE,
    BaseNotificationService,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


def get_service(
    hass: HomeAssistant,
    config: ConfigType,
    discovery_info: DiscoveryInfoType | None = None,
) -> SmtpNotificationService:
    print(config)
    return SmtpNotificationService(hass)


class SmtpNotificationService(BaseNotificationService):

    def __init__(self, hass):
        self.hass = hass

    def send_message(self, message, **kwargs):
        """Send a message."""
        data = kwargs.get(ATTR_DATA) or {}
        title = kwargs.get(ATTR_TITLE, message)
        url = data.get('url')
        if url is not None:
            message = f'<a href="{url}">{message}</a>'

        qqmail = self.hass.data.get(DOMAIN)
        qqmail.send(title, message, qqmail.from_addr)